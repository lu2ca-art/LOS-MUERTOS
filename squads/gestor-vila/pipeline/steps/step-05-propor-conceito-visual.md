---
id: step-05
type: agent
agent: vito-visual
execution: subagent
model_tier: powerful
name: "Propor Conceito Visual"
inputFile: output/conteudo.md
outputFile: output/conceito-visual.md
---

# Step 05 — Propor Conceito Visual

## Context Loading

Vito carrega: `output/conteudo.md` (copy do Cris OU colada manualmente pelo usuário no plano do projeto), `pipeline/data/vila-identity.md`.

## Instructions

Este step só roda quando `plano.inclui_visual == true`.

**Executar apenas a task `tasks/propor-conceito-visual.md` neste step** — não gerar nenhuma arte final aqui, mesmo que o agente tenha outras tasks declaradas. A arte final só acontece no Step 07, depois do checkpoint de aprovação do Step 06.

1. Ler cada slot do conteúdo.
2. Montar o conceito visual por slot (formato, elemento central, mascote, logo, paleta, composição).
3. Salvar em `output/conceito-visual.md`, sempre terminando com "Aguardando aprovação".

## Output Format

Ver `tasks/propor-conceito-visual.md` — Formato de Saída.

## Output Example

```markdown
# Conceito Visual — story almoço terça

## POST PRINCIPAL
**Formato:** 1080×1350px
**Elemento central:** nachos e guacamole em destaque
**Mascote:** Gato (culinária)
**Logo:** com mascotes
**Paleta:** preto, laranja, ouro
**Composição:** prato em primeiro plano, fundo texturizado escuro, tipografia Bebas Neue

## STORY 1 — Engajamento
**Formato:** 1080×1920px
**Elemento central:** pergunta interativa sobre mesa preferida
**Mascote:** Cachorro
**Logo:** texto
**Paleta:** preto, amarelo
**Composição:** espaço central livre pra enquete do Instagram

---
**Pronto para gerar a arte final? Aguardando aprovação.**
```

## Veto Conditions

- Gerar arte final nesta etapa → bloqueio absoluto, isso é do Step 07
- Conceito com asset fora do brand kit oficial `kAHGNC-y7zM` → revisar antes de apresentar

## Quality Criteria

- [ ] Todo slot do conteúdo tem conceito correspondente
- [ ] Assets conforme `vila-identity.md`
- [ ] Nenhuma arte gerada nesta task
