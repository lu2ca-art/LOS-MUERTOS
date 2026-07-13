---
task: "Criar Copy de Campanha"
order: 2
input: |
  - projeto: output/plano-projeto.md — evento, artista, data (quando aplicável)
  - identity: pipeline/data/vila-identity.md — endereço, público, diferenciais
  - tone: pipeline/data/tone-of-voice.md — Urgente/FOMO e Animado/Festivo para eventos
  - examples: pipeline/data/output-examples.md — exemplos de anúncios aprovados
output: |
  - append: output/{projeto}/conteudo.md — seção ANÚNCIO PAGO com headline + descrição + CTA
---

# Criar Copy de Campanha

## Descrição

Quando o projeto pede copy de campanha/evento — porque o usuário pediu explicitamente, não por gatilho automático — Cris escreve o copy do anúncio pago. Esse copy é passado para Ana Anúncio, que monta o briefing de campanha. É mais direto e urgente que o post orgânico — é para quem ainda não segue a Vila.

## Quando esta task roda

Esta task roda **apenas quando o plano do projeto (Beto ou pedido direto do usuário) pede copy de campanha**. Não existe gatilho automático baseado em cachê, valor de contrato ou histórico de lotação — essa decisão é sempre do usuário, nunca de um dado frio.

## Processo

### 1. Identificar parâmetros do evento

Do `output/plano-projeto.md` ou do que o usuário forneceu diretamente, extrair:
- **Evento:** nome do artista OU "Copa do Mundo — Brasil vs X" OU outro evento
- **Data + Horário:** obrigatório
- **Diferenciais do evento:** por que esta noite é especial
- **Público-alvo principal:** fãs de [gênero musical] OU torcida OU fãs de stand-up

Nunca ler ou incluir valor de cachê, custo de artista ou qualquer dado financeiro interno — essa informação não pertence a este processo.

### 2. Escrever headline (3 variações)

Tom: **Urgente/FOMO** ou **Animado/Festivo**, conforme o tipo de evento.

Regras da headline:
- Máx 40 chars (limite Meta Ads)
- Nome do artista/evento na headline — sempre
- Sem exclamação dupla (!!)
- Sem emoji na headline (Meta restringe alcance)

Exemplos:
- "LU2CA ao vivo na Vila — sábado"
- "Copa com churrasco na Vila. Hoje."
- "DHARA. Sexta. Rua Caldas Novas 49."

### 3. Escrever descrição (2 variações)

Máx 125 chars (Meta Ads primary text padrão):
- Variação A: foco sensorial + evento ("Nacho, drinks e [artista] ao vivo. Chegue antes das 20h.")
- Variação B: foco social + urgência ("Vem com a galera. Mesa ainda disponível. [artista] começa às 21h.")

### 4. Definir CTA

- Evento presencial: **"Obter Trajeto"** (preferencial) OU **"Reservar"**
- NUNCA: "Saiba Mais", "Comprar", "Inscrever-se"

### 5. Adicionar ao conteudo.md

Não substituir o conteúdo orgânico — adicionar seção separada.

## Formato de Saída

Adicionar ao `output/{projeto}/conteudo.md`:

```markdown
---

## ANÚNCIO PAGO — [EVENTO] — [DATA]

**Motivo da campanha:** [pedido do usuário — nunca "gatilho automático"]
**Destinatário:** Ana Anúncio

### Headlines (escolher 1)
1. [headline A — máx 40 chars]
2. [headline B — máx 40 chars]
3. [headline C — máx 40 chars]

### Descrição Primary Text
**Variação A:** [máx 125 chars]
**Variação B:** [máx 125 chars]

### CTA
[Obter Trajeto / Reservar]

### Contexto para Ana Anúncio
- Evento: [nome]
- Data: [data]
- Público: [público-alvo]
- Urgência: [horas até o evento no momento de ativar]
```

## Exemplo de Saída

**Contexto:** projeto pedido pelo usuário para divulgar o show de LU2CA no sábado 23/05

```markdown
## ANÚNCIO PAGO — LU2CA — sábado 23/05

**Motivo da campanha:** pedido do usuário

### Headlines
1. LU2CA ao vivo na Vila — sábado
2. LU2CA. Sábado. Bethaville.
3. Vila recebe LU2CA esta noite

### Descrição Primary Text
**Variação A:** Drinks, nacho e LU2CA ao vivo. Sábado, 21h. Rua Caldas Novas 49.
**Variação B:** Vem com a galera. LU2CA começa às 21h. Mesa ainda disponível.

### CTA
Obter Trajeto

### Contexto para Ana Anúncio
- Evento: LU2CA ao vivo
- Data: sábado, 23/05, 21h
- Público: fãs de MPB/indie, 25-40 anos, Barueri/Bethaville
- Urgência: ativar campanha 48h antes (quinta às 21h)
```

## Critérios de Qualidade

- [ ] Headline ≤ 40 chars
- [ ] Primary text ≤ 125 chars
- [ ] CTA físico (Obter Trajeto ou Reservar)
- [ ] Evento + horário presentes
- [ ] 3 variações de headline para teste A/B
- [ ] Nenhum valor de cachê ou dado financeiro interno presente

## Condições de Veto

- **Headline sem nome do evento/artista** → reescrever
- **CTA "Saiba Mais" ou "Comprar"** → substituir imediatamente
- **Qualquer valor de cachê, custo de artista ou dado financeiro interno** → VETO absoluto — remover
- **Copy gerada sem pedido explícito do usuário/plano do projeto** → bloqueio, essa task não roda sozinha
