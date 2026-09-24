# Biblioteca de Mídia Real — Vila Los Muertos de Fome

Fonte real de material bruto para o Vini Vídeo (e assets visuais para o Vito Visual).
**Pasta compartilhada no iCloud do usuário — somente leitura.** Nunca mover, renomear ou
apagar nada aqui; qualquer output vai para `squads/gestor-vila/output/`, nunca para dentro
desta pasta. (Uma reorganização de nomes foi cogitada em 24/09/2026 e adiada — o usuário
optou por só documentar por enquanto, ver "Nomes que enganam" abaixo.)

## Caminho base

```
/Users/lu2ca/Library/Mobile Documents/com~apple~CloudDocs/LOS MUERTOS MIDIA/
```

**Atenção de encoding:** dentro da raiz, a subpasta de vídeo bruto se chama literalmente
`" mídia"` — com um espaço no início. Ao acessar via script/shell, resolva o nome exato com
`os.listdir()` (Python) em vez de digitar o caminho à mão — o acento em "í" pode estar em
forma decomposta (NFD) e não bater com o que parece igual visualmente.

**Atenção HEIC:** arquivos `.heic`/`.HEIC` (várias pastas de fotos abaixo) **não decodificam
certo com `ffmpeg`** nessa máquina — ele retorna o mapa de profundidade do Portrait Mode
(imagem cinza/preta sem sentido) em vez da foto real. Use `sips -s format jpeg origem.heic
--out destino.jpg` (nativo do macOS) para converter antes de qualquer preview ou uso.

---

## Estrutura da raiz (`LOS MUERTOS MIDIA/`)

| Item | Conteúdo | Uso |
|------|----------|-----|
| ` mídia/` | Vídeo/foto bruto por tema — ver tabela principal abaixo | Fonte pro Vini/Vito |
| `docs/` | `Calendario_Social_Media_Vila_Setembro_2026.xlsx` (calendário oficial do mês, com coluna Status — nunca atualizada além de "Planejado"), contratos, cupom | Referência de planejamento |
| `mascotes/` | Logo e mascotes oficiais — ver seção própria abaixo, tem uma pegadinha de transparência | Vito Visual |
| `mexicano fotos novas/` | 29 fotos `.heic`, still-life de prato (taco/quesadilla/burrito) — **não confundir com `mídia/mexicano/`**, que é vídeo de outra coisa | Fotos de cardápio prontas pra uso |
| `ref kit de marca/` | Imagens/vídeos de referência visual (moodboard), não é material pra editar — é inspiração de estilo | Consulta, não fonte de clipe |
| `midia nova ` *(nota o espaço no fim)* | Vazia (subpastas sem nenhum arquivo) | — |
| `Novo Cardapio 2026.pdf` | Cardápio oficial, solto na raiz | Fonte de preços/pratos |

### `mascotes/` em detalhe

| Subpasta | Conteúdo | Usável direto? |
|----------|----------|----------------|
| `logos los muertos/` (4 PNGs) | Logo completo, wordmark, mascotes isolados | ⚠️ Fundo azul opaco — **não** é o mesmo bug de transparência, mas também não tem versão limpa cortada |
| `logos transparente/` (4 PNGs) | Mesma coisa, "transparente" no nome | 🔴 **Bug confirmado:** alpha uniforme de ~56% (143/255) no canvas inteiro, incluindo o texto — não é um recorte limpo, é uma exportação com opacidade parcial acidental. Composição direta fica lavada/pastel. Dá pra corrigir via `alphaextract`+`lutyuv=y=255`+`alphamerge` (ver `render_branded.py`), mas é gambiarra técnica, não o ideal. |
| `4.png`, `5.png` (soltos, raiz de `mascotes/`) | Variantes menores | Não testado |

**Os assets que realmente funcionam sem gambiarra** são os que o usuário reenviou direto na conversa em 22/09/2026 (alpha binário limpo, sem bug) — já persistidos em `squads/gestor-vila/pipeline/data/brand-assets/` (`logo-wordmark.png`, `mascote-gato.png`, `mascote-cachorro.png`). **Preferir sempre esses** em vez de extrair de `mascotes/` de novo.

---

## Pastas por tema (dentro de `mídia/`)

