// SỐ HỌC — TẬP 1. CHƯƠNG 4. TỔ HỢP VÀ ĐẾM
const C3 = (n) => n.map(() => 'center');

// ============================================================ BÀI 13
const L13 = {
  no: 13, title: 'Tổ hợp và hệ số nhị thức', sub: 'đếm số cách chọn và tính C(n, k) mod p thật nhanh',
  goals: [
    'Nắm **quy tắc nhân**, hoán vị, chỉnh hợp, tổ hợp và hiểu vì sao C(n, k) = n! / (k! · (n − k)!).',
    'Chứng minh được **hằng đẳng thức Pascal** C(n, k) = C(n − 1, k − 1) + C(n − 1, k) bằng một lập luận đếm.',
    'Biết vì sao không thể chia thẳng giai thừa theo mô-đun, và dùng **nghịch đảo giai thừa** để trả lời mỗi truy vấn C(n, k) mod p trong O(1).',
    'Chọn đúng công cụ cho từng giới hạn: tam giác Pascal, giai thừa, nhân dần, định lí Lucas.',
  ],
  warmup: [
    'Lớp em có 30 bạn. Cô giáo cần chọn **3 bạn đi thi Tin học**. Bạn Minh nhẩm: "Bạn thứ nhất có 30 cách chọn, bạn thứ hai 29, bạn thứ ba 28, vậy 30 · 29 · 28 = 24 360 cách." Bạn Lan cãi: "Chọn An, Bình, Chi hay chọn Chi, An, Bình thì vẫn là một đội thôi!" Ai đúng?',
    'Cả hai đều có lí, chỉ là hai câu hỏi khác nhau: Minh đếm **có thứ tự** (thi đấu theo lượt 1, 2, 3), Lan đếm **không thứ tự** (chỉ cần biết đội gồm những ai). Bài học này phân biệt rõ hai cách đếm ấy, rồi trả lời một câu hỏi rất "Tin học": làm sao tính số cách chọn k trong n vật khi n tới một triệu, cho một trăm nghìn câu hỏi, mỗi câu trong nháy mắt?',
  ],
  body: [
    { h: 'Quy tắc nhân, hoán vị và giai thừa' },
    'Mọi phép đếm trong bài này dựa trên một quy tắc rất đơn giản: nếu một việc gồm **hai bước liên tiếp**, bước đầu có a cách làm và **với mỗi cách** của bước đầu, bước sau có b cách làm, thì cả việc có **a · b** cách. Quy tắc mở rộng cho nhiều bước: số cách bằng tích số cách của từng bước.',
    'Bạn Minh trong phần khởi động đã dùng đúng quy tắc này: chọn người thi lượt 1 (30 cách), rồi lượt 2 (còn 29 cách), rồi lượt 3 (còn 28 cách), được 30 · 29 · 28 = 24 360. Cách đếm có thứ tự như vậy có tên riêng.',
    { box: 'def', title: 'ĐỊNH NGHĨA (HOÁN VỊ, CHỈNH HỢP)', body: [
      { ul: [
        'Một **hoán vị** của n vật là một cách xếp cả n vật thành một hàng. Số hoán vị là n! = 1 · 2 · ... · n (đọc là "n giai thừa"); quy ước 0! = 1.',
        'Một **chỉnh hợp chập k** của n vật là một cách chọn k vật **có thứ tự**. Số chỉnh hợp là A(n, k) = n · (n − 1) · ... · (n − k + 1) = n! / (n − k)!.',
      ] },
    ] },
    'Giai thừa tăng **cực nhanh**. Bảng dưới cho thấy 20! vẫn vừa kiểu `long long` (giới hạn khoảng 9,2 · 10^18^), nhưng 21! đã vượt cả `unsigned long long`. Đây là lí do mọi bài đếm trong thi đấu đều yêu cầu in kết quả **theo mô-đun** một số nguyên tố, thường là p = 10^9^ + 7.',
    { table: { cols: [900, 2300, 900, 4518], head: ['n', 'n!', 'n', 'n!'],
      rows: [['0', '1', '6', '720'], ['1', '1', '7', '5 040'], ['2', '2', '8', '40 320'], ['3', '6', '9', '362 880'], ['4', '24', '10', '3 628 800'], ['5', '120', '20', '2 432 902 008 176 640 000 (vừa `long long`)'], ['', '', '21', '51 090 942 171 709 440 000 (**tràn** 2^64^)']],
      aligns: ['center', 'center', 'center', 'center'] } },

    { h: 'Tổ hợp và tam giác Pascal' },
    'Bây giờ đến câu hỏi của bạn Lan: chỉ quan tâm **đội gồm những ai**, không quan tâm thứ tự.',
    { box: 'def', title: 'ĐỊNH NGHĨA (TỔ HỢP)', body: [
      'Một **tổ hợp chập k** của n vật là một tập con gồm k vật (không có thứ tự). Số tổ hợp kí hiệu là C(n, k) (sách giáo khoa viết C~n~^k^, đọc là "n chọn k"), còn gọi là **hệ số nhị thức**. Quy ước C(n, k) = 0 khi k < 0 hoặc k > n.',
      { formula: 'C(n, k) = n! / (k! · (n − k)!)' },
    ] },
    { box: 'why', title: 'VÌ SAO CÔNG THỨC ĐÚNG?', body: [
      'Đếm số chỉnh hợp A(n, k) theo **hai bước**: bước 1 chọn tập k vật (C(n, k) cách), bước 2 xếp thứ tự k vật đó (k! cách). Theo quy tắc nhân, A(n, k) = C(n, k) · k!, nên C(n, k) = A(n, k) / k! = n! / (k! · (n − k)!).',
      'Với lớp 30 bạn: mỗi đội 3 bạn được Minh đếm đúng 3! = 6 lần (6 thứ tự), nên số đội là 24 360 / 6 = **4 060**. Cả Minh và Lan đều đúng với câu hỏi của mình.',
    ] },
    { box: 'example', title: 'VÍ DỤ: XỔ SỐ 6/45', body: [
      'Một vé xổ số chọn 6 số khác nhau trong các số 1..45, thứ tự không quan trọng. Số vé khác nhau là C(45, 6) = 45 · 44 · 43 · 42 · 41 · 40 / 720 = **8 145 060**. Mua một vé, khả năng trúng giải đặc biệt chỉ là 1 phần 8 triệu.',
    ] },
    'Công thức giai thừa đẹp nhưng chưa cho ta thấy **cấu trúc** của các số C(n, k). Hãy xét một ví dụ nhỏ: chọn 2 bạn trong 5 bạn đánh số 1..5. Ta chia các cách chọn thành hai nhóm theo câu hỏi "bạn số 5 có được chọn không?".',
    { fig: 'f13_chon', w: 5.9, cap: 'Mười cách chọn 2 trong 5 bạn, chia theo bạn số 5: có (4 cách) hoặc không (6 cách).' },
    'Nếu bạn 5 được chọn, ta chỉ còn chọn thêm 1 bạn trong 4 bạn kia: C(4, 1) = 4 cách. Nếu bạn 5 không được chọn, ta phải chọn đủ 2 bạn trong 4 bạn kia: C(4, 2) = 6 cách. Hai nhóm không giao nhau và phủ hết mọi cách, nên C(5, 2) = 4 + 6 = 10. Lập luận này đúng với mọi n và k.',
    { box: 'theorem', title: 'ĐỊNH LÍ (HẰNG ĐẲNG THỨC PASCAL)', body: [
      'Với mọi n ≥ 1 và 1 ≤ k ≤ n − 1:',
      { formula: 'C(n, k) = C(n − 1, k − 1) + C(n − 1, k)' },
      'cùng với hai "đầu mút" C(n, 0) = C(n, n) = 1 và tính đối xứng C(n, k) = C(n, n − k).',
    ] },
    { box: 'why', body: [
      'Xét một vật cố định, chẳng hạn vật thứ n. Mỗi tập con k phần tử **hoặc chứa** vật n (khi đó k − 1 phần tử còn lại chọn trong n − 1 vật: C(n − 1, k − 1) cách), **hoặc không chứa** vật n (cả k phần tử chọn trong n − 1 vật: C(n − 1, k) cách). Hai trường hợp loại trừ nhau, nên cộng lại.',
      'Đối xứng: chọn k vật để **lấy** cũng chính là chọn n − k vật để **bỏ lại**, hai việc tương ứng một-một.',
    ] },
    'Xếp các số C(n, k) thành hàng thứ n (k = 0, 1, ..., n), ta được **tam giác Pascal**: mỗi số bên trong bằng tổng hai số đứng ngay trên nó.',
    { fig: 'f13_pascal', w: 6.0, cap: 'Tam giác Pascal tới hàng 8. Mỗi ô bên trong bằng tổng hai ô phía trên; cột phải là tổng mỗi hàng.' },
    { box: 'note', title: 'NHỊ THỨC NEWTON VÀ TỔNG MỖI HÀNG', body: [
      'Khai triển (a + b)^n^ = (a + b)(a + b)...(a + b): mỗi số hạng a^k^b^n−k^ xuất hiện đúng bằng số cách chọn k thừa số đóng góp a, tức C(n, k) lần. Vậy (a + b)^n^ = Σ C(n, k) · a^k^ · b^n−k^, đó là lí do C(n, k) được gọi là **hệ số nhị thức**. Thay a = b = 1: tổng hàng thứ n bằng **2^n^** (số tập con của tập n phần tử). Thay a = 1, b = −1: tổng đan dấu của mỗi hàng (n ≥ 1) bằng **0**; em sẽ dùng điều này ở Bài 14.',
    ] },

    { h: 'Bài toán TOHOP' },
    { problem: { code: 'TOHOP', statement: [
      'Cho Q truy vấn, mỗi truy vấn gồm hai số nguyên n, k. Với mỗi truy vấn, hãy in C(n, k) mod (10^9^ + 7); nếu k > n thì in 0.',
    ], input: 'Dòng đầu chứa Q (1 ≤ Q ≤ 10^5^). Mỗi dòng trong Q dòng sau chứa n, k (0 ≤ n, k ≤ 10^6^).', output: 'Q dòng, mỗi dòng là đáp số của một truy vấn.' } },
    { examples: 'TOHOP', explain: ['C(5, 2) = 10, C(6, 3) = 20, C(10, 0) = 1; k > n nên C(3, 5) = 0.', 'C(10^6^, 5 · 10^5^) có tới 301 027 chữ số, ta chỉ in số dư. C(n, 1) = C(n, n − 1) = n.', 'Số vé xổ số 6/45. C(0, 0) = 1: chỉ có một cách chọn "không gì cả" từ tập rỗng.'] },

    { h: 'Ý tưởng ngây thơ: Dựng cả tam giác Pascal' },
    'Hằng đẳng thức Pascal chỉ dùng **phép cộng**, mà phép cộng thì lấy dư thoải mái (Bài 1). Vậy ta dựng tam giác Pascal theo mô-đun p, từ hàng 0 đến hàng mx là n lớn nhất trong các truy vấn, rồi tra bảng. Không có phép chia nào, không cần biết p có nguyên tố hay không.',
    { fig: 'f13_ngaytho', w: 2.9, cap: 'Sơ đồ khối của cách dựng tam giác Pascal.' },
    { file: 'TOHOP_ngaytho', title: 'TOHOP.CPP (ngây thơ): tam giác Pascal theo mô-đun' },
    { box: 'count', body: [
      'Hàng n có n + 1 ô, mỗi ô một phép cộng, nên dựng tới hàng mx tốn khoảng mx^2^ / 2 phép cộng và **cùng chừng ấy ô nhớ**. Với mx = 5000: 12,5 triệu ô, chạy tốt. Với mx = 10^6^: khoảng 5 · 10^11^ ô, tức **2 TB** bộ nhớ nếu mỗi ô 4 byte, và hàng trăm giây tính toán.',
    ] },
    { box: 'stuck', body: [
      'Tam giác Pascal tính **tất cả** các C(n, k) trong khi ta chỉ cần 10^5^ giá trị. Công thức n! / (k! · (n − k)!) thì chỉ cần ba giai thừa, và mọi giai thừa tới 10^6^ có thể tính sẵn trong O(n). Nhưng công thức có **phép chia**, mà Bài 1 đã cảnh báo: đồng dư không giữ qua phép chia. 720 mod 7 = 6 và 6 · 6 mod 7 = 1, ta không thể "chia 6 cho 1" để ra C(6, 3) = 20 được.',
    ] },

    { h: 'Phá bế tắc: Giai thừa và nghịch đảo giai thừa' },
    { step: 'Đổi phép chia thành phép nhân với nghịch đảo' },
    'Ở Bài 10 em đã biết: khi p nguyên tố và b không chia hết cho p, tồn tại duy nhất **nghịch đảo** b^−1^ (mod p) thỏa b · b^−1^ ≡ 1, và theo định lí Fermat nhỏ b^−1^ ≡ b^p−2^ (mod p). Chia cho b theo mô-đun p nghĩa là nhân với b^−1^. Ví dụ 2^−1^ ≡ 500 000 004 vì 2 · 500 000 004 = 1 000 000 008 ≡ 1 (mod 10^9^ + 7).',
    'Với p = 10^9^ + 7 > 10^6^ ≥ n, các thừa số 1, 2, ..., n đều nhỏ hơn p nên **không chia hết cho p**, và k!, (n − k)! có nghịch đảo. Đặt fact[i] = i! mod p và ifact[i] = (i!)^−1^ mod p, ta có:',
    { formula: 'C(n, k) ≡ fact[n] · ifact[k] · ifact[n − k]   (mod p)' },
    { step: 'Tính giai thừa đi xuôi, nghịch đảo đi ngược' },
    'fact[i] = fact[i − 1] · i mod p: dễ. Còn ifact[i], nếu dùng lũy thừa nhanh cho từng i thì tốn N · log p, khoảng 3 · 10^7^ phép nhân, cũng được, nhưng có một mẹo đẹp hơn nhiều: chỉ cần **một** lần lũy thừa cho ifact[N], rồi **đi ngược** về 0.',
    { formula: 'ifact[i − 1] = ifact[i] · i   (mod p)' },
    { fig: 'f13_xich', w: 6.3, cap: 'Giai thừa đi xuôi (nhân thêm i); nghịch đảo giai thừa đi ngược (cũng nhân với i), chỉ một lần lũy thừa.' },
    { box: 'why', body: [
      'Vì i! = (i − 1)! · i, nên 1 / (i − 1)! = i / i! = (1 / i!) · i. Viết theo mô-đun: ifact[i] · i · fact[i − 1] ≡ ifact[i] · fact[i] ≡ 1 (mod p), tức ifact[i] · i đúng là nghịch đảo của fact[i − 1]. Theo tính duy nhất của nghịch đảo, ifact[i − 1] = ifact[i] · i mod p.',
    ] },
    { step: 'Chạy tay với p = 10^9^ + 7' },
    'Bảng dưới được sinh bằng chính thuật toán: fact đi xuôi từ 0 đến 6; ifact[6] = 720^p−2^ mod p = 301 388 891, rồi ifact đi ngược. Cột cuối kiểm tra fact[i] · ifact[i] ≡ 1.',
    { table: { cols: [900, 2000, 3000, 2718], head: ['i', 'fact[i]', 'ifact[i]', 'fact[i] · ifact[i] mod p'],
      rows: [['0', '1', '1', '1'], ['1', '1', '1', '1'], ['2', '2', '500 000 004', '1'], ['3', '6', '166 666 668', '1'], ['4', '24', '41 666 667', '1'], ['5', '120', '808 333 339', '1'], ['6', '720', '**301 388 891** (lũy thừa)', '1']],
      aligns: C3([1, 1, 1, 1]) } },
    'Trả lời các truy vấn của ví dụ 1:',
    { table: { cols: [1300, 3000, 3000, 1318], head: ['(n, k)', 'fact[n] · ifact[k] mod p', '· ifact[n − k] mod p', 'Đáp số'],
      rows: [['(5, 2)', '120 · 500 000 004 → 60', '60 · 166 666 668 → 10', '**10**'], ['(6, 3)', '720 · 166 666 668 → 120', '120 · 166 666 668 → 20', '**20**'], ['(10, 0)', '3 628 800 · 1 → 3 628 800', '· ifact[10] → 1', '**1**'], ['(3, 5)', 'k > n', '', '**0**']],
      aligns: C3([1, 1, 1, 1]) } },
    'Để ý dòng đầu: nhân 120 với nghịch đảo của 2 ra 60, đúng như 120 / 2; nhân tiếp với nghịch đảo của 6 ra 10, đúng như 60 / 6. Các con số nghịch đảo trông "kì quặc" nhưng chúng cư xử y như phân số.',
    { step: 'Chương trình' },
    { fig: 'f13_toiuu', w: 3.0, cap: 'Sơ đồ khối của cách dùng giai thừa và nghịch đảo giai thừa.' },
    { file: 'TOHOP', title: 'TOHOP.CPP: giai thừa và nghịch đảo giai thừa' },
    { box: 'count', body: [
      'Chuẩn bị: N phép nhân cho fact, một lần lũy thừa (khoảng 2 · 30 phép nhân), N phép nhân cho ifact: tổng O(N + log p) với N = 10^6^. Mỗi truy vấn: 2 phép nhân, O(1). Cả chương trình khoảng 2 · 10^6^ + 2 · 10^5^ phép nhân, chạy dưới 0,1 giây; bộ nhớ hai mảng 10^6^ số `long long`, 16 MB.',
    ] },
    { table: { cols: [2600, 3000, 3018], head: ['', 'Tam giác Pascal', 'Giai thừa + nghịch đảo'],
      rows: [['Thời gian chuẩn bị', 'O(n^2^): 5 · 10^11^', 'O(n + log p): 2 · 10^6^'], ['Bộ nhớ', 'O(n^2^): 2 TB', 'O(n): 16 MB'], ['Mỗi truy vấn', 'O(1)', 'O(1)'], ['Yêu cầu mô-đun', 'bất kì', 'p nguyên tố, p > n']],
      aligns: C3([1, 1, 1]) } },
  ],
  ext: [
    { sub: 'Mở rộng 1: Bài toán chia kẹo của Euler' },
    'Có bao nhiêu cách chia 10 cái kẹo giống nhau cho 3 bạn An, Bình, Chi (bạn nào cũng có thể không được cái nào)? Mẹo của Euler: xếp 10 cái kẹo thành hàng và đặt thêm **2 vạch ngăn**. Kẹo trước vạch thứ nhất là của An, giữa hai vạch là của Bình, sau vạch thứ hai là của Chi. Mỗi cách chia ứng với đúng một cách chọn 2 vị trí làm vạch trong 12 vị trí.',
    { fig: 'f13_keo', w: 6.0, cap: 'Mỗi cách chia kẹo là một cách đặt 2 vạch giữa 10 viên kẹo.' },
    { box: 'theorem', title: 'ĐỊNH LÍ (CHIA KẸO)', body: [
      'Số nghiệm nguyên **không âm** của x~1~ + x~2~ + ... + x~k~ = n là C(n + k − 1, k − 1). Số nghiệm nguyên **dương** (mỗi bạn ít nhất một kẹo) là C(n − 1, k − 1): phát trước mỗi bạn một cái rồi chia n − k cái còn lại.',
    ] },
    'Với 10 kẹo, 3 bạn: C(12, 2) = 66 cách; nếu mỗi bạn ít nhất một cái: C(9, 2) = 36 cách. Cả hai đều trả lời được bằng TOHOP.',
    { sub: 'Mở rộng 2: n rất lớn, k nhỏ: nhân dần' },
    'Nếu n tới 10^18^ nhưng k chỉ tới 10^6^, ta không thể lập bảng giai thừa tới n. Khi đó dùng trực tiếp C(n, k) = n · (n − 1) · ... · (n − k + 1) / k!: tử số là tích k thừa số (lấy dư từng thừa số), mẫu số k! có nghịch đảo vì k < p. Công thức đúng cả khi n ≥ p, vì đẳng thức C(n, k) · k! = n(n − 1)...(n − k + 1) là đẳng thức số nguyên. Mỗi truy vấn tốn O(k + log p).',
    { file: 'TOHOP_nhandan', title: 'TOHOP_NHANDAN.CPP: C(n, k) bằng tích k thừa số' },
    { sub: 'Mở rộng 3: Định lí Lucas khi p nhỏ' },
    'Khi mô-đun p là số nguyên tố **nhỏ** (ví dụ p = 7 hay p = 10 007) mà n lớn hơn p, cách giai thừa hỏng vì n! chia hết cho p. Định lí Lucas cứu ta: viết n và k trong **hệ cơ số p**.',
    { box: 'theorem', title: 'ĐỊNH LÍ (LUCAS)', body: [
      'Nếu n = (n~t~ ... n~1~ n~0~)~p~ và k = (k~t~ ... k~1~ k~0~)~p~ là biểu diễn cơ số p (p nguyên tố) thì:',
      { formula: 'C(n, k) ≡ C(n~t~, k~t~) · ... · C(n~1~, k~1~) · C(n~0~, k~0~)   (mod p)' },
      'trong đó C(a, b) = 0 nếu b > a. Mỗi thừa số có a, b < p, tính bằng giai thừa tới p − 1.',
    ] },
    'Ví dụ: C(1000, 500) mod 7. Ta có 1000 = (2626)~7~, 500 = (1313)~7~, nên C(1000, 500) ≡ C(2, 1) · C(6, 3) · C(2, 1) · C(6, 3) = 2 · 20 · 2 · 20 = 1600 ≡ **4** (mod 7). Với n = 10^18^ chỉ có khoảng log~p~ n chữ số, nên mỗi truy vấn rất nhanh sau O(p) chuẩn bị.',
    { file: 'TOHOP_lucas', title: 'TOHOP_LUCAS.CPP: định lí Lucas, đọc n, k, p' },
    { table: { cols: [2400, 2900, 3318], head: ['Cách tính C(n, k) mod m', 'Dùng khi', 'Độ phức tạp'],
      rows: [['Tam giác Pascal', 'n ≤ khoảng 5000, m bất kì', 'O(n^2^) chuẩn bị, O(1) mỗi truy vấn'], ['Giai thừa + nghịch đảo', 'n ≤ 10^7^, m = p nguyên tố > n', 'O(n + log p) chuẩn bị, O(1)'], ['Nhân dần', 'n tới 10^18^, k nhỏ, p nguyên tố > k', 'O(k + log p) mỗi truy vấn'], ['Định lí Lucas', 'p nguyên tố nhỏ, n tới 10^18^', 'O(p) chuẩn bị, O(log~p~ n)']],
      aligns: ['left', 'left', 'left'] } },
    { sub: 'Mở rộng 4: Số Catalan' },
    'Có bao nhiêu dãy gồm n cặp ngoặc "đúng" (mỗi tiền tố có số ngoặc mở không ít hơn số ngoặc đóng)? Với n = 3 có 5 dãy: ((())), (()()), (())(), ()(()), ()()(). Đáp số tổng quát là **số Catalan** C~n~ = C(2n, n) / (n + 1) = C(2n, n) − C(2n, n + 1); dãy bắt đầu 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862. Số Catalan cũng đếm số cây nhị phân n nút, số cách chia đa giác lồi n + 2 đỉnh thành tam giác... Với TOHOP em tính được C~n~ mod p trong O(1): fact[2n] · ifact[n] · ifact[n + 1].',
  ],
  traps: [
    '**Chia thẳng theo mô-đun:** `fact[n] / (fact[k] * fact[n-k]) % p` cho kết quả vô nghĩa, vì fact[] đã là số dư. Phải nhân với nghịch đảo.',
    '**Quên kiểm tra k > n hoặc k < 0:** truy cập ifact[n − k] với chỉ số âm gây lỗi bộ nhớ. Luôn trả 0 trước.',
    '**Tràn khi nhân ba số:** `fact[n] * ifact[k] * ifact[n-k] % p` tràn `long long` vì tích ba số cỡ 10^9^ tới 10^27^. Lấy dư sau **mỗi** phép nhân.',
    '**Mô-đun không nguyên tố hoặc p ≤ n:** khi đó k! có thể không có nghịch đảo. Dùng tam giác Pascal (n nhỏ) hoặc Lucas (p nhỏ).',
    '**Nhầm có thứ tự và không thứ tự:** chọn đội thì dùng C(n, k), xếp lượt thi thì dùng A(n, k) = C(n, k) · k!.',
  ],
  remember: [
    'C(n, k) = n! / (k! · (n − k)!) = số tập con k phần tử của tập n phần tử; C(n, k) = 0 khi k < 0 hoặc k > n.',
    'Hằng đẳng thức Pascal C(n, k) = C(n − 1, k − 1) + C(n − 1, k): chứng minh bằng cách xét một phần tử có được chọn hay không.',
    'Với p nguyên tố > n: C(n, k) ≡ fact[n] · ifact[k] · ifact[n − k]; ifact[N] = fact[N]^p−2^, ifact[i − 1] = ifact[i] · i.',
    'Chia kẹo: số nghiệm không âm của x~1~ + ... + x~k~ = n là C(n + k − 1, k − 1).',
    'p nhỏ, n lớn: định lí Lucas, tách n, k theo cơ số p.',
  ],
  practice: [
    ['13.1', 'CHIA KẸO', 'Đếm số cách chia n kẹo cho k bạn (có/không yêu cầu mỗi bạn ít nhất một cái), mod 10^9^ + 7: chia kẹo Euler + TOHOP.'],
    ['13.2', 'ĐƯỜNG ĐI TRÊN LƯỚI', 'Số đường đi từ (0, 0) tới (m, n) chỉ đi phải/lên là C(m + n, n); có một ô cấm thì trừ số đường đi qua ô đó (quy tắc nhân).'],
    ['13.3', 'TỔ HỢP KHỔNG LỒ', 'C(n, k) mod p với n, k ≤ 10^18^, p nguyên tố ≤ 10^5^, nhiều truy vấn: định lí Lucas.'],
  ],
  quiz: [
    ['Có bao nhiêu cách chọn 3 bạn trong 30 bạn làm đội tuyển? Bao nhiêu cách nếu 3 bạn thi theo lượt 1, 2, 3?', 'Đáp số: C(30, 3) = 4060 và A(30, 3) = 24 360'],
    ['Từ hàng 7 của tam giác Pascal (1, 7, 21, 35, 35, 21, 7, 1), hãy tính C(8, 3) và tổng các số ở hàng 8.', 'Đáp số: C(8, 3) = 21 + 35 = 56; tổng hàng 8 là 2^8^ = 256'],
    ['Chia 10 cái kẹo giống nhau cho 3 bạn sao cho bạn nào cũng có ít nhất 1 cái. Có bao nhiêu cách?', 'Đáp số: C(9, 2) = 36'],
    ['Dùng định lí Lucas, tính C(1000, 500) mod 7 (gợi ý 1000 = (2626)~7~, 500 = (1313)~7~).', 'Đáp số: 2 · 20 · 2 · 20 = 1600 ≡ 4 (mod 7)'],
  ],
  algos: [
    ['Tam giác Pascal C(n, k) mod m', 'O(n²)'],
    ['C(n, k) mod p bằng giai thừa và nghịch đảo giai thừa', 'O(n + log p) chuẩn bị, O(1) mỗi truy vấn'],
    ['C(n, k) mod p nhân dần (n lớn, k nhỏ)', 'O(k + log p)'],
    ['Định lí Lucas (p nguyên tố nhỏ)', 'O(p + log~p~ n)'],
  ],
};

