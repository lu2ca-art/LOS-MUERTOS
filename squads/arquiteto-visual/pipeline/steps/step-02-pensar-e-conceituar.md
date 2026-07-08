---
id: step-02
type: agent
agent: bruno-brainstorm
execution: inline
model_tier: powerful
name: "Pensar e Conceituar"
inputFile: output/contexto.md
outputFile: output/angulos.md
---

# Step 02 — Pensar e Conceituar

Bruno Brainstorm analisa o contexto da sessão e gera a pauta estratégica do dia mais 5 ângulos criativos distintos. Este é o momento de maior rigor estratégico — os ângulos que saem aqui determinam o conteúdo de toda a sessão.

## Context Loading

Antes de gerar qualquer output, Bruno deve:
1. Ler `output/contexto.md` (briefing da sessão)
2. Ler `pipeline/data/lu2ca-universe.md` (vocabulário e era)
3. Ler `pipeline/data/tone-of-voice.md` (6 tons e suas características)
4. Ler `pipeline/data/domain-framework.md` (ERA-ÂNGULO-FORMATO)
5. Verificar em `_memory/memories.md` se há aprendizados de sessões anteriores relevantes

## Instructions

Executar a task `tasks/pensar-e-conceituar.md` na íntegra. Entregar:
- Pauta estratégica (1 frase)
- Recomendação com ★ e justificativa
- 5 ângulos com lens + linha de abertura (cobrindo as 5 dimensões obrigatórias)

O output vai direto para o usuário — Bruno não pede aprovação antes de mostrar; ele mostra e deixa o usuário decidir no checkpoint seguinte.

## Output Format

Ver `tasks/pensar-e-conceituar.md` — Output Format section.

## Output Example

Ver `tasks/pensar-e-conceituar.md` — Output Example section.

## Veto Conditions

Não salvar output se:
1. Algum ângulo não usa vocabulário proprietário de LU2CA
2. Ângulo Vulnerável/Humano ou Comunitário/Gamificado está ausente

## Quality Criteria

- [ ] Pauta estratégica em 1 frase
- [ ] 5 ângulos cobrindo as 5 dimensões
- [ ] Recomendação com ★ justificada
- [ ] Output salvo em `output/angulos.md`
