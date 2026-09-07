# Gestor Vila — Resumo do Sistema (v2)

## 🟢 Meta de 50 categorias atingida (2026-07-16)

**Trabalho ativo:** `pipeline/data/biblioteca-respostas-atual.md` (Rita Resposta) — meta de ~50 categorias no público geral **atingida**.

- **Status atual: 50 categorias** no público geral (segmento A) + 4 institucionais (B-E) = 54 total. Trajetória: 30 (início) → 35 (mineração Apify 2026-07-15) → 41 (brainstorm com o usuário) → **50 (cardápio oficial 2026 incorporado, 2026-07-16)**.
- **Apify validado e usado a fundo em 2026-07-15** (`APIFY_TOKEN` em `.env`, servidor MCP `apify` registrado — ver `claude mcp list`). Fontes mineradas: Instagram, Facebook, Google Maps (500 avaliações — a fonte mais rica), Restaurant Guru, abillion.com. iFood e TripAdvisor não deram certo (bloqueio anti-bot / página inexistente).
- **Cardápio oficial 2026 (PDF, 4 páginas) recebido do usuário em 2026-07-16** — resolveu a maior pendência aberta (lista completa e atual do cardápio à la carte) e confirmou o preço do rodízio (R$98/108, batendo com o que já estava registrado). Todas as seções de cardápio da biblioteca foram reescritas com dados oficiais confirmados, substituindo estimativas baseadas em reviews. 9 categorias novas de cardápio/bebidas nasceram direto do PDF: Comida Mexicana Avulsa, Combos, Hambúrgueres Artesanais, Lanches Rústicos, Porções para Compartilhar, Sobremesas, Bebidas Não Alcoólicas, Drinks/Coquetéis, Chopp e Cerveja.
- **Relatório operacional separado entregue:** `output/relatorio-operacional-avaliacoes-2026-07-15.md` — cobre pico recente de 1★ (44% do histórico em 4 meses, possível problema operacional atual), site oficial fora do ar, possível unidade "Beach" (usuário confirmou que fechou há 2 meses — não mencionar mais), uso do espaço por eventos de terceiros, cardápio desatualizado no abillion, horário divergente entre fontes.
- **Página HTML interativa criada e aprovada pelo usuário:** sumário copiável da biblioteca inteira, com busca, índice e botão de copiar por caixa de texto. Publicada como Artifact (link privado do usuário) e também salva no repo em `output/biblioteca-respostas/pagina-interativa.html` pra persistir entre sessões. Pra atualizar depois de mudanças na `.md`: editar esse HTML e rodar o Artifact tool de novo apontando pro mesmo arquivo (mantém a mesma URL).
- **Pendências que continuam abertas** (ver seção Pendências no arquivo da biblioteca): valores do voucher de aniversário, detalhes do novo sistema de delivery (previsto pra até final de agosto/2026), "hambúrguer de grão de bico" (mencionado em reviews antigas, sumiu do cardápio oficial — confirmar com usuário), "Cone de Banana da Terra" desatualizado no abillion.com, transmissão de jogos/conteúdo (checar licenciamento com jurídico/contábil), espaço pra eventos de terceiros (parcerias com igreja são privadas, não divulgar).
- **Atualização 2026-07-16 (mesma sessão, depois de bater a meta):** usuário decidiu que pendências abertas (voucher, delivery, etc.) não bloqueiam mais o atendimento — viram "encaminhar pra pessoa responsável" quando perguntadas. Adicionada categoria **51 — "Fora do Escopo / Encaminhar pro Atendente"**, o fallback padrão pra qualquer pergunta sem categoria própria (inclusive a decisão de não tocar no assunto de licenciamento de transmissão). Total agora: **51 categorias no público geral**.
- **Página HTML ganhou uma aba "+ Adicionar Categoria"** — formulário pra criar categorias novas direto na página, salvas via `localStorage` (só no navegador de quem usa, não sincroniza entre pessoas) com botão de exportar em Markdown pra colar numa conversa e tornar oficial. Documentado dentro da própria página que é um rascunho local, não a fonte oficial.
- **Usuário perguntou sobre automação** (transformar a biblioteca num sistema de resposta automático de verdade no Instagram) — ainda é só uma exploração, nada decidido/construído. Recomendação dada: começar só por DM (não comentário público), via Instagram Messaging API + matching simples contra as "Perguntas típicas" da biblioteca, com fallback obrigatório pra "Fora do Escopo"/atendimento humano em qualquer caso de baixa confiança ou reclamação. Vale retomar esse assunto com mais profundidade numa sessão futura se o usuário confirmar interesse.
- **Automação em construção (2026-07-16, mesma sessão):** usuário confirmou que quer instalar mesmo sabendo dos riscos. Código em `squads/gestor-vila/automacao-instagram/`: parser que converte a biblioteca `.md` em JSON (`scripts/parse-biblioteca.js` → `data/biblioteca.json`, 55 categorias) e matching por palavra-chave testado contra frases reais.
  - **Pivotou de Vercel pra Cloudflare Workers em 2026-07-16** — Vercel travou numa permissão de conta ("você não tem permissão pra criar projeto"); usuário então pediu explicitamente a opção mais barata e segura, e confirmou Cloudflare Workers depois de eu explicar o porquê (gratuito no volume de um restaurante, sem servidor próprio exposto, TLS gerenciado). Código reescrito pro runtime de Workers (`src/worker.js` + `src/match.js`, ES modules, Web Crypto em vez do `crypto` do Node) — arquivos antigos da tentativa Vercel (`api/`, `lib/`, `public/`) foram removidos.
  - **Testado localmente com `wrangler dev` e passou:** verificação do Meta (GET), resposta de reserva (POST), e reclamação caindo certinho no log `NEEDS_HUMAN` com o texto seguro (sem vazar "escalar pro Lucas").
  - **Bloqueio atual: falta autenticação.** `wrangler` (CLI da Cloudflare) está instalado mas não logado — rodar `npx wrangler login` é ação que só o usuário pode fazer (login/criação de conta). Depois disso, o deploy (`npx wrangler deploy`) já está pronto pra rodar.
  - **Depois do deploy:** ainda falta a parte que só o usuário pode fazer — configurar os 3 segredos via `wrangler secret put` (`VERIFY_TOKEN`, `PAGE_ACCESS_TOKEN`, `APP_SECRET`, nunca colados no chat), e conectar o Instagram Business ao App do Meta (criar app, adicionar a própria conta como testadora — não precisa App Review — gerar token, registrar URL do webhook). Passo a passo completo em `automacao-instagram/README.md`.
  - **Limitações documentadas no README:** matching é por palavra-chave (não IA), "Eventos da Semana" não tem dado real pra responder sozinho (manda resposta de espera), e não existe notificação em tempo real pra humano ainda (só log, via `wrangler tail`) — próximo passo natural depois do deploy ir pro ar.
