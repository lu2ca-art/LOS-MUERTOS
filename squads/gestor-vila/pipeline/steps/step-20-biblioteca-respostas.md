---
id: step-20
type: agent
agent: rita-resposta
execution: inline
model_tier: powerful
name: "Criar Biblioteca de Respostas"
outputFile: output/biblioteca-respostas.md
---

# Step 20 — Criar Biblioteca de Respostas

## Context Loading

Rita carrega: `pipeline/data/vila-identity.md`, `pipeline/data/tone-of-voice.md`, `pipeline/data/biblioteca-respostas-atual.md` (versão anterior, quando existir).

## Instructions

Este step só roda quando `plano.tipo_projeto == 'biblioteca_respostas'` — por pedido explícito do usuário.

1. Executar `tasks/criar-biblioteca-respostas.md` na íntegra.
2. Se há biblioteca anterior, atualizar em vez de recomeçar do zero.
3. Cobrir as categorias mais frequentes primeiro (reserva, horário, cardápio, localização).
4. Definir direcionamento claro pra reclamação e casos fora do padrão — nunca resposta genérica forçada.
5. Salvar o artefato do projeto e sobrescrever `pipeline/data/biblioteca-respostas-atual.md`.

## Output Format

Ver `tasks/criar-biblioteca-respostas.md` — Formato de Saída.

## Output Example

```markdown
# Biblioteca de Respostas — Instagram Vila

**Atualizado em:** 15/07/2026

## Reserva
**Pergunta típica:** "vocês têm reserva?"
**Resposta:** vem sim! a gente não trabalha com reserva formal, mas se for grupo grande (8+) manda mensagem que a gente se organiza pra te receber bem.

## Horário
**Pergunta típica:** "que horas vocês abrem?"
**Resposta:** funcionamos todo dia, a partir das 12h. quinta, sexta e sábado tem show ao vivo às 20h.

## Reclamação
**Situação típica:** cliente insatisfeito
**Direcionamento:** responder "poxa, sentimos muito — conta pra gente o que aconteceu por aqui no direct?" e encaminhar pra conversa direta. Nunca resolver publicamente no comentário.
```

## Veto Conditions

- Resposta vaga pra pergunta objetiva (horário, endereço) → reescrever com informação concreta
- Reclamação com resposta genérica forçada em vez de direcionamento → VETO
- Qualquer valor de cachê presente → VETO absoluto

## Quality Criteria

- [ ] Categorias mais frequentes cobertas
- [ ] Toda resposta tem informação concreta
- [ ] Direcionamento claro pra reclamação e casos grandes
- [ ] Arquivo persistente `biblioteca-respostas-atual.md` atualizado
