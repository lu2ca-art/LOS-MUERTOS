---
task: "Roteirizar Pré-Produção"
order: 1
input: |
  - projeto: output/plano-projeto.md — evento, data, horário (quando aplicável)
  - identity: pipeline/data/vila-identity.md — diferenciais de conteúdo, formato de vídeo
  - research: pipeline/data/research-brief.md — formatos de vídeo com melhor desempenho
output: |
  - file: output/{projeto}/roteiro-video.md — shot list numerado para captação
---

# Roteirizar Pré-Produção

## Descrição

Antes de filmar, Duda monta o shot list: o que captar, em que ordem, por quanto tempo. É um roteiro prático para quem vai gravar com o celular durante o evento ou o dia a dia da Vila — não uma produção audiovisual elaborada.

## Processo

### 1. Identificar o contexto do vídeo

Do plano do projeto ou do pedido direto: é vídeo de show/evento, de bastidor do Chef Alex, do ambiente/salão, ou outro?

### 2. Montar o shot list

Para cada cena: descrição do plano, duração alvo, o que deve estar em quadro. Regras:
- Gancho forte na Cena 1 — o que teria que aparecer nos 2 primeiros segundos para prender atenção
- Pelo menos um plano de comida, salão ou Chef Alex, mesmo em vídeo de show — o restaurante nunca some do corte
- Duração total alvo: 15-30s
- Ordem pensada para edição — cenas na sequência que vão aparecer no corte final, não na ordem de captação

### 3. Definir o momento de captação

Quando captar cada cena (ex: "salão cheio — captar no pico da noite, não na abertura"; "Chef Alex — captar durante o preparo, não posado").

## Formato de Saída

```markdown
# Roteiro de Vídeo (Pré-Produção) — [projeto]

**Contexto:** [evento/dia a dia — o que é o vídeo]
**Duração alvo:** [15-30s]

## Shot List

### Cena 1 — Gancho (0-2s)
**O quê:** [descrição do plano]
**Quando captar:** [momento ideal]
**Duração:** [Xs]

### Cena 2
[mesma estrutura]

### Cena 3
[mesma estrutura]

[...]

## Observações
[qualquer detalhe prático — luz, som ambiente, o que evitar]
```

## Critérios de Qualidade

- [ ] Gancho definido para os 2 primeiros segundos
- [ ] Pelo menos uma cena de comida/salão/Chef Alex presente
- [ ] Duração de cada cena especificada
- [ ] Duração total dentro de 15-30s
- [ ] Momento de captação claro para cada cena

## Condições de Veto

- **Shot list sem cena de comida/restaurante em vídeo de show** → revisar, o restaurante é sempre protagonista
- **Duração total fora de 15-30s sem justificativa** → ajustar
- **Cena sem gancho na abertura** → redesenhar a Cena 1
