// Dựng "Số học — Tập 1: Lý thuyết" thành file .docx (cùng phong cách bộ Lý thuyết đồ thị)
const fs = require('fs'), path = require('path');
const F = require('./fmt');
const { D, C, W, ARIAL, MONO, runs, P, bullets, numbered, cell, table, dataTable, box, gap, figure, codeBlock, sp, allB, none } = F;
const { Document, Packer, Paragraph, TextRun, TableRow, AlignmentType, Header, Footer, PageNumber, LevelFormat, BorderStyle, HeadingLevel } = D;
const ROOT = path.join(__dirname, '..');
const BOOK = 'Số học · Tập 1: Lý thuyết';
const PAGES = fs.existsSync(path.join(__dirname, 'pages.json')) ? JSON.parse(fs.readFileSync(path.join(__dirname, 'pages.json'))) : {};
const ONLY = process.env.CHAPTERS ? process.env.CHAPTERS.split(',').map(Number) : [1, 2, 3, 4, 5];
const CH = ONLY.filter((i) => fs.existsSync(path.join(ROOT, 'content', `ch${i}.js`))).map((i) => require(path.join(ROOT, 'content', `ch${i}.js`)));
const FRONT = require(path.join(ROOT, 'content', 'front.js'));

// các loại khung: [kiểu màu trong fmt.BOX, tiêu đề mặc định]
const KIND = {
  warmup: ['note', 'KHỞI ĐỘNG'], def: ['def', 'ĐỊNH NGHĨA'], theorem: ['theorem', 'ĐỊNH LÍ'], algo: ['recap', 'THUẬT TOÁN'],
  count: ['hint', 'ĐẾM SỐ PHÉP TÍNH'], stuck: ['warn', 'BẾ TẮC'], why: ['theorem', 'VÌ SAO ĐÚNG?'], model: ['model', 'MÔ HÌNH HÓA'],
  imagine: ['model', 'HÃY HÌNH DUNG'], trap: ['warn', 'BẪY THƯỜNG GẶP'], remember: ['remember', 'GHI NHỚ'], note: ['note', 'LƯU Ý'],
  example: ['hint', 'VÍ DỤ'], hint: ['hint', 'GỢI Ý'],
};

let CUR = { lesson: 0, fig: 0, h: 0, step: 0 };
function formula(t) {
  return new Paragraph({ children: runs(t, { bold: true, size: 24 }), alignment: AlignmentType.CENTER, spacing: sp(120, 80) });
}
function subhead(t, o = {}) { return new Paragraph({ children: runs(t, { bold: true, color: o.color || C.red, font: ARIAL, size: 21 }), spacing: sp(80, o.before ?? 160), keepNext: true }); }
function h3(t) {
  return new Paragraph({ children: runs(t, { font: ARIAL, bold: true, color: C.navy, size: 26 }), keepNext: true,
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, space: 2, color: 'B4C6E7' } }, spacing: { before: 280, after: 120 } });
}
function h1(t, o = {}) {
  return new Paragraph({ children: [new TextRun({ text: t, font: ARIAL, bold: true, color: C.navy, size: o.size || 30 })], heading: HeadingLevel.HEADING_1, alignment: AlignmentType.CENTER, spacing: { after: 240 }, pageBreakBefore: o.pb });
}
// "Bước k" trên nền đỏ, giống Tập 1 của bộ đồ thị
function step(t) {
  CUR.step++;
  return new Paragraph({ children: [new TextRun({ text: ` Bước ${CUR.step} `, bold: true, color: 'FFFFFF', font: ARIAL, size: 19, shading: { type: 'clear', fill: C.red, color: 'auto' } }),
    new TextRun({ text: '  ' }), ...runs(t, { bold: true, color: C.red, font: ARIAL, size: 21 })], spacing: sp(80, 180), keepNext: true });
}
// khung BÀI TOÁN: viền mảnh quanh, viền trái đậm xanh, nền trắng
function problemBox(p) {
  const kids = [new Paragraph({ children: [new TextRun({ text: 'BÀI TOÁN: ' + p.code, bold: true, color: C.navy, font: ARIAL, size: 19 })], spacing: sp(60), keepNext: true })];
  kids.push(...blocks(p.statement));
  if (p.input) kids.push(P('**Dữ liệu vào:** ' + p.input));
  if (p.output) kids.push(P('**Kết quả:** ' + p.output));
  if (p.limits) kids.push(P('**Giới hạn:** ' + p.limits));
  return [table([W], [new TableRow({ cantSplit: true, children: [cell(kids, { w: W, mar: { top: 100, bottom: 80, left: 180, right: 160 },
    borders: { top: F.line('1F3864', 6), bottom: F.line('1F3864', 6), right: F.line('1F3864', 6), left: { style: BorderStyle.SINGLE, size: 24, color: C.navy } } })] })]), gap()];
}
// bảng ví dụ: CODE.INP | CODE.OUT | Giải thích; output sinh bằng cách chạy lời giải mẫu (build/run_examples.py)
function examples(code, explain, o = {}) {
  const dir = path.join(ROOT, 'examples', code);
  const ins = fs.readdirSync(dir).filter((f) => f.endsWith('.inp')).sort((a, b) => parseInt(a) - parseInt(b));
  const rows = ins.map((f, i) => {
    const inp = fs.readFileSync(path.join(dir, f), 'utf8').replace(/\s+$/, '');
    const of = path.join(dir, f.replace('.inp', '.out'));
    if (!fs.existsSync(of)) throw new Error('chưa sinh output ví dụ: ' + of);
    const out = fs.readFileSync(of, 'utf8').replace(/\s+$/, '');
    return [inp.split('\n'), out.split('\n'), explain && explain[i] ? explain[i] : ''];
  });
  const mono = { font: MONO, size: 18 };
  const cols = o.cols || [2300, 1700, 4618];
  return [dataTable(cols, [code + '.INP', code + '.OUT', 'Giải thích'], rows.map((r) => [r[0], r[1], Array.isArray(r[2]) ? r[2] : [r[2]]]),
    { size: 20, colRun: [mono, mono, {}] }), gap(140)];
}

