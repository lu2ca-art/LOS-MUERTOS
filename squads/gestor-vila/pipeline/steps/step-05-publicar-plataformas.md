---
step: 05
name: "Publicar em Plataformas"
type: distribution
agent: paulo-postador
execution: subagent
requires_approval: true
---

# Step 05 — Publicar em Plataformas

## Objetivo

Paulo Postador publica o conteúdo aprovado em todas as plataformas, reportando URL de cada publicação.

## Agente Ativo

**Paulo Postador** — Publicador Multiplataforma

## Pré-requisito

Aprovação explícita do usuário registrada no Step 04. Sem aprovação, este step não executa.

## Tasks

Executar `agents/paulo-postador/tasks/publicar-plataformas.md`:

1. Verificar aprovação do Step 04
2. Adaptar copy por plataforma (Instagram, Facebook, TikTok, Google Meu Negócio)
3. Verificar horário ideal de publicação
4. Executar dry-run (credenciais + formato + caracteres)
5. Publicar plataforma por plataforma na ordem: Instagram → Facebook → TikTok → Google Meu Negócio
6. Reportar URL de cada publicação
7. Salvar relatório em `output/publicacoes.md`

## Output Esperado

- `output/publicacoes.md` com status e URLs de todas as plataformas

## Prosseguir para Steps 06 e 07 em paralelo.
