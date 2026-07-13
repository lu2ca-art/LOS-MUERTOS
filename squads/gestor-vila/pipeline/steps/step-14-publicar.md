---
id: step-14
type: agent
agent: paulo-postador
execution: subagent
model_tier: powerful
name: "Publicar em Plataformas"
inputFile: output/conteudo.md
outputFile: output/publicacoes.md
---

# Step 14 — Publicar em Plataformas

## Context Loading

Paulo carrega: `output/conteudo.md`, `output/visuais.md`, confirmação do Step 13.

## Instructions

Este step só roda depois do Step 13 aprovado com sim explícito.

1. Verificar estado de conexão da conta (`@vilalosmuertosdefome`).
2. Se conta errada ou desconectada, entrar em estado PENDENTE — gerar pacote, não publicar.
3. Dry-run antes de qualquer publicação real.
4. Publicar plataforma por plataforma, reportando resultado e URL.

## Output Format

Ver `tasks/publicar-plataformas.md` — Formato de Saída.

## Output Example

```markdown
# Publicações — story almoço terça

| Plataforma | Status | URL | Horário |
|---|---|---|---|
| Instagram | Publicado | instagram.com/p/xyz | 19h02 |
| Facebook | Publicado | facebook.com/... | 19h03 |
```

## Veto Conditions

- Publicar sem o Step 13 aprovado → bloqueio absoluto
- Publicar pela conta errada (`@lu2ca.art` ou outra) → bloqueio absoluto, entrar em PENDENTE
- Reportar "publicado" sem URL → inválido

## Quality Criteria

- [ ] Dry-run executado antes de publicação real
- [ ] URLs retornadas para toda publicação bem-sucedida
- [ ] Estado PENDENTE usado corretamente quando a conta não é a oficial
