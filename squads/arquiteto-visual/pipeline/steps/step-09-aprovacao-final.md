---
id: step-09
type: checkpoint
name: "Aprovação Final"
inputFile: output/review.md
---

# Step 09 — Aprovação Final

Ponto de fechamento da sessão. Vera Veredito emitiu APROVADA — o usuário confirma que está satisfeito e decide o que fazer com o conteúdo aprovado.

## Instructions

Apresentar ao usuário o resumo da sessão (review.md) e perguntar:

1. **Satisfeito com o resultado?** O conteúdo aprovado por Vera está pronto para publicar?
2. **Publicação Instagram:** O post principal (feed ou Reel) deve ser publicado agora via `instagram-publisher`?
3. **Agendamento:** Quer agendar a publicação para um horário específico ou publicar imediatamente?
4. **Aprendizados para próxima sessão:** Há algo dessa sessão que deve ser registrado na memória do squad?

## Output Format

```
=== SESSÃO ENCERRADA ===
Status: APROVADA
Peças produzidas: [lista]
Publicação Instagram: [agendada para [data/hora] / publicada — URL / pendente]
Adaptações: [lista de plataformas — status por plataforma]

=== APRENDIZADOS ===
[resumo de insights ou padrões identificados para memories.md]
```

## Post-Session Actions

Após confirmação do usuário:
1. Se publicação Instagram autorizada: chamar skill `instagram-publisher` com o post aprovado
2. Registrar aprendizados em `_memory/memories.md` (sessão, o que funcionou, o que foi ajustado)
3. Registrar run em `_memory/runs.md` com: data, ângulo, formatos, notas de Vera, status de publicação

## Veto Conditions

Não fechar sessão como encerrada se:
1. Status da sessão em `output/review.md` não é APROVADA — o Step 09 só é atingido quando Vera emitiu APROVADA
2. Publicação via instagram-publisher solicitada sem confirmação explícita do usuário

## Quality Criteria

- [ ] Usuário confirmou satisfação com o resultado
- [ ] Status de publicação definido (publicado / agendado / pendente) para cada plataforma
- [ ] Aprendizados registrados em `_memory/memories.md`
- [ ] Run registrado em `_memory/runs.md`
