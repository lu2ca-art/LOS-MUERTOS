---
task: "Caçar Referências"
order: 1
input: |
  - identidade: pipeline/data/vila-identity.md
  - tom: pipeline/data/tone-of-voice.md
  - anti-padroes: pipeline/data/anti-patterns.md
  - foco (opcional): tema/pilar específico pedido pelo usuário (ex: "shows", "domingo em família", "Copa do Mundo")
output: |
  - file: output/referencias/YYYY-MM-DD-referencias.md — até 8 referências ranqueadas com mecanismo + adaptação
---

# Caçar Referências

## Descrição

Hugo pesquisa restaurantes, bares, casas de show e perfis gastronômicos em raios crescentes (Barueri/Grande SP → estado de SP → Brasil → mundo) usando `web_search` e `web_fetch`, buscando formatos e mecanismos de conteúdo replicáveis para a Vila. Cada referência é analisada, não copiada — o valor está no "por que funcionou" e no "como adaptar".

## Processo

### 1. Definir escopo da busca

Se o usuário deu um foco (ex: "referências pra sexta-feira" ou "ideias pra Copa"), pesquisar em torno desse tema. Sem foco definido, cobrir de forma equilibrada os pilares de conteúdo da semana (ver `pipeline/data/vila-identity.md`).

### 2. Buscar por raio, em ordem

1. **Local (Barueri/Grande SP):** concorrência direta — outros bares/restaurantes/casas de show da região.
2. **Estadual (SP):** portais gastronômicos, contas de grande alcance no estado.
3. **Nacional (Brasil):** campanhas sazonais, ativações de datas comemorativas, redes com identidade forte.
4. **Global:** restaurantes temáticos, bares Tex-Mex/Día de los Muertos fora do Brasil, blogs de F&B marketing.

Usar `web_search` para descobrir perfis/posts/matérias relevantes; usar `web_fetch` para ler o conteúdo completo antes de extrair o mecanismo.

### 3. Filtrar e ranquear

Descartar qualquer achado que:
- Não tenha fonte rastreável (link/perfil)
- Dependa de um mecanismo impossível de adaptar com os recursos da Vila
- Sugira linguagem ou formato vetado por `anti-patterns.md`

Ranquear os sobreviventes por **prioridade** = facilidade de adaptação × potencial de impacto. Selecionar no máximo 8.

### 4. Documentar mecanismo + adaptação

Para cada referência selecionada, escrever:
- O que é (formato, plataforma, contexto)
- Por que funcionou (o mecanismo — gancho, timing, estrutura, CTA)
- Como adaptar para a Vila, citando recurso concreto da casa (Chef Alex, música ao vivo qui-sáb, mascotes, identidade Día de los Muertos)

## Formato de Saída

```markdown
# Referências — [data]

**Foco da busca:** [tema ou "cobertura geral dos pilares semanais"]

---

## 1. [Nome/perfil da referência] — Prioridade: Alta
**Raio:** Local / Estadual / Nacional / Global
**Fonte:** [link]
**O que é:** [formato + plataforma + contexto]
**Mecanismo:** [por que funcionou]
**Adaptação pra Vila:** [tradução concreta usando recursos reais da casa]

## 2. [...]

---

## Resumo por raio
| Raio | Qtd. referências |
|------|-------------------|
| Local | X |
| Estadual | X |
| Nacional | X |
| Global | X |
```

## Exemplo de Saída

```markdown
## 1. @churrascaria.xyz (Alphaville) — Prioridade: Alta
**Raio:** Local
**Fonte:** instagram.com/churrascaria.xyz
**O que é:** Story diário "bastidor às 17h" mostrando o chef preparando o prato do dia, 15s, sem CTA comercial.
**Mecanismo:** Humaniza a cozinha e cria expectativa recorrente — o público volta todo dia pra ver o próximo prato.
**Adaptação pra Vila:** já existe o slot STORY CHEF ALEX recorrente — testar horário fixo (17h) e formato "prato do dia" pra criar hábito de consumo, sem mudar o tom pessoal já estabelecido.

## 2. Cantina temática CDMX (México) — Prioridade: Média
**Raio:** Global
**Fonte:** [blog F&B internacional]
**O que é:** Ativação de Día de los Muertos com decoração + menu especial + trilha ao vivo por 3 dias.
**Mecanismo:** Concentra a identidade cultural da marca em uma janela curta e de alta intensidade, gerando FOMO.
**Adaptação pra Vila:** planejar uma "semana Día de los Muertos" com Chef Alex + música ao vivo reforçada — já alinhado à identidade Tex Mex BR e ao pilar Cultural/Identitário.
```

## Critérios de Qualidade

- [ ] Máximo 8 referências, todas ranqueadas por prioridade
- [ ] Cobertura de pelo menos 2 raios geográficos diferentes por rodada (a menos que o foco seja hiperlocal)
- [ ] Toda referência tem fonte rastreável
- [ ] Todo mecanismo é explicado antes da adaptação
- [ ] Toda adaptação cita recurso concreto e real da Vila
- [ ] Nenhuma sugestão viola os hard caps de `anti-patterns.md`

## Condições de Veto

- **Referência sem fonte** → descartar, não incluir no output
- **Adaptação genérica** ("postar mais stories") sem ligação com recurso real da Vila → reescrever ou descartar
- **Mecanismo que exige orçamento ou infraestrutura que a Vila não tem** (ex: drone, equipe de produção grande) → descartar ou marcar como "Prioridade: Baixa — requer investimento"
