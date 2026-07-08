---
step: 01
name: "Briefing do Dia"
type: data_collection
agent: inline
---

# Step 01 — Briefing do Dia

## Objetivo

Ler o Google Agenda completo do dia e montar o briefing que orienta todos os agentes. O **calendário principal** define o conteúdo. O **calendário Música e Eventos** é informação de contexto — nunca o motor do conteúdo.

## Hierarquia das fontes

| Fonte | Papel |
|-------|-------|
| `losmuertosdefome@gmail.com` (calendário principal) | **PRIMÁRIO** — define quais slots de conteúdo rodam, quais datas comemorativas aproveitar, quais ações offline acontecem |
| Calendário "Música e Eventos" | **SECUNDÁRIO** — informa se há show, qual artista (nome apenas), que horas. Nunca define o conteúdo, nunca expõe valores de cachê |

## Ações a executar

### 1. Ler o calendário principal do dia
Usar `mcp__claude_ai_Google_Calendar__list_events` com:
- `calendarId: losmuertosdefome@gmail.com`
- `startTime / endTime` cobrindo o dia completo

Identificar e separar por tipo de evento:
- **`[POST PRINCIPAL]`** — categoria do post do feed (ex: "Rodízio v2", "Experiência Cultural", "Família")
- **`[STORY]`** — categorias de stories do dia (ex: "Happy Hour", "Feijoada", "Agenda Fim de Semana")
- **`[STORY] Chef Alex Coelho`** — sempre presente, bastidor de cozinha
- Datas comemorativas — emojis indicam relevância gastronômica (🍔🍟🍕🍹 etc.)
- Ações offline — não entram no conteúdo digital, mas informam o contexto da equipe

### 2. Ler o calendário Música e Eventos
Usar `mcp__claude_ai_Google_Calendar__list_events` com:
- `calendarId: 8aae14c6f254952e7d792048ac23a573ce8e6b90fa32508f7ad832c49b335614@group.calendar.google.com`
- Mesmo dia

Extrair **apenas**:
- Nome do artista ou tipo de evento ("Samba", "Stand-up", "Jogo do Brasil")
- Horário de início
- **IGNORAR completamente** qualquer valor monetário nos eventos (ex: "LU2CA - 600$ sáb" → registrar apenas "LU2CA, 20h")

### 3. Classificar o tipo de dia

| Tipo de dia | Critério |
|-------------|----------|
| `copa` | Evento "Jogo do Brasil" no calendário de Música |
| `standup` | Evento "Stand Up" ou variantes no calendário de Música |
| `samba` | Evento "Samba" no calendário de Música |
| `show` | Qualquer outro artista ao vivo no calendário de Música |
| `domingo` | Domingo sem eventos especiais |
| `normal` | Qualquer outro dia |

Copa do Mundo tem prioridade máxima — sobrepõe qualquer classificação.

### 4. Identificar se há gatilho de campanha paga

Sim se:
- Há show ao vivo E o restaurante quer divulgação (padrão: sim para shows com artista nomeado)
- Há jogo do Brasil (Copa do Mundo)
- Há Stand-up Comedy

Nunca expor valor de cachê no briefing — a decisão de divulgação não é baseada em quanto o músico ganha.

### 5. Salvar output/briefing.md

O briefing é salvo em dois formatos no mesmo arquivo: YAML estruturado (para consumo dos agentes) + Markdown descritivo (para leitura humana).

**Formato YAML obrigatório no topo do arquivo:**

```yaml
briefing:
  data: YYYY-MM-DD
  dia_semana: [Segunda|Terça|Quarta|Quinta|Sexta|Sábado|Domingo]
  pilar: [Agenda da Semana|Rodízio v1|Domínio Territorial|Rodízio v2|Experiência Cultural|Família|Aniversário]
  eventos_agenda: [lista de eventos do Google Agenda principal]
  show:
    tem_show: [true|false]
    artista: [nome — só se tem_show == true]
    horario: [HH:MM — só se tem_show == true]
  campanha_paga: [SIM|NAO]
  tipo_campanha: [show_padrao|show_destaque|copa|standup|samba|null]
  datas_comemorativas: [lista ou null]
```

**Seguido do formato Markdown descritivo:**

```markdown
# Briefing do Dia — [DIA DA SEMANA, DATA]

**Tipo de dia:** [copa / standup / samba / show / domingo / normal]
**Data:** [data completa]
**Run ID:** [YYYY-MM-DD-HHmmss]

---

## Calendário de Conteúdo

### Post Principal do Feed
- **Categoria:** [Agenda da Semana / Rodízio v1 / Domínio Territorial / Rodízio v2 / Experiência Cultural / Família / Aniversário]
- **Formato:** Feed Instagram + Facebook (POST PRINCIPAL)

### Stories do Dia
- **Story 1:** [categoria — ex: Happy Hour (abertura) / Experiência Cultural / Feijoada]
- **Story 2:** [categoria — ex: Happy Hour (reforço) / Agenda Jogos / Noite Temática / Cardápio]
- **Story Chef Alex:** Bastidor de cozinha (recorrente diário)

### Datas Comemorativas
[lista das datas do dia com descrição e relevância para restaurante/gastronomia]
[deixar vazio se não houver data relevante]

### Ação Offline
- [ação offline do dia — ex: "Feira de Barueri (Stand / Panfletagem)"]
- [informativo para equipe, não entra no conteúdo digital]

---

## Entretenimento da Noite

- **Tem apresentação:** [SIM / NÃO]
- **Artista / Tipo:** [nome do artista OU "Samba" OU "Stand-up" OU "Jogo do Brasil" OU "—"]
- **Horário:** [hora]
- **Story de Divulgação:** [SIM — adicionar STORY SHOW ao conteúdo / NÃO]

---

## Campanha Paga

- **Ativar ads:** [SIM / NÃO]
- **Tipo de campanha:** [show ao vivo / Copa / stand-up / —]
- **Foco:** experiência Vila (comida + entretenimento), não apenas o artista
- **Passar para Ana Anúncio:** [SIM / NÃO]

---

## Notas para Agentes

[Qualquer observação relevante: data comemorativa que casa com o cardápio, artista muito conhecido que merece destaque maior no story, Copa com grande audiência esperada, etc.]

**Não incluir:** valores de cachê, custo de artistas, informações financeiras internas.
```

## Prosseguir para Step 02 — Cris Criativa.
