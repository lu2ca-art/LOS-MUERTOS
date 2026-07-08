---
id: step-01
type: checkpoint
name: "Contexto da Sessão"
outputFile: output/contexto.md
---

# Step 01 — Contexto da Sessão

Ponto de entrada da sessão. O usuário preenche o briefing — era atual, mood, próximos lançamentos, últimos posts e formatos desejados. Bruno Brainstorm só avança após este contexto estar preenchido.

## Instructions

Perguntar ao usuário (via AskUserQuestion ou texto direto):

1. **Era e mood:** Qual a era atual? Qual o mood da semana? (ex: "era CIDADE NEON, semana de lançamento iminente")
2. **Próximos lançamentos:** Há algum lançamento nos próximos 7-14 dias?
3. **Últimos posts:** O que foi postado nos últimos 7 dias? Quais performaram melhor?
4. **Formatos desejados:** Quais formatos para esta sessão? (Reel, feed, Stories, combinação?)
5. **Plataformas adicionais:** Alguma adaptação além do Instagram? (Twitter, newsletter, YouTube?)

## Output Format

```
=== CONTEXTO DA SESSÃO ===
Era: [era atual]
Mood: [humor/energia da semana]
Lançamento próximo: [sim — [nome] em [prazo] / não]
Últimos posts: [lista breve]
Formatos: [lista dos formatos solicitados]
Plataformas adicionais: [lista ou "apenas Instagram"]
```

## Output Example

```
=== CONTEXTO DA SESSÃO ===
Era: CIDADE NEON
Mood: semana de movimento — energia alta antes do lançamento
Lançamento próximo: sim — 'CHUVA' em 5 dias
Últimos posts: carrossel filosófico (3 dias atrás, 67 curtidas), Story de enquete (2 dias)
Formatos: Reel principal + feed de suporte + Stories (3-4 frames)
Plataformas adicionais: newsletter para a tripulação
```

## Veto Conditions

Não avançar para o Step 02 se:
1. Formato desejado não foi especificado — Bruno Brainstorm precisa dessa informação para calibrar os ângulos
2. Era atual não foi confirmada — o vocabulário ativo depende da era

## Quality Criteria

- [ ] Todos os 5 campos preenchidos (era, mood, lançamento, últimos posts, formatos)
- [ ] Plataformas adicionais confirmadas (mesmo que seja "apenas Instagram")
- [ ] Output salvo em `output/contexto.md`