- **Próximo passo sugerido:** usuário roda `npx wrangler login` (dentro de `automacao-instagram/`) e avisa — daí eu sigo com `wrangler deploy` e o resto do checklist do README.
- **Regra que já foi corrigida e não pode voltar a acontecer:** nunca nomear uma pessoa específica (ex: "Lucas") no texto de resposta que vai pro público — só como nota interna. Isso já está registrado como Principle/Anti-Pattern permanente no `rita-resposta.agent.md`.

---

## O que é

Sistema de gestão de social media e marketing para o **Vila Los Muertos de Fome**, restaurante Tex Mex BR em Bethaville, Barueri, SP. Rua Caldas Novas 49. Chef Alex Coelho. Aberto 7 dias. Música ao vivo qui-sáb 20h. Stand-up comedy, samba, Copa do Mundo.

Construído no **Opensquad**, um framework de orquestração de agentes de IA. Reescrito de ponta a ponta em julho/2026: saiu o modelo de cadência automática (rodava sozinho por dia da semana), entrou um modelo **por projeto, sob demanda** — nada roda sem comando explícito do usuário.

---

## Princípio Central

**Você inicia tudo.** Não existe execução automática por data, calendário ou dado frio (cachê, valor de contrato, histórico). Um projeto só nasce quando você diz o que quer — em texto livre ("projeto story almoço, iniciar pipe") ou nomeando um agente direto ("Cris, escreve uma copy pra isso aqui").

