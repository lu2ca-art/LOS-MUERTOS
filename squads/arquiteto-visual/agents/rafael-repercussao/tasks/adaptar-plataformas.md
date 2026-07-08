---
task: "Adaptar Plataformas"
order: 1
input: |
  - conteudo_instagram: Caption e script aprovados de Carlos Caption
  - plataformas_solicitadas: Lista de plataformas pedidas na sessão (Twitter/X, YouTube Script, YouTube Shorts, Blog Post, Email Newsletter)
output: |
  - adaptacoes: Conteúdo nativo por plataforma solicitada
  - status_publicacao: URLs dos posts publicados (quando autorizado) ou pendente de aprovação
---

# Adaptar Plataformas

Rafael Repercussão recebe o conteúdo aprovado de Carlos Caption e produz versões nativas para cada plataforma solicitada. Nunca copia e cola — cada adaptação é construída para a convenção da plataforma de destino. A voz de LU2CA não muda; o tamanho, o ritmo e a intimidade mudam.

## Process

1. **Ler conteúdo aprovado:** Carregar `squads/arquiteto-visual/output/conteudo-instagram.md`. Identificar o tom confirmado e o vocabulário ativo. Este é o núcleo — as adaptações partem da mesma ideia, nunca do mesmo texto.

2. **Adaptar por plataforma solicitada** (apenas as plataformas pedidas na sessão):

   **Twitter/X (≤280 chars):**
   Destilar para a essência em 280 chars. 1-2 frases máximo. Vocabulário de LU2CA preservado. Nenhum hashtag sem solicitação explícita. Mencionar lu2ca.art quando couber.

   **YouTube Script (3-5 min):**
   Abertura que retém em 15s (sem "ei pessoal"). Desenvolvimento da filosofia central em 3-5 blocos de fala. Closing com CTA específico para lu2ca.art. Indicar [pausa], [corte], [B-roll] conforme necessário.

   **YouTube Shorts (15-60s):**
   Hook nos primeiros 3s. Entrega em 1 ideia central. Loop design: final conecta ao início para replay. CTA visual em tela no último segundo.

   **Blog Post (400-600 palavras):**
   H1 = título adaptado (não a caption). Abertura que contextualiza sem repetir o post. Corpo desenvolve o ângulo em 3-4 parágrafos. Menção a lu2ca.art com contexto do ecossistema gamificado. Fechamento com convite à tripulação.

   **Email Newsletter (200-400 palavras):**
   Assunto em ≤50 chars — deve abrir. Saudação: "viajante," (minúsculo, vírgula). Tom = carta íntima. Corpo desenvolve 1 ideia da sessão com contexto pessoal. CTA único para lu2ca.art. Assinatura inegociável: "com amor, LU2CA".

3. **Checkpoint de publicação:** NUNCA publicar sem aprovação explícita. Após entregar as adaptações, perguntar ao usuário quais deseja publicar e quando. Apenas após confirmação executar o skill `blotato`.

4. **Publicar via blotato (quando autorizado):** Para cada plataforma autorizada: dry-run → preview → confirmação → publish → reportar URL. Sem URL confirmada = publicação não confirmada.

5. **Registrar status:** Atualizar `output/adaptacoes.md` com conteúdo de cada plataforma e status (rascunho / agendado / publicado + URL).

## Output Format

```
=== ADAPTAÇÕES ===

--- TWITTER/X ---
[texto ≤280 chars]
Chars: [contagem]

--- YOUTUBE SCRIPT ---
[script 3-5 min com indicações de cena]

--- BLOG POST ---
# [título]
[400-600 palavras]

--- EMAIL NEWSLETTER ---
Assunto: [≤50 chars]

viajante,

[corpo 200-400 palavras]

com amor, LU2CA

=== STATUS DE PUBLICAÇÃO ===
[plataforma]: [rascunho / agendado [data] / publicado — URL]
```

## Output Example

```
=== ADAPTAÇÕES ===

--- TWITTER/X ---
posso não saber tudo, só não posso ficar parado.
mexe o corpitcho, viajante — lu2ca.art 🛹
Chars: 84

--- EMAIL NEWSLETTER ---
Assunto: segunda não vence o corpitcho

viajante,

tem semanas que a gravidade parece maior. não é fraqueza — é física.
mas o corpitcho sabe o que fazer antes da cabeça decidir.

um movimento pequeno muda a trajetória. sempre.
a tripulação sabe disso. é por isso que a gente continua avançando no mapa.

a próxima faixa tá esperando você em lu2ca.art

com amor, LU2CA

=== STATUS DE PUBLICAÇÃO ===
Twitter/X: rascunho — aguardando aprovação
Email Newsletter: rascunho — aguardando aprovação
```

## Quality Criteria

- [ ] Cada adaptação respeitou os limites técnicos (280 chars Twitter, 400-600 palavras Blog, 200-400 palavras Newsletter)
- [ ] lu2ca.art mencionado em todas as adaptações
- [ ] Newsletter tem saudação "viajante," e assinatura "com amor, LU2CA"
- [ ] Nenhuma adaptação é cópia do texto do Instagram
- [ ] Nenhuma publicação sem checkpoint de aprovação anterior
- [ ] URL reportada após toda publicação bem-sucedida

## Veto Conditions

Rejeitar e refazer se qualquer um for verdadeiro:
1. Newsletter sem "com amor, LU2CA" — assinatura inegociável, derivada do padrão estabelecido
2. Qualquer publicação executada sem aprovação explícita do usuário — publicação é irreversível
