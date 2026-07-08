---
task: "Criar Conteúdo Diário"
order: 1
input: |
  - briefing: output/briefing.md — categoria do post, stories, tipo de dia, entretenimento
  - identity: pipeline/data/vila-identity.md — restaurante, chef, cardápio, identidade
  - tone: pipeline/data/tone-of-voice.md — 6 tons, frequência, regras universais
  - examples: pipeline/data/output-examples.md — modelos de copy aprovados
  - anti_patterns: pipeline/data/anti-patterns.md — erros a evitar
output: |
  - file: output/conteudo.md — copy de cada slot do dia
---

# Criar Conteúdo Diário

## Descrição

Cris lê o briefing, identifica a **categoria de conteúdo do dia** (definida pelo Google Agenda principal) e escreve copy para todos os slots. O restaurante é sempre o protagonista. Shows, Copa e Stand-up enriquecem o contexto — nunca substituem o foco gastronômico e de experiência da Vila.

---

## Pilares de Conteúdo do Vila

O calendário define uma categoria para cada dia da semana. Esses são os pilares que orientam o copy:

| Dia | Categoria POST PRINCIPAL | Essência do copy |
|-----|--------------------------|------------------|
| **Segunda** | Agenda da Semana | Apresentar a semana, gerar expectativa para os dias que vêm |
| **Terça** | Rodízio v1 | Foco no cardápio, abundância, variedade, custo-benefício |
| **Quarta** | Domínio Territorial | Vila como ponto de referência de Bethaville/Barueri |
| **Quinta** | Rodízio v2 | Comida como experiência, preparo do Chef Alex, detalhes |
| **Sexta** | Experiência Cultural | A noite começa aqui — happy hour, clima, entretenimento |
| **Sábado** | Família | Acolhimento, refeição compartilhada, memória afetiva |
| **Domingo** | Aniversário | Celebração, gratidão, convite para fazer parte da comunidade |

---

## Processo

### 1. Identificar o contexto do dia

Ler `output/briefing.md` e extrair:
- **Categoria do post principal:** qual é o tema do feed hoje?
- **Stories do dia:** quais categorias de story estão agendadas?
- **Tipo de dia:** copa / standup / samba / show / domingo / normal
- **Tem entretenimento à noite?** artista + horário (se houver)
- **Data comemorativa?** há alguma data relevante para gastronomia?

### 2. Selecionar tom por slot e contexto

| Contexto | POST PRINCIPAL | STORY 1 | STORY 2 | STORY CHEF ALEX | STORY SHOW |
|----------|---------------|---------|---------|-----------------|------------|
| Normal / segunda-quarta | Gastronômico | Acolhedor | Cultural | Gastronômico | — |
| Quinta-feira | Gastronômico | Acolhedor | Urgente/FOMO | Gastronômico | Animado (se show) |
| Sexta | Animado/Festivo | Urgente/FOMO | Gastronômico | Gastronômico | Animado (se show) |
| Sábado | Acolhedor/Familiar | Gastronômico | Animado | Gastronômico | Animado (se show) |
| Domingo | Acolhedor/Familiar | Acolhedor | Cultural | Gastronômico | — |
| Copa do Mundo | Comunitário/Local | Urgente/FOMO | Gastronômico | Gastronômico | Comunitário |
| Stand-up | Animado/Festivo | Urgente/FOMO | Cultural | Gastronômico | Animado |
| Data comemorativa gastronômica | Gastronômico/Sensorial | qualquer | Comunitário | Gastronômico | — |

A data comemorativa **enriquece** o copy da categoria do dia — não substitui a categoria. Ex: se é quinta de Rodízio v2 + Dia do Hambúrguer → o post fala do rodízio com uma pitada do hambúrguer.

### 3. Escrever copy por slot

---

**POST PRINCIPAL (feed Instagram + Facebook)**

Escrever sobre a **categoria do dia**, usando a identidade da Vila:
- Linha 1: gancho direto sobre o tema do dia (comida, clima, experiência, lugar)
- Linhas 2-4: detalhe sensorial, contexto narrativo, personalidade do Vila
- Linha 5: informação prática — dia, horário de abertura ou do evento, endereço
- Linha 6: CTA físico — "vem antes das 19h", "reserva pelo link", "chega com fome"
- Se há show à noite: mencionar naturalmente em uma linha ("hoje à noite tem [artista] ao vivo às 20h")
- **Nunca:** "confira", "venha nos visitar", "link na bio", "o melhor de Barueri"
- Limite: 2.200 chars; ideal 300-600 chars