- **Pedido amplo/ambíguo** → passa pelo **Beto Briefing**, que traduz em um plano de quais especialistas entram, confirma com você antes de despachar.
- **Pedido específico** → vai direto ao agente certo, sem essa triagem.

Em ambos os casos, três garantias valem sempre:
1. **Contexto compartilhado é automático** — identidade da marca, hard caps, direção editorial mais recente (Lia), plano mensal em vigor (Estela), achados de concorrência (Íris).
2. **Renata Revisão roda sempre**, em qualquer tipo de output — conteúdo de marca ou documento interno.
3. **Nunca publica sem seu sim/não explícito**, mesmo com conteúdo fornecido manualmente.

---

## Hierarquia de Conteúdo (regra mais importante, inalterada)

O restaurante, a comida e a experiência são **sempre o protagonista**. Shows são um pilar de entretenimento, nunca o foco principal.

**NUNCA** expor cachê, custo de artista, valor de contrato em nenhum output — nem em documentos internos (relatório, análise de concorrência, plano estratégico). Essa informação é do financeiro, não da agência de marketing. E **nenhuma campanha nasce de cachê ou dado frio** — só de pedido explícito seu.

---

## Agentes (12)

| Agente | Função | Execução | Entra em ação quando |
|--------|--------|----------|----------------------|
| **Beto Briefing** | Recepção/triagem | inline | pedido amplo/ambíguo |
| **Cris Criativa** | Copywriter única — orgânico e campanha | inline | plano inclui copy |
| **Vito Visual** | Designer — conceito + arte final | subagent | plano inclui visual |
| **Duda Direção** | Vídeo — pré e pós-produção | subagent | plano inclui vídeo |
| **Paulo Postador** | Publicação multiplataforma | subagent | plano inclui publicação |
| **Ana Anúncio** | Briefing tático de campanha paga | subagent | plano inclui tráfego pago |
| **Renata Revisão** | QA — hard caps e qualidade | inline | sempre |
| **Rodrigo Resultados** | Relatório de métricas | inline | projeto de relatório |
| **Lia Linha** | Curadoria — pra frente e pra trás | inline | projeto de curadoria |
| **Estela Estratégia** | Planejamento de campanha mensal | inline | projeto de planejamento mensal |
| **Íris Investigação** | Análise de concorrência recorrente | subagent | projeto de análise de concorrência |
| **Rita Resposta** | Biblioteca de respostas padrão de Instagram | inline | projeto de biblioteca de respostas |

Sem "editor estático" separado — Vito já cobre 100% da arte estática.

---

## Pipeline (20 passos possíveis, todos condicionais)

Nenhum passo roda por data. Cada um é avaliado sobre o plano do projeto (do Beto, ou implícito no pedido direto):

```
01 Abertura do Projeto (checkpoint) → 02 Triagem [se amplo] → 03 Confirmação do Time (checkpoint)
→ 04 Criar Conteúdo [se copy] → 05 Propor Conceito Visual [se visual] → 06 Checkpoint de Conceito
→ 07 Gerar Arte Final [se aprovado] → 08 Roteirizar Vídeo Pré-Produção [se vídeo a filmar]
→ 09 Checkpoint de Conceito de Vídeo → 10 Orientar Edição Pós-Produção [se vídeo já filmado]
→ 11 Criar Campanha [se tráfego pago] → 12 Revisão de Qualidade [sempre]
→ 13 Checkpoint Final de Publicação [se publicação, inegociável] → 14 Publicar [se aprovado]
→ 15 Relatório [se projeto de relatório] → 16 Curadoria [se projeto de curadoria]
→ 17 Planejamento Mensal [se projeto de planejamento] → 18 Checkpoint de Escopo de Concorrência
→ 19 Análise de Concorrência [se projeto de concorrência] → 20 Criar Biblioteca de Respostas [se projeto de respostas]
```

Detalhe completo em `squads/gestor-vila/pipeline/pipeline.yaml` e nos 20 arquivos em `pipeline/steps/`.

---

## Tipos de Projeto

