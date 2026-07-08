---
step: 03
name: "Criar Visual"
type: visual_creation
agent: vito-visual
execution: subagent
---

# Step 03 — Criar Visual

## Objetivo

Vito Visual cria o visual de feed (1080×1440px) para o POST PRINCIPAL. Se há gatilho para anúncio pago, também cria a arte de evento (1080×1080px).

## Agente Ativo

**Vito Visual** — Designer Visual Vila

## Tasks

1. Executar `agents/vito-visual/tasks/criar-visual-post.md`
   - Ler `output/conteudo.md` — seção POST PRINCIPAL
   - Documentar design system
   - Criar HTML/CSS 1080×1440px
   - Renderizar via `image-creator`
   - Salvar em `output/visual-01.jpg`

2. Se `output/conteudo.md` contém seção `## ANÚNCIO PAGO`, executar `agents/vito-visual/tasks/criar-arte-evento.md`
   - Criar arte 1080×1080px
   - Renderizar via `image-creator`
   - Salvar em `output/arte-evento.jpg`

## Output Esperado

- `output/visual-01.jpg` — visual de feed (sempre)
- `output/arte-evento.jpg` — arte de evento (se gatilho ativo)

## Prosseguir para Step 04 — Aprovação de Conteúdo.
