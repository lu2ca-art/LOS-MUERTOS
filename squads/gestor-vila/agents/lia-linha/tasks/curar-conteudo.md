---
task: "Curar Conteúdo"
order: 1
input: |
  - memories: _memory/memories.md — preferências e aprendizados acumulados
  - runs: _memory/runs.md — histórico de execuções e resultados
  - identity: pipeline/data/vila-identity.md — pilares de conteúdo
  - tone: pipeline/data/tone-of-voice.md — tons e frequência
  - relatorio: output/relatorio.md do Rodrigo — quando existir
output: |
  - file: output/{projeto}/direcao-semanal.md — direção prospectiva + retrospectiva
  - persist: pipeline/data/direcao-semanal-atual.md — sobrescrito com a direção mais recente
---

# Curar Conteúdo

## Descrição

Lia produz uma direção editorial com duas partes: o que priorizar daqui pra frente, e o que reaproveitar do que já foi feito. As duas juntas formam a curadoria.

## Processo

### 1. Levantar o histórico

Ler `_memory/runs.md` e `_memory/memories.md` em busca de: temas/ângulos que já foram usados, qualquer indicação de performance (do Rodrigo, ou feedback explícito do usuário registrado em memories.md), e o que já foi feito recentemente (pra não repetir sem adaptar).

### 2. Montar a curadoria retrospectiva ("pra trás")

Identificar o que vale reaproveitar: um ângulo, um formato, um tema que teve resultado bom ou feedback positivo. Para cada recomendação, indicar o motivo concreto (não estimar performance sem dado).

Se não há dado suficiente no histórico, dizer isso explicitamente — não inventar recomendação.

### 3. Montar a direção prospectiva ("pra frente")

Olhar o que se aproxima (calendário, datas comemorativas, sazonalidade) e cruzar com os pilares de `vila-identity.md`. Recomendar prioridades — quais pilares merecem mais peso na próxima janela de conteúdo, com base no que está por vir.

### 4. Consolidar e salvar

Salvar o artefato do projeto e sobrescrever o arquivo persistente `pipeline/data/direcao-semanal-atual.md`, que outros projetos vão consultar automaticamente daqui pra frente.

## Formato de Saída

```markdown
# Direção Editorial — [data/janela]

## Pra Trás — Reaproveitamento
1. **[tema/ângulo/formato]** — motivo: [dado concreto ou feedback registrado]
2. [...]
[ou: "sem dado de performance suficiente no histórico para recomendar reaproveitamento"]

## Pra Frente — Prioridades
1. **[pilar/ângulo]** — motivo: [o que se aproxima, por que priorizar]
2. [...]

## Válido até
[quando essa direção deve ser revisada de novo]
```

## Critérios de Qualidade

- [ ] Recomendação de reaproveitamento tem motivo concreto ou é explicitamente marcada como sem dado suficiente
- [ ] Direção prospectiva cruza calendário/sazonalidade com os pilares oficiais
- [ ] Arquivo persistente `direcao-semanal-atual.md` atualizado

## Condições de Veto

- **Recomendação de reaproveitamento sem motivo** → remover ou marcar como especulativa
- **Estimativa de performance sem base em `runs.md`/feedback real** → VETO, reescrever como "sem dado disponível"
