---
task: "Criar Biblioteca de Respostas"
order: 1
input: |
  - identity: pipeline/data/vila-identity.md — restaurante, horário, endereço, diferenciais
  - tone: pipeline/data/tone-of-voice.md — tom da marca
  - biblioteca_anterior: pipeline/data/biblioteca-respostas-atual.md — quando existir, atualizar em vez de recomeçar
output: |
  - file: output/{projeto}/biblioteca-respostas.md — biblioteca completa do projeto
  - persist: pipeline/data/biblioteca-respostas-atual.md — sobrescrito com a versão mais recente
---

# Criar Biblioteca de Respostas

## Descrição

Rita monta (ou atualiza) a biblioteca de respostas padrão pra Instagram — categorias mais frequentes primeiro, cada uma com resposta pronta no tom da Vila e, quando aplicável, direcionamento pra atenção humana.

## Processo

### 1. Levantar as categorias

Se há uma biblioteca anterior, usar como base e perguntar ao usuário se há categorias novas a incluir. Se é a primeira vez, cobrir pelo menos:
- Reserva (tem reserva? como reservar?)
- Horário de funcionamento
- Estacionamento
- Cardápio / restrições alimentares (vegano, alergias, sem glúten)
- Localização / como chegar
- Eventos da semana (show, stand-up — sem cachê)
- Elogio (agradecimento)
- Reclamação (direcionamento, não resposta genérica)
- Evento privado / grupo grande (direcionamento pra conversa direta)

### 2. Escrever a resposta padrão de cada categoria

No tom da Vila (`tone-of-voice.md`), com a informação concreta de `vila-identity.md`. Nunca vago.

### 3. Definir direcionamento quando aplicável

Para reclamação séria, negociação de evento grande, ou qualquer coisa fora do padrão: a entrada não é uma resposta pronta, é uma instrução de escalonamento — "responder com acolhimento inicial + encaminhar pra conversa direta com [quem]".

### 4. Salvar e persistir

Salvar o artefato do projeto e sobrescrever `pipeline/data/biblioteca-respostas-atual.md`, a versão viva que a equipe usa no dia a dia.

## Formato de Saída

```markdown
# Biblioteca de Respostas — Instagram Vila

**Atualizado em:** [data]

## Reserva
**Pergunta típica:** "vocês têm reserva?" / "como reservo?"
**Resposta:** [resposta pronta no tom da Vila]

## Horário
**Pergunta típica:** "que horas vocês abrem?"
**Resposta:** [resposta pronta]

## Reclamação
**Situação típica:** cliente insatisfeito com atendimento/comida
**Direcionamento:** responder com acolhimento inicial ("poxa, sentimos muito, conta pra gente o que aconteceu") + encaminhar pra conversa direta — nunca resolver publicamente no comentário
**Nunca:** resposta genérica de desculpa sem abertura pra resolver de verdade

[demais categorias...]
```

## Critérios de Qualidade

- [ ] Categorias mais frequentes cobertas (reserva, horário, cardápio, localização)
- [ ] Toda resposta tem informação concreta, não vaga
- [ ] Reclamação e casos grandes têm direcionamento, não resposta genérica forçada
- [ ] Tom consistente com a voz da Vila
- [ ] Nenhum dado financeiro interno presente
- [ ] Arquivo persistente atualizado

## Condições de Veto

- **Resposta vaga pra pergunta objetiva** → reescrever com informação concreta
- **Resposta genérica forçada em reclamação** → VETO, trocar por direcionamento
- **Cachê ou valor de contrato em resposta sobre evento** → VETO absoluto
