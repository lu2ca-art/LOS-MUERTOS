/* =========================================================================
   VILA LOS MUERTOS DE FOME — configuração central
   Tudo que muda com o tempo (telefone, links, promoções) está AQUI.
   Editar este arquivo é suficiente — não precisa mexer no resto do site.
   ========================================================================= */

window.VILA = {

  /* --- contato -----------------------------------------------------------
     whatsapp: só números, com 55 (país) + 11 (DDD). Sem espaço, sem traço.
     >>> TROCAR PELO NÚMERO REAL DA VILA <<<                                */
  whatsapp: "5511000000000",

  /* mensagens que já vão escritas quando a pessoa clica */
  msgReserva: "oi! quero reservar uma mesa na Vila. pode confirmar pra mim?",
  msgRodizio: "oi! queria saber do rodízio Tex Mex — dia, horário e mesa pra quantas pessoas.",
  msgEvento:  "oi! quero fazer um evento na Vila. me passa o orçamento?",
  msgDelivery:"oi! quero pedir delivery direto com vocês.",

  /* --- redes e delivery -------------------------------------------------- */
  instagram: "https://www.instagram.com/vilalosmuertosdefome/",
  ifood:  "https://www.ifood.com.br/delivery/barueri-sp/vila-los-muertos-de-fome-bethaville-i/d3cc6212-4f83-4611-87c8-8fd67f2b8cad",
  food99: "https://oia.99app.com/dlp9/5iJezd?area=BR",

  /* --- endereço ---------------------------------------------------------- */
  endereco: "Rua Caldas Novas, 49 — Bethaville I, Barueri/SP",
  maps: "https://www.google.com/maps/search/?api=1&query=Vila+Los+Muertos+de+Fome+Rua+Caldas+Novas+49+Bethaville+Barueri+SP",
  mapsEmbed: "https://www.google.com/maps?q=Rua+Caldas+Novas,+49+-+Bethaville+I,+Barueri+-+SP&output=embed",

  /* --- horários (24h, fuso de São Paulo) ---------------------------------
     0 = domingo ... 6 = sábado. fecha 24 = meia-noite.                     */
  horarios: {
    0: { abre: 11, fecha: 23 },
    1: { abre: 11, fecha: 15 },
    2: { abre: 11, fecha: 23 },
    3: { abre: 11, fecha: 23 },
    4: { abre: 11, fecha: 23 },
    5: { abre: 11, fecha: 23 },
    6: { abre: 11, fecha: 24 }
  },

  /* --- galeria "nosso espaço" -------------------------------------------
     Coloque as fotos do salão em site/img/ e liste os arquivos aqui.
     Ex.: { src: "img/espaco-01.jpg", alt: "salão à noite" }
     Enquanto estiver vazio, a seção mostra os slots com instrução.        */
  galeria: []
};
