---
task: "Relatório de Marketing Semanal"
order: 1
input: |
  - publicacoes: output/{projeto}/publicacoes.md — posts do período com URLs
  - campanha: output/{projeto}/campanha.md — campanhas pagas do período (se houver)
  - metricas: via skill meta-business (quando configurada) ou informadas manualmente pelo usuário
output: |
  - file: output/{projeto}/relatorio.md — relatório de performance de marketing
---

# Relatório de Marketing

## Descrição

Rodrigo analisa a performance de tudo que foi publicado e impulsionado no período — orgânico e pago — e entrega direção com recomendações específicas por agente. Roda **apenas quando o usuário pede um projeto de relatório** — não existe execução automática por dia da semana.

## Fonte de dados — Meta Business (placeholder)

Rodrigo usa a skill `meta-business` para puxar métricas reais automaticamente. **Enquanto essa skill não estiver configurada** (depende de credenciais que o usuário vai fornecer):
- Rodrigo avisa: "Integração Meta Business ainda não configurada — informe os dados manualmente ou configure a skill para puxar automaticamente."
- Segue com dados fornecidos manualmente pelo usuário como alternativa temporária, registrando claramente quais números vieram de qual fonte.
- Assim que a skill estiver configurada, passa a puxar os dados automaticamente sem mudança de processo.

## Processo

### 1. Levantar publicações do período

De `output/{projeto}/publicacoes.md`, listar todos os posts publicados com:
- Plataforma
- Tipo de conteúdo (show, gastronomia, bastidor, Copa, etc.)
- Data e horário de publicação
- URL

Registrar para cada post (via skill `meta-business` quando configurada, ou manualmente):
- **Alcance:** pessoas únicas que viram
- **Impressões:** visualizações totais
- **Engajamento:** curtidas + comentários + compartilhamentos + salvamentos
- **Taxa de engajamento:** engajamento / alcance × 100

Se métricas não estão disponíveis por nenhuma das duas vias, registrar como "dado não coletado" e indicar onde coletar (Instagram Insights, Meta Business Suite, TikTok Analytics).

### 2. Analisar performance de stories separadamente

Stories têm métricas distintas do feed:
- **Views:** visualizações únicas por story
- **Toque para frente:** usuário pulou — conteúdo não engajou
- **Toque para trás:** usuário voltou — conteúdo interessou
- **Saída:** usuário fechou o app — conteúdo perdeu a atenção
- **Resposta / Enquete:** interação direta

Separar análise de stories da análise de feed.

### 3. Analisar campanhas pagas (se houve)

De `output/campanha.md` da semana, para cada campanha rodada:
- Plataforma (Meta Ads / TikTok Ads)
- Evento âncora
- Orçamento investido
- Alcance obtido
- Impressões
- CPM (custo por mil impressões) = orçamento / impressões × 1000
- Cliques em CTA (Obter Trajeto / Reservar) — se disponível

Se os dados reais das campanhas não estão disponíveis, registrar orçamento investido e indicar onde coletar os resultados (Meta Ads Manager, TikTok Ads Manager).

### 4. Identificar top 3 conteúdos da semana

Ranquear por taxa de engajamento (ou alcance se engajamento não disponível). Identificar:
- O que funcionou: tipo de conteúdo, horário, evento
- O padrão: stories com enquete vs. feed estático, show vs. gastronomia, etc.

### 5. Comparar com semana anterior (se houver histórico)

Se há `output/relatorio.md` de semanas anteriores:
- Comparar alcance médio por post
- Comparar taxa de engajamento média
- Comparar alcance de campanhas pagas (CPM melhorou ou piorou?)

Se não há histórico, esta é a semana base. Documentar como "semana 1 — baseline".

### 6. Redigir recomendações

Mínimo 3 recomendações, cada uma direcionada a um agente:

**Para Cris Criativa:** tipo de copy/formato que performou melhor
**Para Vito Visual:** elementos visuais com maior engajamento
**Para Ana Anúncio:** ajuste de segmentação ou timing de campanhas

Recomendação precisa ter:
- O dado que justifica
- A ação específica
- Para quem

Exemplo: "Taxa de engajamento de stories com enquete foi 2× maior que stories informativos. **Cris:** incluir elemento interativo nos próximos 3 stories de show."

### 7. Projeção / alertas para próxima semana

- Quais eventos do próximo período têm maior potencial de alcance
- Sinalizar oportunidades para o usuário decidir se quer pedir uma campanha — nunca recomendar ativação automática por cachê ou valor
- Copa do Mundo ou outro evento de alto potencial — se próximo, emitir **ALERTA DE OPORTUNIDADE**

## Formato de Saída

