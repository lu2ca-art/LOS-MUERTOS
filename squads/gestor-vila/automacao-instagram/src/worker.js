import categorias from "../data/biblioteca.json";
import { matchIntent } from "./match.js";

const GRAPH_API_VERSION = "v21.0";

function hex(buffer) {
  return [...new Uint8Array(buffer)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

function timingSafeEqualStr(a, b) {
  if (a.length !== b.length) return false;
  let result = 0;
  for (let i = 0; i < a.length; i++) result |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return result === 0;
}

async function isValidSignature(rawBody, signatureHeader, appSecret) {
  if (!appSecret) return true; // sem APP_SECRET configurado, pula validação (só pra dev/teste)
  if (!signatureHeader) return false;
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(appSecret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const sigBuffer = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(rawBody));
  const expected = "sha256=" + hex(sigBuffer);
  return timingSafeEqualStr(expected, signatureHeader);
}

// Ponto único pra "avisar um humano". Hoje só loga (visível em `wrangler
// tail` e no dashboard da Cloudflare) — trocar por um webhook do
// Slack/e-mail/WhatsApp quando escolherem o canal. Ver README.md, seção
// "Próximo passo: notificação de verdade".
function notifyHuman(reason, senderId, userText, replySent) {
  console.log(
    JSON.stringify({
      tag: "NEEDS_HUMAN",
      reason,
      senderId,
      userText,
      replySent,
      at: new Date().toISOString(),
    })
  );
}

async function sendReply(recipientId, text, pageAccessToken) {
  const url = `https://graph.facebook.com/${GRAPH_API_VERSION}/me/messages?access_token=${encodeURIComponent(
    pageAccessToken
  )}`;
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ recipient: { id: recipientId }, message: { text } }),
  });
  if (!res.ok) {
    const body = await res.text().catch(() => "");
    console.error("Falha ao enviar resposta via Graph API:", res.status, body);
  }
}

async function processEvents(payload, env) {
  const pageAccessToken = env.PAGE_ACCESS_TOKEN;
  const entries = payload.entry || [];
  for (const entry of entries) {
    const messagingEvents = entry.messaging || [];
    for (const event of messagingEvents) {
      // Ignora eco do próprio bot, confirmações de leitura, etc.
      if (!event.message || event.message.is_echo) continue;
      const senderId = event.sender && event.sender.id;
      const text = event.message.text;
      if (!senderId || !text) continue;

      const match = matchIntent(text, categorias);

      if (match.isFallback) {
        const fallback = categorias.find((c) => c.isForaEscopo);
        const reply = fallback ? fallback.resposta : "Já te retorno, um instante!";
        if (pageAccessToken) await sendReply(senderId, reply, pageAccessToken);
        notifyHuman("sem-match-confiavel", senderId, text, reply);
        continue;
      }

      const cat = match.categoria;
      if (pageAccessToken) await sendReply(senderId, cat.resposta, pageAccessToken);

      const needsHuman = cat.isReclamacao || cat.isInstitucional || cat.requiresManualData;
      if (needsHuman) {
        notifyHuman(
          cat.isReclamacao ? "reclamacao" : cat.isInstitucional ? "institucional" : "precisa-dado-atualizado",
          senderId,
          text,
          cat.resposta
        );
      }
    }
  }
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // --- Verificação do webhook (Meta chama isso quando você registra a URL) ---
    if (request.method === "GET") {
      const mode = url.searchParams.get("hub.mode");
      const token = url.searchParams.get("hub.verify_token");
      const challenge = url.searchParams.get("hub.challenge");
      if (mode === "subscribe" && token === env.VERIFY_TOKEN) {
        return new Response(challenge, { status: 200 });
      }
      return new Response("Verificação falhou — verify_token não bate.", { status: 403 });
    }

    if (request.method !== "POST") {
      return new Response("Method Not Allowed", { status: 405 });
    }

    const rawBody = await request.text();
    const signature = request.headers.get("x-hub-signature-256");
    if (!(await isValidSignature(rawBody, signature, env.APP_SECRET))) {
      return new Response("Invalid signature", { status: 401 });
    }

    let payload;
    try {
      payload = JSON.parse(rawBody);
    } catch {
      return new Response("JSON inválido", { status: 400 });
    }

    // Responde 200 na hora (boa prática — evita retry do Meta) e processa o
    // resto em background com waitUntil, sem segurar a resposta.
    ctx.waitUntil(
      processEvents(payload, env).catch((err) => console.error("Erro processando evento:", err))
    );

    return new Response("EVENT_RECEIVED", { status: 200 });
  },
};
