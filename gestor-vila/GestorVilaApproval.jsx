(function () {
const { lintContent, hasCriticalFindings } =
  typeof require !== 'undefined' ? require('./qaLint') : window.qaLint;

const CHECKPOINT_LABELS = {
  '04': 'Aprovação Humana ①',
  '09': 'Aprovação Final ②',
};

function SeverityBadge({ severity }) {
  const color = severity === 'critical' ? '#c0392b' : '#c9a227';
  return (
    <span
      style={{
        display: 'inline-block',
        padding: '2px 8px',
        borderRadius: 999,
        fontSize: 11,
        fontWeight: 700,
        textTransform: 'uppercase',
        color: '#0d0d0d',
        background: color,
        marginRight: 8,
      }}
    >
      {severity === 'critical' ? 'veto' : 'aviso'}
    </span>
  );
}

function LintFindings({ findings }) {
  if (!findings.length) {
    return (
      <p style={{ color: '#2a9d8f', fontSize: 13, margin: '8px 0' }}>
        Nenhuma violação das regras de qualidade encontrada.
      </p>
    );
  }
  return (
    <ul style={{ listStyle: 'none', padding: 0, margin: '8px 0' }}>
      {findings.map((f, i) => (
        <li key={i} style={{ marginBottom: 6, fontSize: 13 }}>
          <SeverityBadge severity={f.severity} />
          {f.message}
        </li>
      ))}
    </ul>
  );
}

function GestorVilaApproval({ run, checkpointId, approver = 'Luca', onApprove, onReject }) {
  const isContentCheckpoint = checkpointId === '04';
  const [editedLegenda, setEditedLegenda] = React.useState(
    isContentCheckpoint ? run.content?.legenda || '' : ''
  );
  const [rejecting, setRejecting] = React.useState(false);
  const [justification, setJustification] = React.useState('');
  const [error, setError] = React.useState(null);

  const meta = run.content || {};
  const findings = isContentCheckpoint ? lintContent(editedLegenda, meta) : [];
  const blocked = isContentCheckpoint && hasCriticalFindings(findings);

  const handleApprove = () => {
    setError(null);
    try {
      const payload = isContentCheckpoint
        ? { approver, editedContent: { legenda: editedLegenda } }
        : { approver };
      onApprove(payload);
    } catch (e) {
      setError(e.message);
    }
  };

  const handleConfirmReject = () => {
    setError(null);
    try {
      onReject({ approver, justification });
      setRejecting(false);
      setJustification('');
    } catch (e) {
      setError(e.message);
    }
  };

  return (
    <div
      style={{
        background: '#1a1512',
        border: '1px solid #3a2f26',
        borderRadius: 12,
        padding: 24,
        color: '#f2e9dc',
        fontFamily: 'system-ui, sans-serif',
        maxWidth: 640,
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
        <h2 style={{ margin: 0, fontSize: 18, color: '#e0b23c' }}>
          {CHECKPOINT_LABELS[checkpointId] || `Checkpoint ${checkpointId}`}
        </h2>
        <span style={{ fontSize: 12, opacity: 0.7 }}>{run.id}</span>
      </div>

      {isContentCheckpoint ? (
        <div style={{ marginTop: 16 }}>
          <label style={{ fontSize: 12, opacity: 0.8, display: 'block', marginBottom: 4 }}>
            Legenda
          </label>
          <textarea
            value={editedLegenda}
            onChange={(e) => setEditedLegenda(e.target.value)}
            rows={5}
            style={{
              width: '100%',
              background: '#0d0d0d',
              color: '#f2e9dc',
              border: '1px solid #3a2f26',
              borderRadius: 8,
              padding: 10,
              fontSize: 14,
              resize: 'vertical',
            }}
          />
          {run.visual?.canvaDesignId && (
            <p style={{ fontSize: 12, opacity: 0.6, marginTop: 6 }}>
              Arte: {run.visual.canvaDesignId}
            </p>
          )}
          <div style={{ marginTop: 12 }}>
            <LintFindings findings={findings} />
          </div>
        </div>
      ) : (
        <div style={{ marginTop: 16 }}>
          <p style={{ fontSize: 14, lineHeight: 1.5 }}>{run.content?.legenda}</p>
          {run.qaReport && (
            <p style={{ fontSize: 13, opacity: 0.8 }}>
              QA: {run.qaReport.aprovado ? 'aprovado' : 'reprovado'} — {run.qaReport.observacoes}
            </p>
          )}
          {run.metrics && (
            <div style={{ display: 'flex', gap: 16, marginTop: 8, fontSize: 13 }}>
              <span>Alcance: {run.metrics.alcance}</span>
              <span>Curtidas: {run.metrics.curtidas}</span>
              <span>Comentários: {run.metrics.comentarios}</span>
              <span>Compart.: {run.metrics.compartilhamentos}</span>
            </div>
          )}
        </div>
      )}

      {error && <p style={{ color: '#c0392b', fontSize: 13 }}>{error}</p>}

      {!rejecting ? (
        <div style={{ display: 'flex', gap: 12, marginTop: 20 }}>
          <button
            onClick={handleApprove}
            disabled={blocked}
            style={{
              background: blocked ? '#4a4a4a' : '#2a9d8f',
              color: '#0d0d0d',
              border: 'none',
              borderRadius: 8,
              padding: '10px 20px',
              fontWeight: 700,
              cursor: blocked ? 'not-allowed' : 'pointer',
            }}
            title={blocked ? 'Existe veto de qualidade pendente. Ajuste o texto.' : ''}
          >
            Aprovar
          </button>
          <button
            onClick={() => setRejecting(true)}
            style={{
              background: 'transparent',
              color: '#c0392b',
              border: '1px solid #c0392b',
              borderRadius: 8,
              padding: '10px 20px',
              fontWeight: 700,
              cursor: 'pointer',
            }}
          >
            Reprovar
          </button>
        </div>
      ) : (
        <div style={{ marginTop: 20 }}>
          <label style={{ fontSize: 12, opacity: 0.8, display: 'block', marginBottom: 4 }}>
            Justificativa da reprovação
          </label>
          <textarea
            value={justification}
            onChange={(e) => setJustification(e.target.value)}
            rows={3}
            style={{
              width: '100%',
              background: '#0d0d0d',
              color: '#f2e9dc',
              border: '1px solid #3a2f26',
              borderRadius: 8,
              padding: 10,
              fontSize: 14,
              resize: 'vertical',
            }}
          />
          <div style={{ display: 'flex', gap: 12, marginTop: 12 }}>
            <button
              onClick={handleConfirmReject}
              disabled={!justification.trim()}
              style={{
                background: !justification.trim() ? '#4a4a4a' : '#c0392b',
                color: '#f2e9dc',
                border: 'none',
                borderRadius: 8,
                padding: '10px 20px',
                fontWeight: 700,
                cursor: !justification.trim() ? 'not-allowed' : 'pointer',
              }}
            >
              Confirmar reprovação
            </button>
            <button
              onClick={() => setRejecting(false)}
              style={{
                background: 'transparent',
                color: '#f2e9dc',
                border: '1px solid #3a2f26',
                borderRadius: 8,
                padding: '10px 20px',
                cursor: 'pointer',
              }}
            >
              Cancelar
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

if (typeof module !== 'undefined' && module.exports) module.exports = GestorVilaApproval;
if (typeof window !== 'undefined') window.GestorVilaApproval = GestorVilaApproval;
})();
