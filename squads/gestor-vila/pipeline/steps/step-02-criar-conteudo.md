---
step: 02
name: "Criar Conteúdo"
type: content_creation
agent: cris-criativa
execution: inline
---

# Step 02 — Criar Conteúdo

## Objetivo

Cris Criativa lê o briefing do dia e escreve o copy completo para todos os slots ativos. Se há gatilho para anúncio pago, também escreve o copy do anúncio.

## Agente Ativo

**Cris Criativa** — Criadora de Conteúdo Vila

## Tasks

1. Executar `agents/cris-criativa/tasks/criar-conteudo-diario.md`
   - Ler `output/briefing.md`
   - Selecionar ton de voz correto para o tipo de dia
   - Escrever copy de todos os slots ativos
   - Verificar hard caps H1-H4
   - Salvar em `output/conteudo.md`

2. Se `briefing.tem_evento_pago == true`, executar `agents/cris-criativa/tasks/criar-anuncio-evento.md`
   - Escrever 3 headlines + 2 variações de primary text
   - Adicionar seção `## ANÚNCIO PAGO` em `output/conteudo.md`

## Output Esperado

- `output/conteudo.md` com copy de todos os slots
- Seção `## ANÚNCIO PAGO` adicionada se gatilho ativo

## Prosseguir para Step 03 — Vito Visual.
