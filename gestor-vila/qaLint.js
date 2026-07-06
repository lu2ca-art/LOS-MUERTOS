(function () {
const GENERIC_MARKETING_PHRASES = [
  'confira',
  'venha nos visitar',
  'link na bio',
];

const DIGITAL_CTA_PATTERN = /\b(clique|clica|acesse|acessa)\b/i;

const FINANCIAL_LEAK_PATTERN = /\b(cachê|cache|custo do contrato|valor do contrato)\b/i;
const CURRENCY_PATTERN = /r\$\s?\d/i;

function lintContent(text, meta = {}) {
  const findings = [];
  const lower = (text || '').toLowerCase();

  GENERIC_MARKETING_PHRASES.forEach((phrase) => {
    if (lower.includes(phrase)) {
      findings.push({
        rule: 'linguagem-generica',
        severity: 'warning',
        message: `Frase de marketing genérica encontrada: "${phrase}".`,
      });
    }
  });

  if (DIGITAL_CTA_PATTERN.test(text || '')) {
    findings.push({
      rule: 'cta-digital',
      severity: 'critical',
      message: 'CTA digital detectado. O CTA precisa ser físico (vem, reserva, aparece).',
    });
  }

  if (meta.tipo === 'show') {
    const faltando = [];
    if (!meta.artista) faltando.push('artista');
    if (!meta.horario) faltando.push('horário');
    if (!meta.dia) faltando.push('dia');
    if (faltando.length) {
      findings.push({
        rule: 'show-incompleto',
        severity: 'critical',
        message: `Story de show sem: ${faltando.join(', ')}.`,
      });
    }
  }

  if (FINANCIAL_LEAK_PATTERN.test(text || '') || (CURRENCY_PATTERN.test(text || '') && FINANCIAL_LEAK_PATTERN.test(text || ''))) {
    findings.push({
      rule: 'vazamento-financeiro',
      severity: 'critical',
      message: 'Possível vazamento de valor financeiro interno (cachê/custo de contrato).',
    });
  }

  return findings;
}

function hasCriticalFindings(findings) {
  return findings.some((f) => f.severity === 'critical');
}

const qaLintExports = { lintContent, hasCriticalFindings };

if (typeof module !== 'undefined' && module.exports) module.exports = qaLintExports;
if (typeof window !== 'undefined') window.qaLint = qaLintExports;
})();
