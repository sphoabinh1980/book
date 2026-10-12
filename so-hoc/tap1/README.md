# Số học — Tập 1: Lý thuyết

Mã nguồn dựng cuốn **Số học — Tập 1: Lý thuyết** (tài liệu bồi dưỡng học sinh giỏi Tin học), cùng phong cách với bộ
*Lý thuyết đồ thị*. Sản phẩm: `../SH_1_LyThuyet.docx` và `../SH_1_LyThuyet.pdf`.

| Thư mục | Nội dung |
|---|---|
| `content/` | Nội dung 5 chương (`ch1.js` … `ch5.js`), phần đầu sách và phụ lục (`front.js`) |
| `code/` | Chương trình in trong sách: `CODE.cpp` (lời giải tốt), `CODE_ngaytho.cpp` (cách ngây thơ), các biến thể |
| `examples/CODE/k.inp` | Ví dụ của các bài toán; `k.out` sinh tự động bằng lời giải trong `code/` |
| `verify/` | Đối chiếu các chương trình với nhau và với tính toán chính xác bằng Python trên test ngẫu nhiên |
| `figs/` | Script vẽ hình (matplotlib) và ảnh `png/` |
| `build/` | Bộ dựng `.docx` (Node.js `docx`), đánh số trang mục lục, xem trước từng chương |

```bash
build/build_all.sh           # vẽ hình, sinh ví dụ, kiểm tra code, dựng .docx + .pdf
python3 verify/run.py        # đối chiếu mọi chương trình trên 300 test ngẫu nhiên mỗi bài
python3 build/preview.py 2   # xem nhanh riêng chương 2
```
Hướng dẫn biên soạn (cấu trúc bài học, quy tắc, đề cương 20 bài): `AUTHORING.md`.
