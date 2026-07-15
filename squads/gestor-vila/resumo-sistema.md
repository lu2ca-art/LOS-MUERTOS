# Gestor Vila — Resumo do Sistema (v2)

## 🔴 Sessão em andamento — retomar daqui (2026-07-15)

**Trabalho ativo:** expandindo `pipeline/data/biblioteca-respostas-atual.md` (Rita Resposta) rumo a ~50 categorias.

- **Status atual:** 30 categorias no público geral (segmento A) + 4 institucionais (B-E) = 34 total.
- **Meta:** ~46-50 no público geral, mantendo B-E enxutos (são só redirecionamento pro WhatsApp, não expandir).
- **Pendências já marcadas no arquivo** (não inventar, só confirmar com o usuário): lista de pratos vegetarianos/veganos/sem-glúten, valores do voucher de aniversário (em validação pelo gerente), detalhes do novo sistema de delivery, lista completa do cardápio à la carte.
- **Bloqueio:** a extensão Claude in Chrome não conectou nesta sessão (tentativas via skill, `/chrome`, e restart parcial não surtiram efeito) — sem isso, não dá pra ler comentários/DMs reais do Instagram @vilalosmuertosdefome pra minerar mais categorias com precisão. Alternativa que funcionou: usar avaliações públicas do Google/Restaurant Guru via WebSearch/WebFetch (revelou cardápio à la carte não documentado em nenhum lugar — Hambúrguer Yellow, Dadinho de Tapioca, Parmegiana, Peixe-espada).
- **Próximo passo sugerido:** (1) tentar `/chrome` de novo numa sessão nova pra ver se conecta; (2) se conectar, navegar de verdade no Instagram pra ler comentários reais; (3) se não conectar, seguir expandindo por prints que o usuário manda + brainstorm assistido categoria por categoria, do jeito que vinha funcionando bem até aqui.
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
