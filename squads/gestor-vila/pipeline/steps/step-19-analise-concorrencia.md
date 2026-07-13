---
id: step-19
type: agent
agent: iris-investigacao
execution: subagent
model_tier: fast
name: "Análise de Concorrência"
outputFile: output/analise-concorrencia.md
---

# Step 19 — Análise de Concorrência

## Context Loading

Íris carrega: `_opensquad/core/best-practices/researching.md`, `pipeline/data/vila-identity.md`, `_investigations/concorrentes/` (histórico anterior por concorrente).

## Instructions

Este step só roda depois do Step 18 confirmado.

1. Executar `tasks/monitorar-concorrencia.md` na íntegra.
2. Para cada concorrente confirmado, coletar dados atuais via `apify`/`web_search`.
3. Comparar com a checagem anterior, quando existir.
4. Anexar (nunca sobrescrever) o histórico por concorrente e sintetizar no artefato do projeto.

## Output Format

Ver `tasks/monitorar-concorrencia.md` — Formato de Saída.

## Output Example

```markdown
# Análise de Concorrência — 14/07

## Concorrentes Monitorados
1. Quintal BethaVille — zero ads pagos, cresceu só orgânico
2. Cabana Burger Alphaville — 1 ad irrelevante, <R$100

## O que mudou desde a última checagem
Quintal BethaVille aumentou frequência de posts de 3x/semana para 5x/semana.

## Gaps observados
Nenhum concorrente local investe em campanha paga de forma consistente.
```

## Veto Conditions

- Rodar sem o Step 18 confirmado → bloqueio absoluto
- Sobrescrever histórico anterior em vez de anexar → VETO
- Recomendação estratégica presente (isso é da Estela) → remover

## Quality Criteria

- [ ] Pelo menos 3 concorrentes monitorados
- [ ] Toda observação com fonte e data
- [ ] Histórico por concorrente preservado
