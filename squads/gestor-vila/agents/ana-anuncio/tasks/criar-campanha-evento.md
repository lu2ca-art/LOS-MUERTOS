---
task: "Criar Campanha de Evento"
order: 1
input: |
  - conteudo: output/{projeto}/conteudo.md — seção ANÚNCIO PAGO com headlines e contexto
  - arte: output/{projeto}/arte-evento.jpg — visual 1080×1080px aprovado
  - research: pipeline/data/research-brief.md — contexto restaurante e público
output: |
  - file: output/{projeto}/campanha.md — briefing completo de campanha Meta Ads + TikTok Ads
---

# Criar Campanha de Evento

## Descrição

Ana monta o briefing completo de campanha para Meta Ads (Instagram + Facebook) e TikTok Ads. O foco é atrair pessoas para viver a experiência da Vila — comida, ambiente, entretenimento. Geolocalização é o primeiro filtro — campanhas fora do raio de Barueri são dinheiro desperdiçado. O artista é um argumento de atração, nunca o produto da campanha.

## Gatilho

Esta task roda APENAS quando `output/{projeto}/conteudo.md` contém seção `## ANÚNCIO PAGO`. Sem essa seção, não há campanha.

## Processo

### 1. Identificar parâmetros do evento

Do `output/{projeto}/conteudo.md`, seção ANÚNCIO PAGO:
- Evento âncora + data + horário
- Tipo de campanha (show ao vivo / Copa / stand-up / data comemorativa)
- Público-alvo indicado por Cris Criativa
- Headlines disponíveis (3 variações)

**Ignorar completamente:** qualquer referência a valores de cachê, custo de artista, ou informações financeiras internas — não são dados de campanha.

### 2. Definir orçamento por tipo de evento

| Tipo de evento              | Meta Ads/dia | TikTok/dia | Duração |
|-----------------------------|--------------|------------|---------|
| Show ao vivo — padrão       | R$40         | R$25       | 2 dias  |
| Show ao vivo — destaque*    | R$50         | R$30       | 2 dias  |
| Copa do Mundo (jogo Brasil) | R$60–80      | R$40       | 3 dias  |
| Stand-up Comedy             | R$35         | R$20       | 2 dias  |
| Samba / Evento recorrente   | R$30         | R$15       | 1-2 dias|
| Data comemorativa gastronômica | R$25      | —          | 1 dia   |

*Show destaque: artista com forte presença regional ou público confirmado acima da média — critério baseado em histórico de lotação, não em cachê.

### 3. Definir segmentação completa

**Geolocalização (OBRIGATÓRIA):**
- Centro: Barueri, SP (ou coordenadas da Vila: Rua Caldas Novas 49)
- Raio: 12km (padrão) — máx 15km
- Excluir: zonas industriais fora do perímetro residencial

**Idade e gênero:**
- Show MPB/indie: 25-45 anos, todos os gêneros
- Copa do Mundo: 18-55 anos, todos os gêneros
- Stand-up: 22-40 anos, todos os gêneros
- Show sertanejo/pop: 20-50 anos, todos os gêneros

**Interesses por tipo de evento:**

| Evento          | Interesses primários                                   | Interesses secundários              |
|-----------------|--------------------------------------------------------|-------------------------------------|
| Show ao vivo    | Música ao Vivo, Shows e Concertos, Entretenimento      | Restaurantes, Bar, Gastronomia      |
| Copa do Mundo   | Futebol, Copa do Mundo FIFA, Brasil, Seleção Brasileira| Bares esportivos, Cerveja           |
| Stand-up        | Comédia Stand-up, Humor, Entretenimento                | Restaurantes, Teatro                |
| Feijoada/Especial| Gastronomia Brasileira, Culinária, Restaurantes       | Família, Domingo, Cultura BR        |

**Comportamentos (Meta Ads):**
- Pessoas que viajam com frequência (turistas no raio)
- Engajados com páginas locais de Barueri/Bethaville
- Usuários que visitaram locais próximos (Custom Audience quando disponível)

### 4. Definir duração e timing

| Evento          | Início da campanha        | Duração total     | Pico de orçamento        |
|-----------------|---------------------------|-------------------|--------------------------|
| Show (qui-sáb)  | 48h antes                 | 2-3 dias          | Dia do show (dobrar bid) |
| Copa            | 72h antes                 | 3-4 dias          | Dia do jogo (dobrar bid) |
| Stand-up        | 48h antes                 | 2 dias            | Dia do evento            |
| Especial semanal| 24h antes                 | 1-2 dias          | Dia do evento            |

### 5. Montar briefing completo

Dois briefings separados: Meta Ads e TikTok Ads.

**Meta Ads (Instagram + Facebook):**
- Objetivo: Alcance ou Consideração local
- Posicionamento: Instagram Feed + Instagram Stories + Facebook Feed
- CTA: Obter Trajeto (preferencial) ou Reservar
- Visual: `output/{projeto}/arte-evento.jpg`
- Headlines: 3 variações (A/B/C testing)

**TikTok Ads:**
- Objetivo: Alcance Local
- Formato: TopView ou In-Feed Ad
- CTA: Obter Trajeto
- Criativo: adaptar arte-evento.jpg para 9:16 (indicar que adaptação é necessária)
- Note: TikTok Ads para negócios locais pequenos — testar com orçamento menor

