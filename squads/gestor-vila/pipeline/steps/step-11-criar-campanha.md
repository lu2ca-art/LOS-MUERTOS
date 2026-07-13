---
id: step-11
type: agent
agent: ana-anuncio
execution: subagent
model_tier: powerful
name: "Criar Campanha de Anúncios"
inputFile: output/conteudo.md
outputFile: output/campanha.md
---

# Step 11 — Criar Campanha de Anúncios

## Context Loading

Ana carrega: `output/conteudo.md` (seção ANÚNCIO PAGO, quando existir), `output/arte-evento.jpg` (quando existir), `pipeline/data/research-brief.md`.

## Instructions

Este step só roda quando `plano.inclui_trafego_pago == true` — sempre por pedido explícito do usuário, nunca por classificação automática de evento ou cachê.

1. Se há evento de calendário associado, extrair parâmetros de `conteudo.md`.
2. Se não há (campanha solicitada sem evento de calendário), perguntar diretamente: público-alvo, verba, objetivo.
3. Definir orçamento por tipo de evento (tabela oficial) — nunca por cachê.
4. Definir segmentação completa (raio, idade, interesses).
5. Montar os dois briefings (Meta Ads e TikTok Ads).

## Output Format

Ver `tasks/criar-campanha-evento.md` — Formato de Saída.

## Output Example

```markdown
# Briefing de Campanha — RUNA — sexta 18/07

**Tipo de campanha:** show ao vivo — padrão
**Foco:** experiência Vila — nacho, drinks, RUNA ao vivo

## META ADS
**Geolocalização:** Raio 12km de Barueri
**Idade:** 25-45 anos
**Orçamento:** R$40/dia · 2 dias · Total R$80
**CTA:** Obter Trajeto

## RESUMO FINANCEIRO
| Meta Ads | R$40/dia | 2d | R$80 |
| TikTok | R$25/dia | 2d | R$50 |
| **TOTAL** | | | **R$130** |
```

## Veto Conditions

- Campanha sem raio de geolocalização → VETO
- Qualquer valor de cachê ou custo de artista no briefing → VETO absoluto
- Campanha criada sem pedido explícito do usuário → bloqueio

## Quality Criteria

- [ ] Raio ≤ 15km de Barueri
- [ ] Orçamento por tipo de evento, nunca por cachê
- [ ] CTA físico (Obter Trajeto/Reservar)
- [ ] Briefing TikTok separado do Meta Ads
