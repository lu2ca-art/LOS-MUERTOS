---
step: 09
name: "Aprovação Final"
type: checkpoint
agent: inline
---

# Step 09 — Aprovação Final

## Objetivo

Encerramento formal da sessão. Apresentar resumo da sessão ao usuário e confirmar que o pipeline está completo.

## Instructions

Apresente o resumo da sessão ao usuário:

1. Listar todas as publicações feitas (URLs de `output/publicacoes.md`)
2. Mostrar o status final da revisão de Renata (`output/review.md`)
3. Se há `output/campanha.md`, resumir o briefing de campanha e lembrar que a ativação é manual
4. Se há `output/relatorio.md` (segunda-feira), destacar recomendações e alertas de oportunidade emitidos por Rodrigo

**Formato do resumo:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SESSÃO COMPLETA — Vila Los Muertos de Fome
  [DATA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PUBLICAÇÕES
  ✅ Instagram: [URL]
  ✅ Facebook: [URL]
  ✅ TikTok: [URL]
  ✅ Google Meu Negócio: [URL]

REVISÃO DE QUALIDADE
  Status: APROVADA
  [notas de destaque da Renata]

CAMPANHA PAGA (se aplicável)
  ⚠️ Briefing pronto em output/campanha.md
  Ativar manualmente no Meta Ads Manager:
  [data e hora de ativação recomendada]

RELATÓRIO DE MARKETING (se segunda-feira)
  [recomendações e alertas de Rodrigo Resultados]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Pergunte ao usuário usando AskUserQuestion se deseja:

- **Encerrar a sessão** — tudo certo, sessão completa
- **Ver o relatório de marketing** — solicitar Rodrigo Resultados (se não foi segunda-feira)
- **Ajustar algo** — indicar o que deve ser revisado

**Se o usuário encerrar:** confirmar sessão encerrada e atualizar `squads/gestor-vila/_memory/memories.md` com os aprendizados da sessão.
