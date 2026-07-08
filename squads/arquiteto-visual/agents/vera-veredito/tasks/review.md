---
task: "Revisar Sessão"
order: 1
input: |
  - conteudo_instagram: Caption e script de Carlos Caption (output/conteudo-instagram.md)
  - visual_rendered: Visual de Diana Design (output/visual-01.jpg)
  - adaptacoes: Adaptações de Rafael Repercussão (output/adaptacoes.md)
output: |
  - review: Tabela de vereditos por peça com nota, raciocínio e briefing de correção quando necessário
  - sessao_status: APROVADA / CONDICIONAL / REJEITADA — com próximo passo concreto
---

# Revisar Sessão

Vera Veredito revisa todo o conteúdo produzido na sessão e emite veredito formal APROVADO / CONDICIONAL / REJEITADO por peça, com nota 1-10 e raciocínio derivado dos critérios reais investigados. A sessão só fecha como APROVADA quando todas as peças têm nota ≥7/10.

## Process

1. **Carregar critérios:** Ler `pipeline/data/quality-criteria.md` completamente. Os critérios de Vera são derivados da investigação real de 6 perfis — não de best practices genéricos.

2. **Verificar hard caps primeiro** (qualquer violação = REJEITADO imediato, sem nota):
   - **H1**: Caption com >3 linhas → REJEITADO imediato
   - **H2**: Marketing language presente ("confira", "não perca", "link na bio", "disponível em todas as plataformas") → REJEITADO imediato
   - **H3**: Visual com background claro ou gradiente pastel → REJEITADO imediato
   - **H4**: Newsletter sem "com amor, LU2CA" → REJEITADO imediato

3. **Atribuir nota por peça** (para peças que passaram nos hard caps):
   - 9-10: Benchmark de referência — supera os exemplos reais de alto engajamento
   - 7-8: APROVADO — cumpre todos os critérios, pronto para publicar
   - 5-6: CONDICIONAL — ≤2 correções específicas necessárias
   - 1-4: REJEITADO — problema estrutural, requer refazer com briefing

4. **Emitir veredito por peça:** Tabela com: peça | nota | veredito | raciocínio (1-2 frases máximo).

5. **Briefing de correção para CONDICIONAIs e REJEITADOs:** Máx 2 correções por peça CONDICIONAL. Para REJEITADOs, briefing direcionado ao agente criador com: critério violado + o que está errado + o que deve ser diferente.

6. **Verificar ecossistema gamificado:** Independentemente das notas individuais — se nenhuma peça da sessão menciona lu2ca.art ou desbloqueio, sinalizar gap como alerta separado.

7. **Emitir status da sessão:** APROVADA (todas ≥7) / CONDICIONAL (alguma entre 5-6, sem hard cap violado) / REJEITADA (algum hard cap ou nota ≤4). Incluir próximo passo concreto.

## Output Format

```
=== REVISÃO DA SESSÃO ===

| Peça | Nota | Veredito | Raciocínio |
|------|------|----------|------------|
| [nome] | [X]/10 | APROVADO/CONDICIONAL/REJEITADO | [1-2 frases] |

=== BRIEFING DE CORREÇÃO ===
[apenas para CONDICIONAL e REJEITADO]

[Peça] → [Agente responsável]
Critério violado: [H1-H4 ou S1-S10]
Problema: [o que está errado]
Correção: [o que deve ser diferente]

=== STATUS DA SESSÃO ===
[APROVADA / CONDICIONAL / REJEITADA]

[Alerta ecossistema gamificado — se nenhuma peça menciona lu2ca.art]

Próximo passo: [ação concreta]
```

## Output Example

```
=== REVISÃO DA SESSÃO ===

| Peça | Nota | Veredito | Raciocínio |
|------|------|----------|------------|
| Caption Feed | 8/10 | APROVADO | Hook autônomo em 71 chars, vocabulário LU2CA presente, sem marketing language. Referência ao ecossistema implícita via "próxima faixa". |
| Script Reel | 7/10 | APROVADO | Loop design presente, CTA não é "me siga". Delivery dentro de 20s — completion rate favorável. |
| Visual 01 | 9/10 | APROVADO | Fundo #0a0a0a confirmado, grain presente (opacity 0.07), lu2ca.art visível, hierarquia de 3 elementos respeitada. Benchmark: supera o padrão do lançamento de 91 curtidas. |
| Newsletter | 6/10 | CONDICIONAL | Assinatura "com amor, LU2CA" presente. Corpo de 380 palavras — dentro do range. Abertura fraca: primeira frase não abre — reformular como confissão direta. |

=== BRIEFING DE CORREÇÃO ===

Newsletter → Rafael Repercussão
Critério violado: S3 (abertura deve reter em 2 frases)
Problema: "nessa semana queremos falar sobre movimento" — é anúncio, não confissão
Correção: começar com confissão direta no tom Vulnerável — ex: "essa semana a gravidade estava maior que o normal."

=== STATUS DA SESSÃO ===
CONDICIONAL

Próximo passo: Rafael Repercussão reformula abertura da Newsletter conforme briefing acima. Após correção, Vera re-revisa apenas a Newsletter.
```

## Quality Criteria

- [ ] Todos os hard caps verificados (H1-H4) antes de qualquer nota
- [ ] Veredito formal emitido por peça com nota numérica
- [ ] Raciocínio derivado de critério específico — nunca "parece bom" ou "eu gosto"
- [ ] CONDICIONAL tem ≤2 correções específicas e acionáveis
- [ ] REJEITADO inclui briefing de correção com agente responsável e ação concreta
- [ ] Ecossistema gamificado verificado — alerta emitido se lu2ca.art ausente de toda a sessão
- [ ] Status da sessão emitido com próximo passo concreto

## Veto Conditions

Rejeitar e refazer se qualquer um for verdadeiro:
1. Sessão marcada como APROVADA com qualquer peça abaixo de 7/10 — o padrão mínimo é inegociável
2. Feedback vago emitido ("melhorar a copy", "pode ficar melhor") — toda correção precisa de critério, problema e solução específicos
