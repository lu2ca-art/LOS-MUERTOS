---
task: "Criar Visual de Post"
order: 1
input: |
  - conteudo: output/YYYY-MM-DD-HHmmss/v1/conteudo.md — copy do POST PRINCIPAL e stories
  - identity: pipeline/data/vila-identity.md — brand kit, paleta, fontes, assets
tool: canva_mcp
output: |
  - file: output/YYYY-MM-DD-HHmmss/v1/visuais.md — lista de design_ids por slot
---

# Criar Visual de Post

## Descrição

Vito cria todos os visuais do dia via **Canva MCP**, usando obrigatoriamente o brand kit `kAHGNC-y7zM` ("LOS MUERTOS"). O fluxo é: `generate-design` → `create-design-from-candidate` → registrar `design_id`.

> ⚠️ Nunca usar o brand kit "Perna de Porco + Texano". Verificar antes de cada chamada.

## Processo

### 1. Verificar brand kit disponível

```
mcp__claude_ai_Canva__list-brand-kits
→ confirmar que kAHGNC-y7zM ("LOS MUERTOS") está listado
```

### 2. Ler conteudo.md

Extrair de cada slot:
- **POST PRINCIPAL:** elemento central (artista OU prato OU evento), horário, dia
- **STORY 1:** pergunta interativa, tom
- **STORY 2:** detalhe concreto, CTA físico
- **STORY CHEF ALEX:** roteiro de bastidor
- **STORY SHOW** (se presente): artista, horário, tom festivo

### 3. Gerar visual por slot

Para cada slot, executar a sequência completa:

```
Passo A — Gerar candidatos:
mcp__claude_ai_Canva__generate-design
  brand_kit_id: kAHGNC-y7zM
  prompt: [prompt descritivo do slot — ver tabela abaixo]
→ retorna: job_id + candidate_id

Passo B — Criar design final:
mcp__claude_ai_Canva__create-design-from-candidate
  job_id: [retornado no passo A]
  candidate_id: [retornado no passo A]
→ retorna: design_id ← REGISTRAR

Passo C — Confirmar visual:
mcp__claude_ai_Canva__get-design-thumbnail
  design_id: [retornado no passo B]
→ verificar se visual está correto antes de prosseguir
```

### 4. Prompts por slot

| Slot | Formato | Prompt base |
|------|---------|-------------|
| **Post Principal** | 1080×1350 (4:5) | "Post feed Instagram Vila Los Muertos de Fome. Fundo preto com textura grunge/ruído. Logo principal com mascotes (`MAHGNLbQWgA`) visível e legível no topo. Tipografia bold Bebas Neue centralizada. Letras sempre minúsculas. [elemento central do dia]. Paleta: preto, ouro #F0B400, laranja #F03C14. Adicionar o [Mascote correspondente] no canto da composição." |
| **Story Engajamento** | 1080×1920 (9:16) | "Story Instagram 9:16. Layout limpo, espaço central vago para sticker/enquete. Fundo preto texturizado. Logo texto (`MAHGNFlIHeA`) pequeno no rodapé. Letras minúsculas em Bebas Neue amarelo. Pergunta: [pergunta do STORY 1]. Incluir Mascote Cachorro (`MAHGNAoapdI`) espiando da base." |
| **Story Informação** | 1080×1920 (9:16) | "Story Instagram 9:16. Fundo escuro. Destaque de prato ou bebida com borda fina dourada (#F0B400). Detalhe [detalhe do STORY 2] em Oswald creme. CTA em destaque na parte inferior: [CTA da Cris] em Azul Real (#0014C8) bold e caixa baixa." |
| **Story Chef Alex** | 1080×1920 (9:16) | "Story bastidores de cozinha 9:16. Estética real, orgânica e sem excessos. Chef Alex Coelho. Fundo escuro. Badge 'segredos do chef' com o Mascote Gato (`MAHGNL0Ig4Y`) no topo. [roteiro do story]." |
| **Story Show** | 1080×1920 (9:16) | "Story show ao vivo 9:16. Estética de cartaz lambe-lambe urbano noturno. Nome do artista [ARTISTA] em Bebas Neue gigante amarelo ou magenta. Data e Horário [HH:MM] visíveis. Mascote Cachorro (`MAHGNAoapdI`) em destaque festivo ao lado. CTA: 'chega cedo'." |

### 5. Assets disponíveis para incluir no prompt

| Asset | ID | Quando usar |
|-------|-----|-------------|
| **Logo com mascotes** | `MAHGNLbQWgA` | Posts Principais de Feed, capas de eventos ou anúncios de grande alcance. |
| **Logo texto** | `MAHGNFlIHeA` | Stories, layouts verticais ou peças com muita informação (assinatura compacta). |
| **Mascote cachorro** | `MAHGNAoapdI` | Símbolo de festa e noite. Usar em: **Shows (Quinta a Sábado), Samba, Happy Hour e Stand-up**. |
| **Mascote gato** | `MAHGNL0Ig4Y` | Símbolo de culinária e calor familiar. Usar em: **Feijoada (Domingo), bastidores do Chef e receitas**. |
| **Post referência** | `DAHGRk_auLQ` | Consultar como padrão dourado de balanceamento de cor, grunge e alinhamento. |

### 6. Salvar visuais.md

```markdown
# Visuais — [DATA]

## POST PRINCIPAL
design_id: [ID]
formato: 1080×1350px
slot: post_principal

## STORY 1 — Engajamento
design_id: [ID]
formato: 1080×1920px
slot: story_engajamento

## STORY 2 — Informação
design_id: [ID]
formato: 1080×1920px
slot: story_informacao

## STORY CHEF ALEX
design_id: [ID]
formato: 1080×1920px
slot: story_chef_alex

## STORY SHOW (condicional)
design_id: [ID]
formato: 1080×1920px
slot: story_show
```

## Critérios de Qualidade

- [ ] Brand kit `kAHGNC-y7zM` confirmado antes de cada geração
- [ ] Sequência completa executada para cada slot (generate → create → thumbnail)
- [ ] design_id registrado para cada visual em visuais.md
- [ ] Thumbnail verificado — visual corresponde ao slot
- [ ] Formato correto por slot (1080×1350 feed / 1080×1920 stories)

## Condições de Veto

- **Brand kit errado** → cancelar e regerar com `kAHGNC-y7zM`
- **Visual genérico** (poderia ser qualquer restaurante) → regerar com prompt mais específico
- **design_id ausente** → nunca avançar para Step 04 sem registrar os IDs
