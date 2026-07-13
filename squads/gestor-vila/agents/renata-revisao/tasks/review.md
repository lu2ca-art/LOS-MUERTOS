---
task: "Revisão de Qualidade"
order: 1
input: |
  - outputs: todo output gerado no projeto (o que existir): conteudo.md, visuais.md, arte-evento.jpg, roteiro-video.md, orientacao-edicao.md, publicacoes.md, campanha.md, relatorio.md, analise-concorrencia.md, plano-campanha-mensal.md, direcao-semanal.md
  - criteria: pipeline/data/quality-criteria.md — critérios objetivos de avaliação
output: |
  - file: output/{projeto}/review.md — tabela de vereditos com notas e briefings de correção
---

# Revisão de Qualidade

## Descrição

Renata emite veredito formal para **todo output do projeto** — não só conteúdo de marca (copy, visual, vídeo, anúncio), mas também documentos internos (relatório, análise de concorrência, plano estratégico, direção editorial). APROVADO / CONDICIONAL / REJEITADO, com nota 1-10 e raciocínio baseado nos critérios da Vila. Hard caps são verificados primeiro. CONDICIONAL aceita máx 2 correções. Mais de 2 problemas = REJEITADO. A sessão só encerra como APROVADA quando todas as peças estão ≥ 7/10. Renata roda sempre, em qualquer tipo de projeto — não é opcional mesmo quando o projeto não termina em publicação.

## Processo

### 1. Verificar hard caps (antes de qualquer nota)

Do `pipeline/data/quality-criteria.md`:

| Cap | Critério                                                         | Resultado se violado |
|-----|------------------------------------------------------------------|----------------------|
| H1  | Marketing language ("confira", "venha nos visitar", "link na bio", "temos o melhor") | REJEITADO automático |
| H2  | Post de show sem artista + horário + dia                         | REJEITADO automático |
| H3  | CTA digital em evento presencial ("clique aqui", "acesse")      | REJEITADO automático |
| H4  | Publicação sem aprovação do usuário (verificar publicacoes.md, quando existir) | REJEITADO automático |
| H5  | Qualquer valor de cachê, custo de artista ou dado financeiro interno presente em qualquer output (incluindo relatório, análise de concorrência, plano estratégico) | REJEITADO automático |
| H6  | Campanha ou decisão justificada por cachê/valor/histórico automático em vez de pedido explícito do usuário | REJEITADO automático |

Se qualquer hard cap for violado, emitir REJEITADO imediatamente para a peça afetada — sem nota numérica — e incluir briefing de correção.

### 1b. Critérios para documentos internos (relatório, análise de concorrência, plano estratégico, direção editorial)

Quando o projeto produz esse tipo de output, avaliar também:

| Critério | O que avaliar | Peso |
|----------|----------------|------|
| D1 Fonte e data | Toda observação/dado tem origem identificável | Alto |
| D2 Sem estimativa inventada | Nenhuma métrica ou performance apresentada sem base real | Alto |
| D3 Recomendação justificada | Nenhuma recomendação sem motivo concreto | Médio |
| D4 KPI mensurável (planos estratégicos) | Objetivos têm métrica numérica, não vagos | Alto |

### 2. Avaliar critérios soft (peças sem hard cap violado)

Do `pipeline/data/quality-criteria.md`, critérios S1-S8:

| Critério | O que avaliar                               | Peso |
|----------|---------------------------------------------|------|
| S1 Concretude | Nome real + horário real (não "em breve") | Alto |
| S2 Tom de voz | Tom correto para tipo de dia              | Alto |
| S3 Identidade visual | Fundo escuro, paleta Vila, tipografia bold | Alto |
| S4 CTA físico | Chama para ação presencial                | Médio |
| S5 Hierarquia visual | Artista > horário > endereço visualmente | Médio |
| S6 Adaptação de plataforma | Copy diferente por plataforma (quando publicado) | Médio |
| S7 Legibilidade | Contraste ≥ 4.5:1 no visual               | Alto |
| S8 Consistência de marca | Visual reconhecível como "Vila"        | Médio |

### 3. Atribuir nota por peça

| Nota | Significado                                              |
|------|----------------------------------------------------------|
| 9-10 | Excelente — modelo para próximas sessões                 |
| 7-8  | Aprovado — pequenos detalhes opcionais de melhoria       |
| 5-6  | CONDICIONAL — 1-2 correções específicas necessárias      |
| 3-4  | REJEITADO — múltiplos problemas ou problema fundamental  |
| 1-2  | REJEITADO — violação de identidade ou hard cap           |

### 4. Montar tabela de vereditos

Uma linha por peça. Para CONDICIONAL e REJEITADO, incluir briefing de correção no campo "Correção".

### 5. Determinar status da sessão

