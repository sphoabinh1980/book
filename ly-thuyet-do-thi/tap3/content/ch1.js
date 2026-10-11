// TẬP 3 — CHƯƠNG 1. LÀM QUEN VỚI ĐỒ THỊ
module.exports = {
  no: 1,
  intro: 'Các bài tập của chương 1 kiểm tra những kĩ năng nền tảng: đếm bậc, chọn cách biểu diễn đồ thị, duyệt đồ thị bằng DFS và BFS. Thuật toán không khó, nên điểm số thường bị mất ở những chỗ rất "đời thường": tràn số, tràn ngăn xếp, dữ liệu bị lặp, hoặc làm lại một việc nhiều lần trong khi chỉ cần làm một lần. Bảng dưới đây tóm tắt con đường từ cách ngây thơ tới lời giải mẫu của từng bài.',
  solutions: [
    // ================================================================ 1.1
    {
      id: '1.1', key: 'Định lí bắt tay + điều kiện "người nhiều nhất".',
      understand: [
        'Mỗi bạn là một **đỉnh**, mỗi lần bắt tay là một **cạnh** nối hai đỉnh khác nhau; vì hai bạn được bắt tay nhiều lần nên đồ thị có thể có **cạnh lặp**, nhưng không có **khuyên**. Câu hỏi trở thành: dãy d~1~, ..., d~n~ có phải là **dãy bậc** của một đa đồ thị không khuyên hay không, và nếu có thì đồ thị ấy có bao nhiêu cạnh.',
        'Theo định lí bắt tay, nếu tồn tại thì số cạnh **bắt buộc** bằng (d~1~ + ... + d~n~) / 2, nên phần khó duy nhất là quyết định "có tồn tại hay không".',
        { fig: 'tap2:battay', w: 5.8, cap: 'Ví dụ 1 có một cách bắt tay hợp lệ; ví dụ 3 thì bạn 1 "thiếu người" để bắt tay.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Mô phỏng từng cái bắt tay',
        body: [
          'Nếu chưa nghĩ ra điều kiện, ta có thể **thử xây** đồ thị: chừng nào còn ít nhất hai bạn chưa đủ số lần bắt tay, cho **hai bạn còn thiếu nhiều nhất** bắt tay nhau. Nếu cuối cùng còn sót đúng một bạn chưa đủ thì không thể xếp được. (Chọn hai bạn thiếu nhiều nhất là quan trọng: nếu chọn tùy tiện, ta có thể để lại một bạn thiếu rất nhiều mà không còn ai bắt tay cùng.)',
          { fig: 'f_battay_naive', w: 3.4, cap: 'Sơ đồ khối của cách mô phỏng.' },
          { file: 'BATTAY_1mophong', title: 'Cách ngây thơ: mô phỏng bằng hàng đợi ưu tiên' },
          'Chạy tay ví dụ 1 (d = 3 2 2 1 2): lần lượt bắt tay các cặp (1, 2), (1, 3), (5, 1), (2, 3), (4, 5); sau 5 bước mọi bạn đều đủ: in **5**.',
          { cx: 'mỗi vòng lặp tạo đúng một cái bắt tay, nên có S/2 vòng, mỗi vòng O(log n). Tổng O(S log n) với S = d~1~ + ... + d~n~.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1, 2** (d~i~ ≤ 100, n ≤ 100): S ≤ 10^4^, chạy tức thì.', '**Subtask 3** (d~i~ ≤ 10^9^, n ≤ 10^5^): S tới 10^14^, mô phỏng không bao giờ xong.'] },
        'Cách mô phỏng được **{{S:BATTAY_1mophong}} điểm**. Hai cách "rút gọn" hay gặp cũng chỉ được điểm một phần:',
        { ul: ['**Chỉ kiểm tra tổng chẵn** (đúng định lí bắt tay nhưng quên điều kiện thứ hai): sai ở ví dụ 3, được **{{S:BATTAY_2tongchan}} điểm** (chỉ Subtask 1, nơi đề bài đảm bảo điều kiện thứ hai luôn đúng).', '**Đủ hai điều kiện nhưng cộng bằng `int`**: tổng 10^14^ bị tràn số, được **{{S:BATTAY_3int}} điểm**.'] },
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Mô phỏng làm **từng cái bắt tay một**, trong khi câu hỏi chỉ cần biết **có** làm được hay không. Ta cần một điều kiện kiểm tra được bằng một lần duyệt dãy.'] },
      ],
      breakthrough: [
        'Gọi S là tổng và M là số lớn nhất trong dãy. Hai điều kiện **cần** rất tự nhiên:',
        { ol: ['**S chẵn** (định lí bắt tay: tổng bậc bằng 2 lần số cạnh).', '**M ≤ S − M**: mỗi cái bắt tay của bạn "nhiều nhất" cần một bạn **khác**, và tổng số lần bắt tay của những bạn khác là S − M.'] },
        { box: 'theorem', title: 'VÌ SAO HAI ĐIỀU KIỆN LÀ ĐỦ?', body: [
          'Quy nạp theo S. Nếu S = 0 thì không cần bắt tay. Nếu S > 0, cho hai bạn có số lớn nhất M ≥ M~2~ bắt tay một lần (M~2~ > 0 vì M ≤ S − M). Dãy mới có tổng S − 2, vẫn chẵn; chỉ cần kiểm tra điều kiện 2 cho số lớn nhất mới M\'.',
          { ul: ['Nếu M\' = M − 1: điều kiện M − 1 ≤ (S − 2) − (M − 1) tương đương 2M ≤ S, đúng theo giả thiết.', 'Nếu không, M\' = M là một số chưa bị giảm, tức dãy có ít nhất **ba** số bằng M, nên S ≥ 3M. Cần 2M + 2 ≤ S: đúng khi M ≥ 2; khi M = 1 thì S ≥ 3 và S chẵn nên S ≥ 4 = 2M + 2.'] },
          'Vậy dãy mới vẫn thỏa hai điều kiện, theo quy nạp xếp được. Chính thuật toán mô phỏng ở mục 2 là cách xây dựng theo lập luận này'] },
        'Chạy tay ba ví dụ:',
        { table: { cols: [1900, 1300, 1300, 2000, 2118], head: ['Dãy d', 'S', 'M', 'S chẵn? M ≤ S − M?', 'Đáp số'],
          rows: [['3 2 2 1 2', '10', '3', 'Đúng; 3 ≤ 7', '**5**'], ['3 3 1 2', '9', '3', 'Sai', '**−1**'], ['6 1 1', '8', '6', 'Đúng; 6 > 2', '**−1**']], aligns: [0, 'center', 'center', 'center', 'center'].map((a) => a === 'center' ? 'center' : 'left') } },
      ],
      optimal: [
        { fig: 'f_battay_opt', w: 2.8, cap: 'Sơ đồ khối của lời giải mẫu.' },
        { file: 'BATTAY', title: 'BATTAY.CPP: kiểm tra hai điều kiện, O(n)' },
        { cx: 'một lần duyệt dãy: O(n) thời gian, O(1) bộ nhớ.' },
      ],
      traps: ['**Tràn số:** S có thể tới 10^5^ · 10^9^ = 10^14^; cả S lẫn M phải là `long long`.', '**Quên điều kiện M ≤ S − M:** tổng chẵn là chưa đủ (ví dụ 3).', '**n = 1:** dãy một số d~1~ chỉ hợp lệ khi d~1~ = 0; công thức M ≤ S − M tự xử lí đúng trường hợp này.'],
      approaches: [['BATTAY_1mophong', 'Mô phỏng từng cái bắt tay'], ['BATTAY_2tongchan', 'Chỉ kiểm tra tổng chẵn'], ['BATTAY_3int', 'Đủ hai điều kiện, dùng int'], ['BATTAY', 'Đủ hai điều kiện, long long']],
    },
    // ================================================================ 1.2
    {
      id: '1.2', key: 'Bán bậc vào/ra sau khi bỏ cung lặp.',
      understand: [
        'Mỗi tài khoản là một đỉnh, quan hệ "u theo dõi v" là một **cung** u → v. Người nổi tiếng là đỉnh c có **bán bậc vào** bằng n − 1 (mọi đỉnh khác đều có cung tới c) và **bán bậc ra** bằng 0. Chi tiết làm bài khác bài "đếm bậc" thông thường: **một cung có thể xuất hiện nhiều lần** trong dữ liệu.',
        { fig: 'tap2:noitieng', w: 3.8, cap: 'Ví dụ 1: dòng "2 3" bị ghi hai lần nhưng chỉ là một cung.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Thử từng người, đếm lại trên toàn bộ dữ liệu',
        body: [
          'Với mỗi người v, duyệt lại cả m dòng dữ liệu để đếm số người theo dõi v và số người v theo dõi.',
          { fig: 'f_noitieng_naive', w: 3.2, cap: 'Sơ đồ khối của cách thử từng người.' },
          { file: 'NOITIENG_1ngaytho', title: 'Cách ngây thơ: O(n · m)' },
          { cx: 'n lần duyệt m dòng: O(n · m). Với n = m = 2·10^5^ là 4·10^10^ phép tính.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n ≤ 1000): n · m ≤ 2·10^8^ phép so sánh đơn giản, chạy kịp: **{{P:NOITIENG_1ngaytho:1}} điểm**.', '**Subtask 2, 3**: quá thời gian.'] },
        'Tổng cộng **{{S:NOITIENG_1ngaytho}} điểm**. Cách sửa tự nhiên là đếm bậc **một lần** cho mọi đỉnh (như Bài 1 của Tập 1): mỗi dòng u v cộng 1 vào ra[u] và vào[v]. Cách này đúng với Subtask 2 nhưng **sai** khi có dòng lặp: ở ví dụ 1, vào[3] = 4 ≠ n − 1. Được **{{S:NOITIENG_2khongloaitrung}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Đếm bậc theo từng dòng dữ liệu là đếm **số dòng**, không phải đếm **số cung khác nhau**. Phải biến danh sách dòng thành danh sách cung trước khi đếm.'] },
      ],
      breakthrough: [
        'Hai dòng giống nhau là hai cặp (u, v) bằng nhau. Sau khi **sắp xếp** danh sách cặp, các cặp bằng nhau đứng liền nhau; hàm `unique` giữ lại mỗi cặp một lần. Khi đó đếm bậc như bình thường.',
        { table: { cols: [2400, 3000, 3218], head: ['Bước', 'Danh sách cặp (u, v)', 'Ghi chú'], rows: [
          ['Dữ liệu vào', '(1,3) (2,3) (4,3) (1,2) (4,1) (2,3)', '6 dòng'], ['Sau khi sắp xếp', '(1,2) (1,3) (2,3) (2,3) (4,1) (4,3)', 'hai cặp (2,3) đứng cạnh nhau'],
          ['Sau `unique`', '(1,2) (1,3) (2,3) (4,1) (4,3)', '5 cung khác nhau'], ['Đếm bậc', 'vào[3] = 3 = n − 1, ra[3] = 0', 'đáp số **3**']] } },
        { box: 'theorem', title: 'VÌ SAO CÓ NHIỀU NHẤT MỘT NGƯỜI NỔI TIẾNG?', body: ['Giả sử a và b đều nổi tiếng. Vì a nổi tiếng nên b phải theo dõi a, nhưng b nổi tiếng thì không theo dõi ai: mâu thuẫn. Vì vậy chỉ cần duyệt v và in đỉnh thỏa mãn (nếu có).'] },
      ],
      optimal: [
        { file: 'NOITIENG', title: 'NOITIENG.CPP: bỏ cung lặp rồi đếm bán bậc, O(m log m)' },
        { cx: 'sắp xếp O(m log m), đếm O(n + m).' },
        { box: 'def', title: 'MỞ RỘNG: BÀI TOÁN NGƯỜI NỔI TIẾNG KINH ĐIỂN', body: ['Nếu thay vì danh sách cung, ta chỉ được **hỏi** "a có theo dõi b không?", thì vẫn tìm được người nổi tiếng với chỉ khoảng 3n câu hỏi: giữ một ứng viên c; với mỗi người i, nếu c theo dõi i thì c không thể nổi tiếng, đổi c = i. Cuối cùng kiểm tra lại ứng viên duy nhất.'] },
      ],
      traps: ['**Quên dòng lặp:** lỗi phổ biến nhất của bài, mất trọn Subtask 3.', '**Dùng ma trận kề** để khử lặp: n = 2·10^5^ thì ma trận có 4·10^10^ ô, không đủ bộ nhớ.', '**Quên điều kiện bán bậc ra bằng 0**: một người được mọi người theo dõi nhưng lại theo dõi người khác thì không nổi tiếng.'],
      approaches: [['NOITIENG_1ngaytho', 'Thử từng người, duyệt lại m dòng'], ['NOITIENG_2khongloaitrung', 'Đếm bậc, không bỏ dòng lặp'], ['NOITIENG', 'Bỏ cung lặp rồi đếm bậc']],
    },
    // ================================================================ 1.3
    {
      id: '1.3', key: 'Hướng cạnh từ đỉnh bậc nhỏ sang bậc lớn: O(m√m).',
      understand: [
        'Ta cần đếm số **chu trình độ dài 3** (tam giác) trong một đơn đồ thị vô hướng tới 10^5^ đỉnh và 2·10^5^ cạnh. Mỗi tam giác {x, y, z} có ba cạnh, ba đỉnh; cách đếm nào cũng phải cẩn thận để mỗi tam giác chỉ được tính **một lần**.',
        { fig: 'tap2:tamgiac', w: 5.6, cap: 'Hai ví dụ của đề.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Thử mọi bộ ba đỉnh',
        body: [
          'Lưu ma trận kề a và thử mọi bộ ba x < y < z.',
          { fig: 'f_tamgiac_naive', w: 2.9, cap: 'Sơ đồ khối của cách thử mọi bộ ba.' },
          { file: 'TAMGIAC_1bavonglap', title: 'Cách ngây thơ: ba vòng lặp' },
          { cx: 'trên giấy là O(n^3^). Thực tế điều kiện `a[x][y]` được kiểm tra trước nên vòng z chỉ thật sự chạy khi (x, y) là cạnh: O(n · m). Bộ nhớ O(n^2^).' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n ≤ 100) và **Subtask 2** (n ≤ 2000): chạy kịp, **{{S:TAMGIAC_1bavonglap}} điểm**.', '**Subtask 3** (n ≤ 10^5^): ma trận 10^10^ ô không thể khai báo.'] },
        'Hai cải tiến "nửa vời" dễ nghĩ tới đều dừng ở cùng mức điểm:',
        { ul: ['**Ma trận `bitset`, đếm theo cạnh:** với mỗi cạnh (u, v), số tam giác chứa nó là `(a[u] & a[v]).count()`; cộng lại rồi chia 3. Rất nhanh, nhưng vẫn cần ma trận n × n: **{{S:TAMGIAC_2bitset}} điểm**.',
          '**Danh sách kề, đếm theo cạnh:** với mỗi cạnh (u, v), đánh dấu các bạn của u rồi duyệt các bạn của v. Không cần ma trận, nhưng chi phí là Σ (deg u + deg v) trên mọi cạnh = Σ deg(v)^2^. Một "ngôi sao" có 10^5^ cạnh làm con số này lên 10^10^: **{{S:TAMGIAC_3theocanh}} điểm**.'] },
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Các đỉnh có bậc rất lớn bị duyệt lại rất nhiều lần (mỗi cạnh chạm vào chúng lại duyệt toàn bộ danh sách kề của chúng). Cần một cách đếm mà mỗi đỉnh chỉ phải "mở rộng" các hàng xóm ít ỏi của mình.'] },
      ],
      breakthrough: [
        'Đặt một thứ tự toàn phần trên các đỉnh: u **thấp hơn** v nếu deg(u) < deg(v), hoặc bậc bằng nhau và u < v. **Hướng** mỗi cạnh từ đầu thấp sang đầu cao. Mỗi tam giác có đúng một đỉnh thấp nhất u, đỉnh giữa v và đỉnh cao nhất w, nên nó xuất hiện **đúng một lần** dưới dạng u → v → w cùng với u → w.',
        { box: 'theorem', title: 'VÌ SAO MỖI ĐỈNH CHỈ CÓ ÍT CUNG ĐI RA?', body: ['Giả sử u có k cung đi ra. Các đỉnh đích đều "cao hơn" u nên có bậc ít nhất deg(u) ≥ k. Vậy có k đỉnh bậc ≥ k, tổng bậc ít nhất k^2^ ≤ 2m, suy ra k ≤ √(2m) ≈ 632. Mỗi cạnh u → v chỉ phải duyệt các cung ra của v (không quá √(2m)), nên tổng chi phí là O(m√m) ≈ 1,3·10^8^ phép tính đơn giản trong trường hợp xấu nhất.'] },
        'Chạy tay ví dụ 1. Bậc: deg(1) = 2, deg(2) = 3, deg(3) = 4, deg(4) = 4, deg(5) = 3, deg(6) = 2.',
        { table: { cols: [1100, 2600, 4918], head: ['Đỉnh u', 'Cung đi ra (u → v)', 'Tam giác tìm được (u → v → w và u → w)'], rows: [
          ['1', '1 → 2, 1 → 3', '1 → 2 → 3: **{1, 2, 3}**'], ['2', '2 → 3, 2 → 4', '2 → 3 → 4: **{2, 3, 4}**'], ['3', '3 → 4', '(không có)'], ['4', '(không có)', '(không có)'],
          ['5', '5 → 3, 5 → 4', '5 → 3 → 4: **{3, 4, 5}**'], ['6', '6 → 4, 6 → 5', '6 → 5 → 4: **{4, 5, 6}**']] } },
        'Đếm được 4 tam giác, mỗi tam giác đúng một lần.',
      ],
      optimal: [
        { fig: 'f_tamgiac_opt', w: 3.0, cap: 'Sơ đồ khối của lời giải mẫu.' },
        { file: 'TAMGIAC', title: 'TAMGIAC.CPP: định hướng cạnh theo bậc, O(m√m)' },
        { cx: 'O(m√m) thời gian, O(n + m) bộ nhớ. Mảng `mark[w] = u` thay cho việc xóa dấu sau mỗi đỉnh.' },
      ],
      traps: ['**Đếm ba lần mỗi tam giác** rồi quên chia 3 (ở các cách đếm theo cạnh).', '**So sánh chỉ theo bậc** mà không phá hòa bằng số hiệu: hai đỉnh cùng bậc sẽ không có thứ tự, cạnh giữa chúng bị hướng cả hai chiều hoặc không chiều nào.', '**Khai báo ma trận kề cho n = 10^5^:** 10^10^ byte, chương trình không chạy được.'],
      approaches: [['TAMGIAC_1bavonglap', 'Ba vòng lặp trên ma trận kề'], ['TAMGIAC_2bitset', 'Ma trận bitset, đếm theo cạnh'], ['TAMGIAC_3theocanh', 'Danh sách kề, đếm theo cạnh'], ['TAMGIAC', 'Định hướng cạnh theo bậc']],
    },
    // ================================================================ 2.1
    {
      id: '2.1', key: 'Duyệt ma trận đúng thứ tự, chỉ lấy i < j.',
      understand: [
        'Bài luyện chuyển đổi giữa ba cách biểu diễn của Tập 1, Bài 2. Ma trận kề đối xứng, nên mỗi cạnh (u, v) xuất hiện **hai lần**: ở ô (u, v) và ô (v, u). Danh sách cạnh chỉ được in mỗi cạnh một lần, còn danh sách kề của u thì phải có v và danh sách kề của v phải có u.',
        { fig: 'tap2:chuyendoi', w: 5.6, cap: 'Ba cách biểu diễn cùng một đồ thị.' },
      ],
      naive: {
        title: 'Cách ngây thơ: In mọi ô bằng 1 thành một cạnh',
        body: [
          'Cách viết vội vàng nhất là gặp ô bằng 1 nào thì thêm cạnh đó vào danh sách cạnh. Danh sách kề thì đúng, nhưng danh sách cạnh bị gấp đôi.',
          { file: 'CHUYENDOI_1haichieu', title: 'Cách sai: thiếu điều kiện i < j' },
          'Với ví dụ, chương trình in "8" ở dòng đầu thay vì "4", kèm cả (2, 1), (3, 1), ... Mọi test có ít nhất một cạnh đều sai: **{{S:CHUYENDOI_1haichieu}} điểm**.',
        ],
      },
      stuck: [
        'Ngoài lỗi đếm đôi, có hai nỗi lo khác: phải **sắp xếp** danh sách cạnh và các danh sách kề hay không, và đọc 10^6^ số có kịp không.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Ma trận đối xứng: thông tin của nửa trên đường chéo đã đủ để dựng danh sách cạnh. Câu hỏi là làm sao để kết quả **tự** đúng thứ tự mà không phải sắp xếp.'] },
      ],
      breakthrough: [
        'Ta đọc ma trận **theo thứ tự hàng**: i = 1..n, trong mỗi hàng j = 1..n. Hai quan sát:',
        { ol: ['Các cạnh (i, j) với i < j được gặp theo đúng thứ tự "tăng dần theo i, cùng i thì tăng dần theo j" mà đề yêu cầu.', 'Trong hàng i, các j được gặp theo thứ tự tăng dần, nên đẩy j vào g[i] ngay khi gặp thì g[i] tự được sắp xếp.'] },
        'Vậy chỉ cần một lần đọc, thêm điều kiện i < j cho danh sách cạnh. Đọc 10^6^ số bằng `scanf` mất khoảng 0,1 – 0,2 giây.',
        { fig: 'f_chuyendoi', w: 3.2, cap: 'Sơ đồ khối của lời giải mẫu.' },
      ],
      optimal: [
        { file: 'CHUYENDOI', title: 'CHUYENDOI.CPP: một lần đọc ma trận, O(n²)' },
        { cx: 'O(n^2^) để đọc ma trận (không thể ít hơn vì phải đọc hết dữ liệu), bộ nhớ O(n + m).' },
      ],
      traps: ['**Đếm đôi cạnh** khi quên điều kiện i < j.', '**Lưu cả ma trận** vào mảng `int a[1000][1000]` vẫn được (4 MB), nhưng không cần thiết.', '**In dòng trống sai:** đỉnh cô lập vẫn phải có một dòng "0".'],
      approaches: [['CHUYENDOI_1haichieu', 'In mọi ô bằng 1 thành cạnh'], ['CHUYENDOI', 'Duyệt theo hàng, lấy i < j']],
    },
    // ================================================================ 2.2
    {
      id: '2.2', key: 'Duyệt danh sách ngắn hơn + ghi nhớ cặp đã hỏi.',
      understand: [
        'Số bạn chung của u và v là |N(u) ∩ N(v)|, kích thước giao của hai danh sách kề. Bài kiểm tra việc chọn cách biểu diễn: ma trận kề trả lời "w có kề u không" trong O(1) nhưng tốn O(n) cho mỗi câu hỏi và O(n^2^) bộ nhớ; danh sách kề thì gọn nhưng phải tính giao.',
        { fig: 'tap2:banchung', w: 5.0, cap: 'Lượt xem (1, 5): giao của {2, 3, 4} và {2, 3, 4, 6}.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Ma trận kề, duyệt mọi w',
        body: [
          { fig: 'f_banchung_naive', w: 3.0, cap: 'Sơ đồ khối của cách dùng ma trận kề.' },
          { file: 'BANCHUNG_1matran', title: 'Cách ngây thơ: ma trận kề, O(n) mỗi câu hỏi' },
          { cx: 'O(n^2^) bộ nhớ, O(n · q) thời gian. Với n = 500: 5·10^7^ phép tính.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n ≤ 500): chạy tốt: **{{S:BANCHUNG_1matran}} điểm**.', '**Subtask 2, 3** (n tới 10^5^): ma trận quá lớn.'] },
        'Chuyển sang danh sách kề **đã sắp xếp**: với câu hỏi (u, v), duyệt danh sách **ngắn hơn** và tìm nhị phân trong danh sách dài hơn. Mỗi câu hỏi tốn O(min(deg u, deg v) · log n). Khi mọi bậc ≤ 300 (Subtask 2), mỗi câu hỏi tốn vài nghìn phép tính: chạy kịp. Nhưng Subtask 3 có hai "người nổi tiếng" cùng 5·10^4^ bạn và 10^5^ câu hỏi đều hỏi cặp này: 5·10^9^ phép tính. Cách này được **{{S:BANCHUNG_2nhiphan}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Cùng một cặp (u, v) được hỏi lại hàng vạn lần, và lần nào chương trình cũng tính lại từ đầu.'] },
      ],
      breakthrough: [
        '**Ghi nhớ** đáp số của mỗi cặp đã tính (dùng `map` với khóa là cặp đã chuẩn hóa: u là đỉnh có danh sách ngắn hơn). Vấn đề còn lại: có thể có nhiều cặp **khác nhau** cùng tốn kém không?',
        { box: 'theorem', title: 'ĐÁNH GIÁ: TỔNG CHI PHÍ TRÊN CÁC CẶP KHÁC NHAU', body: [
          'Chọn ngưỡng B = √q. Đỉnh **lớn** là đỉnh có bậc > m/B; có không quá 2m/(m/B) = 2B đỉnh lớn.',
          { ul: ['Cặp có ít nhất một đỉnh nhỏ: chi phí ≤ bậc của đỉnh nhỏ ≤ m/B; có ≤ q cặp: tổng ≤ q · m/B = m√q.', 'Cặp gồm hai đỉnh lớn: mỗi đỉnh lớn u ghép với nhiều nhất 2B đỉnh lớn khác, chi phí mỗi lần ≤ deg(u); tổng ≤ Σ deg(u) · 2B ≤ 2m · 2B = 4m√q.'] },
          'Vậy tổng chi phí là O(m√q · log n), khoảng 3·10^7^ · 17 phép tính trong trường hợp xấu nhất: chạy kịp.'] },
      ],
      optimal: [
        { file: 'BANCHUNG', title: 'BANCHUNG.CPP: danh sách ngắn hơn, tìm nhị phân, ghi nhớ cặp' },
        { cx: 'O((m + q) log n + m√q log n) thời gian, O(n + m + q) bộ nhớ.' },
      ],
      traps: ['**Chuẩn hóa khóa của `map`:** (u, v) và (v, u) là cùng một câu hỏi; nếu không chuẩn hóa, kẻ ra đề có thể hỏi xen kẽ hai chiều để làm ghi nhớ mất tác dụng một nửa.', '**Quên sắp xếp danh sách kề** trước khi dùng `binary_search`.', '**Dùng ma trận** cho n = 10^5^.'],
      approaches: [['BANCHUNG_1matran', 'Ma trận kề, duyệt mọi w'], ['BANCHUNG_2nhiphan', 'Danh sách ngắn hơn + tìm nhị phân'], ['BANCHUNG', 'Như trên + ghi nhớ cặp đã hỏi']],
    },
    // ================================================================ 2.3
    {
      id: '2.3', key: 'Mỗi sự kiện chỉ ảnh hưởng tới 5 ô.',
      understand: [
        'Lưới R × C là một đồ thị không cần dựng: ô (x, y) kề với tối đa 4 ô (x ± 1, y), (x, y ± 1). Một ô trống là **khả nghi** khi số ô trống kề với nó bằng đúng k. Sau mỗi sự kiện, một ô đổi trạng thái và ta cần số ô khả nghi.',
        { fig: 'tap2:bando', w: 5.8, cap: 'Ví dụ: số trong ô trống là số ô trống kề nó; ô vàng là ô khả nghi (k = 2).' },
      ],
      naive: {
        title: 'Cách ngây thơ: Đếm lại toàn bộ sau mỗi sự kiện',
        body: [
          { fig: 'f_bando_naive', w: 2.9, cap: 'Sơ đồ khối của cách đếm lại.' },
          { file: 'BANDO_1demlai', title: 'Cách ngây thơ: O(R · C) mỗi sự kiện' },
          { cx: 'O(R · C · (q + 1)). Với R = C = 1000, q = 2·10^5^ là 2·10^11^ phép tính.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (q = 0) và **Subtask 2** (lưới 100 × 100, q ≤ 100): chạy tức thì.', '**Subtask 3**: không thể chạy xong.'] },
        'Được **{{S:BANDO_1demlai}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Mỗi sự kiện chỉ thay đổi **một** ô, vậy mà ta đếm lại cả triệu ô.'] },
      ],
      breakthrough: [
        'Ô (x, y) đổi trạng thái thì những giá trị nào có thể thay đổi?',
        { ul: ['Trạng thái của chính ô (x, y) (trống hay đá), và số ô trống kề nó **không đổi** (vì các ô kề không đổi), nhưng nó có thể trở thành / thôi là ô khả nghi.', 'Số ô trống kề của **bốn ô kề** (x, y) thay đổi đúng 1.', 'Mọi ô khác: không có gì thay đổi.'] },
        'Vì vậy chỉ cần xét 5 ô: **trừ** đóng góp cũ của 5 ô (ô nào đang khả nghi thì trừ 1), đổi trạng thái, rồi **cộng** đóng góp mới của 5 ô. Kĩ thuật "trừ cũ – cộng mới" này rất hay dùng khi dữ liệu thay đổi cục bộ.',
        { table: { cols: [2600, 3000, 3018], head: ['Sự kiện', '5 ô bị ảnh hưởng', 'Thay đổi'], rows: [
          ['Đào ô (1, 3)', '(1, 3), (1, 2), (1, 4), (2, 3)', 'trước: chỉ (1, 2) khả nghi, trừ 1; sau: (1, 4) có 2 kề trống, cộng 1; vẫn **6**'],
          ['Lấp ô (2, 2)', '(2, 2), (1, 2), (3, 2), (2, 1), (2, 3)', 'trước: (2, 1), (3, 2) khả nghi, trừ 2; sau: (1, 2) giảm còn 2 kề trống, cộng 1; 6 − 2 + 1 = **5**']] } },
      ],
      optimal: [
        { file: 'BANDO', title: 'BANDO.CPP: trừ cũ – cộng mới trên 5 ô, O(1) mỗi sự kiện' },
        { cx: 'O(R · C + q) thời gian, O(R · C) bộ nhớ.' },
      ],
      traps: ['**Quên chính ô (x, y)** trong 5 ô cần cập nhật.', '**Ra ngoài lưới** khi xét ô kề của ô ở biên.', '**Cập nhật trước khi trừ:** phải trừ đóng góp **cũ** trước khi đổi trạng thái, rồi mới cộng đóng góp mới.'],
      approaches: [['BANDO_1demlai', 'Đếm lại toàn bộ sau mỗi sự kiện'], ['BANDO', 'Trừ cũ – cộng mới trên 5 ô']],
    },
    // ================================================================ 3.1
    {
      id: '3.1', key: 'Loang bằng ngăn xếp tự quản lí.',
      understand: [
        'Mỗi ô đất là một đỉnh, hai ô đất chung cạnh được nối bằng một cạnh. Hòn đảo là **thành phần liên thông**, diện tích là số đỉnh của thành phần. Thuật toán là "loang" (DFS hoặc BFS) quen thuộc; chỗ khó duy nhất là kích thước: lưới 1000 × 1000 có thể là **một** hòn đảo 10^6^ ô.',
        { fig: 'tap2:demdao', w: 4.2, cap: 'Bốn hòn đảo của ví dụ.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Loang bằng DFS đệ quy',
        body: [
          { fig: 'f_demdao_naive', w: 3.3, cap: 'Sơ đồ khối của hàm loang đệ quy.' },
          { file: 'DEMDAO_1dequy', title: 'Cách ngây thơ: DFS đệ quy' },
          { cx: 'O(R · C) thời gian, nhưng độ sâu đệ quy có thể tới R · C = 10^6^.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (R, C ≤ 50): độ sâu ≤ 2500, chạy tốt.', '**Subtask 2**: một hòn đảo phủ kín bảng 1000 × 1000 (hoặc hình "con rắn" dài) làm đệ quy sâu 10^6^ tầng. Mỗi tầng tốn vài chục byte ngăn xếp, vượt giới hạn 8 MB: chương trình bị dừng với lỗi **Runtime Error**.'] },
        'Được **{{S:DEMDAO_1dequy}} điểm**, dù thuật toán hoàn toàn đúng.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Ngăn xếp của chương trình (stack) nhỏ hơn nhiều so với bộ nhớ chung (heap): thường chỉ 1 – 8 MB. Đệ quy sâu hàng triệu tầng là cách chắc chắn nhất để mất điểm.'] },
      ],
      breakthrough: [
        'Thay ngăn xếp của hệ thống bằng một `vector` **tự quản lí** (nằm trên heap, giới hạn bởi 256 MB): đẩy ô xuất phát vào, rồi lặp "lấy một ô ra, đẩy các ô đất kề chưa thăm vào".',
        { box: 'theorem', title: 'ĐÁNH DẤU KHI ĐẨY, KHÔNG PHẢI KHI LẤY', body: ['Nếu chỉ đánh dấu khi lấy ô ra, một ô có thể bị đẩy vào ngăn xếp nhiều lần (bởi nhiều ô kề) và được đếm vào diện tích nhiều lần. Đánh dấu **ngay khi đẩy** đảm bảo mỗi ô vào ngăn xếp đúng một lần, kích thước ngăn xếp không quá R · C.'] },
        { fig: 'f_demdao_opt', w: 3.0, cap: 'Sơ đồ khối của bước loang không đệ quy.' },
      ],
      optimal: [
        { file: 'DEMDAO', title: 'DEMDAO.CPP: loang bằng ngăn xếp tự quản lí, O(R · C)' },
        { cx: 'O(R · C) thời gian và bộ nhớ. Dùng `queue` thay `vector` (BFS) cũng được.' },
      ],
      traps: ['**DFS đệ quy** trên lưới lớn: tràn ngăn xếp.', '**Đánh dấu muộn:** đếm trùng diện tích, ngăn xếp phình to.', '**Coi hai ô chung góc là kề nhau:** đề chỉ cho phép 4 hướng.'],
      approaches: [['DEMDAO_1dequy', 'DFS đệ quy'], ['DEMDAO', 'Loang bằng ngăn xếp tự quản lí']],
    },
    // ================================================================ 3.2
    {
      id: '3.2', key: 'Đáp số = (m − (n − k)) + (k − 1).',
      link: 'Bài 9',
      understand: [
        'Ta được xóa cạnh hoặc thêm cạnh, cần biến đồ thị (có thể có khuyên, cạnh lặp) thành một cây với ít thao tác nhất. Một cây có hai tính chất: **liên thông** và có **đúng n − 1 cạnh**. Đáp số phụ thuộc vào hai đại lượng: số cạnh m và số thành phần liên thông k.',
        { fig: 'tap2:caykhong', w: 6.0, cap: 'Ba bộ dữ liệu của ví dụ.' },
      ],
      naive: {
        title: 'Cách ngây thơ: Chỉ sửa số cạnh cho bằng n − 1',
        body: [
          'Một lời giải "trông như đúng": cây có n − 1 cạnh, vậy cần |m − (n − 1)| thao tác thêm hoặc bớt.',
          { file: 'CAYKHONG_1chiemcanh', title: 'Cách sai: chỉ quan tâm số cạnh' },
          'Ở bộ 2 của ví dụ: m = 4 = n − 1 nên chương trình in 0, nhưng đồ thị gồm một tam giác và một cạnh rời, không phải cây.',
        ],
      },
      stuck: [
        'Khi đồ thị liên thông và không có khuyên, cạnh lặp (Subtask 1), mỗi cạnh thừa đều nằm trên chu trình và xóa nó không làm mất liên thông, nên công thức |m − (n − 1)| = m − n + 1 lại đúng: **{{S:CAYKHONG_1chiemcanh}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Số cạnh đúng chưa đủ: các cạnh phải "rải" đều để nối mọi đỉnh. Cần đếm số thành phần liên thông, và chứng minh được một cận dưới chặt.'] },
      ],
      breakthrough: [
        'Gọi k là số thành phần liên thông, a là số lần thêm và r là số lần xóa.',
        { ol: ['**Cận dưới cho a:** xóa cạnh không bao giờ làm giảm k; mỗi lần thêm cạnh giảm k nhiều nhất 1. Cuối cùng k = 1, nên **a ≥ k − 1**.', '**Cận dưới cho r:** số cạnh cuối cùng m − r + a = n − 1, nên r = m − n + 1 + a ≥ **m − n + k**.', '**Đạt được:** trong mỗi thành phần giữ lại một cây khung và xóa các cạnh còn lại: đúng m − (n − k) lần xóa (khuyên và cạnh lặp nằm trong số này). Sau đó nối k cây bằng k − 1 cạnh.'] },
        'Vậy đáp số là **(m − (n − k)) + (k − 1) = m − n + 2k − 1**.',
        { table: { cols: [1600, 1200, 1200, 1200, 3418], head: ['Bộ', 'n', 'm', 'k', 'm − n + 2k − 1'], rows: [['1', '4', '3', '1', '3 − 4 + 2 − 1 = **0**'], ['2', '5', '4', '2', '4 − 5 + 4 − 1 = **2**'], ['3', '3', '3', '2', '3 − 3 + 4 − 1 = **3**']] } },
        'Đếm k bằng DSU (Tập 1, Bài 9): mỗi lần gộp thành công hai nhóm, k giảm 1. Khuyên (u, u) và cạnh lặp tự động bị bỏ qua vì hai đầu đã cùng nhóm.',
        { fig: 'f_caykhong_opt', w: 3.0, cap: 'Sơ đồ khối xử lí một bộ dữ liệu.' },
      ],
      optimal: [
        { file: 'CAYKHONG', title: 'CAYKHONG.CPP: DSU đếm số thành phần' },
        { cx: 'O((n + m) · α(n)) cho mỗi bộ dữ liệu; tổng trên cả tệp O(Σn + Σm).' },
      ],
      traps: ['**Không khởi tạo lại DSU** giữa các bộ dữ liệu.', '**Khai báo mảng toàn cục cỡ cố định rồi "xóa" bằng `memset` cả mảng** cho mỗi bộ: với T = 10^4^ bộ, tốn 10^4^ · 2·10^5^ phép gán. Chỉ khởi tạo n + 1 phần tử đầu.', '**Quên khuyên:** đỉnh có khuyên vẫn có thể là đỉnh cô lập (thành phần riêng).'],
      approaches: [['CAYKHONG_1chiemcanh', 'Chỉ sửa số cạnh: |m − (n − 1)|'], ['CAYKHONG', 'Công thức m − n + 2k − 1 với DSU']],
    },
    // ================================================================ 3.3
    {
      id: '3.3', key: 'Kích thước thành phần; nối hai nhóm lớn nhất.',
      understand: [
        'Ba câu hỏi đều quy về **kích thước các thành phần liên thông** s~1~, s~2~, ..., s~k~:',
        { ol: ['Máy v liên lạc được với s~comp(v)~ máy (tính cả nó).', 'Số cặp liên lạc được: Σ s~i~(s~i~ − 1)/2.', 'Một sợi cáp nối hai nhóm khác nhau kích thước a, b tạo thêm a · b cặp mới; nối trong cùng một nhóm không tạo cặp nào. Vậy chọn hai nhóm **lớn nhất**.'] },
        { fig: 'tap2:duphong', w: 5.0, cap: 'Ví dụ: hai nhóm 3 máy và một máy lẻ.' },
      ],
      naive: {
        title: 'Cách ngây thơ: BFS riêng từ từng máy',
        body: [
          'Câu hỏi 1 có thể trả lời trực tiếp: với mỗi máy s, BFS để đếm số máy tới được.',
          { fig: 'f_duphong_naive', w: 2.9, cap: 'Sơ đồ khối của cách BFS từ từng máy.' },
          { file: 'DUPHONG_1bfsmoimay', title: 'Cách ngây thơ: n lần BFS' },
          { cx: 'O(n · (n + m)). Với n = 1000 là 2·10^6^; với n = 10^5^ là 2·10^10^.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (n ≤ 1000): chạy kịp: **{{P:DUPHONG_1bfsmoimay:1}} điểm**.', '**Subtask 2, 3**: quá thời gian.'] },
        'Cải tiến tự nhiên: các máy cùng nhóm có cùng đáp số, nên chỉ cần duyệt **mỗi nhóm một lần** (DFS từ đỉnh chưa thăm, ghi số hiệu nhóm). Viết DFS bằng **đệ quy** thì đúng và nhanh ở Subtask 2, nhưng Subtask 3 có mạng hình đường thẳng 5·10^5^ máy: đệ quy sâu 5·10^5^ tầng, tràn ngăn xếp. Cách này được **{{S:DUPHONG_2dequy}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Thuật toán đã đúng, độ phức tạp đã tốt; chỉ còn "chiếc áo" đệ quy là không vừa với dữ liệu.'] },
      ],
      breakthrough: [
        'Duyệt từng nhóm bằng ngăn xếp tự quản lí (như bài 3.1), ghi comp[v] và sz[k]. Sau đó:',
        { ul: ['Dòng 1: in sz[comp[v]] cho mọi v.', 'Dòng 2: Σ sz[k](sz[k] − 1)/2, dùng `long long` (có thể tới 1,25·10^11^).', 'Dòng 3: sắp xếp sz giảm dần, cộng thêm sz[1] · sz[2] nếu có ít nhất hai nhóm.'] },
        { box: 'theorem', title: 'VÌ SAO NỐI HAI NHÓM LỚN NHẤT LÀ TỐT NHẤT?', body: ['Số cặp mới là a · b với a, b là kích thước hai nhóm khác nhau được nối. Tích này lớn nhất khi a, b là hai số lớn nhất trong dãy sz (mọi số đều dương).'] },
        'Ví dụ: sz = (3, 3, 1). Dòng 2: 3 + 3 + 0 = 6. Dòng 3: 6 + 3 · 3 = **15**.',
      ],
      optimal: [
        { file: 'DUPHONG', title: 'DUPHONG.CPP: duyệt từng thành phần một lần, không đệ quy' },
        { cx: 'O(n + m + k log k).' },
      ],
      traps: ['**Tràn số** ở dòng 2 và 3 khi dùng `int`.', '**Chỉ có một nhóm:** không có cặp nhóm nào để nối, dòng 3 bằng dòng 2.', '**DFS đệ quy** trên đồ thị đường thẳng.'],
      approaches: [['DUPHONG_1bfsmoimay', 'BFS riêng từ từng máy'], ['DUPHONG_2dequy', 'Duyệt mỗi nhóm một lần, DFS đệ quy'], ['DUPHONG', 'Duyệt mỗi nhóm một lần, ngăn xếp']],
    },
    // ================================================================ 4.1
    {
      id: '4.1', key: 'BFS một lần từ ô xuất phát.',
      understand: [
        'Mỗi ô là một đỉnh; hai ô có cạnh nếu quân mã nhảy được từ ô này sang ô kia. Số nước ít nhất là **khoảng cách** trên đồ thị không trọng số: BFS. Điểm đặc biệt: **mọi câu hỏi có chung ô xuất phát**.',
        { fig: 'tap2:madituan', w: 5.0, cap: 'Kết quả BFS từ ô (1, 1) trên bàn cờ 5 × 5.' },
      ],
      naive: {
        title: 'Cách ngây thơ: BFS lại cho mỗi câu hỏi',
        body: [
          { fig: 'f_maditan_naive', w: 2.9, cap: 'Sơ đồ khối của cách BFS cho từng câu hỏi.' },
          { file: 'MADITUAN_1bfsmoicau', title: 'Cách ngây thơ: một lần BFS cho mỗi câu hỏi' },
          { cx: 'O(Q · N^2^) trong trường hợp xấu nhất.' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 1** (N ≤ 8): mỗi lần BFS chỉ 64 ô: chạy tốt.', '**Subtask 2** (Q = 1): một lần BFS trên 10^6^ ô: chạy tốt.', '**Subtask 3**: 10^5^ lần BFS trên 10^6^ ô là 10^11^ bước.'] },
        'Được **{{S:MADITUAN_1bfsmoicau}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Mỗi lần BFS đều bắt đầu từ cùng một ô, và đều tính lại khoảng cách tới gần như mọi ô. Kết quả của lần BFS đầu tiên đã trả lời được tất cả các câu hỏi.'] },
      ],
      breakthrough: [
        'BFS **một lần** từ (x~0~, y~0~) trên toàn bàn cờ, lưu d[x][y] cho mọi ô (−1 nếu không tới được), rồi trả lời mỗi câu hỏi bằng một phép tra bảng.',
        'Chạy tay với N = 5, xuất phát (1, 1), các ô được lấy ra khỏi hàng đợi theo từng lớp:',
        { table: { cols: [1100, 6000, 1518], head: ['Lớp d', 'Các ô', 'Số ô'], rows: [['0', '(1, 1)', '1'], ['1', '(2, 3), (3, 2)', '2'], ['2', '(1, 3), (1, 5), (2, 4), (3, 1), (3, 5), (4, 2), (4, 4), (5, 1), (5, 3)', '9'],
          ['3', '(1, 2), (1, 4), (2, 1), (2, 5), (3, 4), (4, 1), (4, 3), (4, 5), (5, 2), (5, 4)', '10'], ['4', '**(2, 2)**, (3, 3), **(5, 5)**', '3']] } },
        'Ô (5, 5) và cả ô (2, 2) "ngay bên cạnh" đều cần 4 nước, khớp với ví dụ.',
        { box: 'def', title: 'MỞ RỘNG: KHI MỖI CÂU HỎI CÓ Ô XUẤT PHÁT RIÊNG', body: ['Nếu ô xuất phát khác nhau, không thể BFS một lần. Với bàn cờ **vô hạn** người ta có công thức đóng cho số nước của quân mã; với bàn cờ hữu hạn, có thể BFS ngược từ ô đích nếu các câu hỏi có chung ô đích.'] },
      ],
      optimal: [
        { file: 'MADITUAN', title: 'MADITUAN.CPP: BFS một lần, trả lời O(1)' },
        { cx: 'O(N^2^ + Q).' },
      ],
      traps: ['**Bàn cờ nhỏ (N ≤ 3):** có ô không tới được, phải in −1 (ví dụ ô giữa bàn 3 × 3).', '**Khai báo `int d[1000][1000]` trong hàm `main`:** 4 MB trên ngăn xếp có thể gây lỗi; dùng `vector` hoặc biến toàn cục.', '**Nhầm hàng và cột** khi đánh số từ 1.'],
      approaches: [['MADITUAN_1bfsmoicau', 'BFS lại cho mỗi câu hỏi'], ['MADITUAN', 'BFS một lần, trả lời bằng tra bảng']],
    },
    // ================================================================ 4.2
    {
      id: '4.2', key: 'BFS nhiều nguồn cho lửa, BFS cho An với điều kiện "<".',
      understand: [
        'Hai "đối tượng" cùng di chuyển: lửa lan theo mọi hướng từ **nhiều** ô, còn An chọn đường đi. Điểm mấu chốt: **lửa không phụ thuộc vào An**. Vì vậy có thể tính trước, cho mỗi ô, phút lửa tới ô đó, rồi coi đó là "hạn chót" để An bước vào.',
        { fig: 'tap2:chaytron', w: 5.8, cap: 'Ví dụ 1: phút lửa tới (trái) và phút An có mặt (phải).' },
      ],
      naive: {
        title: 'Cách ngây thơ: Mô phỏng từng phút trên toàn bảng',
        body: [
          'Mô phỏng đúng như đề bài: giữ hai bảng "ô đang cháy" và "ô An có thể đang đứng". Mỗi phút, cho lửa lan, rồi cho An đi sang các ô kề chưa cháy.',
          { fig: 'f_chaytron_naive', w: 3.2, cap: 'Sơ đồ khối của cách mô phỏng từng phút.' },
          { file: 'CHAYTRON_2mophong', title: 'Cách ngây thơ: mô phỏng từng phút' },
          { cx: 'mỗi phút O(R · C); số phút có thể tới cỡ R · C. Tổng O((R · C)^2^).' },
        ],
      },
      stuck: [
        { ul: ['**Subtask 2** (lưới ≤ 100 × 100): chạy kịp.', '**Subtask 1, 3** (lưới 1000 × 1000, đường chạy dài): quá thời gian.'] },
        'Mô phỏng được **{{S:CHAYTRON_2mophong}} điểm**. Một bạn khác nhận ra Subtask 1 không có lửa nên viết BFS cho An mà **bỏ qua lửa**: đúng Subtask 1 nhưng sai khi có lửa: **{{S:CHAYTRON_1bolua}} điểm**.',
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Mỗi phút, mô phỏng lại tính lại trạng thái lửa của cả bảng, trong khi đường đi của lửa là **cố định**, có thể tính một lần là xong.'] },
      ],
      breakthrough: [
        '**Lần 1: BFS nhiều nguồn cho lửa.** Đẩy mọi ô `F` vào hàng đợi với f = 0. BFS cho f[x][y] = phút lửa tới ô (x, y) (vô cùng nếu không bao giờ tới).',
        '**Lần 2: BFS cho An.** Từ ô `J`, An được bước vào ô (u, v) ở phút t + 1 khi và chỉ khi ô đó không phải tường và **t + 1 < f[u][v]** (lửa tới **sau** An). Ô biên đầu tiên được lấy ra khỏi hàng đợi, ở phút t, cho đáp số t + 1.',
        { box: 'theorem', title: 'VÌ SAO BFS VẪN ĐÚNG KHI CÓ "HẠN CHÓT"?', body: ['Nếu An tới được ô X ở phút t mà lửa chưa tới, thì tới X sớm hơn càng an toàn hơn. Vì vậy đến mỗi ô **sớm nhất có thể** luôn là tốt nhất, và BFS (cho thời điểm sớm nhất) không bỏ sót cách đi nào.'] },
        'Chi tiết quan trọng nhất là dấu **<**. Viết **≤** (cho An vào ô mà lửa tới cùng phút) là sai: đề bài nói An không được bước vào ô mà lửa tới vào cùng phút đó. Cách viết sai này trông gần như giống hệt lời giải mẫu, vượt qua cả hai ví dụ, nhưng trượt những test có "cuộc đua sát nút": chỉ được **{{S:CHAYTRON_3cungluc}} điểm**.',
        { table: { cols: [1500, 1800, 2400, 2918], head: ['Ô (ví dụ 1)', 'Phút lửa tới', 'Phút An tới (đi lên)', 'Được vào?'], rows: [['(2, 3)', '2', '1', '1 < 2: được'], ['(2, 4)', '2', '2', '2 < 2: **không**'], ['(3, 2)', '4', '1', 'được'], ['(5, 2)', '5', '3', 'được, ra ngoài ở phút **4**']] } },
      ],
      optimal: [
        { file: 'CHAYTRON', title: 'CHAYTRON.CPP: hai lần BFS, O(R · C)' },
        { cx: 'mỗi ô vào mỗi hàng đợi nhiều nhất một lần: O(R · C).' },
      ],
      traps: ['**Dấu ≤ thay vì <** (lỗi kinh điển của bài này).', '**An đứng sẵn ở ô biên:** đáp số là 1.', '**Ô không có lửa tới:** f = vô cùng, nhớ dùng giá trị đủ lớn.', '**BFS từng nguồn lửa riêng lẻ** rồi lấy min: đúng nhưng chậm gấp số ô lửa lần.'],
      approaches: [['CHAYTRON_1bolua', 'BFS cho An, bỏ qua lửa'], ['CHAYTRON_2mophong', 'Mô phỏng từng phút'], ['CHAYTRON_3cungluc', 'Hai lần BFS, điều kiện ≤ (sai)'], ['CHAYTRON', 'Hai lần BFS, điều kiện <']],
    },
    // ================================================================ 4.3
    {
      id: '4.3', key: 'Tô hai màu + tổng tập con bằng bitset.',
      understand: [
        'Hai bạn ghét nhau phải khác đội: đây là bài **tô hai màu** đồ thị (Tập 1, Bài 4). Trong mỗi thành phần liên thông, cách tô hai màu là **duy nhất** (sai khác một lần đổi màu toàn bộ). Gọi a~i~, b~i~ là số đỉnh hai màu của thành phần i; ta chỉ được chọn, cho mỗi thành phần, màu nào vào đội A.',
        { fig: 'tap2:chiadoi', w: 5.2, cap: 'Ví dụ 1: ba thành phần có hiệu 0, 2 và 1.' },
        'Độ chênh lệch cuối cùng là |±c~1~ ± c~2~ ± ... ± c~k~| với c~i~ = |a~i~ − b~i~|. Bài toán trở thành: **chia các số c~i~ thành hai nhóm có tổng gần nhau nhất**.',
      ],
      naive: {
        title: 'Cách ngây thơ: Thử mọi cách chia',
        body: [
          { fig: 'f_chiadoi_naive', w: 3.2, cap: 'Sơ đồ khối của cách thử 2ⁿ cách chia.' },
          { file: 'CHIADOI_1vetcan', title: 'Cách ngây thơ: thử 2ⁿ tập con' },
          { cx: 'O(2^n^ · m): chỉ dùng được khi n ≤ 20: **{{S:CHIADOI_1vetcan}} điểm**.' },
        ],
      },
      stuck: [
        'Sau khi tô màu (O(n + m)), còn lại bài toán chia các c~i~. Hai hướng hay gặp:',
        { ul: ['**Tham lam:** xét c~i~ từ lớn tới nhỏ, đặt mỗi số vào phía đang có tổng nhỏ hơn. Đúng khi đồ thị liên thông (chỉ có một số), nhưng sai với dãy 3, 3, 2, 2, 2: tham lam cho 3 + 2 + 2 = 7 và 3 + 2 = 5, chênh 2, trong khi 3 + 3 = 2 + 2 + 2 chênh 0. Được **{{S:CHIADOI_2thamlam}} điểm**.',
          '**Quy hoạch động cái túi:** can[x] = có chọn được nhóm có tổng x không; với mỗi c~i~ cập nhật can từ cao xuống thấp. Đúng, nhưng tốn O(k · S) với S = Σ c~i~ ≤ n. Khi có 10^5^ đỉnh cô lập (k = S = 10^5^), tốn 10^10^ phép tính: **{{S:CHIADOI_3qhd}} điểm**.'] },
        { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: ['Quy hoạch động tổng tập con đã đúng; vấn đề là hằng số và số lượng phần tử. Cần làm mỗi bước cập nhật nhanh hơn, và giảm số bước.'] },
      ],
      breakthrough: [
        'Hai cải tiến độc lập:',
        { ol: ['**`bitset`:** lưu can dưới dạng `bitset<100001>`; bước "thêm số d" chỉ là `can |= can << d`, xử lí 64 giá trị một lúc: mỗi bước tốn S / 64 phép tính.',
          '**Gộp các số bằng nhau:** vì Σ c~i~ ≤ n, số giá trị **khác nhau** của c~i~ không quá khoảng √(2n) ≈ 450. Một giá trị d xuất hiện t lần được tách thành các "gói" d, 2d, 4d, ..., phần dư; mọi số lượng từ 0 tới t đều ghép được từ các gói. Số gói chỉ khoảng log t cho mỗi giá trị.'] },
        'Tổng số bước cập nhật O(√n · log n), mỗi bước O(n / 64): rất nhanh. Cuối cùng tìm x có can[x] = 1 làm |S − 2x| nhỏ nhất.',
        { table: { cols: [2400, 2600, 3618], head: ['Ví dụ 1', 'Giá trị', 'Ghi chú'], rows: [['Hiệu c~i~', '0, 2, 1', 'S = 3'], ['Tổng tập con đạt được', '0, 1, 2, 3', 'chọn {1} hoặc {2}'], ['Đáp số', 'min |3 − 2x| = **1**', 'x = 1 hoặc x = 2']] } },
      ],
      optimal: [
        { file: 'CHIADOI', title: 'CHIADOI.CPP: tô màu + tổng tập con bằng bitset' },
        { cx: 'O(n + m + (n / 64) · √n · log n).' },
      ],
      traps: ['**Quên các đỉnh cô lập:** mỗi đỉnh cô lập là một thành phần có hiệu 1.', '**Phát hiện chu trình lẻ** phải kiểm tra cả cạnh nối tới đỉnh đã tô (không chỉ cạnh cây BFS).', '**Tham lam** cho bài chia tập: chỉ đúng trong một số trường hợp đặc biệt.'],
      approaches: [['CHIADOI_1vetcan', 'Thử 2ⁿ cách chia'], ['CHIADOI_2thamlam', 'Tô màu + tham lam'], ['CHIADOI_3qhd', 'Tô màu + QHĐ cái túi O(k · S)'], ['CHIADOI', 'Tô màu + bitset, gộp số bằng nhau']],
    },
  ],
};
