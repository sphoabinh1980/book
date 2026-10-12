// Số học — Tập 1: phần đầu sách và phụ lục
module.exports = { build, back, targets };
function pg(ctx, key) { const p = ctx.PAGES[key]; return p ? String(p) : '000'; }

function build(ctx) {
  const { F, CH, blocks, h1 } = ctx;
  const { D, C, W, ARIAL, P, bullets, cell, table, dataTable, box, gap, figure } = F;
  const { Paragraph, TextRun, TableRow, AlignmentType, TabStopType, BorderStyle } = D;
  const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, NB = { top: none, bottom: none, left: none, right: none };
  const out = [];
  // ---------- BÌA
  out.push(new Paragraph({ children: [new TextRun({ text: 'Tổng hợp và biên soạn: Lê Thành Nam', bold: true, italics: true, color: '404040' })], alignment: AlignmentType.RIGHT, spacing: { after: 240 } }));
  const cp = (t, o) => new Paragraph({ children: [new TextRun({ text: t, font: ARIAL, ...o })], alignment: AlignmentType.CENTER, spacing: { after: o.after ?? 0, line: 276, lineRule: 'auto' } });
  out.push(table([W], [
    new TableRow({ children: [cell([cp('TÀI LIỆU BỒI DƯỠNG HỌC SINH GIỎI TIN HỌC', { bold: true, color: 'FFD966', size: 22, after: 200 }),
      cp('SỐ HỌC', { bold: true, color: 'FFFFFF', size: 64, after: 80 }), cp('Từ cơ bản đến nâng cao', { italics: true, color: 'FFFFFF', size: 34 })],
      { w: W, fill: C.navy, borders: NB, mar: { top: 420, bottom: 420, left: 300, right: 300 } })] }),
    new TableRow({ children: [cell([cp('TẬP 1  ·  LÝ THUYẾT', { bold: true, color: 'FFFFFF', size: 30 })], { w: W, fill: C.red, borders: NB, mar: { top: 140, bottom: 140, left: 200, right: 200 } })] }),
  ]));
  out.push(gap(300), ...figure('cover1', 6.2, null), gap(200));
  CH.forEach((ch) => out.push(new Paragraph({ children: [new TextRun({ text: `Chương ${ch.no}. ${ch.title}`, bold: true, color: C.navy, font: ARIAL, size: 22 })], alignment: AlignmentType.CENTER, spacing: { after: 70 } })));
  out.push(gap(200));
  out.push(new Paragraph({ children: [new TextRun({ text: 'Dành cho học sinh THCS, THPT ôn luyện học sinh giỏi Tin học các cấp', italics: true, color: '595959', size: 21 })], alignment: AlignmentType.CENTER }));

  // ---------- LỜI NÓI ĐẦU
  const nL = CH.reduce((s, ch) => s + ch.lessons.length, 0);
  out.push(h1('LỜI NÓI ĐẦU', { pb: true }));
  out.push(...blocks([
    'Khoảng năm 300 trước Công nguyên, trong bộ sách *Cơ sở*, Euclid mô tả một cách tìm ước chung lớn nhất của hai số chỉ bằng những phép trừ liên tiếp. Hơn hai nghìn năm sau, chính thuật toán ấy chạy hàng tỉ lần mỗi ngày bên trong các máy tính: trong phần mềm mã hóa bảo vệ tài khoản ngân hàng, trong các thư viện tính toán, và trong gần như mọi đề thi học sinh giỏi Tin học có một chút "mùi số học".',
    'Học sinh thường gặp ba khó khăn với các bài số học. Thứ nhất, **số quá lớn**: đề cho n tới 10^12^, 10^18^, có khi là một số dài cả triệu chữ số, và mọi vòng lặp "thử từng số" đều chạy không kịp. Thứ hai, **những cái bẫy âm thầm**: tràn số, số dư âm, chia trong đồng dư..., chương trình không báo lỗi mà chỉ in ra kết quả sai. Thứ ba, các công thức thường được học thuộc như những "câu thần chú", nên khi đề bài thay đổi một chút là không biết bắt đầu từ đâu.',
    'Cuốn sách này được viết để giải quyết cả ba khó khăn ấy. Mỗi bài học không đưa ra công thức ngay. Em sẽ được đặt trước một bài toán cụ thể, viết chương trình ngây thơ (có sơ đồ khối và code đầy đủ), đếm số phép tính hoặc chỉ ra chỗ tràn số để thấy bế tắc, rồi được dẫn từng bước tới ý tưởng tốt, kèm chứng minh vì sao nó đúng. Mọi ví dụ đều được chạy tay bằng bảng và hình vẽ; các con số trong bảng được sinh ra bằng cách chạy chính thuật toán, nên em có thể tin từng con số.',
    'Bộ tài liệu gồm ba tập đi cùng nhau:',
    { ul: [`**Tập 1: Lý thuyết** (cuốn sách này) gồm ${nL} bài học trong ${CH.length} chương: ${CH.map((c) => c.title.charAt(0) + c.title.slice(1).toLowerCase()).join('; ')}.`,
      '**Tập 2: Bài tập** gồm các bài tập theo từng bài học, ở ba mức độ (cơ bản, trung bình, nâng cao), có ràng buộc theo subtask như đề thi thật. Tên các bài tập được giới thiệu ở mục *Luyện tập* cuối mỗi bài học.',
      '**Tập 3: Hướng dẫn giải** phân tích từng bài tập từ cách ngây thơ đến cách tối ưu, kèm chương trình hoàn chỉnh và bảng điểm theo thuật toán.'] },
    'Chương trình được viết bằng C++ theo chuẩn C++14, đọc và ghi tệp theo kiểu "có tệp thì đọc tệp" để dùng được cả với phần mềm chấm Themis lẫn các trang chấm trực tuyến. Mọi chương trình trong sách đều đã được kiểm tra bằng cách đối chiếu với chương trình ngây thơ (hoặc với phép tính số lớn chính xác) trên hàng trăm bộ dữ liệu ngẫu nhiên.',
    'Chúc các em học tập say mê và đạt kết quả cao!',
  ]));
  out.push(P('*Lê Thành Nam*', { align: AlignmentType.RIGHT }));

  // ---------- CÁCH HỌC
  out.push(h1('CÁCH HỌC VỚI TÀI LIỆU NÀY', { pb: true }));
  out.push(P('Mỗi bài học đi theo cùng một con đường, giống như cách một người giỏi suy nghĩ khi gặp bài mới:'));
  out.push(dataTable([2200, 6418], ['Phần', 'Nội dung'], [
    ['**Khởi động**', 'Một câu chuyện, một câu đố gần gũi để em bắt đầu nghĩ.'],
    ['**Kiến thức nền**', 'Định nghĩa, định lí, hình vẽ trực quan và ví dụ tính tay.'],
    ['**Bài toán**', 'Đề bài cụ thể, có ví dụ được sinh bằng chính chương trình trong sách.'],
    ['**Ý tưởng ngây thơ**', 'Cách làm đầu tiên ai cũng nghĩ ra, kèm sơ đồ khối, chương trình đầy đủ và phần đếm số phép tính.'],
    ['**Bế tắc**', 'Chỉ ra chính xác vì sao cách ngây thơ chậm (hoặc sai, hoặc tràn số), và đặt câu hỏi dẫn tới ý tưởng mới.'],
    ['**Phá bế tắc**', 'Từng bước: ý tưởng, chạy tay bằng hình và bảng, chứng minh, chương trình.'],
    ['**Mở rộng**', 'Các biến thể và ứng dụng thường gặp trong đề thi.'],
    ['**Bẫy thường gặp**', 'Những lỗi đã làm mất điểm của nhiều thế hệ học sinh.'],
    ['**Ghi nhớ**', 'Tóm tắt những điều cốt lõi nhất.'],
    ['**Luyện tập**', 'Giới thiệu các bài tập tương ứng ở Tập 2 và vài câu tự kiểm tra có đáp số.'],
  ], { size: 21 }), gap(200));
  out.push(P('Các khung màu trong sách có ý nghĩa cố định:'));
  const sw = (fill, bar, t) => cell([new Paragraph({ children: [new TextRun({ text: t, bold: true, color: bar, font: ARIAL, size: 18 })] })],
    { w: 2200, fill, borders: { top: none, bottom: none, right: none, left: { style: BorderStyle.SINGLE, size: 24, color: bar } } });
  const rowK = (fill, bar, t, d) => new TableRow({ cantSplit: true, children: [sw(fill, bar, t), cell([P(d, { after: 0 })], { w: 6418 })] });
  out.push(table([2200, 6418], [
    rowK('FDF0E6', 'C55A11', 'KHỞI ĐỘNG', 'Câu hỏi mở đầu bài học.'),
    rowK('FFFFFF', '1F3864', 'BÀI TOÁN', 'Đề bài chính thức.'),
    rowK('EEF3FA', '1F3864', 'ĐỊNH NGHĨA', 'Khái niệm mới cần nắm chính xác.'),
    rowK('F1ECF8', '6A4C93', 'ĐỊNH LÍ', 'Kết quả quan trọng, thường kèm chứng minh.'),
    rowK('F3F6FA', '1F3864', 'THUẬT TOÁN', 'Các bước của thuật toán, viết bằng lời.'),
    rowK('E6F4F3', '1B7F79', 'ĐẾM SỐ PHÉP TÍNH', 'Phân tích độ phức tạp: O(√n), O(log n), O(n log log n)...'),
    rowK('FBEAEA', 'C0504D', 'BẾ TẮC', 'Chỗ cách làm hiện tại không vượt qua được.'),
    rowK('F1ECF8', '6A4C93', 'VÌ SAO ĐÚNG?', 'Lập luận chứng minh tính đúng đắn.'),
    rowK('FFF6DB', 'B26A00', 'HÃY HÌNH DUNG', 'Hình ảnh trực quan giúp nhớ lâu.'),
    rowK('E6F4F3', '1B7F79', 'VÍ DỤ', 'Một ví dụ tính tay ngắn.'),
    rowK('FDF0E6', 'C55A11', 'LƯU Ý', 'Chi tiết nhỏ nhưng dễ sai.'),
    rowK('FBEAEA', 'C0504D', 'BẪY THƯỜNG GẶP', 'Các lỗi hay gặp.'),
    rowK('EAF5E6', '2E7D32', 'GHI NHỚ', 'Tóm tắt cuối bài.'),
  ]), gap(200));
  out.push(ctx.subhead('Quy ước màu trong hình vẽ', { color: C.navy }));
  out.push(dataTable([2600, 6018], ['Màu', 'Ý nghĩa'], [
    ['Ô vàng viền đỏ', 'Giá trị đang xét ở bước đó, hoặc kết quả cuối cùng.'],
    ['Ô xanh dương', 'Giá trị đã tính xong.'],
    ['Ô cam nhạt', 'Dữ liệu vào (chữ số, số hạng...).'],
    ['Ô xám', 'Giá trị khởi tạo, hoặc số đã bị loại (ví dụ: hợp số trong sàng).'],
    ['Chữ đỏ', 'Kết luận, đáp số, hoặc chỗ cần chú ý.'],
  ], { size: 21 }), gap(200));
  out.push(ctx.subhead('Kí hiệu dùng trong sách', { color: C.navy }));
  out.push(dataTable([2200, 6418], ['Kí hiệu', 'Ý nghĩa'], [
    ['a mod m', 'Số dư (không âm) của a khi chia cho m.'],
    ['⌊x⌋, ⌈x⌉', 'Phần nguyên dưới (số nguyên lớn nhất ≤ x), phần nguyên trên (số nguyên nhỏ nhất ≥ x).'],
    ['b | a', 'b chia hết a (a chia hết cho b).'],
    ['a ≡ b (mod m)', 'a và b đồng dư theo mô-đun m: m | (a − b).'],
    ['gcd(a, b), lcm(a, b)', 'Ước chung lớn nhất, bội chung nhỏ nhất (trong lời văn viết ƯCLN, BCNN).'],
    ['p', 'Thường dùng cho số nguyên tố.'],
    ['d(n), σ(n), φ(n)', 'Số ước, tổng các ước, số các số trong 1..n nguyên tố cùng nhau với n.'],
    ['C(n, k)', 'Số cách chọn k phần tử từ n phần tử (tổ hợp chập k của n).'],
    ['O(...)', 'Độ phức tạp thời gian. Máy tính làm khoảng 10^8^ phép tính đơn giản mỗi giây.'],
  ], { size: 21 }), gap(200));
  out.push(...box('remember', 'LỜI KHUYÊN KHI HỌC', [P('Hãy đọc với giấy và bút bên cạnh. Mỗi khi gặp một bảng chạy tay, hãy che bảng lại và tự tính trước. Mỗi khi gặp một định lí, hãy thử nó với vài số nhỏ trước khi đọc chứng minh. Và mỗi khi viết một chương trình số học, hãy tự hỏi ba câu: **giá trị lớn nhất có thể là bao nhiêu? có số âm không? có phép chia nào không?** Ba câu hỏi ấy chặn được phần lớn các lỗi số học.', { after: 0 })]));

  // ---------- MỤC LỤC
  out.push(h1('MỤC LỤC', { pb: true, size: 34 }));
  const tocLine = (t, page, lvl) => new Paragraph({
    children: lvl === 0 ? [new TextRun({ text: t, font: ARIAL, bold: true, color: C.navy, size: 21 }), new TextRun({ text: '\t', size: 22 }), new TextRun({ text: page, bold: true, size: 22 })]
      : [new TextRun({ text: t, size: 22 }), new TextRun({ text: '\t' + page, size: 22 })],
    tabStops: [{ type: TabStopType.RIGHT, position: W, leader: 'dot' }], spacing: lvl === 0 ? { before: 140, after: 50 } : { before: 0, after: 20 }, indent: lvl ? { left: 360 } : undefined });
  out.push(tocLine('LỜI NÓI ĐẦU', pg(ctx, 'loinoidau'), 0), tocLine('CÁCH HỌC VỚI TÀI LIỆU NÀY', pg(ctx, 'cachhoc'), 0));
  CH.forEach((ch) => {
    out.push(tocLine(`CHƯƠNG ${ch.no}. ${ch.title}`, pg(ctx, 'ch' + ch.no), 0));
    ch.lessons.forEach((L) => out.push(tocLine(`Bài ${L.no}. ${L.title}`, pg(ctx, 'L' + L.no), 1)));
  });
  out.push(tocLine('PHỤ LỤC A. TỔNG HỢP THUẬT TOÁN VÀ CÔNG THỨC', pg(ctx, 'plA'), 0), tocLine('PHỤ LỤC B. NHỮNG CON SỐ ĐÁNG NHỚ', pg(ctx, 'plB'), 0));
  return out;
}

