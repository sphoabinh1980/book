// SỐ HỌC — TẬP 1. CHƯƠNG 1. CHIA HẾT VÀ ƯỚC SỐ
const L1 = {
  no: 1, title: 'Phép chia có dư và đồng dư', sub: 'thương, số dư và số dư của một số rất lớn',
  goals: [
    'Hiểu chính xác **thương** và **số dư** của phép chia, kể cả khi số bị chia là số âm.',
    'Biết phép `/` và `%` của C++ khác quy ước toán học ở chỗ nào, và cách sửa trong một dòng.',
    'Nắm khái niệm **đồng dư** a ≡ b (mod m) và các tính chất cộng, trừ, nhân của nó.',
    'Tính được số dư của một số có tới hàng triệu chữ số trong O(độ dài), không cần lưu cả số.',
  ],
  warmup: [
    'Hôm nay là **thứ Hai**. Cô giáo hỏi: "1000 ngày nữa là thứ mấy? Còn 100 ngày trước là thứ mấy?" Cả lớp đếm trên lịch một lúc rồi bỏ cuộc. Một bạn ngồi cuối lớp trả lời sau mười giây: "Chủ nhật, và thứ Bảy ạ."',
    'Bạn ấy không đếm từng ngày. Bạn ấy chỉ cần biết 1000 **chia cho 7 dư bao nhiêu**. Bài học này cho em cách nghĩ ấy, rồi dùng nó để tính số dư của một số dài một triệu chữ số, thứ mà không kiểu số nào của C++ chứa nổi.',
  ],
  body: [
    { h: 'Phép chia có dư' },
    'Chia 17 cái kẹo cho 5 bạn, mỗi bạn được 3 cái và còn thừa 2 cái. Ta viết 17 = 5 · 3 + 2: **3 là thương**, **2 là số dư**. Số dư phải nhỏ hơn số bạn: nếu còn thừa từ 5 cái trở lên thì chia thêm được một lượt nữa.',
    { box: 'def', title: 'ĐỊNH NGHĨA (PHÉP CHIA CÓ DƯ)', body: [
      'Với số nguyên a và số nguyên dương b, luôn tồn tại **duy nhất** một cặp số nguyên q, r sao cho:',
      { formula: 'a = b · q + r   và   0 ≤ r < b' },
      'q gọi là **thương**, r gọi là **số dư** của phép chia a cho b. Kí hiệu: q = ⌊a / b⌋ (phần nguyên dưới, tức số nguyên lớn nhất không vượt quá a / b), r = a mod b. Nếu r = 0 ta nói a **chia hết** cho b, viết b | a.',
    ] },
    'Trên trục số, phép chia có dư có một hình ảnh rất dễ nhớ: đi từ 0 theo những bước nhảy dài b, dừng ở **bội số của b gần a nhất mà không vượt quá a**. Số bước nhảy là q, đoạn còn lại tới a là r. Cách nhìn này đúng cả khi a âm: khi đó ta nhảy sang trái.',
    { fig: 'f1_trucso', w: 6.3, cap: 'Thương là số bước nhảy, số dư là đoạn còn lại; số dư luôn thuộc [0, b).' },
    { box: 'why', title: 'VÌ SAO CẶP (q, r) LUÔN TỒN TẠI VÀ DUY NHẤT?', body: [
      '**Tồn tại:** các bội số của b chia trục số thành những đoạn dài b liền nhau. Số a rơi vào đúng một đoạn [b · q, b · q + b), nên r = a − b · q thỏa 0 ≤ r < b.',
      '**Duy nhất:** giả sử a = b · q + r = b · q\' + r\' với 0 ≤ r, r\' < b. Trừ vế: b · (q − q\') = r\' − r. Vế phải nằm trong khoảng (−b, b) mà lại là bội của b, nên nó bằng 0. Vậy r = r\', q = q\'.',
    ] },

    { h: 'Phép chia trong C++ và số âm' },
    'Với a ≥ 0, phép `a / b` và `a % b` của C++ cho đúng q và r. Nhưng với a âm, C++ **làm tròn thương về phía 0** chứ không làm tròn xuống, nên số dư có thể âm:',
    { table: { cols: [1100, 1100, 1500, 1500, 1700, 1718], head: ['a', 'b', 'a / b (C++)', 'a % b (C++)', 'q (toán học)', 'r (toán học)'],
      rows: [['17', '5', '3', '2', '3', '2'], ['−17', '5', '**−3**', '**−2**', '−4', '3'], ['−7', '3', '**−2**', '**−1**', '−3', '2'], ['−6', '3', '−2', '0', '−2', '0']],
      aligns: [1, 1, 1, 1, 1, 1].map(() => 'center') } },
    'Quy tắc của C++ (từ chuẩn C++11): `a / b` bỏ phần thập phân (làm tròn về 0), còn `a % b` mang **dấu của a** và luôn thỏa `a == (a / b) * b + a % b`. Khi đề bài cần số dư theo nghĩa toán học (luôn không âm), hãy dùng công thức:',
    { formula: 'r = ((a % m) + m) % m' },
    'Nếu a % m đã không âm thì cộng m rồi lấy dư lần nữa không làm thay đổi gì; nếu a % m âm (thuộc khoảng (−m, 0)) thì cộng m đưa nó về đúng khoảng [0, m).',
    { box: 'example', title: 'VÍ DỤ: THỨ TRONG TUẦN', body: [
      'Đánh số thứ Hai = 0, thứ Ba = 1, ..., Chủ nhật = 6. Sau (hoặc trước) k ngày kể từ ngày t thì thứ là (t + k) mod 7, với k âm nghĩa là lùi về quá khứ.',
      { ul: ['1000 ngày nữa: 1000 = 7 · 142 + 6, ra 6: **Chủ nhật**.', '100 ngày trước: −100 = 7 · (−15) + 5, ra 5: **thứ Bảy**. Trong C++, `-100 % 7` bằng −2: phải sửa thành `((-100 % 7) + 7) % 7 = 5`.', '10^18^ ngày nữa: 10^18^ mod 7 = 1: **thứ Ba**. (Em sẽ tự tính được số này ở cuối bài.)'] },
    ] },

    { h: 'Đồng dư' },
    'Trên "đồng hồ 7 ngăn" ở Hình 1.2, các số 3, 10, 17, −4 đều rơi vào cùng ngăn 3. Chúng khác nhau, nhưng với câu hỏi "thứ mấy?" thì chúng **như nhau**. Toán học có một từ riêng cho chữ "như nhau" ấy.',
    { box: 'def', title: 'ĐỊNH NGHĨA (ĐỒNG DƯ)', body: [
      'Cho số nguyên dương m. Hai số nguyên a, b gọi là **đồng dư theo mô-đun m**, viết a ≡ b (mod m), nếu chúng có cùng số dư khi chia cho m; tương đương: **m chia hết a − b**.',
    ] },
    { fig: 'f1_dongho', w: 5.6, cap: 'Mỗi số nguyên rơi vào đúng một trong m "ngăn" 0, 1, ..., m − 1. Các số cùng ngăn thì đồng dư với nhau.' },
    'Sức mạnh của đồng dư nằm ở chỗ: khi chỉ quan tâm đến số dư, ta được phép **thay một số bằng số dư của nó** ở bất kì đâu trong một biểu thức chỉ có cộng, trừ, nhân.',
    { box: 'theorem', title: 'ĐỊNH LÍ (TÍNH CHẤT CỦA ĐỒNG DƯ)', body: [
      'Nếu a ≡ a\' (mod m) và b ≡ b\' (mod m) thì:',
      { ul: ['a + b ≡ a\' + b\' (mod m)', 'a − b ≡ a\' − b\' (mod m)', 'a · b ≡ a\' · b\' (mod m)', 'a^k^ ≡ a\'^k^ (mod m) với mọi số tự nhiên k.'] },
      'Dạng hay dùng trong lập trình: (a + b) mod m = ((a mod m) + (b mod m)) mod m, và (a · b) mod m = ((a mod m) · (b mod m)) mod m.',
    ] },
    { box: 'why', body: [
      'Đặt a = a\' + m · s và b = b\' + m · t. Khi đó a + b = (a\' + b\') + m · (s + t), nên a + b và a\' + b\' chênh nhau một bội của m. Với phép nhân: a · b = a\' · b\' + m · (a\' · t + b\' · s + m · s · t): lại chênh nhau một bội của m. Lũy thừa là nhân nhiều lần.',
    ] },
    { box: 'note', title: 'CẨN THẬN VỚI PHÉP CHIA', body: [
      'Đồng dư **không** cho phép chia hai vế một cách tùy tiện: 2 · 3 ≡ 2 · 8 (mod 10) (vì 6 và 16 cùng dư 6), nhưng 3 ≢ 8 (mod 10). Phép "chia" trong đồng dư cần một công cụ riêng là **nghịch đảo mô-đun**, em sẽ học ở Bài 10.',
    ] },

    { h: 'Bài toán SODU' },
    { problem: { code: 'SODU', statement: [
      'Cho một số nguyên không âm N rất lớn, có tới 10^6^ chữ số, và số nguyên dương m. Hãy tính số dư của N khi chia cho m.',
    ], input: 'Dòng đầu chứa N (không có chữ số 0 thừa ở đầu). Dòng thứ hai chứa m (1 ≤ m ≤ 10^9^).', output: 'Một số nguyên là N mod m.' } },
    { examples: 'SODU', explain: ['2026 = 7 · 289 + 3.', 'N có 30 chữ số, vượt xa giới hạn của mọi kiểu số nguyên trong C++.', 'Số bị chia nhỏ hơn số chia: thương bằng 0, số dư chính là N.'] },

    { h: 'Ý tưởng ngây thơ: Dựng lại cả số N' },
    'Cách tự nhiên nhất: đọc N, đổi ra một số nguyên, rồi lấy dư. Vì N được cho dưới dạng các chữ số nên ta đọc vào xâu và dựng lại N từ trái sang phải: mỗi chữ số mới làm N gấp 10 lần rồi cộng thêm chữ số đó.',
    { fig: 'f1_ngaytho', w: 2.7, cap: 'Sơ đồ khối của cách dựng lại cả số N.' },
    { file: 'SODU_ngaytho', title: 'SODU.CPP (ngây thơ): dựng lại N bằng unsigned long long' },
    { box: 'count', body: [
      'Chương trình chỉ có một vòng lặp qua các chữ số: O(L) phép tính với L là độ dài của N, rất nhanh. Vấn đề không nằm ở thời gian mà ở **độ lớn**: `unsigned long long` chỉ chứa được số nhỏ hơn 2^64^ ≈ 1,8 · 10^19^, tức khoảng 19 chữ số.',
    ] },
    { box: 'stuck', body: [
      'Với ví dụ 2 (30 chữ số), N bị **tràn số** từ chữ số thứ 20: máy tính âm thầm bỏ đi phần vượt quá 2^64^ và chương trình in ra một con số sai mà không báo lỗi gì. Một số có 10^6^ chữ số cần khoảng 3,3 triệu bit, không kiểu số nào của C++ chứa nổi. Nhưng ta có thật sự cần **cả** số N không? Đề bài chỉ hỏi số dư của nó.',
    ] },

    { h: 'Phá bế tắc: Chỉ giữ lại số dư' },
    { step: 'Viết N theo sơ đồ Horner' },
    'Cách dựng N từ trái sang phải chính là cách viết N theo **sơ đồ Horner**. Ví dụ với N = 2026:',
    { formula: '2026 = ((2 · 10 + 0) · 10 + 2) · 10 + 6' },
    'Biểu thức này chỉ gồm phép nhân và phép cộng. Theo định lí về tính chất đồng dư, ở **mỗi bước** ta được thay kết quả trung gian bằng số dư của nó khi chia cho m, mà số dư cuối cùng không đổi.',
    { step: 'Duy trì số dư của phần đầu' },
    'Gọi r là số dư của phần đầu của N (các chữ số đã đọc) khi chia cho m. Ban đầu chưa đọc chữ số nào: r = 0. Đọc thêm chữ số c thì phần đầu mới bằng (phần đầu cũ) · 10 + c, nên:',
    { formula: 'r ← (r · 10 + c) mod m' },
    'Vì luôn có 0 ≤ r < m nên r · 10 + c < 10 · m ≤ 10^10^: vừa vặn trong `long long`, không bao giờ tràn.',
    { step: 'Chạy tay với N = 2026, m = 7' },
    { fig: 'f1_horner', w: 6.0, cap: 'Mỗi chữ số mới đẩy r sang một giá trị mới; r luôn nhỏ hơn 7.' },
    { table: { cols: [1500, 1700, 2900, 2518], head: ['Chữ số đọc', 'Phần đầu của N', 'r · 10 + c', 'r mới (mod 7)'],
      rows: [['2', '2', '0 · 10 + 2 = 2', '2'], ['0', '20', '2 · 10 + 0 = 20', '20 mod 7 = **6**'], ['2', '202', '6 · 10 + 2 = 62', '62 mod 7 = **6**'], ['6', '2026', '6 · 10 + 6 = 66', '66 mod 7 = **3**']],
      aligns: ['center', 'center', 'center', 'center'] } },
    'Kiểm tra lại cột thứ hai: 20 mod 7 = 6, 202 = 7 · 28 + 6, 2026 = 7 · 289 + 3. Đúng như bảng: r luôn là số dư của phần đầu, dù ta không hề lưu phần đầu ấy.',
    { box: 'why', body: [
      '**Bất biến:** sau khi đọc k chữ số đầu, r là số dư của số tạo bởi k chữ số đó khi chia cho m.',
      'Đúng khi k = 0 (r = 0). Giả sử đúng tới k, gọi phần đầu là A, ta có A ≡ r (mod m). Phần đầu mới là A · 10 + c ≡ r · 10 + c (mod m) theo tính chất đồng dư, nên (r · 10 + c) mod m chính là số dư của phần đầu mới. Khi k = L, phần đầu chính là N.',
    ] },
    { step: 'Chương trình' },
    { fig: 'f1_toiuu', w: 2.7, cap: 'Sơ đồ khối của cách chỉ giữ số dư.' },
    { file: 'SODU', title: 'SODU.CPP: sơ đồ Horner, chỉ giữ số dư' },
    { box: 'count', body: ['Mỗi chữ số tốn một phép nhân, một phép cộng, một phép lấy dư: O(L) thời gian và O(1) bộ nhớ ngoài xâu đầu vào. Với L = 10^6^, chương trình chạy chưa tới một phần trăm giây.'] },
  ],
  ext: [
    { sub: 'Mở rộng 1: Dấu hiệu chia hết cho 3, 9 và 11' },
    'Vì 10 ≡ 1 (mod 9), mọi lũy thừa 10^k^ ≡ 1 (mod 9). Do đó một số đồng dư với **tổng các chữ số** của nó theo mô-đun 9 (và theo mô-đun 3). Đây là lí do của dấu hiệu chia hết cho 3 và 9 em đã học ở tiểu học. Tương tự, 10 ≡ −1 (mod 11), nên 10^k^ ≡ (−1)^k^ (mod 11): một số đồng dư với **tổng đan dấu** các chữ số của nó tính từ hàng đơn vị. Ví dụ 918 082: 2 − 8 + 0 − 8 + 1 − 9 = −22, chia hết cho 11, nên 918 082 chia hết cho 11.',
    { sub: 'Mở rộng 2: Số dư của tổng và tích rất dài' },
    'Khi cần (a~1~ + a~2~ + ... + a~n~) mod m hay (a~1~ · a~2~ · ... · a~n~) mod m, hãy lấy dư **sau mỗi phép tính**, đúng như trong SODU. Với tích, nhớ rằng hai số nhỏ hơn m ≤ 10^9^ nhân nhau được số tới 10^18^: vẫn vừa `long long`. Khi m tới 10^18^, tích hai số dư có thể tới 10^36^: phải dùng `__int128` hoặc phép nhân đặc biệt ở Bài 9.',
    { sub: 'Mở rộng 3: Chữ số tận cùng và tính tuần hoàn' },
    'Chữ số tận cùng của a là a mod 10. Các lũy thừa 2^1^, 2^2^, 2^3^, ... có chữ số tận cùng 2, 4, 8, 6, 2, 4, 8, 6, ...: lặp lại với **chu kì** 4, vì chỉ có hữu hạn số dư nên dãy số dư sớm muộn phải lặp. Ví dụ 2026 mod 4 = 2, nên 2^2026^ có chữ số tận cùng giống 2^2^, tức là **4**.',
  ],
  traps: [
    '**Số dư âm:** trong C++, `-7 % 3` bằng −1, không phải 2. Dùng `((a % m) + m) % m` khi a có thể âm.',
    '**Tràn số trung gian:** dùng `int` cho r khi m = 10^9^ thì r · 10 + c có thể tới khoảng 10^10^ > 2^31^. Hãy dùng `long long`.',
    '**Lấy dư quá muộn:** cộng dồn cả dãy rồi mới lấy dư thì tổng đã tràn từ trước. Lấy dư ngay sau mỗi phép tính.',
    '**Chia hai vế của đồng dư:** 2 · 3 ≡ 2 · 8 (mod 10) nhưng 3 ≢ 8 (mod 10). Đừng "giản ước" khi chưa học Bài 10.',
    '**Đọc N vào kiểu số:** `cin >> N` với N 30 chữ số không báo lỗi rõ ràng, chỉ cho kết quả sai. Đọc vào xâu.',
  ],
  remember: [
    'a = b · q + r với 0 ≤ r < b; q = ⌊a / b⌋ là bội số lớn nhất của b không vượt quá a (tính theo số lần b).',
    'C++ làm tròn thương về 0; số dư theo nghĩa toán học là `((a % m) + m) % m`.',
    'a ≡ b (mod m) khi và chỉ khi m | (a − b). Đồng dư giữ nguyên qua cộng, trừ, nhân, lũy thừa; không giữ qua phép chia.',
    'Sơ đồ Horner: r ← (r · 10 + c) mod m cho số dư của số rất lớn trong O(độ dài).',
  ],
  practice: [
    ['1.1', 'NGÀY TRONG TUẦN', 'Thứ của ngày cách hôm nay k ngày, |k| ≤ 10^18^, k có thể âm. Số dư không âm.'],
    ['1.2', 'CHỮ SỐ CUỐI', 'Chữ số tận cùng của a^b^ với a, b cho dưới dạng xâu rất dài: dùng tính tuần hoàn (chu kì 4) và số dư của số lớn.'],
    ['1.3', 'VIẾT LIỀN', 'Số dư khi chia cho m của số 123456789101112...n (viết liền 1..n): sơ đồ Horner theo từng số, nhân với 10^(số chữ số)^.'],
  ],
  quiz: [
    ['Theo quy ước toán học, (−23) mod 5 bằng bao nhiêu? Trong C++, `-23 % 5` cho kết quả gì?', 'Đáp số: 2 và −3'],
    ['Hôm nay là thứ Tư. Sau 2026 ngày là thứ mấy?', 'Đáp số: 2026 mod 7 = 3, nên là thứ Bảy'],
    ['Không dùng máy tính, tìm số dư của 123 456 789 khi chia cho 9 và khi chia cho 11.', 'Đáp số: tổng chữ số 45 nên dư 0 khi chia cho 9; tổng đan dấu 9 − 8 + 7 − 6 + 5 − 4 + 3 − 2 + 1 = 5 nên dư 5 khi chia cho 11'],
    ['Chạy tay SODU với N = 10^18^ (chữ số 1 và 18 chữ số 0), m = 7. Vì sao chỉ cần để ý rằng 10 ≡ 3 và 3^6^ ≡ 1 (mod 7)?', 'Đáp số: 10^18^ ≡ 3^18^ = (3^6^)^3^ ≡ 1 (mod 7)'],
  ],
};

module.exports = {
  no: 1, title: 'CHIA HẾT VÀ ƯỚC SỐ',
  intro: [
    'Mọi thứ trong số học bắt đầu từ một phép tính em đã biết từ năm lớp 3: phép chia có dư. Từ đó nảy ra những câu hỏi rất "Tin học": số dư của một số dài một triệu chữ số là bao nhiêu? Một số có bao nhiêu ước? Làm sao tìm ước chung lớn nhất của hai số cỡ 10^18^ trong nháy mắt? Phương trình 3x + 5y = 2026 có nghiệm nguyên không?',
    'Chương này xây nền móng cho cả cuốn sách: đồng dư, ước số, ước chung lớn nhất và thuật toán Euclid. Thuật toán Euclid ra đời hơn 2300 năm trước, nhưng đến nay vẫn là một trong những thuật toán được dùng nhiều nhất trong lập trình thi đấu.',
  ],
  lessons: [L1],
};
