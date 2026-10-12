# Số học — Tập 3: Hướng dẫn giải

Lời giải chi tiết cho cả 60 bài tập của Tập 2, cùng khuôn với *Lý thuyết đồ thị — Tập 3*.
Sản phẩm: `../SH_3_HuongDanGiai.docx` và `../SH_3_HuongDanGiai.pdf`.

Mỗi lời giải đi theo 7 bước: Hiểu bài toán → Cách ngây thơ → Bế tắc → Phá bế tắc → Cách tối ưu → Bẫy thường gặp →
Bảng điểm theo thuật toán. Mọi con số "được bao nhiêu điểm" là **điểm chấm thật**: mỗi chương trình trong `code/` được
biên dịch và chạy trên bộ test theo subtask của đề, với giới hạn thời gian, bộ nhớ của đề và ngăn xếp 8 MB.

| Thư mục | Nội dung |
|---|---|
| `content/` | Nội dung lời giải (`ch1.js` … `ch5.js`), phần đầu sách và phụ lục (`front.js`) |
| `code/CODE.cpp` | Lời giải mẫu dạng dễ đọc; `code/CODE_<k><tên>.cpp`: các cách làm được phân tích |
| `code/lib/` | Thư viện mã nguồn hay dùng (Phụ lục B) |
| `tgen/` | Bộ sinh test theo subtask cho từng bài |
| `judge/` | `judge.py` chấm điểm, kết quả ở `scores.json`; subtask/giới hạn lấy trực tiếp từ đề Tập 2 |
| `figs/` | Sơ đồ khối; hình minh họa đề dùng lại của Tập 2 |
| `build/` | Bộ dựng `.docx`, đánh số trang mục lục, xem trước từng chương |

```bash
build/build_all.sh               # chấm lại tất cả, vẽ hình, dựng .docx + .pdf
build/build_all.sh --no-judge    # chỉ dựng từ scores.json hiện có
python3 -u judge/judge.py CODE   # chấm lại một bài
```
Trong nội dung, `{{S:tên}}` là tổng điểm và `{{P:tên:k}}` là điểm subtask k của `code/tên.cpp`. Hướng dẫn biên soạn: `AUTHORING.md`.
