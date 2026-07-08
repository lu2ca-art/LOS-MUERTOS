# Quality Criteria — Arquiteto Visual

> Critérios de qualidade derivados da investigação de 6 perfis e benchmarks de domínio.
> Referência para Vera Veredito e todos os agentes criadores.

---

## Sistema de Pontuação

| Nota | Classificação | Ação |
|------|-------------|------|
| 9-10 | Excelente | APROVADO — publicação imediata |
| 7-8 | Bom | APROVADO — pode ter ajuste cosmético menor |
| 5-6 | Satisfatório | CONDICIONAL — ≤2 correções específicas obrigatórias |
| 3-4 | Abaixo do padrão | REJEITADO — recriar com briefing de correção |
| 1-2 | Inadequado | REJEITADO — violação de critérios hard |

---

## Critérios HARD (Rejeição Imediata)

Violação de qualquer critério abaixo = REJEITADO sem negociação.

### H1: Caption ≤3 linhas
**Como verificar:** contar as quebras de linha no output
**Por quê é hard:** padrão universal dos 6 perfis investigados — posts longos têm desempenho consistentemente inferior

### H2: Zero marketing language
**Palavras e frases proibidas:**
- "confira", "não perca", "saiu", "disponível em todas as plataformas"
- "link na bio" (quando é o único CTA e não referencia URL específica)
- "ouça agora no Spotify" ou equivalente como frase central
- "clique aqui", "acesse já"

**Por quê é hard:** mata autenticidade — a audiência alternativa 18-30 é alérgica a marketing language

### H3: Background visual escuro
**Critério:** fundo ≤ #333333 em qualquer canal RGB
**Por quê é hard:** quebra o design system CIDADE NEON sem exceção

### H4: Sem publicação sem aprovação
**Como verificar:** Rafael só publica após checkpoint aprovado
**Por quê é hard:** publicação é irreversível

---

## Critérios SOFT (Scoring)

Cada critério vale até 1 ponto na nota final (máx 10).

### Conteúdo Textual

**S1: Hook independente nos primeiros 125 chars (peso 2)**
- 2 pts: hook funciona como frase autônoma, prende atenção
- 1 pt: hook funciona mas é fraco
- 0 pts: hook não funciona sozinho

**S2: Vocabulário LU2CA presente (peso 2)**
- 2 pts: ≥2 termos assinatura (corpitcho, viajante, tripulação, mundo seco, voadão, etc.)
- 1 pt: 1 termo assinatura
- 0 pts: zero termos de vocabulário próprio

**S3: Consistência de tom (peso 1)**
- 1 pt: tom escolhido é mantido do início ao fim
- 0 pts: mistura de tons não intencional

**S4: Referência ao ecossistema gamificado (peso 1)**
- 1 pt: lu2ca.art ou mecânica de desbloqueio mencionados
- 0 pts: ausência total na sessão (não por peça — por sessão)

**S5: Engagement driver (peso 1)**
- 1 pt: pergunta, jogo, desafio ou convite presente (em ≤30% dos posts)
- 0 pts: ausência ou saturação (em todos os posts)

### Reel Específico

**S6: Script completo com loop design (peso 1)**
- 1 pt: hook 0-2s + delivery + loop design + CTA específico
- 0 pts: faltam seções ou CTA genérico

**S7: Duração ≤30s para Reel padrão (peso 1)**
- 1 pt: duração indicada ≤30s
- 0 pts: duração sem indicação ou >60s

### Story Específico

**S8: Elemento interativo presente (peso 1)**
- 1 pt: poll / quiz / caixa de perguntas / slider com prompt específico
- 0 pts: story sem elemento interativo ou prompt genérico ("o que você acha?")

### Visual Específico

**S9: Contraste texto/fundo ≥4.5:1 (peso 2)**
- 2 pts: contraste verificável ≥4.5:1 em todo texto
- 1 pt: contraste estimado adequado
- 0 pts: contraste claramente insuficiente

**S10: Grain + assinatura presentes (peso 1)**
- 1 pt: grain texture + "CIDADE NEON · lu2ca.art" ou "⚡️ lu2ca.art"
- 0 pts: ausência de qualquer um dos dois

---

## Critérios por Tipo de Peça

### Caption de Feed
- [ ] ≤3 linhas (H1)
- [ ] Zero marketing language (H2)
- [ ] Hook funcional nos primeiros 125 chars (S1)
- [ ] Vocabulário LU2CA ≥1 termo (S2)
- [ ] Tudo minúsculo exceto projeto em CAPS
- [ ] Zero hashtags (ou ≤5 se solicitado explicitamente)

### Reel Script
- [ ] Hook 0-2s com text overlay definido (S6)
- [ ] Delivery com indicação de cortes a cada 3-5s
- [ ] Loop design especificado (final → início)
- [ ] CTA específico (pergunta ou ação — não "me siga")
- [ ] Caption associada ≤3 linhas (H1)
- [ ] Duração indicada ≤30s (S7)

### Story Sequence
- [ ] 4-7 frames (não menos, não mais)
- [ ] Frame opener com gancho em ≤2 linhas
- [ ] ≥1 frame interativo (S8)
- [ ] Prompt do elemento interativo é específico e binário
- [ ] Frame final com conclusão ou link sticker para lu2ca.art

### Visual HTML (1080×1440px)
- [ ] Dimensões exatas: width: 1080px; height: 1440px (H3-dimensional)
- [ ] Background escuro ≤#333333 (H3)
- [ ] Contraste texto/fundo ≥4.5:1 (S9)
- [ ] Grain texture aplicada (S10)
- [ ] Assinatura presente: "CIDADE NEON · lu2ca.art" (S10)
- [ ] Máx 2 cores de acento
- [ ] HTML self-contained (sem dependências externas quebráveis)

### Adaptação Multiplataforma
- [ ] Adaptação nativa (não cópia) por plataforma
- [ ] Limites respeitados (280 chars Twitter, etc.)
- [ ] lu2ca.art mencionado em todas as adaptações
- [ ] Newsletter com assinatura "com amor, LU2CA"
- [ ] Nenhuma publicação sem aprovação (H4)

---

## Benchmarks Reais (Derivados da Investigação)

| Tipo de post | Curtidas médias | Comentários médios | Padrão mais eficaz |
|---|---|---|---|
| Lançamento com projeto + URL | 91 | 32 | Nome projeto + URL + 1 emoji |
| Comunitário/Gamificado | 107 | 14 | Tripulação + viajante + desafio |
| Filosófico longo | 33 | 6 | Declaração geracional densa |
| Motivacional curto | 24 | 5 | Corpitcho + permissão |
| Cultural/minimalista | 24 | 2 | Emoji + @mention |

**Conclusão:** Posts comunitários e de lançamento superam posts filosóficos em alcance. Mas os filosóficos criam profundidade de identificação — equilíbrio é chave.
