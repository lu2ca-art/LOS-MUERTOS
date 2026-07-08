---
task: "Criar Feed"
order: 2
input: |
  - angulo_selecionado: O ângulo escolhido com lens e linha de abertura
  - tom_confirmado: Tom de voz (Lírico, Filosófico, Motivacional, Comunitário, Cultural, Vulnerável)
output: |
  - caption_feed: Caption pronta para post de feed (≤3 linhas, hook ≤125 chars)
  - notas_publicacao: Observações sobre timing, CTA ou instruções de publicação
---

# Criar Feed

Carlos Caption escreve a caption de um post de feed do Instagram — estático ou carrossel — com hook autônomo nos primeiros 125 chars, tudo minúsculo exceto o projeto, zero hashtags, zero marketing language.

## Process

1. **Carregar voz:** Ler `pipeline/data/tone-of-voice.md` e identificar as características do tom confirmado. Revisar os exemplos reais de alto engajamento em `pipeline/data/output-examples.md` para calibrar o nível de concisão esperado.

2. **Selecionar estrutura por tom:**
   - Lírico/Poético: pergunta poética de 5-10 palavras + emoji
   - Filosófico/Geracional: declaração de 1-2 linhas que acumula impacto
   - Motivacional/Movimento: observação pessoal + comando carinhoso com corpitcho
   - Comunitário/Gamificado: tripulação → viajante + referência a lu2ca.art ou desbloqueio
   - Cultural/Minimalista: emoji de identidade + referência mínima
   - Vulnerável/Confessional: confissão direta em 1-2 linhas, sem emoji ou 1 máximo

3. **Escrever linha 1 (hook):** Esta é a linha mais importante. Deve funcionar como frase autônoma em ≤125 chars. Testar mentalmente: se fosse a única linha, prenderia? Usar a linha de abertura do ângulo como ponto de partida.

4. **Escrever linhas 2-3 (se necessário):** Apenas se o tom pede desenvolvimento. Muitos posts poderosos têm apenas 1 linha. Nunca forçar conteúdo para ocupar espaço.

5. **Adicionar CTA (apenas em <30% dos posts):** Quando apropriado, adicionar pergunta direta no final. Mas não em todo post — o excesso de CTAs satura e soa como marketing.

6. **Verificar checklist:** Caption ≤3 linhas? Zero hashtags? Zero marketing language? Tudo minúsculo exceto projeto? Hook autônomo nos 125 chars?

## Output Format

```
=== CAPTION DE FEED ===
[linha 1 — hook autônomo, ≤125 chars]

[linha 2 opcional — desenvolvimento ou vocabulário LU2CA]

[linha 3 opcional — CTA ou fechamento — apenas em <30% dos posts]

=== NOTAS ===
Tom: [nome do tom aplicado]
CTA: [sim/não — se sim, tipo]
Sugestão de horário: [dia e período se relevante para a sessão]
```

## Output Example

> Use como referência de qualidade, não como template rígido.

```
=== CAPTION DE FEED — Lançamento ===
'CIDADE NEON' disponível em lu2ca.art 🎆

=== NOTAS ===
Tom: Cultural/Minimalista
CTA: não — a URL é o CTA implícito
Sugestão de horário: qualquer dia, 18h-21h

---

=== CAPTION DE FEED — Comunitário ===
a tripulação deseja à você uma boa semana, viajante 🧳

e te desafia a desbloquear a próxima faixa e vir contar na dm

'CIDADE NEON' em lu2ca.art

=== NOTAS ===
Tom: Comunitário/Gamificado
CTA: sim — "vir contar na dm" (implícito)
Engajamento de referência: 107 curtidas — maior da análise
```

## Quality Criteria

- [ ] Caption ≤3 linhas (verificado antes de entregar)
- [ ] Linha 1 funciona como hook autônomo em ≤125 chars
- [ ] Tudo minúsculo exceto nome do projeto em CAPS
- [ ] Zero hashtags (ou ≤5 se solicitado explicitamente)
- [ ] Zero marketing language ("confira", "não perca", "link na bio", "disponível em todas as plataformas")
- [ ] Vocabulário LU2CA presente se o tom pede
- [ ] CTA apenas quando adequado ao tom (não em todo post)

## Veto Conditions

Rejeitar e refazer se qualquer um for verdadeiro:
1. Caption tem >3 linhas — rejeição imediata sem exceção
2. Qualquer instância de marketing language — rejeição imediata