// ============================================================ BÀI 14
const L14 = {
  no: 14, title: 'Nguyên lí bù trừ', sub: 'đếm hợp của nhiều tập hợp: cộng, trừ, cộng xen kẽ',
  goals: [
    'Phát biểu và chứng minh **nguyên lí bù trừ** cho 2, 3 và k tập hợp.',
    'Đếm số bội số trong [1, N] bằng ⌊N / a⌋, biết vì sao bội chung của a, b là bội của **lcm(a, b)** chứ không phải của a · b.',
    'Duyệt 2^k^ tập con bằng **mặt nạ bit**, tính lcm của mỗi tập con chỉ bằng một phép gcd, và **chặn tràn số** khi lcm vượt N.',
    'Áp dụng bù trừ để đếm số nguyên tố cùng nhau với n và số hoán vị không điểm cố định.',
  ],
  warmup: [
    'Lớp 10 Tin có 100 học sinh. Thống kê cho thấy 60 em thích Toán, 50 em thích Tin, và 30 em thích cả hai. Hỏi có bao nhiêu em thích ít nhất một trong hai môn? Cộng 60 + 50 = 110 thì vượt cả sĩ số! Lỗi ở đâu? Ba mươi em thích cả hai đã bị **đếm hai lần**: đáp số đúng là 60 + 50 − 30 = 80.',
    'Ý tưởng "cộng rồi trừ phần đếm trùng" nghe đơn giản, nhưng với ba, bốn, ... hai mươi tập hợp thì phần trùng chồng lên nhau rất rối. Bài này cho em quy luật chung, rồi dùng nó trả lời câu hỏi: trong các số từ 1 đến 10^18^, có bao nhiêu số chia hết cho ít nhất một trong 20 số cho trước?',
  ],
  body: [
    { h: 'Đếm bội số trong một đoạn' },
    'Trong các số 1, 2, ..., N, các bội của a là a, 2a, 3a, ..., q · a với q · a ≤ N < (q + 1) · a. Theo định nghĩa phép chia có dư (Bài 1), q chính là thương ⌊N / a⌋. Vậy:',
    { formula: 'số bội của a trong [1, N] = ⌊N / a⌋' },
    'Ví dụ trong [1, 30] có ⌊30 / 2⌋ = 15 số chẵn, ⌊30 / 3⌋ = 10 bội của 3, ⌊30 / 5⌋ = 6 bội của 5. Còn số chia hết cho **cả** 2 và 3? Một số chia hết cho cả a và b khi và chỉ khi nó là bội chung của a và b, tức là bội của **lcm(a, b)** (Bài 3). Với 2 và 3, lcm = 6, nên có ⌊30 / 6⌋ = 5 số: 6, 12, 18, 24, 30.',
    { box: 'note', title: 'LCM, KHÔNG PHẢI TÍCH', body: [
      'Chỉ khi a, b nguyên tố cùng nhau thì lcm(a, b) = a · b. Số chia hết cho cả 4 và 6 là bội của lcm(4, 6) = 12 chứ không phải của 24: trong [1, 100] có ⌊100 / 12⌋ = **8** số như vậy (12, 24, ..., 96), không phải ⌊100 / 24⌋ = 4.',
    ] },

    { h: 'Nguyên lí bù trừ' },
    'Kí hiệu |A| là số phần tử của tập A. Câu chuyện lớp 10 Tin chính là công thức cho **hai tập**: |A ∪ B| = |A| + |B| − |A ∩ B|. Với **ba tập**, hãy nhìn vào hình dưới: ba hình tròn là các bội của 2, 3 và 5 trong [1, 30], và mỗi số được viết đúng vào vùng của nó.',
    { fig: 'f14_venn', w: 5.3, cap: 'Các số 1..30 xếp theo chúng chia hết cho 2, 3, 5 hay không. Có 22 số nằm trong ít nhất một hình tròn.' },
    'Cộng ba tập: 15 + 10 + 6 = 31. Nhưng các số ở vùng giao hai tập (6, 12, 10, 15...) bị đếm hai lần, còn số 30 ở giữa bị đếm **ba** lần. Trừ các giao từng cặp: 31 − 5 − 3 − 2 = 21. Lúc này số 30 đã bị cộng 3 lần rồi trừ 3 lần, tức **không được đếm lần nào**! Cộng lại giao của cả ba: 21 + 1 = **22**. Đếm trực tiếp trên hình: 8 + 4 + 2 + 4 + 2 + 1 + 1 = 22, khớp.',
    { box: 'theorem', title: 'ĐỊNH LÍ (NGUYÊN LÍ BÙ TRỪ)', body: [
      'Với các tập hữu hạn A~1~, A~2~, ..., A~k~:',
      { formula: '|A~1~ ∪ ... ∪ A~k~| = Σ |A~i~| − Σ |A~i~ ∩ A~j~| + Σ |A~i~ ∩ A~j~ ∩ A~l~| − ...' },
      'Nói gọn: lấy tổng theo mọi tập con khác rỗng S của {1, ..., k} của số phần tử của giao các A~i~ (i ∈ S), mang dấu **+** khi S có lẻ phần tử, dấu **−** khi S có chẵn phần tử.',
    ] },
    { box: 'why', body: [
      'Xét một phần tử x nằm trong đúng t ≥ 1 tập. Trong tổng trên, x được cộng ở mọi tập con S gồm các tập chứa x: có C(t, 1) tập con 1 phần tử (dấu +), C(t, 2) tập con 2 phần tử (dấu −), ... Tổng số lần x được đếm là:',
      { formula: 'C(t, 1) − C(t, 2) + C(t, 3) − ... = 1 − (1 − 1)^t^ = 1' },
      'Đẳng thức cuối là nhị thức Newton với a = 1, b = −1 (Bài 13): C(t, 0) − C(t, 1) + C(t, 2) − ... = 0. Vậy mỗi phần tử của hợp được đếm **đúng một lần**, còn phần tử nằm ngoài mọi tập (t = 0) không được đếm lần nào.',
    ] },
    'Bảng dưới kiểm tra điều đó với ba tập: dù một số nằm trong 1, 2 hay 3 tập, tổng số lần đếm luôn là 1.',
    { table: { cols: [2400, 1400, 1400, 1400, 2018], head: ['Số nằm trong t tập', '+ C(t, 1)', '− C(t, 2)', '+ C(t, 3)', 'Tổng số lần đếm'],
      rows: [['t = 1 (ví dụ 4)', '1', '0', '0', '**1**'], ['t = 2 (ví dụ 6)', '2', '−1', '0', '**1**'], ['t = 3 (ví dụ 30)', '3', '−3', '1', '**1**']],
      aligns: C3([1, 1, 1, 1, 1]) } },

    { h: 'Bài toán BUTRU' },
    { problem: { code: 'BUTRU', statement: [
      'Cho số nguyên dương N và k số nguyên dương a~1~, a~2~, ..., a~k~. Hãy đếm số các số nguyên x trong đoạn [1, N] chia hết cho **ít nhất một** trong các số a~i~.',
    ], input: 'Dòng đầu chứa N và k (1 ≤ N ≤ 10^18^, 1 ≤ k ≤ 20). Dòng thứ hai chứa a~1~, ..., a~k~ (1 ≤ a~i~ ≤ 10^18^, có thể trùng nhau).', output: 'Một số nguyên là số lượng cần đếm.' } },
    { examples: 'BUTRU', explain: ['Đúng như Hình 14.1: 15 + 10 + 6 − 5 − 3 − 2 + 1 = 22.', 'lcm(10^9^ + 7, 10^9^ + 9) đã vượt 10^18^ nên mọi giao chứa cặp này bằng 0; lcm của cả ba số cỡ 10^27^, nhân thẳng thì tràn số.', '25 + 16 + 10 − 8 − 5 − 3 + 1 = 36; giao của bội 4 và bội 6 là bội của 12.'] },

    { h: 'Ý tưởng ngây thơ: Xét từng số' },
    'Cách tự nhiên nhất: đi qua từng x từ 1 đến N, thử chia cho từng a~i~; gặp một a~i~ chia hết x thì đếm x và dừng thử (để mỗi x chỉ được đếm một lần).',
    { fig: 'f14_ngaytho', w: 3.0, cap: 'Sơ đồ khối của cách xét từng số.' },
    { file: 'BUTRU_ngaytho', title: 'BUTRU.CPP (ngây thơ): xét từng x trong [1, N]' },
    { box: 'count', body: [
      'Tối đa N · k phép chia lấy dư. Với N = 10^6^, k = 20: 2 · 10^7^ phép, chạy tức thì. Với N = 10^18^: 2 · 10^19^ phép, máy tính 10^9^ phép mỗi giây cần khoảng **600 năm**.',
    ] },
    { box: 'stuck', body: [
      'Ta không thể nhìn từng số một. Nhưng câu hỏi "có bao nhiêu bội của L trong [1, N]" thì trả lời được trong **một phép chia**: ⌊N / L⌋. Nguyên lí bù trừ biến bài toán về đúng những câu hỏi như vậy, mỗi câu cho một tập con của {a~1~, ..., a~k~}. Với k = 20 có 2^20^ − 1 = 1 048 575 tập con khác rỗng: nhỏ hơn 10^18^ rất nhiều.',
    ] },

    { h: 'Phá bế tắc: Bù trừ trên 2^k^ tập con' },
    { step: 'Mỗi tập con cho một số hạng' },
    'Gọi A~i~ là tập các bội của a~i~ trong [1, N]. Giao các A~i~ với i thuộc tập con S là tập các bội của L(S) = lcm của các a~i~, i ∈ S, nên có ⌊N / L(S)⌋ phần tử. Nguyên lí bù trừ cho ngay:',
    { formula: 'đáp số = Σ~S ≠ ∅~ (−1)^|S| + 1^ · ⌊N / L(S)⌋' },
    'Để duyệt mọi tập con, ta dùng **mặt nạ bit**: số nguyên S từ 1 đến 2^k^ − 1, bit thứ i của S bằng 1 nghĩa là a~i~ thuộc tập con (đánh số a~0~, ..., a~k−1~ như trong chương trình). Số phần tử |S| là số bit 1, hàm `__builtin_popcount(S)` cho ngay.',
    { step: 'Tính lcm của mỗi tập con chỉ bằng một phép gcd' },
    'Nếu với mỗi S ta lại tính lcm của cả |S| số thì tốn k phép gcd mỗi tập. Mẹo: gọi i là **bit 1 thấp nhất** của S (`__builtin_ctz(S)`), thì S bỏ đi i là `S & (S - 1)`, một số **nhỏ hơn** S nên đã được tính trước. Vì lcm có tính kết hợp:',
    { formula: 'L[S] = lcm(L[S & (S − 1)], a~i~)' },
    { fig: 'f14_tapcon', w: 6.2, cap: 'Tám tập con của {2, 3, 5}. Mũi tên đỏ: L[S] được tính từ tập con bỏ phần tử nhỏ nhất. Xanh cộng, hồng trừ.' },
    { step: 'Chạy tay với N = 30, a = (2, 3, 5)' },
    'Bảng dưới là kết quả chạy đúng vòng lặp của chương trình (mặt nạ viết bit a~0~ ở bên phải):',
    { table: { cols: [1100, 1300, 1000, 1500, 900, 800, 1000, 1018], head: ['S', 'Tập con', 'Bit i', 'L[S bỏ i]', 'L[S]', 'Dấu', '⌊30 / L⌋', 'ans'],
      rows: [['001', '{2}', '0', '1', '2', '+', '15', '15'], ['010', '{3}', '1', '1', '3', '+', '10', '25'], ['011', '{2, 3}', '0', '3', '6', '−', '5', '20'], ['100', '{5}', '2', '1', '5', '+', '6', '26'], ['101', '{2, 5}', '0', '5', '10', '−', '3', '23'], ['110', '{3, 5}', '1', '5', '15', '−', '2', '21'], ['111', '{2, 3, 5}', '0', '15', '30', '+', '1', '**22**']],
      aligns: C3([1, 1, 1, 1, 1, 1, 1, 1]) } },
    { step: 'Chặn tràn số khi lcm vượt N' },
    'Ví dụ 2 cho thấy nguy hiểm: lcm của ba số nguyên tố cỡ 10^9^ là khoảng 10^27^, vượt xa 2^63^. Nhân thẳng thì `long long` tràn và ⌊N / L⌋ ra rác. Nhưng để ý: **một khi L > N thì ⌊N / L⌋ = 0**, và mọi tập lớn hơn có lcm còn lớn hơn (là bội của L), cũng cho 0. Vậy ta chỉ cần biết "L có vượt N không", không cần giá trị thật của L.',
    { fig: 'f14_tran', w: 6.3, cap: 'Gặp lcm vượt N thì ghi L = N + 1 và không nhân thêm nữa, nên không bao giờ tràn số.' },
    'Tính lcm(x, a) = (x / gcd(x, a)) · a. Đặt y = x / gcd(x, a); để biết y · a > N mà **không nhân**, ta so sánh y > ⌊N / a⌋.',
    { box: 'why', title: 'VÌ SAO PHÉP SO SÁNH ĐÚNG?', body: [
      'Đặt q = ⌊N / a⌋, tức q · a ≤ N < (q + 1) · a. Nếu y ≤ q thì y · a ≤ q · a ≤ N. Nếu y ≥ q + 1 thì y · a ≥ (q + 1) · a > N. Vậy y · a > N khi và chỉ khi y > q. Mọi phép tính ở đây đều có giá trị không vượt quá N ≤ 10^18^, an toàn trong `long long`; và khi y · a ≤ N thì phép nhân cũng không tràn.',
      'Còn giá trị gán N + 1 ≤ 10^18^ + 1 vẫn vừa `long long`; mọi tập chứa S kế thừa giá trị này qua dòng `if (x > n)`.',
    ] },
    { step: 'Chương trình' },
    { fig: 'f14_toiuu', w: 3.0, cap: 'Sơ đồ khối của cách bù trừ trên các tập con.' },
    { file: 'BUTRU', title: 'BUTRU.CPP: bù trừ trên mọi tập con, chặn tràn lcm' },
    { box: 'count', body: [
      'Mỗi tập con: một phép gcd (không quá khoảng 90 bước với số 64 bit, theo định lí Lamé ở Bài 3), một phép chia và một phép so sánh. Tổng O(2^k^ · log N): với k = 20 khoảng 10^6^ tập con, chạy trong vài phần trăm giây. Mảng L có 2^20^ phần tử `long long`, 8 MB. So với cách ngây thơ, ta đã đổi sự phụ thuộc vào **N** (10^18^) thành phụ thuộc vào **k** (2^20^ ≈ 10^6^).',
    ] },
  ],
  ext: [
    { sub: 'Mở rộng 1: Cắt nhánh bằng đệ quy' },
    'Khi các a~i~ khá lớn, phần lớn tập con có lcm vượt N. Thay vì duyệt cả 2^k^ mặt nạ, ta xây tập con bằng **đệ quy**: thêm dần a~j~ với chỉ số tăng dần, và khi lcm vượt N thì **bỏ cả nhánh** (mọi tập chứa nó đều cho 0). Ta cũng bỏ trước các số trùng nhau, vì chúng không làm thay đổi tập các bội. Trường hợp xấu nhất vẫn là 2^k^, nhưng thường nhanh hơn rất nhiều và không cần mảng 2^k^ phần tử.',
    { file: 'BUTRU_dfs', title: 'BUTRU_DFS.CPP: bù trừ bằng đệ quy có cắt nhánh' },
    { sub: 'Mở rộng 2: Đếm số nguyên tố cùng nhau với n' },
    'Có bao nhiêu x trong [1, N] nguyên tố cùng nhau với n? Phân tích n ra thừa số nguyên tố (Bài 7) được các ước nguyên tố **phân biệt** p~1~, ..., p~k~. Số x **không** nguyên tố cùng nhau với n là số x chia hết cho ít nhất một p~i~: chính là BUTRU với a = (p~1~, ..., p~k~). Đáp số là N trừ đi số đó. Vì tích 15 số nguyên tố đầu tiên đã là 614 889 782 588 491 410 ≈ 6,1 · 10^17^, mọi n ≤ 10^18^ có **không quá 15** ước nguyên tố phân biệt: tối đa 2^15^ tập con.',
    'Ví dụ n = 30, N = 100: số bội của 2, 3 hoặc 5 là 50 + 33 + 20 − 16 − 10 − 6 + 3 = 74, nên có 100 − 74 = **26** số nguyên tố cùng nhau với 30. Khi N = n, đáp số chính là φ(n) của Bài 11: với n = 30 là 30 − 22 = 8 (đúng tám số nằm ngoài ba hình tròn ở Hình 14.1). Công thức tích φ(n) = n · Π(1 − 1/p) thực ra là nguyên lí bù trừ viết gọn.',
    { sub: 'Mở rộng 3: Hoán vị không điểm cố định' },
    'Cuối năm, n bạn bỏ quà vào một hộp rồi mỗi bạn rút ngẫu nhiên một món. Có bao nhiêu cách rút để **không bạn nào nhận lại quà của mình**? Đó là số hoán vị không có điểm cố định, kí hiệu D(n). Gọi A~i~ là tập các hoán vị giữ nguyên vị trí i; giao của j tập A~i~ có (n − j)! phần tử, và có C(n, j) cách chọn j vị trí. Bù trừ cho:',
    { formula: 'D(n) = Σ~j=0..n~ (−1)^j^ · C(n, j) · (n − j)! = n! · (1 − 1/1! + 1/2! − ... ± 1/n!)' },
    'Ví dụ D(4) = 24 − 24 + 12 − 4 + 1 = 9. Khi lập trình, dùng hệ thức truy hồi D(n) = (n − 1) · (D(n − 1) + D(n − 2)) với D(0) = 1, D(1) = 0 để tính mọi D(n) mod p trong O(n). Tỉ lệ D(n) / n! tiến rất nhanh về 1/e ≈ 0,3679: dù có bao nhiêu bạn, xác suất không ai nhận lại quà của mình luôn xấp xỉ 37%.',
    { table: { cols: [700, 900, 900, 1100, 1300, 1300, 1500, 918], head: ['n', '1', '2', '3', '4', '5', '6', '7'],
      rows: [['D(n)', '0', '1', '2', '9', '44', '265', '1854'], ['n!', '1', '2', '6', '24', '120', '720', '5040'], ['D(n) / n!', '0', '0,5', '0,333', '0,375', '0,3667', '0,36806', '0,36786']],
      aligns: C3([1, 1, 1, 1, 1, 1, 1, 1]) } },
  ],
  traps: [
    '**Giao là bội của tích:** bội chung của a, b là bội của lcm(a, b), không phải a · b. Chỉ bằng nhau khi gcd(a, b) = 1.',
    '**Tràn số khi tính lcm:** tích (x / g) · a có thể vượt 2^63^. Luôn so sánh x / g > N / a trước khi nhân, gặp lcm > N thì gán N + 1.',
    '**Nhầm dấu:** tập con có lẻ phần tử mang dấu +, chẵn phần tử mang dấu −. Đổi ngược sẽ ra số âm.',
    '**Dùng `1 << k` với k lớn:** với k = 20 thì 2^20^ ổn, nhưng nếu k tới 60 thì bù trừ thuần túy không khả thi; cần cắt nhánh hoặc ý tưởng khác.',
    '**Ngây thơ đếm trùng:** quên `break` sau khi gặp một a~i~ chia hết x thì x được đếm nhiều lần.',
  ],
  remember: [
    'Số bội của a trong [1, N] là ⌊N / a⌋; bội chung của các a~i~ là bội của lcm của chúng.',
    '|A ∪ B ∪ C| = |A| + |B| + |C| − |A ∩ B| − |A ∩ C| − |B ∩ C| + |A ∩ B ∩ C|; tổng quát: dấu (−1)^|S|+1^ theo mọi tập con S.',
    'Chứng minh: phần tử thuộc t tập được đếm C(t, 1) − C(t, 2) + ... = 1 lần.',
    'Duyệt tập con bằng mặt nạ bit; L[S] = lcm(L[S & (S − 1)], a[ctz(S)]); lcm vượt N thì chặn ở N + 1.',
  ],
  practice: [
    ['14.1', 'BỘI SỐ', 'Đếm số trong [L, R] chia hết cho a hoặc b nhưng không chia hết cho c: đếm trên [1, R] trừ [1, L − 1], bù trừ với 3 tập.'],
    ['14.2', 'NGUYÊN TỐ CÙNG NHAU', 'Q truy vấn: đếm x ≤ N nguyên tố cùng nhau với n (n, N ≤ 10^12^): phân tích n, bù trừ trên các ước nguyên tố.'],
    ['14.3', 'TẶNG QUÀ', 'Số hoán vị của n phần tử có đúng m điểm cố định, mod 10^9^ + 7: C(n, m) · D(n − m), dùng TOHOP và truy hồi D(n).'],
  ],
  quiz: [
    ['Trong các số từ 1 đến 1000 có bao nhiêu số chia hết cho ít nhất một trong các số 3, 5, 7?', 'Đáp số: 333 + 200 + 142 − 66 − 47 − 28 + 9 = 543'],
    ['Có bao nhiêu số trong [1, 100] nguyên tố cùng nhau với 30?', 'Đáp số: 100 − 74 = 26'],
    ['Năm bạn đổi quà sao cho không ai nhận lại quà của mình. Có bao nhiêu cách?', 'Đáp số: D(5) = 120 − 120 + 60 − 20 + 5 − 1 = 44'],
    ['Với k = 20, chương trình BUTRU duyệt bao nhiêu tập con khác rỗng? Vì sao trong [1, 100] có 8 số chia hết cho cả 4 và 6?', 'Đáp số: 2^20^ − 1 = 1 048 575; vì chúng là bội của lcm(4, 6) = 12'],
  ],
  algos: [
    ['Nguyên lí bù trừ trên k số (đếm bội trong [1, N])', 'O(2^k^ · log N)'],
    ['Đếm số nguyên tố cùng nhau với n trong [1, N]', 'O(√n + 2^ω(n)^)'],
    ['Số hoán vị không điểm cố định D(n)', 'O(n)'],
  ],
};

