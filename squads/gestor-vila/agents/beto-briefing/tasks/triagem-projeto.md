---
task: "Triagem de Projeto"
order: 1
input: |
  - pedido: texto livre do usuário descrevendo o projeto
  - identity: pipeline/data/vila-identity.md — restaurante, chef, identidade
  - direcao_semanal: pipeline/data/direcao-semanal-atual.md — se existir
  - plano_mensal: pipeline/data/plano-campanha-mensal-atual.md — se existir
  - concorrencia: _investigations/concorrentes/ — arquivos mais recentes, se existirem
output: |
  - file: output/plano-projeto.md — plano do projeto com agentes necessários e pendências
---

# Triagem de Projeto

## Descrição

Beto lê o pedido do usuário, entende o objetivo real por trás dele, e monta um plano de quais especialistas da agência precisam entrar em ação. Nunca despacha ninguém sem essa etapa ser confirmada.

## Processo

### 1. Ler o pedido e identificar o objetivo

O que o usuário realmente quer como resultado final? Um post pronto? Só uma copy? Uma campanha de tráfego? Um relatório? Uma análise de concorrência? Um plano do mês? Nem todo pedido é sobre conteúdo — pode ser puramente estratégico ou analítico.

### 2. Consultar contexto de fundo

Antes de montar o plano, verificar (sem perguntar ao usuário, se os arquivos existirem):
- `pipeline/data/direcao-semanal-atual.md` — há uma direção editorial recente da Lia que se aplica?
- `pipeline/data/plano-campanha-mensal-atual.md` — há um plano de campanha da Estela em vigor?
- `_investigations/concorrentes/` — há achados recentes da Íris relevantes pro pedido?
- Se o pedido menciona uma data/evento específico, ler o Google Calendar (`losmuertosdefome@gmail.com` + calendário "Música e Eventos") só pra extrair contexto factual (artista, horário) — **nunca ler ou expor valores de cachê**.

### 3. Mapear o pedido para os especialistas disponíveis

| Se o pedido envolve... | Especialista |
|---|---|
| Escrever copy (qualquer tom — orgânico, campanha, urgência) | Cris Criativa |
| Arte estática (post, story, anúncio) | Vito Visual |
| Vídeo — planejar captação ou orientar edição de material já filmado | Duda Direção |
| Publicar em plataformas | Paulo Postador |
| Campanha de tráfego pago (briefing tático, evento específico) | Ana Anúncio |
| Relatório de métricas/resultados | Rodrigo Resultados |
| Planejar a semana / reaproveitar conteúdo antigo | Lia Linha |
| Planejamento de campanha em nível de mês/calendário | Estela Estratégia |
| Análise de concorrentes locais | Íris Investigação |

Um pedido pode envolver mais de um especialista (ex: copy + visual + publicar). Incluir só os que o objetivo realmente exige.

### 4. Identificar o que falta

Para cada especialista incluído no plano, checar se o input que ele precisa já está disponível (no pedido do usuário, no contexto de fundo, ou em algo que o usuário já forneceu) ou se precisa ser perguntado. Exemplos:
- Duda precisa saber se é pré-produção (ainda vai filmar) ou pós-produção (já filmou e quer orientação de corte).
- Ana precisa de público-alvo, verba e objetivo se não há evento de calendário associado.
- Vito/Cris precisam saber se há uma copy/conceito já pronto que o usuário quer usar como input manual, em vez de gerar do zero.

### 5. Sinalizar se o projeto inclui publicação

Se o plano inclui Paulo Postador, deixar isso explícito — isso implica um checkpoint final de aprovação manual obrigatório antes de qualquer publicação, sem exceção.

### 6. Apresentar o plano e perguntar o que falta

Nunca despachar sem essa confirmação.

## Formato de Saída

Salvar em `output/plano-projeto.md`:

```markdown
# Plano do Projeto — [nome/descrição curta do projeto]

**Pedido original:** [texto do usuário]
**Objetivo identificado:** [o que o usuário realmente quer como resultado]

## Contexto de fundo consultado
- Direção semanal (Lia): [resumo de 1 linha, ou "não há direção recente"]
- Plano mensal (Estela): [resumo de 1 linha, ou "não há plano em vigor"]
- Concorrência (Íris): [resumo de 1 linha, ou "sem achados recentes"]

## Especialistas necessários
1. [Agente] — [o que vai produzir]
2. [Agente] — [o que vai produzir]

## Inclui publicação?
[SIM — checkpoint final de aprovação manual obrigatório / NÃO]

## Pendências (perguntar ao usuário antes de despachar)
- [pergunta objetiva 1]
- [pergunta objetiva 2]
- [ou "nenhuma pendência — pronto para confirmar"]
```

## Critérios de Qualidade

- [ ] Objetivo do pedido identificado com clareza, não só reformulado
- [ ] Plano lista só os especialistas necessários, sem excesso
- [ ] Contexto de fundo (Lia/Estela/Íris) consultado antes de montar o plano
- [ ] Toda pendência de input está listada como pergunta objetiva
- [ ] Sinalização clara se o projeto envolve publicação

## Condições de Veto

- **Plano com agente que decide algo baseado em cachê/valor/histórico automático** → VETO absoluto — reescrever a justificativa
- **Plano despachado sem passar pela confirmação do usuário** → bloqueio, nunca avançar sem esse checkpoint
- **Pendência de input não identificada** (especialista ficaria travado no meio do trabalho) → revisar o plano antes de apresentar
