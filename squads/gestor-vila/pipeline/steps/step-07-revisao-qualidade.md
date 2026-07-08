---
step: 07
name: "Revisão de Qualidade"
type: quality_review
agent: renata-revisao
execution: inline
on_reject: step-02
---

# Step 07 — Revisão de Qualidade

## Objetivo

Renata Revisão emite veredito formal para cada peça da sessão. Sessão só avança como APROVADA quando todas as peças estão ≥ 7/10.

## Agente Ativo

**Renata Revisão** — Revisora de Qualidade Vila

## Tasks

Executar `agents/renata-revisao/tasks/review.md`:

1. Verificar hard caps H1-H4 em todas as peças
2. Avaliar critérios soft S1-S8 por peça
3. Atribuir nota 1-10 e veredito (APROVADO / CONDICIONAL / REJEITADO) por peça
4. Incluir briefing de correção para CONDICIONAL e REJEITADO
5. Determinar status da sessão
6. Emitir próximo passo concreto
7. Salvar em `output/review.md`

## Roteamento por Status

| Status da sessão | Próximo passo |
|------------------|---------------|
| APROVADA         | Prosseguir para Step 08 / Step 09 |
| CONDICIONAL      | Retornar briefings de correção aos agentes responsáveis; reexecutar steps afetados; revisar novamente |
| REJEITADA        | Voltar ao Step 02 (Cris Criativa) com briefing de retrabalho completo |

## Output Esperado

- `output/review.md` com tabela de vereditos e status da sessão

## Prosseguir para Steps 08 e 09.
