---
id: step-08
type: agent
agent: vera-veredito
execution: inline
model_tier: powerful
name: "Revisão de Qualidade"
on_reject: step-04
inputFile: output/conteudo-instagram.md
outputFile: output/review.md
---

# Step 08 — Revisão de Qualidade

Vera Veredito revisa todo o conteúdo da sessão e emite veredito formal por peça. Se qualquer peça for REJEITADA (nota ≤4 ou hard cap violado), o pipeline retorna ao Step 04 com briefing de correção para Carlos Caption. A sessão não avança para o Step 09 sem todas as peças com nota ≥7.

## Context Loading

Vera deve carregar:
1. `output/conteudo-instagram.md` (conteúdo de Carlos Caption)
2. `output/visual-01.jpg` (visual de Diana Design — revisão visual)
3. `output/adaptacoes.md` (adaptações de Rafael Repercussão)
4. `pipeline/data/quality-criteria.md` (critérios oficiais com benchmarks reais)

## Instructions

Executar a task `tasks/review.md` na íntegra:

1. Verificar hard caps primeiro (H1-H4) — qualquer violação = REJEITADO sem nota
2. Atribuir nota 1-10 por peça que passou nos hard caps
3. Emitir tabela de vereditos com raciocínio derivado de critérios específicos
4. Para CONDICIONAL: ≤2 correções acionáveis
5. Para REJEITADO: briefing completo para o agente responsável
6. Verificar ecossistema gamificado (lu2ca.art) em toda a sessão
7. Emitir status da sessão (APROVADA / CONDICIONAL / REJEITADA)

**on_reject behavior:** Se status = REJEITADA (hard cap ou nota ≤4), o pipeline retorna automaticamente ao Step 04. Carlos Caption recebe o briefing de correção de Vera e refaz apenas as peças problemáticas.

## Output Format

Ver `tasks/review.md` — Output Format section.

## Veto Conditions

Não emitir APROVADA se:
1. Qualquer peça tem nota <7 — a sessão é avaliada como conjunto
2. Hard cap foi violado em qualquer peça — REJEITADO é inegociável

## Quality Criteria

- [ ] Hard caps verificados antes de qualquer nota
- [ ] Veredito formal emitido por peça com nota numérica
- [ ] Raciocínio baseado em critério específico dos dados reais investigados
- [ ] Briefings de correção acionáveis para toda peça CONDICIONAL ou REJEITADA
- [ ] Ecossistema gamificado verificado para toda a sessão
- [ ] Output salvo em `output/review.md`
