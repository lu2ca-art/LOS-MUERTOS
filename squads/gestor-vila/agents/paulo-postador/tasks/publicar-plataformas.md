---
task: "Publicar em Plataformas"
order: 1
input: |
  - conteudo: output/conteudo.md — copy por slot e por plataforma
  - visual: output/visual-01.jpg — imagem do feed
  - aprovacao: confirmação explícita do usuário no Step 04
skills:
  - instagram-publisher
  - blotato
output: |
  - file: output/publicacoes.md — relatório de publicação com URLs e status por plataforma
---

# Publicar em Plataformas

## Descrição

Paulo executa a publicação após aprovação explícita. Nunca publica sem confirmação. Dry-run primeiro, publicação real depois. Reporta URL de cada publicação bem-sucedida.

## REGRA ABSOLUTA

**Nunca publicar sem aprovação explícita do usuário no checkpoint Step 04.**
Se não há aprovação registrada, Paulo para e aguarda. Não há exceção.

## Processo

### 1. Verificar aprovação

Confirmar que o checkpoint Step 04 foi respondido com aprovação. Se não há resposta de aprovação:
- Parar imediatamente
- Exibir: `PUBLICAÇÃO SUSPENSA — Aguardando aprovação do Step 04`
- Não continuar

### 2. Preparar adaptações por plataforma

Do `output/conteudo.md`, adaptar o POST PRINCIPAL para cada plataforma:

| Plataforma        | Limite      | Adaptação necessária                        | Skill         |
|-------------------|-------------|---------------------------------------------|---------------|
| Instagram (feed)  | 2.200 chars | Copy original + visual-01.jpg               | instagram-publisher |
| Facebook          | 63.206 chars| Copy original + visual-01.jpg               | blotato       |
| TikTok            | 2.200 chars | Copy encurtado, hashtags específicos TikTok | blotato       |
| Google Meu Negócio| 1.500 chars | Copy informativo, foco em endereço/horário  | blotato       |

**Adaptação TikTok:** retirar o CTA "vem com a galera" e substituir por call direto para o vídeo/local. Adicionar 3-5 hashtags relevantes (ex: #BarueriSP #MusicaAoVivo #VilaDe MuertosDeFome).

**Adaptação Google Meu Negócio:** foco em informação prática (endereço, horário de funcionamento, evento do dia). Sem tom poético — usuário busca info.

### 3. Verificar horário de publicação

| Plataforma          | Horário ideal    | Fallback              |
|---------------------|------------------|-----------------------|
| Instagram           | 18h – 21h        | 12h se evento hoje à noite |
| Facebook            | junto com Instagram | sem delay            |
| TikTok              | 12h OU 20h       | preferir 20h para show noturno |
| Google Meu Negócio  | 9h – 17h         | publicar quando disponível |

Se o horário atual está fora do ideal, perguntar ao usuário: publicar agora ou agendar?

### 4. Executar dry-run

Antes de qualquer publicação real:

```
DRY-RUN CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Instagram credentials: válidas
[ ] visual-01.jpg: formato JPEG, ≤ 8MB, proporção 4:5 (1080×1350) ou quadrado
[ ] Copy Instagram: ≤ 2.200 chars — [CONTADOR]
[ ] Facebook credentials: válidas
[ ] TikTok credentials: válidas
[ ] Copy TikTok: ≤ 2.200 chars — [CONTADOR]
[ ] Google Meu Negócio credentials: válidas
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESULTADO: PASSOU / FALHOU em [item]
```

Se dry-run falhar em qualquer item: parar e reportar antes de continuar.

### 5. Publicar plataforma por plataforma

Publicar na ordem: Instagram → Facebook → TikTok → Google Meu Negócio

Após cada publicação, reportar resultado antes de continuar para a próxima.

**Se Instagram falhar:** reportar erro, perguntar se continua para as demais.
**Se qualquer outra falhar:** reportar, continuar com as restantes, documentar falha no relatório.

### 6. Salvar relatório

Salvar `output/publicacoes.md` com todas as URLs e status.

## Formato de Saída

```markdown
# Relatório de Publicação — [DATA] [HORA]

## Dry-Run
- Status: PASSOU / FALHOU
- [itens verificados]

## Publicações

| Plataforma          | Status    | URL                        | Horário       |
|---------------------|-----------|----------------------------|---------------|
| Instagram           | ✅ Publicado | [url]                   | [hora]        |
| Facebook            | ✅ Publicado | [url]                   | [hora]        |
| TikTok              | ✅ Publicado | [url]                   | [hora]        |
| Google Meu Negócio  | ✅ Publicado | [url]                   | [hora]        |

## Falhas
[se houver: descrição do erro e ação corretiva]

## Resumo
- Publicações bem-sucedidas: X/4
- Falhas: X
- Próximo passo: [Renata Revisão / corrigir falha X]
```

## Exemplo de Saída

```markdown
# Relatório de Publicação — quinta, 21 mai · 18h47

## Dry-Run
- Status: PASSOU
- Instagram JPEG 1080×1350 válido (2.1MB)
- Copy Instagram: 312 chars ✅
- Copy TikTok: 198 chars ✅

## Publicações

| Plataforma         | Status     | URL                                          | Horário |
|--------------------|------------|----------------------------------------------|---------|
| Instagram          | ✅ Publicado| https://instagram.com/p/ABC123              | 18h47   |
| Facebook           | ✅ Publicado| https://facebook.com/vilalosmuertos/posts/1  | 18h48   |
| TikTok             | ✅ Publicado| https://tiktok.com/@vilalosmuertos/video/1   | 18h49   |
| Google Meu Negócio | ✅ Publicado| [url GMB]                                   | 18h50   |

## Resumo
- Publicações bem-sucedidas: 4/4
- Próximo passo: Renata Revisão (Step 07)
```

## Critérios de Qualidade

- [ ] Aprovação explícita confirmada antes de publicar
- [ ] Dry-run executado e passou
- [ ] Copy adaptado por plataforma (não copy-paste)
- [ ] Publicação plataforma por plataforma com reporte
- [ ] URLs retornadas para todas as publicações bem-sucedidas
- [ ] Horário respeitado por plataforma
- [ ] Relatório salvo em output/publicacoes.md

## Condições de Veto

- **Publicar sem aprovação do Step 04** → VETO ABSOLUTO, nenhuma exceção
- **"Publicado" sem URL** → inválido, tentar novamente ou documentar como falha
- **Mesmo copy em todas as plataformas sem adaptação** → adaptar antes de publicar
