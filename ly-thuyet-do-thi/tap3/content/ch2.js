// TẬP 3 — CHƯƠNG 2. ĐƯỜNG ĐI NGẮN NHẤT
module.exports = {
  no: 2,
  intro: 'Ở chương này, cách ngây thơ thường không sai mà chỉ chậm: chạy lại cùng một thuật toán quá nhiều lần, hoặc dùng thuật toán "quá mạnh" (Bellman-Ford) khi chỉ cần Dijkstra. Mặt khác, rất nhiều lời giải "trông như đúng" mất điểm vì tràn số, vì sai một dấu so sánh, hoặc vì bỏ quên một chi tiết của mô hình (giới hạn số cạnh, thời điểm xuất bến, đèn đỏ...).',
  solutions: [
    // ================================================================ 5.1
    {
      id: '5.1', key: 'Dijkstra với hàng đợi ưu tiên và long long.',
      understand: [
        'Đồ thị có hướng, trọng số không âm, một nguồn: đây là bài toán gốc của thuật toán Dijkstra (Tập 1, Bài 5). Hai chi tiết: in −1 cho đỉnh không tới được, và khoảng cách có thể tới (n − 1) · 10^9^ ≈ 10^14^.',
        { fig: 'tap2:duongtruong', w: 4.6, cap: 'Cây đường đi ngắn nhất từ nút 1 của ví dụ.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Dijkstra O(n²)',
        body: [
          'Cài đặt Dijkstra nguyên bản: mỗi lượt duyệt cả n đỉnh để tìm đỉnh chưa chốt có nhãn nhỏ nhất.',
          { fig: 'f_duongtruong_naive', w: 3.0, cap: 'Sơ đồ khối của Dijkstra O(n²).' },
          { file: 'DUONGTRUONG_1on2', title: 'Cách ngây thơ: Dijkstra tìm đỉnh nhỏ nhất bằng vòng lặp' },
          { cx: 'n lượt, mỗi lượt O(n): O(n^2^ + m). Với n = 1000 là 10^6^; với n = 10^5^ là 10^10^.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n ≤ 1000): **{{P:DUONGTRUONG_1on2:1}} điểm**.', '**Subtask 2** (n ≤ 10^5^): quá thời gian.'] },
        'Một lỗi khác "đắt giá" hơn: cài Dijkstra với hàng đợi ưu tiên nhưng lưu khoảng cách bằng `int`. Ở các test có trọng số tới 10^9^, chỉ cần đường đi qua 3 cạnh là tràn số; chương trình được **{{S:DUONGTRUONG_2int}} điểm**, kém cả cách ngây thơ.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Việc tìm "đỉnh chưa chốt có nhãn nhỏ nhất" tốn O(n) mỗi lượt. Cần một cấu trúc dữ liệu lấy ra phần tử nhỏ nhất nhanh hơn.'] },
      ],
      breakthrough: [
        'Dùng `priority_queue` chứa các cặp (nhãn, đỉnh). Mỗi lần giảm d[v] thì đẩy thêm một cặp mới (không xóa cặp cũ). Khi lấy ra cặp (du, u) mà du ≠ d[u] thì đó là **bản cũ**, bỏ qua.',
        'Chạy tay ví dụ (nguồn s = 1):',
        { table: { cols: [2000, 3400, 3218], head: ['Lấy ra', 'Nới lỏng', 'd[1..6] sau bước'], rows: [
          ['(0, 1)', '1→2: 4; 1→3: 1', '0 4 1 ∞ ∞ ∞'], ['(1, 3)', '3→2: 1 + 2 = 3; 3→4: 9', '0 3 1 9 ∞ ∞'], ['(3, 2)', '2→4: 3 + 5 = 8', '0 3 1 8 ∞ ∞'],
          ['(4, 2)', 'bản cũ, bỏ qua', '0 3 1 8 ∞ ∞'], ['(8, 4)', '4→5: 11', '0 3 1 8 11 ∞'], ['(9, 4)', 'bản cũ, bỏ qua', ''], ['(11, 5)', '5→1: không cải thiện', '0 3 1 8 11 ∞']] } },
        'Nút 6 vẫn là ∞: in −1.',
      ],
      optimal: [
        { fig: 'f_duongtruong_opt', w: 3.4, cap: 'Sơ đồ khối của Dijkstra với hàng đợi ưu tiên.' },
        { file: 'DUONGTRUONG', title: 'DUONGTRUONG.CPP: Dijkstra O(m log n)' },
        { cx: 'mỗi cung đẩy nhiều nhất một cặp: O(m log m) = O(m log n).' },
      ],
      traps: ['**`int` cho khoảng cách** (mất trọn điểm).', '**In "vô cùng"** thay vì −1 cho đỉnh không tới được.', '**Quên bỏ qua bản cũ:** vẫn đúng nhưng có thể chậm đi nhiều lần.', '**Trọng số 0:** Dijkstra vẫn đúng; không cần xử lí riêng.'],
      approaches: [['DUONGTRUONG_1on2', 'Dijkstra O(n²)'], ['DUONGTRUONG_2int', 'Dijkstra + hàng đợi, khoảng cách int'], ['DUONGTRUONG', 'Dijkstra + hàng đợi, long long']],
    },
    // ================================================================ 5.2
    {
      id: '5.2', key: 'Dijkstra hai đầu + quét các "mốc" d₁.',
      understand: [
        'Đỉnh v quan trọng khi **mọi** đường đi ngắn nhất 1 → n đều qua v. Từ Tập 1, ta đã biết kiểm tra v nằm trên **một** đường ngắn nhất: d~1~[v] + d~n~[v] = D, với d~1~, d~n~ là khoảng cách từ 1 và từ n, D = d~1~[n]. Điều kiện "mọi" mạnh hơn nhiều.',
        { fig: 'tap2:nutgiao', w: 5.0, cap: 'Mọi đỉnh của ví dụ đều nằm trên một đường ngắn nhất, nhưng chỉ 1, 4, 7 nằm trên tất cả.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Xóa thử từng đỉnh',
        body: [
          'v quan trọng khi và chỉ khi xóa v đi thì khoảng cách từ 1 tới n tăng lên (hoặc không còn đường). Vậy thử xóa từng đỉnh và chạy lại Dijkstra.',
          { fig: 'f_nutgiao_naive', w: 3.0, cap: 'Sơ đồ khối của cách xóa thử từng đỉnh.' },
          { file: 'NUTGIAO_1xoadinh', title: 'Cách ngây thơ: n lần Dijkstra' },
          { cx: 'O(n · m log n): với n = 1000, m = 2000 khoảng 2·10^7^; với n = 10^5^ thì quá chậm.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1**: **{{P:NUTGIAO_1xoadinh:1}} điểm**.', '**Subtask 2**: quá thời gian.'] },
        'Một lời giải sai hay gặp: in mọi đỉnh có d~1~[v] + d~n~[v] = D (nằm trên **một** đường ngắn nhất). Ở ví dụ, chương trình in cả 7 đỉnh: **{{S:NUTGIAO_2motduong}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Ta biết **tập** các đỉnh và cạnh nằm trên đường ngắn nhất (một DAG), nhưng chưa biết đỉnh nào là "cổ chai" mà mọi đường đều phải qua. Số đường đi có thể lên tới 2^n/2^: không thể liệt kê.'] },
      ],
      breakthrough: [
        'Mọi trọng số đều dương nên dọc theo **bất kì** đường ngắn nhất nào, giá trị d~1~ tăng ngặt từ 0 tới D. Hãy coi mỗi giá trị d~1~[v] của các đỉnh "trên đường" là một **mốc** trên trục số. Một đường ngắn nhất đi qua mốc x theo một trong hai cách: dừng ở một đỉnh có d~1~ = x, hoặc đi qua một cạnh (a, b) với d~1~[a] < x < d~1~[b] ("nhảy qua" mốc x).',
        { box: 'theorem', title: 'ĐIỀU KIỆN CẦN VÀ ĐỦ', body: ['Đỉnh v (trên đường) là quan trọng khi và chỉ khi: **không** có đỉnh nào khác trên đường có cùng mốc d~1~[v], và **không** có cạnh-đường-ngắn-nhất nào nhảy qua mốc d~1~[v].', 'Nếu có đỉnh u ≠ v cùng mốc thì đường ngắn nhất qua u không qua v (vì các mốc trên một đường tăng ngặt). Nếu có cạnh (a, b) nhảy qua mốc thì đường 1 → a → b → n là đường ngắn nhất không qua v. Ngược lại, mọi đường ngắn nhất buộc phải "đáp" xuống mốc d~1~[v], và chỉ có v ở đó.'] },
        'Cài đặt: nén các mốc, với mỗi cạnh đường ngắn nhất cộng 1 vào khoảng mốc (l, r) mở bằng **mảng hiệu**, rồi quét.',
        { table: { cols: [1300, 1700, 3000, 2618], head: ['Mốc d₁', 'Các đỉnh', 'Bị nhảy qua bởi', 'Quan trọng?'], rows: [
          ['0', '1', '—', '**1**'], ['2', '2, 3', '—', 'không (hai đỉnh)'], ['5', '4', '—', '**4**'], ['6', '5', 'cạnh 4 – 6 (5 → 7)', 'không'], ['7', '6', 'cạnh 5 – 7 (6 → 10)', 'không'], ['10', '7', '—', '**7**']] } },
        { box: 'def', title: 'CÁCH KHÁC: ĐẾM SỐ ĐƯỜNG ĐI', body: ['Đếm số đường ngắn nhất cnt~1~[v] (từ 1) và cnt~n~[v] (từ n) trong lúc chạy Dijkstra; v quan trọng khi cnt~1~[v] · cnt~n~[v] = cnt~1~[n]. Số đường quá lớn nên phải lấy theo mô-đun một số nguyên tố, và khi đó có (rất nhỏ) khả năng hai số khác nhau trùng mô-đun. Trên bộ test của sách, cách này cũng được **{{S:NUTGIAO_3demduong}} điểm**.'] },
      ],
      optimal: [
        { file: 'NUTGIAO', title: 'NUTGIAO.CPP: hai lần Dijkstra + quét mốc bằng mảng hiệu' },
        { cx: 'hai lần Dijkstra O(m log n), sắp xếp mốc O(n log n), quét O(n + m log n).' },
      ],
      traps: ['**"Trên một đường" khác "trên mọi đường".**', '**Quên kiểm tra cạnh theo cả hai chiều** (đồ thị vô hướng: cạnh (u, v) có thể được dùng theo chiều v → u).', '**So sánh khoảng cách khi một trong hai là vô cùng:** cộng LLONG_MAX sẽ tràn số.'],
      approaches: [['NUTGIAO_1xoadinh', 'Xóa thử từng đỉnh'], ['NUTGIAO_2motduong', 'Chỉ kiểm tra d₁[v] + dₙ[v] = D'], ['NUTGIAO_3demduong', 'Đếm số đường đi theo mô-đun'], ['NUTGIAO', 'Quét mốc bằng mảng hiệu']],
    },
    // ================================================================ 5.3
    {
      id: '5.3', key: 'Dijkstra theo thời điểm tới; tính chuyến kế tiếp bằng công thức.',
      understand: [
        'Mỗi tuyến là một cung có "trọng số" **phụ thuộc thời điểm**: nếu tới bến u lúc t, ta phải chờ chuyến kế tiếp rồi mới đi w phút. Đỉnh là bến, nhãn d[v] là **thời điểm sớm nhất** có mặt ở v.',
        { fig: 'tap2:xebuyt', w: 5.4, cap: 'Ví dụ: chờ chuyến lúc 20 ở bến 2, về tới bến 4 lúc 32.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Nới lỏng mọi tuyến tới khi ổn định',
        body: [
          'Giống Bellman-Ford: lặp đi lặp lại việc duyệt mọi tuyến, cập nhật thời điểm tới, cho tới khi không còn gì thay đổi.',
          { fig: 'f_xebuyt_naive', w: 3.0, cap: 'Sơ đồ khối của cách nới lỏng lặp.' },
          { file: 'XEBUYT_1bellman', title: 'Cách ngây thơ: nới lỏng lặp' },
          { cx: 'mỗi lượt O(m); số lượt có thể tới n. Tổng O(n · m) = 2·10^10^ trong trường hợp xấu nhất.' },
        ],
      },
      stuck: [
        'Nếu các tuyến được liệt kê "ngược chiều" so với đường đi tốt nhất, mỗi lượt chỉ tiến thêm được một bến. Cách này chỉ được **{{S:XEBUYT_1bellman}} điểm** (Subtask 2, n ≤ 1000).',
        'Ở chiều ngược lại, nhiều bạn dùng Dijkstra ngay nhưng quên việc **chờ xe**: coi như tới bến lúc t thì xe chạy ngay lúc t (chỉ kiểm tra t ≤ b). Đúng với Subtask 1 (a = 0, p = 1 nghĩa là xe chạy bất cứ lúc nào) nhưng sai khi có lịch chạy: **{{S:XEBUYT_2dingay}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Dijkstra được chứng minh cho trọng số cố định không âm. Ở đây "trọng số" thay đổi theo thời điểm tới. Dijkstra còn đúng không?'] },
      ],
      breakthrough: [
        { box: 'theorem', title: 'TỚI SỚM KHÔNG BAO GIỜ THIỆT', body: ['Gọi arr(t) là thời điểm tới v nếu rời u lúc t (đi tuyến u → v). Vì có thể chờ ở bến, arr(t) **không giảm** theo t: tới u sớm hơn thì luôn có thể chờ để lên đúng chuyến mà người tới muộn lên. Với tính chất này (gọi là FIFO), lập luận của Dijkstra vẫn đúng nguyên vẹn: khi chốt u với thời điểm nhỏ nhất, không cách nào khác tới u sớm hơn.'] },
        'Chuyến sớm nhất xuất bến không trước t được tính bằng công thức, không lặp từng chuyến:',
        { ul: ['nếu t ≤ a: xuất bến lúc a;', 'ngược lại: xuất bến lúc a + ⌈(t − a) / p⌉ · p;', 'nếu thời điểm xuất bến > b: không đi được tuyến này nữa.'] },
        { table: { cols: [1500, 1900, 3200, 2018], head: ['Chốt bến', 'Thời điểm', 'Tuyến xét', 'Tới'], rows: [
          ['1', '0', '1→2: chuyến 0, tới 10; 1→3: chuyến 10, tới 15', '2: 10, 3: 15'], ['2', '10', '2→4: chuyến 20, tới 32', '4: 32'],
          ['3', '15', '3→4: chuyến 30, tới 33 (không tốt hơn); 3→2: chuyến 15, tới 17 (không tốt hơn)', ''], ['4', '**32**', '', 'đích']] } },
      ],
      optimal: [
        { file: 'XEBUYT', title: 'XEBUYT.CPP: Dijkstra theo thời điểm tới' },
        { cx: 'O(m log n).' },
      ],
      traps: ['**Lặp từng chuyến** để tìm chuyến kế tiếp: p = 1, b − a = 10^9^ thì một lần lặp đã tốn 10^9^ bước.', '**Tràn số** ở biểu thức a + ⌈(t − a)/p⌉ · p khi dùng `int`.', '**Quên điều kiện chuyến cuối b.**'],
      approaches: [['XEBUYT_1bellman', 'Nới lỏng lặp (kiểu Bellman-Ford)'], ['XEBUYT_2dingay', 'Dijkstra, quên chờ xe'], ['XEBUYT', 'Dijkstra theo thời điểm tới']],
    },
    // ================================================================ 6.1
    {
      id: '6.1', key: 'Trọng số −log r, chu trình âm với mọi đỉnh là nguồn.',
      understand: [
        'Mỗi loại tiền là một đỉnh, mỗi quầy là một cung u → v có hệ số r. Đổi qua một vòng nhân số tiền với **tích** các hệ số; vòng đổi có lãi khi tích > 1. Bellman-Ford làm việc với **tổng**, nên cần một phép biến đổi.',
        { fig: 'tap2:doitien', w: 5.4, cap: 'Hai ví dụ của đề.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Thử các vòng ngắn',
        body: [
          'Với n ≤ 3, mọi vòng đổi đơn chỉ gồm 2 hoặc 3 quầy: thử hết các bộ quầy nối thành vòng.',
          { fig: 'f_doitien_naive', w: 2.8, cap: 'Sơ đồ khối của cách thử các vòng ngắn.' },
          { file: 'DOITIEN_1vongngan', title: 'Cách ngây thơ: thử mọi vòng 2 và 3 quầy' },
          { cx: 'O(m^3^). Với m = 10^4^ là 10^12^.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n ≤ 3): **{{P:DOITIEN_1vongngan:1}} điểm**.', '**Subtask 2**: vòng có thể dài tới n = 100 quầy, và m lớn: không thể thử hết.'] },
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Tích các hệ số không phải là thứ Bellman-Ford biết xử lí. Cần chuyển "tích > 1" thành một điều kiện về **tổng**.'] },
      ],
      breakthrough: [
        'Lấy logarit: r~1~ · r~2~ · ... · r~k~ > 1 ⟺ ln r~1~ + ... + ln r~k~ > 0 ⟺ (−ln r~1~) + ... + (−ln r~k~) < 0. Đặt trọng số cung là **−ln r**, vòng có lãi chính là **chu trình âm**.',
        { table: { cols: [2000, 1800, 2400, 2418], head: ['Quầy (ví dụ 1)', 'r', '−ln r', ''], rows: [['1 → 2', '0,9', '+0,1054', ''], ['2 → 3', '1,2', '−0,1823', ''], ['3 → 1', '0,95', '+0,0513', ''], ['Tổng', '', '**−0,0256 < 0**', 'chu trình âm: YES']] } },
        { box: 'theorem', title: 'VÒNG LÃI CÓ THỂ KHÔNG TỚI ĐƯỢC TỪ LOẠI TIỀN 1', body: ['Bellman-Ford từ một nguồn chỉ phát hiện chu trình âm **tới được** từ nguồn. Đề không có "nguồn": khởi tạo d[v] = 0 cho **mọi** v (tương đương thêm một đỉnh ảo nối tới mọi đỉnh với trọng số 0). Chạy Bellman-Ford chỉ từ loại tiền 1 là một lỗi thật sự: trên bộ test của sách, cách đó chỉ được **{{S:DOITIEN_2tumot}} điểm**.'] },
      ],
      optimal: [
        { file: 'DOITIEN', title: 'DOITIEN.CPP: Bellman-Ford với trọng số −ln r' },
        { cx: 'O(n · m) = 10^6^.' },
      ],
      traps: ['**So sánh số thực không có sai số:** dùng d[u] + w < d[v] − 10^−9^ để tránh vòng lặp do sai số làm tròn.', '**Chỉ xuất phát từ loại tiền 1.**', '**Nhân trực tiếp các tỉ giá** trong n lượt: vẫn làm được (tìm "đường đi có tích lớn nhất"), nhưng phải cẩn thận tràn số thực khi tỉ giá lớn.'],
      approaches: [['DOITIEN_1vongngan', 'Thử các vòng 2 và 3 quầy'], ['DOITIEN_2tumot', 'Bellman-Ford chỉ từ loại tiền 1'], ['DOITIEN', 'Bellman-Ford, mọi đỉnh là nguồn']],
    },
    // ================================================================ 6.2
    {
      id: '6.2', key: 'Bellman-Ford đúng k lượt, mỗi lượt từ bản sao.',
      understand: [
        'Đường đi rẻ nhất với **không quá k cạnh**. Dijkstra không biết đếm số cạnh; Bellman-Ford thì có: sau lượt thứ i, nếu cài đặt đúng, d[v] chính là giá rẻ nhất dùng không quá i cạnh.',
        { fig: 'tap2:bayre', w: 5.4, cap: 'Cùng một mạng bay, k = 2 và k = 3 cho hai đáp số khác nhau.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Dijkstra, bỏ qua giới hạn',
        body: [
          'Cách đầu tiên nhiều bạn viết là Dijkstra thông thường, "hi vọng" đường rẻ nhất không quá dài.',
          { file: 'BAYRE_1dijkstra', title: 'Cách ngây thơ: Dijkstra không quan tâm tới k' },
          'Ở ví dụ 1 (k = 2), Dijkstra tìm ra đường 1 → 3 → 2 → 4 giá 170 nhưng dùng 3 chuyến: sai.',
        ],
      },
      stuck: [
        'Dijkstra chỉ đúng ở Subtask 1, nơi k ≥ n − 1 khiến giới hạn không có tác dụng: **{{S:BAYRE_1dijkstra}} điểm**.',
        'Chuyển sang Bellman-Ford chạy đúng k lượt là hướng đúng, nhưng nếu nới lỏng **ngay trên mảng d** thì trong cùng một lượt, một giá trị vừa được cập nhật có thể lập tức được dùng để cập nhật tiếp: một lượt "đi" được nhiều cạnh. Ở ví dụ 1, lượt đầu đã có d[2] = 70 (qua 3) và nếu chuyến 2 → 4 được xét sau đó thì d[4] = 170 ngay sau 2 lượt. Cách này cũng chỉ được **{{S:BAYRE_2khongsaochep}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Ý nghĩa "sau lượt i, d dùng không quá i cạnh" chỉ đúng khi mọi phép nới lỏng của lượt i đều xuất phát từ kết quả của lượt i − 1.'] },
      ],
      breakthrough: [
        'Mỗi lượt, sao chép d thành nd, chỉ đọc từ d và ghi vào nd, cuối lượt gán d = nd. Có thể dừng sớm khi một lượt không thay đổi gì.',
        { table: { cols: [1800, 3600, 3218], head: ['Lượt', 'd[1..4]', 'Ý nghĩa'], rows: [['0', '0, ∞, ∞, ∞', 'chưa bay'], ['1', '0, 100, 50, ∞', '≤ 1 chuyến'], ['2', '0, 70, 50, **200**', '≤ 2 chuyến: đáp số ví dụ 1'], ['3', '0, 70, 50, **170**', '≤ 3 chuyến: đáp số ví dụ 2']] } },
        { fig: 'f_bayre_opt', w: 3.0, cap: 'Sơ đồ khối của Bellman-Ford k lượt.' },
      ],
      optimal: [
        { file: 'BAYRE', title: 'BAYRE.CPP: Bellman-Ford k lượt có sao chép' },
        { cx: 'O(k · (n + m)) = 10^3^ · 1,1·10^4^ ≈ 10^7^.' },
      ],
      traps: ['**Nới lỏng tại chỗ** (lỗi kinh điển).', '**Cộng với vô cùng:** chỉ nới lỏng khi d[u] hữu hạn.', '**Dừng sớm sai:** chỉ dừng khi cả lượt không có thay đổi nào.'],
      approaches: [['BAYRE_1dijkstra', 'Dijkstra, bỏ qua giới hạn k'], ['BAYRE_2khongsaochep', 'Bellman-Ford k lượt, không sao chép'], ['BAYRE', 'Bellman-Ford k lượt, có sao chép']],
    },
    // ================================================================ 6.3
    {
      id: '6.3', key: 'Hệ ràng buộc hiệu: đường đi dài nhất, phát hiện chu trình dương.',
      understand: [
        'Mỗi ràng buộc là một bất đẳng thức dạng ngày[y] ≥ ngày[x] + c:',
        { ul: ['Loại 1 "A sau B ít nhất c ngày": ngày[A] ≥ ngày[B] + c, cung B → A nhãn c.', 'Loại 2 "A không muộn hơn B quá c ngày": ngày[A] ≤ ngày[B] + c ⟺ ngày[B] ≥ ngày[A] − c, cung A → B nhãn −c.'] },
        'Ngày sớm nhất của mỗi trận chính là 1 + độ dài **đường đi dài nhất** tới nó trong đồ thị ràng buộc. Một **chu trình có tổng dương** cho ra ngày[A] > ngày[A]: vô nghiệm.',
        { fig: 'tap2:lichthidau', w: 5.4, cap: 'Đồ thị ràng buộc của ví dụ 1.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Quy hoạch động trên DAG',
        body: [
          'Nếu chỉ có ràng buộc loại 1 (cung nhãn không âm, theo một thứ tự ngầm), đồ thị là DAG: sắp xếp tô pô rồi lấy đường đi dài nhất. Cách này bỏ qua ràng buộc loại 2.',
          { file: 'LICHTHIDAU_1kahn', title: 'Cách ngây thơ: đường đi dài nhất trên DAG (bỏ qua loại 2)' },
          { cx: 'O(n + m).' },
        ],
      },
      stuck: [
        'Đúng Subtask 1: **{{S:LICHTHIDAU_1kahn}} điểm**. Ràng buộc loại 2 tạo ra cung nhãn âm và chu trình, không còn là DAG.',
        'Bellman-Ford "lặp tới khi hết thay đổi" xử lí được cả hai loại, nhưng khi có chu trình dương thì vòng lặp **không bao giờ dừng**: **{{S:LICHTHIDAU_2khongdung}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Cần một giới hạn số lượt để phân biệt "chưa hội tụ" với "không bao giờ hội tụ".'] },
      ],
      breakthrough: [
        'Đây là Bellman-Ford cho đường đi **dài nhất** (đổi dấu so sánh). Khởi tạo ngày[v] = 1 tương đương với một đỉnh ảo nối tới mọi đỉnh. Nếu không có chu trình dương, mọi đường đi dài nhất có không quá n cạnh, nên sau n lượt các giá trị phải ổn định. Nếu lượt thứ n + 1 vẫn còn tăng: có chu trình dương, in −1.',
        { box: 'theorem', title: 'VÌ SAO KẾT QUẢ LÀ "SỚM NHẤT CÓ THỂ"?', body: ['Mỗi lần ngày[y] tăng lên ngày[x] + c là do một ràng buộc **bắt buộc** điều đó. Bằng quy nạp, mọi lịch hợp lệ đều có ngày[v] ít nhất bằng giá trị thuật toán tìm ra; và khi thuật toán dừng thì mọi ràng buộc đều thỏa. Vì vậy kết quả đồng thời là sớm nhất cho mọi trận.'] },
        { table: { cols: [1500, 4500, 2618], head: ['Lượt', 'ngày[1..4]', 'Ghi chú'], rows: [['0', '1, 1, 1, 1', 'khởi tạo'], ['1', '1, 4, 6, 2', '2 ≥ 1 + 3; 3 ≥ 4 + 2; 4 ≥ 1 + 1'], ['2', '1, 4, 6, 2', 'không đổi: dừng, 6 ≤ 1 + 6 thỏa']] } },
        { fig: 'f_lichthidau_opt', w: 3.2, cap: 'Sơ đồ khối của lời giải mẫu.' },
      ],
      optimal: [
        { file: 'LICHTHIDAU', title: 'LICHTHIDAU.CPP: Bellman-Ford đường đi dài nhất, n + 1 lượt' },
        { cx: 'O(n · m) = 5·10^6^.' },
      ],
      traps: ['**Đổi chiều cung sai** khi chuyển ràng buộc loại 2.', '**Lặp vô hạn** khi có chu trình dương.', '**Khởi tạo ngày = 0** (đề yêu cầu ngày là số nguyên dương).'],
      approaches: [['LICHTHIDAU_1kahn', 'Đường dài nhất trên DAG (bỏ qua loại 2)'], ['LICHTHIDAU_2khongdung', 'Bellman-Ford lặp tới khi hết thay đổi'], ['LICHTHIDAU', 'Bellman-Ford n + 1 lượt']],
    },
    // ================================================================ 7.1
    {
      id: '7.1', key: 'Floyd với k ở vòng ngoài cùng.',
      understand: [
        'Cần tổng khoảng cách từ mỗi thành phố tới mọi thành phố khác: bài toán đường đi ngắn nhất **giữa mọi cặp**, n ≤ 400: đúng "sân nhà" của thuật toán Floyd (Tập 1, Bài 7).',
        { fig: 'tap2:thudo', w: 5.0, cap: 'Ma trận khoảng cách của ví dụ.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Bellman-Ford từ từng thành phố',
        body: [
          { fig: 'f_thudo_naive', w: 2.8, cap: 'Sơ đồ khối của cách chạy Bellman-Ford n lần.' },
          { file: 'THUDO_1bellman', title: 'Cách ngây thơ: n lần Bellman-Ford' },
          { cx: 'O(n · n · m) = 400 · 400 · 8·10^4^ ≈ 10^10^ trong trường hợp xấu nhất.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n ≤ 50): chạy kịp: **{{P:THUDO_1bellman:1}} điểm**.', '**Subtask 2**: quá thời gian.'] },
        'Một lỗi tai hại khi cài Floyd là đặt vòng k vào **trong cùng** (for i, for j, for k). Chương trình vẫn chạy nhanh và cho kết quả "trông hợp lí", nhưng sai: **{{S:THUDO_2ktrongcung}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Bellman-Ford từ mỗi nguồn làm lại rất nhiều việc chung giữa các nguồn. Floyd chia sẻ công việc giữa mọi cặp đỉnh, nhưng thứ tự vòng lặp phải đúng ý nghĩa quy hoạch động.'] },
      ],
      breakthrough: [
        'Floyd là quy hoạch động: sau khi xử lí k, d[i][j] là đường ngắn nhất từ i tới j chỉ dùng các đỉnh trung gian thuộc {1, ..., k}. Muốn dùng d[i][k] và d[k][j] "đã hoàn chỉnh với tập {1, ..., k − 1}" thì k phải là vòng **ngoài cùng**.',
        { box: 'theorem', title: 'VÌ SAO ĐẶT k TRONG CÙNG LẠI SAI?', body: ['Với thứ tự (i, j, k), khi tính d[i][j] ta dùng d[i][k], d[k][j] của những cặp có thể **chưa** được tối ưu (ví dụ cặp (k, j) với k > i chưa được xét). Đường ngắn nhất cần đi qua hai đỉnh trung gian trở lên có thể bị bỏ sót.'] },
        'Chạy xong Floyd, tính tổng từng hàng (Hình 7.1.1): hàng 2 và hàng 4 cùng có tổng 7; duyệt i tăng dần, chỉ cập nhật khi **nhỏ hơn hẳn**, nên chọn thành phố **2**.',
      ],
      optimal: [
        { file: 'THUDO', title: 'THUDO.CPP: Floyd O(n³)' },
        { cx: 'O(n^3^) = 6,4·10^7^ phép tính đơn giản; O(n^2^) bộ nhớ.' },
      ],
      traps: ['**Vòng k không ở ngoài cùng.**', '**INF quá lớn:** INF + INF tràn `long long` nếu INF = LLONG_MAX; dùng LLONG_MAX / 4.', '**Nhiều con đường giữa cùng một cặp:** khởi tạo bằng `min`, không gán đè.'],
      approaches: [['THUDO_1bellman', 'Bellman-Ford từ từng thành phố'], ['THUDO_2ktrongcung', 'Floyd, vòng k ở trong cùng'], ['THUDO', 'Floyd, vòng k ở ngoài cùng']],
    },
    // ================================================================ 7.2
    {
      id: '7.2', key: 'Bao đóng bắc cầu bằng bitset.',
      understand: [
        'Quan hệ "mạnh hơn" có tính bắc cầu: a thắng b, b thắng c thì chắc chắn a mạnh hơn c. Kì thủ v xác định được thứ hạng khi với **mọi** u ≠ v, ta biết chắc u mạnh hơn hay yếu hơn v: (số người chắc chắn yếu hơn v) + (số người chắc chắn mạnh hơn v) = n − 1.',
        { fig: 'tap2:xephang', w: 4.6, cap: 'Ví dụ: chỉ kì thủ 2 và 5 xác định được thứ hạng.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Bao đóng bắc cầu kiểu Floyd',
        body: [
          { fig: 'f_xephang_naive', w: 3.0, cap: 'Sơ đồ khối của bao đóng bắc cầu kiểu Floyd.' },
          { file: 'XEPHANG_1floyd', title: 'Cách ngây thơ: Floyd trên ma trận bool' },
          { cx: 'O(n^3^): n = 500 là 1,25·10^8^, chạy kịp; n = 2000 là 8·10^9^.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1, 2** (n ≤ 500): **{{P:XEPHANG_1floyd:1}} + {{P:XEPHANG_1floyd:2}} điểm**.', '**Subtask 3** (n ≤ 2000): quá thời gian.'] },
        'Một lời giải sai: chỉ dùng các kết quả **trực tiếp** (v đã đấu với cả n − 1 người). Ở ví dụ, kì thủ 5 chỉ đấu một trận nhưng vẫn xác định được hạng: **{{S:XEPHANG_2tructiep}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Phép "r[i][j] = r[i][j] or (r[i][k] and r[k][j])" xử lí từng ô một, trong khi với cùng i, k, ta đang "or" cả **hàng** k vào hàng i.'] },
      ],
      breakthrough: [
        'Lưu mỗi hàng của ma trận là một `bitset<2001>`. Khi r[i][k] = 1, mọi người k mạnh hơn cũng yếu hơn i: `r[i] |= r[k]`, một phép toán trên 2001 bit thực hiện bằng khoảng 32 phép toán 64 bit.',
        'Số người chắc chắn yếu hơn v là `r[v].count()`; số người chắc chắn mạnh hơn v là số u có r[u][v] = 1.',
        { table: { cols: [1500, 2700, 2700, 1718], head: ['Kì thủ', 'Chắc chắn yếu hơn', 'Chắc chắn mạnh hơn', 'Tổng'], rows: [['1', '2, 5', '—', '2'], ['2', '5', '1, 3, 4', '**4 = n − 1**'], ['3', '2, 5', '4', '3'], ['4', '3, 2, 5', '—', '3'], ['5', '—', '1, 2, 3, 4', '**4 = n − 1**']] } },
      ],
      optimal: [
        { file: 'XEPHANG', title: 'XEPHANG.CPP: bao đóng bắc cầu bằng bitset' },
        { cx: 'O(n^3^ / 64) ≈ 1,25·10^8^ phép toán 64 bit; bộ nhớ n^2^ bit = 0,5 MB.' },
        { box: 'def', title: 'CÁCH KHÁC', body: ['DFS từ mỗi kì thủ trên đồ thị "thắng" (và trên đồ thị ngược) để đếm số người tới được: O(n · (n + m)) ≈ 2·10^8^ cũng chạy kịp với giới hạn của bài.'] },
      ],
      traps: ['**Chỉ dùng kết quả trực tiếp.**', '**Quên phần "mạnh hơn":** chỉ đếm số người yếu hơn là chưa đủ.', '**Khai báo `bool r[2001][2001]` và dùng ba vòng lặp:** đúng nhưng chậm gấp khoảng 64 lần.'],
      approaches: [['XEPHANG_1floyd', 'Floyd trên ma trận bool'], ['XEPHANG_2tructiep', 'Chỉ dùng kết quả trực tiếp'], ['XEPHANG', 'Bao đóng bắc cầu bằng bitset']],
    },
    // ================================================================ 7.3
    {
      id: '7.3', key: 'Floyd với (max, min).',
      understand: [
        'Tải trọng của một đường đi là tải trọng của con đường **yếu nhất** trên đó; cần đường có tải trọng **lớn nhất** giữa hai thị trấn. Đây là bài toán "đường đi có cạnh nhỏ nhất lớn nhất" (bottleneck path), cho rất nhiều cặp (s, t).',
        { fig: 'tap2:xetai', w: 4.4, cap: 'Từ 1 tới 4, đường 1 → 2 → 3 → 4 chịu được 5 tấn.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Tìm nhị phân + DFS cho từng đơn hàng',
        body: [
          'Với một W cố định, "chở được W tấn từ s tới t" khi s, t liên thông trong đồ thị chỉ gồm các con đường chịu ≥ W. Tính chất này đơn điệu theo W, nên tìm nhị phân W.',
          { fig: 'f_xetai_naive', w: 3.0, cap: 'Sơ đồ khối của cách tìm nhị phân cho từng đơn hàng.' },
          { file: 'XETAI_1moicauhoi', title: 'Cách ngây thơ: tìm nhị phân + DFS mỗi câu hỏi' },
          { cx: 'O(q · log C · (n + m)) ≈ 10^5^ · 30 · 10^5^: quá lớn.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n, q ≤ 50): **{{P:XETAI_1moicauhoi:1}} điểm**.', '**Subtask 2**: quá thời gian.'] },
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Có tới 10^5^ câu hỏi nhưng chỉ có n^2^ = 2,5·10^5^ cặp đỉnh khác nhau: tính trước đáp số cho **mọi cặp** rồi trả lời O(1).'] },
      ],
      breakthrough: [
        'Floyd không chỉ dành cho "tổng nhỏ nhất". Gọi b[i][j] là tải trọng lớn nhất từ i tới j dùng đỉnh trung gian thuộc {1, ..., k}. Đi qua k thì tải trọng là min(b[i][k], b[k][j]); vì vậy:',
        { ul: ['**b[i][j] = max(b[i][j], min(b[i][k], b[k][j]))**, với k ở vòng ngoài cùng.'] },
        'Lập luận đúng đắn giống hệt Floyd thông thường; chỉ cần thay (min, +) bằng (max, min).',
        { table: { cols: [2200, 3200, 3218], head: ['Cặp (ví dụ)', 'Sau Floyd', 'Đường tương ứng'], rows: [['(1, 4)', '**5**', '1 – 2 – 3 – 4: min(10, 5, 8)'], ['(1, 5)', '**2**', 'phải qua 4 – 5 (2 tấn)'], ['(3, 1)', '**5**', '3 – 2 – 1: min(5, 10)']] } },
        { box: 'def', title: 'CÁCH KHÁC: CÂY KHUNG LỚN NHẤT', body: ['Đường đi tốt nhất giữa s và t luôn nằm trên **cây khung lớn nhất** (Tập 1, Bài 10). Dựng cây bằng Kruskal (cạnh nặng trước), rồi DFS từ mỗi đỉnh trên cây để có đáp số cho mọi cặp trong O(n^2^). Cách này cũng được **{{S:XETAI_2caykhung}} điểm**.'] },
      ],
      optimal: [
        { file: 'XETAI', title: 'XETAI.CPP: Floyd (max, min)' },
        { cx: 'O(n^3^ + m + q) ≈ 1,25·10^8^ phép tính đơn giản.' },
      ],
      traps: ['**Nhiều con đường giữa một cặp:** giữ con đường chịu tải **lớn nhất** (dùng max khi khởi tạo).', '**Nhầm min và max** khi chuyển từ Floyd thông thường.', '**b[i][i]:** không cần quan tâm vì đề đảm bảo s ≠ t.'],
      approaches: [['XETAI_1moicauhoi', 'Tìm nhị phân + DFS mỗi đơn hàng'], ['XETAI_2caykhung', 'Cây khung lớn nhất + DFS từ mỗi đỉnh'], ['XETAI', 'Floyd (max, min)']],
    },
    // ================================================================ 8.1
    {
      id: '8.1', key: 'BFS trên trạng thái (nút, t mod P).',
      understand: [
        'Đèn đổi màu theo thời gian nên **vị trí** thôi chưa đủ mô tả tình huống: tới nút u lúc 3 (đèn xanh) khác với tới u lúc 4 (đèn đỏ). Nhưng đèn lặp lại theo chu kì P, nên chỉ cần biết t **mod P**. Trạng thái là cặp (u, t mod P): có n · P ≤ 6·10^5^ trạng thái.',
        { fig: 'tap2:dengiaothong', w: 5.4, cap: 'Ví dụ: xe phải đứng chờ một phút ở nút 3.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Mô phỏng từng phút',
        body: [
          'Giữ tập các nút xe có thể đang có mặt ở phút t (vì được chờ, tập này chỉ lớn dần). Mỗi phút, từ các nút đang đèn xanh, thêm các nút kề.',
          { fig: 'f_dengiaothong_naive', w: 3.2, cap: 'Sơ đồ khối của cách mô phỏng từng phút.' },
          { file: 'DENGIAOTHONG_2mophong', title: 'Cách ngây thơ: mô phỏng từng phút' },
          { cx: 'mỗi phút O(n + m), số phút tới n · P: O(n · P · (n + m)).' },
        ],
      },
      stuck: [
        'Mô phỏng chạy tốt khi n nhỏ (Subtask 2) hoặc khi đáp số nhỏ, nhưng với n = 10^4^, P = 60 và đường đi dài thì quá chậm: **{{S:DENGIAOTHONG_2mophong}} điểm**.',
        'Một lời giải nhanh nhưng sai: BFS thường trên các **nút**, đánh dấu nút đã thăm theo lần tới đầu tiên, chờ đèn xanh rồi đi tiếp. Sai ở chỗ "lần tới đầu tiên" theo thứ tự BFS chưa chắc là **thời điểm** sớm nhất (vì thời gian chờ khác nhau ở mỗi nút): **{{S:DENGIAOTHONG_1khongcho}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Thời gian đã trở thành một phần của "vị trí". Cần một đồ thị mà mỗi bước đi (kể cả bước chờ) đều tốn đúng 1 phút.'] },
      ],
      breakthrough: [
        'Đồ thị trạng thái: từ (u, r) có thể', { ul: ['**chờ**: sang (u, (r + 1) mod P);', '**đi** sang (v, (r + 1) mod P) với mọi v kề u, nếu s~u~[r] = 1 (đèn xanh).'] },
        'Mọi bước tốn 1 phút, nên BFS từ (1, 0) cho thời điểm sớm nhất tới mỗi trạng thái. Trạng thái đầu tiên có u = n được lấy ra cho đáp số.',
        { table: { cols: [1600, 2400, 4618], head: ['Phút', 'Trạng thái lấy ra', 'Đi tới'], rows: [['0', '(1, 0)', 'đèn 1 xanh: (2, 1), (3, 1); chờ: (1, 1)'], ['1', '(2, 1), (3, 1), (1, 1)', 'đèn 2, 3 đỏ, đèn 1 đỏ: chỉ chờ, (2, 2), (3, 2), (1, 2)'], ['2', '(3, 2), ...', 'đèn 3 xanh: (4, 0)'], ['3', '(4, 0)', 'đích: **3**']] } },
        { box: 'def', title: 'MỞ RỘNG: DIJKSTRA THEO THỜI ĐIỂM TỚI', body: ['Vì được chờ tùy ý, tới sớm không bao giờ thiệt (giống bài 5.3). Có thể chạy Dijkstra trên các nút với nhãn "thời điểm tới sớm nhất", mỗi lần rời u thì chờ tới phút xanh gần nhất. Cách nhìn đồ thị trạng thái tổng quát hơn: nó vẫn dùng được khi **không** được chờ ở một số nút.'] },
      ],
      optimal: [
        { file: 'DENGIAOTHONG', title: 'DENGIAOTHONG.CPP: BFS trên trạng thái (nút, t mod P)' },
        { cx: 'O(P · (n + m)) ≈ 60 · 3·10^4^ = 1,8·10^6^.' },
      ],
      traps: ['**Đánh dấu theo nút** thay vì theo trạng thái.', '**Quên bước "chờ"**: khi mọi nút kề đều đang đỏ thì xe kẹt mãi.', '**n = 1:** đáp số là 0.'],
      approaches: [['DENGIAOTHONG_1khongcho', 'BFS trên nút, đánh dấu theo nút'], ['DENGIAOTHONG_2mophong', 'Mô phỏng từng phút'], ['DENGIAOTHONG', 'BFS trên trạng thái (nút, t mod P)']],
    },
    // ================================================================ 8.2
    {
      id: '8.2', key: 'BFS trên trạng thái (ô, số tường đã phá).',
      understand: [
        'Mê cung có thêm "tài nguyên": tối đa k lần phá tường. Hai lần có mặt ở cùng một ô nhưng còn số búa khác nhau là **hai tình huống khác nhau**: lần tới sau có thể đi được những nơi lần tới trước không đi được.',
        { fig: 'tap2:phatuong', w: 5.0, cap: 'Có búa đi thẳng 6 bước; không có búa phải đi vòng 8 bước.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Thử mọi tập tường bị phá',
        body: [
          'Chọn trước tập không quá k bức tường sẽ phá, xóa chúng khỏi bản đồ rồi BFS thường. Thử mọi tập.',
          { fig: 'f_phatuong_naive', w: 3.0, cap: 'Sơ đồ khối của cách thử mọi tập tường.' },
          { file: 'PHATUONG_2thutuong', title: 'Cách ngây thơ: thử mọi tập ≤ k tường' },
          { cx: 'O(W^k^ · R · C) với W là số bức tường: k = 0 hoặc 1 thì chạy được, k ≥ 2 thì bùng nổ.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (k = 0) và **Subtask 2** (k = 1, tối đa 10^4^ lần BFS 10^4^ ô): chạy kịp.', '**Subtask 3** (k tới 10): quá thời gian.'] },
        'Được **{{S:PHATUONG_2thutuong}} điểm**. Một lời giải nhanh nhưng sai: BFS thường, đánh dấu theo **ô**, nhớ số búa đã dùng của lần tới đầu tiên. Khi đường ngắn tới một ô đã dùng hết búa còn đường dài hơn vẫn còn búa, lời giải này bỏ mất đường dài: **{{S:PHATUONG_1theoo}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['"Đã thăm ô (x, y)" là chưa đủ: phải nói rõ đã thăm (x, y) **với bao nhiêu búa đã dùng**.'] },
      ],
      breakthrough: [
        'Trạng thái (x, y, j): đang ở ô (x, y), đã phá j bức tường, 0 ≤ j ≤ k. Có R · C · (k + 1) ≤ 1,1·10^5^ trạng thái. Bước vào ô trống: giữ nguyên j; bước vào ô tường: j tăng 1 (chỉ khi j < k). Mọi bước tốn 1 nên dùng BFS; trạng thái đầu tiên ở ô T là đáp số.',
        'Ở ví dụ 1 (k = 1): (1, 1, 0) → (1, 2, 0) → phá tường (1, 3, 1) → (1, 4, 1) → (2, 4, 1) → (3, 4, 1) → (3, 5, 1) = T sau **6** bước. Với k = 0, trạng thái (1, 3, 1) không được phép, BFS phải đi vòng: **8** bước.',
      ],
      optimal: [
        { file: 'PHATUONG', title: 'PHATUONG.CPP: BFS trên trạng thái (ô, số tường đã phá)' },
        { cx: 'O(R · C · k).' },
      ],
      traps: ['**Đánh dấu theo ô** (mất điểm ở những test có "búa quý").', '**Coi ô S, T là tường** hoặc quên chúng là ô trống.', '**Phá tường mà không tính bước:** bước vào ô vừa phá cũng tốn 1 bước.'],
      approaches: [['PHATUONG_1theoo', 'BFS thường, đánh dấu theo ô'], ['PHATUONG_2thutuong', 'Thử mọi tập ≤ k tường + BFS'], ['PHATUONG', 'BFS trên trạng thái (ô, số tường đã phá)']],
    },
    // ================================================================ 8.3
    {
      id: '8.3', key: 'BFS 0-1 trên trạng thái (ô, hướng).',
      understand: [
        'Trạng thái của robot gồm ô đang đứng và **hướng** đang quay mặt: (x, y, k) với k ∈ {N, E, S, W}, tổng cộng 4 · R · C ≤ 4·10^6^ trạng thái. Có hai loại bước: tiến (miễn phí) và xoay (tốn 1). Ta cần đường đi có **tổng chi phí** nhỏ nhất, không phải ít bước nhất.',
        { fig: 'tap2:robotxoay', w: 4.6, cap: 'Ví dụ: hai lần xoay ở các ô vàng.' },
      ],
      naive: {
        title: 'Cách ngây thơ: BFS thường trên trạng thái',
        body: [
          'BFS coi mọi thao tác (tiến và xoay) đều tốn 1, rồi in số lần xoay trên đường ít **thao tác** nhất tìm được.',
          { file: 'ROBOTXOAY_1bfsthuong', title: 'Cách sai: BFS coi mọi thao tác như nhau' },
          { cx: 'O(R · C), nhanh nhưng tối ưu sai đại lượng.' },
        ],
      },
      stuck: [
        'Đường ít thao tác nhất thường không phải đường ít lần xoay nhất (một đường thẳng dài chỉ tốn 0 nhưng có nhiều bước tiến): **{{S:ROBOTXOAY_1bfsthuong}} điểm**.',
        'Sửa bằng Dijkstra trên đồ thị trạng thái với trọng số 0/1: đúng, và với giới hạn 2 giây vẫn chạy kịp trên bộ test của sách: **{{S:ROBOTXOAY_2dijkstra}} điểm**. Tuy nhiên hàng đợi ưu tiên với 4·10^6^ trạng thái khá nặng.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Trọng số chỉ là 0 hoặc 1: hàng đợi ưu tiên "quá mạnh" cho bài này. Có cấu trúc nào đơn giản như BFS mà vẫn xử lí được cạnh trọng số 0?'] },
      ],
      breakthrough: [
        '**BFS 0-1** (Tập 1, Bài 8): dùng `deque`. Cạnh trọng số 0 (tiến) đẩy trạng thái mới vào **đầu**, cạnh trọng số 1 (xoay) đẩy vào **cuối**. Hàng đợi khi đó luôn chứa các nhãn thuộc {d, d + 1}, đóng vai trò hàng đợi ưu tiên với chi phí O(1) mỗi thao tác.',
        { table: { cols: [2600, 2400, 3618], head: ['Lấy ra (ví dụ)', 'Chi phí', 'Đẩy vào'], rows: [['(1, 1, E)', '0', 'tiến (1, 2, E) vào đầu; xoay (1, 1, N), (1, 1, S) vào cuối'], ['(1, 2, E) ... (1, 5, E)', '0', 'tiến tới cuối hàng; xoay ở (1, 5)'], ['(1, 5, S)', '1', 'tiến (2, 5, S), (3, 5, S) vào đầu'], ['(3, 5, W)', '2', 'tiến (3, 4, W), (3, 3, W) = T: **2**']] } },
        { fig: 'f_robotxoay_opt', w: 3.0, cap: 'Sơ đồ khối của BFS 0-1.' },
      ],
      optimal: [
        { file: 'ROBOTXOAY', title: 'ROBOTXOAY.CPP: BFS 0-1 trên trạng thái (ô, hướng)' },
        { cx: 'O(R · C), mỗi trạng thái được lấy ra một số ít lần.' },
      ],
      traps: ['**BFS thường** tối ưu số thao tác thay vì số lần xoay.', '**Đẩy cạnh 0 vào cuối deque:** thứ tự bị phá vỡ, kết quả sai.', '**Bộ nhớ:** 4·10^6^ trạng thái; dùng mảng một chiều, mã hóa (x, y, k) thành một số.'],
      approaches: [['ROBOTXOAY_1bfsthuong', 'BFS thường (mọi thao tác như nhau)'], ['ROBOTXOAY_2dijkstra', 'Dijkstra trên trạng thái'], ['ROBOTXOAY', 'BFS 0-1 trên trạng thái']],
    },
  ],
};