function back(ctx) {
  const { F, CH, blocks, h1 } = ctx;
  const { D, P, dataTable, gap } = F;
  const { AlignmentType } = D;
  const out = [h1('PHỤ LỤC A. TỔNG HỢP THUẬT TOÁN VÀ CÔNG THỨC')];
  out.push(P('Bảng dưới đây tóm tắt các thuật toán và công thức chính của cuốn sách, cùng độ phức tạp và bài học tương ứng. Hãy dùng nó như một "bản đồ" khi ôn tập: nhìn vào cột đầu, em có nhớ lại được ý tưởng và tự viết được chương trình không?'));
  CH.forEach((ch) => {
    out.push(ctx.subhead(`Chương ${ch.no}. ${ch.title}`, { before: 160, color: F.C.navy }));
    const rows = [];
    ch.lessons.forEach((L) => (L.algos || []).forEach((a) => rows.push([a[0], a[1], `Bài ${L.no}`])));
    out.push(dataTable([4600, 2818, 1200], ['Thuật toán / công thức', 'Độ phức tạp', 'Bài'], rows, { size: 20, aligns: [AlignmentType.LEFT, AlignmentType.CENTER, AlignmentType.CENTER] }), gap(140));
  });
  out.push(h1('PHỤ LỤC B. NHỮNG CON SỐ ĐÁNG NHỚ', { pb: true }));
  out.push(P('Khi đọc ràng buộc của đề bài, những con số dưới đây giúp em ước lượng ngay: vòng lặp chạy bao nhiêu lần, mảng cần bao nhiêu phần tử, kết quả có vừa kiểu dữ liệu không. Mọi giá trị đều được tính lại bằng máy.'));
  out.push(ctx.subhead('Giới hạn của các kiểu số nguyên', { color: F.C.navy }));
  out.push(dataTable([2600, 3400, 2618], ['Kiểu', 'Giá trị lớn nhất', 'Xấp xỉ'], [
    ['`int`', '2^31^ − 1 = 2 147 483 647', '2,1 · 10^9^'], ['`unsigned int`', '2^32^ − 1 = 4 294 967 295', '4,3 · 10^9^'],
    ['`long long`', '2^63^ − 1 = 9 223 372 036 854 775 807', '9,2 · 10^18^'], ['`unsigned long long`', '2^64^ − 1', '1,8 · 10^19^'], ['`__int128`', '2^127^ − 1', '1,7 · 10^38^'],
  ], { size: 20 }), gap(140));
  out.push(ctx.subhead('Số lượng số nguyên tố π(N) và số ước lớn nhất', { color: F.C.navy }));
  out.push(dataTable([1600, 2600, 2400, 2018], ['N', 'π(N): số nguyên tố ≤ N', 'Số ước nhiều nhất của một số ≤ N', 'Đạt tại'], (ctx.NUMBERS || require('./numbers.json')).rows, { size: 20, aligns: [AlignmentType.CENTER, AlignmentType.CENTER, AlignmentType.CENTER, AlignmentType.CENTER] }), gap(140));
  out.push(ctx.subhead('Các mô-đun nguyên tố hay gặp', { color: F.C.navy }));
  out.push(dataTable([3000, 5618], ['Số', 'Ghi chú'], [
    ['10^9^ + 7 = 1 000 000 007', 'Số nguyên tố; tích hai số dư < 10^18^ vừa `long long`.'], ['10^9^ + 9', 'Số nguyên tố, hay dùng cùng 10^9^ + 7 trong băm hai mô-đun.'],
    ['998 244 353 = 119 · 2^23^ + 1', 'Số nguyên tố, dùng trong biến đổi số học nhanh (NTT).'], ['2^61^ − 1', 'Số nguyên tố Mersenne, dùng trong băm, cần nhân `__int128`.'],
  ], { size: 20 }), gap(140));
  return out;
}

function targets(ctx) {
  const t = [{ key: 'loinoidau', re: 'Khoảng năm 300 trước Công nguyên' }, { key: 'cachhoc', re: 'Mỗi bài học đi theo cùng một con đường' },
    { key: 'plA', re: 'Bảng dưới đây tóm tắt các thuật toán' }, { key: 'plB', re: 'Khi đọc ràng buộc của đề bài' }];
  ctx.CH.forEach((ch) => {
    t.push({ key: 'ch' + ch.no, re: 'TRONG CHƯƠNG NÀY', also: `CHƯƠNG ${ch.no}\\.` });
    ch.lessons.forEach((L) => t.push({ key: 'L' + L.no, re: `BÀI ${L.no} `, also: 'Học xong bài này' }));
  });
  return t;
}
