---
task: "Editar Vídeo"
order: 1
input: |
  - material_bruto: biblioteca real em pipeline/data/biblioteca-midia.md (pasta iCloud compartilhada, somente leitura)
  - pedido: descrição do usuário do vídeo desejado (ocasião, plataforma de destino, tom)
  - anti-padroes: pipeline/data/anti-patterns.md
output: |
  - file: output/YYYY-MM-DD-HHmmss/video-final.mp4
  - file: output/YYYY-MM-DD-HHmmss/edit-plan.json — plano usado no render
---

# Editar Vídeo

## Descrição

Vini monta um vídeo curto a partir de clipes brutos já existentes, usando o skill `video-editor`
(FFmpeg local, sem custo). Ele nunca inventa cenas — só monta com o que já foi filmado.

## Processo

### 1. Verificar ambiente

Rodar `ffmpeg -version`. Se não encontrado, parar e reportar as instruções de instalação de
`skills/video-editor/SKILL.md` — não seguir sem o FFmpeg disponível.

### 2. Levantar material disponível

Consultar `pipeline/data/biblioteca-midia.md` pra identificar a pasta temática certa (ex:
`música/` pra show, `copa/` pra Copa do Mundo, `almoço/`/`porções/` pra rodízio) e listar os
arquivos dessa pasta na biblioteca real (via `os.listdir` em Python — nunca digitar o caminho
de `" mídia"` à mão, o acento pode estar em forma decomposta e não bater). Se o pedido do
usuário exigir uma cena que não existe em nenhuma pasta temática, parar e reportar **Material
faltando:** com o que falta ser filmado — não montar um plano com arquivo fictício.

### 3. Definir formato de destino

Confirmar com o pedido do usuário (ou inferir da plataforma mencionada):
- Reels / Stories / TikTok → `9:16`, `1080x1920`
- Feed → `1:1`, `1080x1080`
- YouTube → `16:9`, `1920x1080`

### 4. Montar o plano de edição (`edit-plan.json`)

Selecionar os clipes relevantes, definir `start`/`end` de corte pra cada um, escrever legendas
curtas (≤ 6 palavras/linha, sem linguagem vetada por `anti-patterns.md`), e escolher trilha
opcional com volume entre 0.15–0.3.

### 5. Apresentar o plano e pedir aprovação

Mostrar a lista de clipes usados, cortes, legendas e trilha antes de renderizar. Só renderizar
depois de confirmação explícita — igual ao checkpoint de publicação do Paulo Postador.

### 6. Renderizar

```bash
python3 skills/video-editor/scripts/edit.py \
  --plan "squads/gestor-vila/output/YYYY-MM-DD-HHmmss/edit-plan.json" \
  --output "squads/gestor-vila/output/YYYY-MM-DD-HHmmss/video-final.mp4"
```

### 7. Verificar e reportar

Confirmar que `video-final.mp4` existe no disco antes de reportar sucesso. Reportar duração,
tamanho do arquivo e caminho.

## Formato do `edit-plan.json`

```json
{
  "clips": [
    {"file": "squads/gestor-vila/output/raw/chef-alex-1.mp4", "start": "00:00:02", "end": "00:00:07"}
  ],
  "captions": [
    {"text": "bastidor com o chef alex", "start": "00:00:00", "end": "00:00:03"}
  ],
  "music": {"file": "squads/gestor-vila/assets/trilha.mp3", "volume": 0.25},
  "aspect_ratio": "9:16",
  "resolution": "1080x1920"
}
```

## Critérios de Qualidade

- [ ] Todo clipe do plano confirmado existente antes do render
- [ ] Formato de destino correto pra plataforma pedida
- [ ] Legendas curtas, sem linguagem vetada
- [ ] Plano apresentado e aprovado antes do render
- [ ] Arquivo final verificado no disco, com duração e tamanho reportados

## Condições de Veto

- **Cena pedida sem material bruto correspondente** → parar, reportar Material faltando, não montar plano fictício
- **Render sem aprovação do plano** → vetado, mesma regra do checkpoint de publicação
- **Legenda com linguagem vetada por `anti-patterns.md`** → reescrever antes de incluir no plano
