# Spec técnica — Gestor Vila

> Depende de `01-briefing.md` e `02-prd.md`.

## 1. Arquitetura geral

```
Google Calendar ──▶ 01 Briefing ──▶ 02 Conteúdo ──▶ 03 Visual (Canva) ──▶ 04 Aprovação Humana ①
                                                                                │
                                                        ┌───────────────────────┘
                                                        ▼
                                        05 Publicar (Meta Business Suite)
                                                        │
                                        06 Campanha (condicional, Ana Anúncio)
                                                        │
                                        07 Revisão de Qualidade (regras automáticas)
                                                        │
                                        08 Relatório (métricas da plataforma)
                                                        │
                                        09 Aprovação Final ② ──▶ encerramento do ciclo
```

Cada etapa é uma transição de estado sobre um objeto `run` (uma execução do pipeline para um dia/evento). Os checkpoints 04 e 09 são os únicos pontos que exigem ação humana síncrona; as demais etapas são candidatas a automação, mas nenhuma dispara sem que o run já tenha passado pelo checkpoint anterior.

## 2. Modelo de dados (`run`)

Já implementado em `gestor-vila/pipelineStateMachine.js`:

```js
{
  id: string,
  tipoCampanha: 'copa' | 'standup' | null,
  briefing: { data, pilar, tipo },
  content: { legenda, tipo, artista?, horario?, dia?, editedByHuman? },
  visual: { thumbnailUrl, canvaDesignId },
  campaign: {...} | null,
  qaReport: { aprovado, observacoes },
  metrics: { alcance, curtidas, comentarios, compartilhamentos },
  currentStep: '01'..'09',
  stepStatus: { '01': 'done'|'in_progress'|'pending'|'rejected'|'skipped', ... },
  approvals: { '04': { decision, approver, at, note|justification } | null, '09': {...} | null },
  history: [{ at, step, action, approver?, justification? }],
}
```

Transições (`approveCheckpoint`, `rejectCheckpoint`) e o catálogo de etapas (`STEPS`) já estão implementados e testados via script Node (`node -e`, ver histórico de commits) e em navegador (Playwright).

## 3. Validação de qualidade (`qaLint.js`)

Implementa as regras da seção 5 do PRD como função pura `lintContent(text, meta) → findings[]`, com severidade `warning` (linguagem genérica) ou `critical` (CTA digital, show incompleto, vazamento financeiro). `hasCriticalFindings` bloqueia o botão de aprovação no checkpoint 04 na UI.

**Pendente de validação com Lucca:** essas regras foram escritas a partir da descrição do documento de contexto original, não da reunião de equipe 2026 — não têm ligação direta com o organograma/processos novos (ex.: sistema de bonificação, novas regras de postura). Se ele quiser, dá pra estender o lint pra também checar aderência aos novos processos internos, mas isso não estava no escopo original do PRD.

## 4. Integrações (status real, ver `01-briefing.md`)

| Integração | Uso no pipeline | Status |
|---|---|---|
| Google Calendar | Etapa 01 — fonte de verdade do briefing diário | Ativo (`losmuertosdefome@gmail.com`) |
| Google Calendar (agenda de shows) | Dados de artista/horário pra etapa 02 | Ativo — ler só artista + horário, ignorar valores financeiros |
| Canva | Etapa 03 — geração de arte com Brand Kit `kAHGNC-y7zM` | Configurado |
| Meta Business Suite | Etapa 05/06 — publicação e campanha | **Pendente** — conta travada, consultoria em andamento |
| Look DS, Google Drive, Forms/Sheets, Trello | Outros workstreams (TV Los Muertos, leads) | Fora do escopo deste pipeline |

Enquanto Meta Business Suite não estiver resolvido, as etapas 05/06 não têm integração real — o sistema deve continuar funcionando com dados mockados (`mockData.js`) até lá, sem bloquear o desenvolvimento das etapas 01-04 e 07-09.

## 5. Stack e implementação atual

- **UI:** React 18 + JSX transformado no navegador via Babel standalone — sem etapa de build. React/ReactDOM/Babel vendorizados localmente em `gestor-vila/vendor/` (sem dependência de CDN em produção).
- **Componente de aprovação:** `gestor-vila/GestorVilaApproval.jsx` — edição inline de legenda, exibição de QA/métricas, aprovação/reprovação com justificativa, bloqueio automático por veto de qualidade.
- **Dashboard:** `gestor-vila/index.html` — abas Pipeline / Aprovação / Histórico.
- **Deploy:** Vercel, projeto `los-muertos`, branch `claude/stoic-hopper-7bi13d` → domínio de produção `los-muertos-zeta.vercel.app`, atualiza a cada push (git integration).
- **Dados:** hoje 100% mockados (`gestor-vila/mockData.js`) — nenhuma integração real ainda lê o Google Calendar de verdade nem escreve no Meta Business Suite.

## 6. O que falta pra sair do mock

1. Endpoint/função que lê eventos do Google Calendar e monta o `briefing` real (etapa 01).
2. Geração de conteúdo real (etapa 02) — hoje é texto estático de exemplo.
3. Chamada real ao Canva (`generate-design` → `create-design-from-candidate`) na etapa 03.
4. Publicação real via Meta Business Suite na etapa 05 — bloqueado até a conta ser resolvida.
5. Persistência do `run` (hoje vive só em memória do React state do navegador — fecha a aba, perde o estado).

## 7. Decisão explícita pendente

Antes de implementar qualquer um dos itens da seção 6, confirmar com Lucca a seção 9 do PRD (nomes dos agentes, segundo aprovador, missão/visão) — para não repetir o problema de construir em cima de suposições não validadas.
