---
task: "Criar Anúncio de Evento"
order: 2
input: |
  - briefing: output/briefing.md — evento, artista, data, cachet
  - identity: pipeline/data/vila-identity.md — endereço, público, diferenciais
  - tone: pipeline/data/tone-of-voice.md — Urgente/FOMO para eventos
  - examples: pipeline/data/output-examples.md — exemplos de anúncios aprovados
output: |
  - append: output/conteudo.md — seção ANÚNCIO DE EVENTO com headline + descrição + CTA
---

# Criar Anúncio de Evento

## Descrição

Quando há evento com artista ≥ R$400, Copa do Mundo ou stand-up, Cris escreve o copy do anúncio pago. O anúncio é passado para Ana Anúncio que monta o briefing de campanha. O copy precisa ser mais direto e urgente que o post orgânico — é para quem ainda não segue a Vila.

## Gatilho

Esta task é executada APENAS quando o briefing indica:
- Artista com cachet ≥ R$400 (LU2CA, DHARA, artistas especiais)
- Copa do Mundo (jogos do Brasil: 13/06, 19/06, 24/06)
- Stand-up comedy (evento específico)

Para shows de artistas com cachet < R$400, usar apenas conteúdo orgânico.

## Processo

### 1. Identificar parâmetros do evento

Do `output/briefing.md`, extrair:
- **Evento:** nome do artista OU "Copa do Mundo — Brasil vs X"
- **Data + Horário:** obrigatório
- **Diferenciais do evento:** por que esta noite é especial
- **Público-alvo principal:** fãs de [gênero musical] OU torcida OU fãs de stand-up

### 2. Escrever headline (3 variações)

Tom: **Urgente/FOMO**

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

Adicionar ao `output/conteudo.md`:

```markdown
---

## ANÚNCIO PAGO — [EVENTO] — [DATA]

**Gatilho:** [artista ≥ R$400 / Copa / Stand-up]
**Destinatário:** Ana Anúncio (Step 06)

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
- Cachet estimado: R$[valor]
- Público: [público-alvo]
- Urgência: [horas até o evento no momento de ativar]
```

## Exemplo de Saída

**Contexto:** LU2CA, sábado 23/05, cachet R$600

```markdown
## ANÚNCIO PAGO — LU2CA — sábado 23/05

**Gatilho:** artista ≥ R$400

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
- Cachet estimado: R$600
- Público: fãs de MPB/indie, 25-40 anos, Barueri/Bethaville
- Urgência: ativar campanha 48h antes (quinta às 21h)
```

## Critérios de Qualidade

- [ ] Headline ≤ 40 chars
- [ ] Primary text ≤ 125 chars
- [ ] CTA físico (Obter Trajeto ou Reservar)
- [ ] Evento + horário presentes
- [ ] 3 variações de headline para teste A/B

## Condições de Veto

- **Headline sem nome do evento/artista** → reescrever
- **CTA "Saiba Mais" ou "Comprar"** → substituir imediatamente
- **Anúncio para show com cachet < R$400** → remover, não há gatilho