## Formato de Saída

```markdown
# Briefing de Campanha — [EVENTO] — [DATA]

**Criado por:** Ana Anúncio
**Data de criação:** [data]
**Evento âncora:** [evento + data + horário]
**Tipo de campanha:** [show ao vivo / Copa / stand-up / data comemorativa]
**Foco:** experiência Vila — comida + [entretenimento ao vivo / jogo / comedy]

---

## META ADS — Instagram + Facebook

### Configuração Geral
- **Objetivo:** Alcance / Consideração local
- **Conta:** Vila Los Muertos de Fome
- **Visual:** output/{projeto}/arte-evento.jpg (1080×1080px)

### Segmentação
- **Geolocalização:** Raio [X]km de Barueri, SP (Rua Caldas Novas 49)
- **Idade:** [faixa]
- **Gênero:** Todos
- **Interesses:** [lista]
- **Comportamentos:** [lista]

### Budget
- **Orçamento diário:** R$[valor]/dia
- **Duração:** [X] dias ([data início] → [data fim])
- **Total estimado:** R$[valor total]

### Anúncio
- **Headline 1 (A):** [≤40 chars]
- **Headline 2 (B):** [≤40 chars]
- **Headline 3 (C):** [≤40 chars]
- **Primary text (A):** [≤125 chars]
- **Primary text (B):** [≤125 chars]
- **CTA:** Obter Trajeto / Reservar

### Timing de Ativação
- **Ativar em:** [data e hora exata — ex: "quinta 21 mai às 21h"]
- **Pausar em:** [data e hora exata — ex: "sexta 22 mai às 23h59"]

---

## TIKTOK ADS

### Configuração Geral
- **Objetivo:** Alcance Local
- **Formato:** In-Feed Ad
- **Visual:** Adaptar arte-evento.jpg para 9:16 (indicar para Vito se necessário)

### Segmentação
- **Localização:** Barueri, SP — raio [X]km
- **Idade:** [faixa]
- **Interesses:** [lista TikTok-específica]

### Budget
- **Orçamento diário:** R$[valor]/dia
- **Duração:** [X] dias
- **Total estimado:** R$[valor total]

### Timing de Ativação
- **Ativar em:** [data e hora]

---

## RESUMO FINANCEIRO

| Plataforma   | Orçamento/dia | Dias | Total    |
|--------------|---------------|------|----------|
| Meta Ads     | R$[X]         | [X]  | R$[X]    |
| TikTok Ads   | R$[X]         | [X]  | R$[X]    |
| **TOTAL ADS**|               |      | **R$[X]**|

---

## ALERTA DE OPORTUNIDADE
[Incluir se Copa, artista com forte histórico de público, ou data comemorativa estratégica]
```

## Exemplo de Saída

**Contexto:** LU2CA ao vivo, sábado 30/05 (show destaque — histórico de público)

```markdown
# Briefing de Campanha — LU2CA — sábado 30/05

**Tipo de campanha:** show ao vivo — destaque
**Foco:** experiência Vila — nacho, drinks, e LU2CA ao vivo

## META ADS

**Geolocalização:** Raio 12km de Barueri, SP
**Idade:** 25-45 anos
**Interesses:** LU2CA, Música ao Vivo, MPB, Pop Alternativo, Restaurantes
**Orçamento:** R$50/dia · 2 dias (sex 29/mai → sab 30/mai) · Total R$100
**Headline A:** LU2CA ao vivo na Vila — sábado
**Headline B:** Sábado tem LU2CA. Bethaville. 20h.
**Primary text A:** LU2CA ao vivo. Nacho, drinks e muito show. Sábado, 20h. Rua Caldas Novas 49.
**Primary text B:** O sábado pediu show. LU2CA começa às 20h na Vila. Chega antes.
**CTA:** Obter Trajeto
**Ativar:** qui 28/mai às 20h · **Pausar:** sab 30/mai às 23h59

## RESUMO FINANCEIRO
| Meta Ads | R$50/dia | 2d | R$100 |
| TikTok   | R$30/dia | 2d | R$60  |
| **TOTAL**|          |    | **R$160** |
```

## Critérios de Qualidade

- [ ] Raio de geolocalização ≤ 15km de Barueri
- [ ] Evento específico como âncora da campanha
- [ ] Copy foca na experiência da Vila (comida + entretenimento) — nunca no artista isolado
- [ ] Orçamento definido por tipo de evento (tabela acima) — sem referência a cachê
- [ ] CTA físico (Obter Trajeto ou Reservar)
- [ ] Interesses segmentados para o tipo de evento
- [ ] Timing de ativação especificado com data e hora exatos
- [ ] Briefing TikTok separado do Meta Ads
- [ ] Resumo financeiro apenas com investimento em ads — sem valores de cachê ou contrato

## Condições de Veto

- **Campanha sem raio de geolocalização** → VETO, nenhuma campanha sem raio definido
- **CTA "Saiba Mais"** → substituir por Obter Trajeto
- **Valor de cachê ou custo de artista no briefing** → VETO absoluto — remover antes de entregar
- **Copy centrado no artista sem mencionar comida/experiência** → reescrever — o Vila é protagonista
- **Duração > 4 dias para show semanal** → encurtar, desperdício após o evento