| Pasta | Arquivos | Tamanho | O que **realmente** tem (verificado, não só o nome) |
|-------|----------|---------|------------------------------------------------------|
| `rodizio video/` | 7 | 19 MB | ⚠️ **Não é rodízio sendo servido** — é still-life de pratos variados (petisco, sliders, tacos, tostadas, enchilada, churros) em fundo preto texturizado. Ótimo pra reel de "giro pelo cardápio", péssimo se a pauta pedir rodízio de verdade acontecendo. |
| `almoço/` | 90 | 1.4 GB | Também still-life de prato (não gente comendo) — pratos do dia, PF, saladas. Mesma natureza de `rodizio video/`, volume maior. |
| `porções/` | 3 | 82 MB | Still-life, porções pra compartilhar |
| `lanches e  burgers/` *(2 espaços no nome)* | 17 | 251 MB | Mistura: still-life de lanche/burger **e também** alguns planos de ambiente com rack-focus (ex: `copy_3E9128B9-...MOV`, usado como abertura do reel de terça — comida borrada em primeiro plano, decoração do salão ao fundo). Vale garimpar aqui quando precisar de "ambiente" sem gente/show. |
| ` drinks/` *(espaço no início)* | 169 | 3.1 GB | Não verificado a fundo — nome parece confiável (drinks, happy hour) |
| `copa/` | 34 | 2.3 GB | Copa do Mundo — telão, torcida. Um frame de telão de basquete (não Copa) apareceu misturado em `música/`, então pode haver overlap de contexto "telão" entre as duas pastas |
| `música/` | 71 | 2.3 GB | 🔴 **100% show/evento ao vivo** — banda, samba, karaokê, crowd, telão. **Não existe nenhum plano neutro/vazio aqui.** Se a pauta não for sobre entretenimento, essa pasta vai te dar o clipe errado (aconteceu: reel de rodízio terça/quarta ganhou por engano um clipe de noite de samba). Pra "ambiente" sem show, usar `lanches e burgers/` ou `mexicano fotos novas/` (foto, não vídeo). |
| `mexicano/` | 22 | 320 MB | Vídeo, identidade cultural Tex-Mex — **não confundir com `mexicano fotos novas/`** (foto, na raiz, fora de `mídia/`) |
| `dancinhaholic/` | 14 | 511 MB | Engajamento/trend casual — não verificado nesta sessão |
| `edits/` | 32 | 409 MB | Clipes já cortados/prontos de sessões anteriores — checar antes de reeditar do zero |
| `Fotos/` | 147 | 360 MB | Sem legenda nenhuma nos nomes (`IMG_XXXX.HEIC` genérico). **Usar `sips`, não `ffmpeg`, pra converter** (ver aviso HEIC acima). Não triado ainda — abrir sob demanda quando precisar de algo específico, não vale a pena catalogar tudo de uma vez. |
| `pngs/` | 9 | 9.1 MB | Exports do Canva, assets de design |
| `agenda da semana jul/` | 7 | 12 MB | PNGs de um template de "arte fixa" de julho — pode servir de referência/reaproveitamento pra peça de sexta ("Agenda do Fim de Semana"), mas é conteúdo antigo |
| `detalhes/`, `feed semanal/`, `reels semanal/`, `story semanal/` | vazias | — | Pastas-destino nunca usadas — a ideia original era virar convenção de "selecionados para postar", mas ninguém populou. Cogitado ativar em 24/09/2026, usuário preferiu só documentar por enquanto — **não tratar como fonte de conteúdo pronto ainda, estão vazias mesmo.** |

---

## Nomes que enganam (resumo rápido)

- `rodizio video/` → still-life de prato, **não** rodízio sendo servido
- `almoço/` → também still-life, não gente almoçando
- `música/` → só show/evento, zero plano neutro
- `mexicano/` (vídeo) ≠ `mexicano fotos novas/` (foto) — pastas diferentes, nomes quase iguais
- `logos transparente/` em `mascotes/` → não é limpo, tem alpha parcial de ~56% no canvas inteiro

## Como usar

1. Antes de montar um plano de edição, listar os arquivos da pasta temática relevante
   (`os.listdir` via Python, não `ls` com o caminho digitado à mão).
2. Escolher os clipes pelo nome/data de modificação — nomes como `IMG_0700.MOV` não indicam
   conteúdo, então **extrair um frame de preview antes de decidir** (nome/pasta não é
   confiável, ver "Nomes que enganam" acima). Confirmar com o usuário quando a dúvida persistir.
3. Vídeos filmados no iPhone têm metadado de rotação — o skill `video-editor` já corrige isso
   automaticamente (ver `skills/video-editor/scripts/edit.py`, função `detect_rotation`).
4. Fotos `.heic` — usar `sips`, nunca `ffmpeg` (retorna lixo, ver aviso acima).
5. Nunca escrever, mover ou apagar nada dentro desta biblioteca — é a pasta de origem
   compartilhada, não um scratch space.
