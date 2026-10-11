// Dựng "Lý thuyết đồ thị — Tập 2: Bài tập" thành file .docx
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
const F = require('./fmt');
const { D, C, W, ARIAL, MONO, runs, P, bullets, numbered, cell, table, dataTable, box, gap, figure, codeBlock, sp, none, line, allB } = F;
const { Document, Packer, Paragraph, TextRun, TableRow, AlignmentType, Header, Footer, PageNumber, TabStopType, LevelFormat,
  BorderStyle, VerticalAlign, PageBreak, HeadingLevel } = D;
const ROOT = path.join(__dirname, '..');
const BOOK = 'Lý thuyết đồ thị · Tập 2: Bài tập';
const PAGES = fs.existsSync(path.join(__dirname, 'pages.json')) ? JSON.parse(fs.readFileSync(path.join(__dirname, 'pages.json'))) : {};
const CH = [1, 2, 3, 4, 5].filter((i) => fs.existsSync(path.join(ROOT, 'content', `ch${i}.js`))).map((i) => require(path.join(ROOT, 'content', `ch${i}.js`)));
const FRONT = require(path.join(ROOT, 'content', 'front.js'));
const LEVEL = { 1: ['★☆☆  CƠ BẢN', C.green, 'EAF5E6'], 2: ['★★☆  TRUNG BÌNH', C.amber, 'FFF6DB'], 3: ['★★★  NÂNG CAO', '7A1F1F', 'FBEAEA'] };

// ---------- chạy lời giải để lấy output ví dụ (đảm bảo ví dụ luôn khớp lời giải)
function exampleIO(code) {
  const dir = path.join(ROOT, 'examples', code); const res = [];
  for (let k = 1; fs.existsSync(path.join(dir, `${k}.inp`)); k++) {
    const inp = fs.readFileSync(path.join(dir, `${k}.inp`), 'utf8');
    const out = execFileSync(path.join(ROOT, 'sol', code), { input: inp, cwd: dir }).toString();
    fs.writeFileSync(path.join(dir, `${k}.out`), out);
    res.push([inp.replace(/\n+$/, ''), out.replace(/\n+$/, '')]);
  }
  return res;
}

// ---------- các khối nội dung
let FIG = { lesson: 0, n: 0 };
function blocks(list) {
  const out = [];
  for (const b of list || []) {
    if (typeof b === 'string') out.push(P(b));
    else if (b.ul) out.push(...bullets(b.ul));
    else if (b.ol) out.push(...numbered(b.ol, b));
    else if (b.fig) { FIG.n++; out.push(...figure(b.fig, b.w || 5, b.cap, `Hình ${FIG.lesson}.${FIG.n}.`)); }
    else if (b.box) out.push(...box(b.box, b.title, blocks(b.body), b));
    else if (b.table) out.push(dataTable(b.table.cols, b.table.head, b.table.rows, b.table), gap(140));
    else if (b.code) out.push(...codeBlock(b.title || '', b.code));
    else if (b.sub) out.push(subhead(b.sub));
    else if (b.center) out.push(P(b.center, { align: AlignmentType.CENTER }));
    else if (b.raw) out.push(...b.raw);
    else throw new Error('khối lạ: ' + JSON.stringify(b));
  }
  return out;
}
function subhead(t, o = {}) {
  return new Paragraph({ children: runs(t, { bold: true, color: o.color || C.red, font: ARIAL, size: 21 }), spacing: sp(80, o.before ?? 200), keepNext: true });
}
function h3(t) {
  return new Paragraph({ children: [new TextRun({ text: t, font: ARIAL, bold: true, color: C.navy, size: 26 })], heading: HeadingLevel.HEADING_3, keepNext: true,
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, space: 2, color: 'B4C6E7' } }, spacing: { before: 260, after: 120 } });
}
function h1(t, o = {}) {
  return new Paragraph({ children: [new TextRun({ text: t, font: ARIAL, bold: true, color: C.navy, size: o.size || 30 })], heading: HeadingLevel.HEADING_1,
    alignment: AlignmentType.CENTER, spacing: { after: 240 }, pageBreakBefore: o.pb });
}

