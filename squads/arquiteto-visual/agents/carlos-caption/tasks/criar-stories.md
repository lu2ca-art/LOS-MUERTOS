---
task: "Criar Stories"
order: 3
input: |
  - angulo_selecionado: O ângulo escolhido com lens e linha de abertura
  - tom_confirmado: Tom de voz (Lírico, Filosófico, Motivacional, Comunitário, Cultural, Vulnerável)
  - conteudo_feed: Caption do feed ou script do Reel da mesma sessão (para coesão)
output: |
  - stories_sequence: Sequência de 4-7 frames com copy, elemento interativo e indicação visual
  - notas_stories: Observações sobre ordem, timing e CTA final
---

# Criar Stories

Carlos Caption cria uma sequência de Stories do Instagram — 4 a 7 frames — que amplifica o conteúdo do feed ou Reel da sessão. Cada frame tem copy curta, indicação visual e pelo menos um elemento interativo (enquete, pergunta, slider). Nenhum frame é auto-suficiente — a sequência conta uma história.

## Process

1. **Carregar contexto:** Ler `pipeline/data/lu2ca-universe.md` para vocabulário ativo. Revisar o conteúdo do feed/Reel da sessão — os Stories são amplificação, não repetição.

2. **Definir arco narrativo:** Decidir o fluxo dos frames antes de escrever qualquer copy. Stories têm abertura (prender), desenvolvimento (construir) e fechamento (CTA ou desbloqueio). 4 frames = mínimo viável; 7 frames = máximo — além disso perde completion rate.

3. **Escrever copy por frame:** Máx 3 linhas por frame. Tudo minúsculo exceto projeto em CAPS. Primeira linha de cada frame é o gancho do próximo — o viewer deve querer apertar para avançar.

4. **Posicionar elemento interativo:** Obrigatório em pelo menos 1 frame (máx 2). Escolher:
   - **Enquete** (duas opções): para decisões binárias do universo de LU2CA — "você desbloqueia ou não?"
   - **Pergunta aberta**: para coletar respostas da tripulação
   - **Slider emoji**: para intensidade emocional — "o quanto você sente isso?"
   - **Quiz**: quando há referência cultural ou vocabulário de LU2CA para testar

5. **Escrever frame de fechamento:** Último frame é sempre CTA ou referência a lu2ca.art / desbloqueio. Nunca terminar sem direção — a tripulação precisa de próximo passo.

6. **Verificar arco e checklist:** A sequência tem abertura-desenvolvimento-fechamento? Cada frame avança a narrativa? Elemento interativo em 1-2 frames? Copy ≤3 linhas por frame?

## Output Format

```
=== SEQUÊNCIA DE STORIES ===

FRAME 1 (abertura)
Copy: "[texto — máx 3 linhas, minúsculo]"
Visual: [fundo, cor dominante ou referência à era CIDADE NEON]
Interativo: [nenhum / tipo do elemento]

FRAME [N] (desenvolvimento)
Copy: "[texto]"
Visual: [indicação]
Interativo: [tipo: enquete "opção A" vs "opção B" / pergunta "[texto da pergunta]" / slider [emoji]]

FRAME [ÚLTIMO] (fechamento)
Copy: "[texto com CTA ou lu2ca.art]"
Visual: [indicação]
Interativo: [nenhum ou tipo]

=== NOTAS ===
Frames: [número total]
Interativo: [frame N — tipo]
CTA final: [descrição]
```

## Output Example

```
=== SEQUÊNCIA DE STORIES ===

FRAME 1 (abertura)
Copy: "segunda não vence o corpitcho"
Visual: fundo escuro #0a0a0a, texto neon amarelo, grain textura
Interativo: nenhum

FRAME 2 (desenvolvimento)
Copy: "às vezes a única coisa entre você e a paralisação é um movimento pequeno"
Visual: fundo escuro, texto em branco, sem imagem
Interativo: enquete — "você mexeu hoje?" vs "ainda não"

FRAME 3 (desenvolvimento)
Copy: "mexe o corpitcho bebe 🛹"
Visual: referência ao visual do feed — paleta neon
Interativo: slider 🛹

FRAME 4 (fechamento)
Copy: "a próxima faixa da semana tá esperando em lu2ca.art"
Visual: tipografia com URL lu2ca.art em destaque
Interativo: nenhum

=== NOTAS ===
Frames: 4
Interativo: frame 2 (enquete), frame 3 (slider)
CTA final: desbloqueio em lu2ca.art
```

## Quality Criteria

- [ ] Sequência tem 4-7 frames (não menos, não mais)
- [ ] Pelo menos 1 elemento interativo (máx 2)
- [ ] Copy ≤3 linhas por frame
- [ ] Último frame tem CTA ou referência a lu2ca.art
- [ ] Tudo minúsculo exceto projeto em CAPS
- [ ] Zero marketing language em todos os frames
- [ ] Arco narrativo verificado: abertura → desenvolvimento → fechamento

## Veto Conditions

Rejeitar e refazer se qualquer um for verdadeiro:
1. Nenhum elemento interativo na sequência — inegociável, é o diferencial de Stories
2. Último frame sem CTA ou referência ao ecossistema — Stories sem direção não convertem