function blocks(list) {
  const out = [];
  for (const b of list || []) {
    if (typeof b === 'string') out.push(P(b));
    else if (b.h) { CUR.h++; CUR.step = 0; out.push(h3(`${CUR.h}. ${b.h}`)); }
    else if (b.step) out.push(step(b.step));
    else if (b.ul) out.push(...bullets(b.ul, b));
    else if (b.ol) out.push(...numbered(b.ol, b));
    else if (b.fig) { CUR.fig++; out.push(...figure(b.fig, b.w || 5, b.cap, `Hình ${CUR.lesson}.${CUR.fig}.`)); }
    else if (b.box) { const [k, t] = KIND[b.box] || [b.box, '']; out.push(...box(k, b.title || t, blocks(b.body), { cantSplit: b.cantSplit })); }
    else if (b.table) out.push(dataTable(b.table.cols, b.table.head, b.table.rows, b.table), gap(140));
    else if (b.code) out.push(...codeBlock(b.title || '', b.code));
    else if (b.file) out.push(...codeBlock(b.title || (b.file + '.CPP'), fs.readFileSync(path.join(ROOT, 'code', b.file + '.cpp'), 'utf8')));
    else if (b.problem) out.push(...problemBox(b.problem));
    else if (b.examples) out.push(...examples(b.examples, b.explain, b));
    else if (b.formula) out.push(formula(b.formula));
    else if (b.sub) out.push(subhead(b.sub));
    else if (b.cx) out.push(P('**Độ phức tạp:** ' + b.cx));
    else throw new Error('khối lạ: ' + JSON.stringify(b).slice(0, 200));
  }
  return out;
}

// ---------- một bài học
function lesson(L) {
  CUR = { lesson: L.no, fig: 0, h: 0, step: 0 };
  const out = [new Paragraph({ children: [], pageBreakBefore: true, spacing: { after: 0, line: 120, lineRule: 'exact' } })];
  out.push(table([W], [new TableRow({ cantSplit: true, children: [cell([new Paragraph({ children: [
    new TextRun({ text: `BÀI ${L.no}`, bold: true, color: 'FFD966', font: ARIAL, size: 28 }), new TextRun({ text: '   ' + L.title, bold: true, color: 'FFFFFF', font: ARIAL, size: 28 })],
    heading: HeadingLevel.HEADING_2 })], { w: W, fill: C.navy, borders: allB(C.navy, 4), mar: { top: 120, bottom: 120, left: 200, right: 160 } })] })]));
  out.push(gap(160));
  out.push(new Paragraph({ children: [new TextRun({ text: 'Học xong bài này, em sẽ:', bold: true, italics: true, color: C.navy, size: 23 })], spacing: sp(60, 60), keepNext: true }));
  L.goals.forEach((g) => out.push(new Paragraph({ children: [new TextRun({ text: '✓  ', bold: true, color: C.green, size: 24 }), ...runs(g)],
    indent: { left: 360, hanging: 360 }, spacing: sp(40), alignment: AlignmentType.LEFT })));
  out.push(gap(120));
  out.push(...box('note', 'KHỞI ĐỘNG', blocks(L.warmup)));
  out.push(...blocks(L.body));
  if (L.ext && L.ext.length) { out.push(...blocks([{ h: 'Mở rộng' }]), ...blocks(L.ext)); }
  out.push(...box('warn', 'BẪY THƯỜNG GẶP', bullets(L.traps), { cantSplit: false }));
  out.push(...box('remember', 'GHI NHỚ', bullets(L.remember), { cantSplit: false }));
  if (L.practice && L.practice.length) {
    out.push(subhead('Luyện tập', { color: C.navy, before: 200 }));
    out.push(dataTable([800, 2500, 5318], ['Bài', 'Tên', 'Gợi ý liên hệ'], L.practice.map((r) => [`**${r[0]}**`, `**${r[1]}**`, r[2]]),
      { size: 20, aligns: [AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.LEFT] }), gap(140));
  }
  if (L.quiz && L.quiz.length) {
    out.push(subhead('Tự kiểm tra nhanh', { color: C.navy, before: 160 }));
    out.push(...numbered(L.quiz.map(([q, a]) => `${q} *(${a})*`)));
  }
  return out;
}

