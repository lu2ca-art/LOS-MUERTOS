---
task: "Pensar e Conceituar"
order: 1
input: |
  - contexto_sessao: Briefing preenchido pelo usuário — era atual, mood, próximos lançamentos, últimos posts, formatos desejados
output: |
  - pauta_estrategica: 1 frase descrevendo o que criar e por quê agora
  - recomendacao: qual dos 5 ângulos é mais estratégico e por quê (1 frase)
  - angulos: lista de 5 ângulos criativos com lens + linha de abertura de exemplo cada
---

# Pensar e Conceituar

Bruno Brainstorm analisa o contexto estratégico da sessão e gera a pauta do dia mais 5 ângulos criativos distintos, cada um enraizado numa dimensão diferente do universo de LU2CA.

## Process

1. **Carregar universo:** Ler `pipeline/data/lu2ca-universe.md` completamente. Internalizar vocabulário (corpitcho, viajante, tripulação, mundo seco, CIDADE NEON, desbloquear), era atual, gaps identificados e os posts de maior engajamento real. Ler também `pipeline/data/tone-of-voice.md` para mapear os 6 tons.

2. **Analisar contexto:** Processar o briefing do usuário em `squads/arquiteto-visual/output/contexto.md`. Responder internamente: Qual momento da era CIDADE NEON? Há lançamento próximo? Qual gap é mais urgente (countdown, gamificação, serialização, vulnerabilidade)? Qual formato foi solicitado?

3. **Formular pauta:** Escrever 1 frase estratégica que justifica o conteúdo desta sessão. Exemplo: "Estamos a 7 dias do lançamento de 'CHUVA' — a tripulação precisa de aquecimento emocional antes do countdown explícito começar." Esta frase precede os ângulos.

4. **Gerar 5 ângulos:** Produzir um ângulo para cada uma das 5 dimensões do universo de LU2CA. Para cada ângulo: (a) nome em caps, (b) lens emocional em 1 frase, (c) linha de abertura de exemplo que captura o tom instantaneamente e usa vocabulário de LU2CA.

5. **Sinalizar recomendação:** Identificar o ângulo mais alinhado com a pauta estratégica. Marcá-lo com ★ e justificar a escolha em 1 frase. Deixar claro que o usuário decide.

## Output Format

```
🧠 PAUTA DA SESSÃO
[1 frase estratégica: o que criar e por quê agora]

★ RECOMENDAÇÃO: [nome do ângulo] — [justificativa em 1 frase]

5 ÂNGULOS

1 · FILOSÓFICO/POÉTICO
Lens: [perspectiva reflexiva em 1 frase]
Abertura: "[linha de exemplo usando vocabulário de LU2CA]"

2 · FÍSICO/MOVIMENTO
Lens: [perspectiva energética/corporal em 1 frase]
Abertura: "[linha de exemplo com corpitcho ou gesto]"

3 · COMUNITÁRIO/GAMIFICADO
Lens: [perspectiva de comunidade/lu2ca.art em 1 frase]
Abertura: "[linha de exemplo com viajante, tripulação ou desbloqueio]"

4 · CULTURAL/REFERÊNCIA
Lens: [perspectiva cultural brasileira + global em 1 frase]
Abertura: "[linha de exemplo minimalista com referência]"

5 · VULNERÁVEL/HUMANO
Lens: [perspectiva de confissão/contraste em 1 frase]
Abertura: "[linha de exemplo íntima e honesta]"
```

## Output Example

> Use como referência de qualidade, não como template rígido.

```
🧠 PAUTA DA SESSÃO
Estamos a 5 dias do lançamento de 'CHUVA'. A tripulação precisa sentir que a
chuva está chegando antes de ela chegar — não countdown explícito ainda, mas
a atmosfera. Criar aquecimento emocional que direciona para lu2ca.art.

★ RECOMENDAÇÃO: COMUNITÁRIO/GAMIFICADO — cria antecipação coletiva antes
do lançamento, padrão de fuckyoubenni com "one week till STAYED UP is yours".

5 ÂNGULOS

1 · FILOSÓFICO/POÉTICO
Lens: o mundo seco que antecede a chegada da chuva — escassez antes da abundância
Abertura: "quem vem te molhar nesse mundo seco? ☔️"

2 · FÍSICO/MOVIMENTO
Lens: o corpitcho que resiste à gravidade da segunda-feira antes da tempestade
Abertura: "mexe o corpitcho bebe, segunda não vence 🛹"

3 · COMUNITÁRIO/GAMIFICADO
Lens: a tripulação avança no mapa, a chuva vem pra todos
Abertura: "a tripulação avisa: algo molhado vem aí, viajante 🧳"

4 · CULTURAL/REFERÊNCIA
Lens: chuva como linguagem global — SP, Costa Rica, o mundo
Abertura: "🇧🇷☔️🌍 @dyanlohan"

5 · VULNERÁVEL/HUMANO
Lens: confissão sobre os dias secos que precedem algo que molha tudo
Abertura: "às vezes é preciso se molhar pra entender que você estava seco."
```

## Quality Criteria

- [ ] Pauta estratégica em 1 frase — não uma lista, não um parágrafo
- [ ] Recomendação com ★ e justificativa em 1 frase
- [ ] Exatamente 5 ângulos, cobrindo as 5 dimensões
- [ ] Linha de abertura de exemplo para todos os 5 ângulos
- [ ] Vocabulário LU2CA presente em todos os 5 (corpitcho, viajante, tripulação, mundo seco, CIDADE NEON, ou outros termos proprietários)
- [ ] Ângulo Comunitário/Gamificado referencia lu2ca.art ou desbloqueio

## Veto Conditions

Rejeitar e refazer se qualquer um for verdadeiro:
1. Algum ângulo poderia ser de qualquer outro artista — sem vocabulário proprietário de LU2CA ou sem enraizamento na era CIDADE NEON
2. Faltam o ângulo Vulnerável/Humano ou o Comunitário/Gamificado — as 5 dimensões são obrigatórias
