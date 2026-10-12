// Phần đầu sách (bìa, lời nói đầu, cách sử dụng, mục lục, bảng tổng hợp) và phụ lục
const path = require('path');
module.exports = { build, back, targets };

function pg(ctx, key) { const p = ctx.PAGES[key]; return p ? String(p) : '000'; }

function build(ctx) {
  const { F, CH, LEVEL, blocks, h1 } = ctx;
  const { D, C, W, ARIAL, runs, P, bullets, cell, table, dataTable, box, gap, figure, codeBlock, allB } = F;
  const { Paragraph, TextRun, TableRow, AlignmentType, TabStopType, TabStopPosition, BorderStyle } = D;
  const out = [];
  const nP = CH.reduce((s, ch) => s + ch.lessons.reduce((t, L) => t + L.problems.length, 0), 0);
  const nL = CH.reduce((s, ch) => s + ch.lessons.length, 0);
  const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, NB = { top: none, bottom: none, left: none, right: none };

  // ===== BÌA
  out.push(new Paragraph({ children: [new TextRun({ text: 'Tổng hợp và biên soạn: Lê Thành Nam', bold: true, italics: true, color: '404040' })], alignment: AlignmentType.RIGHT, spacing: { after: 240 } }));
  const cp = (t, o) => new Paragraph({ children: [new TextRun({ text: t, font: ARIAL, ...o })], alignment: AlignmentType.CENTER, spacing: { after: o.after ?? 0, line: 276, lineRule: 'auto' } });
  out.push(table([W], [
    new TableRow({ children: [cell([cp('TÀI LIỆU BỒI DƯỠNG HỌC SINH GIỎI TIN HỌC', { bold: true, color: 'FFD966', size: 22, after: 200 }),
      cp('SỐ HỌC', { bold: true, color: 'FFFFFF', size: 64, after: 80 }), cp('Từ cơ bản đến nâng cao', { italics: true, color: 'FFFFFF', size: 34 })],
      { w: W, fill: C.navy, borders: NB, mar: { top: 420, bottom: 420, left: 300, right: 300 } })] }),
    new TableRow({ children: [cell([cp('TẬP 2  ·  BÀI TẬP', { bold: true, color: 'FFFFFF', size: 30 })], { w: W, fill: C.red, borders: NB, mar: { top: 140, bottom: 140, left: 200, right: 200 } })] }),
  ]));
  out.push(gap(300));
  out.push(...figure('cover', 6.0, null));
  out.push(gap(200));
  CH.forEach((ch) => out.push(new Paragraph({ children: [new TextRun({ text: `Chương ${ch.no}. ${ch.title}`, bold: true, color: C.navy, font: ARIAL, size: 22 })], alignment: AlignmentType.CENTER, spacing: { after: 70 } })));
  out.push(gap(200));
  out.push(new Paragraph({ children: [new TextRun({ text: `${nP} bài tập · ràng buộc theo subtask · ví dụ có giải thích và hình minh họa`, italics: true, color: '595959', size: 21 })], alignment: AlignmentType.CENTER }));

  // ===== LỜI NÓI ĐẦU
  out.push(h1('LỜI NÓI ĐẦU', { pb: true }));
  out.push(...blocks([
    'Học số học mà không làm bài tập cũng giống như học bơi trên cạn. Ở Tập 1, các em đã được dẫn từng bước từ ý tưởng ngây thơ tới thuật toán tốt, đã chạy tay trên những ví dụ nhỏ và hiểu **vì sao** mỗi công thức đúng. Tập 2 này là "bể bơi": nơi các em tự mình gặp đề bài mới, tự nhận ra số học ẩn sau câu chuyện, tự chọn công cụ và tự xử lí những chi tiết chỉ lộ ra khi bắt tay vào code: tràn số, số dư âm, chia trong đồng dư, trường hợp n = 1...',
    'Bộ tài liệu gồm ba tập đi cùng nhau:',
    { ul: [`**Tập 1: Lý thuyết** gồm ${nL} bài học trong ${CH.length} chương.`,
      `**Tập 2: Bài tập** (cuốn sách này) gồm **${nP} bài**: mỗi bài học của Tập 1 có đúng ba bài tập ở ba mức độ **cơ bản**, **trung bình** và **nâng cao**. Tên và ý tưởng các bài trùng với mục "Luyện tập" ở cuối mỗi bài học của Tập 1.`,
      '**Tập 3: Hướng dẫn giải** phân tích từng bài từ cách ngây thơ đến cách tối ưu, kèm chương trình hoàn chỉnh.'] },
    'Mỗi bài tập được trình bày như một đề thi thật: có tên tệp, giới hạn thời gian và bộ nhớ, ràng buộc chia theo **subtask** để em biết với mỗi thuật toán mình nghĩ ra sẽ được bao nhiêu điểm. Mọi ví dụ đều có **giải thích** và phần lớn có **hình minh họa** vẽ cùng bảng màu với Tập 1, để em hình dung đề bài trước khi bắt tay vào code. Cuối mỗi bài là khung **CHÚ Ý** chỉ ra những bẫy thường gặp và khung **HƯỚNG SUY NGHĨ** gợi mở hướng đi mà không "lộ" lời giải.',
    'Để đảm bảo độ tin cậy, mỗi bài tập đều có một chương trình giải mẫu; mọi kết quả trong các ví dụ được sinh ra bằng cách **chạy chính chương trình đó**, và chương trình giải mẫu lại được đối chiếu với một chương trình "vét cạn" (hoặc phép tính số lớn chính xác) trên hàng trăm bộ dữ liệu ngẫu nhiên, cũng như được chạy thử trên dữ liệu lớn nhất để kiểm tra thời gian.',
    'Lời khuyên quan trọng nhất: **hãy tự làm trước khi đọc gợi ý**. Một bài tự nghĩ ra sau hai giờ có giá trị hơn mười bài đọc lời giải. Khi bế tắc thật sự, hãy đọc lại phần lí thuyết tương ứng ở Tập 1, rồi mới đọc khung "Hướng suy nghĩ", và chỉ mở Tập 3 khi đã thử hết sức.',
    'Chúc các em luyện tập bền bỉ và đạt kết quả cao!',
  ]));
  out.push(P('*Lê Thành Nam*', { align: AlignmentType.RIGHT }));

  // ===== CÁCH SỬ DỤNG
  out.push(h1('CÁCH SỬ DỤNG TẬP BÀI TẬP', { pb: true }));
  out.push(P('Mỗi bài tập trong sách đều được trình bày theo cùng một cấu trúc, để em quen mắt và tìm thông tin thật nhanh:'));
  out.push(dataTable([2400, 6218], ['Thành phần', 'Nội dung'], [
    ['**Thanh tiêu đề**', 'Mã bài (số bài học . thứ tự), tên bài và mức độ khó.'],
    ['**Dải thông tin**', 'Tên tệp chương trình, tệp dữ liệu vào, tệp kết quả; giới hạn thời gian và bộ nhớ.'],
    ['**Kiến thức**', 'Kiến thức cần dùng và bài học tương ứng ở Tập 1.'],
    ['**Đề bài**', 'Câu chuyện và yêu cầu của bài toán.'],
    ['**Dữ liệu vào / Kết quả**', 'Khuôn dạng chính xác của tệp vào và tệp ra.'],
    ['**Ràng buộc**', 'Giới hạn chung và bảng **subtask**: mỗi subtask có thêm ràng buộc riêng và chiếm một tỉ lệ điểm.'],
    ['**Ví dụ**', 'Một hoặc vài bộ dữ liệu mẫu, kèm cột giải thích và hình minh họa.'],
    ['**CHÚ Ý**', 'Những bẫy làm mất điểm: tràn số, tràn ngăn xếp, trường hợp đặc biệt...'],
    ['**HƯỚNG SUY NGHĨ**', 'Vài câu gợi mở để đọc khi đã thật sự bế tắc.'],
  ], { size: 20 }), gap(160));
  out.push(ctx.subhead('Ba mức độ của bài tập', { before: 120 }));
  out.push(...figure('levels', 5.6, null));
  out.push(dataTable([2000, 6618], ['Mức độ', 'Ý nghĩa'], [
    [LEVEL[1][0], 'Áp dụng gần như trực tiếp thuật toán của bài học; trọng tâm là cài đặt đúng, đủ nhanh, xử lí cẩn thận dữ liệu vào ra.'],
    [LEVEL[2][0], 'Cần thêm một quan sát, một bước biến đổi hoặc một chi tiết cài đặt quan trọng trước khi dùng được thuật toán.'],
    [LEVEL[3][0], 'Kết hợp nhiều kĩ thuật, mô hình hóa khó, hoặc phải dựng lại đáp án; tương đương bài khó của kì thi học sinh giỏi cấp tỉnh, cấp quốc gia.'],
  ], { size: 20, fills: [[LEVEL[1][2], null], [LEVEL[2][2], null], [LEVEL[3][2], null]] }), gap(160));
  out.push(ctx.subhead('Subtask và chiến lược lấy điểm', { before: 120 }));
  out.push(...blocks([
    'Bảng subtask cho biết với ràng buộc nhỏ hơn em được bao nhiêu phần trăm số điểm. Chẳng hạn ở bài 2.2, chương trình thử mọi số từ 1 tới n (O(n)) đã được một phần số điểm, dù n tới 10^12^ đòi hỏi O(√n). Trong phòng thi, hãy luôn:',
    { ol: ['Viết lời giải ngây thơ cho subtask nhỏ nhất trước: vừa lấy điểm chắc chắn, vừa có công cụ để kiểm tra lời giải tốt.', 'Đọc kĩ các subtask ở giữa: chúng thường gợi ý từng bước tiến tới lời giải đầy đủ.', 'Khi làm xong lời giải tốt, đối chiếu với lời giải ngây thơ trên nhiều bộ dữ liệu nhỏ (xem Phụ lục B).'] },
  ]));
  out.push(ctx.subhead('Quy ước chung', { before: 120 }));
  out.push(...bullets([
    'Các số trên cùng một dòng cách nhau bởi dấu cách. "Mô-đun 10^9^ + 7" nghĩa là in số dư (không âm) khi chia cho 1 000 000 007.',
    'Nếu không ghi khác, giới hạn thời gian là 1 giây và bộ nhớ là 256 MB cho mỗi test.',
    'Với bài có **nhiều đáp án đúng**, đề bài ghi rõ "in cách bất kì"; bài làm được chấm bằng chương trình kiểm tra (checker).',
    'Chương trình đọc và ghi theo kiểu "có tệp thì đọc tệp" như ở Tập 1, để dùng được cả với phần mềm chấm Themis lẫn các trang chấm trực tuyến:',
  ]));
  out.push(...codeBlock('NGAYTHU.CPP: khung chương trình dùng cho mọi bài trong sách', `#include <bits/stdc++.h>
using namespace std;

int main() {
    // Có tệp thì đọc tệp, không có thì đọc từ bàn phím
    if (fopen("NGAYTHU.INP", "r")) {
        freopen("NGAYTHU.INP", "r", stdin);
        freopen("NGAYTHU.OUT", "w", stdout);
    }
    long long n;
    scanf("%lld", &n);
    // ... phần giải bài toán ...
    return 0;
}`));
  out.push(ctx.subhead('Quy ước màu trong hình vẽ', { before: 120 }));
  out.push(P('Hình minh họa dùng chung bảng màu với Tập 1:'));
  out.push(dataTable([2600, 6018], ['Màu', 'Ý nghĩa'], [
    ['Ô **vàng** viền đỏ', 'Giá trị cần chú ý: đáp số, số đang xét, phần tử thuộc đáp án.'], ['Ô **xanh dương**', 'Giá trị đã tính xong, hoặc phần tử "bình thường".'],
    ['Ô **cam nhạt**', 'Dữ liệu vào: chữ số, số hạng, phần tử của dãy.'], ['Ô **xám**', 'Giá trị bị loại (hợp số đã gạch...) hoặc khởi tạo.'],
    ['Chữ **đỏ**', 'Kết luận, đáp số, chỗ dễ sai.'], ['Đỉnh, cạnh (nếu có)', 'Giống Tập 1 của bộ Lý thuyết đồ thị.'],
  ], { size: 20 }), gap(160));
  out.push(...box('remember', 'LỘ TRÌNH LUYỆN TẬP GỢI Ý', bullets([
    `**Vòng 1:** làm ${nL} bài ★☆☆ theo thứ tự các bài học, ngay sau khi học xong bài lí thuyết tương ứng.`,
    `**Vòng 2:** làm ${nL} bài ★★☆; mỗi bài cố gắng tự tìm ra "bước biến đổi" trước khi đọc Hướng suy nghĩ.`,
    `**Vòng 3:** làm ${nL} bài ★★★ như một kì thi thử: bấm giờ, tự lấy điểm từng subtask.`,
    'Ghi lại tiến độ vào bảng ở Phụ lục C để biết mình còn yếu ở chương nào.',
  ])));

  // ===== MỤC LỤC
  out.push(h1('MỤC LỤC', { pb: true, size: 34 }));
  const tocLine = (t, page, lvl) => new Paragraph({
    children: lvl === 0 ? [new TextRun({ text: t, font: ARIAL, bold: true, color: C.navy, size: 21 }), new TextRun({ text: '\t', size: 22 }), new TextRun({ text: page, bold: true, size: 22 })]
      : [new TextRun({ text: t, size: 22 }), new TextRun({ text: '\t' + page, size: 22 })],
    tabStops: [{ type: TabStopType.RIGHT, position: W, leader: 'dot' }], spacing: lvl === 0 ? { before: 160, after: 60 } : { before: 20, after: 20 }, indent: lvl ? { left: 360 } : undefined });
  out.push(tocLine('LỜI NÓI ĐẦU', pg(ctx, 'loinoidau'), 0));
  out.push(tocLine('CÁCH SỬ DỤNG TẬP BÀI TẬP', pg(ctx, 'cachdung'), 0));
  out.push(tocLine(`BẢNG TỔNG HỢP ${nP} BÀI TẬP`, pg(ctx, 'tonghop'), 0));
  CH.forEach((ch) => {
    out.push(tocLine(`CHƯƠNG ${ch.no}. ${ch.title}`, pg(ctx, 'ch' + ch.no), 0));
    ch.lessons.forEach((L) => out.push(tocLine(`Bài ${L.no}. ${L.title}  (bài tập ${L.problems.map((p) => p.id).join(', ')})`, pg(ctx, 'L' + L.no), 1)));
  });
  out.push(tocLine('PHỤ LỤC A. KIỂM TRA TRƯỚC KHI NỘP BÀI', pg(ctx, 'plA'), 0));
  out.push(tocLine('PHỤ LỤC B. TỰ KIỂM TRA BẰNG CÁCH ĐỐI CHIẾU', pg(ctx, 'plB'), 0));
  out.push(tocLine('PHỤ LỤC C. BẢNG THEO DÕI TIẾN ĐỘ', pg(ctx, 'plC'), 0));

  // ===== BẢNG TỔNG HỢP
  out.push(h1(`BẢNG TỔNG HỢP ${nP} BÀI TẬP`, { pb: true }));
  out.push(P('Bảng dưới đây liệt kê toàn bộ các bài tập của sách, kèm tên tệp, mức độ, kiến thức chính và số trang, để em tiện chọn bài theo chủ đề hoặc theo mức độ.'));
  CH.forEach((ch) => {
    out.push(ctx.subhead(`Chương ${ch.no}. ${ch.title}`, { before: 160, color: C.navy }));
    const rows = []; const fills = [];
    ch.lessons.forEach((L) => L.problems.forEach((p) => {
      rows.push([`**${p.id}**`, `**${p.name}**`, '`' + p.code + '`', LEVEL[p.level][0], p.skill, pg(ctx, 'P' + p.id)]);
      fills.push([null, null, null, LEVEL[p.level][2], null, null]);
    }));
    out.push(dataTable([650, 1950, 1450, 1750, 2018, 800], ['Bài', 'Tên bài', 'Tệp', 'Mức độ', 'Kĩ năng rèn luyện', 'Trang'], rows,
      { size: 18, fills, aligns: [AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.LEFT, AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.CENTER] }));
  });
  return out;
}

