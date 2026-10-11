// Dựng "Lý thuyết đồ thị — Tập 3: Hướng dẫn giải" thành file .docx
const fs = require('fs'), path = require('path');
const F = require('./fmt');
const { D, C, W, ARIAL, MONO, runs, P, bullets, numbered, cell, table, dataTable, box, gap, figure, codeBlock, sp, allB } = F;
const { Document, Packer, Paragraph, TextRun, TableRow, AlignmentType, Header, Footer, PageNumber, TabStopType, LevelFormat, BorderStyle, VerticalAlign, HeadingLevel } = D;
const ROOT = path.join(__dirname, '..');
const BOOK = 'Lý thuyết đồ thị · Tập 3: Hướng dẫn giải';
const PAGES = fs.existsSync(path.join(__dirname, 'pages.json')) ? JSON.parse(fs.readFileSync(path.join(__dirname, 'pages.json'))) : {};
const P2 = JSON.parse(fs.readFileSync(path.join(ROOT, '..', 'tap2', 'build', 'pages.json')));
const SCORES = JSON.parse(fs.readFileSync(path.join(ROOT, 'judge', 'scores.json')));
const T2 = [1, 2, 3, 4, 5].map((i) => require(path.join(ROOT, '..', 'tap2', 'content', `ch${i}.js`)));
const PROB = {}; T2.forEach((ch) => ch.lessons.forEach((L) => L.problems.forEach((p) => { PROB[p.id] = { ...p, lesson: L.no, chapter: ch.no }; })));
const CH = [1, 2, 3, 4, 5].filter((i) => fs.existsSync(path.join(ROOT, 'content', `ch${i}.js`))).map((i) => require(path.join(ROOT, 'content', `ch${i}.js`)));
const FRONT = require(path.join(ROOT, 'content', 'front.js'));
const LEVEL = { 1: ['★', 'CƠ BẢN', C.green], 2: ['★★', 'TRUNG BÌNH', C.amber], 3: ['★★★', 'NÂNG CAO', '7A1F1F'] };

// {{S:tên}} → tổng điểm thật của chương trình "tên"; {{P:tên:k}} → điểm subtask k
function score(name) {
  const code = name.split('_')[0];
  const r = SCORES[code] && SCORES[code][name];
  if (!r) throw new Error('chưa chấm: ' + name);
  return r;
}
function subst(t) {
  return t.replace(/\{\{S:([A-Z0-9_a-z]+)\}\}/g, (_, n) => String(score(n).total))
    .replace(/\{\{P:([A-Z0-9_a-z]+):(\d)\}\}/g, (_, n, k) => String(score(n).points[k - 1]));
}
function deep(x) { if (typeof x === 'string') return subst(x); if (Array.isArray(x)) return x.map(deep); if (x && typeof x === 'object' && !x.raw) { const o = {}; for (const k in x) o[k] = deep(x[k]); return o; } return x; }

let FIG = { id: '', n: 0 };
function blocks(list) {
  const out = [];
  for (const b0 of list || []) {
    const b = deep(b0);
    if (typeof b === 'string') out.push(P(b));
    else if (b.ul) out.push(...bullets(b.ul));
    else if (b.ol) out.push(...numbered(b.ol, b));
    else if (b.fig) { FIG.n++; out.push(...figure(b.fig, b.w || 5, b.cap, `Hình ${FIG.id}.${FIG.n}.`)); }
    else if (b.box) out.push(...box(b.box, b.title, blocks(b.body), { cantSplit: b.cantSplit }));
    else if (b.table) out.push(dataTable(b.table.cols, b.table.head, b.table.rows, b.table), gap(140));
    else if (b.code) out.push(...codeBlock(b.title || '', b.code));
    else if (b.file) out.push(...codeBlock(b.title || '', fs.readFileSync(path.join(ROOT, 'code', b.file + '.cpp'), 'utf8')));
    else if (b.sub) out.push(subhead(b.sub));
    else if (b.cx) out.push(P('**Độ phức tạp:** ' + b.cx));
    else throw new Error('khối lạ: ' + JSON.stringify(b));
  }
  return out;
}
function subhead(t, o = {}) { return new Paragraph({ children: runs(t, { bold: true, color: o.color || C.red, font: ARIAL, size: 21 }), spacing: sp(80, o.before ?? 160), keepNext: true }); }
function h3(t) {
  return new Paragraph({ children: [new TextRun({ text: t, font: ARIAL, bold: true, color: C.navy, size: 24 })], keepNext: true,
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, space: 2, color: 'B4C6E7' } }, spacing: { before: 240, after: 110 } });
}
function h1(t, o = {}) {
  return new Paragraph({ children: [new TextRun({ text: t, font: ARIAL, bold: true, color: C.navy, size: o.size || 30 })], heading: HeadingLevel.HEADING_1, alignment: AlignmentType.CENTER, spacing: { after: 240 }, pageBreakBefore: o.pb });
}

