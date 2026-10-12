# Số học — Tập 2: Bài tập

Mã nguồn dựng cuốn **Số học — Tập 2: Bài tập**: 60 bài tập (3 bài cho mỗi bài học của Tập 1, ở ba mức độ cơ bản /
trung bình / nâng cao), cùng khuôn với *Lý thuyết đồ thị — Tập 2*. Sản phẩm: `../SH_2_BaiTap.docx` và `../SH_2_BaiTap.pdf`.

| Thư mục | Nội dung |
|---|---|
| `content/` | Đề bài (`ch1.js` … `ch5.js`), phần đầu sách và phụ lục (`front.js`) |
| `sol/CODE.cpp` | Lời giải mẫu (C++14) cho cả 60 bài — sinh output ví dụ, làm tư liệu cho Tập 3 |
| `examples/CODE/k.inp` | Dữ liệu ví dụ; `k.out` sinh tự động bằng lời giải mẫu khi dựng sách |
| `verify/` | Sinh test ngẫu nhiên, chương trình vét cạn bằng Python, test cỡ tối đa đo thời gian |
| `figs/` | Script vẽ hình (matplotlib, cùng bảng màu Tập 1) và ảnh `png/` |
| `build/` | Bộ dựng `.docx` (Node.js `docx`), đánh số trang mục lục, xem trước từng chương |

```bash
build/build_all.sh            # biên dịch, kiểm tra, vẽ hình, dựng .docx + .pdf
python3 verify/run.py CODE    # kiểm tra một bài
python3 build/preview.py 3    # xem nhanh riêng chương 3
```
Hướng dẫn biên soạn: `AUTHORING.md`.
