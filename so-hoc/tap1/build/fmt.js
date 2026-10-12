// Các thành phần trình bày dùng chung — bám sát định dạng Tập 1
const fs = require('fs');
const path = require('path');
const D = require('docx');
const { Paragraph, TextRun, Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, AlignmentType,
  ImageRun, VerticalAlign, TabStopType, HeightRule } = D;

const C = { navy: '1F3864', red: 'C0504D', txt: '1A1A1A', gray: '595959', lgray: 'A0A0A0', code: '7A1F1F',
  orange: 'C55A11', green: '2E7D32', purple: '6A4C93', teal: '1B7F79', amber: 'B26A00', pink: 'A23B6B' };
const W = 8618; // bề rộng vùng chữ (DXA)
const ARIAL = 'Arial', MONO = 'Courier New';
const FIGDIR = path.join(__dirname, '..', 'figs', 'png');

// ---------- chữ có định dạng: **đậm**, *nghiêng*, `mã`, ^trên^, ~dưới~
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*([\s\S]+?)\*\*|\*([^*]+?)\*|`([^`]+?)`|\^([^^]+?)\^|~([^~]+?)~)/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    if (m[2] !== undefined) out.push(...runs(m[2], { ...base, bold: true }));
    else if (m[3] !== undefined) out.push(...runs(m[3], { ...base, italics: true }));
    else if (m[4] !== undefined) out.push(new TextRun({ text: m[4], ...base, font: MONO, color: base.codeColor || C.code, size: base.size ? base.size - 3 : 20 }));
    else if (m[5] !== undefined) out.push(new TextRun({ text: m[5], ...base, superScript: true }));
    else if (m[6] !== undefined) out.push(new TextRun({ text: m[6], ...base, subScript: true }));
    last = re.lastIndex;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}
const sp = (after = 110, before = 0, line = 276) => ({ after, before, line, lineRule: 'auto' });
function P(text, o = {}) {
  return new Paragraph({ children: runs(text, o.run || {}), alignment: o.align || AlignmentType.JUSTIFIED,
    spacing: o.spacing || sp(o.after ?? 110, o.before ?? 0), keepNext: o.keepNext, indent: o.indent, keepLines: o.keepLines,
    pageBreakBefore: o.pageBreakBefore, tabStops: o.tabStops, border: o.border });
}
function bullets(items, o = {}) {
  return items.map((t) => new Paragraph({ children: runs(t, o.run || {}), numbering: { reference: 'bul', level: o.level || 0 },
    alignment: AlignmentType.JUSTIFIED, spacing: sp(o.after ?? 60) }));
}
// danh sách đánh số kiểu "1)" viết tay, thụt lề treo
function numbered(items, o = {}) {
  return items.map((t, i) => new Paragraph({ children: [new TextRun({ text: (o.labels ? o.labels[i] : `${i + 1})`) + ' ', bold: true, color: o.color || C.navy }), ...runs(t)],
    alignment: AlignmentType.JUSTIFIED, spacing: sp(60), indent: { left: 640, hanging: 340 } }));
}
const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const NB = { top: none, bottom: none, left: none, right: none };
const line = (c = 'A6B4CC', s = 4) => ({ style: BorderStyle.SINGLE, size: s, color: c });
const allB = (c, s) => ({ top: line(c, s), bottom: line(c, s), left: line(c, s), right: line(c, s) });
function cell(children, o = {}) {
  return new TableCell({ children, width: { size: o.w, type: WidthType.DXA }, borders: o.borders || allB('A6B4CC', 4),
    shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: 'auto' } : undefined,
    margins: o.mar || { top: 50, bottom: 50, left: 90, right: 90 }, verticalAlign: o.valign || VerticalAlign.CENTER,
    columnSpan: o.span, rowSpan: o.rowSpan });
}
function table(cols, rows, o = {}) {
  return new Table({ width: { size: cols.reduce((a, b) => a + b, 0), type: WidthType.DXA }, columnWidths: cols, rows,
    alignment: o.align || AlignmentType.CENTER, borders: { top: none, bottom: none, left: none, right: none, insideHorizontal: none, insideVertical: none } });
}
// bảng dữ liệu có hàng tiêu đề xanh nhạt
function dataTable(cols, head, body, o = {}) {
  const hp = (t, i) => new Paragraph({ children: runs(t, { bold: true, color: C.navy, font: ARIAL, size: 19 }), alignment: AlignmentType.CENTER, spacing: { line: 252, lineRule: 'auto' }, keepNext: true });
  const rows = [new TableRow({ tableHeader: true, cantSplit: true, children: head.map((t, i) => cell([hp(t, i)], { w: cols[i], fill: 'E8EEF7' })) })];
  body.forEach((r, ri) => rows.push(new TableRow({ cantSplit: true, height: o.rowHeight ? { value: o.rowHeight, rule: 'atLeast' } : undefined, children: r.map((t, i) => {
    const al = (o.aligns && o.aligns[i]) || AlignmentType.LEFT;
    const paras = (Array.isArray(t) ? t : [t]).map((x) => new Paragraph({ children: runs(String(x), { size: o.size || 21, ...(o.colRun && o.colRun[i] || {}) }), alignment: al, spacing: { line: 252, lineRule: 'auto', after: 0 }, keepNext: o.keepNext }));
    return cell(paras, { w: cols[i], fill: o.zebra && ri % 2 ? 'F7F9FC' : (o.fills && o.fills[ri] && o.fills[ri][i]) || undefined });
  }) })));
  return table(cols, rows);
}
// khung màu có viền trái đậm (giống các khung KHỞI ĐỘNG, ĐỊNH NGHĨA... của Tập 1)
const BOX = {
  recap: ['1F3864', 'F3F6FA'], note: ['C55A11', 'FDF0E6'], hint: ['1B7F79', 'E6F4F3'], model: ['B26A00', 'FFF6DB'],
  remember: ['2E7D32', 'EAF5E6'], theorem: ['6A4C93', 'F1ECF8'], warn: ['C0504D', 'FBEAEA'], def: ['1F3864', 'EEF3FA'],
};
function box(kind, title, children, o = {}) {
  const [c, f] = BOX[kind];
  const kids = [];
  if (title) kids.push(new Paragraph({ children: runs(title, { bold: true, color: c, font: ARIAL, size: 19, codeColor: c }), spacing: sp(60), keepNext: true }));
  kids.push(...children);
  return [table([W], [new TableRow({ cantSplit: o.cantSplit !== false, children: [cell(kids, { w: W, fill: f, mar: { top: 100, bottom: 80, left: 180, right: 160 },
    borders: { top: none, bottom: none, right: none, left: { style: BorderStyle.SINGLE, size: 24, color: c } } })] })]), gap()];
}
const gap = (a = 120) => new Paragraph({ children: [new TextRun({ text: '', size: 8 })], spacing: { after: a, before: 0, line: 120, lineRule: 'exact' } });

// ---------- hình
function pngSize(file) { const b = fs.readFileSync(file); return [b.readUInt32BE(16), b.readUInt32BE(20)]; }
let figCounter = { key: '', n: 0 };
function figure(name, widthIn, cap, label) {
  const file = name.startsWith('tap2:') ? path.join(FIGDIR, name.slice(5) + '.png') : path.join(FIGDIR, name + '.png');
  const [pw, ph] = pngSize(file);
  // sơ đồ khối: in gần đúng cỡ gốc (ảnh 220 dpi) để chữ không quá nhỏ, cho phép cao hơn hình thường
  const isFlow = /_(ngaytho|toiuu)$/.test(name);
  if (isFlow) widthIn = Math.min(pw / 220 * 0.92, 6.0);
  let w = Math.round(widthIn * 96), h = Math.round(w * ph / pw);
  const MAXH = (isFlow ? 5.4 : 3.6) * 96; if (h > MAXH) { w = Math.round(w * MAXH / h); h = Math.round(MAXH); }
  const out = [new Paragraph({ children: [new ImageRun({ type: 'png', data: fs.readFileSync(file), transformation: { width: w, height: h } })],
    alignment: AlignmentType.CENTER, spacing: { before: 60, after: 60 }, keepNext: true })];
  if (cap) out.push(new Paragraph({ children: [new TextRun({ text: label + ' ', bold: true, italics: true, color: '404040', size: 19 }), ...runs(cap, { italics: true, color: '404040', size: 19 })],
    alignment: AlignmentType.CENTER, spacing: sp(160) }));
  return out;
}
// khối mã nguồn (giống Tập 1: nền xám nhạt, viền trái xám xanh, số dòng)
function codeBlock(title, code) {
  const lines = code.replace(/\n$/, '').split('\n');
  const kids = [new Paragraph({ children: runs(title, { bold: true, color: C.gray, font: ARIAL, size: 17 }), spacing: sp(60), keepNext: true })];
  const LIM = 78;
  lines.forEach((ln, i) => {
    // dòng quá dài: ngắt ở dấu cách gần nhất, dòng tiếp theo thụt vào và không đánh số
    const parts = [];
    let rest = ln; const ind = ln.match(/^ */)[0].length + 4;
    while (rest.length > LIM) {
      let cut = rest.lastIndexOf(' ', LIM);
      if (cut <= ind) cut = LIM;
      parts.push(rest.slice(0, cut)); rest = ' '.repeat(ind) + rest.slice(cut).replace(/^ +/, '');
    }
    parts.push(rest);
    const ci = ln.indexOf('//');
    const inComment = (k) => ci >= 0 && k > 0 && parts[0].length > ci;
    parts.forEach((pt, k) => kids.push(new Paragraph({ children: [new TextRun({ text: (k ? '' : String(i + 1)).padStart(3, ' ') + '  ', font: MONO, size: 17, color: 'A0A0A0' }),
      ...(inComment(k) ? [new TextRun({ text: pt, font: MONO, size: 17, color: '7F7F7F', italics: true })] : codeRuns(pt))],
      spacing: { after: 0, line: 240, lineRule: 'auto' }, keepLines: true })));
  });
  return [table([W], [new TableRow({ cantSplit: false, children: [cell(kids, { w: W, fill: 'F7F7F7', mar: { top: 90, bottom: 90, left: 160, right: 120 },
    borders: { top: line('D0D0D0'), bottom: line('D0D0D0'), right: line('D0D0D0'), left: { style: BorderStyle.SINGLE, size: 18, color: '9AA9C4' } } })] })]), gap(160)];
}
const KW = new Set(['int', 'long', 'char', 'bool', 'void', 'return', 'for', 'while', 'if', 'else', 'using', 'namespace', 'const', 'auto', 'double', 'struct', 'vector', 'string']);
function codeRuns(ln) {
  const out = []; const re = /(\/\/.*$|"[^"]*"|#\w+|\b\d+\b|\b[A-Za-z_]\w*\b)/g; let last = 0, m;
  const push = (t, o = {}) => out.push(new TextRun({ text: t, font: MONO, size: 17, color: C.txt, ...o }));
  while ((m = re.exec(ln))) {
    if (m.index > last) push(ln.slice(last, m.index));
    const t = m[0];
    if (t.startsWith('//')) push(t, { color: '7F7F7F', italics: true });
    else if (t.startsWith('"')) push(t, { color: C.green });
    else if (t.startsWith('#')) push(t, { color: C.purple });
    else if (/^\d+$/.test(t)) push(t, { color: C.red });
    else if (KW.has(t)) push(t, { color: C.navy, bold: true });
    else push(t);
    last = re.lastIndex;
  }
  if (last < ln.length) push(ln.slice(last));
  if (!out.length) push(' ');
  return out;
}
module.exports = { D, C, W, ARIAL, MONO, runs, P, bullets, numbered, cell, table, dataTable, box, gap, figure, codeBlock, sp, none, NB, line, allB, BOX };
