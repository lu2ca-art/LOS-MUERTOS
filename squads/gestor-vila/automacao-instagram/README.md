# Vila Instagram Bot — resposta automática de DM

Webhook que recebe mensagens diretas do Instagram da Vila Los Muertos de Fome,
tenta casar o texto com uma categoria da `biblioteca-respostas-atual.md` e
responde sozinho. Quando não tem certeza (ou o assunto é sensível), manda a
resposta de fallback ("Fora do Escopo") e loga pra um humano acompanhar.

Roda em **Cloudflare Workers** — escolhido em vez de auto-hospedar ou usar
Vercel porque, pro volume de mensagens de um restaurante, é gratuito e mais
seguro que manter um servidor próprio no ar (sem porta aberta em roteador,
sem máquina precisando ficar ligada 24h, TLS e infraestrutura gerenciados
pela Cloudflare).

## O que já está pronto e testado localmente

- `scripts/parse-biblioteca.js` — converte a biblioteca `.md` em
  `data/biblioteca.json`. Rodar de novo sempre que a biblioteca mudar:
  ```
  node scripts/parse-biblioteca.js
  ```
- `src/match.js` — matching por palavra-chave (sem IA/LLM, de propósito:
  rápido e fácil de explicar por que respondeu X e não Y).
- `src/worker.js` — o Worker em si (verificação do Meta + recebimento +
  resposta + log de "precisa de humano"). Testado localmente com
  `wrangler dev`: verificação do Meta, resposta de reserva, e reclamação
  caindo certinho no log `NEEDS_HUMAN` — todos passaram.
- `wrangler.toml` — configuração do Worker.

**Isso ainda não fala com o Instagram de verdade.** Faltam duas coisas, e as
duas dependem de login que só você pode fazer (não é algo que eu deva fazer
no seu lugar):

## Passo 1 — Autenticar a Cloudflare (só você)

No terminal, dentro da pasta `automacao-instagram/`:
```
npx wrangler login
```
Isso abre o navegador pra você logar (ou criar conta gratuita) na
Cloudflare. Depois disso, me avisa que eu sigo com o deploy
(`npx wrangler deploy`) — essa parte eu já testei localmente e está pronta
pra ir.

## Passo 2 — Configurar os segredos (também só você, depois do deploy)

Os valores sensíveis **nunca** devem passar por mim ou aparecer numa
mensagem de chat. Depois do primeiro `wrangler deploy`, rode estes comandos
você mesmo (cada um abre um prompt seguro pra colar o valor):
```
npx wrangler secret put VERIFY_TOKEN
npx wrangler secret put PAGE_ACCESS_TOKEN
npx wrangler secret put APP_SECRET
```

| Segredo | O que é | Onde pegar |
|---|---|---|
| `VERIFY_TOKEN` | Senha inventada por você, só pra bater com o Meta na hora de registrar o webhook | Você mesmo inventa (qualquer string) |
| `PAGE_ACCESS_TOKEN` | Token que autoriza o bot a mandar mensagem em nome da Página/Instagram | Painel do app Meta — ver Passo 4 abaixo |
| `APP_SECRET` | Opcional, mas recomendado — valida que a requisição realmente veio do Meta | Painel do app Meta → Configurações Básicas |

## Passo a passo do lado Meta/Instagram (só você consegue fazer isso)

Isso exige login na sua conta — não posso fazer OAuth por você.

### 3. Pré-requisito
A conta do Instagram (@vilalosmuertosdefome) precisa ser **conta
profissional (Business ou Creator)** e estar conectada a uma **Página do
Facebook**. Se já usa Instagram Direct/anúncios pela empresa, provavelmente
já está assim — confirma em Configurações → Contas conectadas, no app do
Instagram.

### 4. Criar o App no Meta Developers
1. Acesse developers.facebook.com → **Meus Apps** → **Criar App**.
2. Tipo de app: **Negócios** (Business).
3. Adicione o produto **Instagram** → **API do Instagram com Messenger**
   (ou "Instagram Graph API", conforme o nome no seu painel).

### 5. Adicionar sua própria conta como testadora (evita revisão do Meta)
Como é a sua própria conta respondendo por si mesma (não um serviço pra
terceiros), você **não precisa esperar App Review** — só precisa:
1. Painel do app → **Funções** (Roles) → **Testadores do Instagram** →
   adicionar `@vilalosmuertosdefome`.
2. Aceitar o convite (chega uma notificação no app do Instagram, em
   Configurações → Apps e sites).

### 6. Gerar o Page Access Token
No painel do app → **Instagram API com Messenger** → **Configuração da
API** → gere um **token de acesso de página** pra Página conectada ao
Instagram da Vila. Cola esse valor no `wrangler secret put
PAGE_ACCESS_TOKEN` do Passo 2 — nunca numa mensagem pra mim.
Tokens padrão expiram em ~60 dias — perto disso, gera de novo do mesmo
jeito.

### 7. Configurar o Webhook
1. Painel do app → **Webhooks** → **Instagram** → **Configurar**.
2. **URL de callback:** a URL que a Cloudflare vai te dar depois do
   deploy (algo como `https://vila-instagram-bot.<seu-usuario>.workers.dev`).
3. **Verify Token:** o mesmo valor que você colocou em `VERIFY_TOKEN` no
   Passo 2.
4. **Campos de assinatura:** marcar **messages**.
5. **Verificar e salvar** — se o Worker já estiver no ar com os segredos
   configurados, o Meta confirma na hora.

## Limitações conhecidas deste MVP (leia antes de confiar demais)

- **Matching por palavra-chave, não por IA.** Previsível e barato, mas
  erra em frase muito indireta ou ambígua. Testado com uma amostra pequena
  de frases reais e acertou a maioria — não é infalível.
- **"Eventos da Semana"** não responde com dado real (a agenda muda toda
  semana e não está na biblioteca) — o bot manda uma resposta de espera
  genérica e loga pra humano completar.
- **Reclamação, categorias institucionais (B-E) e "Fora do Escopo"** sempre
  respondem automaticamente *e* ficam marcadas nos logs como
  `NEEDS_HUMAN` — hoje isso só aparece nos logs (`npx wrangler tail` em
  tempo real, ou o dashboard da Cloudflare). **Ainda não existe
  notificação em tempo real** (Slack, e-mail, WhatsApp) — alguém precisa
  checar os logs periodicamente até isso ser conectado.
- **Comentários públicos do Instagram não são cobertos** — só mensagem
  direta (DM). Responder comentário publicamente com bot é mais arriscado
  pra marca e foi deixado de fora de propósito.
- Sem testes automatizados ainda (só validação manual local). Antes de
  considerar isso "em produção de verdade", vale mandar mensagens de teste
  reais pro Instagram e conferir se a resposta e o log batem com o
  esperado.

## Próximo passo: notificação de verdade

Hoje `notifyHuman()` em `src/worker.js` só faz `console.log`. Trocar por
notificação real é a mudança mais valiosa depois do deploy ir pro ar — por
exemplo, um webhook do Slack (`fetch` num incoming webhook URL) ou um
envio de e-mail. É uma chamada a mais dentro dessa mesma função, não
precisa redesenhar nada.

## Comandos úteis

```
node scripts/parse-biblioteca.js   # re-gerar data/biblioteca.json depois de editar a biblioteca
npx wrangler dev --local           # testar localmente antes de mandar pro ar
npx wrangler deploy                # publicar (depois de autenticado)
npx wrangler tail                  # ver os logs em tempo real, incluindo NEEDS_HUMAN
```
