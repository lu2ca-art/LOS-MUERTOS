---
id: step-03
type: checkpoint
name: "Confirmação do Time"
inputFile: output/plano-projeto.md
outputFile: output/plano-projeto.md
---

# Step 03 — Confirmação do Time

## Context Loading

Carregar `output/plano-projeto.md` — se o Step 02 rodou, contém o plano completo do Beto; se foi pulado (pedido específico), este step apresenta diretamente o agente identificado no pedido original.

## Instructions

1. Se o Step 02 rodou: apresentar o plano (especialistas, o que cada um vai produzir, pendências) e perguntar as pendências identificadas.
2. Se o Step 02 foi pulado (pedido específico): confirmar rapidamente que o agente certo foi identificado, sem reapresentar um "plano" completo — fricção mínima para pedidos diretos.
3. Nunca avançar para os steps seguintes sem essa confirmação explícita do usuário.
4. Registrar a resposta do usuário (aprovação + respostas às pendências) no arquivo.

## Output Format

Anexar ao `plano-projeto.md`:

```markdown
## Confirmação do Usuário
[resposta literal do usuário]

## Pendências Resolvidas
- [pergunta] → [resposta]
```

## Output Example

```markdown
## Confirmação do Usuário
pode seguir, e o público é fãs de MPB 25-45 anos

## Pendências Resolvidas
- "qual o público-alvo da campanha?" → "fãs de MPB 25-45 anos"
```

## Veto Conditions

- Avançar para qualquer step de agente sem essa confirmação → bloqueio absoluto
- Pendência identificada no Step 02 e não resolvida aqui → não avançar, perguntar de novo

## Quality Criteria

- [ ] Confirmação explícita do usuário registrada
- [ ] Toda pendência do Step 02 (quando houve) foi resolvida
- [ ] Nenhum trabalho de especialista começou antes desta confirmação