// ---------- một lời giải
function solution(s, first) {
  const p = PROB[s.id]; if (!p) throw new Error('không có bài ' + s.id);
  FIG = { id: s.id, n: 0 };
  const out = [new Paragraph({ children: [], pageBreakBefore: !first, spacing: { after: 0, line: 120, lineRule: 'exact' } })];
  out.push(table([W], [new TableRow({ cantSplit: true, children: [cell([new Paragraph({ children: [
    new TextRun({ text: `BÀI ${s.id}`, bold: true, color: 'FFD966', font: ARIAL, size: 26 }), new TextRun({ text: '   ' + p.name, bold: true, color: 'FFFFFF', font: ARIAL, size: 26 })],
    heading: HeadingLevel.HEADING_2 })], { w: W, fill: C.navy, borders: allB(C.navy, 4), mar: { top: 110, bottom: 110, left: 200, right: 160 } })] })]));
  out.push(gap(100));
  const [st, lv, lc] = LEVEL[p.level];
  const hc = (t) => new Paragraph({ children: [new TextRun({ text: t, bold: true, color: C.navy, font: ARIAL, size: 18 })], alignment: AlignmentType.CENTER });
  const vc = (ch) => new Paragraph({ children: ch, alignment: AlignmentType.CENTER });
  const cols = [2150, 2150, 1150, 1150, 2018];
  out.push(table(cols, [
    new TableRow({ children: ['Dữ liệu vào', 'Kết quả', 'Thời gian', 'Bộ nhớ', 'Mức độ'].map((t, i) => cell([hc(t)], { w: cols[i], fill: 'E8EEF7' })) }),
    new TableRow({ children: [
      cell([vc([new TextRun({ text: p.code + '.INP', font: MONO, size: 18 })])], { w: cols[0] }), cell([vc([new TextRun({ text: p.code + '.OUT', font: MONO, size: 18 })])], { w: cols[1] }),
      cell([vc([new TextRun({ text: p.time || '1 giây', size: 20 })])], { w: cols[2] }), cell([vc([new TextRun({ text: p.mem || '256 MB', size: 20 })])], { w: cols[3] }),
      cell([vc([new TextRun({ text: st + ' ', color: lc, size: 20 }), new TextRun({ text: lv, bold: true, color: lc, size: 18, font: ARIAL })])], { w: cols[4] })] }),
  ]));
  out.push(new Paragraph({ children: [new TextRun({ text: `Liên hệ: Tập 1, Bài ${p.lesson}${s.link ? ', ' + s.link : ''} · Đề bài: Tập 2, trang ${P2['P' + s.id] || '?'}`, italics: true, color: '595959', size: 20 })], spacing: sp(60, 100) }));
  out.push(h3('1. Hiểu bài toán'), ...blocks(s.understand));
  out.push(h3('2. ' + s.naive.title), ...blocks(s.naive.body));
  out.push(h3('3. ' + (s.stuckTitle || 'Bế tắc')), ...blocks(s.stuck));
  out.push(h3('4. ' + (s.breakTitle || 'Phá bế tắc')), ...blocks(s.breakthrough));
  out.push(h3('5. ' + (s.optTitle || 'Cách tối ưu')), ...blocks(s.optimal));
  out.push(h3('6. Bẫy thường gặp'), ...bullets(deep(s.traps)));
  out.push(h3('7. Bảng điểm theo thuật toán'));
  const sub = p.subtasks.map((x) => x[0]);
  const head = ['Thuật toán', ...sub.map((x, i) => `ST${i + 1} (${x})`), 'Tổng'];
  const wsub = Math.min(1100, Math.floor(4200 / (sub.length + 1)));
  const tc = [W - wsub * (sub.length + 1), ...sub.map(() => wsub), wsub];
  const rows = [], fills = [];
  s.approaches.forEach(([name, label]) => {
    const r = score(name);
    rows.push([label, ...r.points.map(String), `**${r.total}**`]);
    fills.push(name === p.code ? tc.map(() => 'EAF5E6') : tc.map(() => null));
  });
  if (!s.approaches.some(([n]) => n === p.code)) throw new Error('thiếu lời giải mẫu trong bảng điểm ' + s.id);
  out.push(dataTable(tc, head, rows, { size: 19, fills, aligns: [AlignmentType.LEFT, ...sub.map(() => AlignmentType.CENTER), AlignmentType.CENTER] }));
  out.push(new Paragraph({ children: [new TextRun({ text: `Chấm trên ${countTests(s.id)} test, giới hạn ${p.time || '1 giây'}, ${p.mem || '256 MB'}, ngăn xếp 8 MB. Dòng tô xanh là lời giải mẫu.`, italics: true, color: '7F7F7F', size: 17 })], spacing: sp(160, 60) }));
  return out;
}
function countTests(id) {
  const code = PROB[id].code; const r = SCORES[code][code];
  return r.verdicts.length;
}

