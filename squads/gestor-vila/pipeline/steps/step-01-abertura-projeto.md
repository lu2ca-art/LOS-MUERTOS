---
id: step-01
type: checkpoint
name: "Abertura do Projeto"
outputFile: output/plano-projeto.md
---

# Step 01 — Abertura do Projeto

## Context Loading

Nenhum contexto prévio — este é sempre o primeiro passo de qualquer execução da agência.

## Instructions

1. Perguntar ao usuário o que ele quer fazer, em texto livre (ex: "projeto story almoço", "preciso de uma copy pro vídeo que já filmei", "projeto: análise de concorrência").
2. Não interpretar ainda — só capturar o pedido tal como veio.
3. Classificar internamente (para o step seguinte decidir se roda a triagem do Beto): o pedido é amplo/ambíguo (envolve vários especialistas ou não está claro o que exatamente é necessário) ou específico (já nomeia o agente ou a entrega exata, ex: "Cris, escreve uma copy pra isso aqui")?
4. Registrar essa classificação como `pedido_amplo_ou_ambiguo: true/false` no início do arquivo de saída — isso decide se o Step 02 (triagem do Beto) roda ou é pulado.

## Output Format

```markdown
# Plano do Projeto

pedido_amplo_ou_ambiguo: [true/false]

## Pedido Original
[texto exato do usuário]
```

## Output Example

```markdown
# Plano do Projeto

pedido_amplo_ou_ambiguo: true

## Pedido Original
projeto story almoço, iniciar pipe
```

Exemplo de pedido específico (pula triagem):

```markdown
# Plano do Projeto

pedido_amplo_ou_ambiguo: false

## Pedido Original
Cris, preciso de uma copy pro vídeo que eu já filmei do show de sábado — contexto: LU2CA tocou, salão cheio, quero postar hoje.
```

## Veto Conditions

- Prosseguir sem capturar o pedido literal do usuário → bloqueio
- Classificar como amplo/ambíguo ou específico sem justificativa clara → revisar antes de salvar

## Quality Criteria

- [ ] Pedido original capturado sem reinterpretação
- [ ] Classificação amplo/ambíguo vs. específico registrada
- [ ] Nenhum trabalho de especialista começou ainda neste step
