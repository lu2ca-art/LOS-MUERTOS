---
task: "Criar Visual"
order: 1
input: |
  - angulo_selecionado: O ângulo com lens e linha de abertura
  - tom_confirmado: Tom de voz da sessão
  - conteudo_instagram: Caption ou script gerado por Carlos Caption na mesma sessão
output: |
  - visual_html: Código HTML/CSS completo do visual 1080×1440px
  - visual_rendered: Arquivo JPEG renderizado via skill image-creator (output/visual-01.jpg)
  - notas_visuais: Decisões de design: cor dominante, tipografia, hierarquia aplicada
---

# Criar Visual

Diana Design cria o visual de fundo para o post de feed ou Reel — 1080×1440px em HTML/CSS, renderizado via skill `image-creator`. O visual segue o design system CIDADE NEON: fundo escuro, acentos neon, grain texture, tipografia bold sem serifa. Nunca cria layout claro, nunca usa gradiente pastel, nunca centraliza logo de forma que compete com o texto.

## Process

1. **Carregar design system:** Internalizar o design system CIDADE NEON definido nos dados do pipeline. Paleta primária: fundo #0a0a0a, neon amarelo #f9f320, neon ciano #00f5e9, coral #ff2d55. Grain texture: SVG noise filter opacity 0.06-0.10. Tipografia: bold sans-serif (Inter Bold / Bebas Neue).

2. **Derivar tom visual do conteúdo:** Ler a caption ou script de Carlos Caption. Mapear o tom confirmado para decisão visual:
   - Lírico/Poético → ciano #00f5e9, espaçamento amplo, minimalismo
   - Filosófico → branco sobre #0a0a0a, texto dominante
   - Motivacional → amarelo #f9f320, energia, contraste máximo
   - Comunitário → coral #ff2d55, elemento de movimento ou viagem
   - Cultural → paleta mínima, 1 emoji de identidade como âncora
   - Vulnerável → fundo quase preto, texto pequeno, silêncio visual

3. **Definir hierarquia tipográfica:** Máx 3 elementos visuais por layout. Hierarquia: (1) palavra ou frase âncora em destaque, (2) linha de suporte em corpo menor, (3) URL lu2ca.art ou elemento de era — sempre presente mas nunca dominante.

4. **Escrever HTML/CSS:** Produzir código completo autocontido. Dimensões: 1080×1440px. Incluir: SVG noise filter para grain, fonte carregada via Google Fonts ou system font stack, grain aplicado como pseudo-elemento ou overlay. Sem JavaScript. Inline styles para garantir render consistente.

5. **Renderizar via image-creator:** Chamar o skill `image-creator` com o HTML produzido. Output salvo em `output/visual-01.jpg`.

6. **Verificar resultado:** O visual passa no checklist? Fundo escuro? Grain presente? Nenhum elemento em fundo claro? lu2ca.art visível mas não dominante?

## Output Format

```
=== VISUAL HTML ===
[código HTML/CSS completo — 1080×1440px, autocontido]

=== RENDER ===
[chamada ao skill image-creator]
Arquivo: output/visual-01.jpg

=== NOTAS VISUAIS ===
Tom aplicado: [nome do tom]
Cor dominante: [hex]
Tipografia: [fonte usada]
Grain: [opacity aplicada]
lu2ca.art: [posição no layout]
```

## Output Example

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&display=swap');
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1080px; height: 1440px; overflow: hidden;
    background: #0a0a0a; font-family: 'Inter', sans-serif;
    position: relative;
  }
  .grain {
    position: absolute; inset: 0; z-index: 10;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
    opacity: 0.07; pointer-events: none;
  }
  .content {
    position: relative; z-index: 20;
    display: flex; flex-direction: column;
    justify-content: center; align-items: flex-start;
    height: 100%; padding: 120px 90px;
  }
  .headline {
    font-size: 148px; font-weight: 900; line-height: 0.9;
    color: #f9f320; text-transform: lowercase; letter-spacing: -4px;
  }
  .sub {
    font-size: 42px; font-weight: 900; color: #ffffff;
    margin-top: 60px; opacity: 0.85; text-transform: lowercase;
  }
  .url {
    position: absolute; bottom: 80px; left: 90px;
    font-size: 28px; font-weight: 900; color: #ffffff;
    opacity: 0.4; text-transform: lowercase; letter-spacing: 2px;
  }
</style>
</head>
<body>
  <div class="grain"></div>
  <div class="content">
    <div class="headline">segunda<br>não<br>vence</div>
    <div class="sub">mexe o corpitcho bebe 🛹</div>
  </div>
  <div class="url">lu2ca.art</div>
</body>
</html>
```

## Quality Criteria

- [ ] Dimensões exatas: 1080×1440px
- [ ] Fundo escuro (#0a0a0a ou similar — nunca claro)
- [ ] Grain texture presente (SVG noise, opacity 0.06-0.10)
- [ ] Máx 3 elementos visuais — hierarquia clara
- [ ] lu2ca.art presente no layout (pode ser discreto)
- [ ] Código HTML autocontido — sem dependências externas não carregadas
- [ ] Render executado via skill image-creator — output/visual-01.jpg confirmado

## Veto Conditions

Rejeitar e refazer se qualquer um for verdadeiro:
1. Background claro ou gradiente pastel — rejeição imediata, viola o design system CIDADE NEON
2. lu2ca.art ausente do visual — é o hub central, não pode faltar
