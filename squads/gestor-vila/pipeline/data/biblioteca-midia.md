# Biblioteca de Mídia Real — Vila Los Muertos de Fome

Fonte real de material bruto para o Vini Vídeo (e assets visuais para o Vito Visual).
**Pasta compartilhada no iCloud do usuário — somente leitura.** Nunca mover, renomear ou
apagar nada aqui; qualquer output vai para `squads/gestor-vila/output/`, nunca para dentro
desta pasta.

## Caminho base

```
/Users/lu2ca/Library/Mobile Documents/com~apple~CloudDocs/LOS MUERTOS MIDIA/ mídia/
```

**Atenção de encoding:** o nome da subpasta é literalmente `" mídia"` — com um espaço no
início. Ao acessar via script/shell, resolva o nome exato com `os.listdir()` (Python) em vez
de digitar o caminho à mão — o acento em "í" pode estar em forma decomposta (NFD) e não bater
com o que parece igual visualmente.

## Pastas por tema

| Pasta | Vídeos | Tamanho aprox. | Mapeamento sugerido de pilar |
|-------|--------|-----------------|-------------------------------|
| `almoço/` | 72 | 775 MB | Rodízio (terça/quinta), gastronômico/sensorial |
| ` drinks/` *(nota o espaço no início)* | 145 | 3.1 GB | Happy hour, sexta cultural |
| `copa/` | 27 | 2.4 GB | Copa do Mundo 2026 — telão, torcida |
| `música/` | 67 | 2.4 GB | Shows ao vivo qui-sex-sáb |
| `mexicano/` | 22 | 320 MB | Identidade Tex Mex BR, cultural/identitário |
| `lanches e  burgers/` | 17 | 251 MB | Cardápio, porções |
| `dancinhaholic/` | 14 | 511 MB | Conteúdo de engajamento/trend, casual |
| `edits/` | 32 | 409 MB | Clipes já cortados/prontos de sessões anteriores — checar antes de reeditar do zero |
| `porções/` | 3 | 82 MB | Rodízio, prato do dia |
| `Fotos/` | 0 vídeos, 147 fotos | 359 MB | Imagens estáticas — não usar no Vini, mas útil pro Vito Visual |
| `pngs/` | 0 | 9 MB | Assets de design (exports do Canva) |
| `detalhes/`, `feed semanal/`, `reels semanal/`, `story semanal/` | vazias | — | Pastas-destino ainda não usadas — podem virar convenção de "selecionados para postar" |

## Como usar

1. Antes de montar um plano de edição, listar os arquivos da pasta temática relevante
   (`os.listdir` via Python, não `ls` com o caminho digitado à mão).
2. Escolher os clipes pelo nome/data de modificação — nomes como `IMG_0700.MOV` não indicam
   conteúdo, então quando possível confirmar com o usuário qual clipe é qual antes de montar
   o plano final.
3. Vídeos filmados no iPhone têm metadado de rotação — o skill `video-editor` já corrige isso
   automaticamente (ver `skills/video-editor/scripts/edit.py`, função `detect_rotation`).
4. Nunca escrever, mover ou apagar nada dentro desta biblioteca — é a pasta de origem
   compartilhada, não um scratch space.
