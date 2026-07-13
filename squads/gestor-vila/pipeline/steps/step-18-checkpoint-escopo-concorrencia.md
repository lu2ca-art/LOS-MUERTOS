---
id: step-18
type: checkpoint
name: "Checkpoint de Escopo de Concorrência"
---

# Step 18 — Checkpoint de Escopo de Concorrência

## Context Loading

Carregar `_investigations/concorrentes/` (lista de concorrentes já monitorados, se houver).

## Instructions

Este step só roda quando `plano.tipo_projeto == 'analise_concorrencia'`. É obrigatório antes de qualquer step subagent de pesquisa (regra do framework).

1. Perguntar ou confirmar quais concorrentes monitorar (3-5 locais de Bethaville/Barueri/Alphaville).
2. Se já há histórico, propor a mesma lista por padrão.
3. Aguardar confirmação antes de despachar a Íris.

## Output Format

Registrar a lista confirmada de concorrentes.

## Output Example

```
Confirmado: Quintal BethaVille, Cabana Burger Alphaville, Killer Burger.
```

## Veto Conditions

- Despachar a Íris sem essa confirmação → bloqueio absoluto

## Quality Criteria

- [ ] Lista de concorrentes confirmada explicitamente pelo usuário