function chapterStart(ch) {
  const out = [new Paragraph({ children: [new TextRun({ text: `CHƯƠNG ${ch.no}. `, color: C.red, font: ARIAL, bold: true, size: 40 }), new TextRun({ text: T2[ch.no - 1].title, color: C.navy, font: ARIAL, bold: true, size: 40 })],
    heading: HeadingLevel.HEADING_1, border: { bottom: { style: BorderStyle.SINGLE, size: 14, space: 6, color: C.red } }, spacing: { after: 160 } })];
  out.push(P(ch.intro, { run: { italics: true, color: '404040' }, after: 200 }));
  const rows = [], fills = [];
  ch.solutions.forEach((s) => {
    const p = PROB[s.id];
    const best = s.approaches.map(([n, l]) => [n, l, score(n).total]);
    const naive = best[0];
    rows.push([`**${s.id}**`, `**${p.name}**`, LEVEL[p.level][0], naive[1] + ` (${naive[2]})`, s.key]);
    fills.push([null, null, null, null, null]);
  });
  out.push(dataTable([700, 1900, 800, 2600, 2618], ['Bài', 'Tên bài', 'Mức', 'Cách ngây thơ (điểm)', 'Chìa khóa của lời giải'], rows, { size: 18, aligns: [AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.LEFT] }), gap(160));
  return out;
}

const pageProps = { page: { size: { width: 10772, height: 15024 }, margin: { top: 1134, right: 1077, bottom: 1134, left: 1077, header: 560, footer: 520 } } };
const hdr = (t) => ({ default: new Header({ children: [new Paragraph({ children: [new TextRun({ text: t, italics: true, color: '7F7F7F', size: 17 })], alignment: AlignmentType.RIGHT,
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, space: 4, color: 'BFBFBF' } } })] }) });
const ftr = () => ({ default: new Footer({ children: [new Paragraph({ children: [new TextRun({ children: [PageNumber.CURRENT], color: '7F7F7F', size: 18 })], alignment: AlignmentType.CENTER })] }) });

function build() {
  const ctx = { F, CH, T2, PROB, PAGES, LEVEL, blocks, subhead, h1, h3, SCORES, score, BOOK };
  const sections = [{ properties: { ...pageProps, titlePage: true }, headers: { ...hdr(BOOK), first: new Header({ children: [new Paragraph('')] }) },
    footers: { ...ftr(), first: new Footer({ children: [new Paragraph('')] }) }, children: FRONT.build(ctx) }];
  CH.forEach((ch) => {
    const kids = chapterStart(ch);
    ch.solutions.forEach((s, i) => kids.push(...solution(s, false)));
    sections.push({ properties: { ...pageProps }, headers: hdr(`${BOOK} · CHƯƠNG ${ch.no}. ${T2[ch.no - 1].title}`), footers: ftr(), children: kids });
  });
  if (FRONT.back) sections.push({ properties: { ...pageProps }, headers: hdr(`${BOOK} · PHỤ LỤC`), footers: ftr(), children: FRONT.back(ctx) });
  const doc = new Document({
    creator: 'Lê Thành Nam', title: 'Lý thuyết đồ thị — Tập 3: Hướng dẫn giải',
    styles: { default: { document: { run: { font: 'Times New Roman', size: 23, color: C.txt } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: ARIAL, bold: true, color: C.navy, size: 40 }, paragraph: { outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: ARIAL, bold: true, size: 26 }, paragraph: { outlineLevel: 1 } }] },
    numbering: { config: [{ reference: 'bul', levels: [
      { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 640, hanging: 300 } }, run: { color: C.navy, bold: true } } },
      { level: 1, format: LevelFormat.BULLET, text: '◦', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1100, hanging: 300 } } } }] }] },
    sections,
  });
  return Packer.toBuffer(doc);
}
module.exports = { build };
if (require.main === module) build().then((buf) => { const o = process.argv[2] || path.join(__dirname, 'out.docx'); fs.writeFileSync(o, buf); console.log('wrote', o); });