| Tipo | Exemplo de pedido |
|------|--------------------|
| Conteúdo do dia | "projeto story almoço" |
| Copy avulsa | "Cris, preciso de uma copy pra isso aqui" |
| Campanha de evento | "projeto: divulgar o show de sábado" |
| Só tráfego pago | "projeto: campanha de tráfego pro fim de semana" |
| Relatório | "projeto: relatório da semana" |
| Curadoria | "projeto: planejar a semana" |
| Planejamento mensal | "projeto: planejamento de julho" |
| Análise de concorrência | "projeto: análise de concorrência" |
| Biblioteca de respostas | "projeto: criar biblioteca de respostas" |

---

## Placeholders de API (aguardando configuração)

Dois pontos do sistema têm a estrutura pronta mas dependem de credenciais que o usuário ainda não forneceu:

- **`skills/meta-business/`** — Rodrigo Resultados usaria isso pra puxar métricas reais do Meta Business automaticamente. Até configurar, ele pede os dados manualmente.
- **`skills/video-analysis/`** — Duda Direção usaria isso pra assistir vídeo bruto na pós-produção. Até configurar, essa parte fica bloqueada com aviso claro (a pré-produção funciona normalmente sem depender disso).

Nenhum dos dois placeholders quebra o resto do sistema.

---

## Organização de Output

`output/{projeto}/{run_id}/` — organizado por nome do projeto, não só por timestamp, pra facilitar achar tudo de um projeto depois.

Dados persistentes (fora de `output/`, nunca versionados por run):
- `pipeline/data/direcao-semanal-atual.md` — última curadoria da Lia
- `pipeline/data/plano-campanha-mensal-atual.md` — último plano da Estela
- `pipeline/data/biblioteca-respostas-atual.md` — versão viva da biblioteca da Rita, compartilhada com a equipe
- `_investigations/concorrentes/` — histórico acumulado de monitoramento da Íris

---

## Estrutura de Arquivos

```
squads/gestor-vila/
├── pipeline-visual.html          ← dashboard (roster de agentes, fluxo do pipeline, tipos de projeto)
├── squad.yaml                    ← configuração do squad
├── agents/
│   ├── beto-briefing.agent.md + tasks/
│   ├── cris-criativa.agent.md + tasks/
│   ├── vito-visual.agent.md + tasks/ (conceito + arte final + arte de evento)
│   ├── duda-direcao.agent.md + tasks/ (pré-produção + pós-produção)
│   ├── paulo-postador.agent.md + tasks/
│   ├── ana-anuncio.agent.md + tasks/
│   ├── renata-revisao.agent.md + tasks/
│   ├── rodrigo-resultados.agent.md + tasks/
│   ├── lia-linha.agent.md + tasks/
│   ├── estela-estrategia.agent.md + tasks/
│   ├── iris-investigacao.agent.md + tasks/
│   └── rita-resposta.agent.md + tasks/
├── pipeline/
│   ├── pipeline.yaml              ← 20 steps condicionais
│   ├── steps/step-01 a step-20
│   └── data/
│       ├── vila-identity.md, tone-of-voice.md, output-examples.md, anti-patterns.md
│       ├── research-brief.md, quality-criteria.md
│       ├── direcao-semanal-atual.md, plano-campanha-mensal-atual.md, biblioteca-respostas-atual.md (persistentes)
├── _investigations/concorrentes/  ← histórico da Íris
└── output/
    └── {projeto}/{run_id}/v1/
```

---

## O que ainda pode melhorar

- **Skills de API pendentes** — Meta Business e análise de vídeo precisam das credenciais do usuário pra sair do modo placeholder.
- **Nunca rodou de verdade** — todo o sistema foi reescrito nesta sessão; falta uma primeira execução real ponta a ponta pra validar o fluxo condicional na prática.
- **Publicação real** — Paulo Postador ainda não tem sessão autenticada nas plataformas (sem `.mcp.json`/credenciais no repo).
- **Bot de resposta automática no Instagram** — sinalizado como prioridade real pelo usuário (cliente sem resposta = receita perdendo). A Rita Resposta cobre a biblioteca manual primeiro; a automação de verdade é um projeto técnico separado (Instagram Messaging API, atenção às restrições da Meta pra automação de DM) ainda não escopado.
