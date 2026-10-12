// Tập 3 — phần đầu sách và phụ lục
const fs = require('fs'), path = require('path');
module.exports = { build, back, targets };
function pg(ctx, key) { const p = ctx.PAGES[key]; return p ? String(p) : '000'; }

function build(ctx) {
  const { F, CH, T2, PROB, LEVEL, blocks, h1 } = ctx;
  const { D, C, W, ARIAL, P, bullets, cell, table, dataTable, box, gap, figure } = F;
  const { Paragraph, TextRun, TableRow, AlignmentType, TabStopType, BorderStyle } = D;
  const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, NB = { top: none, bottom: none, left: none, right: none };
  const out = [];
  out.push(new Paragraph({ children: [new TextRun({ text: 'Tổng hợp và biên soạn: Lê Thành Nam', bold: true, italics: true, color: '404040' })], alignment: AlignmentType.RIGHT, spacing: { after: 240 } }));
  const cp = (t, o) => new Paragraph({ children: [new TextRun({ text: t, font: ARIAL, ...o })], alignment: AlignmentType.CENTER, spacing: { after: o.after ?? 0, line: 276, lineRule: 'auto' } });
  out.push(table([W], [
    new TableRow({ children: [cell([cp('TÀI LIỆU BỒI DƯỠNG HỌC SINH GIỎI TIN HỌC', { bold: true, color: 'FFD966', size: 22, after: 200 }),
      cp('SỐ HỌC', { bold: true, color: 'FFFFFF', size: 64, after: 80 }), cp('Từ cơ bản đến nâng cao', { italics: true, color: 'FFFFFF', size: 34 })],
      { w: W, fill: C.navy, borders: NB, mar: { top: 420, bottom: 420, left: 300, right: 300 } })] }),
    new TableRow({ children: [cell([cp('TẬP 3  ·  HƯỚNG DẪN GIẢI', { bold: true, color: 'FFFFFF', size: 30 })], { w: W, fill: C.red, borders: NB, mar: { top: 140, bottom: 140, left: 200, right: 200 } })] }),
  ]));
  out.push(gap(260), ...figure('cover3', 6.0, null), gap(160));
  T2.forEach((ch) => out.push(new Paragraph({ children: [new TextRun({ text: `Chương ${ch.no}. ${ch.title}`, bold: true, color: C.navy, font: ARIAL, size: 22 })], alignment: AlignmentType.CENTER, spacing: { after: 70 } })));
  out.push(gap(200));
  out.push(new Paragraph({ children: [new TextRun({ text: `Phân tích từ cách ngây thơ đến cách tối ưu · ${Object.keys(PROB).length} bài · bảng điểm chấm thật`, italics: true, color: '595959', size: 21 })], alignment: AlignmentType.CENTER, spacing: { after: 60 } }));
  out.push(new Paragraph({ children: [new TextRun({ text: 'Dành cho học sinh THCS, THPT ôn luyện học sinh giỏi Tin học các cấp', italics: true, color: '595959', size: 21 })], alignment: AlignmentType.CENTER }));

  // LỜI NÓI ĐẦU
  out.push(h1('LỜI NÓI ĐẦU', { pb: true }));
  out.push(...blocks([
    `Tập 3 trình bày lời giải cho cả ${Object.keys(PROB).length} bài tập của Tập 2. Mỗi lời giải không chỉ đưa ra chương trình đạt 100 điểm, mà đi lại đúng con đường một học sinh giỏi suy nghĩ trong phòng thi: bắt đầu từ cách ngây thơ, đếm số phép tính để thấy bế tắc, rồi phá bế tắc bằng một quan sát hay một công cụ phù hợp của số học.`,
    'Với các bài số học, điểm thường không mất vì thuật toán mà vì những chi tiết cài đặt: tích hai số vượt `long long`, số dư âm, chia trong đồng dư, quên trường hợp n = 1 hay m = 1, dùng `sqrt` số thực... Vì vậy bên cạnh cách ngây thơ, nhiều bài còn phân tích những lời giải **"trông như đúng"**: đúng thuật toán nhưng sai một chi tiết, và cho thấy chi tiết đó làm mất bao nhiêu điểm.',
    'Mọi chương trình trong sách đều được kiểm tra hai lần: lời giải mẫu được đối chiếu với lời giải vét cạn trên hàng trăm bộ dữ liệu nhỏ ngẫu nhiên, và **mọi** cách làm (kể cả cách ngây thơ, cách sai) đều được chấm trên bộ test của sách với giới hạn thời gian và bộ nhớ của đề, ngăn xếp 8 MB. Các con số trong **bảng điểm** cuối mỗi bài là điểm thực tế mà từng chương trình nhận được, không phải ước lượng.',
  ]));
  out.push(P('*Lê Thành Nam*', { align: AlignmentType.RIGHT }));

  // CẤU TRÚC
  out.push(h1('CẤU TRÚC MỘT LỜI GIẢI', { pb: true }));
  out.push(dataTable([2300, 6318], ['Mục', 'Nội dung'], [
    ['**1. Hiểu bài toán**', 'Diễn đạt lại đề bằng ngôn ngữ số học: đề bài thực chất hỏi gì, đại lượng nào lớn tới đâu; nhận ra mô hình quen thuộc ẩn sau câu chuyện.'],
    ['**2. Cách ngây thơ**', 'Sơ đồ khối, chương trình và độ phức tạp của cách làm đầu tiên ai cũng nghĩ ra.'],
    ['**3. Bế tắc**', 'Vì sao cách hiện tại không vượt qua được subtask lớn; đôi khi kèm một lời giải trung gian hoặc một lời giải sai "trông như đúng".'],
    ['**4. Phá bế tắc**', 'Quan sát then chốt, thuật toán, chạy tay trên ví dụ, lập luận vì sao đúng.'],
    ['**5. Cách tối ưu**', 'Chương trình hoàn chỉnh và độ phức tạp.'],
    ['**6. Bẫy thường gặp**', 'Những lỗi làm mất điểm hay gặp nhất.'],
    ['**7. Bảng điểm**', 'Điểm thực tế của từng cách làm trên bộ test. Dòng tô xanh là lời giải mẫu.'],
  ], { size: 20 }), gap(200));
  out.push(ctx.subhead('Cách chấm điểm trong sách', { before: 120 }));
  out.push(...bullets([
    'Mỗi bài có một bộ test chia theo đúng các subtask của Tập 2 (thường 2 – 6 test cho mỗi subtask, gồm cả test ngẫu nhiên lẫn test được thiết kế để "bẫy" những lỗi hay gặp: số lớn nhất, số nguyên tố lớn, số âm, m = 1...). Đáp án của test được sinh bằng lời giải mẫu đã kiểm chứng.',
    'Mỗi chương trình chạy với giới hạn thời gian và bộ nhớ của đề, **ngăn xếp 8 MB** (như phần lớn hệ thống chấm chạy Linux; trên Windows, ngăn xếp mặc định chỉ 1 MB nên đệ quy sâu còn nguy hiểm hơn).',
    'Một subtask được **trọn điểm** khi chương trình qua **mọi** test của subtask đó, ngược lại được 0 điểm.',
    'Bài có nhiều đáp án được chấm bằng chương trình kiểm tra (checker).',
  ]));
  out.push(...box('remember', 'LỜI KHUYÊN', blocks(['Đừng đọc lời giải như đọc truyện. Sau mục 3, hãy gấp sách và tự tìm cách phá bế tắc trong ít nhất mười lăm phút. Sau mục 5, hãy tự viết lại chương trình mà không nhìn sách, rồi tự sinh test để đối chiếu với cách ngây thơ của chính em (Tập 2, Phụ lục B).'])));

  // MỤC LỤC
  out.push(h1('MỤC LỤC', { pb: true, size: 34 }));
  const tocLine = (t, page, lvl) => new Paragraph({
    children: lvl === 0 ? [new TextRun({ text: t, font: ARIAL, bold: true, color: C.navy, size: 21 }), new TextRun({ text: '\t', size: 22 }), new TextRun({ text: page, bold: true, size: 22 })]
      : [new TextRun({ text: t, size: 21 }), new TextRun({ text: '\t' + page, size: 21 })],
    tabStops: [{ type: TabStopType.RIGHT, position: W, leader: 'dot' }], spacing: lvl === 0 ? { before: 140, after: 50 } : { before: 0, after: 0 }, indent: lvl ? { left: 360 } : undefined });
  out.push(tocLine('LỜI NÓI ĐẦU', pg(ctx, 'loinoidau'), 0), tocLine('CẤU TRÚC MỘT LỜI GIẢI', pg(ctx, 'cautruc'), 0));
  CH.forEach((ch) => {
    out.push(tocLine(`CHƯƠNG ${ch.no}. ${T2[ch.no - 1].title}`, pg(ctx, 'ch' + ch.no), 0));
    ch.solutions.forEach((s) => out.push(tocLine(`Bài ${s.id}. ${PROB[s.id].name}`, pg(ctx, 'S' + s.id), 1)));
  });
  if (back) { out.push(tocLine('PHỤ LỤC A. TỔNG HỢP LỜI GIẢI VÀ ĐIỂM SỐ', pg(ctx, 'plA'), 0), tocLine('PHỤ LỤC B. THƯ VIỆN MÃ NGUỒN HAY DÙNG', pg(ctx, 'plB'), 0)); }
  return out;
}