```markdown
# Relatório de Marketing — Semana [DD/MM → DD/MM/AAAA]

**Gerado em:** [data] (segunda-feira)
**Por:** Rodrigo Resultados

---

## PERFORMANCE ORGÂNICA — FEED

| Post              | Plataforma  | Tipo        | Data  | Alcance | Engajamento | Taxa Eng. |
|-------------------|-------------|-------------|-------|---------|-------------|-----------|
| [post]            | Instagram   | [tipo]      | [data]| [X]     | [X]         | [X]%      |
| ...               |             |             |       |         |             |           |
| **MÉDIA**         |             |             |       | [X]     | [X]         | [X]%      |

*Dado não coletado: [listar posts sem métricas e onde coletar]*

---

## PERFORMANCE ORGÂNICA — STORIES

| Story             | Plataforma | Views | Toque frente | Toque trás | Saída | Interação |
|-------------------|------------|-------|--------------|------------|-------|-----------|
| [story]           | Instagram  | [X]   | [X]%         | [X]%       | [X]%  | [X]       |

---

## CAMPANHAS PAGAS

| Campanha          | Plataforma | Investido | Alcance | Impressões | CPM    |
|-------------------|------------|-----------|---------|------------|--------|
| [evento]          | Meta Ads   | R$[X]     | [X]     | [X]        | R$[X]  |
| **TOTAL**         |            | R$[X]     | [X]     |            |        |

---

## TOP 3 CONTEÚDOS DA SEMANA

1. **[post]** — [motivo: taxa de engajamento X%, alcance Y, horário Z]
2. **[post]** — [motivo]
3. **[post]** — [motivo]

**Padrão identificado:** [o que esses 3 têm em comum]

---

## COMPARAÇÃO COM SEMANA ANTERIOR

| Métrica               | Semana passada | Semana anterior | Variação |
|-----------------------|----------------|-----------------|----------|
| Alcance médio/post    | [X]            | [X]             | [+/-X%]  |
| Taxa de engajamento   | [X]%           | [X]%            | [+/-X%]  |
| CPM médio (ads)       | R$[X]          | R$[X]           | [+/-X%]  |

*Se primeira semana: dados desta semana são o baseline.*

---

## RECOMENDAÇÕES

### Para Cris Criativa
[dado] → [ação específica]

### Para Vito Visual
[dado] → [ação específica]

### Para Ana Anúncio
[dado] → [ação específica]

---

## PRÓXIMA SEMANA

| Evento              | Data   | Potencial  | Recomendação                     |
|---------------------|--------|------------|----------------------------------|
| [evento]            | [data] | Alto/Médio | Ativar campanha [X] dias antes  |

## ALERTA DE OPORTUNIDADE
[Incluir se Copa, artista especial, ou semana de alto potencial]

---

## DADOS AUSENTES
[Listar métricas não coletadas e onde buscá-las]
```

## Exemplo de Saída

```markdown
# Relatório de Marketing — Semana 11/05 → 17/05/2026

## PERFORMANCE ORGÂNICA — FEED

| Post           | Plataforma | Tipo  | Data  | Alcance | Eng. | Taxa  |
|----------------|------------|-------|-------|---------|------|-------|
| RUNA ao vivo   | Instagram  | show  | 14/05 | 1.840   | 147  | 8,0%  |
| Domingo feijoada| Instagram | gast. | 17/05 | 980     | 62   | 6,3%  |
| LU2CA - sáb    | Instagram  | show  | 16/05 | 4.200   | 504  | 12,0% |
| **MÉDIA**      |            |       |       | 2.340   | 238  | 8,8%  |

## TOP 3 CONTEÚDOS

1. **LU2CA sáb** — 12% engajamento, 4.200 alcance (2× a média)
2. **RUNA qui** — 8% engajamento, acima da média de shows regulares
3. **Feijoada dom** — menor alcance, mas salvamentos acima do esperado

**Padrão:** posts de artistas com nome conhecido superam shows regulares em 2-3×.

## RECOMENDAÇÕES

### Para Cris Criativa
LU2CA gerou 2× mais engajamento com copy direto (nome na primeira linha). Replicar estrutura: nome do artista na linha 1, horário na linha 2.

### Para Vito Visual
Visual do LU2CA com bloco terracota puro teve salvamentos 3× acima da média. Testar variação similar para DHARA no sábado seguinte.

### Para Ana Anúncio
CPM da campanha LU2CA ficou R$8,40 — 15% abaixo do esperado. Sugestão: mesmo segmento (25-45, raio 12km, interesse em MPB) para próximas campanhas de artistas similares.

## 🚨 ALERTA DE OPORTUNIDADE
**DHARA — sáb 23/05:** baseado na performance do LU2CA, estimar alcance 3.000-5.000 com campanha equivalente. Recomendar orçamento R$50/dia Meta Ads, ativar qui 21/05.
```

## Critérios de Qualidade

- [ ] Performance de cada publicação listada (com dados ou como "ausente")
- [ ] Stories analisados separadamente do feed
- [ ] Campanhas pagas com investimento e resultado (ou "dados não coletados")
- [ ] Top 3 conteúdos com justificativa baseada em dados
- [ ] Comparação com semana anterior (ou baseline documentado)
- [ ] Mínimo 3 recomendações acionáveis por agente
- [ ] Projeção de próxima semana com alertas
- [ ] Dados ausentes documentados

## Condições de Veto

- **Recomendação sem dado que justifica** → reescrever com métrica real
- **"Performance excelente" sem número** → substituir por dado concreto
- **Relatório sem recomendações** → incompleto, não salvar
- **Métricas inventadas** → remover e registrar como dado ausente
