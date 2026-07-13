---
id: step-07
type: agent
agent: vito-visual
execution: subagent
model_tier: powerful
name: "Gerar Arte Final"
inputFile: output/conceito-visual.md
outputFile: output/visuais.md
---

# Step 07 — Gerar Arte Final

## Context Loading

Vito carrega: `output/conceito-visual.md` (aprovado no Step 06), `output/conteudo.md`, `pipeline/data/vila-identity.md`.

## Instructions

Este step só roda depois do Step 06 aprovado.

**Executar `tasks/gerar-arte-final.md`** para as peças orgânicas (post, stories). **Se `conteudo.md` contém seção ANÚNCIO PAGO, executar também `tasks/criar-arte-evento.md`** em seguida, para a arte quadrada de campanha.

1. Verificar brand kit disponível.
2. Gerar cada peça via Canva MCP (post/stories) e, se aplicável, via image-creator (arte de evento).
3. Registrar todos os design_ids e o caminho do arquivo de arte de evento.

## Output Format

Ver `tasks/gerar-arte-final.md` e `tasks/criar-arte-evento.md` — Formato de Saída.

## Output Example

```markdown
# Visuais — story almoço terça

## POST PRINCIPAL
design_id: DAG-abc123
formato: 1080×1350px
slot: post_principal

## STORY 1 — Engajamento
design_id: DAG-def456
formato: 1080×1920px
slot: story_engajamento
```

## Veto Conditions

- Gerar sem o conceito aprovado no Step 06 → bloqueio absoluto
- Brand kit errado → cancelar e regerar com `kAHGNC-y7zM`
- design_id ausente para qualquer peça → nunca avançar para revisão

## Quality Criteria

- [ ] Conceito aprovado seguido fielmente
- [ ] Todos os design_ids registrados
- [ ] Thumbnail verificado antes de reportar
