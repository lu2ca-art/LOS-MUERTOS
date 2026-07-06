(function () {
const mockRunCheckpoint04 = {
  id: 'run-2026-07-06',
  currentStep: '04',
  tipoCampanha: null,
  briefing: {
    data: '2026-07-06',
    pilar: 'Post Principal',
    tipo: 'post',
  },
  content: {
    legenda:
      'Segunda de chef vazio na cozinha não existe. Hoje o Alex tá testando uma versão nova do taco de costela desfiada, e quem passar aqui à noite prova antes de entrar no cardápio oficial. Vem sentar com a gente.',
    tipo: 'post',
  },
  visual: {
    thumbnailUrl: null,
    canvaDesignId: 'DAG-mock-001',
  },
  approvals: { '04': null, '09': null },
  stepStatus: {
    '01': 'done',
    '02': 'done',
    '03': 'done',
    '04': 'in_progress',
    '05': 'pending',
    '06': 'pending',
    '07': 'pending',
    '08': 'pending',
    '09': 'pending',
  },
  history: [
    { at: '2026-07-06T10:02:00-03:00', step: '01', action: 'completed' },
    { at: '2026-07-06T10:15:00-03:00', step: '02', action: 'completed' },
    { at: '2026-07-06T10:41:00-03:00', step: '03', action: 'completed' },
  ],
};

const mockRunCheckpoint09 = {
  id: 'run-2026-07-05',
  currentStep: '09',
  tipoCampanha: null,
  briefing: {
    data: '2026-07-05',
    pilar: 'Story Diário',
    tipo: 'show',
  },
  content: {
    legenda: 'Hoje tem Trio Fronteira no palco às 21h, sábado de resenha completa.',
    tipo: 'show',
    artista: 'Trio Fronteira',
    horario: '21h',
    dia: 'sábado',
  },
  qaReport: {
    aprovado: true,
    observacoes: 'Sem ocorrências. CTA físico, dados do show completos.',
  },
  metrics: {
    alcance: 4820,
    curtidas: 312,
    comentarios: 18,
    compartilhamentos: 9,
  },
  approvals: { '04': { decision: 'approved', approver: 'Luca', at: '2026-07-05T09:30:00-03:00', note: null }, '09': null },
  stepStatus: {
    '01': 'done',
    '02': 'done',
    '03': 'done',
    '04': 'done',
    '05': 'done',
    '06': 'skipped',
    '07': 'done',
    '08': 'done',
    '09': 'in_progress',
  },
  history: [
    { at: '2026-07-05T09:30:00-03:00', step: '04', action: 'approved', approver: 'Luca' },
    { at: '2026-07-05T10:00:00-03:00', step: '05', action: 'completed' },
    { at: '2026-07-05T20:15:00-03:00', step: '07', action: 'completed' },
    { at: '2026-07-05T20:20:00-03:00', step: '08', action: 'completed' },
  ],
};

const mockDataExports = { mockRunCheckpoint04, mockRunCheckpoint09 };

if (typeof module !== 'undefined' && module.exports) module.exports = mockDataExports;
if (typeof window !== 'undefined') window.mockData = mockDataExports;
})();