// ---------- một bài tập
function problem(p, first) {
  const out = [];
  const [lv, lc, lf] = LEVEL[p.level];
  const ban = new TableRow({ cantSplit: true, children: [
    cell([new Paragraph({ children: [new TextRun({ text: `BÀI ${p.id}`, bold: true, color: 'FFFFFF', font: ARIAL, size: 24 })], alignment: AlignmentType.CENTER })],
      { w: 1500, fill: C.navy, borders: allB(C.navy, 4), mar: { top: 110, bottom: 110, left: 80, right: 80 } }),
    cell([new Paragraph({ children: [new TextRun({ text: p.name, bold: true, color: C.navy, font: ARIAL, size: 28 })] })],
      { w: 4918, fill: 'EEF3FA', borders: allB(C.navy, 4), mar: { top: 110, bottom: 110, left: 200, right: 100 } }),
    cell([new Paragraph({ children: [new TextRun({ text: lv, bold: true, color: lc, font: ARIAL, size: 18 })], alignment: AlignmentType.CENTER })],
      { w: 2200, fill: lf, borders: allB(C.navy, 4), mar: { top: 110, bottom: 110, left: 60, right: 60 } }),
  ] });
  out.push(new Paragraph({ children: [], pageBreakBefore: !first, spacing: { after: 0, line: 120, lineRule: 'exact' } }));
  out.push(table([1500, 4918, 2200], [ban]));
  const inf = (lab, val, w) => cell([new Paragraph({ children: [new TextRun({ text: lab, color: C.gray, font: ARIAL, size: 15 })], alignment: AlignmentType.CENTER, spacing: { after: 10 } }),
    new Paragraph({ children: [new TextRun({ text: val, bold: true, color: C.txt, font: val.includes('.') && !val.includes(' ') ? MONO : ARIAL, size: 18 })], alignment: AlignmentType.CENTER })],
    { w, fill: 'F7F7F7', borders: allB('D0D0D0', 4), mar: { top: 50, bottom: 50, left: 60, right: 60 } });
  out.push(table([2154, 2154, 2154, 2156], [new TableRow({ cantSplit: true, children: [
    inf('Chương trình', `${p.code}.CPP`, 2154), inf('Dữ liệu vào', `${p.code}.INP`, 2154), inf('Kết quả', `${p.code}.OUT`, 2154),
    inf('Giới hạn', `${p.time || '1 giây'} · ${p.mem || '256 MB'}`, 2156)] })]));
  out.push(new Paragraph({ children: [new TextRun({ text: 'Kiến thức: ', bold: true, italics: true, color: C.teal, size: 19 }), ...runs(p.topic, { italics: true, color: '404040', size: 19 })],
    spacing: sp(140, 100) }));
  out.push(...blocks(p.statement));
  out.push(subhead('Dữ liệu vào'), ...blocks(p.input));
  out.push(subhead('Kết quả'), ...blocks(p.output));
  out.push(subhead('Ràng buộc'));
  if (p.limits) out.push(...blocks(p.limits));
  if (p.subtasks) {
    const tot = p.subtasks.reduce((a, s) => a + s[0], 0);
    if (tot !== 100) throw new Error(`${p.code}: tổng điểm ${tot}`);
    out.push(dataTable([1250, 1000, 6368], ['Subtask', 'Điểm', 'Ràng buộc thêm'],
      p.subtasks.map((s, i) => [String(i + 1), `${s[0]}%`, s[1]]), { aligns: [AlignmentType.CENTER, AlignmentType.CENTER, AlignmentType.LEFT], size: 20 }), gap(100));
  }
  // ví dụ
  const io = exampleIO(p.code);
  out.push(subhead(io.length > 1 ? 'Ví dụ' : 'Ví dụ'));
  io.forEach(([inp, outp], k) => {
    const ex = (p.examples || [])[k] || {};
    const cols = ex.cols || p.exCols || [2300, 1900, 4418];
    const mono = (s) => s.split('\n').map((l) => new Paragraph({ children: [new TextRun({ text: l === '' ? ' ' : l, font: MONO, size: 19 })], spacing: { after: 0, line: 240, lineRule: 'auto' } }));
    const hd = (t) => new Paragraph({ children: [new TextRun({ text: t, bold: true, color: C.navy, font: ARIAL, size: 18 })], alignment: AlignmentType.CENTER, keepNext: true });
    const mar = { top: 70, bottom: 70, left: 120, right: 100 };
    const head = [cell([hd(`${p.code}.INP`)], { w: cols[0], fill: 'E8EEF7' }), cell([hd(`${p.code}.OUT`)], { w: cols[1], fill: 'E8EEF7' })];
    const body = [cell(mono(inp), { w: cols[0], fill: 'FBFBFB', valign: VerticalAlign.TOP, mar }), cell(mono(outp), { w: cols[1], fill: 'FBFBFB', valign: VerticalAlign.TOP, mar })];
    if (cols.length === 3) {
      head.push(cell([hd('Giải thích')], { w: cols[2], fill: 'E8EEF7' }));
      body.push(cell((ex.explain ? (Array.isArray(ex.explain) ? ex.explain : [ex.explain]) : ['']).map((t) => P(t, { run: { size: 20 }, after: 60, align: AlignmentType.LEFT })),
        { w: cols[2], valign: VerticalAlign.TOP, mar }));
    }
    out.push(table(cols, [new TableRow({ tableHeader: true, cantSplit: true, children: head }), new TableRow({ cantSplit: (inp.split('\n').length < 30), children: body })]));
    out.push(gap(120));
    if (ex.after) out.push(...blocks(ex.after));
  });
  if (p.after) out.push(...blocks(p.after));
  if (p.notes) out.push(...box('note', 'CHÚ Ý', blocks(p.notes), { cantSplit: false }));
  if (p.hints) out.push(...box('hint', 'HƯỚNG SUY NGHĨ', bullets(p.hints), { cantSplit: false }));
  return out;
}

