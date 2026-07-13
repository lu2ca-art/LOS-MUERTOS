---
id: step-10
type: agent
agent: duda-direcao
execution: subagent
model_tier: powerful
name: "Orientar Edição (Pós-Produção)"
outputFile: output/orientacao-edicao.md
---

# Step 10 — Orientar Edição (Pós-Produção)

## Context Loading

Duda carrega: material de vídeo bruto fornecido pelo usuário, `pipeline/data/vila-identity.md`.

## Instructions

Este step só roda quando `plano.inclui_video_pos_producao == true` — o usuário já filmou e quer orientação de corte.

**Executar apenas `tasks/orientar-edicao.md` neste step.**

1. Verificar se a skill `video-analysis` está configurada.
2. Se não estiver: apresentar o aviso de "aguardando configuração" e parar aqui — não pedir ao usuário para descrever o vídeo manualmente.
3. Se estiver configurada: assistir o material via skill, montar a orientação de corte com timestamps.

## Output Format

Ver `tasks/orientar-edicao.md` — Formato de Saída.

## Output Example

```markdown
# Orientação de Edição — show de sábado

**Material analisado:** video_show_sabado.mp4
**Duração do corte proposto:** 22s

## Ordem de Corte

### 1. 0:14-0:17
**O quê:** salão cheio, gente cantando
**Por quê:** gancho — energia imediata

### 2. 0:32-0:38
**O quê:** LU2CA tocando, plano médio
**Por quê:** conteúdo principal do show

### 3. 1:05-1:09
**O quê:** prato saindo da cozinha
**Por quê:** presença do restaurante no corte

## Trechos descartados
- 0:00-0:14 — câmera tremida, sem energia

## Observação
Material tinha boa presença de comida — nenhum ajuste necessário quanto a isso.
```

Exemplo quando a skill não está configurada:

```
⚠️ Orientação de edição indisponível — skill video-analysis aguardando configuração.
A pré-produção (shot list) continua disponível normalmente.
```

## Veto Conditions

- Executar sem a skill configurada, tentando adivinhar o conteúdo → bloqueio absoluto
- Pedir ao usuário para descrever o vídeo manualmente → nunca

## Quality Criteria

- [ ] Skill verificada antes de qualquer tentativa de análise
- [ ] Se configurada: timestamps exatos do material original
- [ ] Se não configurada: aviso claro apresentado, sem simular análise
