---
id: step-08
type: agent
agent: duda-direcao
execution: subagent
model_tier: fast
name: "Roteirizar Vídeo (Pré-Produção)"
inputFile: output/plano-projeto.md
outputFile: output/roteiro-video.md
---

# Step 08 — Roteirizar Vídeo (Pré-Produção)

## Context Loading

Duda carrega: `output/plano-projeto.md`, `pipeline/data/vila-identity.md`, `pipeline/data/research-brief.md`.

## Instructions

Este step só roda quando `plano.inclui_video_pre_producao == true` — ou seja, o usuário ainda vai filmar e quer um shot list.

**Executar apenas `tasks/roteirizar-pre-producao.md` neste step.**

1. Identificar o contexto do vídeo (show, bastidor, ambiente).
2. Montar o shot list numerado com duração e momento de captação por cena.
3. Garantir gancho nos 2 primeiros segundos e presença do restaurante no corte.

## Output Format

Ver `tasks/roteirizar-pre-producao.md` — Formato de Saída.

## Output Example

```markdown
# Roteiro de Vídeo (Pré-Produção) — show de sexta

**Contexto:** show ao vivo, RUNA, 20h
**Duração alvo:** 20s

## Shot List

### Cena 1 — Gancho (0-2s)
**O quê:** close no salão cheio, gente cantando junto
**Quando captar:** pico da noite, por volta das 20h30
**Duração:** 3s

### Cena 2
**O quê:** RUNA tocando, plano médio
**Quando captar:** durante o show
**Duração:** 5s

### Cena 3
**O quê:** prato saindo da cozinha, Chef Alex ao fundo
**Quando captar:** entre 20h-20h15, antes do pico do show
**Duração:** 4s

## Observações
Captar com celular na horizontal do salão pra Cena 1, luz baixa — usar modo noturno se disponível.
```

## Veto Conditions

- Shot list sem cena de comida/salão/Chef Alex → revisar, restaurante sempre protagonista
- Cena sem gancho na abertura → redesenhar Cena 1

## Quality Criteria

- [ ] Duração de cada cena especificada
- [ ] Duração total entre 15-30s
- [ ] Pelo menos uma cena do restaurante presente
