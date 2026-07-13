---
id: step-04
type: agent
agent: cris-criativa
execution: inline
name: "Criar Conteúdo"
inputFile: output/plano-projeto.md
outputFile: output/conteudo.md
---

# Step 04 — Criar Conteúdo

## Context Loading

Cris carrega: `output/plano-projeto.md` (plano confirmado), `pipeline/data/vila-identity.md`, `pipeline/data/tone-of-voice.md`, `pipeline/data/output-examples.md`, `pipeline/data/anti-patterns.md`, `pipeline/data/direcao-semanal-atual.md` (quando existir).

## Instructions

Este step só roda quando `plano.inclui_copy == true`.

1. Executar `tasks/criar-conteudo-diario.md` para o conteúdo orgânico do dia.
2. Se o plano também indica copy de campanha/evento (`plano.inclui_trafego_pago == true` ou pedido explícito de copy de evento), executar em seguida `tasks/criar-copy-campanha.md`, anexando ao mesmo `conteudo.md`.
3. Nunca escrever copy de campanha sem esse pedido explícito no plano.
4. Verificar hard caps antes de salvar.

## Output Format

Ver `tasks/criar-conteudo-diario.md` e `tasks/criar-copy-campanha.md` — Formato de Saída.

## Output Example

```markdown
# Conteúdo do Dia — Terça, 14/07

**Categoria do dia:** Rodízio v1
**Tom principal:** Gastronômico/Sensorial

## POST PRINCIPAL

nachos crocantes, guacamole feito na hora, jalapeño na medida certa. o Alex caprichou.
terça é dia de rodízio na Vila — variedade sem parar de sair da cozinha.
a partir das 19h. Rua Caldas Novas 49, Bethaville.
chega com fome.

## STORY 1 — Rodízio
Qual mesa você escolhe numa terça assim? 🌮

## STORY 2 — Cardápio
hoje o nacho vem com um toque novo. pergunta pro garçom.

## STORY CHEF ALEX
hoje o Alex testou uma versão nova do guacamole. aprovado pela equipe.

## Status
- [x] Hard caps H1-H4 verificados
- [x] Todos os slots com categoria/tema concreto
- [x] Pronto para Vito Visual
```

## Veto Conditions

- Copy de campanha gerada sem `plano.inclui_trafego_pago == true` ou pedido explícito → VETO
- Qualquer valor de cachê ou dado financeiro interno presente → VETO absoluto

## Quality Criteria

- [ ] Post principal ≤ 3 linhas
- [ ] Tom correto para o tipo de dia/projeto
- [ ] Nenhuma marketing language proibida
- [ ] Hard caps H1-H4 verificados antes de salvar
