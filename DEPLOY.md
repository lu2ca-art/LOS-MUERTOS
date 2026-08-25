# Deploy — como o site da Vila vai pro ar

> Leia isto antes de tentar publicar qualquer coisa. O que parecia
> "não consigo subir" era, na verdade, "subiu mas ninguém consegue abrir".

## Como está montado

O projeto Vercel **`los-muertos`** está ligado ao repositório
`lu2ca-art/LOS-MUERTOS` e faz deploy sozinho **a cada push, em qualquer branch**.

- push na `main` → deploy de **produção**
- push em qualquer outro branch → deploy de **preview**, com URL própria

Não precisa criar projeto novo, não precisa subir arquivo na mão. É só commitar
e dar push — a Vercel faz o resto em ~1 minuto.

## URLs

| o quê | endereço |
|---|---|
| produção | `los-muertos-zeta.vercel.app` |
| landing page da Vila (branch `claude/landing-page-cardapio-zgdjll`) | `los-muertos-git-claude-landi-0822b8-luccaminibal-7179s-projects.vercel.app/site/` |
| painel do projeto | vercel.com/luccaminibal-7179s-projects/los-muertos |

O site fica em `/site/` porque a **Root Directory** do projeto é a raiz do
repositório. Se quiser que a landing page seja a página principal (`/`), mude a
Root Directory pra `site` em *Project Settings → General → Root Directory*.

## ⚠️ Os dois problemas que travam tudo

### 1. Vercel Authentication (Deployment Protection)

Estava **ligado** (`ssoProtection: all_except_custom_domains`). Com isso, toda
URL `.vercel.app` do projeto responde `302` e joga pra tela de login da Vercel.
Resultado: o deploy funciona, mas o link não abre pra ninguém que não esteja
logado na conta — nem pra clientes, nem pra equipe, nem pro Claude em sessões
seguintes.

**Como desligar:**
`vercel.com` → projeto **los-muertos** → **Settings** → **Deployment Protection**
→ *Vercel Authentication* → **Disabled** → **Save**

### 2. A autorização da Vercel no Claude é somente leitura

O Claude consegue listar projetos, ver deployments e buscar conteúdo de URLs
protegidas — mas recebe `403 forbidden` ao tentar **criar** ou **alterar**
projeto. Ou seja: ele não consegue consertar o item 1 sozinho, nem criar um
projeto novo.

**Como resolver:**
claude.ai → **Settings** → **Connectors** → **Vercel** → reconectar, autorizando
acesso **a todos os projetos** (não "projetos selecionados") e com permissão de
escrita.

## Checklist pra publicar algo novo

1. Commit e push no branch de trabalho
2. Esperar ~1 min — o deploy sai sozinho
3. Pegar a URL de preview no painel da Vercel (ou pedir pro Claude listar)
4. Pra ir pra produção: merge na `main`
