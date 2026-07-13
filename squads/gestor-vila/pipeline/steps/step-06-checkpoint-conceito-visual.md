---
id: step-06
type: checkpoint
name: "Checkpoint de Conceito Visual"
inputFile: output/conceito-visual.md
---

# Step 06 — Checkpoint de Conceito Visual

## Context Loading

Carregar `output/conceito-visual.md`.

## Instructions

1. Apresentar o conceito visual completo ao usuário, slot por slot.
2. Perguntar aprovação explícita ou pedido de ajuste.
3. Se o usuário pedir ajuste, voltar ao Step 05 com a direção de correção.
4. Só avançar para o Step 07 (arte final) com aprovação explícita.

## Output Format

Registrar a resposta do usuário — aprovação ou ajuste pedido.

## Output Example

```
Aprovado. Pode gerar a arte final.
```

ou

```
Troca o mascote do post principal pro Cachorro, esse dia tem show à noite também.
```

## Veto Conditions

- Avançar para o Step 07 sem aprovação explícita → bloqueio absoluto
- Interpretar silêncio como aprovação → nunca, sempre esperar resposta

## Quality Criteria

- [ ] Conceito completo apresentado antes da pergunta
- [ ] Resposta do usuário registrada literalmente
- [ ] Ajustes pedidos redirecionam ao Step 05, não ao Step 07
