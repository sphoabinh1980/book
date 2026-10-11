# Lý thuyết đồ thị — Tập 3: Hướng dẫn giải

Mã nguồn dựng cuốn **Tập 3: Hướng dẫn giải** — lời giải chi tiết cho cả 51 bài của Tập 2.
Sản phẩm: `../DT_3_HuongDanGiai.docx` và `../DT_3_HuongDanGiai.pdf`.

Mỗi lời giải đi theo 7 bước: Hiểu bài toán → Cách ngây thơ → Bế tắc → Phá bế tắc → Cách tối ưu →
Bẫy thường gặp → Bảng điểm theo thuật toán. Mọi con số "được bao nhiêu điểm" trong sách là **điểm chấm thật**:
mỗi chương trình trong `code/` được biên dịch và chạy trên bộ test của sách với giới hạn thời gian, bộ nhớ của đề.

| Thư mục | Nội dung |
|---|---|
| `content/` | Nội dung lời giải (`ch1.js` … `ch5.js`), phần đầu sách và phụ lục (`front.js`) |
| `code/CODE.cpp` | Lời giải mẫu (đọc dễ, có chú thích) — đã đối chiếu với chương trình trâu của Tập 2 |
| `code/CODE_<k><tên>.cpp` | Các cách ngây thơ / cách "trông như đúng" được phân tích trong sách |
| `code/lib/` | Thư viện mã nguồn hay dùng (Phụ lục B) |
| `tgen/` | Bộ sinh test theo subtask (`chN.py`, mỗi bài một hàm `g_CODE(subtask, i, rng)`) và chương trình chấm cho bài nhiều đáp án |
| `judge/` | `judge.py` chấm điểm, kết quả ở `scores.json` (sách đọc trực tiếp từ tệp này) |
| `figs/` | Sơ đồ khối (`flow.py`, `flows_chN.py`); hình minh họa đề bài dùng lại của Tập 2 |
| `build/` | Bộ dựng `.docx` (Node.js `docx`) và script đánh số trang mục lục |

```bash
build/build_all.sh             # chấm lại tất cả, vẽ hình, dựng .docx + .pdf
build/build_all.sh --no-judge  # chỉ dựng sách từ scores.json hiện có
python3 -u judge/judge.py CODE # chấm lại một bài
```

Trong nội dung, `{{S:tên}}` là tổng điểm và `{{P:tên:k}}` là điểm subtask k của chương trình `code/tên.cpp`;
bộ dựng thay bằng điểm chấm thật và dừng lại nếu chương trình đó chưa được chấm.