---

**STORY 1 — Engajamento (15s)**

Baseado na categoria do story 1 do briefing (ex: "Happy Hour", "Feijoada", "Experiência Cultural"):
- 1-2 frases curtas sobre o tema + pergunta interativa (enquete, slider, caixa)
- Foco: engajamento, curiosidade, participação
- Exemplo para Happy Hour: "Como é o seu happy hour perfeito? 🍹 Mesa boa / Balcão animado"
- **Nunca** mencionar preço ou informação financeira interna

---

**STORY 2 — Informação (15s)**

Baseado na categoria do story 2 do briefing (ex: "Cardápio", "Noite Temática", "Agenda Jogos"):
- 1-2 frases com detalhe específico (ingrediente do prato, destaque do cardápio, agenda do fim de semana)
- CTA final: "manda mensagem" / "aparece por aqui" / "Rua Caldas Novas 49" — **nunca "link na bio"**
- Limite: 250 chars

---

**STORY CHEF ALEX — Bastidor (30s)**

Recorrente em todos os dias. Tom pessoal — como se Alex falasse direto:
- Revelar processo, bastidor, ingrediente especial, dificuldade do dia
- Foco: o humano por trás da comida, não a venda
- Fechar com algo caloroso, não com CTA comercial
- Limite: 300 chars
- Exemplos bons: "hoje o Alex acordou às 6h pra deixar o guacamole no ponto certo" / "o segredo do nacho tostado não é a farinha, é o tempo de forno"

---

**STORY SHOW — Entretenimento** *(adicionar SOMENTE quando briefing.tem_entretenimento == SIM)*

Este é o único slot onde o show aparece de forma dedicada. Formato:
- Linha 1: nome do artista e o que traz de especial (voz, estilo, energia — nunca cachê)
- Linha 2: horário + convite implícito (não "compre ingresso" — é entrada gratuita no Vila)
- Linha 3: contextualizar com o Vila ("a noite aqui começa antes do show")
- Para Copa: "hoje o Brasil joga aqui. Telão, cerveja gelada e muita torcida."
- Para Stand-up: "é noite de stand-up no Vila. [nome] é a atração. Rindo antes de comer."
- Limite: 200 chars
- **Nunca:** valor de cachê, "artista de R$X", comparativo financeiro

---

### 4. Verificar hard caps antes de salvar

- [ ] **H1 — Zero marketing language:** "confira", "venha nos visitar", "link na bio", "temos o melhor", "não perca" → reescrever
- [ ] **H2 — Horário em todo show:** se há entretenimento, o story show deve ter artista + horário + dia
- [ ] **H3 — CTA físico apenas:** vem, reserva, aparece, chega — nunca "clique", "acesse", "confira"
- [ ] **H4 — Nenhum valor financeiro interno:** cachê, custo do artista, preço de contrato → VETO absoluto

---

## Formato de Saída

Salvar em `output/conteudo.md`:

