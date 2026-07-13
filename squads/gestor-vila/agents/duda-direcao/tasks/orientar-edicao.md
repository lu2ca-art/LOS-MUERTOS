---
task: "Orientar Edição"
order: 2
input: |
  - material_bruto: vídeo(s) fornecido(s) pelo usuário
  - identity: pipeline/data/vila-identity.md — diferenciais de conteúdo
skill: video-analysis
output: |
  - file: output/{projeto}/orientacao-edicao.md — orientação de corte com timestamps
---

# Orientar Edição

## Descrição

Quando o usuário já filmou o material sozinho e quer orientação de corte, Duda assiste o vídeo bruto de verdade — via skill `video-analysis` — e monta a orientação de edição: o que manter, o que descartar, a ordem final. Duda nunca pede pro usuário descrever o vídeo manualmente.

## Placeholder — aguardando configuração

A skill `video-analysis` ainda não está configurada (depende de credenciais de API que o usuário vai fornecer). Até lá:
- Esta task fica **bloqueada** com aviso claro: "Orientação de edição indisponível — skill video-analysis aguardando configuração."
- A pré-produção (`roteirizar-pre-producao.md`) continua funcionando normalmente, sem depender disso.
- Assim que a skill estiver configurada, esta task passa a funcionar sem nenhuma mudança de processo.

## Processo (quando a skill estiver configurada)

### 1. Assistir o material bruto

Usar a skill `video-analysis` para processar o(s) vídeo(s) fornecido(s) — visual e áudio/fala. Nunca substituir isso por perguntar ao usuário o que tem no vídeo.

### 2. Identificar os melhores momentos

Do material completo, identificar: os trechos com energia real (show, salão cheio, reação genuína), qualquer aparição do Chef Alex ou da comida, e o melhor candidato a gancho de abertura.

### 3. Montar a orientação de corte

Definir a ordem final, os timestamps exatos de entrada/saída de cada trecho, e a duração total do corte proposto (alvo: 15-30s).

### 4. Garantir que o restaurante aparece

Se o material é de um show e não há nenhum plano de comida/salão/Chef Alex, sinalizar isso explicitamente — não impor um corte que exclua o restaurante sem avisar.

## Formato de Saída

```markdown
# Orientação de Edição — [projeto]

**Material analisado:** [arquivo(s) fornecido(s)]
**Duração do corte proposto:** [Xs]

## Ordem de Corte

### 1. [timestamp original, ex: 0:04-0:09]
**O quê:** [descrição do trecho]
**Por quê:** [motivo — gancho, energia, restaurante]

### 2. [timestamp original]
[mesma estrutura]

[...]

## Trechos descartados (e por quê)
- [timestamp] — [motivo do descarte]

## Observação
[se faltou plano de comida/salão/Chef Alex no material bruto, sinalizar aqui]
```

## Critérios de Qualidade

- [ ] Material bruto assistido de verdade via skill, nunca descrito pelo usuário
- [ ] Ordem final com timestamps exatos do material original
- [ ] Duração do corte proposto entre 15-30s
- [ ] Presença do restaurante confirmada ou sinalizada como ausente

## Condições de Veto

- **Task executada sem a skill video-analysis configurada** → bloqueio, apresentar aviso de configuração pendente
- **Pedir ao usuário para descrever o vídeo manualmente** → nunca, isso anula o propósito da task
- **Corte sem nenhuma referência ao restaurante, sem sinalizar isso ao usuário** → revisar antes de entregar