// ============================================================ BÀI 15
const L15 = {
  no: 15, title: 'Dãy truy hồi và lũy thừa ma trận', sub: 'số Fibonacci thứ 10^18^ trong 84 phép nhân ma trận',
  goals: [
    'Hiểu **dãy truy hồi** qua dãy Fibonacci và bài toán lát gạch; biết vì sao F~n~ tăng theo cấp số nhân.',
    'Biết nhân hai ma trận và viết một bước truy hồi thành **phép nhân ma trận** với một vectơ trạng thái.',
    'Chứng minh Q^n^ = [[F~n+1~, F~n~], [F~n~, F~n−1~]] và dùng **lũy thừa nhanh** (Bài 9) để tính F~n~ mod m với n ≤ 10^18^ trong O(log n).',
    'Mở rộng cho truy hồi tuyến tính bậc k và đếm đường đi trên đồ thị.',
  ],
  warmup: [
    'Hành lang trường em dài n mét, rộng 1 mét. Bác bảo vệ lát gạch bằng hai loại: viên vuông 1 × 1 và viên dài 1 × 2. Hành lang 1 mét có 1 cách lát, 2 mét có 2 cách (hai viên vuông hoặc một viên dài), 3 mét có 3 cách, 4 mét có 5 cách... Hành lang 10^18^ mét có bao nhiêu cách? (Lấy dư cho 10^9^ cho gọn.)',
    'Các số 1, 2, 3, 5, 8, 13... chính là **dãy Fibonacci** nổi tiếng. Tính số hạng thứ một trăm thì dễ, chỉ cần một vòng lặp. Nhưng số hạng thứ 10^18^ thì vòng lặp chạy hơn 30 năm. Bài này cho em một công cụ rất mạnh: biến "một bước của dãy" thành **một phép nhân ma trận**, rồi nhảy 10^18^ bước chỉ bằng vài chục phép nhân.',
  ],
  body: [
    { h: 'Dãy Fibonacci và bài toán lát gạch' },
    { box: 'def', title: 'ĐỊNH NGHĨA (DÃY FIBONACCI)', body: [
      { formula: 'F~0~ = 0,   F~1~ = 1,   F~n~ = F~n−1~ + F~n−2~ (n ≥ 2)' },
      'Một dãy mà mỗi số hạng được tính từ một số số hạng đứng trước theo một quy tắc cố định gọi là **dãy truy hồi**. Các giá trị đầu (ở đây F~0~, F~1~) gọi là **giá trị khởi đầu**.',
    ] },
    { table: { cols: [700, 790, 790, 790, 790, 790, 790, 790, 790, 790, 798], head: ['n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      rows: [['F~n~', '0', '1', '1', '2', '3', '5', '8', '13', '21', '34'], ['n', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'], ['F~n~', '55', '89', '144', '233', '377', '610', '987', '1597', '2584', '4181']],
      aligns: Array(11).fill('center') } },
    'Vì sao hành lang lại dẫn tới Fibonacci? Gọi T(n) là số cách lát hành lang dài n. Nhìn vào **viên gạch cuối cùng**: nếu là viên vuông, phần còn lại dài n − 1, có T(n − 1) cách; nếu là viên dài, phần còn lại dài n − 2, có T(n − 2) cách. Hai trường hợp tách bạch, nên T(n) = T(n − 1) + T(n − 2), với T(1) = 1, T(2) = 2. Đây đúng là dãy Fibonacci dịch đi một chỉ số: **T(n) = F~n+1~**.',
    { fig: 'f15_lat', w: 6.3, cap: 'Mọi cách lát hành lang dài 1..5. Với n = 5: viên cuối là ô vuông (5 cách) hoặc thanh dài (3 cách).' },
    'Dãy Fibonacci tăng rất nhanh: mỗi số hạng gấp khoảng 1,618 lần số trước (con số này là **tỉ lệ vàng** (1 + √5) / 2). F~92~ = 7 540 113 804 746 346 429 là số Fibonacci lớn nhất còn vừa `long long`, F~93~ đã tràn. Vì vậy đề bài luôn hỏi F~n~ **mod m**.',

    { h: 'Ma trận và bước truy hồi' },
    'Để tính F~i+2~ ta cần **hai** số liền trước F~i+1~ và F~i~. Hãy gói chúng thành một cặp (F~i+1~, F~i~), gọi là **trạng thái**. Một bước của dãy biến trạng thái (F~i+1~, F~i~) thành (F~i+2~, F~i+1~) = (F~i+1~ + F~i~, F~i+1~): giống như một cửa sổ rộng hai ô trượt sang phải một ô. Mỗi thành phần mới là một **tổ hợp tuyến tính** của các thành phần cũ, và toán học có sẵn một công cụ để viết những phép biến đổi như vậy: ma trận.',
    { box: 'def', title: 'ĐỊNH NGHĨA (NHÂN MA TRẬN)', body: [
      'Ma trận cỡ r × c là một bảng số có r hàng, c cột; X[i][j] là phần tử ở hàng i, cột j (đánh số từ 0). Tích của ma trận A cỡ r × t và B cỡ t × c là ma trận C = A · B cỡ r × c với:',
      { formula: 'C[i][j] = A[i][0] · B[0][j] + A[i][1] · B[1][j] + ... + A[i][t−1] · B[t−1][j]' },
      'tức "hàng i của A nhân lần lượt với cột j của B rồi cộng lại". Ma trận đơn vị I có 1 trên đường chéo, 0 ở chỗ khác, thỏa A · I = I · A = A.',
    ] },
    { fig: 'f15_truot', w: 6.3, cap: 'Một bước Fibonacci là một phép nhân với ma trận Q: cửa sổ (F~i+1~, F~i~) trượt sang phải một ô.' },
    'Nhân Q = [[1, 1], [1, 0]] (viết theo hàng) với cột (F~i+1~, F~i~): hàng đầu cho 1 · F~i+1~ + 1 · F~i~ = F~i+2~, hàng sau cho 1 · F~i+1~ + 0 · F~i~ = F~i+1~. Vậy **mỗi bước của dãy là một lần nhân với Q**, và đi n bước là nhân với Q n lần, tức nhân với Q^n^.',
    { box: 'theorem', title: 'ĐỊNH LÍ (LŨY THỪA CỦA Q)', body: [
      'Với mọi n ≥ 1:',
      { formula: 'Q^n^ = [[F~n+1~, F~n~], [F~n~, F~n−1~]]' },
      'Nói riêng, F~n~ chính là phần tử Q^n^[0][1]. Quy ước Q^0^ = I thì công thức cũng đúng với n = 0 nếu đặt F~−1~ = 1.',
    ] },
    { box: 'why', body: [
      'Quy nạp theo n. Với n = 1: Q = [[1, 1], [1, 0]] = [[F~2~, F~1~], [F~1~, F~0~]], đúng. Giả sử đúng với n, ta có Q^n+1^ = Q^n^ · Q = [[F~n+1~ + F~n~, F~n+1~], [F~n~ + F~n−1~, F~n~]] = [[F~n+2~, F~n+1~], [F~n+1~, F~n~]], đúng với n + 1.',
    ] },
    { box: 'note', title: 'TÍNH KẾT HỢP: CHÌA KHÓA CỦA LŨY THỪA NHANH', body: [
      'Phép nhân ma trận **không giao hoán** (thường A · B ≠ B · A) nhưng **có tính kết hợp**: (A · B) · C = A · (B · C). Lũy thừa nhanh ở Bài 9 chỉ cần tính kết hợp, vì nó gom các thừa số Q thành từng nhóm Q^2^, Q^4^, Q^8^... Mọi lũy thừa của cùng một ma trận Q lại giao hoán với nhau, nên thứ tự nhân trong chương trình không quan trọng.',
    ] },

    { h: 'Bài toán FIBO' },
    { problem: { code: 'FIBO', statement: [
      'Cho hai số nguyên n và m. Hãy tính F~n~ mod m, với F~0~ = 0, F~1~ = 1, F~n~ = F~n−1~ + F~n−2~.',
    ], input: 'Một dòng chứa n và m (0 ≤ n ≤ 10^18^, 1 ≤ m ≤ 10^9^).', output: 'Một số nguyên là F~n~ mod m.' } },
    { examples: 'FIBO', explain: ['F~10~ = 55; cũng là số cách lát hành lang dài 9.', 'n = 10^18^: vòng lặp n bước chạy hơn 30 năm.', 'F~0~ = 0. Các trường hợp n = 0 và m = 1 (mọi số dư đều 0) là bẫy hay gặp.'] },

    { h: 'Ý tưởng ngây thơ: Lặp n bước' },
    'Giữ hai biến a = F~i~, b = F~i+1~ (đã lấy dư cho m) và tịnh tiến n lần: (a, b) ← (b, (a + b) mod m). Sau n lần, a = F~n~ mod m. Lưu ý b khởi tạo bằng `1 % m` để đúng cả khi m = 1.',
    { fig: 'f15_ngaytho', w: 2.7, cap: 'Sơ đồ khối của cách lặp n bước.' },
    { file: 'FIBO_ngaytho', title: 'FIBO.CPP (ngây thơ): lặp n bước' },
    { box: 'count', body: [
      'Đúng n vòng lặp, mỗi vòng một phép cộng và một phép lấy dư: O(n) thời gian, O(1) bộ nhớ. Với n = 10^9^, chương trình chạy khoảng 6 giây; với n = 10^18^ thì cần khoảng 10^9^ lần như thế, tức **hơn 30 năm**.',
    ] },
    { box: 'stuck', body: [
      'Mỗi vòng lặp chỉ đi được **một** bước của dãy. Muốn nhanh, ta phải nhảy nhiều bước một lúc: biết F~1000~ và F~1001~ thì có tính thẳng F~2000~ được không? Định lí lũy thừa của Q trả lời: nhảy n bước là nhân với Q^n^, và Q^n^ thì tính được bằng bình phương liên tiếp như a^b^ ở Bài 9.',
    ] },

    { h: 'Phá bế tắc: Lũy thừa nhanh của ma trận' },
    { step: 'Đưa bài toán về tính Q^n^' },
    'Theo định lí, F~n~ mod m = Q^n^[0][1] mod m. Vậy chỉ cần tính Q^n^ với mọi phần tử lấy dư cho m. Phép lấy dư được phép làm sau mỗi phép nhân, cộng (Bài 1), vì mỗi phần tử của tích chỉ dùng nhân và cộng.',
    { step: 'Bình phương liên tiếp' },
    'Viết n ở hệ nhị phân. Ví dụ 10 = (1010)~2~ = 8 + 2, nên Q^10^ = Q^8^ · Q^2^. Các lũy thừa Q, Q^2^, Q^4^, Q^8^ có được bằng cách **bình phương** liên tiếp; ta nhân vào kết quả những lũy thừa ứng với **bit 1** của n.',
    { fig: 'f15_luythua', w: 6.2, cap: 'Q^10^ = Q^2^ · Q^8^: chỉ nhân các lũy thừa ứng với bit 1 của 10 = (1010)~2~.' },
    { step: 'Chạy tay với n = 10, m = 1000' },
    'Bảng dưới là các giá trị thật của vòng lặp trong chương trình (ma trận viết theo hàng, hàng cách nhau bởi dấu chấm phẩy). Ban đầu R = I = [1 0; 0 1], M = Q.',
    { table: { cols: [800, 1000, 900, 2300, 2400, 1218], head: ['Lượt', 'n còn lại', 'Bit cuối', 'M', 'R sau lượt', 'n mới'],
      rows: [['0', '10', '0', 'Q = [1 1; 1 0]', '[1 0; 0 1] (giữ nguyên)', '5'], ['1', '5', '1', 'Q^2^ = [2 1; 1 1]', 'R · M = [2 1; 1 1]', '2'], ['2', '2', '0', 'Q^4^ = [5 3; 3 2]', '[2 1; 1 1] (giữ nguyên)', '1'], ['3', '1', '1', 'Q^8^ = [34 21; 21 13]', 'R · M = **[89 55; 55 34]**', '0']],
      aligns: C3([1, 1, 1, 1, 1, 1]) } },
    'Kết thúc: R = Q^10^ = [89 55; 55 34] = [F~11~ F~10~; F~10~ F~9~], đáp số R[0][1] = **55**. Bốn lượt thay cho mười bước của cách ngây thơ; với n = 10^18^ là 60 lượt thay cho 10^18^ bước.',
    { box: 'why', title: 'VÌ SAO VÒNG LẶP ĐÚNG?', body: [
      'Gọi N là giá trị ban đầu của n. **Bất biến:** ở đầu mỗi lượt, R · M^n^ = Q^N^. Ban đầu R = I, M = Q, n = N: đúng. Nếu n chẵn, M^n^ = (M · M)^n/2^, nên thay M ← M · M, n ← n / 2 giữ nguyên bất biến. Nếu n lẻ, M^n^ = M · (M · M)^(n−1)/2^, nên R ← R · M rồi bình phương M và n ← (n − 1) / 2 cũng giữ bất biến. Khi n = 0: R · I = R = Q^N^.',
    ] },
    { step: 'Tràn số và trường hợp m = 1' },
    'Mọi phần tử luôn nhỏ hơn m ≤ 10^9^, nên mỗi tích nhỏ hơn 10^18^ và tổng hai tích nhỏ hơn 2 · 10^18^, vẫn dưới giới hạn 9,2 · 10^18^ của `long long`. Lấy dư một lần sau khi cộng là đủ. Ma trận đơn vị ban đầu viết là `1 % m` để khi m = 1 mọi phần tử đều bằng 0.',
    { step: 'Chương trình' },
    { fig: 'f15_toiuu', w: 2.9, cap: 'Sơ đồ khối của lũy thừa nhanh ma trận.' },
    { file: 'FIBO', title: 'FIBO.CPP: lũy thừa nhanh ma trận 2 x 2' },
    { box: 'count', body: [
      'Số lượt bằng số bit của n, tối đa 60 với n ≤ 10^18^. Mỗi lượt một phép bình phương và có thể thêm một phép nhân R · M: tối đa 120 phép nhân ma trận, mỗi phép 8 phép nhân số. Với n = 10^18^ (60 bit, 24 bit 1): đúng 60 + 24 = **84** phép nhân ma trận, khoảng 700 phép nhân số. Độ phức tạp O(log n), so với O(n) của cách lặp.',
    ] },
    { table: { cols: [2600, 3000, 3018], head: ['n', 'Lặp n bước', 'Lũy thừa ma trận'],
      rows: [['10', '10 bước', '4 lượt'], ['10^9^', '10^9^ bước (≈ 6 giây)', '30 lượt'], ['10^18^', '10^18^ bước (≈ 30 năm)', '60 lượt (≈ 1 micro giây)']],
      aligns: C3([1, 1, 1]) } },
  ],
  ext: [
    { sub: 'Mở rộng 1: Truy hồi tuyến tính bậc k' },
    'Cùng ý tưởng áp dụng cho mọi dãy f~n~ = c~1~ f~n−1~ + c~2~ f~n−2~ + ... + c~k~ f~n−k~. Trạng thái là k số hạng liên tiếp (f~i+k−1~, ..., f~i~); ma trận chuyển T cỡ k × k có hàng đầu là c~1~, ..., c~k~, các hàng sau "chép" thành phần lên một vị trí (T[i][i − 1] = 1). Ma trận này gọi là **ma trận đồng hành**. Mỗi phép nhân ma trận k × k tốn k^3^ phép nhân, nên cả thuật toán là O(k^3^ log n).',
    'Ví dụ dãy **Tribonacci** f~n~ = f~n−1~ + f~n−2~ + f~n−3~ với f~0~ = f~1~ = 0, f~2~ = 1 cho 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274...; nó đếm số cách đi lên cầu thang khi mỗi bước được bước 1, 2 hoặc 3 bậc.',
    { file: 'FIBO_tongquat', title: 'FIBO_TONGQUAT.CPP: truy hồi bậc k, đọc k n m, các c và f(0..k-1)' },
    { sub: 'Mở rộng 2: Đếm đường đi độ dài n trên đồ thị' },
    'Cho đồ thị có ma trận kề A (A[u][v] = 1 nếu có cạnh u − v). Khi đó **A^n^[u][v] là số đường đi độ dài đúng n** (được đi lại đỉnh, cạnh cũ) từ u tới v. Lí do giống hệt quy tắc nhân: một đường đi độ dài n + 1 từ u tới v là đường đi độ dài n từ u tới một đỉnh w nào đó, rồi thêm cạnh w − v; tổng theo w chính là công thức nhân ma trận.',
    { fig: 'f15_dothi', w: 5.4, cap: 'A^3^[1][3] = 4: có bốn đường đi độ dài 3 từ đỉnh 1 tới đỉnh 3.' },
    'Bốn đường đi đó là 1 → 2 → 1 → 3, 1 → 3 → 1 → 3, 1 → 3 → 2 → 3 và 1 → 3 → 4 → 3. Với n tới 10^18^ và đồ thị vài chục đỉnh, chỉ cần thay ma trận T trong FIBO_TONGQUAT bằng A.',
    { sub: 'Mở rộng 3: Công thức nhân đôi' },
    'Từ Q^2k^ = Q^k^ · Q^k^ và định lí lũy thừa của Q, so sánh các phần tử ta được hai đẳng thức đẹp:',
    { formula: 'F~2k~ = F~k~ · (2F~k+1~ − F~k~),    F~2k+1~ = F~k~^2^ + F~k+1~^2^' },
    'Biết cặp (F~k~, F~k+1~) thì tính ngay cặp (F~2k~, F~2k+1~), và từ đó (F~2k+1~, F~2k+2~). Đệ quy theo n / 2 cho thuật toán O(log n) gọn hơn, ít phép nhân hơn ma trận (khoảng 3 thay vì 8 phép nhân số mỗi bậc).',
    { file: 'FIBO_nhandoi', title: 'FIBO_NHANDOI.CPP: công thức nhân đôi' },
    { sub: 'Mở rộng 4: Chu kì Pisano' },
    'Dãy F~n~ mod m chỉ phụ thuộc vào cặp hai số dư liên tiếp, mà chỉ có m^2^ cặp, nên dãy số dư phải **tuần hoàn**; hơn nữa nó lặp lại ngay từ cặp (0, 1). Độ dài chu kì gọi là **chu kì Pisano** π(m). Ví dụ chữ số tận cùng của F~n~ (m = 10) lặp lại sau 60 số hạng.',
    { table: { cols: [1500, 600, 600, 600, 600, 700, 900, 1000, 2118], head: ['m', '2', '3', '5', '7', '10', '100', '1000', '10^9^'],
      rows: [['π(m)', '3', '8', '20', '16', '60', '300', '1500', '1,5 · 10^9^']],
      aligns: Array(9).fill('center') } },
    'Vì 10^18^ mod (1,5 · 10^9^) = 10^9^, ta có F(10^18^) ≡ F(10^9^) (mod 10^9^): ví dụ 2 của FIBO cũng giải được bằng vòng lặp 10^9^ bước. Nhưng chu kì Pisano có thể lớn tới 6m, nên lũy thừa ma trận vẫn là cách an toàn nhất.',
  ],
  traps: [
    '**Lấy dư quá muộn:** dãy Fibonacci tràn `long long` từ F~93~. Lấy dư sau mỗi phép cộng, nhân.',
    '**Cộng hai tích rồi mới lấy dư với m lớn:** với m ≤ 10^9^ thì an toàn (< 2 · 10^18^); nếu m tới 10^18^ phải dùng `__int128` (Bài 9).',
    '**Quên trường hợp m = 1:** khởi tạo ma trận đơn vị bằng 1 thay vì `1 % m` sẽ in 1 khi n = 0, m = 1 thay vì 0.',
    '**Lệch chỉ số:** Q^n^[0][1] = F~n~ nhưng Q^n^[0][0] = F~n+1~. Số cách lát hành lang dài n là F~n+1~, không phải F~n~.',
    '**Nhân ma trận sai thứ tự chỉ số:** C[i][j] = Σ A[i][l] · B[l][j]; đảo i, j sẽ ra ma trận chuyển vị, sai với ma trận không đối xứng.',
  ],
  remember: [
    'Truy hồi tuyến tính = một phép nhân ma trận lên vectơ trạng thái; n bước = nhân với T^n^.',
    'Q = [[1, 1], [1, 0]], Q^n^ = [[F~n+1~, F~n~], [F~n~, F~n−1~]].',
    'Lũy thừa nhanh ma trận: O(k^3^ log n); với Fibonacci (k = 2) chỉ khoảng 2 · log~2~ n phép nhân ma trận.',
    'A^n^[u][v] = số đường đi độ dài n từ u tới v.',
    'Phần tử < m ≤ 10^9^ thì tổng hai tích < 2 · 10^18^, an toàn trong `long long`.',
  ],
  practice: [
    ['15.1', 'LÁT GẠCH', 'Số cách lát hành lang 2 × n bằng các viên 1 × 2 (đặt dọc hoặc ngang), n ≤ 10^18^: lại là Fibonacci, dùng FIBO.'],
    ['15.2', 'TRIBONACCI', 'Số cách lên cầu thang n bậc, mỗi bước 1, 2 hoặc 3 bậc, mod 10^9^ + 7, n ≤ 10^18^: ma trận đồng hành 3 × 3.'],
    ['15.3', 'ĐƯỜNG ĐI ĐỘ DÀI K', 'Đồ thị ≤ 50 đỉnh, đếm đường đi độ dài đúng K ≤ 10^18^ giữa hai đỉnh: lũy thừa ma trận kề.'],
  ],
  quiz: [
    ['Tính F~20~. Hành lang dài 10 mét có bao nhiêu cách lát?', 'Đáp số: F~20~ = 6765; số cách lát là F~11~ = 89'],
    ['Chữ số tận cùng của F~2025~ là bao nhiêu? (Gợi ý: π(10) = 60.)', 'Đáp số: 2025 mod 60 = 45, F~45~ = 1 134 903 170, chữ số tận cùng là 0'],
    ['Chương trình FIBO thực hiện bao nhiêu phép nhân ma trận với n = 10^18^ (có 60 chữ số nhị phân, trong đó 24 chữ số 1)?', 'Đáp số: 60 phép bình phương + 24 phép nhân vào R = 84'],
    ['Với Q = [[1, 1], [1, 0]], hãy tính Q^4^ và đọc ra F~4~, F~5~.', 'Đáp số: Q^4^ = [[5, 3], [3, 2]], F~4~ = 3, F~5~ = 5'],
  ],
  algos: [
    ['Số Fibonacci bằng lũy thừa nhanh ma trận', 'O(log n)'],
    ['Truy hồi tuyến tính bậc k (ma trận đồng hành)', 'O(k³ log n)'],
    ['Số đường đi độ dài n trên đồ thị V đỉnh', 'O(V³ log n)'],
    ['Fibonacci bằng công thức nhân đôi', 'O(log n)'],
  ],
};

