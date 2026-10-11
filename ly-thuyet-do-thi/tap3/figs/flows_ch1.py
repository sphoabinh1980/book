from flow import flow
flow('f_battay_naive', [('term', 'Bắt đầu'), ('io', 'Đọc n và d₁, ..., dₙ'), ('proc', 'Đưa mọi dᵢ > 0 vào hàng đợi ưu tiên'), ('loop', 'còn ≥ 2 bạn\nchưa đủ?'),
    ('proc', 'lấy hai bạn thiếu nhiều nhất a, b\ncnt ← cnt + 1\ntrả lại a − 1, b − 1 (nếu còn > 0)'), ('end', ''), ('dec', 'còn sót\nmột bạn?', ('In −1', 'io')), ('io', 'In cnt'), ('term', 'Kết thúc')])
flow('f_battay_opt', [('term', 'Bắt đầu'), ('io', 'Đọc n và d₁, ..., dₙ'), ('proc', 'S ← tổng các dᵢ (long long)\nM ← dᵢ lớn nhất'), ('dec', 'S lẻ hoặc\nM > S − M ?', ('In −1', 'io')), ('io', 'In S / 2'), ('term', 'Kết thúc')])
flow('f_noitieng_naive', [('term', 'Bắt đầu'), ('io', 'Đọc n, m và m dòng (u, v)'), ('proc', 'v ← 1'), ('loop', 'v ≤ n ?'),
    ('proc', 'duyệt cả m dòng, đếm\nvào(v) và ra(v)'), ('proc', 'nếu vào(v) = n − 1 và ra(v) = 0\nthì ghi nhận v'), ('proc', 'v ← v + 1'), ('end', ''), ('io', 'In kết quả'), ('term', 'Kết thúc')])
flow('f_tamgiac_naive', [('term', 'Bắt đầu'), ('io', 'Đọc đồ thị vào ma trận kề a'), ('loop', 'còn bộ ba\nx < y < z ?'), ('proc', 'nếu a[x][y], a[y][z], a[x][z]\nđều đúng thì cnt ← cnt + 1'), ('end', ''), ('io', 'In cnt'), ('term', 'Kết thúc')])
flow('f_tamgiac_opt', [('term', 'Bắt đầu'), ('io', 'Đọc cạnh, tính bậc'), ('proc', 'hướng mỗi cạnh từ đỉnh "thấp"\nsang đỉnh "cao"'), ('loop', 'còn đỉnh u ?'),
    ('proc', 'đánh dấu mọi v với u → v'), ('proc', 'với mỗi u → v → w:\nnếu w được đánh dấu, cnt ← cnt + 1'), ('end', ''), ('io', 'In cnt'), ('term', 'Kết thúc')])
flow('f_chuyendoi', [('term', 'Bắt đầu'), ('io', 'Đọc n'), ('loop', 'còn ô (i, j)\ntheo thứ tự hàng?'), ('io', 'Đọc x = a[i][j]'),
    ('proc', 'nếu x = 1: thêm j vào g[i];\nnếu thêm i < j: thêm (i, j)\nvào danh sách cạnh'), ('end', ''), ('io', 'In danh sách cạnh,\nrồi n dòng danh sách kề'), ('term', 'Kết thúc')])
flow('f_banchung_naive', [('term', 'Bắt đầu'), ('io', 'Đọc cạnh vào ma trận kề a'), ('loop', 'còn câu hỏi\n(u, v)?'), ('proc', 'c ← số w có a[u][w] và a[v][w]\n(duyệt w = 1..n)'), ('io', 'In c'), ('end', ''), ('term', 'Kết thúc')])
flow('f_bando_naive', [('term', 'Bắt đầu'), ('io', 'Đọc bản đồ'), ('io', 'In đếmLại()'), ('loop', 'còn sự kiện\n(x, y)?'), ('proc', 'đổi trạng thái ô (x, y)'), ('io', 'In đếmLại()   — O(R·C)'), ('end', ''), ('term', 'Kết thúc')])
flow('f_demdao_naive', [('term', 'Hàm dfs(x, y)'), ('dec', 'ra ngoài bảng hoặc\nkhông phải ô đất?', ('trở về', 'term')), ('proc', 'đánh dấu (x, y); diện tích + 1'), ('proc', 'dfs(x − 1, y); dfs(x + 1, y)\ndfs(x, y − 1); dfs(x, y + 1)'), ('term', 'trở về')])
flow('f_demdao_opt', [('term', 'Bắt đầu loang từ ô đất (i, j)'), ('proc', 'đánh dấu (i, j), đẩy vào ngăn xếp'), ('loop', 'ngăn xếp\ncòn ô?'),
    ('proc', 'lấy ô (x, y) ra; diện tích + 1'), ('proc', 'ô đất kề chưa đánh dấu:\nđánh dấu và đẩy vào'), ('end', ''), ('term', 'xong một hòn đảo')])
flow('f_caykhong_opt', [('term', 'Một bộ dữ liệu'), ('proc', 'DSU n đỉnh, k ← n'), ('loop', 'còn cạnh (u, v)?'), ('proc', 'nếu root(u) ≠ root(v):\ngộp hai nhóm, k ← k − 1'), ('end', ''), ('io', 'In (m − (n − k)) + (k − 1)'), ('term', 'Kết thúc')])
flow('f_duphong_naive', [('term', 'Bắt đầu'), ('io', 'Đọc mạng'), ('proc', 's ← 1'), ('loop', 's ≤ n ?'), ('proc', 'BFS từ s trên toàn mạng\nsz[s] ← số máy tới được'), ('proc', 's ← s + 1'), ('end', ''), ('io', 'Tính và in ba dòng'), ('term', 'Kết thúc')])
flow('f_maditan_naive', [('term', 'Bắt đầu'), ('io', 'Đọc N, ô xuất phát, Q'), ('loop', 'còn câu hỏi?'), ('io', 'Đọc ô đích (x, y)'), ('proc', 'BFS từ ô xuất phát\ntrên N × N ô'), ('io', 'In d(x, y)'), ('end', ''), ('term', 'Kết thúc')])
flow('f_chaytron_naive', [('term', 'Bắt đầu'), ('proc', 'fire ← các ô F; here ← ô J; t ← 0'), ('loop', 'An còn chỗ\nđứng?'), ('dec', 'có ô "here"\nở biên?', ('In t + 1', 'io')),
    ('proc', 'lửa lan: duyệt toàn bảng'), ('proc', 'An đi: duyệt toàn bảng,\nbỏ các ô đã cháy'), ('proc', 't ← t + 1'), ('end', ''), ('io', 'In −1'), ('term', 'Kết thúc')])
flow('f_chiadoi_naive', [('term', 'Bắt đầu'), ('io', 'Đọc n, m và các cặp ghét nhau'), ('loop', 'còn mask từ 0\ntới 2ⁿ − 1 ?'),
    ('proc', 'bit i của mask = 1: bạn i ở đội A'), ('dec', 'có cặp ghét nhau\ncùng đội?', ('bỏ qua mask', 'proc')), ('proc', 'best ← min(best, |n − 2·|A||)'), ('end', ''), ('io', 'In best (−1 nếu không có)'), ('term', 'Kết thúc')])
