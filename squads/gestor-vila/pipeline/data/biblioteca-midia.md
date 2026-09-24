# Biblioteca de Mídia Real — Vila Los Muertos de Fome

Fonte real de material bruto para o Vini Vídeo (e assets visuais para o Vito Visual).
**Pasta compartilhada no iCloud do usuário.** Qualquer output vai para
`squads/gestor-vila/output/`, nunca para dentro desta pasta.

**Atualização de política (24/09/2026):** as pastas cujo nome batia errado com o conteúdo
foram **renomeadas** (não mais "documentar e não mexer" — ver "Renomeações feitas" abaixo).
Reorganização de arquivo-por-arquivo dentro das pastas continua **não feita** — risco de
escala (700+ arquivos) e julgamento em conteúdo ambíguo é alto demais pra fazer sem checkpoint
com o usuário. Ver a decisão completa na conversa de 24/09 — resumo: renomear pasta inteira é
baixo risco (uma operação), re-triar arquivo por arquivo é alto risco (centenas de decisões
sem supervisão) e fica pra quando surgir necessidade pontual, não em lote.

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

## Renomeações feitas em 24/09/2026

| Nome antigo | Nome novo | Motivo |
|---|---|---|
| `mídia/rodizio video/` | `mídia/still-life-pratos/` | Não era rodízio sendo servido, era still-life de prato |
| `mídia/música/` | `mídia/shows-e-eventos/` | Era 100% show/evento, nome "música" sugeria algo mais neutro |
| `mexicano fotos novas/` (raiz) | `cardapio-fotos-still-life/` (raiz) | Disambiguar do vídeo `mídia/mexicano/`, que é outra coisa |
| `mídia/mexicano/` | `mídia/identidade-cultural-mexicana/` | Mesmo motivo, do outro lado da confusão |

Toda referência a essas pastas em `edit-plan.json`/scripts já usava os caminhos antigos —
**atualizadas junto com a renomeação** (ver `output/reel-produto-22-09/edit-plan.json`,
que continua reproduzindo o mesmo resultado depois da mudança).

---

## Estrutura da raiz (`LOS MUERTOS MIDIA/`)

