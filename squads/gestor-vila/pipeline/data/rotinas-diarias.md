# Rotinas de Trabalho — Gestor Vila

Cadência de cada um dos 9 agentes. "Diária" nem sempre significa "produz algo novo todo dia" —
alguns agentes checam diariamente e agem só quando a condição é atendida (marcado como
**condicional**). Isso evita ruído: Ana não monta campanha todo dia, só quando há evento pago
de verdade.

## Pipeline Diário (Cris → Vito → checkpoint → Paulo → Ana* → Renata → Rodrigo*)

| Horário | Agente | Rotina | Ação |
|---------|--------|--------|------|
| 08:00 | *(inline)* Briefing | Diária | Lê Google Agenda (`losmuertosdefome@gmail.com` + Música e Eventos), monta `briefing.md` |
| 08:15 | **Cris Criativa** | Diária | Escreve todo o conteúdo do dia (post principal + stories) |
| 08:45 | **Vito Visual** | Diária | Cria as artes a partir do conteúdo do Cris |
| 09:00 | *(checkpoint)* Aprovação | Diária | **Pausa aqui** — aguarda aprovação explícita do usuário, nunca segue sozinho |
| 18h–21h (IG) / 12h ou 20h (TikTok) | **Paulo Postador** | Diária, após aprovação | Publica no horário de pico de cada plataforma — nunca publica sem aprovação do Step anterior |
| 24–72h antes do evento | **Ana Anúncio** | Condicional | Só ativa quando o briefing do dia tem evento pago (show ≥R$400, Copa, stand-up) |
| Após publicação | **Renata Revisão** | Diária | Verifica os hard caps antes/depois de publicar |
| Segunda 09h | **Rodrigo Resultados** | Semanal | Relatório da semana anterior — métricas, insights, ROI |

## Agentes Sob Demanda (fora do pipeline diário automático)

| Agente | Rotina proposta | Ação |
|--------|------------------|------|
| **Hugo Caçador** | Semanal — segunda 07h (antes do resto do pipeline acordar) | Caça 5-8 referências novas pra alimentar a semana de conteúdo, entrega antes do Cris escrever o conteúdo de segunda |
| **Vini Vídeo** | Rotativa — terça, quinta, sábado | Edita 1 reels a partir da biblioteca real (`pipeline/data/biblioteca-midia.md`), alternando o tema pela pasta do dia (ex: ter=rodízio, qui=música, sáb=drinks) |
| **Carmen Atendimento** | Contínua (24/7) quando o canal estiver conectado | Responde clientes em tempo real — **hoje bloqueada**, sem WhatsApp Business/Instagram Direct conectados |

## Regras da Rotina

1. **Checkpoints nunca são pulados.** Mesmo em execução automática, Step 04 (aprovação de
   conteúdo) e Step 09 (aprovação final) sempre pausam esperando o usuário. Isso vale também
   pra qualquer automação futura via cron/schedule — não é negociável.
2. **Condicional não é opcional, é responsivo.** Ana e Rodrigo checam a condição todo dia/toda
   semana; a ausência de ação é o comportamento correto quando a condição não bate, não uma
   falha.
3. **Hugo antes do Cris.** A caçada de referências de segunda de manhã deve terminar antes do
   Cris começar a escrever, pra que ele possa puxar ideias frescas quando fizer sentido.
4. **Vini não inventa material.** A rotina rotativa de terça/quinta/sábado só produz vídeo se
   existir material bruto correspondente na biblioteca — ver regra "nunca inventar cenas" no
   `vini-video.agent.md`.
5. **Dashboard sempre reflete a rotina real.** Toda execução (ou tentativa bloqueada) atualiza
   `squads/gestor-vila/agent-status.html` — ver regra em `CLAUDE.md`.