// ============================================================ BÀI 16
const L16 = {
  no: 16, title: 'Kĩ thuật chia khối ⌊n / i⌋', sub: 'tổng số ước của 1..n trong O(√n)',
  goals: [
    'Chứng minh Σ~x ≤ n~ d(x) = Σ~i ≤ n~ ⌊n / i⌋ bằng phép **đếm hai lần**.',
    'Hiểu vì sao dãy ⌊n / 1⌋, ⌊n / 2⌋, ..., ⌊n / n⌋ chỉ có **không quá 2√n giá trị khác nhau**.',
    'Tìm được khối [i, j] lớn nhất có cùng giá trị ⌊n / i⌋ bằng công thức j = ⌊n / ⌊n / i⌋⌋, và tính tổng trong O(√n).',
    'Áp dụng cho Σ i · ⌊n / i⌋ (tổng các ước), Σ n mod i và phương pháp hyperbol.',
  ],
  warmup: [
    'Thầy giáo viết lên bảng các số 1, 2, ..., 12 rồi hỏi: "Tổng số ước của tất cả các số này là bao nhiêu?" Cả lớp chia nhau đếm: số 1 có 1 ước, số 2 có 2 ước, số 12 có 6 ước... cộng lại được 35. Thầy hỏi tiếp: "Còn từ 1 đến 10^12^ thì sao?"',
    'Đếm ước của từng số là hết hi vọng. Nhưng nếu **đổi góc nhìn**, thay vì hỏi "số x có bao nhiêu ước", ta hỏi "số i là ước của bao nhiêu số", thì bài toán biến thành một tổng các thương ⌊n / i⌋. Và tổng ấy có một bí mật: tuy có n số hạng nhưng chỉ có khoảng 2√n giá trị khác nhau. Với n = 10^12^, đó là hai triệu thay vì một nghìn tỉ.',
  ],
  body: [
    { h: 'Tổng số ước và phép đếm hai lần' },
    'Kí hiệu d(x) là số ước dương của x (Bài 2). Bảng dưới liệt kê d(x) với x từ 1 đến 12 và tổng của chúng.',
    { table: { cols: [900, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 998], head: ['x', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'Tổng'],
      rows: [['d(x)', '1', '2', '2', '3', '2', '4', '2', '4', '3', '4', '2', '6', '**35**'], ['⌊12 / x⌋', '12', '6', '4', '3', '2', '2', '1', '1', '1', '1', '1', '1', '**35**']],
      aligns: Array(14).fill('center') } },
    'Hai hàng có cùng tổng 35 dù từng số hạng khác hẳn nhau. Không phải trùng hợp: hàng dưới đếm cùng một thứ theo một cách khác.',
    { box: 'theorem', title: 'ĐỊNH LÍ (ĐỔI THỨ TỰ ĐẾM)', body: [
      { formula: 'D(n) = d(1) + d(2) + ... + d(n) = ⌊n / 1⌋ + ⌊n / 2⌋ + ... + ⌊n / n⌋' },
    ] },
    { box: 'why', body: [
      'Cả hai vế đều đếm số **cặp (i, x)** với 1 ≤ x ≤ n và i là ước của x. Đếm theo x trước: với mỗi x có d(x) giá trị i, được vế trái. Đếm theo i trước: với mỗi i, các x nhận i làm ước là các bội của i trong [1, n], có ⌊n / i⌋ số (Bài 14), được vế phải.',
      'Viết x = i · j, ta còn có cách nhìn thứ ba: D(n) là **số điểm nguyên (i, j)** với i, j ≥ 1 và i · j ≤ n, tức số điểm nguyên nằm dưới đường hypebol i · j = n (Hình 16.1).',
    ] },
    { fig: 'f16_luoi', w: 4.2, cap: 'Các điểm (i, j) với i · j ≤ 12. Cột i có ⌊12 / i⌋ điểm; các điểm vàng nằm trên đường i · j = 12 ứng với 6 ước của 12.' },

    { h: 'Bậc thang ⌊n / i⌋' },
    'Vẽ chiều cao ⌊n / i⌋ của từng cột i, ta được một **bậc thang** đi xuống. Phía đầu, mỗi bậc chỉ rộng một cột và tụt rất nhanh (20, 10, 6, 5...); phía sau, bậc thang thoải dần và mỗi bậc rộng ra: 4 cột cùng cao 2, rồi 10 cột cùng cao 1.',
    { fig: 'f16_bacthang', w: 6.2, cap: 'Bậc thang ⌊20 / i⌋. Các cột cùng chiều cao tạo thành một khối (cùng màu): chỉ có 8 khối cho 20 cột.' },
    'Chỉ có 8 giá trị khác nhau: 20, 10, 6, 5, 4, 3, 2, 1. Nếu cộng **theo khối** thay vì theo từng cột, ta chỉ làm 8 phép cộng. Hai câu hỏi cần trả lời: có bao nhiêu khối, và làm sao biết một khối kết thúc ở đâu?',
    { box: 'theorem', title: 'ĐỊNH LÍ (SỐ GIÁ TRỊ KHÁC NHAU)', body: [
      'Dãy ⌊n / i⌋ với i = 1, 2, ..., n có không quá 2√n giá trị khác nhau.',
    ] },
    { box: 'why', body: [
      'Chia các chỉ số i thành hai phần. **Phần i ≤ √n:** chỉ có không quá √n chỉ số, nên không quá √n giá trị. **Phần i > √n:** khi đó ⌊n / i⌋ ≤ n / i < √n, nên giá trị là một số nguyên dương nhỏ hơn √n: cũng không quá √n khả năng. Cộng lại: không quá 2√n giá trị.',
    ] },
    { table: { cols: [2400, 3000, 3218], head: ['n', 'Số khối (số giá trị khác nhau)', '2 · ⌊√n⌋'],
      rows: [['20', '8', '8'], ['100', '19', '20'], ['10^4^', '199', '200'], ['10^6^', '1 999', '2 000'], ['10^12^', '1 999 999', '2 000 000']],
      aligns: C3([1, 1, 1]) } },
    { box: 'theorem', title: 'ĐỊNH LÍ (ĐIỂM CUỐI CỦA KHỐI)', body: [
      'Cho 1 ≤ i ≤ n và q = ⌊n / i⌋. Chỉ số **lớn nhất** j thỏa ⌊n / j⌋ = q là:',
      { formula: 'j = ⌊n / q⌋' },
    ] },
    { box: 'why', body: [
      '⌊n / j⌋ ≥ q tương đương q · j ≤ n, tương đương j ≤ n / q, tức j ≤ ⌊n / q⌋. Vậy các chỉ số j có ⌊n / j⌋ ≥ q là đúng 1, 2, ..., ⌊n / q⌋. Vì ⌊n / j⌋ không tăng theo j, các chỉ số từ i đến ⌊n / q⌋ đều có ⌊n / j⌋ ≥ q và ≤ ⌊n / i⌋ = q, tức bằng q; còn j = ⌊n / q⌋ + 1 thì ⌊n / j⌋ < q. Do đó khối chứa i kết thúc đúng tại ⌊n / q⌋.',
    ] },

    { h: 'Bài toán TONGUOC' },
    { problem: { code: 'TONGUOC', statement: [
      'Cho số nguyên dương n. Hãy tính S(n) = ⌊n / 1⌋ + ⌊n / 2⌋ + ... + ⌊n / n⌋, cũng chính là tổng số ước của các số 1, 2, ..., n.',
    ], input: 'Một số nguyên n (1 ≤ n ≤ 10^12^).', output: 'Một số nguyên là S(n).' } },
    { examples: 'TONGUOC', explain: ['20 + 10 + 6 + 5 + 4 + 3 + 2 · 4 + 1 · 10 = 66 (Hình 16.2).', 'S(n) xấp xỉ n · (ln n + 0,1544), cỡ 2,8 · 10^13^: vẫn vừa `long long`.', 'Số 1 có đúng một ước.'] },

    { h: 'Ý tưởng ngây thơ: Cộng từng thương' },
    'Công thức đã có sẵn, chỉ cần một vòng lặp i từ 1 đến n, cộng dồn n / i.',
    { fig: 'f16_ngaytho', w: 2.6, cap: 'Sơ đồ khối của cách cộng từng thương.' },
    { file: 'TONGUOC_ngaytho', title: 'TONGUOC.CPP (ngây thơ): cộng từng thương' },
    { box: 'count', body: [
      'Đúng n phép chia: O(n). Phép chia 64 bit khá chậm: với n = 10^9^ chương trình chạy khoảng 3 giây, nên với n = 10^12^ cần khoảng **một giờ**.',
    ] },
    { box: 'stuck', body: [
      'Cách ngây thơ tính ⌊n / i⌋ cho cả n chỉ số i, trong khi ta vừa chứng minh chỉ có không quá 2√n giá trị khác nhau: với n = 10^12^, hơn 99,9998% phép chia là "tính lại" một giá trị đã biết. Nếu ở mỗi i ta biết ngay khối hiện tại kéo dài tới đâu, ta có thể **nhảy qua cả khối**.',
    ] },

    { h: 'Phá bế tắc: Gom các khối cùng giá trị' },
    { step: 'Nhảy qua cả khối' },
    'Bắt đầu từ i = 1. Ở mỗi lượt: tính q = ⌊n / i⌋, điểm cuối khối j = ⌊n / q⌋; cả khối [i, j] gồm j − i + 1 số hạng cùng bằng q, góp vào tổng q · (j − i + 1). Rồi nhảy sang i = j + 1.',
    { formula: 'q = ⌊n / i⌋,   j = ⌊n / q⌋,   s ← s + q · (j − i + 1),   i ← j + 1' },
    { step: 'Chạy tay với n = 20' },
    { table: { cols: [1000, 1400, 1400, 1600, 1918, 1300], head: ['i', 'q = ⌊20 / i⌋', 'j = ⌊20 / q⌋', 'Độ dài khối', 'Góp q · (j − i + 1)', 's'],
      rows: [['1', '20', '1', '1', '20', '20'], ['2', '10', '2', '1', '10', '30'], ['3', '6', '3', '1', '6', '36'], ['4', '5', '4', '1', '5', '41'], ['5', '4', '5', '1', '4', '45'], ['6', '3', '6', '1', '3', '48'], ['7', '2', '10', '4', '8', '56'], ['11', '1', '20', '10', '10', '**66**']],
      aligns: C3([1, 1, 1, 1, 1, 1]) } },
    'Tám lượt thay cho hai mươi, đúng bằng số khối trên Hình 16.2. Sáu khối đầu dài 1 (phần i ≤ √20), hai khối cuối dài (phần giá trị nhỏ): đúng như chứng minh về 2√n.',
    { box: 'why', title: 'VÌ SAO THUẬT TOÁN ĐÚNG VÀ DỪNG?', body: [
      'Theo định lí điểm cuối của khối, mọi chỉ số trong [i, j] có cùng giá trị q, nên phần đóng góp q · (j − i + 1) đúng bằng tổng các số hạng của khối. Vì j ≥ i (do ⌊n / q⌋ ≥ i khi q = ⌊n / i⌋), mỗi lượt i tăng ít nhất 1, các khối nối tiếp nhau phủ kín [1, n] không chồng lấn, và vòng lặp dừng khi i > n. Mỗi lượt kết thúc một khối, nên số lượt bằng số giá trị khác nhau, không quá 2√n.',
    ] },
    { step: 'Chương trình' },
    { fig: 'f16_toiuu', w: 2.7, cap: 'Sơ đồ khối của cách gom khối.' },
    { file: 'TONGUOC', title: 'TONGUOC.CPP: gom khối cùng giá trị n / i' },
    { box: 'count', body: [
      'Mỗi lượt hai phép chia, một phép nhân: tổng O(√n). Với n = 10^12^: 1 999 999 lượt, khoảng 4 triệu phép chia, chạy trong vài phần trăm giây. Tổng s ≤ 2,8 · 10^13^, tích q · (j − i + 1) ≤ n: không tràn `long long`.',
    ] },
  ],
  ext: [
    { sub: 'Mở rộng 1: Phương pháp hyperbol' },
    'Nhìn lại hình các điểm nguyên dưới hypebol i · j ≤ n. Hình nhận đường chéo i = j làm trục đối xứng. Gọi r = ⌊√n⌋. Mỗi điểm có i ≤ r hoặc j ≤ r (không thể cả hai đều > √n vì khi đó i · j > n). Đếm các điểm có i ≤ r (cột trái: Σ~i≤r~ ⌊n / i⌋), cộng các điểm có j ≤ r (hàng dưới: cùng tổng đó, do đối xứng), thì hình vuông r × r bị đếm hai lần:',
    { formula: 'S(n) = 2 · (⌊n / 1⌋ + ⌊n / 2⌋ + ... + ⌊n / r⌋) − r^2^' },
    { fig: 'f16_hyperbol', w: 4.2, cap: 'Phương pháp hyperbol với n = 12, r = 3: S(12) = 2 · (12 + 6 + 4) − 9 = 35.' },
    'Thuật toán chỉ có một vòng lặp r ≈ √n bước, nhanh gấp đôi cách gom khối. Lưu ý tính r = ⌊√n⌋ bằng `sqrtl` rồi **sửa** cho chắc chắn, vì số thực có sai số làm tròn.',
    { file: 'TONGUOC_hyperbol', title: 'TONGUOC_HYPERBOL.CPP: đếm điểm dưới hypebol' },
    { sub: 'Mở rộng 2: Tổng các ước Σ σ(x)' },
    'Gọi σ(x) là tổng các ước của x. Đếm hai lần như trên: mỗi i là ước của ⌊n / i⌋ số, mỗi lần góp **giá trị i**, nên σ(1) + ... + σ(n) = Σ i · ⌊n / i⌋. Trong một khối [i, j] cùng thương q, phần đóng góp là q · (i + (i + 1) + ... + j) = q · (i + j) · (j − i + 1) / 2. Ví dụ n = 20 cho tổng 339. Với n = 10^12^, tổng này khoảng 8,2 · 10^23^, vượt `long long`, nên đề bài thường hỏi theo mô-đun; tổng (i + j)(j − i + 1) có thể tới 10^24^, phải tính bằng `__int128`:',
    { code: 'const long long M = 1000000007;\nlong long s = 0;\nfor (long long i = 1, j; i <= n; i = j + 1) {\n    long long q = n / i;\n    j = n / q;\n    __int128 t = (__int128)(i + j) * (j - i + 1) / 2;  // i + ... + j\n    s = (s + (long long)(t % M) * (q % M)) % M;\n}', title: 'Tổng σ(1) + ... + σ(n) mod 10^9 + 7 (với n = 10^12 cho 146462362)' },
    { sub: 'Mở rộng 3: Tổng các số dư Σ n mod i' },
    'Vì n mod i = n − i · ⌊n / i⌋, ta có Σ~i=1..n~ (n mod i) = n^2^ − Σ i · ⌊n / i⌋: quy về ngay Mở rộng 2. Ví dụ n = 20: 400 − 339 = 61.',
    { sub: 'Mở rộng 4: Hai thương cùng lúc' },
    'Với tổng có dạng Σ f(⌊n / i⌋, ⌊m / i⌋), cả hai thương cùng không đổi trên đoạn [i, j] với j = min(⌊n / ⌊n / i⌋⌋, ⌊m / ⌊m / i⌋⌋). Số khối không quá 2(√n + √m). Kĩ thuật này xuất hiện rất nhiều trong các bài đếm cặp số có ƯCLN cho trước ở Tập 2.',
  ],
  traps: [
    '**Chia cho 0:** chỉ tính j = n / q khi q ≥ 1, tức khi i ≤ n. Điều kiện vòng lặp `i <= n` bảo đảm điều đó.',
    '**Dùng `int` cho i, j:** với n = 10^12^ thì i, j, n đều vượt 2^31^. Dùng `long long` cho mọi biến.',
    '**Tính √n bằng số thực:** `sqrt(n)` có thể lệch 1 khi n gần một số chính phương lớn. Luôn sửa bằng hai vòng `while`.',
    '**Tràn ở tổng có trọng số:** Σ i · ⌊n / i⌋ và (i + j)(j − i + 1) vượt `long long` khi n = 10^12^. Dùng `__int128` hoặc lấy dư.',
    '**Quên rằng khối có thể dài 1:** ở phần i ≤ √n mỗi khối chỉ có một chỉ số; công thức vẫn đúng, không cần xử lí riêng.',
  ],
  remember: [
    'Σ~x≤n~ d(x) = Σ~i≤n~ ⌊n / i⌋ = số điểm nguyên (i, j) với i · j ≤ n.',
    'Dãy ⌊n / i⌋ có không quá 2√n giá trị khác nhau.',
    'Khối chứa i kết thúc tại j = ⌊n / ⌊n / i⌋⌋; nhảy i ← j + 1 cho O(√n).',
    'Hyperbol: S(n) = 2 · Σ~i≤r~ ⌊n / i⌋ − r^2^ với r = ⌊√n⌋.',
  ],
  practice: [
    ['16.1', 'TỔNG ƯỚC', 'σ(1) + ... + σ(n) mod 10^9^ + 7, n ≤ 10^12^: chia khối, tổng cấp số cộng trong mỗi khối.'],
    ['16.2', 'TỔNG DƯ', 'Σ (n mod i) với i từ 1 đến k (k có thể khác n), mod 10^9^ + 7: n mod i = n − i · ⌊n / i⌋, chia khối trên [1, min(n, k)].'],
    ['16.3', 'HAI THƯƠNG', 'Σ (n mod i) · (m mod i) với i từ 1 đến min(n, m), n, m ≤ 10^12^: viết n mod i = n − i · ⌊n / i⌋, khai triển rồi chia khối đồng thời theo hai thương, dùng công thức Σ i và Σ i^2^ trên mỗi khối.'],
  ],
  quiz: [
    ['Tính S(100) = Σ ⌊100 / i⌋. Thuật toán gom khối chạy bao nhiêu lượt?', 'Đáp số: S(100) = 482, 19 lượt'],
    ['Liệt kê các giá trị khác nhau của ⌊36 / i⌋ với i = 1..36. Có bao nhiêu giá trị?', 'Đáp số: 1, 2, 3, 4, 5, 6, 7, 9, 12, 18, 36: 11 giá trị'],
    ['Tính 20 mod 1 + 20 mod 2 + ... + 20 mod 20.', 'Đáp số: 400 − 339 = 61'],
    ['Dùng phương pháp hyperbol tính S(12).', 'Đáp số: r = 3, 2 · (12 + 6 + 4) − 9 = 35'],
  ],
  algos: [
    ['Chia khối ⌊n / i⌋ (tổng số ước của 1..n)', 'O(√n)'],
    ['Phương pháp hyperbol', 'O(√n)'],
    ['Tổng σ(1..n), tổng n mod i bằng chia khối', 'O(√n)'],
  ],
};

module.exports = {
  no: 4, title: 'TỔ HỢP VÀ ĐẾM',
  intro: [
    'Có bao nhiêu cách chọn đội tuyển? Bao nhiêu số nhỏ hơn 10^18^ chia hết cho ít nhất một trong hai mươi số cho trước? Số Fibonacci thứ 10^18^ chia cho 10^9^ dư bao nhiêu? Tổng số ước của mọi số từ 1 đến một nghìn tỉ là bao nhiêu? Những câu hỏi "đếm" như vậy có đáp số khổng lồ, không thể liệt kê từng trường hợp, nhưng lại trả lời được trong chưa tới một giây nếu ta **đếm thông minh**.',
    'Chương này trình bày bốn công cụ đếm cơ bản của lập trình thi đấu: hệ số nhị thức theo mô-đun, nguyên lí bù trừ, lũy thừa ma trận cho dãy truy hồi và kĩ thuật chia khối ⌊n / i⌋. Mỗi công cụ dựa trên kiến thức của ba chương trước: nghịch đảo mô-đun, ước chung lớn nhất, lũy thừa nhanh, phép chia có dư, và là nền móng cho rất nhiều bài toán ở Tập 2.',
  ],
  lessons: [L13, L14, L15, L16],
};
