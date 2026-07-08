# Gestor Vila — Resumo do Sistema

## O que é

Sistema de gestão de social media e marketing para o **Vila Los Muertos de Fome**, restaurante Tex Mex BR em Bethaville, Barueri, SP. Rua Caldas Novas 49. Chef Alex Coelho. Aberto 7 dias. Música ao vivo qui-sáb 20h. Stand-up comedy, Copa 2026.

Construído no **Opensquad**, um framework de orquestração de agentes de IA. Cada agente tem uma persona, tasks e regras próprias. O pipeline executa os agentes em sequência.

---

## Hierarquia de Conteúdo (regra mais importante)

O **Google Agenda principal** (`losmuertosdefome@gmail.com`) é a fonte primária — define o conteúdo de cada dia. O calendário **Música e Eventos** é fonte secundária — fornece nome do artista e horário apenas.

O restaurante, a comida e a experiência são **sempre o protagonista**. Shows são um pilar de entretenimento, nunca o foco principal.

**NUNCA** expor cachê, custo de artista, valor de contrato em nenhum conteúdo ou campanha.

---

## Pilares de Conteúdo por Dia

| Dia | POST PRINCIPAL |
|-----|----------------|
| Segunda | Agenda da Semana |
| Terça | Rodízio v1 — cardápio, abundância |
| Quarta | Domínio Territorial — Vila como referência de Bethaville |
| Quinta | Rodízio v2 — experiência, preparo do Chef Alex |
| Sexta | Experiência Cultural — happy hour, clima, entretenimento |
| Sábado | Família — acolhimento, refeição compartilhada |
| Domingo | Aniversário — celebração, comunidade |

---

## Agentes

| Agente | Função |
|--------|--------|
| **Cris Criativa** | Copywriter — escreve todo o conteúdo orgânico (post feed + stories) |
| **Vito Visual** | Designer — cria artes para post, stories e anúncios |
| **Paulo Postador** | Publica nas plataformas (Instagram, TikTok, Facebook, iFood, Google Meu Negócio) |
| **Ana Anúncio** | Tráfego pago — briefing de campanhas Meta Ads + TikTok Ads |
| **Renata Revisão** | QA — verifica hard caps antes de publicar |
| **Rodrigo Resultados** | Relatórios de marketing — métricas, insights, ROI |

---

## Pipeline (9 steps)

```
Step 01 — Briefing do Dia     → lê Google Agenda, monta briefing
Step 02 — Criar Conteúdo      → Cris escreve copy de todos os slots
Step 03 — Criar Visual        → Vito cria as artes
Step 04 — Aprovação           → checkpoint com o usuário
Step 05 — Publicar            → Paulo publica nas plataformas
Step 06 — Criar Campanha      → Ana monta briefing de ads (condicional)
Step 07 — Revisão de Qualidade → Renata verifica hard caps
Step 08 — Relatório           → Rodrigo registra métricas
Step 09 — Aprovação Final     → checkpoint de encerramento
```

---

## Slots de Conteúdo Diário

Produzidos pelo Cris Criativa toda vez que o pipeline roda:

1. **POST PRINCIPAL** — feed Instagram + Facebook. Segue o pilar do dia. Show mencionado em no máximo uma linha, nunca como tema central.
2. **STORY 1** — engajamento 15s com pergunta interativa (enquete, slider, caixa).
3. **STORY 2** — informação 15s com detalhe concreto + CTA físico.
4. **STORY CHEF ALEX** — bastidor de cozinha 30s. Tom pessoal, sem CTA comercial. Recorrente todo dia.
5. **STORY SHOW** *(condicional — só quando há entretenimento)* — artista + horário + experiência. Nunca cachê.
6. **ANÚNCIO PAGO** *(condicional — só quando briefing.campanha_paga == SIM)* — dados para Ana Anúncio.

---

## Hard Caps (regras invioláveis do copy)

- **H1** — Zero marketing language: "confira", "venha nos visitar", "link na bio", "o melhor de Barueri" → reescrever
- **H2** — Todo story de show deve ter artista + horário + dia
- **H3** — CTA físico apenas: "vem", "reserva", "aparece", "chega" — nunca "clique", "acesse"
- **H4** — Nenhum valor financeiro interno: cachê, custo do artista, preço de contrato → VETO absoluto

---

## Tom de Voz (6 tons)

| Tom | Quando usar |
|-----|-------------|
| Acolhedor/Familiar | Domingo, família, feijoada |
| Animado/Festivo | Shows, stand-up, Copa, Samba |
| Gastronômico/Sensorial | Pratos, cardápio, Chef Alex |
| Cultural/Identitário | Identidade Tex Mex BR, Día de los Muertos |
| Comunitário/Local | Bethaville, Barueri, pertencimento |
| Urgente/FOMO | Copa, eventos esgotando, última hora |

