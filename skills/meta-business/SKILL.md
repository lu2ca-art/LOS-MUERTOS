---
name: meta-business
description: >
  Pull real performance metrics (reach, impressions, engagement, CPM, ad spend)
  from Meta Business Suite / Marketing API for organic posts and paid campaigns.
  PLACEHOLDER — not yet configured. Requires a Meta Business API access token
  from the user before this skill can be used.
description_pt-BR: >
  Puxa métricas reais de performance (alcance, impressões, engajamento, CPM, gasto)
  do Meta Business Suite / Marketing API para posts orgânicos e campanhas pagas.
  PLACEHOLDER — ainda não configurada. Precisa de um token de acesso à API do
  Meta Business fornecido pelo usuário antes de poder ser usada.
type: mcp
version: "0.1.0-placeholder"
mcp:
  server_name: meta-business
  command: npx
  args: ["-y", "meta-business-mcp"]
  transport: stdio
env:
  - META_BUSINESS_ACCESS_TOKEN
  - META_AD_ACCOUNT_ID
categories: [analytics, advertising, reporting]
status: placeholder
---

# Meta Business — Skill (Placeholder)

## Status: aguardando configuração

Esta skill ainda não está configurada. `META_BUSINESS_ACCESS_TOKEN` e `META_AD_ACCOUNT_ID` não estão definidos. Até serem fornecidos:

- **Rodrigo Resultados** (`squads/gestor-vila/agents/rodrigo-resultados`) avisa o usuário que a integração não está disponível e segue com dados de métrica informados manualmente.
- Nenhum outro agente depende desta skill.
- Nada no restante do squad quebra por causa dessa ausência.

## When to use (após configurada)

Use esta skill quando o Rodrigo Resultados precisar de métricas reais de posts orgânicos (Instagram/Facebook Insights) ou campanhas pagas (Meta Ads) em vez de dados informados manualmente pelo usuário.

## Instructions (após configurada)

1. Autenticar com `META_BUSINESS_ACCESS_TOKEN`.
2. Para posts orgânicos: consultar Instagram/Facebook Insights por post — alcance, impressões, engajamento.
3. Para campanhas pagas: consultar a Marketing API pelo `META_AD_ACCOUNT_ID` — investimento, alcance, impressões, CPM, cliques em CTA.
4. Retornar os dados brutos para o Rodrigo estruturar no relatório — esta skill não gera texto, só dados.

## Setup

1. Criar um app no [Meta for Developers](https://developers.facebook.com/).
2. Gerar um token de acesso de sistema (system user token) com permissões `ads_read`, `read_insights`, `pages_read_engagement`.
3. Obter o `META_AD_ACCOUNT_ID` no Meta Ads Manager.
4. Definir `META_BUSINESS_ACCESS_TOKEN` e `META_AD_ACCOUNT_ID` no ambiente (`.env` ou `.claude/settings.local.json`, conforme o mecanismo de configuração de MCP do projeto).
5. Reinstalar/resolver a skill — o runner do Opensquad detecta a configuração automaticamente na próxima execução.

## Nunca

- Nunca usar dados de cachê/custo de artista como métrica desta skill — ela só lida com performance de conteúdo e campanha, não com dados financeiros internos de contratação.
