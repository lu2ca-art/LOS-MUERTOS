(function () {
const STEPS = [
  { id: '01', name: 'Briefing do Dia', owner: 'Sistema' },
  { id: '02', name: 'Criar Conteúdo', owner: 'Cris Criativa' },
  { id: '03', name: 'Criar Visual', owner: 'Vito Visual' },
  { id: '04', name: 'Aprovação Humana ①', owner: '—', checkpoint: true },
  { id: '05', name: 'Publicar', owner: 'Paulo Postador' },
  { id: '06', name: 'Criar Campanha', owner: 'Ana Anúncio', condicional: true },
  { id: '07', name: 'Revisão de Qualidade', owner: 'Renata Revisão' },
  { id: '08', name: 'Relatório', owner: 'Rodrigo Resultados' },
  { id: '09', name: 'Aprovação Final ②', owner: '—', checkpoint: true },
];

const STEP_ORDER = STEPS.map((s) => s.id);

function stepAfter(stepId) {
  const idx = STEP_ORDER.indexOf(stepId);
  return STEP_ORDER[idx + 1] || null;
}

function stepBefore(stepId) {
  const idx = STEP_ORDER.indexOf(stepId);
  return STEP_ORDER[idx - 1] || null;
}

function createPipelineRun({ id, briefing, tipoCampanha = null } = {}) {
  const stepStatus = {};
  STEP_ORDER.forEach((s) => {
    stepStatus[s] = s === '01' ? 'done' : 'pending';
  });
  return {
    id: id || `run-${Date.now()}`,
    tipoCampanha,
    briefing: briefing || null,
    content: null,
    visual: null,
    campaign: null,
    qaReport: null,
    metrics: null,
    currentStep: '02',
    stepStatus,
    approvals: { '04': null, '09': null },
    history: [],
  };
}

function logHistory(run, entry) {
  run.history.push({ at: new Date().toISOString(), ...entry });
}

function advanceTo(run, stepId) {
  run.currentStep = stepId;
  run.stepStatus[stepId] = 'in_progress';
}

function completeStep(run, stepId, output) {
  run.stepStatus[stepId] = 'done';
  if (output) Object.assign(run, output);
  const next = stepAfter(stepId);
  if (next) advanceTo(run, next);
  logHistory(run, { step: stepId, action: 'completed' });
  return run;
}

function approveCheckpoint(run, checkpointId, { approver, editedContent, note } = {}) {
  if (!STEPS.find((s) => s.id === checkpointId && s.checkpoint)) {
    throw new Error(`Etapa ${checkpointId} não é um checkpoint de aprovação.`);
  }
  if (editedContent && checkpointId === '04') {
    run.content = { ...run.content, ...editedContent, editedByHuman: true };
  }
  run.approvals[checkpointId] = {
    decision: 'approved',
    approver: approver || 'desconhecido',
    at: new Date().toISOString(),
    note: note || null,
  };
  run.stepStatus[checkpointId] = 'done';
  logHistory(run, { step: checkpointId, action: 'approved', approver, note });
  const next = stepAfter(checkpointId);
  if (checkpointId === '04' && next === '05' && run.tipoCampanha == null && !run.campaignRequested) {
    run.stepStatus['06'] = 'skipped';
  }
  if (next) advanceTo(run, next);
  return run;
}

function rejectCheckpoint(run, checkpointId, { approver, justification }) {
  if (!justification || !justification.trim()) {
    throw new Error('Reprovação exige justificativa.');
  }
  if (!STEPS.find((s) => s.id === checkpointId && s.checkpoint)) {
    throw new Error(`Etapa ${checkpointId} não é um checkpoint de aprovação.`);
  }
  run.approvals[checkpointId] = {
    decision: 'rejected',
    approver: approver || 'desconhecido',
    at: new Date().toISOString(),
    justification,
  };
  run.stepStatus[checkpointId] = 'rejected';
  logHistory(run, { step: checkpointId, action: 'rejected', approver, justification });

  const backTo = checkpointId === '04' ? '02' : '07';
  run.stepStatus[backTo] = 'pending';
  advanceTo(run, backTo);
  return run;
}

function isCopaFlag(briefing) {
  return Boolean(briefing && briefing.tipo_campanha === 'copa');
}

const pipelineStateMachineExports = {
  STEPS,
  STEP_ORDER,
  stepAfter,
  stepBefore,
  createPipelineRun,
  completeStep,
  approveCheckpoint,
  rejectCheckpoint,
  isCopaFlag,
};

if (typeof module !== 'undefined' && module.exports) module.exports = pipelineStateMachineExports;
if (typeof window !== 'undefined') window.pipelineStateMachine = pipelineStateMachineExports;
})();
