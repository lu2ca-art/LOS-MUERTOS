---
step: 08
name: "Relatório de Marketing"
type: reporting
agent: rodrigo-resultados
execution: inline
condition: "dia_da_semana == 'segunda' OR solicitado_explicitamente == true"
---

# Step 08 — Relatório de Marketing

## Objetivo

Rodrigo Resultados analisa a performance de tudo que foi publicado e impulsionado na semana anterior e entrega recomendações para a próxima.

## Agente Ativo

**Rodrigo Resultados** — Analista de Marketing Vila

## Condição de Execução

Este step só roda se:
- Hoje é segunda-feira, OU
- O usuário solicitou explicitamente o relatório

Em outros dias de pipeline normal, este step é pulado e a execução vai direto para Step 09.

## Tasks

Executar `agents/rodrigo-resultados/tasks/relatorio-marketing.md`:

1. Levantar publicações da semana anterior de `output/publicacoes.md`
2. Coletar métricas de performance (alcance, engajamento) por plataforma — quando disponíveis
3. Analisar stories separadamente do feed
4. Analisar campanhas pagas de `output/campanha.md` se houve
5. Identificar top 3 conteúdos da semana com justificativa
6. Comparar com semana anterior se houver histórico (ou documentar como baseline)
7. Redigir mínimo 3 recomendações acionáveis direcionadas a agentes específicos
8. Projetar próxima semana com alertas de oportunidade (Copa, artista especial)
9. Documentar dados ausentes e onde coletá-los
10. Salvar em `output/relatorio.md`

## Output Esperado

- `output/relatorio.md` com análise de performance + recomendações

## Prosseguir para Step 09 — Aprovação Final.
