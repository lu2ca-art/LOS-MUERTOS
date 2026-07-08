---
step: 04
name: "Aprovação de Conteúdo"
type: checkpoint
agent: inline
---

# Step 04 — Aprovação de Conteúdo

## Objetivo

Apresentar o conteúdo completo (copy + visual) para aprovação do usuário antes da publicação.

## Instructions

Apresente ao usuário um preview completo do conteúdo criado:

1. Exibir o copy de cada slot do `output/conteudo.md`
2. Confirmar que `output/visual-01.jpg` foi gerado
3. Se há `output/arte-evento.jpg`, confirmar
4. Se há seção `## ANÚNCIO PAGO`, resumir o briefing de campanha que será criado

Pergunte ao usuário usando AskUserQuestion:

- **Opção A: Aprovar e publicar** — conteúdo está ótimo, publicar em todas as plataformas
- **Opção B: Aprovar com ajuste** — publicar, mas com uma correção específica (descrever)
- **Opção C: Reprovar** — refazer o conteúdo com nova direção

**Se o usuário APROVAR:** registrar aprovação e prosseguir para Step 05 — Paulo Postador.

**Se o usuário REPROVAR:** voltar para Step 02 — Cris Criativa com a direção de correção informada.

**Se o usuário APROVAR COM AJUSTE:** aplicar o ajuste antes de prosseguir para Step 05.

## Nota para Paulo Postador

Paulo só pode publicar após aprovação explícita neste step. A aprovação aqui é o único gatilho válido para publicação.
