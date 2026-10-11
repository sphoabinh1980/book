from flow import flow
flow('f_duongtruong_naive', [('term', 'Bắt đầu'), ('io', 'Đọc đồ thị; d[s] ← 0, d[v] ← ∞'), ('loop', 'còn đỉnh\nchưa chốt?'), ('proc', 'u ← đỉnh chưa chốt có d nhỏ nhất\n(duyệt cả n đỉnh)'),
    ('proc', 'chốt u; nới lỏng các cung u → v'), ('end', ''), ('io', 'In d[1..n]'), ('term', 'Kết thúc')])
flow('f_duongtruong_opt', [('term', 'Bắt đầu'), ('proc', 'd[s] ← 0; đẩy (0, s) vào hàng đợi ưu tiên'), ('loop', 'hàng đợi\ncòn phần tử?'), ('proc', 'lấy (du, u) nhỏ nhất'),
    ('dec', 'du ≠ d[u] ?', ('bỏ qua (bản cũ)', 'proc')), ('proc', 'với mỗi u → v: nếu d[u] + w < d[v]\nthì cập nhật d[v], đẩy (d[v], v)'), ('end', ''), ('io', 'In d[1..n]'), ('term', 'Kết thúc')])
flow('f_nutgiao_naive', [('term', 'Bắt đầu'), ('proc', 'D ← Dijkstra từ 1 tới n'), ('loop', 'còn đỉnh v\n(khác 1, n)?'), ('proc', 'Dijkstra lại, cấm đi qua v'),
    ('proc', 'nếu khoảng cách mới > D\nthì v là nút quan trọng'), ('end', ''), ('io', 'In các nút quan trọng'), ('term', 'Kết thúc')])
flow('f_xebuyt_naive', [('term', 'Bắt đầu'), ('proc', 'd[1] ← 0, d[v] ← ∞'), ('loop', 'lượt trước có\nthay đổi?'), ('proc', 'với mỗi tuyến u → v: tính chuyến\nsớm nhất sau d[u], cập nhật d[v]'), ('end', ''), ('io', 'In d[n]'), ('term', 'Kết thúc')])
flow('f_doitien_naive', [('term', 'Bắt đầu'), ('loop', 'còn bộ hai/ba\nquầy nối vòng?'), ('dec', 'tích tỉ giá > 1 ?', ('In YES', 'io')), ('end', ''), ('io', 'In NO'), ('term', 'Kết thúc')])
flow('f_bayre_opt', [('term', 'Bắt đầu'), ('proc', 'd[1] ← 0, d[v] ← ∞'), ('loop', 'đã chạy\n< k lượt?'), ('proc', 'nd ← bản sao của d'), ('proc', 'với mỗi chuyến u → v (giá c):\nnd[v] ← min(nd[v], d[u] + c)'), ('proc', 'd ← nd'), ('end', ''), ('io', 'In d[n]'), ('term', 'Kết thúc')])
flow('f_lichthidau_opt', [('term', 'Bắt đầu'), ('proc', 'đổi ràng buộc thành cung x → y nhãn c\n(ngày[y] ≥ ngày[x] + c); ngày[v] ← 1'), ('loop', 'chưa quá\nn + 1 lượt?'),
    ('proc', 'với mỗi cung: nếu ngày[x] + c > ngày[y]\nthì tăng ngày[y]'), ('dec', 'không có\nthay đổi?', ('In ngày[1..n]', 'io')), ('end', ''), ('io', 'In −1'), ('term', 'Kết thúc')])
flow('f_thudo_naive', [('term', 'Bắt đầu'), ('loop', 'còn thành phố s?'), ('proc', 'Bellman-Ford từ s: O(n · m)'), ('proc', 'tổng khoảng cách; cập nhật kết quả'), ('end', ''), ('io', 'In thành phố tốt nhất'), ('term', 'Kết thúc')])
flow('f_xephang_naive', [('term', 'Bắt đầu'), ('io', 'Đọc kết quả vào ma trận r'), ('loop', 'k = 1..n'), ('proc', 'với mọi i, j: nếu r[i][k] và r[k][j]\nthì r[i][j] ← đúng'), ('end', ''), ('proc', 'đếm số người so sánh được với v'), ('io', 'In các v có đủ n − 1'), ('term', 'Kết thúc')])
flow('f_xetai_naive', [('term', 'Bắt đầu'), ('loop', 'còn câu hỏi\n(s, t)?'), ('proc', 'tìm nhị phân W trên [0, 10⁹]'), ('proc', 'mỗi bước: DFS chỉ qua đường\nchịu ≥ W, kiểm tra tới t'), ('io', 'In W lớn nhất'), ('end', ''), ('term', 'Kết thúc')])
flow('f_dengiaothong_naive', [('term', 'Bắt đầu'), ('proc', 'cur ← {1}; t ← 0'), ('loop', 't ≤ n · P ?'), ('dec', 'n thuộc cur ?', ('In t', 'io')), ('proc', 'nút u ∈ cur có đèn xanh lúc t:\nthêm mọi nút kề vào cur'), ('proc', 't ← t + 1'), ('end', ''), ('io', 'In −1'), ('term', 'Kết thúc')])
flow('f_phatuong_naive', [('term', 'Hàm thử(từ, còn)'), ('proc', 'best ← min(best, BFS trên bản đồ hiện tại)'), ('dec', 'còn = 0 ?', ('trở về', 'term')), ('loop', 'còn bức tường i\n≥ từ?'), ('proc', 'phá tường i; thử(i + 1, còn − 1);\nxây lại tường i'), ('end', ''), ('term', 'trở về')])
flow('f_robotxoay_opt', [('term', 'Bắt đầu'), ('proc', 'đẩy trạng thái (S, h) vào deque, d = 0'), ('loop', 'deque còn\ntrạng thái?'), ('proc', 'lấy (x, y, k) ở đầu deque'), ('dec', 'ô (x, y) là T ?', ('In d', 'io')),
    ('proc', 'tiến (giá 0): đẩy vào ĐẦU'), ('proc', 'xoay trái/phải (giá 1): đẩy vào CUỐI'), ('end', ''), ('io', 'In −1'), ('term', 'Kết thúc')])
