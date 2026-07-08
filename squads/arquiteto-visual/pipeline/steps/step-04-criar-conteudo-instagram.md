---
id: step-04
type: agent
agent: carlos-caption
execution: inline
model_tier: powerful
name: "Criar Conteúdo Instagram"
inputFile: output/angulo-selecionado.md
outputFile: output/conteudo-instagram.md
---

# Step 04 — Criar Conteúdo Instagram

Carlos Caption recebe o ângulo selecionado e o tom confirmado e produz o conteúdo completo para Instagram — script de Reel, caption de feed e/ou sequência de Stories conforme os formatos da sessão.

## Context Loading

Antes de escrever, Carlos deve:
1. Ler `output/angulo-selecionado.md` (ângulo, tom, linha de abertura)
2. Ler `pipeline/data/tone-of-voice.md` (características do tom confirmado)
3. Ler `pipeline/data/output-examples.md` (exemplos reais de alto engajamento para calibrar nível de concisão)
4. Ler `pipeline/data/lu2ca-universe.md` (vocabulário ativo da era)

## Instructions

Executar as tasks correspondentes aos formatos da sessão:
- **Reel solicitado** → `tasks/criar-reel.md` (obrigatório: HOOK, SETUP, DELIVERY, LOOP, CTA + caption)
- **Feed solicitado** → `tasks/criar-feed.md` (hook autônomo ≤125 chars, ≤3 linhas)
- **Stories solicitados** → `tasks/criar-stories.md` (4-7 frames, elemento interativo obrigatório)

Se múltiplos formatos foram solicitados, Carlos executa todas as tasks na ordem: Reel → Feed → Stories.

**Nota sobre on_reject:** Se Vera Veredito rejeitar no Step 08 e o loop voltar aqui, Carlos recebe o briefing de correção de Vera e refaz apenas as peças CONDICIONAL ou REJEITADAS — não toda a sessão.

## Output Format

Ver tasks individuais — Output Format de cada task usada.

O arquivo `output/conteudo-instagram.md` consolida todos os outputs:

```
# Conteúdo Instagram — [data da sessão]

## Ângulo: [nome] | Tom: [tom confirmado]

[output de criar-reel.md, se aplicável]

---

[output de criar-feed.md, se aplicável]

---

[output de criar-stories.md, se aplicável]
```

## Veto Conditions

Não salvar output se:
1. Caption (feed ou Reel) com >3 linhas — rejeição imediata
2. Marketing language presente em qualquer peça

## Quality Criteria

- [ ] Todos os formatos solicitados na sessão foram produzidos
- [ ] Nenhuma peça viola os hard caps (caption ≤3 linhas, zero marketing language)
- [ ] Vocabulário LU2CA presente em todas as peças
- [ ] Output consolidado salvo em `output/conteudo-instagram.md`
