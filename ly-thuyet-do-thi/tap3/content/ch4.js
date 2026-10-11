// TẬP 3 — CHƯƠNG 4. CẤU TRÚC CỦA ĐỒ THỊ
module.exports = {
  no: 4,
  intro: 'Chương 4 nhìn vào "bộ xương" của đồ thị: thứ tự tô pô, cầu và khớp, thành phần liên thông mạnh, chu trình Euler. Cách ngây thơ quen thuộc nhất là "thử xóa từng cạnh, từng đỉnh rồi duyệt lại". Lời giải đúng chỉ cần **một** lần DFS (hoặc một lần Kahn) và đọc thêm thông tin từ chính quá trình duyệt đó. Những lời giải "trông như đúng" hay mất điểm vì dừng quá sớm, vì bỏ qua cạnh song song, vì quên gốc của cây DFS, hoặc vì chọn sai chiều khi dựng đáp án.',
  solutions: [
    // ================================================================ 12.1
    {
      id: '12.1', key: 'Kahn: thiếu đỉnh thì có vòng; hàng đợi từng có ≥ 2 đỉnh thì nhiều đáp án.',
      understand: [
        'Mỗi kết quả "a b" là một cung a → b. Một bảng xếp hạng thỏa mãn chính là một **thứ tự tô pô** (Tập 1, Bài 12). Có ba khả năng: không có thứ tự nào (đồ thị có chu trình), có đúng một, hoặc có nhiều.',
        { fig: 'tap2:xhgiaidau', w: 5.6, cap: 'Ba ví dụ: duy nhất, nhiều bảng, mâu thuẫn.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Thử mọi bảng xếp hạng',
        body: [
          'Với n ≤ 8 có 8! = 40 320 hoán vị. Thử từng hoán vị, kiểm tra cả m kết quả; đếm số hoán vị hợp lệ (đếm tới 2 là đủ).',
          { fig: 'f_xhgiaidau_naive', w: 3.0, cap: 'Sơ đồ khối của cách thử mọi hoán vị.' },
          { file: 'XHGIAIDAU_1hoanvi', title: 'Cách ngây thơ: duyệt mọi hoán vị' },
          { cx: 'O(n! · m): chỉ dùng được khi n rất nhỏ.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n ≤ 8): **{{P:XHGIAIDAU_1hoanvi:1}} điểm**.', '**Subtask 2**: 10^5^! hoán vị, không thể.'] },
        'Chuyển sang Kahn là đúng hướng. Nhưng một lỗi rất hay gặp là **dừng sớm**: thấy hàng đợi có hai đội là in 0 ngay. Nếu phía sau còn một vòng mâu thuẫn thì đáp số phải là −1 (mâu thuẫn được ưu tiên). Ví dụ n = 4 với hai kết quả "3 4" và "4 3": hàng đợi ban đầu là {1, 2}, chương trình in 0, nhưng đáp án là −1. Cách này chỉ được **{{S:XHGIAIDAU_2dungsom}} điểm**: test nào có cả hai hiện tượng đều sai.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Chạy Kahn thì ra một thứ tự, nhưng làm sao biết thứ tự đó **duy nhất**, và làm sao kiểm tra mâu thuẫn **trước khi** kết luận "nhiều đáp án"?'] },
      ],
      breakthrough: [
        'Chạy Kahn **đến hết** và ghi lại hai thông tin:',
        { ul: ['**Có vòng?** Số đội lấy ra được ít hơn n thì các đội còn lại đều nằm trên (hoặc phía sau) một vòng: in −1.', '**Duy nhất?** Nếu có lúc hàng đợi chứa từ hai đội trở lên, hai đội đó có thể đổi thứ tự cho nhau (không ai "trên" ai), nên có nhiều đáp án. Ngược lại, mỗi bước chỉ có một lựa chọn, nên thứ tự là duy nhất.'] },
        'Chạy tay ví dụ 1 (cung 1 → 3, 3 → 2, 2 → 4, 1 → 2):',
        { table: { cols: [1400, 2400, 2400, 2418], head: ['Bước', 'Hàng đợi', 'Lấy ra', 'Bán bậc vào còn lại'], rows: [
          ['khởi đầu', '{1}', '', '2: 2, 3: 1, 4: 1'], ['1', '{1}', '1', '2: 1, 3: **0** → vào hàng đợi'], ['2', '{3}', '3', '2: **0** → vào hàng đợi'], ['3', '{2}', '2', '4: **0** → vào hàng đợi'], ['4', '{4}', '4', 'lấy đủ 4 đội']] } },
        'Hàng đợi luôn chỉ có một đội, lấy ra đủ 4 đội: bảng duy nhất **1 3 2 4**. Ở ví dụ 2, ngay từ đầu hàng đợi là {1, 3}: in 0. Ở ví dụ 3, không đội nào có bán bậc vào 0: lấy ra 0 < 3 đội, in −1.',
        { fig: 'f_xhgiaidau_opt', w: 3.4, cap: 'Sơ đồ khối của Kahn có kiểm tra tính duy nhất.' },
        { box: 'theorem', title: 'VÌ SAO "HÀNG ĐỢI LUÔN MỘT ĐỘI" LÀ ĐỦ?', body: ['Nếu mỗi bước chỉ có đúng một đội u sẵn sàng, thì đội lấy ra liền sau u phải có cung từ u (nếu không, nó đã sẵn sàng cùng lúc với u). Vậy thứ tự tìm được là một đường đi qua cả n đội, và mọi thứ tự tô pô đều phải tôn trọng đường đi đó: chỉ có một thứ tự.'] },
      ],
      optimal: [
        { file: 'XHGIAIDAU', title: 'XHGIAIDAU.CPP: Kahn, kiểm tra vòng và tính duy nhất' },
        { cx: 'O(n + m).' },
      ],
      traps: ['**Dừng sớm khi hàng đợi có hai đội** mà chưa kiểm tra vòng.', '**Kiểm tra tính duy nhất chỉ ở bước đầu** (chỉ đếm số đội có bán bậc vào 0 lúc đầu).', '**Dùng hàng đợi ưu tiên** rồi so sánh với một thứ tự khác: tốn công mà không cần thiết.'],
      approaches: [['XHGIAIDAU_1hoanvi', 'Duyệt mọi hoán vị'], ['XHGIAIDAU_2dungsom', 'Kahn, dừng ngay khi hàng đợi có hai đội'], ['XHGIAIDAU', 'Kahn chạy đến hết']],
    },
    // ================================================================ 12.2
    {
      id: '12.2', key: 'Hai lượt QHĐ trên thứ tự tô pô: sớm nhất (xuôi) và muộn nhất (ngược).',
      understand: [
        'Mỗi công việc là một đỉnh có trọng số t~i~; cung p → i nghĩa là p phải xong trước i. Thời điểm hoàn thành dự án là độ dài **đường đi dài nhất** (tính tổng trọng số đỉnh) trên DAG. Việc **then chốt** là việc nằm trên **một** đường đi dài nhất nào đó: kéo dài nó thêm 1 thì đường đi ấy dài thêm 1.',
        { fig: 'tap2:xaynha', w: 5.6, cap: 'Ví dụ: dự án xong lúc 8; có hai đường dài nhất.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Thử kéo dài từng việc',
        body: [
          'Làm đúng như định nghĩa: tính T; với mỗi việc i, tăng t~i~ thêm 1, tính lại T\' và so sánh.',
          { fig: 'f_xaynha_naive', w: 3.0, cap: 'Sơ đồ khối của cách thử từng việc.' },
          { file: 'XAYNHA_1thuthem', title: 'Cách ngây thơ: thử kéo dài từng việc' },
          { cx: 'O(n · (n + m)): n = 1000 khoảng 3·10^6^; n = 10^5^ khoảng 3·10^10^.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n ≤ 1000): **{{P:XAYNHA_1thuthem:1}} điểm**.', '**Subtask 2**: quá thời gian.'] },
        'Một lời giải nhanh nhưng sai: tìm **một** đường dài nhất (lần ngược từ việc kết thúc muộn nhất) rồi in các việc trên đường đó. Ở ví dụ, đường 1 → 3 → 5 và đường 1 → 2 → 4 → 5 đều dài 8; lần ngược chỉ được một trong hai. Kết quả: **{{S:XAYNHA_2motduong}} điểm**, vì khi thời gian các việc nhỏ, có rất nhiều đường dài nhất.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Cần biết **mỗi** việc có nằm trên **một** đường dài nhất nào đó hay không, mà không thử từng việc và không liệt kê các đường.'] },
      ],
      breakthrough: [
        'Một đường đi qua việc v gồm hai nửa: nửa **trước** v và nửa **sau** v. Tính riêng hai nửa bằng hai lượt QHĐ theo thứ tự tô pô:',
        { ul: ['**Lượt xuôi:** es[v] = thời điểm bắt đầu sớm nhất = max(es[p] + t~p~) trên các việc p làm trước v. T = max(es[v] + t~v~).', '**Lượt ngược** (thứ tự tô pô đảo lại): lf[v] = thời điểm kết thúc muộn nhất mà dự án vẫn xong lúc T = min(lf[w] − t~w~) trên các việc w làm sau v (lf[v] = T nếu không có việc nào sau v).', 'Việc v **then chốt** khi và chỉ khi nó **không có thời gian dự trữ**: es[v] + t~v~ = lf[v].'] },
        'Chạy tay ví dụ (t = 3, 2, 4, 2, 1, 2):',
        { table: { cols: [1100, 1500, 1500, 1500, 1500, 1518], head: ['Việc', 't', 'es', 'es + t', 'lf', 'Then chốt?'], rows: [
          ['1', '3', '0', '3', '3', '**có**'], ['2', '2', '3', '5', 'min(7 − 2, 8 − 2) = 5', '**có**'], ['3', '4', '3', '7', '8 − 1 = 7', '**có**'], ['4', '2', '5', '7', '8 − 1 = 7', '**có**'], ['5', '1', 'max(7, 7) = 7', '**8**', '8', '**có**'], ['6', '2', '5', '7', '8', 'không (dư 1 ngày)']] } },
        { fig: 'f_xaynha_opt', w: 3.0, cap: 'Sơ đồ khối của hai lượt QHĐ.' },
      ],
      optimal: [
        { file: 'XAYNHA', title: 'XAYNHA.CPP: hai lượt QHĐ trên thứ tự tô pô' },
        { cx: 'O(n + Σk~i~).' },
      ],
      traps: ['**Chỉ lần một đường dài nhất.**', '**Dùng int:** T có thể tới 10^5^ · 10^9^ = 10^14^.', '**Duyệt theo số hiệu công việc** thay vì thứ tự tô pô: công việc i có thể phụ thuộc vào công việc có số hiệu lớn hơn.', '**Lượt ngược bắt đầu từ lf = ∞** thay vì lf = T với các việc cuối cùng.'],
      approaches: [['XAYNHA_1thuthem', 'Thử kéo dài từng việc'], ['XAYNHA_2motduong', 'Chỉ lần một đường dài nhất'], ['XAYNHA', 'Hai lượt QHĐ (sớm nhất / muộn nhất)']],
    },
    // ================================================================ 12.3
    {
      id: '12.3', key: 'Chỉ giữ các nút vừa tới được từ 1 vừa tới được n; có vòng trong đó thì vô số.',
      understand: [
        'Nếu đồ thị không có chu trình, số lộ trình được đếm bằng QHĐ trên thứ tự tô pô: f[1] = 1, f[v] = tổng f[u] trên các đường u → v. Khó khăn là đồ thị **có thể có chu trình**: một vòng chỉ gây ra vô số lộ trình khi nó vừa **tới được từ 1**, vừa **tới được n**.',
        { fig: 'tap2:demlotrinh', w: 5.8, cap: 'Ba ví dụ: 5 lộ trình; vòng vô hại; vòng làm vô số lộ trình.' },
      ],
      naive: {
        title: 'Cách ngây thơ: QHĐ theo số hiệu nút',
        body: [
          'Ở Subtask 1, mọi con đường có u < v, nên thứ tự 1, 2, ..., n đã là một thứ tự tô pô: cứ duyệt u tăng dần và cộng f[u] vào f[v].',
          { fig: 'f_demlotrinh_naive', w: 2.6, cap: 'Sơ đồ khối của QHĐ theo số hiệu.' },
          { file: 'DEMLOTRINH_1theonhan', title: 'Cách ngây thơ: QHĐ theo số hiệu nút' },
          { cx: 'O(n + m), nhưng chỉ đúng khi u < v.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (u < v): **{{P:DEMLOTRINH_1theonhan:1}} điểm**.', '**Subtask 2, 3**: số hiệu không còn là thứ tự tô pô, và có chu trình: sai.'] },
        'Cải tiến "nửa vời": chạy Kahn trên các nút tới được từ 1, gặp chu trình là in −1. Cách này sai ở ví dụ 2: vòng 3 ⇄ 4 tới được từ 1 nhưng không dẫn tới 5. Chỉ được **{{S:DEMLOTRINH_2moichutrinh}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Phải phân biệt vòng **có ích** (nằm trên một lộ trình 1 → n) với vòng **vô hại** (không tới được từ 1, hoặc không dẫn tới n).'] },
      ],
      breakthrough: [
        'Một nút v nằm trên một lộ trình 1 → n khi và chỉ khi v **tới được từ 1** (tập A, duyệt từ 1 trên đồ thị) và **tới được n** (tập B, duyệt từ n trên đồ thị đảo chiều). Chỉ giữ lại các nút thuộc A ∩ B và các đường nối hai nút như vậy:',
        { ul: ['Nếu đồ thị con này có chu trình: có thể đi vòng bao nhiêu lần tùy ý rồi mới tới n, nên **vô số** lộ trình (in −1).', 'Ngược lại nó là DAG: chạy Kahn kèm QHĐ đếm f, lấy theo mô-đun.'] },
        { table: { cols: [1300, 2300, 2300, 2718], head: ['Ví dụ', 'A (từ 1)', 'B (tới n)', 'Kết luận'], rows: [
          ['1', '{1, 2, 3, 4, 5}', '{1, 2, 3, 4, 5}', 'DAG: f = 1, 1, 2, 3, **5**'], ['2', '{1, 2, 3, 4, 5}', '{1, 2, 5}', 'bỏ 3, 4 (vòng vô hại): **1**'], ['3', '{1, 2, 3, 4}', '{1, 2, 3, 4}', 'vòng 2 ⇄ 3 còn lại: **−1**']] } },
        { fig: 'f_demlotrinh_opt', w: 3.0, cap: 'Sơ đồ khối của lời giải.' },
      ],
      optimal: [
        { file: 'DEMLOTRINH', title: 'DEMLOTRINH.CPP: lọc nút có ích, Kahn + QHĐ' },
        { cx: 'O(n + m).' },
      ],
      traps: ['**Coi mọi chu trình là vô số lộ trình.**', '**Quên khuyên** u → u: đó cũng là một vòng (Kahn tự phát hiện vì bán bậc vào không bao giờ về 0).', '**In 0 khi không tới được n?** Đúng, nhưng nhớ kiểm tra trước khi xét vòng.', '**Kiểm tra "vô số" bằng f lớn:** f đã lấy mô-đun nên không dùng để phát hiện vô hạn được.'],
      approaches: [['DEMLOTRINH_1theonhan', 'QHĐ theo số hiệu nút'], ['DEMLOTRINH_2moichutrinh', 'Mọi chu trình đều là vô số'], ['DEMLOTRINH', 'Lọc nút có ích + Kahn']],
    },
    // ================================================================ 13.1
    {
      id: '13.1', key: 'num/low, bỏ qua đúng CẠNH vừa đi tới (không bỏ đỉnh cha).',
      understand: [
        'Con đường huyết mạch chính là **cầu** của đồ thị vô hướng (Tập 1, Bài 13). Điểm khác: có thể có **nhiều con đường nối cùng một cặp nút**; hai con đường song song không bao giờ là cầu.',
        { fig: 'tap2:huyetmach', w: 5.4, cap: 'Ví dụ: đường 4 và 7 là huyết mạch; đường 5 và 6 song song.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Chặn thử từng con đường',
        body: [
          'Đếm số thành phần liên thông (DSU). Với mỗi con đường i, đếm lại khi bỏ i; tăng lên thì i là huyết mạch.',
          { fig: 'f_huyetmach_naive', w: 2.8, cap: 'Sơ đồ khối của cách chặn thử.' },
          { file: 'HUYETMACH_1xoatung', title: 'Cách ngây thơ: chặn thử từng con đường' },
          { cx: 'O(m · (n + m)).' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n, m ≤ 1000): **{{P:HUYETMACH_1xoatung:1}} điểm**.', '**Subtask 2, 3**: 2·10^5^ lần dựng DSU: quá thời gian.'] },
        'Thuật toán num/low trong nhiều tài liệu viết "bỏ qua đỉnh cha" (`if (v == parent) continue`). Với đồ thị có cạnh song song, cách viết này bỏ qua **cả** con đường song song thứ hai, nên coi đường 5 là cầu. Chỉ đúng khi không có đường song song: **{{S:HUYETMACH_2chacha}} điểm** (chỉ Subtask 2).',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Cạnh song song là một "đường vòng" độ dài 2. Phải bỏ qua đúng **con đường** vừa đi tới, không phải mọi con đường dẫn về đỉnh cha.'] },
      ],
      breakthrough: [
        'Lưu số hiệu con đường cùng với đỉnh kề. Khi DFS từ u, bỏ qua đúng con đường pe[u] đã dùng để tới u. Con đường song song thứ hai có số hiệu khác, nên được coi là **cạnh ngược**, cập nhật low.',
        'Đường (p, u) trên cây DFS là cầu khi và chỉ khi **low[u] > num[p]**: từ cây con gốc u không có cạnh ngược nào "trèo" lên tới p hoặc cao hơn.',
        'Chạy tay ví dụ (DFS từ 1):',
        { table: { cols: [1100, 1500, 1300, 2400, 2318], head: ['Đỉnh', 'Tới bằng', 'num', 'low', 'Kết luận khi xong'], rows: [
          ['1', '', '1', '1', ''], ['2', 'đường 1', '2', '1', ''], ['3', 'đường 2', '3', '1 (đường 3 về 1)', ''], ['4', 'đường 4', '4', '4', 'low[4] = 4 > num[3] = 3: **đường 4 là cầu**'], ['5', 'đường 5', '5', '4 (đường 6 về 4)', 'low[5] = 4 = num[4]: không'], ['6', 'đường 7', '6', '6', 'low[6] = 6 > num[5] = 5: **đường 7 là cầu**']] } },
        { fig: 'f_huyetmach_opt', w: 2.8, cap: 'Xử lí khi DFS rời khỏi đỉnh u.' },
        { box: 'note', title: 'DFS KHÔNG ĐỆ QUY', body: ['Đồ thị là một đường thẳng 10^5^ đỉnh thì DFS đệ quy sâu 10^5^ tầng. Lời giải dùng ngăn xếp tự quản lí: st chứa đường đi từ gốc, it[u] là vị trí cạnh tiếp theo cần xét của u. Khi u hết cạnh, lấy u ra và cập nhật low của đỉnh cha (đỉnh mới ở đỉnh ngăn xếp).'] },
      ],
      optimal: [
        { file: 'HUYETMACH', title: 'HUYETMACH.CPP: num/low không đệ quy, bỏ qua theo số hiệu cạnh' },
        { cx: 'O(n + m).' },
      ],
      traps: ['**Bỏ qua theo đỉnh cha** khi có cạnh song song.', '**Quên đồ thị không liên thông:** phải DFS từ mọi đỉnh chưa thăm.', '**Dùng low[u] ≥ num[p]** (điều kiện của khớp) cho cầu.', '**In số hiệu theo thứ tự tìm được**, quên sắp xếp tăng dần.'],
      approaches: [['HUYETMACH_1xoatung', 'Chặn thử từng con đường'], ['HUYETMACH_2chacha', 'num/low, bỏ qua đỉnh cha'], ['HUYETMACH', 'num/low, bỏ qua cạnh vừa đi tới']],
    },
    // ================================================================ 13.2
    {
      id: '13.2', key: 'Khớp: số phần = (số con c có low[c] ≥ num[u]) + 1, riêng gốc thì không cộng 1.',
      understand: [
        'Trạm có sự cố làm lưới bị chia cắt chính là **khớp** (đỉnh khớp). Ở đây cần thêm **số phần** sau khi bỏ khớp đó.',
        { fig: 'tap2:bienap', w: 5.4, cap: 'Ví dụ: trạm 3 chia lưới thành 2 phần, trạm 4 thành 3 phần.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Cho từng trạm hỏng rồi đếm',
        body: [
          'Với mỗi trạm x, bỏ x đi và đếm số thành phần liên thông của phần còn lại bằng BFS.',
          { fig: 'f_bienap_naive', w: 2.8, cap: 'Sơ đồ khối của cách thử từng trạm.' },
          { file: 'BIENAP_1xoatung', title: 'Cách ngây thơ: thử từng trạm' },
          { cx: 'O(n · (n + m)).' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n, m ≤ 1000): **{{P:BIENAP_1xoatung:1}} điểm**.', '**Subtask 2**: 10^5^ lần BFS trên 3·10^5^ phần tử: quá thời gian.'] },
        'Dùng num/low nhưng áp dụng cùng một công thức "số con bị tách + 1" cho **cả gốc**: gốc không có "phần phía trên", nên gốc có một con sẽ bị báo nhầm là chia lưới thành 2 phần. Kết quả: **{{S:BIENAP_2quengoc}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Cần đếm, chỉ bằng một lần DFS, khi bỏ u thì các con của u trên cây DFS rơi vào bao nhiêu phần khác nhau.'] },
      ],
      breakthrough: [
        'Xét đỉnh u và một con c của nó trên cây DFS. Khi u hỏng, cây con gốc c **bị tách riêng** khi và chỉ khi không có cạnh ngược nào từ cây con đó lên **trên** u: **low[c] ≥ num[u]**. Gọi cnt[u] là số con như vậy.',
        { ul: ['u **không phải gốc**: mỗi con bị tách là một phần; các con còn lại cùng **phần phía trên** (chứa cha của u) tạo thêm 1 phần. Số phần = cnt[u] + 1.', 'u **là gốc**: không có phần phía trên; mọi con của gốc đều có low ≥ num[gốc] = 1. Số phần = cnt[gốc] = số con.'] },
        'Chạy tay ví dụ (DFS 1 → 2 → 3 → 4 → 5 → 6, rồi 4 → 7):',
        { table: { cols: [1200, 1200, 1400, 2300, 2518], head: ['Đỉnh', 'num', 'low', 'Con c có low[c] ≥ num', 'Số phần khi hỏng'], rows: [
          ['1 (gốc)', '1', '1', '2 (con duy nhất)', 'cnt = 1: không chia cắt'], ['2', '2', '1', 'không có', '1'], ['3', '3', '1', '4 (low 4 ≥ 3)', '1 + 1 = **2**'], ['4', '4', '4', '5 (low 4 ≥ 4), 7 (low 7 ≥ 4)', '2 + 1 = **3**'], ['5', '5', '4', 'không có (low[6] = 4 < 5)', '1'], ['6, 7', '6, 7', '4, 7', 'là lá', '1']] } },
        'Đúng với đáp án: trạm 3 (2 phần) và trạm 4 (3 phần).',
      ],
      optimal: [
        { file: 'BIENAP', title: 'BIENAP.CPP: num/low không đệ quy, đếm số con bị tách' },
        { cx: 'O(n + m).' },
      ],
      traps: ['**Xử lí gốc như mọi đỉnh khác.**', '**Đếm số con có low[c] ≥ num[u] nhưng quên +1** cho phần phía trên.', '**DFS đệ quy** trên lưới dạng đường thẳng 10^5^ trạm.'],
      approaches: [['BIENAP_1xoatung', 'Thử từng trạm, BFS đếm phần'], ['BIENAP_2quengoc', 'num/low, quên trường hợp gốc'], ['BIENAP', 'num/low, xử lí riêng gốc']],
    },
    // ================================================================ 13.3
    {
      id: '13.3', key: 'Nén khối không cầu → cây cầu; đáp số ⌈số lá / 2⌉.',
      understand: [
        'Mạng chịu được một sự cố khi và chỉ khi **không có cầu**. Cần thêm ít cáp nhất để mọi cầu biến mất. Một sợi cáp mới (a, b) "cứu" mọi cầu nằm trên đường đi từ a tới b.',
        { fig: 'tap2:capduphong', w: 5.4, cap: 'Ví dụ: bốn cầu, nén vòng {1, 2, 3} được cây có 3 lá.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Coi mạng như một cây',
        body: [
          'Nếu mạng là một cây (Subtask 1), mọi cạnh đều là cầu. Mỗi lá phải được nối thêm ít nhất một sợi cáp, và một sợi cáp phủ được nhiều nhất hai lá: cần ⌈L / 2⌉ sợi với L là số lá (và cận này đạt được).',
          { fig: 'f_capduphong_naive', w: 2.6, cap: 'Sơ đồ khối của cách đếm lá trên cây.' },
          { file: 'CAPDUPHONG_1lacay', title: 'Cách ngây thơ: đếm lá của đồ thị ban đầu' },
          { cx: 'O(n + m).' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (cây): **{{P:CAPDUPHONG_1lacay:1}} điểm**.', '**Subtask 2, 3**: có vòng; đỉnh bậc 1 của đồ thị không còn là "lá" đúng nghĩa. Ở ví dụ, đồ thị chỉ có 2 đỉnh bậc 1 (5 và 7) nhưng đáp số là 2, không phải 1.'] },
        'Tìm cầu bằng cách xóa thử từng cạnh rồi nén lại thì đúng, nhưng O(m · (n + m)): **{{S:CAPDUPHONG_2xoatung}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Công thức ⌈L / 2⌉ chỉ dùng được trên một **cây**. Cần biến đồ thị thành một cây mà vẫn giữ nguyên các cầu.'] },
      ],
      breakthrough: [
        { ol: ['Tìm mọi cầu bằng num/low (như bài HUYETMACH).', '**Nén** mỗi thành phần còn lại sau khi bỏ hết cầu (thành phần liên thông 2-cạnh) thành một đỉnh: dùng DSU gộp hai đầu của mọi cạnh **không phải** cầu.', 'Các cầu nối các đỉnh nén thành một **cây** (gọi là cây cầu). Đếm số lá L = số đỉnh nén có đúng một cầu đi vào.', 'Nếu cây chỉ có một đỉnh (không có cầu), đáp số 0; ngược lại đáp số ⌈L / 2⌉.'] },
        { table: { cols: [2600, 3000, 3018], head: ['Đỉnh nén', 'Các cầu nối vào', 'Bậc trên cây cầu'], rows: [['{1, 2, 3}', '3 – 4', '1: **lá**'], ['{4}', '3 – 4, 4 – 5, 4 – 6', '3'], ['{5}', '4 – 5', '1: **lá**'], ['{6}', '4 – 6, 6 – 7', '2'], ['{7}', '6 – 7', '1: **lá**']] } },
        'L = 3, đáp số ⌈3 / 2⌉ = **2**.',
        { fig: 'f_capduphong_opt', w: 2.8, cap: 'Sơ đồ khối của lời giải.' },
        { box: 'theorem', title: 'VÌ SAO ⌈L / 2⌉ SỢI LÀ ĐỦ?', body: ['Đánh số các lá theo thứ tự DFS trên cây cầu: ℓ~1~, ℓ~2~, ..., ℓ~L~. Nối ℓ~i~ với ℓ~i + L/2~ (khi L lẻ, nối thêm lá cuối với một lá bất kì). Mỗi cạnh của cây chia các lá thành hai phần, mỗi phần là một **đoạn liên tiếp** trong thứ tự DFS (tính vòng quanh), và cách nối "cách nhau L/2" luôn có một sợi cáp đi qua hai phần. Vậy mọi cạnh của cây đều nằm trên một vòng mới.'] },
      ],
      optimal: [
        { file: 'CAPDUPHONG', title: 'CAPDUPHONG.CPP: tìm cầu, nén bằng DSU, đếm lá' },
        { cx: 'O((n + m) · α(n)).' },
      ],
      traps: ['**Đếm lá trên đồ thị ban đầu** thay vì trên cây cầu.', '**Quên trường hợp không có cầu:** cả mạng nén thành một đỉnh, đáp số là 0.', '**Bỏ qua cạnh song song** khi tìm cầu (như bài HUYETMACH).'],
      approaches: [['CAPDUPHONG_1lacay', 'Đếm lá của đồ thị ban đầu'], ['CAPDUPHONG_2xoatung', 'Tìm cầu bằng cách xóa thử'], ['CAPDUPHONG', 'num/low + nén + đếm lá']],
    },
    // ================================================================ 14.1
    {
      id: '14.1', key: 'Nén thành phần liên thông mạnh; đếm thành phần có bán bậc vào 0.',
      understand: [
        'Báo tin cho một học sinh thì cả **thành phần liên thông mạnh** chứa bạn đó đều biết, rồi tin lan sang các thành phần "phía sau". Nén mỗi thành phần thành một đỉnh, ta được một DAG (Tập 1, Bài 14).',
        { fig: 'tap2:tindon', w: 5.4, cap: 'Ví dụ: bốn thành phần {1, 2, 3}, {4}, {5}, {6, 7}.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Đếm học sinh không ai kể cho',
        body: [
          'Một học sinh không có ai kể cho (bán bậc vào 0) thì bắt buộc phải được báo trực tiếp. Trên đồ thị không có chu trình (Subtask 1), báo cho đúng những bạn đó là đủ: từ mỗi đỉnh, đi ngược mãi các cung sẽ dừng ở một đỉnh có bán bậc vào 0.',
          { fig: 'f_tindon_naive', w: 2.6, cap: 'Sơ đồ khối của cách đếm bán bậc vào 0.' },
          { file: 'TINDON_1bacvao0', title: 'Cách ngây thơ: đếm học sinh có bán bậc vào 0' },
          { cx: 'O(n + m).' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (không có chu trình): **{{P:TINDON_1bacvao0:1}} điểm**.', '**Subtask 2, 3**: một nhóm bạn kể tin vòng quanh cho nhau mà không ai bên ngoài kể cho họ (như nhóm {1, 2, 3} ở ví dụ) cần một người được báo, nhưng không ai trong nhóm có bán bậc vào 0. Ví dụ ra 1 thay vì 2.'] },
        'Nén thành phần đúng, nhưng **nhầm chiều**: đếm các thành phần không có cung đi **ra** (những nhóm "cuối dòng" mà tin phải tới). Đó là số nhóm cần **nhận** tin, không phải số nhóm cần **được báo**: **{{S:TINDON_2bacra}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['"Bán bậc vào 0" chỉ đúng trên DAG. Cần biến đồ thị có chu trình thành DAG mà không làm thay đổi đáp số.'] },
      ],
      breakthrough: [
        'Nén mỗi thành phần liên thông mạnh thành một đỉnh. Trên DAG mới, câu trả lời là số đỉnh có bán bậc vào 0 (lập luận của Subtask 1). Một thành phần có bán bậc vào 0 khi không có cung nào từ thành phần **khác** đi vào nó.',
        { table: { cols: [2400, 3200, 3018], head: ['Thành phần', 'Cung đi vào từ thành phần khác', 'Phải báo trực tiếp?'], rows: [['{1, 2, 3}', 'không có', '**có**'], ['{4}', '3 → 4, 5 → 4', 'không'], ['{5}', 'không có', '**có**'], ['{6, 7}', '4 → 6', 'không']] } },
        'Đáp số **2**: báo cho một bạn trong {1, 2, 3} và cho bạn 5.',
        { fig: 'f_tindon_opt', w: 3.0, cap: 'Sơ đồ khối của lời giải.' },
        { box: 'note', title: 'TARJAN KHÔNG ĐỆ QUY', body: ['Ngăn xếp cs mô phỏng ngăn xếp gọi hàm; ngăn xếp S là ngăn xếp của thuật toán Tarjan. Khi u hết cạnh: lấy u khỏi cs, cập nhật low của cha, và nếu low[u] = num[u] thì lấy khỏi S mọi đỉnh tới u: đó là một thành phần. Cũng có thể dùng Kosaraju với hai lần DFS không đệ quy.'] },
      ],
      optimal: [
        { file: 'TINDON', title: 'TINDON.CPP: Tarjan không đệ quy, đếm thành phần nguồn' },
        { cx: 'O(n + m).' },
      ],
      traps: ['**Đếm học sinh có bán bậc vào 0** khi có chu trình.', '**Đếm cung trong cùng thành phần** vào bán bậc vào.', '**Tarjan đệ quy** khi máy chấm có ngăn xếp nhỏ (1 MB như nhiều máy chấm chạy Windows): vòng dài 10^5^ đỉnh sẽ làm tràn ngăn xếp. Lời giải mẫu dùng bản không đệ quy cho an toàn.'],
      approaches: [['TINDON_1bacvao0', 'Đếm học sinh có bán bậc vào 0'], ['TINDON_2bacra', 'Nén, đếm thành phần không có cung ra'], ['TINDON', 'Nén, đếm thành phần không có cung vào']],
    },
    // ================================================================ 14.2
    {
      id: '14.2', key: 'Nén SCC (vào thành phần là nhặt hết), QHĐ đường dài nhất trên DAG.',
      understand: [
        'Đã vào một thành phần liên thông mạnh thì đi được tới **mọi** địa điểm trong đó rồi quay ra: nhặt hết vàng của cả thành phần. Nén mỗi thành phần thành một đỉnh có trọng số w = tổng vàng, bài toán trở thành **đường đi có tổng trọng số lớn nhất** trên DAG, xuất phát từ thành phần chứa 1.',
        { fig: 'tap2:khobau', w: 5.4, cap: 'Ví dụ: vòng {1, 2, 3} (9 đồng) rồi sang 6 (7 đồng): 16.' },
      ],
      naive: {
        title: 'Cách ngây thơ: QHĐ theo thứ tự tô pô trên đồ thị gốc',
        body: [
          'Nếu đồ thị không có chu trình (Subtask 1), mỗi địa điểm thăm nhiều nhất một lần: best[v] = g~v~ + max best[u] trên các cung u → v, tính theo thứ tự tô pô (Kahn).',
          { fig: 'f_khobau_naive', w: 3.0, cap: 'Sơ đồ khối của QHĐ trên DAG.' },
          { file: 'KHOBAU_1dag', title: 'Cách ngây thơ: QHĐ theo Kahn trên đồ thị gốc' },
          { cx: 'O(n + m).' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (không có chu trình): **{{P:KHOBAU_1dag:1}} điểm**.', '**Subtask 2**: các đỉnh trên chu trình không bao giờ có bán bậc vào 0, Kahn bỏ sót cả vùng đó.'] },
        'Một lời giải đúng thuật toán nhưng lưu tổng vàng bằng `int`: tổng có thể tới 10^5^ · 10^9^ = 10^14^. Tràn số ngay cả ở Subtask 1: **{{S:KHOBAU_2int}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Đi vòng thì được nhặt nhiều địa điểm, nhưng không được tính một địa điểm hai lần. Cần một cách "gói" cả vòng lại thành một khối.'] },
      ],
      breakthrough: [
        'Tìm các thành phần bằng Tarjan. Thuật toán Tarjan đánh số thành phần theo **thứ tự tô pô ngược**: mọi cung giữa hai thành phần đều đi từ số **lớn** sang số **nhỏ**. Vậy chỉ cần duyệt x từ comp(1) giảm dần về 0 là đã theo đúng thứ tự tô pô:',
        { ul: ['best[comp(1)] = w[comp(1)], các thành phần khác chưa tới được (−1).', 'Với mỗi x đã tới được và mỗi cung x → y: best[y] = max(best[y], best[x] + w[y]).', 'Đáp số là max best[x].'] },
        { table: { cols: [2200, 2000, 2400, 2018], head: ['Thành phần', 'w', 'Tới từ', 'best'], rows: [['A = {1, 2, 3}', '5 + 1 + 3 = 9', 'xuất phát', '9'], ['B = {4, 5}', '4 + 2 = 6', 'A', '9 + 6 = 15'], ['C = {6}', '7', 'A', '9 + 7 = **16**']] } },
        { fig: 'f_khobau_opt', w: 3.0, cap: 'Sơ đồ khối của QHĐ trên đồ thị nén.' },
      ],
      optimal: [
        { file: 'KHOBAU', title: 'KHOBAU.CPP: Tarjan không đệ quy + QHĐ trên đồ thị nén' },
        { cx: 'O(n + m).' },
      ],
      traps: ['**Tràn số:** dùng long long cho w và best.', '**QHĐ từ mọi thành phần**, quên rằng phải xuất phát từ 1.', '**Duyệt thành phần theo chiều tăng** với Tarjan (ngược thứ tự tô pô).', '**Cộng w[x] hai lần** (một lần khi tới x, một lần khi rời x).'],
      approaches: [['KHOBAU_1dag', 'QHĐ trên đồ thị gốc (Kahn)'], ['KHOBAU_2int', 'Nén + QHĐ, dùng int'], ['KHOBAU', 'Nén + QHĐ, dùng long long']],
    },
    // ================================================================ 14.3
    {
      id: '14.3', key: '2-SAT: cung ¬x → y, ¬y → x; Tarjan; chọn khẳng định có số thành phần nhỏ hơn.',
      understand: [
        'Mỗi thí sinh i ứng với một biến đúng/sai: x~i~ = "nhận i". Mỗi giám khảo là một mệnh đề (a ∨ b) với a, b là x~i~ hoặc ¬x~i~. Đây chính là bài toán **2-SAT** (Tập 1, Bài 14).',
        { fig: 'tap2:tuyenchon', w: 5.6, cap: 'Đồ thị kéo theo của ví dụ 1.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Thử mọi phương án',
        body: [
          'Với n ≤ 20 có 2^20^ ≈ 10^6^ phương án. Biểu diễn phương án bằng một mặt nạ bit và kiểm tra lần lượt các giám khảo, dừng ngay khi có người không hài lòng.',
          { fig: 'f_tuyenchon_naive', w: 2.8, cap: 'Sơ đồ khối của cách thử mọi phương án.' },
          { file: 'TUYENCHON_1vetcan', title: 'Cách ngây thơ: thử mọi mặt nạ' },
          { cx: 'O(2^n^ · m) trong trường hợp xấu nhất.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n ≤ 20): **{{P:TUYENCHON_1vetcan:1}} điểm**.', '**Subtask 2**: 2^100000^ phương án.'] },
        'Cài đúng 2-SAT nhưng dựng phương án **ngược chiều** (chọn khẳng định có số thành phần **lớn** hơn) thì vẫn in YES đúng lúc, nhưng phương án thường không thỏa mãn: **{{S:TUYENCHON_2nguocthutu}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Phải "lan truyền" hệ quả của từng lựa chọn: chọn loại thí sinh này thì bắt buộc nhận thí sinh kia... Cần một cấu trúc ghi lại mọi hệ quả cùng lúc.'] },
      ],
      breakthrough: [
        'Dựng **đồ thị kéo theo** 2n đỉnh (x~i~ và ¬x~i~). Mệnh đề (a ∨ b) tương đương "nếu không a thì b" và "nếu không b thì a": thêm hai cung **¬a → b** và **¬b → a**.',
        { ul: ['Nếu x~i~ và ¬x~i~ cùng một thành phần liên thông mạnh thì x~i~ kéo theo ¬x~i~ và ngược lại: **vô nghiệm**.', 'Ngược lại luôn có nghiệm: với Tarjan (đánh số theo thứ tự tô pô ngược), chọn x~i~ đúng khi **comp[x~i~] < comp[¬x~i~]**, tức là x~i~ nằm "sau" ¬x~i~ trong thứ tự tô pô.'] },
        'Ví dụ 1: (1 ∨ 2), (¬1 ∨ 3), (¬2 ∨ ¬3), (2 ∨ ¬3) cho 8 cung:',
        { table: { cols: [2600, 3000, 3018], head: ['Giám khảo', 'Cung thứ nhất', 'Cung thứ hai'], rows: [['1 ∨ 2', '¬1 → 2', '¬2 → 1'], ['¬1 ∨ 3', '1 → 3', '¬3 → ¬1'], ['¬2 ∨ ¬3', '2 → ¬3', '3 → ¬2'], ['2 ∨ ¬3', '¬2 → ¬3', '3 → 2']] } },
        'Từ 3 có 3 → 2 → ¬3: chọn "nhận 3" sẽ kéo theo "loại 3", nên 3 bị loại. Rồi ¬3 → ¬1 (loại 1), ¬1 → 2 (nhận 2). Phương án **010**.',
        { fig: 'f_tuyenchon_opt', w: 3.2, cap: 'Sơ đồ khối của lời giải 2-SAT.' },
        { box: 'theorem', title: 'VÌ SAO CHỌN THEO THỨ TỰ TÔ PÔ LÀ ĐÚNG?', body: ['Giả sử cách chọn làm hỏng một mệnh đề (a ∨ b): cả a và b đều sai, tức ¬a và ¬b đúng. Theo cách chọn, ¬a đứng sau a và ¬b đứng sau b trong thứ tự tô pô. Nhưng có cung ¬a → b nên b đứng sau ¬a, và cung ¬b → a nên a đứng sau ¬b. Ghép lại: a < ¬a ≤ b < ¬b ≤ a, vô lí. (Ở đây "≤" là thứ tự tô pô của các thành phần.)'] },
      ],
      optimal: [
        { file: 'TUYENCHON', title: 'TUYENCHON.CPP: 2-SAT bằng Tarjan không đệ quy' },
        { cx: 'O(n + m).' },
      ],
      traps: ['**Chọn ngược chiều** (đặc biệt khi đổi từ Tarjan sang Kosaraju: Kosaraju đánh số theo thứ tự tô pô **xuôi**).', '**Chỉ thêm một cung** cho mỗi mệnh đề.', '**Mệnh đề (x ∨ x)** (cả hai mong muốn giống nhau): vẫn đúng với cách dựng trên, nó tạo cung ¬x → x, buộc x đúng.'],
      approaches: [['TUYENCHON_1vetcan', 'Thử mọi phương án'], ['TUYENCHON_2nguocthutu', '2-SAT, dựng phương án ngược chiều'], ['TUYENCHON', '2-SAT bằng Tarjan']],
    },
    // ================================================================ 15.1
    {
      id: '15.1', key: 'Định lí Euler: số điểm bậc lẻ là 0 hoặc 2, và các đoạn liên thông với nhau.',
      understand: [
        'Vẽ một nét là đi qua mọi cạnh đúng một lần: **đường đi Euler** (Tập 1, Bài 15). Có hai điều kiện: số đỉnh bậc lẻ là 0 hoặc 2, và mọi đỉnh **có cạnh** cùng nằm trong một thành phần liên thông. Điểm không có đoạn nào thì bỏ qua.',
        { fig: 'tap2:netve', w: 5.8, cap: 'Ba hình của ví dụ: vẽ được, bốn điểm lẻ, hai mảnh rời.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Chỉ đếm điểm bậc lẻ',
        body: [
          'Ở Subtask 1, hình liên thông và mọi điểm đều có đoạn: chỉ cần đếm số điểm bậc lẻ.',
          { fig: 'f_netve_naive', w: 2.6, cap: 'Sơ đồ khối của cách chỉ đếm bậc.' },
          { file: 'NETVE_1chiembac', title: 'Cách ngây thơ: chỉ đếm điểm bậc lẻ' },
          { cx: 'O(n + m) cho mỗi hình.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1**: **{{P:NETVE_1chiembac:1}} điểm**.', '**Subtask 2**: hình 3 của ví dụ (hai tam giác rời nhau) có mọi điểm bậc chẵn nhưng không vẽ được bằng một nét.'] },
        'Thêm kiểm tra liên thông nhưng tính bậc của vòng nhỏ (u, u) là **1** thay vì 2: một hình có vòng nhỏ bị coi là có điểm bậc lẻ. Được **{{S:NETVE_2khuyen}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Điều kiện về bậc là cần nhưng chưa đủ; điều kiện liên thông chỉ áp dụng cho các điểm **có đoạn**, và vòng nhỏ đóng góp 2 vào bậc.'] },
      ],
      breakthrough: [
        { ol: ['Đọc từng đoạn (u, v): deg[u]++, deg[v]++ (vòng nhỏ u = v làm deg[u] tăng 2, đúng như "đi vào rồi đi ra"), và gộp u, v trong DSU.', 'Duyệt các điểm có deg > 0: đếm số điểm bậc lẻ, và kiểm tra chúng có cùng gốc DSU không.', 'Vẽ được khi và chỉ khi liên thông và số điểm lẻ bằng 0 hoặc 2.'] },
        { table: { cols: [1500, 3400, 1900, 1818], head: ['Hình', 'Bậc các điểm', 'Liên thông?', 'Kết luận'], rows: [['1', '1: 4, 2: 4, **3: 3, 4: 3**, 5: 2', 'có', '**YES**'], ['2', '**1: 3, 2: 1, 3: 1, 4: 1**', 'có', '**NO**'], ['3', 'mọi điểm bậc 2', '**không**', '**NO**']] } },
      ],
      optimal: [
        { file: 'NETVE', title: 'NETVE.CPP: đếm bậc lẻ + DSU kiểm tra liên thông' },
        { cx: 'O((n + m) · α(n)) cho mỗi hình.' },
      ],
      traps: ['**Kiểm tra liên thông trên mọi điểm**, kể cả điểm không có đoạn nào.', '**Vòng nhỏ chỉ cộng 1 vào bậc.**', '**Quên khởi tạo lại** mảng bậc và DSU giữa các hình.', '**Cho rằng "số điểm lẻ = 1"** có thể xảy ra: tổng bậc luôn chẵn, nên số điểm lẻ luôn chẵn.'],
      approaches: [['NETVE_1chiembac', 'Chỉ đếm điểm bậc lẻ'], ['NETVE_2khuyen', 'Có kiểm tra liên thông, vòng nhỏ cộng 1'], ['NETVE', 'Định lí Euler đầy đủ']],
    },
    // ================================================================ 15.2
    {
      id: '15.2', key: '7 đỉnh, mỗi quân là một cạnh: đường Euler bằng Hierholzer không đệ quy.',
      understand: [
        'Coi mỗi số chấm 0..6 là một **đỉnh**, mỗi quân domino a|b là một **cạnh** nối a với b (quân a|a là vòng nhỏ). Một hàng domino hợp lệ chính là một **đường đi Euler** trên đồ thị 7 đỉnh này: quân đứng sau bắt đầu ở đúng đỉnh mà quân đứng trước kết thúc.',
        { fig: 'tap2:domino', w: 5.6, cap: 'Ví dụ 1: đồ thị 7 đỉnh và đường Euler 2 → 1 → 3 → 2 → 4 → 4.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Quay lui đặt từng quân',
        body: [
          'Thử đặt lần lượt từng quân chưa dùng (theo hai chiều) vào cuối hàng, quay lui khi không đặt tiếp được.',
          { fig: 'f_domino_naive', w: 3.0, cap: 'Sơ đồ khối của cách quay lui.' },
          { file: 'DOMINO_1vetcan', title: 'Cách ngây thơ: quay lui' },
          { cx: 'O(n! · 2^n^) trong trường hợp xấu nhất.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n ≤ 8): **{{P:DOMINO_1vetcan:1}} điểm**.', '**Subtask 2**: n = 10^5^, quay lui không thể.'] },
        'Cài Hierholzer nhưng **quên kiểm tra** đường tìm được có dùng đủ n quân không: nếu các quân tạo thành hai nhóm rời nhau (ví dụ 2: 0|0 và 1|1), chương trình in một hàng thiếu quân. Kết quả: **{{S:DOMINO_2quenlienthong}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Quay lui đặt **quân** (cạnh) theo kiểu "đường đi Hamilton" là bài toán khó. Phải nhìn mỗi quân là một **cạnh** để dùng được lí thuyết Euler.'] },
      ],
      breakthrough: [
        { ol: ['Đếm bậc 7 đỉnh. Số đỉnh bậc lẻ khác 0 và 2: in NO.', 'Bắt đầu từ một đỉnh lẻ (nếu có), hoặc từ một đầu của quân 1.', 'Chạy **Hierholzer không đệ quy**: ngăn xếp chứa (đỉnh, quân dùng để tới đỉnh đó). Đỉnh trên cùng còn quân chưa dùng thì đi tiếp; hết quân thì đẩy vào kết quả.', 'Kết quả ít hơn n + 1 phần tử: các quân không liên thông, in NO. Ngược lại đảo ngược kết quả, in từng quân kèm dấu + hoặc − tùy chiều đi.'] },
        { table: { cols: [1300, 1500, 1500, 1500, 1500, 1318], head: ['Đỉnh', '1', '2', '3', '4', 'Khác'], rows: [['Bậc (ví dụ 1)', '2', '**3**', '2', '**3**', '0'], ['Ghi chú', '', 'lẻ: xuất phát', '', 'lẻ: kết thúc', '']] } },
        { fig: 'f_domino_opt', w: 3.2, cap: 'Sơ đồ khối của lời giải.' },
      ],
      optimal: [
        { file: 'DOMINO', title: 'DOMINO.CPP: Hierholzer không đệ quy trên đồ thị 7 đỉnh' },
        { cx: 'O(n).' },
      ],
      traps: ['**Không kiểm tra tính liên thông** (số quân trong đường đi).', '**Đánh dấu đỉnh** thay vì đánh dấu **quân**: các quân giống hệt nhau phải được dùng riêng.', '**Bỏ qua quân a|a** khi tính bậc (vòng nhỏ cộng 2).', '**Hierholzer đệ quy:** đường đi dài 10^5^ cạnh.'],
      approaches: [['DOMINO_1vetcan', 'Quay lui'], ['DOMINO_2quenlienthong', 'Hierholzer, quên kiểm tra liên thông'], ['DOMINO', 'Hierholzer đầy đủ']],
    },
    // ================================================================ 15.3
    {
      id: '15.3', key: 'Đồ thị de Bruijn: đỉnh là xâu k − 1 chữ số, cạnh là mã; chu trình Euler.',
      understand: [
        'Có b^k^ mã, mỗi mã phải xuất hiện như một đoạn con. Xâu độ dài L có L − k + 1 đoạn con độ dài k, nên L ≥ b^k^ + k − 1. Đáp số đạt đúng cận này: mỗi phím bấm sau k − 1 phím đầu tạo ra một mã **mới**.',
        { fig: 'tap2:ketsat', w: 5.4, cap: 'Đồ thị de Bruijn với b = 2, k = 3.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Quay lui từng phím',
        body: [
          'Bắt đầu bằng k chữ số 0. Thử bấm thêm từng chữ số d sao cho k chữ số cuối là một mã **chưa gặp**; không bấm tiếp được thì quay lui.',
          { fig: 'f_ketsat_naive', w: 3.0, cap: 'Sơ đồ khối của cách quay lui.' },
          { file: 'KETSAT_1quaylui', title: 'Cách ngây thơ: quay lui' },
          { cx: 'Hàm mũ trong trường hợp xấu nhất; độ sâu đệ quy b^k^.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1, 2**: điểm thực tế **{{P:KETSAT_1quaylui:1}}** và **{{P:KETSAT_1quaylui:2}}** (tổng **{{S:KETSAT_1quaylui}} điểm**).', '**Subtask 3**: b^k^ = 10^6^, đệ quy sâu 10^6^ tầng: tràn ngăn xếp.'] },
        'Hierholzer **đệ quy** trên đồ thị de Bruijn là lời giải đúng, nhưng chu trình có 10^6^ cạnh và độ sâu đệ quy cũng tới 10^6^: **{{S:KETSAT_2dequy}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Quay lui đang đi tìm đường **Hamilton** qua các mã (mỗi mã là một đỉnh). Cần đổi góc nhìn: mỗi mã là một **cạnh**, để bài toán trở thành chu trình Euler.'] },
      ],
      breakthrough: [
        'Đồ thị **de Bruijn**: đỉnh là các xâu k − 1 chữ số (N = b^k − 1^ đỉnh, viết như một số hệ b). Từ đỉnh u, bấm chữ số d đi tới đỉnh (u · b + d) mod N; cạnh này ứng với mã k chữ số "u nối d". Mỗi đỉnh có đúng b cạnh ra và b cạnh vào, đồ thị liên thông mạnh: **luôn có chu trình Euler**.',
        'Đi theo chu trình Euler từ đỉnh 00...0: xâu kết quả là k − 1 chữ số 0, tiếp theo là chữ số trên từng cạnh. Mỗi mã xuất hiện đúng một lần, độ dài b^k^ + k − 1.',
        { table: { cols: [2000, 2200, 2200, 2218], head: ['Cạnh thứ', 'Đi từ đỉnh', 'Bấm', 'Mã mới'], rows: [['bắt đầu', '00', '', ''], ['1', '00', '0', '000'], ['2', '00', '1', '001'], ['3', '01', '0', '010'], ['4', '10', '1', '101'], ['5', '01', '1', '011'], ['6', '11', '1', '111'], ['7', '11', '0', '110'], ['8', '10', '0', '100']] } },
        'Ví dụ 1 (b = 2, k = 3) cho xâu **0001011100**, độ dài 2^3^ + 2 = 10.',
        { fig: 'f_ketsat_opt', w: 3.2, cap: 'Sơ đồ khối của lời giải.' },
        { box: 'note', title: 'TRƯỜNG HỢP k = 1', body: ['N = b^0^ = 1: chỉ có một đỉnh, mọi cạnh là vòng nhỏ. Thuật toán vẫn chạy đúng và in b chữ số 0, 1, ..., b − 1 (theo một thứ tự nào đó).'] },
      ],
      optimal: [
        { file: 'KETSAT', title: 'KETSAT.CPP: chu trình Euler trên đồ thị de Bruijn, không đệ quy' },
        { cx: 'O(b^k^).' },
      ],
      traps: ['**Đệ quy sâu 10^6^ tầng.**', '**Quên k − 1 chữ số đầu** của xâu.', '**Tính N = b^k − 1^ bằng pow** (số thực): dùng vòng nhân số nguyên.', '**b = 1:** chỉ có một mã 00...0, đáp số là k chữ số 0.'],
      approaches: [['KETSAT_1quaylui', 'Quay lui từng phím'], ['KETSAT_2dequy', 'Hierholzer đệ quy'], ['KETSAT', 'Hierholzer không đệ quy']],
    },
  ],
};
