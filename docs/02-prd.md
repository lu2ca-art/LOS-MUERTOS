# PRD — Gestor Vila (sistema de marketing semi-automatizado)

> Depende do contexto em `01-briefing.md`.

## 1. Problema

Lucca e Lohany produzem conteúdo diário (posts, stories, campanhas) manualmente, sem um processo que garanta consistência de marca, revisão de qualidade e visibilidade de status — em uma operação que já rodou com um único post principal e story diário, mas que agora precisa escalar (Copa do Mundo 2026, mais eventos, delivery, novos uniformes/decorações).

## 2. Objetivo do produto

Dar ao time de marketing um pipeline com **checkpoints de aprovação humana obrigatórios**, que:
- Lê o calendário editorial (Google Calendar) como fonte de verdade diária.
- Gera conteúdo e visual de forma assistida (não sem revisão).
- Bloqueia publicação de qualquer peça que viole as regras de qualidade da marca.
- Publica, opcionalmente cria campanha paga, e reporta resultado.
- Nunca roda em modo totalmente automático sem que Lucca tenha revisado e aprovado conscientemente pelo menos uma vez o padrão de saída.

## 3. Personas

| Persona | Papel no sistema |
|---|---|
| **Lucca** (Criativo/Marketing) | Aprovador principal — checkpoints 04 e 09. Pode editar conteúdo inline antes de aprovar. Pode reprovar com justificativa. |
| **Lohany** (Produção de Conteúdo) | Fornece matéria-prima (fotos/vídeos) que alimenta a geração de conteúdo e visual. |
| **Alex Coelho** (Chef) | Rosto recorrente do conteúdo de cozinha; não interage diretamente com o sistema, mas é referenciado no conteúdo gerado. |
| **Lucas Coelho** (Diretor) | Possível segundo aprovador para decisões de maior impacto (ex.: valor de campanha paga) — não confirmado, ver seção "Em aberto". |

## 4. Escopo funcional — pipeline de 9 etapas

| # | Etapa | Responsável | Entrada | Saída |
|---|---|---|---|---|
| 01 | Briefing do Dia | Sistema (lê Google Calendar) | Evento do calendário editorial | `briefing` |
| 02 | Criar Conteúdo | Cris Criativa (agente) | `briefing` | `content.legenda` |
| 03 | Criar Visual | Vito Visual (agente, via Canva) | `content` | `visual.canvaDesignId` |
| 04 | **Aprovação Humana ①** | Lucca | `content` + `visual` | aprovado / reprovado com justificativa |
| 05 | Publicar | Paulo Postador (agente, via Meta Business Suite) | conteúdo aprovado | post publicado |
| 06 | Criar Campanha (condicional) | Ana Anúncio (agente) | post publicado + `tipoCampanha` | `campaign` |
| 07 | Revisão de Qualidade | Renata Revisão (agente/regras automáticas) | post publicado | `qaReport` |
| 08 | Relatório | Rodrigo Resultados (agente) | métricas da plataforma | `metrics` |
| 09 | **Aprovação Final ②** | Lucca | `qaReport` + `metrics` | encerramento do ciclo |

Reprovação no checkpoint 04 volta a etapa para 02 (novo conteúdo). Reprovação no checkpoint 09 volta a etapa para 07 (nova revisão de qualidade). Toda reprovação exige justificativa registrada no histórico.

> Nota: "Cris Criativa", "Vito Visual", "Paulo Postador", "Ana Anúncio", "Renata Revisão", "Rodrigo Resultados" são nomes de agentes definidos em versão anterior deste projeto (não vieram da reunião de equipe). Mantidos aqui como nomenclatura interna do pipeline — **a confirmar com Lucca se é isso que ele quer**, já que não têm correspondência com pessoas reais da operação.

## 5. Regras de qualidade — invioláveis (hard caps)

Aplicadas automaticamente antes do checkpoint 04, bloqueando aprovação até correção:
- Zero linguagem de marketing genérica ("confira", "venha nos visitar", "link na bio").
- Todo story de show precisa ter artista + horário + dia.
- CTA sempre físico ("vem", "reserva", "aparece") — nunca digital ("clique", "acesse").
- Nenhum valor financeiro interno (cachê, custo de contrato) pode vazar — veto absoluto.

## 6. Tratamento de eventos especiais

- **Copa do Mundo 2026 (jogos do Brasil):** tom Urgente/FOMO ativado 3 dias antes; campanha paga automática; post principal substituído pelo contexto Copa; flag `tipo_campanha: copa`.
- **Stand-up Comedy:** campanha paga, tom animado/festivo.
- **Datas comemorativas gastronômicas:** integradas ao post do dia, sem substituir o pilar padrão.

## 7. Requisitos não funcionais

- Nenhuma etapa publica ou dispara gasto de mídia sem passar pelo checkpoint humano correspondente.
- Todo histórico de decisão (aprovação/reprovação, quem, quando, por quê) é auditável.
- O sistema deve funcionar mesmo antes de todas as integrações reais estarem prontas (hoje: dados mockados como fallback).

## 8. Fora de escopo (por enquanto)

- Automação de WhatsApp (reservas/institucional) — workstream separado, ainda em estudo.
- CRM de clientes — workstream separado, a construir.
- TV Los Muertos (digital signage) — workstream separado, gerenciado via Look DS/Trello.
- Cardápio digital — workstream separado.
- Aprovação de segundo nível pelo Lucas Coelho — não confirmado que existe hoje.

## 9. Em aberto (perguntas pro Lucca antes de avançar)

1. Os nomes dos agentes (Cris Criativa, Vito Visual etc.) devem continuar, ou ele prefere associar cada etapa a uma ferramenta/pessoa real (ex.: "Geração de Conteúdo" em vez de "Cris Criativa")?
2. Lucas Coelho participa de alguma aprovação, ou o checkpoint humano é só o Lucca?
3. Missão/visão/valores formais (ver `01-briefing.md`, seção 5) — ainda pendente de resposta.

## 10. Critérios de sucesso do MVP

- Lucca consegue abrir o link do sistema, ver o que está pendente de aprovação, editar e aprovar/reprovar um post real gerado a partir de um evento real do calendário.
- Nenhum post com violação de hard cap chega ao checkpoint sem aviso visível.
- Histórico completo do ciclo (da leitura do calendário até o relatório) fica visível em um único lugar.
