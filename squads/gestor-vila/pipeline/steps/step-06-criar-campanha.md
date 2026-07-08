---
step: 06
name: "Criar Campanha de Anúncios"
type: paid_media
agent: ana-anuncio
execution: subagent
condition: "briefing.tem_evento_pago == true"
---

# Step 06 — Criar Campanha de Anúncios

## Objetivo

Ana Anúncio cria o briefing completo de campanha paga para Meta Ads e TikTok Ads quando há evento qualificado.

## Agente Ativo

**Ana Anúncio** — Gestora de Tráfego Pago

## Condição de Execução

Este step só roda quando `output/briefing.md` indica `Ativar anúncio: SIM`. Se o briefing do dia não tem evento pago, este step é pulado.

## Tasks

Executar `agents/ana-anuncio/tasks/criar-campanha-evento.md`:

1. Verificar se `output/conteudo.md` contém seção `## ANÚNCIO PAGO`
2. Identificar tipo de evento e calcular orçamento pela tabela de tipo (não por cachê)
3. Montar segmentação completa (raio 12km Barueri, interesses por evento, idade)
4. Definir timing de ativação (horas/dias antes do evento)
5. Montar briefing Meta Ads + TikTok Ads separados
6. Incluir resumo financeiro de investimento em ads — sem cachê ou custo de artista
7. Emitir ALERTA DE OPORTUNIDADE se Copa, artista com histórico de público acima da média, ou data comemorativa estratégica
8. Salvar em `output/campanha.md`

**Regra crítica:** Nenhum valor de cachê, contrato ou custo de artista entra no briefing. O copy de campanha deve centrar na experiência da Vila (comida + entretenimento) — o artista é argumento, não protagonista.

## Output Esperado

- `output/campanha.md` com briefing completo de campanha

## Prosseguir para Step 07 — Revisão de Qualidade.

## Nota

A campanha não é ativada automaticamente — é um briefing para configuração manual no Meta Ads Manager / TikTok Ads. A ativação requer ação do usuário.
