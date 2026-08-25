# Site da Vila Los Muertos de Fome

Landing page única, estática (HTML + CSS + JS, sem build). Abre direto: é só dar
duplo clique no `index.html` ou subir a pasta em qualquer hospedagem.

```
site/
├── index.html        ← a página inteira
├── css/styles.css    ← visual (paleta, tipografia, layout)
├── js/config.js      ← *** o que você vai mexer no dia a dia ***
├── js/main.js        ← comportamento (carrossel, horário, filtros)
├── img/              ← fotos
└── vercel.json       ← configuração de cache pra publicação
```

## 1. O que precisa ser preenchido antes de divulgar

Abra **`js/config.js`** e troque:

| campo | o que é |
|---|---|
| `whatsapp` | **obrigatório.** Número real da Vila, só dígitos, com 55 + DDD. Ex: `5511987654321`. Hoje está com um número de exemplo. |

Todo o resto (iFood, 99Food, Instagram, endereço, horários) já está preenchido
com os dados reais da casa.

## 2. As fotos — numeradas na ordem da página

Toda foto do site tem um número, na ordem em que aparece de cima pra baixo.
Para trocar qualquer uma: **salve a foto nova com o mesmo número** em `site/img/`
(ex.: `7.jpg`) e pronto — o site pega sozinho, não precisa mexer em código.

Hoje todas as 34 já existem (recortes dos encartes e dos posts), então o site
está completo. Substitua na ordem de prioridade que der.

### Carrossel do topo — as mais importantes

| nº | onde aparece | que foto tirar |
|----|--------------|----------------|
| 1 | fundo do slide "rodízio" | close de totopos enchendo o quadro inteiro |
| 2 | foto do slide "rodízio" | panelinha mexicana completa, vista de cima |
| 3 | fundo do slide "delivery" | close de cheddar derretido escorrendo |
| 4 | foto do slide "delivery" | mini burgers |
| 5 | fundo do slide "música ao vivo" | salão à noite com show rolando |
| 6 | foto do slide "música ao vivo" | tacos e burrito na tábua |
| 7 | fundo do slide "eventos" | mesa grande de grupo, clima de festa |
| 8 | foto do slide "eventos" | combo completo: taco + burrito + tostada |

### Faixa de delivery

| nº | onde aparece | que foto tirar |
|----|--------------|----------------|
| 9 | fundo da faixa "a gente leva" | totopos ou prato em close, bem texturizado |

### Rodízio — as 4 etapas + sobremesa

| nº | etapa | que foto tirar |
|----|-------|----------------|
| 10 | entradas | panelinha com totopos, batata e onion rings |
| 11 | etapa 1 | burrito de carne, tacos e quesadilla |
| 12 | etapa 2 | mini lanche de pernil e mini burgers |
| 13 | etapa 3 | taco al pastor, enchillada e tostada |
| 14 | sobremesa | churritos com sorvete |

### Faixa do meio

| nº | onde aparece | que foto tirar |
|----|--------------|----------------|
| 15 | "tudo feito na hora" | guacamole sendo batido ou preparo na cozinha |

### Cardápio à la carte

| nº | prato |
|----|-------|
| 16 | entremès tex mex |
| 17 | nachos con chilli |
| 18 | nachos con guacamole |
| 19 | nachos muy lokos |
| 20 | queso que te quiero |
| 21 | quesadilla corn bacon |
| 22 | dobradilla |
| 23 | el taco |
| 24 | el burriton |
| 25 | al pastor |
| 26 | tostadas |
| 27 | enchilladas |

### Eventos e nosso espaço

| nº | onde aparece | que foto tirar |
|----|--------------|----------------|
| 28 | seção eventos | mesa montada para um grupo grande |
| 29 | galeria | salão cheio à noite |
| 30 | galeria | mesa servida |
| 31 | galeria | noite de música ao vivo |
| 32 | galeria | turma na Vila, gente se divertindo |
| 33 | galeria | fachada da casa |
| 34 | galeria | detalhe da decoração |

### Como tirar

- **Horizontal**, no mínimo **1600px** de largura
- Luz do ambiente, **sem flash**
- Prato de cima ou em 45°, fundo escuro
- JPG direto do celular serve

## 3. Galeria "nosso espaço"

A galeria já usa as fotos 29 a 34. Para escolher outras, liste em
`js/config.js`:

```js
galeria: [
  { src: "img/29.jpg", alt: "salão à noite" },
  { src: "img/30.jpg", alt: "mesa grande pra turma" }
]
```

Enquanto a lista estiver vazia, a seção mostra fotos de prato + um aviso de onde
colocar as imagens do salão.

## 4. Mudar preço ou item do cardápio

Estão escritos direto no `index.html`, cada um num bloco `<article class="item">`.
Procure o nome do prato no arquivo e edite o texto e o valor.

## 5. Publicar

- **Vercel / Netlify:** aponte para a pasta `site/`, sem comando de build.
- **Hospedagem comum (FTP):** suba o conteúdo da pasta `site/` para a raiz.

## Detalhes que o site faz sozinho

- Mostra **"aberto agora / fechado"** no topo, calculado no fuso de São Paulo
  a partir dos horários do `config.js`.
- Destaca o dia de hoje na tabela de horários.
- Carrossel gira sozinho a cada 7s, pausa quando o mouse está em cima, aceita
  seta do teclado e arrastar no celular.
- Respeita quem tem "reduzir movimento" ligado no sistema.
