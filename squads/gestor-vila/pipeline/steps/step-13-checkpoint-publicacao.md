---
id: step-13
type: checkpoint
name: "Checkpoint Final de Publicação"
inputFile: output/review.md
---

# Step 13 — Checkpoint Final de Publicação

## Context Loading

Carregar `output/review.md` e todo o conteúdo/visual/vídeo já produzido e aprovado.

## Instructions

Este step só roda quando `plano.inclui_publicacao == true`.

1. Apresentar um resumo final de tudo que vai ser publicado — copy, visual, plataformas de destino.
2. Perguntar explicitamente: sim ou não para publicar.
3. **Este checkpoint é inegociável** — mesmo que o conteúdo tenha sido fornecido manualmente pelo usuário e já aprovado pela Renata, a publicação nunca acontece sem esse sim/não explícito aqui.
4. Se não aprovado, não avançar para o Step 14 — encerrar ou aguardar ajuste.

## Output Format

Registrar a resposta do usuário.

## Output Example

```
Sim, pode publicar.
```

ou

```
Não, ainda não — quero revisar a arte de novo antes.
```

## Veto Conditions

- Avançar para o Step 14 sem esse sim/não explícito → bloqueio absoluto, sem exceção
- Pular este checkpoint por já ter passado pela Renata → nunca — são gates independentes

## Quality Criteria

- [ ] Resumo completo apresentado antes da pergunta
- [ ] Resposta sim/não explícita registrada
