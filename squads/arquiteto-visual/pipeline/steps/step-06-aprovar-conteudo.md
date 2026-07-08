---
id: step-06
type: checkpoint
name: "Aprovar Conteúdo"
inputFile: output/conteudo-instagram.md
---

# Step 06 — Aprovar Conteúdo

O usuário revisa o conteúdo completo de Carlos Caption e o visual de Diana Design antes de avançar para adaptações multiplataforma e revisão formal. Este checkpoint impede que adaptações sejam produzidas para conteúdo que o usuário ainda quer ajustar.

## Instructions

Apresentar ao usuário:
- O conteúdo de `output/conteudo-instagram.md` (script, caption, stories)
- O visual de `output/visual-01.jpg` (quando disponível)

Depois perguntar:

1. **Conteúdo aprovado?** O script/caption/stories estão prontos para avançar?
2. **Visual aprovado?** O visual de fundo está alinhado com a era CIDADE NEON?
3. **Plataformas a adaptar:** Quais plataformas devem receber adaptações nesta sessão? (confirmar ou ajustar o que foi definido no Step 01)
4. **Publicação autorizada?** Rafael Repercussão pode publicar diretamente nas plataformas ou apenas produzir rascunhos?

## Output Format

```
=== APROVAÇÃO DE CONTEÚDO ===
Conteúdo Instagram: [APROVADO / AJUSTAR — descrição do ajuste]
Visual: [APROVADO / AJUSTAR — descrição do ajuste / AGUARDANDO se ainda não entregue]
Plataformas para adaptar: [lista confirmada]
Publicação: [AUTORIZADA / APENAS RASCUNHO]
```

## Veto Conditions

Não avançar para o Step 07 se:
1. Usuário pediu ajuste no conteúdo — voltar ao Step 04 com o feedback
2. Publicação não foi explicitamente confirmada como "autorizada" ou "apenas rascunho" — Rafael precisa saber antes de começar

## Quality Criteria

- [ ] Usuário revisou o conteúdo (não apenas o pipeline avançou automaticamente)
- [ ] Status de publicação definido (autorizada vs rascunho)
- [ ] Plataformas adicionais confirmadas
- [ ] Ajustes solicitados registrados para retorno ao Step 04, se necessário