| Item | Conteúdo | Uso |
|------|----------|-----|
| ` mídia/` | Vídeo/foto bruto por tema — ver tabela principal abaixo | Fonte pro Vini/Vito |
| `docs/` | `Calendario_Social_Media_Vila_Setembro_2026.xlsx` (calendário oficial do mês, com coluna Status — nunca atualizada além de "Planejado"), contratos, cupom | Referência de planejamento |
| `mascotes/` | Logo e mascotes oficiais — ver seção própria abaixo, tem uma pegadinha de transparência | Vito Visual |
| `cardapio-fotos-still-life/` *(ex-`mexicano fotos novas/`)* | 29 fotos `.heic`, still-life de prato (taco/quesadilla/burrito) — **não confundir com `mídia/identidade-cultural-mexicana/`**, que é vídeo de outra coisa | Fotos de cardápio prontas pra uso |
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
| `still-life-pratos/` *(ex-`rodizio video/`)* | 7 | 19 MB | Still-life de pratos variados (petisco, sliders, tacos, tostadas, enchilada, churros) em fundo preto texturizado. Ótimo pra reel de "giro pelo cardápio", não serve se a pauta pedir rodízio de verdade acontecendo. |
| `almoço/` | 90 | 1.4 GB | Também still-life de prato (não gente comendo) — pratos do dia, PF, saladas. Mesma natureza de `still-life-pratos/`, volume maior. Nome mantido (ainda descreve bem o horário/contexto, só não é "gente almoçando"). |
| `porções/` | 3 | 82 MB | Still-life, porções pra compartilhar |
| `lanches e  burgers/` *(2 espaços no nome)* | 17 | 251 MB | Mistura: still-life de lanche/burger **e também** alguns planos de ambiente com rack-focus (ex: `copy_3E9128B9-...MOV`, usado como abertura do reel de terça — comida borrada em primeiro plano, decoração do salão ao fundo). Vale garimpar aqui quando precisar de "ambiente" sem gente/show. |
| ` drinks/` *(espaço no início)* | 169 | 3.1 GB | Não verificado a fundo — nome parece confiável (drinks, happy hour) |
| `copa/` | 34 | 2.3 GB | Copa do Mundo — telão, torcida. Um frame de telão de basquete (não Copa) apareceu misturado em `shows-e-eventos/`, então pode haver overlap de contexto "telão" entre as duas pastas |
| `shows-e-eventos/` *(ex-`música/`)* | 71 | 2.3 GB | 🔴 **100% show/evento ao vivo** — banda, samba, karaokê, crowd, telão. **Não existe nenhum plano neutro/vazio aqui.** Se a pauta não for sobre entretenimento, essa pasta vai te dar o clipe errado (aconteceu: reel de rodízio terça/quarta ganhou por engano um clipe de noite de samba). Pra "ambiente" sem show, usar `lanches e burgers/` ou `cardapio-fotos-still-life/` (foto, não vídeo). |
| `identidade-cultural-mexicana/` *(ex-`mexicano/`)* | 22 | 320 MB | Vídeo, identidade cultural Tex-Mex — **não confundir com `cardapio-fotos-still-life/`** (foto, na raiz, fora de `mídia/`) |
| `dancinhaholic/` | 14 | 511 MB | Engajamento/trend casual — não verificado nesta sessão |
| `edits/` | 32 | 409 MB | Clipes já cortados/prontos de sessões anteriores — checar antes de reeditar do zero |
| `Fotos/` | 147 | 360 MB | Sem legenda nenhuma nos nomes (`IMG_XXXX.HEIC` genérico). **Usar `sips`, não `ffmpeg`, pra converter** (ver aviso HEIC acima). Não triado ainda — abrir sob demanda quando precisar de algo específico, triagem em lote fica pra quando fizer sentido, não hoje. |
| `pngs/` | 9 | 9.1 MB | Exports do Canva, assets de design |
| `agenda da semana jul/` | 7 | 12 MB | PNGs de um template de "arte fixa" de julho — pode servir de referência/reaproveitamento pra peça de sexta ("Agenda do Fim de Semana"), mas é conteúdo antigo |
| `detalhes/`, `feed semanal/`, `reels semanal/`, `story semanal/` | vazias | — | Pastas-destino nunca usadas — a ideia original era virar convenção de "selecionados para postar". Ainda não ativadas — ficam pra quando tivermos um fluxo de "arquivo final aprovado entra aqui" combinado com o usuário, não é prioridade agora. |

---

## Nomes que ainda merecem atenção (não renomeados, mas verificar antes de usar)

- `almoço/` → still-life de prato, não gente almoçando (nome mantido por já comunicar o contexto/horário certo)
- `dancinhaholic/`, ` drinks/` → conteúdo não verificado nesta sessão, confirmar com um frame antes de usar

## Como usar

1. Antes de montar um plano de edição, listar os arquivos da pasta temática relevante
   (`os.listdir` via Python, não `ls` com o caminho digitado à mão).
2. Escolher os clipes pelo nome/data de modificação — nomes como `IMG_0700.MOV` não indicam
   conteúdo, então **extrair um frame de preview antes de decidir**. Confirmar com o usuário
   quando a dúvida persistir.
3. Vídeos filmados no iPhone têm metadado de rotação — o skill `video-editor` já corrige isso
   automaticamente (ver `skills/video-editor/scripts/edit.py`, função `detect_rotation`).
4. Fotos `.heic` — usar `sips`, nunca `ffmpeg` (retorna lixo, ver aviso acima).
5. Renomear pasta inteira é uma operação de baixo risco (feito quando o nome engana);
   reorganizar arquivo-por-arquivo dentro de uma pasta não é — fazer só sob demanda pontual,
   nunca em lote sem checkpoint com o usuário.