function back(ctx) {
  const { F, CH, LEVEL, blocks, h1 } = ctx;
  const { D, C, W, P, bullets, dataTable, box, gap, codeBlock } = F;
  const { AlignmentType } = D;
  const out = [];
  out.push(h1('PHỤ LỤC A. KIỂM TRA TRƯỚC KHI NỘP BÀI'));
  out.push(P('Rất nhiều điểm bị mất không phải vì thuật toán sai mà vì những lỗi nhỏ. Trước khi nộp, hãy rà lại danh sách dưới đây; các lỗi này đã xuất hiện trong khung CHÚ Ý của nhiều bài tập.'));
  const chk = (title, items) => box('recap', title, bullets(items.map((t) => '☐  ' + t)));
  out.push(...chk('ĐỌC GHI DỮ LIỆU', ['Tên tệp đúng chính tả, viết hoa đúng như đề (NGAYTHU.INP, NGAYTHU.OUT).', 'Đọc nhanh (`scanf` hoặc `ios::sync_with_stdio(false)`) khi dữ liệu có từ 10^5^ số trở lên.', 'Số cho dưới dạng **xâu** (hàng nghìn chữ số) phải đọc vào `string`, không đọc vào kiểu số.', 'In đúng khuôn dạng: số dòng, thứ tự, dấu cách; in −1 / NO đúng như yêu cầu.']));
  out.push(...chk('TRÀN SỐ', ['Mọi biến có thể vượt 2·10^9^ đều là `long long`; tích hai số tới 10^18^ dùng `__int128`.', 'Lấy dư **sau mỗi phép tính** khi đề yêu cầu mô-đun; tích hai số dư < 10^9^ + 7 vừa `long long`.', 'BCNN: chia trước, nhân sau; kiểm tra vượt giới hạn trước khi nhân.', 'Vòng lặp `for (d = 1; d * d <= n; d++)`: d phải là `long long` khi n tới 10^18^.']));
  out.push(...chk('SỐ DƯ VÀ PHÉP CHIA', ['Số âm: `a % m` có thể âm trong C++; dùng `((a % m) + m) % m`.', 'Không chia trong đồng dư: nhân với nghịch đảo (Tập 1, Bài 10), và chỉ khi gcd(b, m) = 1.', 'Kết quả trừ theo mô-đun phải cộng thêm m trước khi lấy dư.', 'm = 1: mọi số dư đều bằng 0. Đã thử chưa?']));
  out.push(...chk('TRƯỜNG HỢP ĐẶC BIỆT', ['n = 0, n = 1, n là số nguyên tố, n là số chính phương, n là lũy thừa của 2.', 'a = 0 hoặc b = 0 trong gcd, lũy thừa 0^0^ (thường quy ước bằng 1).', 'Sàng: các số 0 và 1 không phải số nguyên tố; số 2 là số nguyên tố chẵn duy nhất.', 'Nhiều bộ dữ liệu trong một tệp: đã khởi tạo lại các mảng, biến đếm chưa?']));
  out.push(...chk('KIỂM TRA CUỐI CÙNG', ['Chạy lại toàn bộ ví dụ trong đề.', 'Tự tạo một test lớn nhất để đo thời gian.', 'Đối chiếu với lời giải ngây thơ trên test ngẫu nhiên nhỏ (Phụ lục B).', 'Thử test lớn nhất có kết quả đã biết (ví dụ n = 10^18^) để kiểm tra tràn số.']));

  out.push(h1('PHỤ LỤC B. TỰ KIỂM TRA BẰNG CÁCH ĐỐI CHIẾU', { pb: true }));
  out.push(...blocks([
    'Mọi lời giải mẫu của bộ sách đều được kiểm tra bằng kĩ thuật **đối chiếu** (còn gọi là "chấm trâu"). Ý tưởng rất đơn giản: viết một chương trình **ngây thơ** (thường là vét cạn, chậm nhưng chắc chắn đúng), sinh thật nhiều bộ dữ liệu **nhỏ** ngẫu nhiên, chạy cả hai chương trình và so sánh kết quả. Chỉ cần một bộ cho kết quả khác nhau là em đã có trong tay một test nhỏ làm lộ lỗi sai.',
    'Ba chương trình cần có:',
    { ul: ['`GEN.CPP`: sinh ngẫu nhiên một bộ dữ liệu nhỏ và in ra màn hình.', '`TRAU.CPP`: lời giải ngây thơ.', '`SOL.CPP`: lời giải cần kiểm tra.'] },
    'Lưu ý: khi đối chiếu, hãy đặt các chương trình ở thư mục **không có** tệp `.INP` của bài, để kiểu đọc "có tệp thì đọc tệp" chuyển sang đọc từ bàn phím (luồng chuẩn).',
  ]));
  out.push(...codeBlock('GEN.CPP: sinh ngẫu nhiên một bộ dữ liệu nhỏ cho bài 2.2 (một số n ≤ 1000)', `#include <bits/stdc++.h>
using namespace std;

int main(int argc, char* argv[]) {
    mt19937 rng(atoi(argv[1]));     // hạt giống lấy từ tham số dòng lệnh
    int n = rng() % 1000 + 1;       // số nhỏ: vét cạn chạy tức thì
    printf("%d\\n", n);
    return 0;
}`));
  out.push(...codeBlock('DOICHIEU.CPP: chạy 1000 test, dừng ở test đầu tiên có kết quả khác nhau', `#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int t = 1; t <= 1000; t++) {
        string seed = to_string(t);
        system(("gen " + seed + " > test.inp").c_str());
        system("sol < test.inp > sol.out");
        system("trau < test.inp > trau.out");
        // Windows dùng "fc", Linux dùng "cmp -s"
        if (system("fc sol.out trau.out > nul") != 0) {
            printf("Sai o test %d, xem tep test.inp\\n", t);
            return 0;
        }
    }
    printf("Ca 1000 test deu khop!\\n");
    return 0;
}`));
  out.push(...box('note', 'CHÚ Ý', blocks(['Với bài có nhiều đáp án đúng (đề bài ghi "in cách bất kì"), không thể so sánh trực tiếp hai tệp kết quả. Hãy viết một chương trình **kiểm tra**: đọc dữ liệu vào và kết quả của em, rồi kiểm tra kết quả có hợp lệ không và có tối ưu bằng kết quả của chương trình trâu không.',
    'Test ngẫu nhiên nên **nhỏ** (số nhỏ, dãy ngắn): khi phát hiện sai, em sẽ chạy tay được ngay trên test đó. Với bài số học, Python tính được số nguyên lớn chính xác, nên một dòng Python cũng có thể là "chương trình trâu" rất tốt.'])));

  out.push(h1('PHỤ LỤC C. BẢNG THEO DÕI TIẾN ĐỘ', { pb: true }));
  out.push(P('Sau mỗi lần làm bài, hãy ghi lại ngày làm, số điểm (theo subtask) và một dòng ghi chú về điều học được hoặc lỗi đã mắc. Đọc lại cột ghi chú trước mỗi kì thi.'));
  CH.forEach((ch) => {
    const rows = []; const fills = [];
    ch.lessons.forEach((L) => L.problems.forEach((p) => { rows.push([`**${p.id}**`, p.name, LEVEL[p.level][0].split(' ')[0], '', '', '']); fills.push([null, null, LEVEL[p.level][2], null, null, null]); }));
    out.push(ctx.subhead(`Chương ${ch.no}. ${ch.title}`, { before: 140, color: C.navy }));
    out.push(dataTable([650, 2400, 900, 1150, 900, 2618], ['Bài', 'Tên bài', 'Mức độ', 'Ngày làm', 'Điểm', 'Ghi chú'], rows,
      { size: 18, fills, rowHeight: 480, aligns: [AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.CENTER, AlignmentType.CENTER, AlignmentType.CENTER, AlignmentType.LEFT] }));
  });
  return out;
}

