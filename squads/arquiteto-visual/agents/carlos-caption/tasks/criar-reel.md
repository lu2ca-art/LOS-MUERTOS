---
task: "Criar Reel"
order: 1
input: |
  - angulo_selecionado: O ângulo escolhido por Bruno Brainstorm com lens e linha de abertura
  - tom_confirmado: Tom de voz escolhido (Lírico, Filosófico, Motivacional, Comunitário, Cultural, Vulnerável)
output: |
  - reel_script: Script completo com HOOK, SETUP, DELIVERY, LOOP, CTA
  - caption: Caption de feed para acompanhar o Reel (≤3 linhas)
---

# Criar Reel

Carlos Caption transforma o ângulo selecionado num script completo de Reel para Instagram — pronto para gravar, com hook em 0-2s, delivery com indicação de cortes, loop design e CTA específico — mais a caption de acompanhamento.

## Process

1. **Carregar tom:** Ler `pipeline/data/tone-of-voice.md` e identificar as características do tom confirmado pelo usuário. Carregar `pipeline/data/lu2ca-universe.md` para internalizar o vocabulário ativo da era.

2. **Construir HOOK (0-2s):** Escrever a abertura que decide se o viewer fica ou swipa. Deve usar a linha de abertura do ângulo como base ou superá-la. Especificar: [Visual] (o que aparece na tela), [Audio] (música, som ambiente, silêncio), [Text Overlay] (máx 10 palavras em tela). Nunca logo, nunca "ei pessoal".

3. **Construir SETUP (2-5s):** Contexto em 1-2 frases máximo. Estabelece o "por quê" sem explicar demais. Especificar ação visual ou corte de câmera.

4. **Construir DELIVERY (5-60s):** Entrega do conteúdo principal. Indicar cortes ou ângulos de câmera a cada 3-5 segundos. Escrever o que é falado ou aparece em tela. Manter o vocabulário de LU2CA ativo.

5. **Projetar LOOP:** Especificar como o final do Reel conecta visual ou narrativamente ao início. O loop incentiva replay — um dos maiores sinais algorítmicos. Ex: "freeze frame do final funde com o close de abertura".

6. **Escrever CTA (últimos 3-5s):** 1 pergunta direta ao viewer ou 1 ação específica. Nunca "me siga" — o follow vem da qualidade. Ex: "e você, vai ficar parado essa semana?" ou "↓ comenta o nome".

7. **Escrever caption:** Linha 1 = hook autônomo ≤125 chars. Linhas 2-3 (máx) = desenvolvimento ou vocabulário de LU2CA. Zero hashtags. Tudo minúsculo exceto projeto em CAPS.

## Output Format

```
=== REEL SCRIPT ===

HOOK (0-2s):
[Visual]: [O que aparece na tela — ação, cena, close]
[Audio]: [Música, som, silêncio — especificar]
[Text Overlay]: "[texto em tela — máx 10 palavras]"

SETUP (2-5s):
[Visual]: [Corte ou transição]
[Script]: "[fala ou texto — 1-2 frases]"

DELIVERY ([X]s-[Y]s):
[Visual]: [Sequência de cenas com indicação de corte a cada 3-5s]
[Script]: "[fala principal — vocabulário de LU2CA]"
[Text Overlay]: "[palavra-chave em tela com emoji]"

LOOP:
[Descrição de como o final conecta ao início]

CTA (últimos 3-5s):
[Visual]: [Frame final]
[Script]: "[pergunta ou ação direta]"
[Text Overlay]: "[CTA em tela]"

=== CAPTION ===
[linha 1 — hook autônomo ≤125 chars]

[linha 2-3 opcional — vocabulário LU2CA ou desenvolvimento]
```

## Output Example

> Use como referência de qualidade, não como template rígido.

```
=== REEL SCRIPT ===

HOOK (0-2s):
[Visual]: close do rosto ao sair da cama — câmera lenta, iluminação neon de janela
[Audio]: beat de abertura de 'Sexta-Feira' (LU2CA, Pinotti) — corte seco no beat
[Text Overlay]: "segunda não vence"

SETUP (2-5s):
[Visual]: corte para tênis no chão sendo calçado
[Script]: "posso até não saber muito sobre isso ou aquilo."

DELIVERY (5-20s):
[Visual]: skate em rua iluminada por neon → corte → mãos no volante → corte → caminhada rápida
[Script]: "só não posso ficar parado."
[Text Overlay]: "mexe o corpitcho bebe 🛹"

LOOP:
Freeze no frame do olhar direto à câmera → funde com o close do rosto na cama do HOOK.
Quem replay vê a conexão imediata.

CTA (últimos 3-5s):
[Visual]: freeze final olhando diretamente à câmera
[Script]: "e você, vai ficar parado essa semana?"
[Text Overlay]: "↓ comenta"

=== CAPTION ===
posso até não saber muito sobre isso ou aquilo, só não posso ficar parado.

mexe o corpitcho bebe, se cair levanta 🛹
```

## Quality Criteria

- [ ] Hook especificado com [Visual], [Audio] e [Text Overlay] — nenhum campo vazio
- [ ] Hook usa a linha de abertura do ângulo ou a supera
- [ ] Delivery tem indicação de corte a cada 3-5s
- [ ] Loop design especificado — como o final conecta ao início
- [ ] CTA é pergunta ou ação específica — nunca "me siga"
- [ ] Caption ≤3 linhas com hook autônomo nos primeiros 125 chars
- [ ] Vocabulário LU2CA presente em script e/ou caption
- [ ] Duração estimada ≤30s para completion rate máximo

## Veto Conditions

Rejeitar e refazer se qualquer um for verdadeiro:
1. Caption tem >3 linhas — rejeição imediata, sem exceção
2. Loop design ausente — é obrigatório em todo script de Reel
