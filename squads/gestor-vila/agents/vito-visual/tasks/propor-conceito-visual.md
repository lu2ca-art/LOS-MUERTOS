---
task: "Propor Conceito Visual"
order: 1
input: |
  - conteudo: output/{projeto}/conteudo.md — copy de cada slot (do Cris Criativa OU colada manualmente pelo usuário)
  - identity: pipeline/data/vila-identity.md — brand kit, paleta, fontes, assets
output: |
  - file: output/{projeto}/conceito-visual.md — descrição do conceito por slot, para aprovação
---

# Propor Conceito Visual

## Descrição

Antes de gerar qualquer arte final, Vito descreve o conceito visual de cada peça — o que vai aparecer, quais assets do brand kit, qual paleta, qual composição — e apresenta isso num checkpoint para o usuário aprovar ou redirecionar. Isso vale **sempre**, mesmo quando a copy foi colada manualmente pelo usuário em vez de vir do Cris Criativa: consistência de processo, independente de onde a copy veio.

## Processo

### 1. Ler o conteúdo de cada slot

Extrair de `conteudo.md` (ou do que o usuário forneceu diretamente):
- **POST PRINCIPAL:** elemento central (artista OU prato OU evento), horário, dia
- **STORY 1:** pergunta interativa, tom
- **STORY 2:** detalhe concreto, CTA físico
- **STORY CHEF ALEX** (se presente): roteiro de bastidor
- **STORY SHOW** (se presente): artista, horário, tom festivo
- **ANÚNCIO PAGO** (se presente): evento, headline

### 2. Montar o conceito por slot

Para cada peça, descrever (sem gerar nada ainda):
- Formato (1080×1350 feed / 1080×1920 story / 1080×1080 anúncio)
- Elemento central da composição
- Qual mascote (Cachorro ou Gato) e por quê
- Qual logo (com mascotes ou texto)
- Paleta principal daquela peça (2-3 cores da paleta oficial)
- Tipografia e tom geral

Usar `pipeline/data/vila-identity.md` (diretrizes por slot, tabela de assets) como base — nunca inventar assets ou cores fora do brand kit oficial.

### 3. Apresentar para aprovação

O conceito é sempre um checkpoint — nunca gerar a arte final sem essa aprovação, mesmo que o pedido pareça simples ou a copy já esteja pronta.

## Formato de Saída

```markdown
# Conceito Visual — [projeto]

## POST PRINCIPAL
**Formato:** 1080×1350px
**Elemento central:** [artista/prato/evento]
**Mascote:** [Cachorro/Gato — motivo]
**Logo:** [com mascotes/texto]
**Paleta:** [2-3 cores]
**Composição:** [descrição curta]

## STORY 1 — Engajamento
[mesma estrutura]

## STORY 2 — Informação
[mesma estrutura]

## STORY CHEF ALEX (se presente)
[mesma estrutura]

## STORY SHOW (se presente)
[mesma estrutura]

## ANÚNCIO PAGO (se presente)
[mesma estrutura]

---
**Pronto para gerar a arte final? Aguardando aprovação.**
```

## Critérios de Qualidade

- [ ] Todo slot presente no conteúdo tem um conceito correspondente
- [ ] Assets (mascote, logo) escolhidos conforme a tabela de diretrizes de `vila-identity.md`
- [ ] Paleta usada é só a paleta oficial da Vila
- [ ] Nenhuma arte é gerada nesta task — só o conceito

## Condições de Veto

- **Conceito com brand kit ou asset fora do padrão oficial** → revisar antes de apresentar
- **Avançar para geração de arte sem essa etapa** → bloqueio, nunca pular o conceito
