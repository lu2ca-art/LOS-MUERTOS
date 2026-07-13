---
task: "Criar Arte de Evento"
order: 3
input: |
  - conteudo: output/{projeto}/conteudo.md — seção ANÚNCIO PAGO com evento e dados
  - conceito: output/{projeto}/conceito-visual.md — conceito aprovado, seção ANÚNCIO PAGO
  - identity: pipeline/data/vila-identity.md — design system, paleta
skill: image-creator
output: |
  - file: output/{projeto}/arte-evento.jpg — arte 1080×1080px para anúncio pago (formato quadrado Meta Ads)
---

# Criar Arte de Evento

## Descrição

Arte específica para anúncio pago. Formato quadrado 1080×1080px (padrão Meta Ads e TikTok Ads). Mais direta e impactante que o visual de feed orgânico — precisa funcionar em 1 segundo de scroll. O nome do artista ou evento é o único elemento que importa no primeiro golpe de vista.

## Gatilho

Esta task roda apenas quando `output/{projeto}/conteudo.md` contém seção `## ANÚNCIO PAGO` **e** o conceito correspondente já foi aprovado pelo usuário em `conceito-visual.md`. Sem essas duas condições, não há arte de evento.

## Processo

### 1. Design system para arte de evento (formato quadrado)

```
Viewport:       1080 × 1080px (quadrado, padrão Meta/TikTok)
Background:     #1A1A1A com textura ou #C4502A como bloco de cor
Primária:       nome do evento em máximo impacto visual
Hierarquia:     1 elemento dominante + 2 elementos secundários máx
Margem segura:  80px em cada lado (Meta recomenda safe zone)
Texto no visual: máx 20% da área (regra Meta Ads para alcance máximo)
```

### 2. Extrair dados do anúncio

Do `output/conteudo.md`, seção ANÚNCIO PAGO:
- **Nome do evento:** artista OU "COPA 2026" OU nome do stand-up
- **Data + Horário:** formato curto ("SAB 23/05 · 21H")
- **Chamada direta:** 1 linha (extraída da headline do anúncio)

### 3. Layout por tipo de evento

**SHOW DE ARTISTA:**
- Bloco de cor terracota (#C4502A) na metade superior
- Nome do artista em Bebas Neue ou Oswald Bold, off-white, tamanho máximo possível
- "AO VIVO" em badge pequeno
- Metade inferior: fundo preto, data e "Vila Los Muertos de Fome" em amarelo

**COPA DO MUNDO:**
- Fundo #1A1A1A
- "COPA 2026" em amarelo Oswald Bold, tamanho máximo
- "Brasil vs X · [HORA]" em terracota
- Barra verde/amarela CSS no rodapé (cores Brasil sem imagem)
- "Vila Los Muertos de Fome" pequeno

**STAND-UP COMEDY:**
- Fundo preto total
- Microfone SVG simples no centro (via CSS border-radius criativo ou path simples)
- Nome do comediante em branco, bold
- Data em amarelo

### 4. Regra de texto ≤ 20% da área

Meta Ads penaliza visuais com texto em mais de 20% da área. Calcular:
- Área total: 1080 × 1080 = 1.166.400 px²
- 20% = 233.280 px²
- Manter texto confinado — elementos gráficos (cores, fundos) preenchem o resto

### 5. Renderizar e verificar

Chamar `image-creator`. Verificar:
- [ ] Formato exato 1080×1080px
- [ ] Nome do evento legível em 1 segundo
- [ ] Texto ≤ 20% da área (estimativa visual)
- [ ] Margens seguras respeitadas (80px em cada borda)
- [ ] Contraste ≥ 4.5:1

## Formato de Saída

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Bebas+Neue&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  width: 1080px;
  height: 1080px;
  overflow: hidden;
  /* ... */
}
</style>
</head>
<body>
  <!-- nome do evento dominante, data, vila -->
</body>
</html>
```

Salvar render como `output/arte-evento.jpg`.

## Exemplo de Saída

**Contexto:** LU2CA ao vivo, sábado 23/05, 21h

```
┌─────────────────────────────────────┐  <- #C4502A terracota
│                                     │
│           L U 2 C A                 │  <- Bebas Neue off-white, 144px
│                                     │
│         AO VIVO  ·  21H             │  <- Oswald 48px off-white
├─────────────────────────────────────┤  <- divisor amarelo 4px
│  SAB 23/05                          │  <- Oswald 36px amarelo
│  Vila Los Muertos de Fome           │  <- Oswald 28px off-white
│  Rua Caldas Novas 49 · Bethaville   │  <- Oswald 22px off-white 70%
└─────────────────────────────────────┘  <- #1A1A1A preto
```

## Critérios de Qualidade

- [ ] Formato 1080×1080px exato
- [ ] Nome do evento é o elemento dominante
- [ ] Texto ≤ 20% da área total
- [ ] Margem segura ≥ 80px em cada borda
- [ ] Render executado e verificado
- [ ] Zero texto genérico ou placeholder

## Condições de Veto

- **Texto ocupa mais de 30% da área** → redesenhar com elementos gráficos maiores
- **Nome do evento não é legível em 1 segundo** → aumentar tamanho, reduzir elementos secundários
- **Formato errado (não 1080×1080)** → corrigir dimensões no body CSS
