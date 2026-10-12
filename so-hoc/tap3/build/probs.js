// In ra thông tin các bài tập của Tập 2 (mã, subtask, thời gian, bộ nhớ) cho bộ chấm
const path = require('path');
const out = {};
for (const i of [1, 2, 3, 4, 5]) for (const L of require(path.join(__dirname, '..', '..', 'tap2', 'content', `ch${i}.js`)).lessons)
  for (const p of L.problems) out[p.code] = { id: p.id, name: p.name, subtasks: p.subtasks.map((s) => s[0]), sublim: p.subtasks.map((s) => s[1]), limits: p.limits, tl: parseFloat(p.time || '1'), mem: parseInt(p.mem || '256'), level: p.level };
console.log(JSON.stringify(out));