// ---------- tiêu đề chương, bài học
function lessonBanner(L) {
  return [table([W], [new TableRow({ cantSplit: true, children: [cell([new Paragraph({ children: [
    new TextRun({ text: `BÀI ${L.no}`, bold: true, color: 'FFD966', font: ARIAL, size: 28 }), new TextRun({ text: '   ' + L.title, bold: true, color: 'FFFFFF', font: ARIAL, size: 28 })],
    heading: HeadingLevel.HEADING_2 })], { w: W, fill: C.navy, borders: allB(C.navy, 4), mar: { top: 120, bottom: 120, left: 200, right: 160 } })] })]), gap(160)];
}
function lesson(L, chap) {
  FIG = { lesson: L.no, n: 0 };
  const out = [new Paragraph({ children: [], pageBreakBefore: true, spacing: { after: 0, line: 120, lineRule: 'exact' } }), ...lessonBanner(L)];
  out.push(...box('recap', `ÔN NHANH KIẾN THỨC · Tập 1, Bài ${L.no}`, bullets(L.recap)));
  out.push(new Paragraph({ children: [new TextRun({ text: 'Ba bài tập của bài học này', bold: true, italics: true, color: C.navy })], spacing: sp(80, 60), keepNext: true }));
  out.push(dataTable([800, 2600, 2100, 3118], ['Bài', 'Tên bài', 'Mức độ', 'Kĩ năng rèn luyện'],
    L.problems.map((p) => [`**${p.id}**`, `**${p.name}**`, LEVEL[p.level][0], p.skill]),
    { aligns: [AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.CENTER, AlignmentType.LEFT], size: 20,
      fills: L.problems.map((p) => [null, null, LEVEL[p.level][2], null]) }), gap(200));
  L.problems.forEach((p, i) => out.push(...problem(p, i === 0)));
  return out;
}
function chapterStart(ch) {
  const out = [];
  out.push(new Paragraph({ children: [new TextRun({ text: `CHƯƠNG ${ch.no}. `, color: C.red, font: ARIAL, bold: true, size: 40 }), new TextRun({ text: ch.title, color: C.navy, font: ARIAL, bold: true, size: 40 })],
    heading: HeadingLevel.HEADING_1, border: { bottom: { style: BorderStyle.SINGLE, size: 14, space: 6, color: C.red } }, spacing: { after: 160 } }));
  out.push(P(ch.intro, { run: { italics: true, color: '404040' }, after: 200 }));
  const kids = [];
  ch.lessons.forEach((L) => {
    kids.push(new Paragraph({ children: [new TextRun({ text: `Bài ${L.no}. `, bold: true, size: 22 }), new TextRun({ text: L.title, size: 22 })], spacing: sp(30, 60) }));
    L.problems.forEach((p) => kids.push(new Paragraph({ children: [new TextRun({ text: `${p.id}  `, bold: true, color: C.navy, size: 20, font: ARIAL }),
      new TextRun({ text: p.name, size: 20, bold: true }), new TextRun({ text: '\t' + LEVEL[p.level][0], size: 16, color: LEVEL[p.level][1], font: ARIAL, bold: true })],
      tabStops: [{ type: TabStopType.RIGHT, position: W - 400 }], indent: { left: 500 }, spacing: sp(20) })));
  });
  out.push(...box('recap', 'TRONG CHƯƠNG NÀY', kids));
  if (ch.figure) out.push(...figure(ch.figure.name, ch.figure.w, null));
  if (ch.advice) out.push(...box('remember', 'LỜI KHUYÊN CHO CHƯƠNG NÀY', bullets(ch.advice)));
  return out;
}