function back(ctx) {
  const { F, CH, PROB, LEVEL, blocks, h1, score } = ctx;
  const { D, C, P, dataTable, gap, codeBlock } = F;
  const { AlignmentType } = D;
  const out = [h1('PHỤ LỤC A. TỔNG HỢP LỜI GIẢI VÀ ĐIỂM SỐ')];
  out.push(P('Bảng dưới đây tóm tắt "chìa khóa" của từng lời giải, cùng điểm của cách ngây thơ và của lời giải mẫu trên bộ test của sách. Khoảng cách giữa hai cột điểm chính là phần thưởng cho việc phá bế tắc.'));
  CH.forEach((ch) => {
    out.push(ctx.subhead(`Chương ${ch.no}. ${ctx.T2[ch.no - 1].title}`, { before: 160, color: C.navy }));
    const rows = ch.solutions.map((s) => [`**${s.id}**`, `**${PROB[s.id].name}**`, s.key, String(score(s.approaches[0][0]).total), `**${score(PROB[s.id].code).total}**`]);
    out.push(dataTable([700, 2000, 3918, 1000, 1000], ['Bài', 'Tên bài', 'Chìa khóa của lời giải', 'Ngây thơ', 'Lời giải mẫu'], rows,
      { size: 18, aligns: [AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.LEFT, AlignmentType.CENTER, AlignmentType.CENTER] }));
  });
  out.push(h1('PHỤ LỤC B. THƯ VIỆN MÃ NGUỒN HAY DÙNG', { pb: true }));
  out.push(P('Những đoạn mã dưới đây xuất hiện lặp lại trong nhiều lời giải của sách. Hãy tự gõ lại chúng cho tới khi viết được không cần nhìn, không sai một kí tự: trong phòng thi, chúng là "viên gạch" để xây những lời giải lớn hơn.'));
  const lib = path.join(__dirname, '..', 'code', 'lib');
  for (const [f, t] of [['gcd', 'ƯCLN, BCNN không tràn số, Euclid mở rộng'], ['modular', 'Nhân mô-đun bằng __int128, lũy thừa nhanh, nghịch đảo'], ['sieve', 'Sàng Eratosthenes và sàng ước nguyên tố nhỏ nhất (spf)'],
    ['factor', 'Phân tích thừa số nguyên tố, số ước, tổng ước, phi Euler'], ['millerrabin', 'Miller–Rabin cho mọi số 64 bit'], ['combin', 'Giai thừa, nghịch đảo giai thừa, tổ hợp C(n, k)'],
    ['crt', 'Định lí số dư Trung Hoa (gộp hai phương trình)'], ['matrix', 'Lũy thừa ma trận'], ['blocks', 'Chia khối theo ⌊n / i⌋'], ['bigint', 'Số nguyên lớn: cộng, nhân với số nhỏ, in ra']]) {
    if (fs.existsSync(path.join(lib, f + '.cpp'))) out.push(...codeBlock(t, fs.readFileSync(path.join(lib, f + '.cpp'), 'utf8')));
  }
  return out;
}

function targets(ctx) {
  const t = [{ key: 'loinoidau', re: 'Tập 3 trình bày lời giải cho cả \\d+ bài' }, { key: 'cautruc', re: 'Cách chấm điểm trong sách' },
    { key: 'plA', re: 'Bảng dưới đây tóm tắt "chìa khóa"' }, { key: 'plB', re: 'Những đoạn mã dưới đây xuất hiện lặp lại' }];
  ctx.CH.forEach((ch) => {
    t.push({ key: 'ch' + ch.no, re: 'Cách ngây thơ \\(điểm\\)', also: `CHƯƠNG ${ch.no}\\.` });
    ch.solutions.forEach((s) => t.push({ key: 'S' + s.id, re: `BÀI ${s.id.replace('.', '\\.')}\\b` }));
  });
  return t;
}
