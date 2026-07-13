---
id: step-16
type: agent
agent: lia-linha
execution: inline
model_tier: powerful
name: "Curadoria de Conteúdo"
outputFile: output/direcao-semanal.md
---

# Step 16 — Curadoria de Conteúdo

## Context Loading

Lia carrega: `_memory/memories.md`, `_memory/runs.md`, `pipeline/data/vila-identity.md`, `pipeline/data/tone-of-voice.md`, `output/relatorio.md` (mais recente, quando existir).

## Instructions

Este step só roda quando `plano.tipo_projeto == 'curadoria'` — por pedido explícito do usuário.

1. Executar `tasks/curar-conteudo.md` na íntegra.
2. Montar a curadoria retrospectiva (reaproveitamento) e prospectiva (prioridades).
3. Salvar o artefato do projeto e sobrescrever `pipeline/data/direcao-semanal-atual.md`.

## Output Format

Ver `tasks/curar-conteudo.md` — Formato de Saída.

## Output Example

```markdown
# Direção Editorial — semana de 14/07

## Pra Trás — Reaproveitamento
1. **Ângulo "nome do artista na linha 1"** — motivo: relatório de 07/07 mostrou 2x mais engajamento

## Pra Frente — Prioridades
1. **Rodízio** — motivo: nenhum post desse pilar nas últimas 2 semanas

## Válido até
21/07
```

## Veto Conditions

- Recomendação de reaproveitamento sem motivo concreto → remover
- Estimativa de performance sem base em `runs.md`/relatório real → VETO

## Quality Criteria

- [ ] Recomendação dividida em pra frente / pra trás
- [ ] Arquivo persistente `direcao-semanal-atual.md` atualizado