- **APROVADA:** todas as peças ≥ 7/10
- **CONDICIONAL:** 1+ peças com nota 5-6, todas com correções claras (máx 2 por peça)
- **REJEITADA:** qualquer hard cap violado OU qualquer peça < 5 OU qualquer peça com > 2 problemas

### 6. Emitir próximo passo

- **APROVADA:** indicar que sessão está completa
- **CONDICIONAL:** briefing de correção para cada agente responsável
- **REJEITADA:** briefing de retrabalho para o agente que produziu a peça rejeitada — não um step fixo, já que projetos diferentes envolvem agentes diferentes

## Formato de Saída

```markdown
# Revisão de Qualidade — [DATA]

**Revisora:** Renata Revisão
**Critérios:** pipeline/data/quality-criteria.md

---

## Hard Caps

| Cap | Verificação                        | Status |
|-----|------------------------------------|--------|
| H1  | Marketing language ausente          | ✅ / ❌ |
| H2  | Posts de show com artista + horário | ✅ / ❌ |
| H3  | CTAs físicos                        | ✅ / ❌ |
| H4  | Publicação com aprovação            | ✅ / ❌ |
| H5  | Nenhum dado financeiro interno (cachê) exposto | ✅ / ❌ |
| H6  | Nenhuma decisão por gatilho automático | ✅ / ❌ |

---

## Tabela de Vereditos

| Peça                | Nota | Veredito    | Critério avaliado          | Correção                          |
|---------------------|------|-------------|----------------------------|-----------------------------------|
| POST PRINCIPAL      | X/10 | APROVADO    | [critério]                 | —                                 |
| STORY 1             | X/10 | CONDICIONAL | Critério violado: [S?]     | Correção: [ação específica — para [agente]] |
| STORY 2             | X/10 | REJEITADO   | Critério violado: [H? / S?]| Correção: [ação específica — para [agente]] |
| STORY CHEF ALEX     | X/10 | APROVADO    | [critério]                 | —                                 |
| VISUAL (feed)       | X/10 | [veredito]  | [critério]                 | [correção se necessária]          |
| ARTE EVENTO         | X/10 | [veredito]  | [critério]                 | [correção se necessária]          |

---

## Status da Sessão

**[APROVADA / CONDICIONAL / REJEITADA]**

[1-2 frases com raciocínio]

---

## Próximo Passo

[instrução concreta: quem faz o quê — ou "sessão encerrada como APROVADA"]
```

## Exemplo de Saída

```markdown
# Revisão de Qualidade — quinta, 21 mai

## Hard Caps

| H1 | Marketing language ausente | ✅ |
| H2 | Post de show com RUNA + 21h + quinta | ✅ |
| H3 | CTAs físicos ("vem com a galera") | ✅ |
| H4 | Publicação confirmada via Paulo Postador | ✅ |

## Tabela de Vereditos

| Peça             | Nota | Veredito    | Critério              | Correção                                     |
|------------------|------|-------------|-----------------------|----------------------------------------------|
| POST PRINCIPAL   | 8/10 | APROVADO    | S1, S2, S4 ok        | —                                            |
| STORY 1          | 7/10 | APROVADO    | Enquete presente      | —                                            |
| STORY 2          | 5/10 | CONDICIONAL | Critério violado: S3 — CTA "link na bio" presente | Correção: Cris substituir "link na bio" por "manda mensagem" |
| STORY CHEF ALEX  | 8/10 | APROVADO    | Tom pessoal correto   | —                                            |
| VISUAL (feed)    | 9/10 | APROVADO    | Identidade Vila forte | —                                            |

## Status da Sessão

**CONDICIONAL**

Story 2 usa "link na bio" — hard cap H1 (marketing language). Uma correção simples de Cris Criativa resolve.

## Próximo Passo

Cris Criativa: Story 2 — substituir "link na bio" por "manda mensagem" ou endereço direto. Resubmeter para revisão.
```

## Critérios de Qualidade

- [ ] Hard caps verificados antes de qualquer nota
- [ ] Veredito emitido por peça com nota numérica
- [ ] Raciocínio referencia critério específico (H1-H4 ou S1-S8)
- [ ] Briefing de correção incluído para CONDICIONAL e REJEITADO
- [ ] Correção direcionada ao agente responsável (não genérica)
- [ ] Status da sessão emitido (APROVADA / CONDICIONAL / REJEITADA)
- [ ] Próximo passo concreto ao final

## Condições de Veto

- **Sessão declarada APROVADA com qualquer peça < 7/10** → erro crítico de revisão
- **Veredito sem nota numérica** → incompleto
- **Feedback vago** ("melhorar o texto", "ajustar o visual") → reescrever com ação específica
- **CONDICIONAL com > 2 correções na mesma peça** → converter para REJEITADO
- **REJEITADO sem briefing de correção** → sempre incluir direção para retrabalho
