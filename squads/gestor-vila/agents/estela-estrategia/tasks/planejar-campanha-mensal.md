---
task: "Planejar Campanha Mensal"
order: 1
input: |
  - strategist: _opensquad/core/best-practices/strategist.md — metodologia de planejamento
  - identity: pipeline/data/vila-identity.md — pilares, público, marca
  - relatorio: output/relatorio.md — mais recente do Rodrigo, quando existir
  - concorrencia: _investigations/concorrentes/ — achados mais recentes da Íris, quando existirem
  - direcao_semanal: pipeline/data/direcao-semanal-atual.md — quando existir
output: |
  - file: output/{projeto}/plano-campanha-mensal.md — plano estratégico do período
  - persist: pipeline/data/plano-campanha-mensal-atual.md — sobrescrito com o plano mais recente
---

# Planejar Campanha Mensal

## Descrição

Estela monta o plano estratégico do próximo período — objetivos mensuráveis, alocação por pilar, janelas de investimento — usando a metodologia de `strategist.md` e os dados reais disponíveis (relatório do Rodrigo, achados da Íris).

## Processo

### 1. Carregar contexto

Reunir: perfil da Vila (`vila-identity.md`), relatório de performance mais recente (se existir), achados de concorrência mais recentes (se existirem), direção semanal em vigor (se existir). Se algum desses estiver ausente, sinalizar explicitamente o que está faltando e quais suposições estão sendo feitas no lugar.

### 2. Analisar posição atual

Avaliar forças, fraquezas, oportunidades e ameaças com base no que os dados mostram — não em intuição. Se não há dado suficiente para alguma dimensão, dizer isso.

### 3. Definir objetivos estratégicos do período

2-4 objetivos, cada um com KPI numérico, prazo e fonte de medição. Nunca objetivo vago.

### 4. Desenhar alocação por pilar e janelas de investimento

Distribuir prioridade entre os pilares de conteúdo da Vila. Identificar quais janelas do calendário (eventos, sazonalidade) merecem mais investimento e por quê.

### 5. Definir cadência de revisão

Quando esse plano será revisado, e que nível de desempenho (abaixo ou acima do esperado) dispara um ajuste.

### 6. Salvar e persistir

Salvar o artefato do projeto e sobrescrever `pipeline/data/plano-campanha-mensal-atual.md`.

## Formato de Saída

```markdown
# Plano de Campanha — [período]

## Contexto Consultado
- Relatório mais recente: [resumo ou "indisponível — suposições: ..."]
- Concorrência: [resumo ou "sem achados recentes"]
- Direção semanal em vigor: [resumo ou "nenhuma"]

## Objetivos Estratégicos
1. **[objetivo]** — KPI: [métrica, valor-alvo, prazo, fonte]
2. [...]

## Alocação por Pilar
| Pilar | Prioridade | Justificativa |
|---|---|---|
| [pilar] | [alta/média/baixa] | [motivo com dado real] |

## Janelas de Investimento do Período
| Janela | Motivo | Ação recomendada |
|---|---|---|

## Diferenciação (vs. concorrência)
[o que a Vila faz diferente, com base nos achados da Íris — nunca cópia]

## Cadência de Revisão
[quando revisar, o que dispara ajuste]

## Próximos Passos
1. [ação concreta]
```

## Critérios de Qualidade

- [ ] Pelo menos 2 objetivos com KPI numérico
- [ ] Toda prioridade de pilar justificada com dado real, não intuição
- [ ] Diferenciação da concorrência articulada, não cópia
- [ ] Cadência de revisão definida
- [ ] Contexto ausente sinalizado explicitamente, nunca preenchido com suposição não declarada

## Condições de Veto

- **Objetivo sem KPI numérico** → reescrever
- **Recomendação que copia concorrente diretamente** → VETO, reescrever como diferenciação
- **Plano sem cadência de revisão** → bloqueio, adicionar antes de entregar
- **Qualquer critério de alocação baseado em cachê/valor de artista** → VETO absoluto
