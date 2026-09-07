// Matching simples baseado em sobreposição de palavras entre a mensagem do
// cliente e as "perguntas típicas" catalogadas na biblioteca. Nada de
// embeddings/LLM aqui de propósito — é rápido, previsível e fácil de
// depurar quando alguém perguntar "por que respondeu isso".
// (Idêntico em lógica ao lib/match.js da versão Vercel — só em formato de
// módulo ES porque é o que o Cloudflare Workers espera.)

const STOPWORDS = new Set([
  "a", "o", "as", "os", "de", "da", "do", "das", "dos", "e", "ou", "que",
  "um", "uma", "uns", "umas", "eu", "voce", "voces", "vc", "vcs", "pra",
  "para", "com", "sem", "no", "na", "nos", "nas", "se", "por", "mais",
  "tem", "ter", "vou", "esta", "tá", "ta", "aqui", "ai", "la", "e", "é",
  "sao", "são", "aquele", "aquela", "isso", "esse", "essa",
]);

export function normalize(s) {
  return (s || "")
    .toLowerCase()
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "") // remove acentos
    .replace(/[^a-z0-9\s]/g, " ") // pontuação vira espaço — nunca gruda em palavra
    .replace(/\s+/g, " ")
    .trim();
}

export function tokens(s) {
  return normalize(s)
    .split(" ")
    .filter((w) => w.length > 1 && !STOPWORDS.has(w));
}

// Pontua o quanto a mensagem do cliente "bate" com uma frase catalogada.
// 1.0 = contém a frase inteira (ou vice-versa). Caso contrário, proporção
// de palavras-chave em comum sobre o total de palavras da frase catalogada.
function scorePhrase(userTokensSet, userNorm, phrase) {
  const phraseNorm = normalize(phrase);
  if (!phraseNorm) return 0;
  if (userNorm.includes(phraseNorm) || phraseNorm.includes(userNorm)) return 1;

  const phraseTokens = tokens(phrase);
  if (!phraseTokens.length) return 0;
  const shared = phraseTokens.filter((t) => userTokensSet.has(t));
  return shared.length / phraseTokens.length;
}

export const THRESHOLD = 0.55;

// Algumas categorias usam "Situação típica" (descrição abstrata pra quem
// mantém a biblioteca) em vez de frases reais de cliente — o que enfraquece
// o matching justamente nas categorias mais sensíveis (Reclamação) ou mais
// comuns em DM real (institucional B-E). Esses sinônimos só existem aqui,
// na camada de automação — não mudam o texto oficial da biblioteca.
const SINONIMOS = {
  "reclamacao": [
    "demorou muito", "demora", "atendimento ruim", "comida fria",
    "veio errado", "pessimo", "horrivel", "nao gostei", "reclamar",
    "reclamação", "cobraram errado", "cobrança errada", "experiência ruim",
    "muito ruim", "decepcionado", "decepcionada",
  ],
  "elogio": [
    "adorei", "amei", "muito bom", "top demais", "parabéns", "sensacional",
    "maravilhoso", "incrível", "melhor lugar",
  ],
  "artista-querendo-tocar-na-vila": [
    "sou artista", "sou banda", "quero tocar aí", "meu som", "minha banda",
    "toco música", "sou músico", "book de shows",
  ],
  "parceria-patrocinio-imprensa-ou-proposta-de-empresa": [
    "parceria", "patrocínio", "sou jornalista", "matéria", "divulgação",
    "permuta", "sou influenciador", "proposta comercial",
  ],
  "fornecedor-distribuidora-oferecendo-produto": [
    "sou fornecedor", "represento uma distribuidora", "vendo pra restaurante",
    "tenho um produto",
  ],
  "vaga-de-emprego-curriculo-colaborador": [
    "vaga de emprego", "tem vaga", "mando meu currículo", "quero trabalhar aí",
    "procurando emprego",
  ],
};

export function matchIntent(userText, categorias) {
  const userNorm = normalize(userText);
  const userTokensSet = new Set(tokens(userText));

  let best = null;
  let bestScore = 0;

  for (const cat of categorias) {
    if (cat.isForaEscopo) continue; // nunca é alvo de match, só fallback
    const frases = [...cat.perguntas, cat.titulo, ...(SINONIMOS[cat.id] || [])];
    for (const frase of frases) {
      const s = scorePhrase(userTokensSet, userNorm, frase);
      if (s > bestScore) {
        bestScore = s;
        best = cat;
      }
    }
  }

  if (!best || bestScore < THRESHOLD) {
    return { categoria: null, score: bestScore, isFallback: true };
  }
  return { categoria: best, score: bestScore, isFallback: false };
}
