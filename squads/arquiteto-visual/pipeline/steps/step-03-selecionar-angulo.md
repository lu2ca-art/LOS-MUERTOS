---
id: step-03
type: checkpoint
name: "Selecionar Ângulo"
inputFile: output/angulos.md
outputFile: output/angulo-selecionado.md
---

# Step 03 — Selecionar Ângulo

O usuário escolhe qual dos 5 ângulos será desenvolvido na sessão e confirma o tom de voz. Bruno Brainstorm pode ajustar a linha de abertura se o usuário quiser iterar antes de avançar para Carlos Caption.

## Instructions

Após apresentar os 5 ângulos do Step 02, perguntar:

1. **Qual ângulo?** Qual dos 5 ângulos deseja desenvolver? (ou o usuário pode propor variação)
2. **Tom confirmado?** O tom de voz sugerido para o ângulo está correto? (Lírico, Filosófico, Motivacional, Comunitário, Cultural, Vulnerável)
3. **Linha de abertura:** A linha de abertura de exemplo está boa ou quer ajustar antes de Carlos Caption escrever?

## Output Format

```
=== ÂNGULO SELECIONADO ===
Ângulo: [nome em caps]
Lens: [perspectiva em 1 frase]
Linha de abertura: "[linha final aprovada]"
Tom confirmado: [nome do tom]
Formato principal: [Reel / feed / Stories]
```

## Output Example

```
=== ÂNGULO SELECIONADO ===
Ângulo: FÍSICO/MOVIMENTO
Lens: o corpitcho que resiste à segunda-feira com velocidade
Linha de abertura: "posso não saber tudo. só não posso ficar parado."
Tom confirmado: Motivacional/Movimento
Formato principal: Reel + feed de suporte
```

## Veto Conditions

Não avançar para o Step 04 se:
1. Tom de voz não foi confirmado — Carlos Caption precisa do tom para calibrar estrutura e vocabulário
2. Formato principal não está claro — determina qual task Carlos Caption vai executar (criar-reel vs criar-feed)

## Quality Criteria

- [ ] Ângulo selecionado pelo usuário (não imposto pelo sistema)
- [ ] Tom de voz explicitamente confirmado
- [ ] Linha de abertura aprovada (original ou ajustada)
- [ ] Output salvo em `output/angulo-selecionado.md`