```markdown
# Conteúdo do Dia — [DIA DA SEMANA, DATA]

**Categoria do dia:** [ex: Experiência Cultural — Sexta]
**Tipo de dia:** [show / copa / standup / samba / domingo / normal]
**Tom principal:** [tom selecionado]
**Entretenimento:** [Artista, 20h / Jogo do Brasil, 19h / —]

---

## POST PRINCIPAL

**Plataforma:** Instagram + Facebook
**Categoria:** [categoria do dia]
**Tom:** [tom]

[copy completo]

---

## STORY 1 — [Categoria do Story 1]

**Formato:** Story 15s com [enquete / slider / caixa de pergunta]
**Tom:** [tom]

[copy + tipo de interação definido]

---

## STORY 2 — [Categoria do Story 2]

**Formato:** Story 15s texto/foto
**Tom:** [tom]

[copy completo]

---

## STORY CHEF ALEX — Bastidor

**Formato:** Story 30s vídeo ou foto bastidor
**Tom:** Gastronômico/Sensorial
**Personagem:** Chef Alex Coelho

[copy — como se Alex falasse direto, sem CTA de venda]

---

## STORY SHOW — Entretenimento
*[Incluir apenas se tem_entretenimento == SIM]*

**Artista/Evento:** [nome]
**Horário:** [hora]
**Formato:** Story 15-30s
**Tom:** Animado/Festivo

[copy — experiência + artista + horário. Sem valor financeiro.]

---

## ANÚNCIO PAGO
*[Incluir apenas se briefing.campanha_paga == SIM — fornece contexto para Ana Anúncio]*

**Evento âncora:** [artista ou Copa ou stand-up]
**Data/hora:** [data + horário]
**Tipo de campanha:** [show ao vivo / Copa / stand-up]
**Público-alvo:** [perfil — ex: "fãs de música ao vivo, 25-45 anos, Barueri"]

### Headlines (3 variações, ≤40 chars cada)
1. [headline 1]
2. [headline 2]
3. [headline 3]

### Primary Text (2 variações, ≤125 chars cada)
**A:** [texto]
**B:** [texto]

### CTA
Obter Trajeto

---

## Status

- [ ] Hard caps H1-H4 verificados
- [ ] Todos os slots com categoria/tema concreto
- [ ] CTA físico em todas as peças
- [ ] Nenhum valor financeiro interno visível
- [ ] Pronto para Vito Visual
```

---

## Exemplos de Copy Aprovados

**Quinta de Rodízio v2 — com show do CARLOS às 20h:**

```
## POST PRINCIPAL (Rodízio v2)

Quinta à noite tem aquela fome boa.
O Alex deixou o rodízio no ponto: nacho crocante, frango desfiado, guacamole fresco — tudo saindo da cozinha.
Não precisa de motivo pra aparecer. Quinta, a partir das 19h. Rua Caldas Novas 49, Bethaville.
À noite tem CARLOS ao vivo às 20h.
chega com fome.

## STORY 1 — Rodízio v2
Qual mesa você escolhe numa quinta assim? 🌮
Mesa do canto / Mesa no meio do barulho

## STORY 2 — Agenda Fim de Semana
Sexta e sábado têm show também.
Agenda do fim de semana: [artistas + horários].
Rua Caldas Novas 49.

## STORY CHEF ALEX
hoje o Alex fez três lotes de guacamole porque o primeiro sumiu antes do almoço.
é bom assim.

## STORY SHOW — CARLOS
CARLOS ao vivo aqui hoje.
MPB e pop com aquela pegada. Começa às 20h.
a noite no Vila é assim.
```

**Sexta — Experiência Cultural — sem show:**

```
## POST PRINCIPAL (Experiência Cultural)

Sexta é diferente aqui.
Não é só happy hour — é aquele momento em que você finalmente respira.
Mesa boa, drink gelado, nacho com guacamole. O Alex capricha mais quando sente que o clima pede.
Sexta, a partir das 19h. Rua Caldas Novas 49, Bethaville.
chega antes que lotar.

## STORY 1 — Happy Hour (abertura)
Como é o seu início de sexta? 🥃
Primeira mesa / Chego mais tarde

## STORY 2 — Happy Hour (reforço)
Happy hour no Vila.
O que muda aqui: a cozinha do Chef Alex não para durante o happy hour.
Rua Caldas Novas 49.

## STORY CHEF ALEX
na sexta o Alex deixa o nacho mais generoso.
ele acha que sexta merece isso.
```

---

## Critérios de Qualidade

- [ ] POST PRINCIPAL segue a categoria do calendário (não o show)
- [ ] Cada slot tem personagem real: chef, prato específico com nome, artista (se show)
- [ ] Story Chef Alex é pessoal e sobre comida/cozinha — não uma propaganda
- [ ] Story Show aparece apenas quando há entretenimento — focado na experiência
- [ ] Zero informação financeira interna (cachê, custo, "artista de R$X")

## Condições de Veto

- **Copy sem tema concreto** (só genérico) → reescrever antes de passar para Vito
- **Marketing language presente** → reescrever imediatamente
- **Post de show sem artista + horário no Story Show** → bloqueio, não passa
- **Cachê ou valor de contrato no copy** → VETO absoluto — remover e reescrever
