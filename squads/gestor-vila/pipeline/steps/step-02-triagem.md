---
id: step-02
type: agent
agent: beto-briefing
execution: inline
name: "Triagem"
inputFile: output/plano-projeto.md
outputFile: output/plano-projeto.md
---

# Step 02 — Triagem

## Context Loading

Beto carrega: `output/plano-projeto.md` (pedido original), `pipeline/data/vila-identity.md`, `pipeline/data/direcao-semanal-atual.md`, `pipeline/data/plano-campanha-mensal-atual.md`, `_investigations/concorrentes/` (mais recentes) — os que existirem.

## Instructions

Este step só roda quando `plano-projeto.md` tem `pedido_amplo_ou_ambiguo: true` (senão, pulado — o pedido específico já indica o agente a acionar).

1. Executar a task `tasks/triagem-projeto.md` na íntegra.
2. Consultar o contexto de fundo automático (direção semanal, plano mensal, concorrência) antes de montar o plano.
3. Mapear o pedido para os especialistas necessários.
4. Identificar pendências de input.
5. Sobrescrever `output/plano-projeto.md` com o plano completo, mantendo o pedido original no topo.

## Output Format

Ver `tasks/triagem-projeto.md` — Formato de Saída.

## Output Example

```markdown
# Plano do Projeto

pedido_amplo_ou_ambiguo: true

## Pedido Original
projeto story almoço, iniciar pipe

## Objetivo Identificado
Post + stories orgânicos para o horário de almoço, sem evento de show associado.

## Contexto de Fundo Consultado
- Direção semanal (Lia): prioridade em Rodízio e Domínio Territorial essa semana
- Plano mensal (Estela): nenhum em vigor
- Concorrência (Íris): sem achados recentes

## Especialistas Necessários
1. Cris Criativa — copy orgânica do dia
2. Vito Visual — arte estática para o post e stories

plano.inclui_copy: true
plano.inclui_visual: true
plano.inclui_video_pre_producao: false
plano.inclui_video_pos_producao: false
plano.inclui_trafego_pago: false
plano.inclui_publicacao: true
plano.tipo_projeto: conteudo

## Inclui publicação?
SIM — checkpoint final de aprovação manual obrigatório

## Pendências
nenhuma pendência — pronto para confirmar
```

## Veto Conditions

- Plano com agente decidindo algo baseado em cachê/valor/histórico automático → VETO absoluto
- Plano despachado sem passar pela confirmação do usuário (Step 03) → bloqueio

## Quality Criteria

- [ ] Plano lista só os especialistas necessários
- [ ] Contexto de fundo consultado e registrado
- [ ] Flags `plano.*` presentes para orientar os steps condicionais seguintes
- [ ] Pendências de input listadas como perguntas objetivas
