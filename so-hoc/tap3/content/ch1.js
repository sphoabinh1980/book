// SỐ HỌC — TẬP 3. CHƯƠNG 1. CHIA HẾT VÀ ƯỚC SỐ
module.exports = {
  no: 1,
  intro: 'Các bài tập của chương 1 không đòi hỏi thuật toán phức tạp, nhưng là nơi các lỗi số học "kinh điển" lộ ra rõ nhất: số dư âm, tràn số khi nhân, đọc số quá lớn vào kiểu số, duyệt tới n thay vì √n. Ở mỗi bài, em sẽ thấy một lời giải "trông như đúng" mất điểm vì đúng một chi tiết như thế. Bảng dưới đây tóm tắt con đường từ cách ngây thơ tới lời giải mẫu của từng bài.',
  solutions: [
    // ================================================================ 1.1
    {
      id: '1.1', key: 'Số dư không âm: ((d + k mod 7) mod 7 + 7) mod 7.',
      understand: [
        'Bảy ngày trong tuần lặp lại vòng tròn: đi thêm 7 ngày lại về đúng thứ cũ. Đánh số lại thứ Hai = 0, thứ Ba = 1, ..., Chủ nhật = 6 (tức d = t − 2). Khi đó "k ngày nữa" là ngăn số (d + k) mod 7 trên vòng tròn, và "|k| ngày trước" chính là trường hợp k âm của cùng công thức.',
        'Câu hỏi thực chất là: tính **số dư không âm** của d + k khi chia cho 7, với k có thể âm và lớn tới 10^18^.',
        { fig: 'tap2:ngaythu', w: 5.8, cap: 'Mỗi thứ là một ngăn trên vòng tròn 7 ngăn.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Đếm từng ngày',
        body: [
          'Làm đúng như khi đếm trên lịch: xuất phát từ hôm nay, mỗi bước đi thêm một ngày (k > 0) hoặc lùi một ngày (k < 0), lặp |k| lần.',
          { fig: 'f_ngaythu_naive', w: 3.0, cap: 'Sơ đồ khối của cách đếm từng ngày.' },
          { file: 'NGAYTHU_1demngay', title: 'Cách ngây thơ: đếm từng ngày' },
          { cx: 'O(|k|) cho mỗi câu hỏi, tổng O(Q · max|k|).' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (Q ≤ 100, k ≤ 10^6^): tối đa 10^8^ bước đơn giản, chạy kịp: **{{P:NGAYTHU_1demngay:1}} điểm**.', '**Subtask 2, 3** (|k| tới 10^18^): một câu hỏi thôi cũng cần 10^18^ bước, tức hàng trăm năm.'] },
        'Tổng cộng **{{S:NGAYTHU_1demngay}} điểm**. Ai đã học Bài 1 sẽ thay vòng lặp bằng phép chia lấy dư `(t − 2 + k) % 7 + 2`. Cách này chạy tức thì và đúng với k ≥ 0, nhưng khi k âm thì `%` của C++ trả về số **âm**: với t = 2, k = −100 chương trình in (−100) % 7 + 2 = −2 + 2 = **0**, một "thứ" không tồn tại. Được **{{S:NGAYTHU_2quenam}} điểm** (mất trọn Subtask 3).',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Phép chia lấy dư cho ta "đi vòng" trong O(1), nhưng trong C++ nó chỉ đúng nghĩa toán học khi số bị chia không âm. Cần một cách lấy số dư **luôn nằm trong [0, 6]**.'] },
      ],
      breakthrough: [
        { step: 'Thu gọn k trước' },
        'Theo tính chất đồng dư, đi k ngày và đi k mod 7 ngày cho cùng một thứ. Trong C++, `k % 7` nằm trong khoảng (−7, 7), nên d + k % 7 nằm trong (−7, 13): không bao giờ tràn số, dù k = ±10^18^.',
        { step: 'Sửa số dư âm' },
        'Lấy r = (d + k % 7) % 7, ta có r ∈ (−7, 7). Nếu r âm thì r + 7 chính là số dư đúng (vì hai số chênh nhau đúng một lần 7). Viết gọn một dòng: `r = (r + 7) % 7`, đúng cho cả r âm lẫn r không âm.',
        { formula: 'đáp số = ((d + k mod 7) mod 7 + 7) mod 7 + 2,   d = t − 2' },
        { step: 'Chạy tay các ví dụ' },
        { table: { cols: [1300, 1100, 1800, 1500, 1500, 1418], head: ['(t, k)', 'd', 'k % 7 (C++)', 'r trước khi sửa', 'r sau khi sửa', 'Đáp số'],
          rows: [['(2, 1000)', '0', '6', '6', '6', '**8**'], ['(2, −100)', '0', '−2', '−2', '5', '**7**'], ['(2, 10^18^)', '0', '1', '1', '1', '**3**'], ['(8, 0)', '6', '0', '6', '6', '**8**'], ['(5, −7)', '3', '0', '3', '3', '**5**']],
          aligns: ['center', 'center', 'center', 'center', 'center', 'center'] } },
        { box: 'theorem', title: 'VÌ SAO (r + 7) % 7 LUÔN ĐÚNG?', body: ['Với r ∈ (−7, 7): nếu r ≥ 0 thì r + 7 ∈ [7, 14) nên (r + 7) % 7 = r; nếu r < 0 thì r + 7 ∈ (0, 7) nên (r + 7) % 7 = r + 7. Cả hai trường hợp đều cho số trong [0, 6] đồng dư với r theo mô-đun 7.'] },
      ],
      optimal: [
        { fig: 'f_ngaythu_opt', w: 2.8, cap: 'Sơ đồ khối của lời giải mẫu.' },
        { file: 'NGAYTHU', title: 'NGAYTHU.CPP: số dư không âm, O(1) mỗi câu hỏi' },
        { cx: 'O(1) cho mỗi câu hỏi, O(Q) cho cả bài.' },
      ],
      traps: ['**Số dư âm:** `-100 % 7 == -2` trong C++. Luôn đưa về đoạn [0, m) trước khi dùng.', '**Cộng một bội lớn "cho chắc dương":** (t − 2 + k + 7 · 10^18^) % 7 tràn `long long`. Hãy thu gọn k % 7 trước.', '**Nhầm cách đánh số:** đề dùng 2..8 (8 là Chủ nhật), phải trừ 2 trước và cộng 2 sau.'],
      approaches: [['NGAYTHU_1demngay', 'Đếm từng ngày'], ['NGAYTHU_2quenam', '(t − 2 + k) % 7 + 2, quên số âm'], ['NGAYTHU', 'Số dư không âm']],
    },
    // ================================================================ 1.2
    {
      id: '1.2', key: 'Chữ số cuối của a^b^ chỉ phụ thuộc a mod 10 và b mod 4 (b > 0).',
      understand: [
        'Chữ số tận cùng của a^b^ là a^b^ mod 10. Theo tính chất đồng dư, có thể thay a bằng a mod 10 (chữ số cuối của a). Phần khó còn lại là **số mũ** b: nó có tới 10^5^ chữ số nên không thể lặp b lần, cũng không đọc vào kiểu số được.',
        'Bảng ở Tập 2 (Hình 1.2) cho thấy dãy chữ số cuối của x, x^2^, x^3^, ... luôn tuần hoàn với chu kì 1, 2 hoặc 4: mọi chu kì đều là ước của 4.',
        { fig: 'tap2:chusocuoi', w: 5.4, cap: 'Chữ số cuối của a^b^ theo chữ số cuối của a (hàng) và b (cột).' },
      ],
      naive: {
        title: 'Cách ngây thơ: Nhân b lần',
        body: [
          'Đọc a, b vào `long long`, rồi nhân dần b lần, mỗi lần chỉ giữ chữ số cuối (lấy dư cho 10 ngay sau phép nhân, như Bài 1).',
          { fig: 'f_chusocuoi_naive', w: 2.6, cap: 'Sơ đồ khối của cách nhân b lần.' },
          { file: 'CHUSOCUOI_1lap', title: 'Cách ngây thơ: nhân b lần' },
          { cx: 'O(b) cho mỗi câu hỏi.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (a, b ≤ 10^6^): 10 câu hỏi × 10^6^ phép nhân, chạy tức thì: **{{P:CHUSOCUOI_1lap:1}} điểm**.', '**Subtask 2** (b ≤ 10^18^): quá thời gian.', '**Subtask 3**: a, b có 10^5^ chữ số, không đọc nổi vào `long long`.'] },
        'Tổng cộng **{{S:CHUSOCUOI_1lap}} điểm**. Nhận ra tính tuần hoàn rồi, nhiều bạn dùng b mod 4 nhưng vẫn đọc số vào `unsigned long long`: đúng hai subtask đầu, hỏng hẳn khi số có hàng nghìn chữ số: **{{S:CHUSOCUOI_2longlong}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Ta cần b mod 4 của một số **cho dưới dạng xâu**. Và cẩn thận: số dư 0 không có nghĩa là "mũ 0".'] },
      ],
      breakthrough: [
        { step: 'Chỉ cần chữ số cuối của a' },
        'x = a mod 10 chính là kí tự cuối của xâu a: `x = a.back() - \'0\'`.',
        { step: 'Số mũ chỉ cần biết theo mô-đun 4' },
        'Vì chu kì của mọi chữ số đều chia hết 4, với b ≥ 1 ta có x^b^ ≡ x^e^ (mod 10) với e là số trong {1, 2, 3, 4} đồng dư với b theo mô-đun 4. Chú ý chữ "1, 2, 3, **4**": khi b chia hết cho 4 thì phải dùng e = 4, **không** phải e = 0 (2^4^ = 16 tận cùng 6, còn 2^0^ = 1). Riêng b = 0 thì a^0^ = 1.',
        { step: 'b mod 4 trên xâu: sơ đồ Horner' },
        'Như bài SODU (Tập 1, Bài 1): e ← (e · 10 + c) mod 4 với từng chữ số c của b. Chạy tay ví dụ a = 2, b = 2026:',
        { table: { cols: [2000, 3300, 3318], head: ['Chữ số c', 'e · 10 + c', 'e mới = (…) mod 4'], rows: [['2', '0 · 10 + 2 = 2', '2'], ['0', '2 · 10 + 0 = 20', '0'], ['2', '0 · 10 + 2 = 2', '2'], ['6', '2 · 10 + 6 = 26', '**2**']], aligns: ['center', 'center', 'center'] } },
        'e = 2 nên chữ số cuối là 2^2^ = **4**. Với ví dụ 2: x = 9, b kết thúc bằng "10" nên b mod 4 = 2 (một số chia 4 dư bao nhiêu chỉ phụ thuộc hai chữ số cuối, vì 100 chia hết cho 4), đáp số 9^2^ = 81 → **1**.',
        'Lỗi "số dư 0 nghĩa là mũ 0" phổ biến đến mức đáng một dòng riêng trong bảng điểm: chương trình đọc xâu và tính b mod 4 hoàn toàn đúng, chỉ quên trường hợp e = 0, được **{{S:CHUSOCUOI_3mu0}} điểm**, vì gần như subtask nào cũng có test với b chia hết cho 4.',
      ],
      optimal: [
        { fig: 'f_chusocuoi_opt', w: 3.0, cap: 'Sơ đồ khối của lời giải mẫu.' },
        { file: 'CHUSOCUOI', title: 'CHUSOCUOI.CPP: chữ số cuối và số mũ theo mô-đun 4' },
        { cx: 'O(độ dài của b) cho mỗi câu hỏi.' },
      ],
      traps: ['**b ≡ 0 (mod 4) nhưng b > 0:** dùng mũ 4, không dùng mũ 0.', '**b = 0:** đáp số 1 (kể cả a = 0, theo quy ước của đề).', '**Đọc số khổng lồ vào kiểu số:** dùng `string`.', '**Dùng `pow(a, b)`:** số thực tràn và mất chính xác ngay từ những số rất nhỏ.'],
      approaches: [['CHUSOCUOI_1lap', 'Nhân b lần'], ['CHUSOCUOI_2longlong', 'Mô-đun 4 nhưng đọc vào unsigned long long'], ['CHUSOCUOI_3mu0', 'Đọc xâu, quên trường hợp b chia hết cho 4'], ['CHUSOCUOI', 'Đọc xâu, số mũ 1..4']],
    },
    // ================================================================ 1.3
    {
      id: '1.3', key: 'Horner theo từng số: r ← r · 10^k^ + i, cập nhật 10^k^ khi i đổi số chữ số.',
      understand: [
        'Số bé Na viết là 1 · 2 · 3 ... n viết liền nhau. Khi viết thêm số i (có k chữ số) vào bên phải, giá trị cũ bị "dịch trái" k chữ số, tức nhân với 10^k^, rồi cộng thêm i. Đây là sơ đồ Horner của bài SODU, chỉ khác ở chỗ mỗi lần ta thêm cả một **khối** chữ số thay vì một chữ số.',
        { fig: 'tap2:vietlien', w: 6.0, cap: 'Viết thêm i giống như nhân phần đã viết với 10 (hoặc 100, 1000...) rồi cộng i.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Viết hẳn cả xâu ra',
        body: [
          'Dựng xâu s = "123...n" bằng `to_string`, rồi tính số dư của s như bài SODU.',
          { fig: 'f_vietlien_naive', w: 2.8, cap: 'Sơ đồ khối của cách viết hẳn xâu.' },
          { file: 'VIETLIEN_1xau', title: 'Cách ngây thơ: dựng cả xâu' },
          { cx: 'O(L) thời gian và O(L) bộ nhớ, với L là tổng số chữ số; n = 10^7^ cho L = 68 888 897.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1, 2** (n ≤ 1000): xâu dài chưa tới 3000 kí tự: **{{P:VIETLIEN_1xau:1}} + {{P:VIETLIEN_1xau:2}} điểm**.', '**Subtask 3** (n = 10^7^): chỉ riêng xâu đã chiếm khoảng 69 MB, và khi `string` tự nới rộng dung lượng, nó có thể đòi tới gấp đôi: vượt giới hạn 64 MB.'] },
        'Tổng cộng **{{S:VIETLIEN_1xau}} điểm**. Một lỗi khác: làm đúng ý tưởng Horner theo khối nhưng khai báo r, p là `int`. Khi m gần 10^9^, tích r · p có thể tới 10^18^ và tràn: chỉ đúng khi m nhỏ, được **{{S:VIETLIEN_2int}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Bộ nhớ không cho phép giữ cả xâu. Ta cần cập nhật số dư **ngay khi viết** mỗi số i, như sơ đồ Horner, mà không cần nhìn lại các chữ số trước.'] },
      ],
      breakthrough: [
        { step: 'Horner theo khối' },
        'Gọi r là số dư của phần đã viết. Viết thêm số i có k chữ số: phần đã viết mới bằng (phần cũ) · 10^k^ + i, nên theo tính chất đồng dư:',
        { formula: 'r ← (r · (10^k^ mod m) + i) mod m' },
        { step: 'Giữ sẵn 10^k^ mod m' },
        'Số chữ số k chỉ thay đổi khi i đạt 10, 100, 1000, ...: với n ≤ 10^7^ chỉ có 7 lần. Giữ p = 10^k^ mod m và mốc nxt = 10^k^; khi i = nxt thì p ← p · 10 mod m, nxt ← nxt · 10.',
        { step: 'Chạy tay với n = 12, m = 1000' },
        { table: { cols: [1100, 1600, 3100, 2818], head: ['i', 'p = 10^k^', 'r · p + i', 'r mới (mod 1000)'],
          rows: [['1', '10', '0 · 10 + 1', '1'], ['2..9', '10', '...', '12, 123, 234, ..., 789'], ['10', '**100**', '789 · 100 + 10 = 78910', '910'], ['11', '100', '910 · 100 + 11 = 91011', '11'], ['12', '100', '11 · 100 + 12 = 1112', '**112**']],
          aligns: ['center', 'center', 'center', 'center'] } },
        'Đúng như 123456789101112 = 1000 · 123456789101 + 112.',
        { box: 'note', title: 'VỀ TRÀN SỐ', body: ['r < m ≤ 10^9^ và p < m nên r · p < 10^18^; cộng i ≤ 10^7^ vẫn nhỏ hơn 9,2 · 10^18^: vừa `long long`. Đây là lí do mọi biến trong lời giải mẫu là `long long`.'] },
      ],
      optimal: [
        { fig: 'f_vietlien_opt', w: 3.0, cap: 'Sơ đồ khối của lời giải mẫu.' },
        { file: 'VIETLIEN', title: 'VIETLIEN.CPP: Horner theo từng số, O(n) thời gian, O(1) bộ nhớ' },
        { cx: 'O(n) thời gian, O(1) bộ nhớ.' },
      ],
      traps: ['**Giữ cả xâu:** vượt giới hạn bộ nhớ 64 MB.', '**`int` cho r hoặc p:** tích r · p tới 10^18^.', '**Tính 10^k^ bằng `pow`:** số thực; hơn nữa 10^k^ không cần thiết, chỉ cần 10^k^ mod m.', '**m = 1:** mọi số dư bằng 0; lời giải mẫu xử lí đúng vì p = 10 % 1 = 0.'],
      approaches: [['VIETLIEN_1xau', 'Dựng cả xâu rồi lấy dư'], ['VIETLIEN_2int', 'Horner theo khối, dùng int'], ['VIETLIEN', 'Horner theo khối, long long']],
    },
  ],
};