Regras universais: sempre minúsculo (exceto nome próprio/artista), sem hashtags excessivos, máximo 2 emojis por post.

---

## Campanhas Pagas (Ana Anúncio)

Ativadas quando há: show com artista nomeado, Jogo do Brasil (Copa), Stand-up Comedy.

**Orçamento por tipo de evento** (não por cachê):

| Tipo | Meta Ads/dia | TikTok/dia | Duração |
|------|-------------|------------|---------|
| Show padrão | R$40 | R$25 | 2 dias |
| Show destaque | R$50 | R$30 | 2 dias |
| Copa do Mundo | R$60–80 | R$40 | 3 dias |
| Stand-up | R$35 | R$20 | 2 dias |
| Samba | R$30 | R$15 | 1-2 dias |

Geolocalização: raio 12km de Barueri (obrigatório). CTA padrão: Obter Trajeto.

---

## Google Agenda — Estrutura Real

O calendário principal tem ~250 eventos mapeados para mai-jun 2026. Cada dia tem:
- `[POST PRINCIPAL]` — categoria do post do feed
- `[STORY]` + `[STORY] Chef Alex Coelho` — stories do dia
- Datas comemorativas com relevância gastronômica
- Ações offline (feiras, panfletagem) — informativas, não entram no conteúdo digital

Calendário secundário: `8aae14c6f254952e7d792048ac23a573ce8e6b90fa32508f7ad832c49b335614@group.calendar.google.com`
Ler apenas: nome do artista + horário. Ignorar valores monetários nos títulos dos eventos.

---

## Brand Kit Canva

Brand Kit ID: `kAHGNC-y7zM` ("LOS MUERTOS") — obrigatório em toda geração de arte.

Assets:
- Logo com mascotes: `MAHGNLbQWgA`
- Logo texto: `MAHGNFlIHeA`
- Mascote cachorro: `MAHGNAoapdI`
- Mascote gato: `MAHGNL0Ig4Y`
- Post referência: `DAHGRk_auLQ`

Nunca usar brand kit "Perna de Porco + Texano".

---

## Dashboard (`pipeline-visual.html`)

Arquivo HTML interativo com 4 abas:
- **Semana** — visualização da semana com progresso de cada dia
- **Agentes** — cards com status de cada agente
- **Pipeline** — barra de progresso dos 9 steps
- **Campanhas** — gerenciador de campanhas pagas com CRUD completo

Campanhas salvas em `localStorage` (chave: `vila-campaigns`).
Botão "Refresh" no header: gera comando para sincronizar dados do Google Agenda no dashboard.

---

## Estrutura de Arquivos

```
squads/gestor-vila/
├── pipeline-visual.html          ← dashboard interativo
├── squad.yaml                    ← configuração do squad
├── agents/
│   ├── cris-criativa.agent.md
│   ├── cris-criativa/tasks/criar-conteudo-diario.md
│   ├── ana-anuncio.agent.md
│   ├── ana-anuncio/tasks/criar-campanha-evento.md
│   ├── vito-visual.agent.md
│   ├── paulo-postador.agent.md
│   ├── renata-revisao.agent.md
│   └── rodrigo-resultados.agent.md
├── pipeline/
│   ├── steps/step-01 ao step-09
│   └── data/
│       ├── vila-identity.md      ← identidade do restaurante
│       ├── tone-of-voice.md      ← 6 tons, frequência, regras
│       ├── output-examples.md    ← modelos de copy aprovados
│       └── anti-patterns.md      ← erros a evitar
└── output/
    └── YYYY-MM-DD-HHmmss/v1/
        ├── briefing.md
        ├── conteudo.md
        └── campanha.md
```

---

## O que ainda pode melhorar

- **Dashboard WEEK** — a constante `WEEK` no HTML ainda não reflete o calendário real com a hierarquia corrigida (comida primeiro, shows como contexto)
- **Copa do Mundo** — jogos do Brasil em 13, 19 e 24/jun precisam de tratamento especial no pipeline (prioridade máxima, dobra orçamento de campanha)
- **Vito Visual** — as tasks de criação de arte ainda não têm diretrizes visuais detalhadas por tipo de slot (story 15s vs. post feed vs. story show)
- **Output atual** (`output/2026-05-20-184155/`) — ainda foi gerado com a hierarquia errada (cachê visível, show como foco). Precisaria de um novo run para gerar output correto.
- **Integração real com plataformas** — Paulo Postador ainda não tem sessão autenticada para publicar automaticamente
