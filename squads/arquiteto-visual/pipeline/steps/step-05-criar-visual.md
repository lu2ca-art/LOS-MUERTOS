---
id: step-05
type: agent
agent: diana-design
execution: subagent
model_tier: powerful
name: "Criar Visual"
inputFile: output/conteudo-instagram.md
outputFile: output/visual-01.jpg
---

# Step 05 — Criar Visual

Diana Design recebe o conteúdo aprovado de Carlos Caption e produz o visual de fundo para o post principal da sessão — 1080×1440px em HTML/CSS renderizado via skill `image-creator`. Executa como subagent em paralelo com o Step 04 quando possível.

## Context Loading

Diana deve carregar:
1. `output/conteudo-instagram.md` (caption e tom da sessão)
2. `output/angulo-selecionado.md` (tom confirmado para decisão de paleta)
3. Design system CIDADE NEON (internalizado via treinamento): fundo #0a0a0a, neon #f9f320/#00f5e9/#ff2d55, grain SVG opacity 0.06-0.10

## Instructions

Executar a task `tasks/criar-visual.md` na íntegra:
1. Derivar tom visual do conteúdo e do tom confirmado
2. Definir hierarquia tipográfica (máx 3 elementos)
3. Escrever HTML/CSS completo 1080×1440px
4. Chamar skill `image-creator` para renderizar
5. Salvar em `output/visual-01.jpg`
6. Registrar decisões visuais nas notas

## Output Format

```
=== VISUAL CRIADO ===
Arquivo: output/visual-01.jpg
Tom visual: [tom aplicado]
Cor dominante: [hex]
Grain: opacity [valor]

=== NOTAS VISUAIS ===
[decisões de design relevantes para revisão de Vera]
```

## Veto Conditions

Não entregar se:
1. Render falhou — reportar erro e aguardar instrução do usuário
2. Background claro detectado no HTML — corrigir antes de renderizar

## Quality Criteria

- [ ] Dimensões 1080×1440px confirmadas no HTML
- [ ] Fundo escuro (#0a0a0a ou similar)
- [ ] Grain presente (opacity 0.06-0.10)
- [ ] lu2ca.art presente no layout
- [ ] Render executado com sucesso — output/visual-01.jpg existe
- [ ] Notas visuais preenchidas para Vera Veredito