function chapterStart(ch) {
  const out = [new Paragraph({ children: [new TextRun({ text: `CHƯƠNG ${ch.no}. `, color: C.red, font: ARIAL, bold: true, size: 40 }), new TextRun({ text: ch.title, color: C.navy, font: ARIAL, bold: true, size: 40 })],
    heading: HeadingLevel.HEADING_1, border: { bottom: { style: BorderStyle.SINGLE, size: 14, space: 6, color: C.red } }, spacing: { after: 200 } })];
  out.push(...blocks(ch.intro));
  if (ch.fig) out.push(...figure(ch.fig, ch.figW || 5.6, null));
  out.push(gap(100));
  out.push(...box('recap', 'TRONG CHƯƠNG NÀY', ch.lessons.map((L) => P(`**Bài ${L.no}.** ${L.title}${L.sub ? ': ' + L.sub : ''}`, { after: 50 }))));
  return out;
}

const pageProps = { page: { size: { width: 10772, height: 15024 }, margin: { top: 1134, right: 1077, bottom: 1134, left: 1077, header: 560, footer: 520 } } };
const hdr = (t) => ({ default: new Header({ children: [new Paragraph({ children: [new TextRun({ text: t, italics: true, color: '7F7F7F', size: 17 })], alignment: AlignmentType.RIGHT,
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, space: 4, color: 'BFBFBF' } } })] }) });
const ftr = () => ({ default: new Footer({ children: [new Paragraph({ children: [new TextRun({ children: [PageNumber.CURRENT], color: '7F7F7F', size: 18 })], alignment: AlignmentType.CENTER })] }) });

function build() {
  const ctx = { F, CH, PAGES, blocks, subhead, h1, h3, BOOK };
  const sections = [{ properties: { ...pageProps, titlePage: true }, headers: { ...hdr(BOOK), first: new Header({ children: [new Paragraph('')] }) },
    footers: { ...ftr(), first: new Footer({ children: [new Paragraph('')] }) }, children: FRONT.build(ctx) }];
  CH.forEach((ch) => {
    const kids = chapterStart(ch);
    ch.lessons.forEach((L) => kids.push(...lesson(L)));
    sections.push({ properties: { ...pageProps }, headers: hdr(`${BOOK} · CHƯƠNG ${ch.no}. ${ch.title}`), footers: ftr(), children: kids });
  });
  if (FRONT.back) sections.push({ properties: { ...pageProps }, headers: hdr(`${BOOK} · PHỤ LỤC`), footers: ftr(), children: FRONT.back(ctx) });
  const doc = new Document({
    creator: 'Lê Thành Nam', title: 'Số học — Tập 1: Lý thuyết',
    styles: { default: { document: { run: { font: 'Times New Roman', size: 23, color: C.txt } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: ARIAL, bold: true, color: C.navy, size: 40 }, paragraph: { outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: ARIAL, bold: true, size: 28 }, paragraph: { outlineLevel: 1 } }] },
    numbering: { config: [{ reference: 'bul', levels: [
      { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 640, hanging: 300 } }, run: { color: C.navy, bold: true } } },
      { level: 1, format: LevelFormat.BULLET, text: '◦', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1100, hanging: 300 } } } }] }] },
    sections,
  });
  return Packer.toBuffer(doc);
}
module.exports = { build };
if (require.main === module) build().then((buf) => { const o = process.argv[2] || path.join(__dirname, 'out.docx'); fs.writeFileSync(o, buf); console.log('wrote', o); });
