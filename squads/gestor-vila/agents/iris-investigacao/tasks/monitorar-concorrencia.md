---
task: "Monitorar Concorrência"
order: 1
input: |
  - identity: pipeline/data/vila-identity.md — posicionamento da Vila, público
  - historico: _investigations/concorrentes/ — checagens anteriores, quando existirem
  - researching: _opensquad/core/best-practices/researching.md — metodologia
output: |
  - persist: _investigations/concorrentes/{concorrente-slug}.md — histórico atualizado por concorrente
  - file: output/{projeto}/analise-concorrencia.md — síntese do projeto
---

# Monitorar Concorrência

## Descrição

Íris atualiza o retrato dos concorrentes locais da Vila — o que mudou desde a última checagem, não uma investigação do zero.

## Processo

### 1. Definir o escopo (checkpoint obrigatório antes de rodar)

Confirmar com o usuário: quais concorrentes monitorar (3-5 locais de Bethaville/Barueri/Alphaville com proposta parecida — bar, música ao vivo, gastronomia local). Se já há histórico em `_investigations/concorrentes/`, usar a mesma lista por padrão, salvo indicação contrária.

### 2. Ler o histórico anterior

Para cada concorrente, checar se já existe `_investigations/concorrentes/{concorrente-slug}.md`. Se sim, usar a última entrada como baseline de comparação.

### 3. Coletar dados atuais

Via skill `apify` (scraping de Instagram/redes públicas) e `web_search`: frequência de posts recente, temas/formatos em uso, sinais de engajamento público, presença de anúncios pagos (Ad Library quando disponível).

### 4. Comparar com a checagem anterior

O que mudou desde a última vez? Novo formato, mudança de frequência, novo posicionamento? Se é a primeira checagem, registrar como baseline.

### 5. Registrar e persistir

Anexar uma nova entrada datada ao arquivo de cada concorrente (não sobrescrever o histórico anterior) e sintetizar no artefato do projeto.

## Formato de Saída

Por concorrente, em `_investigations/concorrentes/{concorrente-slug}.md`:

```markdown
# [Nome do Concorrente]

## Checagem — [data]
**Fonte:** [Instagram/perfil, link ou identificador]
**Frequência de posts:** [observação]
**Temas/formatos em uso:** [observação]
**Sinais de engajamento:** [observação, com fonte]
**Anúncios pagos:** [observação, com fonte]
**Mudou desde a última checagem?** [sim/não + o quê, ou "primeira checagem — baseline"]

---
[checagens anteriores permanecem abaixo, mais antiga no final]
```

Síntese em `output/{projeto}/analise-concorrencia.md`:

```markdown
# Análise de Concorrência — [data]

## Concorrentes Monitorados
1. [nome] — [resumo de 1 linha]
2. [...]

## O que mudou desde a última checagem
[resumo objetivo, por concorrente ou "primeira checagem"]

## Gaps observados
[o que nenhum concorrente está fazendo — sem recomendação, só observação factual]
```

## Critérios de Qualidade

- [ ] Pelo menos 3 concorrentes monitorados
- [ ] Toda observação tem fonte e data
- [ ] Comparação com checagem anterior presente quando histórico existir
- [ ] Histórico por concorrente preservado, nunca sobrescrito
- [ ] Nenhuma recomendação estratégica presente (isso é da Estela)

## Condições de Veto

- **Rodar sem confirmação de escopo do usuário** → bloqueio
- **Sobrescrever histórico anterior em vez de anexar** → VETO, corrigir
- **Observação sem fonte/data** → remover ou completar antes de entregar
- **Recomendação estratégica presente no output** → remover, não é papel da Íris
