---
id: step-07
type: agent
agent: rafael-repercussao
execution: subagent
model_tier: fast
name: "Adaptar Plataformas"
inputFile: output/conteudo-instagram.md
outputFile: output/adaptacoes.md
---

# Step 07 — Adaptar Plataformas

Rafael Repercussão recebe o conteúdo aprovado e produz versões nativas para cada plataforma solicitada no Step 06. Executa como subagent — trabalha em segundo plano enquanto o usuário aguarda. Nunca publica sem autorização explícita confirmada no checkpoint anterior.

## Context Loading

Rafael deve carregar:
1. `output/conteudo-instagram.md` (conteúdo aprovado de Carlos Caption)
2. `output/angulo-selecionado.md` (tom confirmado — deve ser preservado nas adaptações)
3. Resultado do Step 06 (plataformas confirmadas + status de publicação autorizada/rascunho)

## Instructions

Executar a task `tasks/adaptar-plataformas.md` para cada plataforma confirmada no Step 06.

**Protocolo de publicação (quando autorizado no Step 06):**
1. Dry-run: mostrar preview do que será publicado
2. Aguardar confirmação final do usuário
3. Publicar via skill `blotato`
4. Reportar URL do post publicado

**Quando publicação é "apenas rascunho":** Entregar todos os textos adaptados sem chamar `blotato`. Status = "rascunho — aguardando aprovação".

## Output Format

Ver `tasks/adaptar-plataformas.md` — Output Format section.

Consolidar em `output/adaptacoes.md`:

```
# Adaptações — [data da sessão]

[seções por plataforma]

## Status de Publicação
[plataforma]: [rascunho / publicado — URL]
```

## Veto Conditions

Não publicar se:
1. Step 06 definiu "APENAS RASCUNHO" — independentemente de qualquer instrução posterior na task
2. URL não foi retornada pelo blotato — publicação não confirmada sem URL

## Quality Criteria

- [ ] Todas as plataformas confirmadas no Step 06 têm adaptação
- [ ] lu2ca.art mencionado em toda adaptação
- [ ] Newsletter tem "com amor, LU2CA"
- [ ] Status de publicação registrado para cada plataforma
- [ ] Output salvo em `output/adaptacoes.md`