// ---------- tài liệu
const pageProps = { page: { size: { width: 10772, height: 15024 }, margin: { top: 1134, right: 1077, bottom: 1134, left: 1077, header: 560, footer: 520 } } };
const hdr = (t) => ({ default: new Header({ children: [new Paragraph({ children: [new TextRun({ text: t, italics: true, color: '7F7F7F', size: 17 })], alignment: AlignmentType.RIGHT,
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, space: 4, color: 'BFBFBF' } } })] }) });
const ftr = () => ({ default: new Footer({ children: [new Paragraph({ children: [new TextRun({ children: [PageNumber.CURRENT], color: '7F7F7F', size: 18 })], alignment: AlignmentType.CENTER })] }) });

function build() {
  const ctx = { F, CH, PAGES, LEVEL, blocks, subhead, h1, h3, lessonBanner, problem, BOOK };
  const sections = [];
  sections.push({ properties: { ...pageProps, titlePage: true }, headers: { ...hdr(BOOK), first: new Header({ children: [new Paragraph('')] }) },
    footers: { ...ftr(), first: new Footer({ children: [new Paragraph('')] }) }, children: FRONT.build(ctx) });
  CH.forEach((ch) => {
    const kids = chapterStart(ch);
    ch.lessons.forEach((L) => kids.push(...lesson(L, ch)));
    sections.push({ properties: { ...pageProps }, headers: hdr(`${BOOK} · CHƯƠNG ${ch.no}. ${ch.title}`), footers: ftr(), children: kids });
  });
  if (FRONT.back) sections.push({ properties: { ...pageProps }, headers: hdr(`${BOOK} · PHỤ LỤC`), footers: ftr(), children: FRONT.back(ctx) });
  const doc = new Document({
    creator: 'Lê Thành Nam', title: 'Lý thuyết đồ thị — Tập 2: Bài tập', description: 'Tài liệu bồi dưỡng học sinh giỏi Tin học',
    styles: {
      default: { document: { run: { font: 'Times New Roman', size: 23, color: C.txt } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: ARIAL, bold: true, color: C.navy, size: 40 }, paragraph: { outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: ARIAL, bold: true, size: 28 }, paragraph: { outlineLevel: 1 } },
        { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: ARIAL, bold: true, color: C.navy, size: 26 }, paragraph: { outlineLevel: 2 } },
      ],
    },
    numbering: { config: [{ reference: 'bul', levels: [
      { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 640, hanging: 300 } }, run: { color: C.navy, bold: true } } },
      { level: 1, format: LevelFormat.BULLET, text: '–', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1100, hanging: 300 } } } }] }] },
    sections,
  });
  return Packer.toBuffer(doc);
}
module.exports = { build };
if (require.main === module) build().then((buf) => { const o = process.argv[2] || path.join(__dirname, 'out.docx'); fs.writeFileSync(o, buf); console.log('wrote', o); });
