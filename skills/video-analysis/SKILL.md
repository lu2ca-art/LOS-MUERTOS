---
name: video-analysis
description: >
  Watch raw video footage (visual + audio/speech) and identify key moments,
  timestamps, and editing recommendations, without requiring the user to
  describe the footage manually. PLACEHOLDER — not yet configured. Requires
  a video-understanding API/model access from the user before use.
description_pt-BR: >
  Assiste material de vídeo bruto (visual + áudio/fala) e identifica momentos-chave,
  timestamps e recomendações de edição, sem exigir que o usuário descreva o
  material manualmente. PLACEHOLDER — ainda não configurada. Precisa de acesso
  a uma API/modelo de compreensão de vídeo fornecido pelo usuário antes de usar.
type: mcp
version: "0.1.0-placeholder"
mcp:
  server_name: video-analysis
  command: npx
  args: ["-y", "video-analysis-mcp"]
  transport: stdio
env:
  - VIDEO_ANALYSIS_API_KEY
categories: [video, content-production]
status: placeholder
---

# Video Analysis — Skill (Placeholder)

## Status: aguardando configuração

Esta skill ainda não está configurada. `VIDEO_ANALYSIS_API_KEY` não está definida. Até ser fornecida:

- **Duda Direção** (`squads/gestor-vila/agents/duda-direcao`), na task de pós-produção (`orientar-edicao.md`), apresenta o aviso "Orientação de edição indisponível — skill video-analysis aguardando configuração" e não executa a análise.
- A pré-produção do Duda (shot list, `roteirizar-pre-producao.md`) **não depende** desta skill e continua funcionando normalmente.
- Nenhum outro agente depende desta skill.

## When to use (após configurada)

Use esta skill quando o Duda Direção precisar assistir um vídeo bruto fornecido pelo usuário (show, bastidor, etc.) para identificar os melhores trechos e montar uma orientação de corte — nunca para substituir isso por pedir ao usuário que descreva o vídeo manualmente.

## Instructions (após configurada)

1. Receber o arquivo de vídeo fornecido pelo usuário.
2. Processar visual e áudio/fala do material completo.
3. Identificar: trechos de maior energia/movimento, presença de pessoas/comida/ambiente, qualidade técnica de cada trecho (tremido, escuro, etc.).
4. Retornar timestamps de entrada/saída dos melhores momentos para o Duda montar a orientação de corte — esta skill não decide a ordem final, só identifica o material bruto.

## Setup

1. Escolher um provedor de análise de vídeo com suporte nativo a vídeo (ex: um modelo multimodal com input de vídeo).
2. Gerar a credencial de API do provedor escolhido.
3. Definir `VIDEO_ANALYSIS_API_KEY` no ambiente (`.env` ou `.claude/settings.local.json`, conforme o mecanismo de configuração de MCP do projeto).
4. Reinstalar/resolver a skill — o runner do Opensquad detecta a configuração automaticamente na próxima execução.

## Nunca

- Nunca pedir ao usuário para descrever o vídeo frame a frame como alternativa a esta skill — se ela não está configurada, a resposta correta é o aviso de "aguardando configuração", não um substituto manual forçado.
