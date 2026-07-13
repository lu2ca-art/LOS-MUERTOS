---
id: step-12
type: agent
agent: renata-revisao
execution: inline
model_tier: powerful
name: "Revisão de Qualidade"
outputFile: output/review.md
on_reject: "agente_de_origem_da_peca_rejeitada"
---

# Step 12 — Revisão de Qualidade

## Context Loading

Renata carrega todo output já produzido no projeto (o que existir): `conteudo.md`, `visuais.md`, `arte-evento.jpg`, `roteiro-video.md`, `orientacao-edicao.md`, `campanha.md`, `relatorio.md`, `analise-concorrencia.md`, `plano-campanha-mensal.md`, `direcao-semanal.md`, além de `pipeline/data/quality-criteria.md`.

## Instructions

Este step roda **sempre**, em qualquer tipo de projeto que tenha produzido algum output — conteúdo de marca ou documento interno.

1. Executar `tasks/review.md` na íntegra.
2. Verificar hard caps H1-H6 primeiro (incluindo H5 — dado financeiro interno, H6 — decisão por gatilho automático).
3. Para documentos internos (relatório, análise de concorrência, plano estratégico), aplicar também os critérios D1-D4.
4. Atribuir nota e veredito por peça.
5. Se REJEITADO, direcionar o briefing de correção ao agente que produziu a peça especificamente.

## Output Format

Ver `tasks/review.md` — Formato de Saída.

## Output Example

```markdown
# Revisão de Qualidade — story almoço terça

## Hard Caps
| H1 | Marketing language ausente | ✅ |
| H4 | Publicação com aprovação pendente | ✅ |
| H5 | Nenhum dado financeiro interno | ✅ |
| H6 | Nenhuma decisão por gatilho automático | ✅ |

## Tabela de Vereditos
| Peça | Nota | Veredito | Correção |
|---|---|---|---|
| POST PRINCIPAL | 8/10 | APROVADO | — |
| STORY 1 | 7/10 | APROVADO | — |

## Status da Sessão
**APROVADA**

## Próximo Passo
Sessão pronta para o checkpoint final de publicação.
```

## Veto Conditions

- Sessão declarada APROVADA com qualquer peça < 7/10 → erro crítico
- Feedback vago sem ação específica → reescrever

## Quality Criteria

- [ ] Hard caps H1-H6 verificados antes de qualquer nota
- [ ] Critérios D1-D4 aplicados quando há documento interno
- [ ] Correção direcionada ao agente responsável, não genérica
