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

## 2. Trocar/colocar fotos

Todas as imagens ficam em `img/`. Para trocar uma foto, **basta salvar a nova
com o mesmo nome do arquivo** — o site pega sozinho.

| arquivo | onde aparece |
|---|---|
| `tex-nachos.jpg`, `tex-guacamole.jpg`, `tex-cheddar.jpg` | fundos das faixas e dos slides |
| `prato-panelinha.jpg` | entrada do rodízio / entremès tex mex |
| `prato-tacos-burrito.jpg` | etapa 1 do rodízio / enchilladas |
| `prato-miniburger.jpg` | etapa 2 do rodízio / slide de delivery |
| `prato-tostada.jpg` | etapa 3 do rodízio / tostadas |
| `prato-quesadilla.jpg`, `prato-quesadillas-hero.jpg` | quesadillas |
| `prato-nachos-chilli.jpg` | nachos con chilli |
| `prato-alpastor.jpg`, `prato-burriton.jpg`, `prato-taco-pastor.jpg` | originais |
| `prato-combo.jpg` | combos / eventos |

**Recomendação:** fotos na horizontal com no mínimo 1600px de largura, JPG de boa
qualidade. As fotos atuais foram extraídas dos encartes impressos e dos posts do
Instagram — servem, mas foto profissional do prato real deixa o site num outro
patamar.

## 3. Galeria "nosso espaço"

Salve as fotos do salão em `img/` (ex.: `espaco-01.jpg`) e liste em
`js/config.js`:

```js
galeria: [
  { src: "img/espaco-01.jpg", alt: "salão à noite" },
  { src: "img/espaco-02.jpg", alt: "mesa grande pra turma" }
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