// Cách tìm số trang của từng mục trong bản PDF dựng thử (xem build/paginate.py)
function targets(ctx) {
  const t = [{ key: 'loinoidau', re: 'Học số học mà không làm bài tập' }, { key: 'cachdung', re: 'Mỗi bài tập trong sách đều được trình bày theo cùng' },
    { key: 'tonghop', re: 'Bảng dưới đây liệt kê toàn bộ các bài tập' }, { key: 'plA', re: 'Rất nhiều điểm bị mất không phải' },
    { key: 'plB', re: 'Mọi lời giải mẫu của bộ sách đều được kiểm tra' }, { key: 'plC', re: 'Sau mỗi lần làm bài, hãy ghi lại' }];
  ctx.CH.forEach((ch) => {
    t.push({ key: 'ch' + ch.no, re: 'TRONG CHƯƠNG NÀY', also: `CHƯƠNG ${ch.no}\\.` });
    ch.lessons.forEach((L) => {
      t.push({ key: 'L' + L.no, re: `ÔN NHANH KIẾN THỨC · Tập 1, Bài ${L.no}\\b` });
      L.problems.forEach((p) => t.push({ key: 'P' + p.id, re: `BÀI ${p.id.replace('.', '\\.')}\\b` }));
    });
  });
  return t;
}
