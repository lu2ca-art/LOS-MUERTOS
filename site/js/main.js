/* =========================================================================
   VILA LOS MUERTOS DE FOME — comportamento do site
   ========================================================================= */
(function () {
  "use strict";
  var C = window.VILA || {};

  /* ---------- links (whatsapp, delivery, redes) ------------------------- */
  function zap(msg) {
    return "https://wa.me/" + C.whatsapp + "?text=" + encodeURIComponent(msg || "");
  }
  var MSG = {
    reserva: C.msgReserva, rodizio: C.msgRodizio,
    evento: C.msgEvento, delivery: C.msgDelivery
  };
  document.querySelectorAll("[data-zap]").forEach(function (a) {
    a.setAttribute("href", zap(MSG[a.dataset.zap]));
    a.setAttribute("target", "_blank");
    a.setAttribute("rel", "noopener");
  });
  document.querySelectorAll("[data-link]").forEach(function (a) {
    a.setAttribute("href", C[a.dataset.link] || "#");
  });

  var end = document.getElementById("endereco");
  if (end && C.endereco) end.textContent = C.endereco;
  var mapa = document.getElementById("mapa");
  if (mapa && C.mapsEmbed) mapa.setAttribute("src", C.mapsEmbed);
  var ano = document.getElementById("ano");
  if (ano) ano.textContent = new Date().getFullYear();

  /* ---------- horário de São Paulo -------------------------------------- */
  function agoraSP() {
    try {
      var f = new Intl.DateTimeFormat("pt-BR", {
        timeZone: "America/Sao_Paulo", weekday: "short", hour: "2-digit",
        minute: "2-digit", hour12: false
      }).formatToParts(new Date());
      var o = {};
      f.forEach(function (p) { o[p.type] = p.value; });
      var dias = { "dom": 0, "seg": 1, "ter": 2, "qua": 3, "qui": 4, "sex": 5, "sáb": 6, "sab": 6 };
      var d = dias[(o.weekday || "").replace(".", "").toLowerCase().slice(0, 3)];
      return { dia: typeof d === "number" ? d : new Date().getDay(),
               h: parseInt(o.hour, 10), m: parseInt(o.minute, 10) };
    } catch (e) {
      var n = new Date();
      return { dia: n.getDay(), h: n.getHours(), m: n.getMinutes() };
    }
  }

  var NOMES = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"];
  function hhmm(v) { return (v === 24 ? "00" : (v < 10 ? "0" + v : v)) + "h"; }

  var t = agoraSP();
  var hoje = (C.horarios || {})[t.dia];
  var minutos = t.h * 60 + t.m;

  var elStatus = document.getElementById("status");
  var elTxt = document.getElementById("statusTxt");
  if (elStatus && elTxt && hoje) {
    var aberto = minutos >= hoje.abre * 60 && minutos < hoje.fecha * 60;
    elStatus.setAttribute("data-aberto", aberto ? "1" : "0");
    if (aberto) {
      elTxt.textContent = "aberto agora · até " + hhmm(hoje.fecha);
    } else if (minutos < hoje.abre * 60) {
      elTxt.textContent = "abre hoje às " + hhmm(hoje.abre);
    } else {
      var prox = (t.dia + 1) % 7, p = (C.horarios || {})[prox];
      elTxt.textContent = "fechado agora · volta " + NOMES[prox] + " às " + hhmm(p ? p.abre : 11);
    }
  }

  var ul = document.getElementById("horarios");
  if (ul && C.horarios) {
    var ordem = [1, 2, 3, 4, 5, 6, 0];
    ul.innerHTML = ordem.map(function (d) {
      var h = C.horarios[d];
      var faixa = h ? hhmm(h.abre) + " às " + hhmm(h.fecha) : "fechado";
      var extra = d === 1 ? " <span style=\"color:var(--cinza-2)\">(noite: eventos privados)</span>" : "";
      return "<li class=\"" + (d === t.dia ? "hoje" : "") + "\"><span>" + NOMES[d] +
             extra + "</span><b>" + faixa + "</b></li>";
    }).join("");
  }

  /* ---------- menu mobile ------------------------------------------------ */
  var burger = document.getElementById("burger"), menu = document.getElementById("menuNav");
  if (burger && menu) {
    burger.addEventListener("click", function () {
      var ab = burger.getAttribute("aria-expanded") === "true";
      burger.setAttribute("aria-expanded", String(!ab));
      menu.classList.toggle("aberto", !ab);
    });
    menu.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        menu.classList.remove("aberto");
        burger.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---------- carrossel automático --------------------------------------- */
  var car = document.getElementById("carrossel");
  var trilho = document.getElementById("slides");
  if (car && trilho) {
    var slides = Array.prototype.slice.call(trilho.children);
    var pontos = document.getElementById("pontos");
    var atual = 0, timer = null;
    var DUR = 7000;
    var reduz = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    slides.forEach(function (s, i) {
      var b = document.createElement("button");
      b.className = "ponto";
      b.setAttribute("role", "tab");
      b.setAttribute("aria-label", "destaque " + (i + 1));
      b.addEventListener("click", function () { ir(i, true); });
      pontos.appendChild(b);
    });
    document.documentElement.style.setProperty("--dur", DUR + "ms");

    function pinta() {
      trilho.style.transform = "translateX(-" + (atual * 100) + "%)";
      slides.forEach(function (s, i) {
        s.classList.toggle("is-on", i === atual);
        s.setAttribute("aria-hidden", i === atual ? "false" : "true");
      });
      Array.prototype.forEach.call(pontos.children, function (p, i) {
        if (i === atual) { p.setAttribute("aria-current", "true"); }
        else { p.removeAttribute("aria-current"); }
      });
      // reinicia a barrinha de progresso
      var ativo = pontos.children[atual];
      if (ativo) { var c = ativo.cloneNode(true);
        c.addEventListener("click", function () { ir(atual, true); });
        pontos.replaceChild(c, ativo);
        c.setAttribute("aria-current", "true"); }
    }
    function ir(i, manual) {
      atual = (i + slides.length) % slides.length;
      pinta();
      if (manual) roda();
    }
    function roda() {
      clearInterval(timer);
      if (reduz) return;
      timer = setInterval(function () { ir(atual + 1); }, DUR);
    }

    document.getElementById("prox").addEventListener("click", function () { ir(atual + 1, true); });
    document.getElementById("ant").addEventListener("click", function () { ir(atual - 1, true); });

    car.addEventListener("mouseenter", function () { clearInterval(timer); car.classList.add("pausado"); });
    car.addEventListener("mouseleave", function () { car.classList.remove("pausado"); roda(); });
    car.addEventListener("focusin", function () { clearInterval(timer); car.classList.add("pausado"); });
    car.addEventListener("focusout", function () { car.classList.remove("pausado"); roda(); });
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) { clearInterval(timer); } else { roda(); }
    });
    car.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") ir(atual + 1, true);
      if (e.key === "ArrowLeft") ir(atual - 1, true);
    });

    // arrastar no celular
    var x0 = null;
    car.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; clearInterval(timer); }, { passive: true });
    car.addEventListener("touchend", function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 45) { ir(atual + (dx < 0 ? 1 : -1), true); } else { roda(); }
      x0 = null;
    });

    pinta(); roda();
  }

  /* ---------- filtros do cardápio ---------------------------------------- */
  var filtros = document.querySelectorAll(".filtro");
  var grupos = document.querySelectorAll(".grupo");
  filtros.forEach(function (b) {
    b.addEventListener("click", function () {
      filtros.forEach(function (o) { o.setAttribute("aria-pressed", String(o === b)); });
      var f = b.dataset.f;
      grupos.forEach(function (g) {
        g.style.display = (f === "todos" || g.dataset.g === f) ? "" : "none";
      });
    });
  });

  /* ---------- galeria "nosso espaço" ------------------------------------- */
  var gal = document.getElementById("galeria");
  if (gal) {
    var fotos = (C.galeria && C.galeria.length) ? C.galeria : null;
    if (fotos) {
      gal.innerHTML = fotos.map(function (f) {
        return "<figure><img src=\"" + f.src + "\" alt=\"" + (f.alt || "espaço da Vila") + "\" loading=\"lazy\"></figure>";
      }).join("");
    } else {
      var padrao = [
        { src: "img/29.jpg", alt: "salão da Vila" },
        { src: "img/30.jpg", alt: "mesa servida" },
        { src: "img/31.jpg", alt: "noite de música ao vivo" },
        { src: "img/32.jpg", alt: "turma na Vila" },
        { src: "img/33.jpg", alt: "fachada" },
        { src: "img/34.jpg", alt: "detalhe da casa" }
      ];
      gal.innerHTML = padrao.map(function (f) {
        return "<figure><img src=\"" + f.src + "\" alt=\"" + f.alt + "\" loading=\"lazy\"></figure>";
      }).join("");
    }
  }

  /* ---------- animação de entrada ---------------------------------------- */
  var alvos = document.querySelectorAll(".rev");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (ent) {
      ent.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("on"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: .12 });
    alvos.forEach(function (a) { io.observe(a); });
  } else {
    alvos.forEach(function (a) { a.classList.add("on"); });
  }
})();
