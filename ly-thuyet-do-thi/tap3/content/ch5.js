// TẬP 3 — CHƯƠNG 5. CẶP GHÉP VÀ LUỒNG
module.exports = {
  no: 5,
  intro: 'Chương 5 gồm những bài toán "phân phối": xếp người vào chỗ, đặt quân lên bảng, chia nước qua đường ống. Cách ngây thơ thường là **tham lam** (ai đến trước được chọn trước) hoặc **vét cạn**. Tham lam sai vì một lựa chọn sớm có thể chặn mất nhiều lựa chọn tốt hơn về sau; lời giải đúng cho phép **đổi ý** thông qua đường tăng (cặp ghép) hoặc cung ngược (luồng). Nhiều bài còn đòi chỉ ra **cách làm**, không chỉ con số: phải đọc thêm thông tin từ cặp ghép, từ đồ thị thặng dư.',
  solutions: [
    // ================================================================ 16.1
    {
      id: '16.1', key: 'Cặp ghép cực đại trên đồ thị hai phía bằng đường tăng (Kuhn).',
      understand: [
        'Bên trái là thí sinh, bên phải là phòng; thí sinh i nối với các phòng trong danh sách của mình. Mỗi cách xếp là một **cặp ghép**; cần cặp ghép **cực đại** (Tập 1, Bài 16).',
        { fig: 'tap2:xepphong', w: 5.0, cap: 'Ví dụ: xếp được 3 thí sinh.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Vét cạn cách xếp',
        body: [
          'Lần lượt xét từng thí sinh: hoặc xếp vào một phòng còn trống trong danh sách, hoặc không xếp. Cắt nhánh khi có xếp hết số thí sinh còn lại cũng không vượt kỉ lục.',
          { fig: 'f_xepphong_naive', w: 3.0, cap: 'Sơ đồ khối của cách vét cạn.' },
          { file: 'XEPPHONG_1vetcan', title: 'Cách ngây thơ: vét cạn có cắt nhánh' },
          { cx: 'Hàm mũ: khoảng (k + 1)^n^.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n, m ≤ 10): **{{P:XEPPHONG_1vetcan:1}} điểm**.', '**Subtask 2**: n = 1000, không thể.'] },
        'Tham lam "mỗi thí sinh lấy phòng trống đầu tiên trong danh sách" chạy rất nhanh nhưng sai. Ở ví dụ: thí sinh 1 lấy phòng 1, thí sinh 2 (chỉ thi được phòng 1) hết chỗ, thí sinh 3 lấy phòng 2, thí sinh 4 hết chỗ: chỉ 2 người. Kết quả: **{{S:XEPPHONG_2thamlam}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Tham lam không biết **đổi ý**: thí sinh 1 có thể nhường phòng 1 cho thí sinh 2 rồi sang phòng 2. Cần một cách "dời chỗ dây chuyền" có hệ thống.'] },
      ],
      breakthrough: [
        '**Đường tăng:** khi xếp thí sinh u, thử từng phòng p của u. Nếu p trống, xếp ngay. Nếu p đã có người w, thử "đẩy" w sang một phòng khác của w (đệ quy). Mỗi lần xếp thêm được một người, cặp ghép tăng 1. Mảng vis đánh dấu phòng đã thử trong **lần tìm hiện tại** để không đi vòng.',
        'Chạy tay ví dụ (thí sinh 1: {1, 2}, 2: {1}, 3: {2, 3}, 4: {2}):',
        { table: { cols: [1400, 4400, 2818], head: ['Xếp', 'Đường tăng tìm được', 'Phòng 1, 2, 3'], rows: [
          ['1', 'phòng 1 trống', '1, –, –'], ['2', 'phòng 1 (của 1) → 1 dời sang phòng 2', '2, 1, –'], ['3', 'phòng 2 (của 1) → 1 thử phòng 1 (của 2) → 2 hết đường; thử phòng 3: trống', '2, 1, 3'], ['4', 'phòng 2 (của 1) → 1 thử phòng 1 (của 2) → 2 hết đường: **thất bại**', '2, 1, 3']] } },
        'Xếp được **3** thí sinh.',
        { fig: 'f_xepphong_opt', w: 3.0, cap: 'Sơ đồ khối của hàm kuhn(u).' },
        { box: 'theorem', title: 'ĐỊNH LÍ BERGE', body: ['Một cặp ghép là cực đại khi và chỉ khi không còn đường tăng. Thuật toán Kuhn thử tìm đường tăng từ từng đỉnh trái đúng một lần; có thể chứng minh rằng nếu không tìm được đường tăng từ u lúc này thì về sau cũng không cần thử lại u.'] },
      ],
      optimal: [
        { file: 'XEPPHONG', title: 'XEPPHONG.CPP: thuật toán Kuhn' },
        { cx: 'O(n · Σk~i~) = 1000 · 10^5^ = 10^8^ trong trường hợp xấu nhất; thực tế nhanh hơn nhiều.' },
      ],
      traps: ['**Tham lam** theo thứ tự đọc vào.', '**Quên đặt lại vis** cho mỗi thí sinh (dùng biến đếm stamp để khỏi xóa mảng).', '**Đánh dấu thí sinh** thay vì đánh dấu phòng trong vis.'],
      approaches: [['XEPPHONG_1vetcan', 'Vét cạn có cắt nhánh'], ['XEPPHONG_2thamlam', 'Tham lam: phòng trống đầu tiên'], ['XEPPHONG', 'Kuhn (đường tăng)']],
    },
    // ================================================================ 16.2
    {
      id: '16.2', key: 'Tô bàn cờ: domino = cạnh nối ô trắng với ô đen; cặp ghép cực đại.',
      understand: [
        'Tô bảng như bàn cờ: ô (i, j) trắng nếu i + j chẵn, đen nếu lẻ. Hai ô kề cạnh luôn **khác màu**, nên mỗi quân domino phủ đúng một ô trắng và một ô đen. Đặt domino không chồng nhau chính là chọn một **cặp ghép** giữa ô trắng trống và ô đen trống kề cạnh.',
        { fig: 'tap2:datdomino', w: 5.0, cap: 'Ví dụ: 10 ô trống, đặt được 5 quân.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Chia đôi số ô trống',
        body: [
          'Khi không có ô cấm (Subtask 1), luôn phủ được ⌊R·C / 2⌋ quân: xếp ngang từng hàng, hàng lẻ ô thì dùng thêm quân dọc. Vậy chỉ cần đếm ô trống chia 2.',
          { fig: 'f_datdomino_naive', w: 2.4, cap: 'Sơ đồ khối của công thức.' },
          { file: 'DATDOMINO_1congthuc', title: 'Cách ngây thơ: số ô trống chia 2' },
          { cx: 'O(R · C).' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (không có ô cấm): **{{P:DATDOMINO_1congthuc:1}} điểm**.', '**Subtask 2, 3**: sai. Bảng 2 × 2 có hai ô cấm chéo nhau còn 2 ô trống nhưng không kề nhau: đáp số 0, công thức cho 1.'] },
        'Với bảng hẹp có thể dùng **QHĐ trạng thái theo hồ sơ** (broken profile): duyệt từng ô, mặt nạ C bit ghi ô nào đã bị quân trước chiếm. Đúng, nhưng 2^C^ trạng thái chỉ dùng được khi cạnh ngắn của bảng nhỏ: **{{S:DATDOMINO_2bitmask}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Bảng 100 × 100 có tới 10^4^ ô; mọi cách "nhớ trạng thái của cả một hàng" đều quá lớn. Cần một mô hình không phụ thuộc vào hình dạng bảng.'] },
      ],
      breakthrough: [
        'Dựng đồ thị hai phía: bên trái các ô trắng trống, bên phải các ô đen trống, cạnh nối hai ô kề cạnh. Đáp số là **kích thước cặp ghép cực đại**. Đồ thị có tới 5000 đỉnh mỗi bên và khoảng 2·10^4^ cạnh (mỗi ô có tối đa 4 ô kề), Kuhn chạy rất nhanh.',
        { table: { cols: [2900, 2900, 2818], head: ['Bảng', 'Ô trắng / ô đen trống', 'Cặp ghép cực đại'], rows: [['Ví dụ (3 × 4)', '5 / 5', '**5**'], ['2 × 2, cấm (1, 2) và (2, 1)', '2 / 0', '**0**'], ['3 × 3 không cấm', '5 / 4', '**4**']] } },
        { fig: 'f_datdomino_opt', w: 3.0, cap: 'Sơ đồ khối của lời giải.' },
        { box: 'def', title: 'MỞ RỘNG: HOPCROFT–KARP', body: ['Khi đồ thị lớn hơn nữa (10^5^ đỉnh), dùng Hopcroft–Karp: mỗi pha BFS chia tầng rồi tìm nhiều đường tăng ngắn nhất rời nhau bằng DFS; độ phức tạp O(E · √V).'] },
      ],
      optimal: [
        { file: 'DATDOMINO', title: 'DATDOMINO.CPP: tô bàn cờ + Kuhn' },
        { cx: 'O(V · E) trên lí thuyết, với V ≈ 5000, E ≈ 2·10^4^; thực tế chỉ vài phần trăm giây.' },
      ],
      traps: ['**Công thức "số ô trống chia 2"** khi có ô cấm.', '**Nối cả hai chiều** (ô trắng – ô đen và ô đen – ô trắng) rồi chạy Kuhn từ mọi ô: đếm mỗi quân hai lần.', '**Đánh số ô** i · C + j nhưng cấp phát mảng R · R.'],
      approaches: [['DATDOMINO_1congthuc', 'Số ô trống chia 2'], ['DATDOMINO_2bitmask', 'QHĐ hồ sơ trên mặt nạ bit'], ['DATDOMINO', 'Tô bàn cờ + cặp ghép']],
    },
    // ================================================================ 16.3
    {
      id: '16.3', key: 'Định lí König: phủ đỉnh nhỏ nhất = cặp ghép cực đại; dựng phủ từ tập Z.',
      understand: [
        'Đồ thị hai phía: bên trái R hàng, bên phải C cột; mỗi ô quan trọng (r, c) là một **cạnh** nối hàng r với cột c. Lắp camera ở hàng r giám sát mọi cạnh tại r. Cần chọn ít đỉnh nhất sao cho mọi cạnh có ít nhất một đầu được chọn: **phủ đỉnh nhỏ nhất**.',
        { fig: 'tap2:camera', w: 5.0, cap: 'Ví dụ: hàng 1 và cột 3 là đủ.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Thử mọi tập hàng',
        body: [
          'Thử mọi tập hàng H (2^R^ tập). Mọi ô quan trọng không thuộc hàng nào trong H bắt buộc phải được giám sát bằng cột của nó: số camera = |H| + số cột như vậy.',
          { fig: 'f_camera_naive', w: 3.0, cap: 'Sơ đồ khối của cách thử mọi tập hàng.' },
          { file: 'CAMERA_1vetcan', title: 'Cách ngây thơ: thử mọi tập hàng' },
          { cx: 'O(2^R^ · K · log K).' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (R, C ≤ 8): **{{P:CAMERA_1vetcan:1}} điểm**.', '**Subtask 2, 3**: 2^1000^ tập hàng.'] },
        'Biết định lí König thì in đúng **số** camera bằng kích thước cặp ghép cực đại. Nhưng nhiều bạn in luôn "các hàng đã được ghép" làm cách lắp: ở ví dụ đó là hàng 1 và hàng 2, bỏ sót ô (3, 3) và (4, 3). Cách này chỉ đúng dòng đầu: **{{S:CAMERA_2chiinso}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Cặp ghép cho biết **bao nhiêu** camera, nhưng chưa cho biết **lắp ở đâu**. Cần một quy tắc chọn, với mỗi cạnh ghép, đúng một đầu của nó.'] },
      ],
      breakthrough: [
        { ol: ['Tìm cặp ghép cực đại (Kuhn), kích thước t.', 'Tìm tập **Z**: các đỉnh tới được từ một **hàng chưa ghép** bằng đường đan xen (từ hàng sang cột theo cạnh bất kì, từ cột về hàng theo cạnh **ghép**).', 'Phủ đỉnh nhỏ nhất: **các hàng KHÔNG thuộc Z** và **các cột THUỘC Z**. Tập này có đúng t đỉnh: mỗi cạnh ghép đóng góp đúng một đầu.'] },
        'Chạy tay ví dụ:',
        { table: { cols: [2400, 3200, 3018], head: ['Bước', 'Kết quả', 'Ghi chú'], rows: [
          ['Cặp ghép', 'hàng 1 – cột 1, hàng 2 – cột 3', 't = 2'], ['Hàng chưa ghép', 'hàng 3, hàng 4', 'đưa vào Z'], ['Từ hàng 3, 4', 'cột 3', 'cột 3 ghép với hàng 2: thêm hàng 2'], ['Từ hàng 2', 'cột 3 (đã có)', 'Z = {H2, H3, H4, C3}'], ['Phủ', '**H 1** (không thuộc Z), **C 3** (thuộc Z)', '2 camera']] } },
        { fig: 'f_camera_opt', w: 3.2, cap: 'Sơ đồ khối của lời giải.' },
        { box: 'theorem', title: 'VÌ SAO TẬP NÀY LÀ PHỦ?', body: ['Xét một cạnh (r, c). Nếu r ∉ Z thì r được chọn. Nếu r ∈ Z: khi r là hàng chưa ghép, mọi cạnh từ r đều đưa c vào Z; khi r được ghép, r vào Z qua chính cột ghép với nó, và từ r lại đi tiếp được sang c. Vậy c ∈ Z, c được chọn. Mỗi hàng ∉ Z đều đã ghép (hàng chưa ghép thuộc Z) và mỗi cột ∈ Z đều đã ghép (nếu không, có đường tăng); hai đầu của một cạnh ghép không thể cùng được chọn. Do đó số đỉnh đúng bằng t.'] },
      ],
      optimal: [
        { file: 'CAMERA', title: 'CAMERA.CPP: Kuhn + dựng phủ đỉnh theo König' },
        { cx: 'O(R · K) cho Kuhn, O(R + C + K) cho bước dựng phủ.' },
      ],
      traps: ['**In các hàng đã ghép** làm cách lắp.', '**Bắt đầu đường đan xen từ cột chưa ghép** nhưng vẫn dùng công thức "hàng ∉ Z, cột ∈ Z" (phải đổi vai trò tương ứng).', '**In một hàng hai lần** (khi vừa ∉ Z vừa được thêm theo cách khác).'],
      approaches: [['CAMERA_1vetcan', 'Thử mọi tập hàng'], ['CAMERA_2chiinso', 'Đúng số camera, in các hàng đã ghép'], ['CAMERA', 'Kuhn + định lí König']],
    },
    // ================================================================ 17.1
    {
      id: '17.1', key: 'Dinic; S = các trạm tới được từ 1 trên đồ thị thặng dư.',
      understand: [
        'Phần đầu là **luồng cực đại** (Tập 1, Bài 17). Phần sau là **lát cắt nhỏ nhất**: theo định lí luồng cực đại – lát cắt nhỏ nhất, dung lượng nhỏ nhất bằng đúng F. Có thể có nhiều lát cắt cùng dung lượng F; đề bài chọn lát cắt có S **ít trạm nhất**.',
        { fig: 'tap2:duongong', w: 5.4, cap: 'Ví dụ: F = 15, lát cắt S = {1, 2}.' },
      ],
      naive: {
        title: 'Cách ngây thơ: In các ống chảy đầy',
        body: [
          'Tính F bằng Dinic, rồi in mọi ống mà luồng chảy đầy (dung lượng thặng dư bằng 0), vì "ống nút cổ chai thì phải chảy đầy".',
          { fig: 'f_duongong_naive', w: 2.6, cap: 'Sơ đồ khối của cách in ống bão hòa.' },
          { file: 'DUONGONG_1baohoa', title: 'Cách ngây thơ: in các ống bão hòa' },
          { cx: 'O(n^2^ · m) cho Dinic.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (chỉ cần F): **{{P:DUONGONG_1baohoa:1}} điểm**.', '**Subtask 2**: mọi ống trên lát cắt đều chảy đầy, nhưng điều ngược lại không đúng: một ống ở "giữa" mạng cũng có thể chảy đầy mà không thuộc lát cắt nào.'] },
        'Một cách khác: lấy T = các trạm còn **tới được n** trên đồ thị thặng dư, S là phần còn lại. Đó cũng là một lát cắt nhỏ nhất, nhưng là lát cắt có S **nhiều** trạm nhất: **{{S:DUONGONG_2snhieunhat}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Biết giá trị F, nhưng phải tìm đúng **tập** S nhỏ nhất có dung lượng F.'] },
      ],
      breakthrough: [
        'Sau khi chạy xong luồng cực đại, xét **đồ thị thặng dư**. Gọi S là tập các trạm **tới được từ 1** bằng các cung còn dung lượng thặng dư dương.',
        { ul: ['n ∉ S (nếu không sẽ còn đường tăng), nên (S, phần còn lại) là một lát cắt.', 'Mọi ống từ S ra ngoài đều chảy đầy, mọi ống từ ngoài vào S đều không có luồng: dung lượng lát cắt bằng đúng F, nên đây là lát cắt nhỏ nhất.', 'Mọi lát cắt nhỏ nhất (S\', T\') đều có S ⊆ S\': một trạm tới được từ 1 trên đồ thị thặng dư không thể nằm ở phía T\'. Vậy S là lát cắt có **ít trạm nhất**.'] },
        { table: { cols: [2600, 3000, 3018], head: ['Ống', 'Từ S = {1, 2} sang', 'Dung lượng'], rows: [['[2] 1 → 3', 'trạm 3', '8'], ['[3] 2 → 3', 'trạm 3', '2'], ['[4] 2 → 4', 'trạm 4', '5'], ['Tổng', '', '**15** = F']] } },
        { fig: 'f_duongong_opt', w: 2.8, cap: 'Sơ đồ khối của lời giải.' },
      ],
      optimal: [
        { file: 'DUONGONG', title: 'DUONGONG.CPP: Dinic + lát cắt từ đồ thị thặng dư' },
        { cx: 'O(n^2^ · m) trên lí thuyết; với n = 500, m = 5000 Dinic chạy rất nhanh.' },
      ],
      traps: ['**In các ống bão hòa.**', '**Lấy S theo phía của n** (được lát cắt có S lớn nhất).', '**Dùng int** cho luồng: F có thể tới 5000 · 10^9^.', '**Xét cả ống đi từ T vào S**: chúng không thuộc lát cắt.'],
      approaches: [['DUONGONG_1baohoa', 'In các ống bão hòa'], ['DUONGONG_2snhieunhat', 'S = phần không tới được n'], ['DUONGONG', 'S = phần tới được từ 1 trên đồ thị thặng dư']],
    },
    // ================================================================ 17.2
    {
      id: '17.2', key: 'Mỗi đường dung lượng 1, luồng cực đại; lần theo luồng và cắt bỏ vòng.',
      understand: [
        'Mỗi con đường chỉ dùng cho một lộ trình: đặt dung lượng 1. Số lộ trình không chung đường nhiều nhất bằng **luồng cực đại** từ 1 tới n (định lí Menger). Phần khó là **in ra** các lộ trình, mỗi lộ trình không đi qua một nút hai lần.',
        { fig: 'tap2:roinhau', w: 5.4, cap: 'Ví dụ: hai lộ trình không chung con đường nào.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Tìm lộ trình rồi xóa',
        body: [
          'Lặp: tìm một lộ trình ngắn nhất từ 1 tới n bằng BFS trên các con đường chưa dùng, ghi lại, đánh dấu các con đường của nó đã dùng.',
          { fig: 'f_roinhau_naive', w: 3.0, cap: 'Sơ đồ khối của cách tham lam.' },
          { file: 'ROINHAU_1thamlam', title: 'Cách ngây thơ: tìm lộ trình rồi xóa' },
          { cx: 'O(k · (n + m)).' },
        ],
      },
      stuck: [
        'Tham lam sai: một lộ trình chọn sớm có thể chiếm con đường mà hai lộ trình khác cần. Ví dụ đồ thị 1 → 2, 1 → 3, 2 → 3, 2 → 4, 3 → 4 (n = 4) có cả hai lộ trình 1 → 2 → 4 và 1 → 3 → 4; nếu lộ trình đầu tiên chọn 1 → 2 → 3 → 4 thì chỉ còn đường 1 → 3 và 2 → 4 không nối được với nhau. Kết quả: **{{S:ROINHAU_1thamlam}} điểm**.',
        'Dùng luồng là đúng hướng, nhưng nhiều bạn dựng mạng bằng **ma trận** hay **tập** các cặp (u, v), vô tình **gộp các đường song song** làm một cung dung lượng 1. Ba con đường song song từ 1 tới x chỉ còn cho một lộ trình: **{{S:ROINHAU_2gopsongsong}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Tham lam không biết "trả lại" con đường đã chọn. Cần cung ngược của luồng, giữ nguyên từng con đường song song; rồi cần biến luồng thành các lộ trình **đơn**.'] },
      ],
      breakthrough: [
        { ol: ['Mỗi con đường u → v là một cung dung lượng 1 (đường song song là các cung riêng). Chạy Dinic từ 1 tới n: k = luồng cực đại.', 'Con đường có luồng là con đường mà cung của nó đã hết dung lượng. Lưu out[u] = danh sách các con đường có luồng đi ra từ u.', 'Lặp k lần: đi từ 1, mỗi bước lấy con đường có luồng **tiếp theo chưa dùng** ở nút hiện tại (con trỏ ptr[u]), cho tới khi tới n. Bảo toàn luồng đảm bảo luôn đi tiếp được.', 'Nếu quay lại một nút đã có trên lộ trình hiện tại, **cắt bỏ** cả đoạn vòng (các con đường trong vòng vẫn bị coi là đã dùng, không sao vì ta chỉ cần lộ trình không chung đường).'] },
        { fig: 'f_roinhau_opt', w: 3.0, cap: 'Sơ đồ khối của lời giải.' },
        { box: 'note', title: 'VÌ SAO LUỒNG CÓ THỂ CÓ VÒNG?', body: ['Luồng cực đại không nhất thiết là "đẹp": thuật toán có thể đẩy một đơn vị luồng đi vòng quanh một chu trình (ví dụ 3 → 5 → 4 → 3 ở ví dụ) mà giá trị luồng không đổi. Khi lần theo luồng, gặp vòng đó thì phải cắt.'] },
      ],
      optimal: [
        { file: 'ROINHAU', title: 'ROINHAU.CPP: Dinic + lần theo luồng, cắt vòng' },
        { cx: 'O(m · √m) cho Dinic với dung lượng 1; lần theo luồng O(m).' },
      ],
      traps: ['**Tham lam tìm lộ trình rồi xóa.**', '**Gộp đường song song** thành một cung dung lượng 1 (mất lộ trình).', '**Không cắt vòng** khi lần theo luồng.', '**Dùng lại một con đường** ở hai lộ trình (quên con trỏ ptr).'],
      approaches: [['ROINHAU_1thamlam', 'Tìm lộ trình rồi xóa'], ['ROINHAU_2gopsongsong', 'Luồng, gộp đường song song'], ['ROINHAU', 'Luồng + lần theo, cắt vòng']],
    },
    // ================================================================ 17.3
    {
      id: '17.3', key: 'Mạng luồng s → học sinh (a~i~) → ngày (1) → t (b~j~); đủ luồng thì có lịch.',
      understand: [
        'Mỗi học sinh trực nhiều nhất a~i~ ngày, mỗi ngày cần đúng b~j~ bạn, mỗi bạn trực một ngày nhiều nhất một lần. Đây là bài toán **phân phối có giới hạn hai phía**, mô hình hóa bằng luồng.',
        { fig: 'tap2:trucnhat', w: 5.4, cap: 'Mạng luồng của ví dụ 1.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Tham lam theo từng ngày',
        body: [
          'Xếp lần lượt từng ngày; mỗi ngày ưu tiên những bạn còn nhiều lượt trực nhất.',
          { fig: 'f_trucnhat_naive', w: 3.0, cap: 'Sơ đồ khối của cách tham lam.' },
          { file: 'TRUCNHAT_2thamlam', title: 'Cách ngây thơ: tham lam theo từng ngày' },
          { cx: 'O(d · n log n).' },
        ],
      },
      stuck: [
        'Tham lam sai. Ví dụ: bạn 1 trực được ngày 1 và 2, bạn 2 chỉ trực được ngày 1, mỗi bạn trực 1 ngày, mỗi ngày cần 1 bạn. Ngày 1 tham lam có thể chọn bạn 1, đến ngày 2 không còn ai: in NO, trong khi xếp bạn 2 ngày 1, bạn 1 ngày 2 là được. Kết quả: **{{S:TRUCNHAT_2thamlam}} điểm**.',
        'Vét cạn (xếp từng ngày, thử mọi tổ hợp b~j~ bạn, quay lui) đúng nhưng hàm mũ: **{{S:TRUCNHAT_1vetcan}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Có ba loại giới hạn đan vào nhau (mỗi bạn, mỗi ngày, mỗi cặp bạn – ngày). Cần một mô hình xử lí cả ba cùng lúc và cho phép đổi ý.'] },
      ],
      breakthrough: [
        { table: { cols: [2600, 2600, 3418], head: ['Cung', 'Dung lượng', 'Ý nghĩa'], rows: [['s → học sinh i', 'a~i~', 'i trực nhiều nhất a~i~ ngày'], ['học sinh i → ngày j', '1', 'i trực được ngày j, nhiều nhất một lần'], ['ngày j → t', 'b~j~', 'ngày j cần b~j~ bạn']] } },
        'Một lịch trực hợp lệ tương ứng với một luồng có giá trị đúng bằng Σb~j~ (mọi cung vào t đầy), và ngược lại một luồng nguyên như vậy cho ra lịch trực: học sinh i trực ngày j khi cung i → j có luồng. Vậy: chạy luồng cực đại, nếu F < Σb~j~ thì in NO.',
        { table: { cols: [2400, 3000, 3218], head: ['Ví dụ 1', 'Luồng', 'Lịch'], rows: [['Ngày 1 (cần 2)', 'bạn 1, bạn 3', '1 3'], ['Ngày 2 (cần 1)', 'bạn 1', '1'], ['Ngày 3 (cần 2)', 'bạn 2, bạn 3', '2 3'], ['Tổng', 'F = 5 = Σb~j~', '**YES**']] } },
        'Ví dụ 2: không ai trực được ngày 2 nên cung "ngày 2 → t" không bao giờ có luồng, F < Σb~j~: **NO**.',
        { fig: 'f_trucnhat_opt', w: 3.0, cap: 'Sơ đồ khối của lời giải.' },
        { box: 'theorem', title: 'TÍNH NGUYÊN', body: ['Mọi dung lượng là số nguyên thì Dinic (cũng như Ford–Fulkerson) cho ra luồng cực đại **nguyên**: mỗi cung học sinh → ngày có luồng 0 hoặc 1, đọc ra được lịch trực.'] },
      ],
      optimal: [
        { file: 'TRUCNHAT', title: 'TRUCNHAT.CPP: luồng cực đại trên mạng ba tầng' },
        { cx: 'Mạng có n + d + 2 ≤ 402 đỉnh và tối đa n · d + n + d ≈ 4·10^4^ cung; Dinic chạy tức thì.' },
      ],
      traps: ['**Tham lam theo ngày.**', '**Đặt dung lượng học sinh → ngày bằng a~i~** (một bạn trực một ngày nhiều lần).', '**Kiểm tra F = Σa~i~** thay vì Σb~j~.', '**Quên in dòng trống** cho ngày có b~j~ = 0.'],
      approaches: [['TRUCNHAT_1vetcan', 'Vét cạn, quay lui theo ngày'], ['TRUCNHAT_2thamlam', 'Tham lam theo từng ngày'], ['TRUCNHAT', 'Luồng cực đại']],
    },
  ],
};
