// TẬP 3 — CHƯƠNG 3. CÂY VÀ CÂY KHUNG
module.exports = {
  no: 3,
  intro: 'Các bài tập chương 3 xoay quanh ba công cụ: DSU, cây khung nhỏ nhất và nhảy nhị phân trên cây. Cách ngây thơ thường là "làm lại từ đầu sau mỗi thay đổi" hoặc "duyệt lại cây cho mỗi câu hỏi". Những lời giải "trông như đúng" thì hay mất điểm vì DSU không cân bằng, vì quên một loại thông tin (cáp có sẵn, quan hệ khác phe), vì đệ quy quá sâu hoặc vì bảng nhảy nhị phân chiếm quá nhiều bộ nhớ.',
  solutions: [
    // ================================================================ 9.1
    {
      id: '9.1', key: 'DSU nén đường đi + gộp theo kích thước, duy trì cnt và best.',
      understand: [
        'Mỗi lần kết bạn là thêm một cạnh; nhóm bạn là thành phần liên thông. Sau mỗi cạnh mới, cần số thành phần và kích thước thành phần lớn nhất. Các nhóm chỉ **lớn dần**, không bao giờ tách ra: đúng sở trường của DSU (Tập 1, Bài 9).',
        { fig: 'tap2:mangbanbe', w: 6.0, cap: 'Các nhóm bạn của ví dụ sau từng sự kiện.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Duyệt lại cả đồ thị sau mỗi sự kiện',
        body: [
          { fig: 'f_mangbanbe_naive', w: 2.8, cap: 'Sơ đồ khối của cách duyệt lại.' },
          { file: 'MANGBANBE_1bfs', title: 'Cách ngây thơ: DFS lại toàn bộ sau mỗi sự kiện' },
          { cx: 'O(m · (n + m)). Với n = m = 1000 khoảng 2·10^6^; với 2·10^5^ là 8·10^10^.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n, m ≤ 1000): **{{P:MANGBANBE_1bfs:1}} điểm**.', '**Subtask 2**: quá thời gian.'] },
        'Chuyển sang DSU là đúng hướng, nhưng DSU **không cân bằng** (gộp tùy tiện, không nén đường đi) có thể suy biến thành một chuỗi dài. Với dãy sự kiện (1, 2), (1, 3), (1, 4), ..., mỗi lần gộp lại treo cả chuỗi vào một đỉnh mới, và `root(1)` phải đi hết chuỗi: tổng O(n^2^). Được **{{S:MANGBANBE_2dsuthuong}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['DSU chỉ nhanh khi cây của nó **thấp**. Cần hai kĩ thuật giữ cây thấp: gộp cây nhỏ vào cây lớn, và nén đường đi khi tìm gốc.'] },
      ],
      breakthrough: [
        { ul: ['**Gộp theo kích thước:** luôn treo gốc của nhóm nhỏ vào gốc của nhóm lớn. Một đỉnh chỉ bị "đẩy sâu" thêm 1 khi nhóm của nó ít nhất gấp đôi, nên độ sâu không quá log~2~ n.', '**Nén đường đi:** khi tìm gốc, cho mỗi đỉnh trên đường trỏ thẳng (hoặc nhảy hai bậc) lên trên. Kết hợp hai kĩ thuật, mỗi thao tác gần như O(1).'] },
        'Giữ thêm hai biến: cnt (số nhóm, ban đầu n, giảm 1 mỗi lần gộp **thành công**) và best (kích thước lớn nhất; vì nhóm không bao giờ nhỏ đi nên chỉ cần max với kích thước nhóm vừa gộp).',
        { table: { cols: [1600, 3000, 2000, 2018], head: ['Sự kiện', 'Gộp', 'cnt', 'best'], rows: [['1 2', '{1} + {2}', '4', '2'], ['3 4', '{3} + {4}', '3', '2'], ['2 1', 'đã cùng nhóm', '3', '2'], ['2 3', '{1, 2} + {3, 4}', '2', '4'], ['4 5', '{1, 2, 3, 4} + {5}', '1', '5']] } },
        { fig: 'f_mangbanbe_opt', w: 3.0, cap: 'Sơ đồ khối xử lí một sự kiện.' },
      ],
      optimal: [
        { file: 'MANGBANBE', title: 'MANGBANBE.CPP: DSU cân bằng' },
        { cx: 'O((n + m) · α(n)), gần như tuyến tính.' },
      ],
      traps: ['**Giảm cnt cả khi hai bạn đã cùng nhóm** (sự kiện lặp).', '**DSU đệ quy** `root(x) = p[x] = root(p[x])` khi chưa gộp theo kích thước: chuỗi dài làm tràn ngăn xếp.', '**Quên cập nhật best** sau khi gộp.'],
      approaches: [['MANGBANBE_1bfs', 'Duyệt lại cả đồ thị sau mỗi sự kiện'], ['MANGBANBE_2dsuthuong', 'DSU không cân bằng, không nén'], ['MANGBANBE', 'DSU nén đường đi + gộp theo kích thước']],
    },
    // ================================================================ 9.2
    {
      id: '9.2', key: 'Đi ngược thời gian: phá cầu thành xây cầu.',
      understand: [
        'Các cây cầu lần lượt **biến mất**, ta cần số thành phần liên thông sau mỗi lần. DSU chỉ gộp được, không tách được. Nhưng nếu nhìn **ngược thời gian**, các cây cầu lần lượt **xuất hiện**: đúng việc DSU làm tốt.',
        { fig: 'tap2:phacau', w: 6.0, cap: 'Ví dụ: đi ngược từ phải sang trái là xây lại từng cây cầu.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Dựng lại DSU sau mỗi lần sập',
        body: [
          { fig: 'f_phacau_naive', w: 2.8, cap: 'Sơ đồ khối của cách dựng lại.' },
          { file: 'PHACAU_1demlai', title: 'Cách ngây thơ: dựng lại DSU từ các cầu còn lại' },
          { cx: 'O(q · (n + m)).' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n, m ≤ 1000): **{{P:PHACAU_1demlai:1}} điểm**.', '**Subtask 2**: 2·10^5^ lần dựng lại, mỗi lần 4·10^5^ thao tác: quá thời gian.'] },
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Phải "tách" một nhóm khi cầu sập, mà DSU không làm được điều đó. Muốn dùng DSU, cần đổi bài toán để chỉ còn thao tác **gộp**.'] },
      ],
      breakthrough: [
        'Ta biết **trước** toàn bộ danh sách cầu sẽ sập (bài toán **ngoại tuyến**). Bắt đầu từ trạng thái **cuối cùng** (mọi cầu trong danh sách đã sập), rồi đi ngược: với j = q, q − 1, ..., 1, ghi lại số nhóm hiện tại làm đáp số thứ j (đó là trạng thái ngay **sau** khi cầu k~j~ sập), rồi **xây lại** cầu k~j~.',
        { table: { cols: [1500, 2000, 2400, 2718], head: ['Bước ngược', 'Ghi đáp số', 'Xây lại', 'Các nhóm sau đó'], rows: [
          ['khởi đầu', '', 'cầu 3, 5 (không bao giờ sập)', '{1, 3}, {2}, {4, 5}'], ['j = 4', 'ans[4] = **3**', 'cầu 2 (2 – 3)', '{1, 2, 3}, {4, 5}'],
          ['j = 3', 'ans[3] = **2**', 'cầu 6 (5 – 3)', '{1, 2, 3, 4, 5}'], ['j = 2', 'ans[2] = **1**', 'cầu 1', 'không đổi'], ['j = 1', 'ans[1] = **1**', 'cầu 4', 'không đổi']] } },
        'In theo thứ tự j = 1..q: 1, 1, 2, 3, khớp với ví dụ.',
        { fig: 'f_phacau_opt', w: 2.8, cap: 'Sơ đồ khối của lời giải ngược thời gian.' },
      ],
      optimal: [
        { file: 'PHACAU', title: 'PHACAU.CPP: DSU, đi ngược thời gian' },
        { cx: 'O((n + m + q) · α(n)).' },
      ],
      traps: ['**Ghi đáp số sau khi xây lại** (lệch một bước).', '**Quên các cầu không bao giờ sập** ở trạng thái khởi đầu.', '**Áp dụng cho bài trực tuyến:** nếu câu hỏi phụ thuộc vào đáp số trước (dữ liệu được "mã hóa"), kĩ thuật này không dùng được.'],
      approaches: [['PHACAU_1demlai', 'Dựng lại DSU sau mỗi lần sập'], ['PHACAU', 'Đi ngược thời gian với DSU']],
    },
    // ================================================================ 9.3
    {
      id: '9.3', key: 'DSU có chẵn lẻ (hoặc DSU trên 2n đỉnh).',
      understand: [
        'Mỗi mẩu tin cho biết **quan hệ** giữa hai người: cùng phe (0) hay khác phe (1). Quan hệ có thể suy ra theo kiểu "cộng mô-đun 2": a khác b, b khác c thì a cùng c. Thông tin đầu tiên mâu thuẫn là thông tin mà quan hệ nó nói trái với quan hệ đã suy ra được từ các thông tin trước.',
        { fig: 'tap2:haiphe', w: 4.6, cap: 'Ví dụ 1: mẩu tin thứ 5 mâu thuẫn.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Tô màu lại sau mỗi mẩu tin',
        body: [
          'Coi mỗi mẩu tin là một cạnh có nhãn. Các thông tin phù hợp khi và chỉ khi tô được hai màu sao cho cạnh nhãn 0 nối hai đỉnh cùng màu, cạnh nhãn 1 nối hai đỉnh khác màu. Sau mỗi mẩu tin, tô màu lại toàn bộ.',
          { fig: 'f_haiphe_naive', w: 2.8, cap: 'Sơ đồ khối của cách tô màu lại.' },
          { file: 'HAIPHE_1bfslai', title: 'Cách ngây thơ: tô màu lại sau mỗi mẩu tin' },
          { cx: 'O(m · (n + m)).' },
        ],
      },
      stuck: [
        'Chỉ chạy kịp Subtask 2 (n, m ≤ 2000): **{{S:HAIPHE_1bfslai}} điểm**.',
        'Một "cải tiến" sai: dùng DSU thường, gộp những người **cùng phe**, và báo mâu thuẫn khi hai người "khác phe" đã cùng nhóm. Cách này bỏ qua hoàn toàn chuỗi suy luận "khác của khác là cùng": ở ví dụ 2 (1 khác 2, 2 khác 3, 1 khác 3) nó không phát hiện được gì: **{{S:HAIPHE_2dsuthuong}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['DSU thường chỉ nhớ "cùng nhóm hay không". Ta cần nhớ thêm: trong cùng nhóm, hai người **cùng phe hay khác phe**.'] },
      ],
      breakthrough: [
        '**DSU có chẵn lẻ:** ngoài p[x], lưu w[x] ∈ {0, 1} là quan hệ giữa x và cha p[x]. Quan hệ giữa x và gốc là XOR các w trên đường đi; gọi là par(x). Hai người cùng gốc thì quan hệ giữa họ là par(a) XOR par(b).',
        { ul: ['Mẩu tin (a, b, t), a và b cùng gốc: mâu thuẫn khi par(a) XOR par(b) ≠ t.', 'Khác gốc ra, rb: treo ra vào rb với w[ra] = par(a) XOR par(b) XOR t (để quan hệ giữa a và b đúng bằng t).', 'Nén đường đi: khi cho x trỏ thẳng lên gốc thì w[x] mới chính là par(x).'] },
        'Chạy tay ví dụ 1:',
        { table: { cols: [1500, 3800, 3318], head: ['Mẩu tin', 'Kiểm tra', 'Thao tác'], rows: [
          ['(1, 2, khác)', 'gốc 1, gốc 2: khác gốc', 'p[1] = 2, w[1] = 1'], ['(2, 3, khác)', 'gốc 2, gốc 3', 'p[2] = 3, w[2] = 1'], ['(1, 3, cùng)', 'par(1) = 1 XOR 1 = 0, par(3) = 0; 0 XOR 0 = 0 = t', 'phù hợp'],
          ['(3, 4, khác)', 'gốc 3, gốc 4', 'p[3] = 4, w[3] = 1'], ['(4, 1, cùng)', 'par(4) = 0, par(1) = 0 XOR 1 = 1; 0 XOR 1 = 1 ≠ 0', '**mâu thuẫn: in 5**']] } },
        { box: 'def', title: 'CÁCH KHÁC: DSU TRÊN 2n ĐỈNH', body: ['Tạo hai đỉnh cho mỗi người: "a ở phe A" và "a ở phe B". Tin "a khác b" gộp (a~A~, b~B~) và (a~B~, b~A~); tin "a cùng b" gộp (a~A~, b~A~) và (a~B~, b~B~). Có mâu thuẫn khi a~A~ và a~B~ rơi vào cùng một nhóm, tức là khi tin "khác" mà a~A~, b~A~ đã cùng nhóm, hoặc tin "cùng" mà a~A~, b~B~ đã cùng nhóm. Dễ cài hơn, cũng được **{{S:HAIPHE_3dsu2n}} điểm**.'] },
      ],
      optimal: [
        { file: 'HAIPHE', title: 'HAIPHE.CPP: DSU có chẵn lẻ, nén đường đi không đệ quy' },
        { cx: 'O(m · log n) trong trường hợp xấu nhất (chỉ nén đường đi), thực tế gần như tuyến tính.' },
      ],
      traps: ['**Chỉ gộp các cặp "cùng phe"** (bỏ qua suy luận qua quan hệ "khác phe").', '**Cập nhật w sai khi nén đường đi:** w[x] mới phải là quan hệ giữa x và **gốc**, không phải giữa x và cha cũ.', '**DSU đệ quy** không gộp theo kích thước: chuỗi dài 2·10^5^ có thể làm tràn ngăn xếp.'],
      approaches: [['HAIPHE_1bfslai', 'Tô màu lại sau mỗi mẩu tin'], ['HAIPHE_2dsuthuong', 'DSU thường, chỉ gộp "cùng phe"'], ['HAIPHE_3dsu2n', 'DSU trên 2n đỉnh'], ['HAIPHE', 'DSU có chẵn lẻ']],
    },
    // ================================================================ 10.1
    {
      id: '10.1', key: 'Gộp cáp có sẵn vào DSU rồi chạy Kruskal.',
      understand: [
        'Cần một tập cáp lắp thêm rẻ nhất để toàn mạng liên thông, biết rằng một số cáp đã có sẵn (miễn phí). Đây là cây khung nhỏ nhất (Tập 1, Bài 10) với một số cạnh "bắt buộc" có giá 0.',
        { fig: 'tap2:noimang', w: 4.6, cap: 'Ví dụ: cáp xanh có sẵn, cáp đỏ được lắp thêm.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Prim O(n²)',
        body: [
          'Coi cáp có sẵn là cạnh giá 0 và chạy Prim cài đặt đơn giản: mỗi lượt duyệt cả n đỉnh để tìm đỉnh gần cây nhất.',
          { fig: 'f_noimang_naive', w: 3.0, cap: 'Sơ đồ khối của Prim O(n²).' },
          { file: 'NOIMANG_1prim', title: 'Cách ngây thơ: Prim O(n²)' },
          { cx: 'O(n^2^ + m): n = 1000 là 10^6^; n = 10^5^ là 10^10^.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n ≤ 1000): **{{P:NOIMANG_1prim:1}} điểm**.', '**Subtask 2, 3**: quá thời gian.'] },
        'Kruskal (sắp xếp cạnh + DSU) chạy O(m log m), nhưng nhiều bạn **quên cáp có sẵn**: đọc vào rồi bỏ qua. Đúng ở Subtask 1, 2 (k = 0), sai ở Subtask 3: **{{S:NOIMANG_2quencosan}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Kruskal xử lí cạnh theo chi phí tăng dần. Cáp có sẵn có chi phí 0, nhỏ hơn mọi phương án: chúng phải được "nhận" **trước tiên**.'] },
      ],
      breakthrough: [
        'Khởi tạo DSU, gộp hai đầu của mọi cáp có sẵn (không tính tiền). Sau đó chạy Kruskal bình thường trên m phương án. Cuối cùng kiểm tra số nhóm bằng 1; nếu không thì in −1.',
        { table: { cols: [2400, 1700, 4518], head: ['Xét cáp (ví dụ)', 'Giá', 'Kết quả'], rows: [['1 – 2 (có sẵn)', '0', 'gộp: {1, 2}'], ['4 – 5', '1', 'nhận: {4, 5}'], ['2 – 3', '2', 'nhận: {1, 2, 3}'], ['2 – 4', '3', 'nhận: {1, 2, 3, 4, 5}'], ['1 – 3, 3 – 4, 3 – 5', '4, 5, 6', 'bỏ: hai đầu đã cùng nhóm'], ['Tổng', '', '**6**']] } },
      ],
      optimal: [
        { file: 'NOIMANG', title: 'NOIMANG.CPP: DSU với cáp có sẵn + Kruskal' },
        { cx: 'O(k + m log m).' },
      ],
      traps: ['**Quên cáp có sẵn.**', '**Tổng chi phí bằng `int`:** tới (n − 1) · 10^9^ ≈ 10^14^.', '**Không kiểm tra liên thông** ở cuối.'],
      approaches: [['NOIMANG_1prim', 'Prim O(n²)'], ['NOIMANG_2quencosan', 'Kruskal, quên cáp có sẵn'], ['NOIMANG', 'Gộp cáp có sẵn + Kruskal']],
    },
    // ================================================================ 10.2
    {
      id: '10.2', key: 'Cây khung nhỏ nhất + cạnh lớn nhất trên đường đi (nhảy nhị phân).',
      understand: [
        'Độ khó của lộ trình là cạnh **lớn nhất** trên đó; cần lộ trình có độ khó **nhỏ nhất**: bài toán minimax path. Tính chất quan trọng của cây khung nhỏ nhất (Tập 1, Bài 10): đường đi giữa s và t trên cây khung nhỏ nhất luôn là một lộ trình minimax.',
        { fig: 'tap2:itdoc', w: 4.8, cap: 'Mọi lộ trình tốt nhất nằm trên cây khung nhỏ nhất.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Thêm dần cạnh cho từng câu hỏi',
        body: [
          'Sắp xếp cạnh theo độ dốc. Với mỗi câu hỏi (s, t), dùng DSU mới và thêm dần các cạnh; cạnh làm s, t lần đầu cùng nhóm cho đáp số.',
          { fig: 'f_itdoc_naive', w: 2.8, cap: 'Sơ đồ khối của cách thêm dần cạnh cho từng câu hỏi.' },
          { file: 'ITDOC_1moicauhoi', title: 'Cách ngây thơ: Kruskal lại cho mỗi câu hỏi' },
          { cx: 'O(q · m · α(n)).' },
        ],
      },
      stuck: [
        'Subtask 1 chạy tức thì; Subtask 2 (q = 1000, m = 2·10^5^) là 2·10^8^ thao tác DSU. Kết quả thực tế: **{{S:ITDOC_1moicauhoi}} điểm**.',
        'Dựng cây khung một lần rồi **DFS trên cây** cho mỗi câu hỏi, giữ cạnh lớn nhất trên đường đi: O(q · n). Nghe có vẻ vừa sức với Subtask 2, nhưng q = 1000 lần duyệt cây 10^5^ đỉnh là 10^8^ bước nhảy lung tung trong bộ nhớ (danh sách kề, ngăn xếp), cộng thêm việc xóa mảng mỗi lần: thực tế mất vài giây, chỉ được **{{S:ITDOC_2dfscay}} điểm**. Với q = 10^5^ thì 10^10^ bước.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Câu hỏi đã trở thành "cạnh lớn nhất trên đường đi giữa hai đỉnh của một cây". Cần trả lời nhanh hơn O(n) mỗi câu.'] },
      ],
      breakthrough: [
        'Dùng **nhảy nhị phân** như bài toán LCA (Tập 1, Bài 11), lưu thêm mx[v][j] = cạnh lớn nhất trên đoạn đường từ v nhảy lên 2^j^ bước:',
        { ul: ['mx[v][0] = độ dốc cạnh (v, cha v);', 'mx[v][j] = max(mx[v][j − 1], mx[up[v][j − 1]][j − 1]).'] },
        'Đường đi u – v trên cây là u → LCA → v. Khi nâng u (hoặc v) lên 2^j^ bước, gộp mx tương ứng vào đáp số. Đồ thị có thể không liên thông: ta có một **rừng**, mỗi cây treo tại một gốc; hai đỉnh khác cây thì in −1.',
        { box: 'theorem', title: 'VÌ SAO ĐƯỜNG TRÊN CÂY KHUNG NHỎ NHẤT LÀ TỐT NHẤT?', body: ['Giả sử cạnh lớn nhất e trên đường cây giữa s và t có độ dốc h, và có lộ trình P giữa s, t với mọi cạnh < h. Xóa e khỏi cây chia cây thành hai phần, s và t ở hai phía; P phải có một cạnh f nối hai phía, với độ dốc < h. Thay e bằng f được cây khung nhỏ hơn: mâu thuẫn.'] },
      ],
      optimal: [
        { file: 'ITDOC', title: 'ITDOC.CPP: Kruskal + nhảy nhị phân với cạnh lớn nhất' },
        { cx: 'O(m log m + n log n + q log n).' },
        { box: 'def', title: 'CÁCH KHÁC: TRẢ LỜI NGOẠI TUYẾN', body: ['Đọc hết câu hỏi, rồi chạy Kruskal một lần; mỗi khi gộp hai nhóm, trả lời mọi câu hỏi (s, t) vừa trở nên cùng nhóm (gộp danh sách câu hỏi nhỏ vào lớn). Hoặc dựng "cây Kruskal" (Kruskal reconstruction tree) rồi tìm LCA.'] },
      ],
      traps: ['**Quên đồ thị không liên thông:** phải in −1.', '**s = t:** đáp số là 0.', '**Bảng nhảy cho đỉnh gốc:** up[gốc][j] = gốc, mx[gốc][j] = 0.'],
      approaches: [['ITDOC_1moicauhoi', 'Kruskal lại cho mỗi câu hỏi'], ['ITDOC_2dfscay', 'Cây khung + DFS mỗi câu hỏi'], ['ITDOC', 'Cây khung + nhảy nhị phân']],
    },
    // ================================================================ 10.3
    {
      id: '10.3', key: 'Đỉnh ảo "nguồn nước" + Kruskal.',
      understand: [
        'Mỗi nhà phải có nước bằng một trong hai cách: tự đào giếng, hoặc nối ống tới một nhà có nước. Cái khó là không biết trước nên đào giếng ở đâu và bao nhiêu giếng.',
        { fig: 'tap2:giengong', w: 5.4, cap: 'Đỉnh ảo 0 biến "đào giếng" thành "nối ống tới nguồn nước".' },
      ],
      naive: {
        title: 'Cách ngây thơ: Thử mọi tập giếng và mọi tập ống',
        body: [
          { fig: 'f_giengong_naive', w: 3.2, cap: 'Sơ đồ khối của cách vét cạn.' },
          { file: 'GIENGONG_1vetcan', title: 'Cách ngây thơ: thử 2ⁿ⁺ᵐ lựa chọn' },
          { cx: 'O(2^n+m^ · (n + m)): chỉ dùng được cho n + m ≤ 20: **{{S:GIENGONG_1vetcan}} điểm**.' },
        ],
      },
      stuck: [
        'Một ý tưởng "tham lam" hay gặp: đào **một** giếng ở nhà rẻ nhất, rồi nối ống bằng Kruskal (nhóm nào chưa có nước thì đào thêm giếng rẻ nhất trong nhóm). Sai vì có lúc đào thêm giếng rẻ hơn nối một đường ống đắt: **{{S:GIENGONG_2motgieng}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Có hai loại "chi phí" khác nhau (giếng và ống), và số giếng không cố định. Cần đưa cả hai về cùng một loại đối tượng.'] },
      ],
      breakthrough: [
        'Thêm **đỉnh ảo 0** là "nguồn nước". Đào giếng ở nhà i tương đương nối ống từ i tới nguồn với giá a~i~. Một nhà có nước ⟺ nó liên thông với đỉnh 0. Mọi nhà có nước ⟺ đồ thị n + 1 đỉnh liên thông. Đáp số là **cây khung nhỏ nhất** của đồ thị mới.',
        { table: { cols: [2400, 1300, 4918], head: ['Cạnh (theo giá tăng)', 'Giá', 'Kruskal'], rows: [['1 – 2', '2', 'nhận'], ['2 – 3', '2', 'nhận'], ['0 – 4 (giếng nhà 4)', '3', 'nhận'], ['3 – 4', '3', 'nhận: mọi đỉnh đã liên thông'], ['0 – 2, 0 – 3, 0 – 1, 1 – 4', '4, 4, 5, 7', 'bỏ'], ['Tổng', '', '**10**']] } },
        'Prim O(n^2^) trên đồ thị mới cũng đúng, đủ nhanh cho Subtask 2: **{{S:GIENGONG_3prim}} điểm**.',
      ],
      optimal: [
        { file: 'GIENGONG', title: 'GIENGONG.CPP: đỉnh ảo + Kruskal' },
        { cx: 'O((n + m) log(n + m)).' },
      ],
      traps: ['**Đào đúng một giếng.**', '**Tổng chi phí bằng `int`.**', '**Quên rằng đỉnh 0 cũng là một đỉnh của DSU** (mảng phải có n + 1 phần tử).'],
      approaches: [['GIENGONG_1vetcan', 'Thử mọi tập giếng và ống'], ['GIENGONG_2motgieng', 'Một giếng rẻ nhất + Kruskal'], ['GIENGONG_3prim', 'Đỉnh ảo + Prim O(n²)'], ['GIENGONG', 'Đỉnh ảo + Kruskal']],
    },
    // ================================================================ 11.1
    {
      id: '11.1', key: 'LCA nhảy nhị phân, dựng bảng bằng BFS.',
      understand: [
        'Gia phả là một **cây có gốc** (ông tổ). Ông tổ chung gần nhất là **LCA**, số đời chênh lệch là |depth(u) − depth(v)|. Chi tiết: ông tổ không nhất thiết là người số 1, và cây có thể rất sâu.',
        { fig: 'tap2:hohang', w: 4.8, cap: 'Gia phả của ví dụ.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Leo từng bậc',
        body: [
          { fig: 'f_hohang_naive', w: 2.8, cap: 'Sơ đồ khối của cách leo từng bậc.' },
          { file: 'HOHANG_1leo', title: 'Cách ngây thơ: leo từng bậc tới tổ tiên chung' },
          { cx: 'O(n) mỗi câu hỏi; O(n · q) tổng cộng.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n, q ≤ 1000): **{{P:HOHANG_1leo:1}} điểm**.', '**Subtask 2**: gia phả dạng "đường thẳng" 2·10^5^ đời và 2·10^5^ câu hỏi: 4·10^10^ bước.'] },
        'Cài nhảy nhị phân nhưng tính độ sâu bằng **DFS đệ quy**: cây đường thẳng 2·10^5^ tầng, mỗi tầng giữ cả một vòng lặp `for` và vài biến: tràn ngăn xếp 8 MB, **{{S:HOHANG_2dequy}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Leo từng bậc tốn O(độ sâu). Cần leo nhanh hơn, và cần dựng bảng mà không đệ quy.'] },
      ],
      breakthrough: [
        'Bảng **up[v][j]** = tổ tiên thứ 2^j^ của v, với up[v][j] = up[up[v][j − 1]][j − 1]. Dựng bảng theo thứ tự **BFS** từ ông tổ: khi xử lí v, cha của v đã có bảng đầy đủ.',
        { ol: ['Nâng đỉnh sâu hơn lên cùng độ sâu: phân tích hiệu độ sâu theo bit, nhảy 2^j^ khi bit j bằng 1.', 'Nếu hai đỉnh đã trùng: đó là LCA. Ngược lại, với j giảm dần, nếu up[u][j] ≠ up[v][j] thì nhảy cả hai. Cuối cùng LCA là cha của u.'] },
        { table: { cols: [2000, 3600, 3018], head: ['Câu hỏi', 'Diễn biến', 'Kết quả'], rows: [['(7, 4)', 'depth 3 và 2: nâng 7 lên 1 bậc → 5; 5 ≠ 4, nhảy cả hai 1 bậc → 2, 2', '**2**, chênh 1'], ['(7, 6)', 'nâng 7 → 5; 5, 6 nhảy tới 2, 3; cha chung **1**', '**1**, chênh 1'], ['(5, 7)', 'nâng 7 → 5: trùng', '**5**, chênh 1']] } },
      ],
      optimal: [
        { file: 'HOHANG', title: 'HOHANG.CPP: LCA nhảy nhị phân, dựng bảng bằng BFS' },
        { cx: 'O(n log n) dựng bảng, O(log n) mỗi câu hỏi.' },
      ],
      traps: ['**Giả sử ông tổ là người 1.**', '**DFS đệ quy** trên cây sâu.', '**LG quá nhỏ:** 2^LG^ phải lớn hơn độ sâu lớn nhất (2^18^ > 2·10^5^).'],
      approaches: [['HOHANG_1leo', 'Leo từng bậc'], ['HOHANG_2dequy', 'Nhảy nhị phân, DFS đệ quy'], ['HOHANG', 'Nhảy nhị phân, BFS']],
    },
    // ================================================================ 11.2
    {
      id: '11.2', key: 'Nhảy nhị phân kèm min trên đoạn.',
      understand: [
        'Trên cây, giữa hai trạm có đúng một đường truyền: u → LCA(u, v) → v. Cần cạnh nhỏ nhất trên đường đó, cho 10^5^ câu hỏi.',
        { fig: 'tap2:capquang', w: 4.6, cap: 'Đường truyền 4 – 6 đi qua tổ tiên chung 1.' },
      ],
      naive: {
        title: 'Cách ngây thơ: DFS cho mỗi câu hỏi',
        body: [
          { fig: 'f_capquang_naive', w: 2.8, cap: 'Sơ đồ khối của cách DFS cho từng câu hỏi.' },
          { file: 'CAPQUANG_1dfs', title: 'Cách ngây thơ: DFS từ u, giữ cạnh nhỏ nhất' },
          { cx: 'O(n · q).' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n, q ≤ 1000): **{{P:CAPQUANG_1dfs:1}} điểm**.', '**Subtask 2** (cây là đường thẳng 10^5^ trạm) và **Subtask 3**: 10^10^ bước.'] },
        'Subtask 2 gợi ý một bước trung gian: trên đường thẳng, câu hỏi là "giá trị nhỏ nhất trên đoạn [u, v − 1] của dãy băng thông", giải được bằng **bảng thưa** (sparse table): mn[i][j] = min của 2^j^ phần tử bắt đầu từ i. Ý tưởng "đoạn dài 2^j^" ấy chuyển nguyên vẹn lên cây.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Đường đi trên cây không phải một đoạn liên tiếp của một dãy, nhưng nó gồm hai đoạn "thẳng đứng" (từ u lên LCA và từ v lên LCA).'] },
      ],
      breakthrough: [
        'Kết hợp bảng nhảy với min: mn[v][j] = cạnh nhỏ nhất trên đoạn từ v nhảy lên 2^j^ bước; mn[v][0] là cạnh (v, cha v), mn[v][j] = min(mn[v][j − 1], mn[up[v][j − 1]][j − 1]). Khi tìm LCA, mỗi lần nhảy u hoặc v lên 2^j^ bước thì lấy min với mn tương ứng; cuối cùng cộng thêm hai cạnh đi vào LCA.',
        { table: { cols: [1500, 4400, 2718], head: ['Câu hỏi', 'Các bước nhảy (treo tại 1)', 'Kết quả'], rows: [['(4, 5)', 'cùng độ sâu 2; up[4][0] = up[5][0] = 2: lấy mn[4][0] = 7, mn[5][0] = 3', '**3**'], ['(4, 6)', 'cùng độ sâu; nhảy 1 bậc: 4 → 2 (7), 6 → 3 (9); hai cạnh cuối 10, 4', '**4**'], ['(2, 4)', 'nâng 4 lên 1 bậc (7): trùng 2', '**7**']] } },
      ],
      optimal: [
        { file: 'CAPQUANG', title: 'CAPQUANG.CPP: nhảy nhị phân kèm min' },
        { cx: 'O(n log n + q log n).' },
      ],
      traps: ['**Quên hai cạnh cuối** đi vào LCA khi u ≠ v sau bước nhảy.', '**Khởi tạo mn của gốc bằng 0** (thay vì vô cùng) làm mọi đáp số bằng 0.', '**Duyệt cây đệ quy** trên cây đường thẳng 10^5^ đỉnh.'],
      approaches: [['CAPQUANG_1dfs', 'DFS cho mỗi câu hỏi'], ['CAPQUANG', 'Nhảy nhị phân kèm min']],
    },
    // ================================================================ 11.3
    {
      id: '11.3', key: 'Trả lời ngoại tuyến: DFS với ngăn xếp đường đi.',
      understand: [
        'Cấp trên thứ k chính là **tổ tiên thứ k**. Với 2·10^5^ đỉnh, nhảy nhị phân là đủ. Nhưng với n = q = 10^6^ và chỉ **64 MB** bộ nhớ, bảng up[v][j] với 21 cột đã cần 84 MB.',
        { fig: 'tap2:capk', w: 4.6, cap: 'Cây quản lí của ví dụ.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Leo từng bậc',
        body: [
          { file: 'CAPK_1leo', title: 'Cách ngây thơ: leo k bậc' },
          { cx: 'O(min(k, độ sâu)) mỗi câu hỏi; O(n · q) trong trường hợp xấu nhất.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n, q ≤ 1000): **{{P:CAPK_1leo:1}} điểm**.', '**Subtask 2, 3**: cây sâu, quá thời gian.'] },
        'Nhảy nhị phân theo các bit của k giải trọn Subtask 2, nhưng ở Subtask 3 bảng 21 · 10^6^ số nguyên vượt giới hạn 64 MB: **{{S:CAPK_2nhaynhiphan}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Bảng nhảy nhị phân lưu sẵn câu trả lời cho **mọi** đỉnh và mọi lũy thừa của 2, trong khi ta chỉ cần trả lời q câu hỏi cụ thể. Có cách nào chỉ dùng O(n + q) bộ nhớ?'] },
      ],
      breakthrough: [
        'Đọc **toàn bộ** câu hỏi trước và gom theo đỉnh v. DFS (không đệ quy) từ gốc, duy trì mảng **path** là dãy các đỉnh từ gốc tới đỉnh đang đứng. Khi vừa đi xuống v, path chứa đúng các tổ tiên của v theo thứ tự, nên cấp trên thứ k của v là path[|path| − 1 − k] (nếu k < |path|), ngược lại là −1.',
        { table: { cols: [2200, 2400, 4018], head: ['Đang ở', 'path', 'Trả lời'], rows: [['1', '[1]', ''], ['2', '[1, 2]', ''], ['4', '[1, 2, 4]', '(4, 1): path[1] = **2**'], ['5', '[1, 2, 5]', ''], ['7', '[1, 2, 5, 7]', '(7, 2): path[1] = **2**'], ['8', '[1, 2, 5, 8]', '(8, 0): **8**'], ['6', '[1, 3, 6]', '(6, 3): 3 ≥ |path| = 3: **−1**']] } },
        { fig: 'f_capk_opt', w: 3.4, cap: 'Sơ đồ khối của DFS với ngăn xếp đường đi.' },
        'Để tiết kiệm bộ nhớ, danh sách con và danh sách câu hỏi được lưu dạng "đầu – kế tiếp" (mỗi phần tử chỉ tốn một số nguyên), thay cho `vector<vector<int>>`.',
      ],
      optimal: [
        { file: 'CAPK', title: 'CAPK.CPP: trả lời ngoại tuyến bằng DFS và ngăn xếp đường đi' },
        { cx: 'O(n + q) thời gian và bộ nhớ (khoảng 8 mảng 10^6^ số nguyên = 32 MB).' },
      ],
      traps: ['**Bảng nhảy nhị phân với n = 10^6^:** vượt 64 MB.', '**DFS đệ quy** sâu 10^6^ tầng.', '**k lớn hơn độ sâu** (tới 10^9^): phải in −1, không truy cập ngoài mảng.', '**`vector<vector<int>>` cho 10^6^ đỉnh:** mỗi vector rỗng đã tốn 24 byte, cộng phần dư khi cấp phát.'],
      approaches: [['CAPK_1leo', 'Leo từng bậc'], ['CAPK_2nhaynhiphan', 'Nhảy nhị phân (bảng 21 · n)'], ['CAPK', 'Ngoại tuyến: DFS + ngăn xếp đường đi']],
    },
  ],
};
