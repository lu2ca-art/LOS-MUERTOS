---
id: step-17
type: agent
agent: estela-estrategia
execution: inline
model_tier: powerful
name: "Planejamento de Campanha Mensal"
outputFile: output/plano-campanha-mensal.md
---

# Step 17 — Planejamento de Campanha Mensal

## Context Loading

Estela carrega: `_opensquad/core/best-practices/strategist.md`, `pipeline/data/vila-identity.md`, `output/relatorio.md` (mais recente), `_investigations/concorrentes/` (mais recentes), `pipeline/data/direcao-semanal-atual.md`.

## Instructions

Este step só roda quando `plano.tipo_projeto == 'planejamento_mensal'` — por pedido explícito do usuário.

1. Executar `tasks/planejar-campanha-mensal.md` na íntegra.
2. Definir objetivos com KPI numérico.
3. Alocar prioridade por pilar com justificativa em dado real.
4. Salvar o artefato do projeto e sobrescrever `pipeline/data/plano-campanha-mensal-atual.md`.

## Output Format

Ver `tasks/planejar-campanha-mensal.md` — Formato de Saída.

## Output Example

```markdown
# Plano de Campanha — julho 2026

## Objetivos Estratégicos
1. **Aumentar alcance médio de post** — KPI: de 2.000 para 2.800 até 31/07, fonte: relatório semanal

## Alocação por Pilar
| Pilar | Prioridade | Justificativa |
|---|---|---|
| Rodízio | Alta | maior engajamento histórico segundo relatório |

## Cadência de Revisão
Revisão semanal às segundas, via projeto de relatório.
```

## Veto Conditions

- Objetivo sem KPI numérico → reescrever
- Recomendação que copia concorrente diretamente → VETO

## Quality Criteria

- [ ] Pelo menos 2 objetivos com KPI numérico
- [ ] Cadência de revisão definida
- [ ] Arquivo persistente `plano-campanha-mensal-atual.md` atualizado
