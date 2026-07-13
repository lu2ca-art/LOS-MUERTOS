---
id: step-15
type: agent
agent: rodrigo-resultados
execution: inline
model_tier: powerful
name: "Relatório de Marketing"
outputFile: output/relatorio.md
---

# Step 15 — Relatório de Marketing

## Context Loading

Rodrigo carrega: `output/publicacoes.md` e `output/campanha.md` do período analisado, skill `meta-business` (quando configurada).

## Instructions

Este step só roda quando `plano.tipo_projeto == 'relatorio'` — por pedido explícito do usuário, nunca automático por dia da semana.

1. Verificar se a skill `meta-business` está configurada; se não, avisar e seguir com dados manuais.
2. Levantar publicações e campanhas do período.
3. Analisar performance orgânica e paga separadamente.
4. Identificar top conteúdos e montar recomendações por agente.

## Output Format

Ver `tasks/relatorio-marketing.md` — Formato de Saída.

## Output Example

```markdown
# Relatório de Marketing — semana 07/07 → 13/07

## PERFORMANCE ORGÂNICA — FEED
| Post | Alcance | Engajamento | Taxa |
|---|---|---|---|
| RUNA ao vivo | 1.840 | 147 | 8,0% |

## RECOMENDAÇÕES
### Para Cris Criativa
Posts com nome do artista na linha 1 tiveram mais engajamento — manter padrão.
```

## Veto Conditions

- Métricas inventadas → remover, registrar como dado ausente
- Relatório sem recomendações → incompleto, não salvar

## Quality Criteria

- [ ] Fonte de cada métrica identificada (skill ou manual)
- [ ] Mínimo 3 recomendações acionáveis por agente
- [ ] Dados ausentes documentados explicitamente
