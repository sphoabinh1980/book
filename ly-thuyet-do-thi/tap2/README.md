# Lý thuyết đồ thị — Tập 2: Bài tập

Mã nguồn dựng cuốn **Tập 2: Bài tập** (51 bài, 3 bài cho mỗi bài học của Tập 1, ở ba mức độ cơ bản / trung bình / nâng cao).
Sản phẩm: `../DT_2_BaiTap.docx` và `../DT_2_BaiTap.pdf`.

| Thư mục | Nội dung |
|---|---|
| `content/` | Nội dung đề bài (`ch1.js` … `ch5.js`), phần đầu sách và phụ lục (`front.js`) |
| `examples/CODE/k.inp` | Dữ liệu ví dụ của từng bài; `k.out` được sinh tự động bằng lời giải mẫu khi dựng sách |
| `sol/CODE.cpp` | Lời giải mẫu (C++17) cho cả 51 bài — dùng để sinh output ví dụ và làm tư liệu cho Tập 3 |
| `verify/` | Sinh test ngẫu nhiên + chương trình trâu / chương trình chấm để đối chiếu lời giải mẫu |
| `figs/` | Script vẽ hình (matplotlib, cùng bảng màu Tập 1) và ảnh `png/` |
| `build/` | Bộ dựng `.docx` (thư viện `docx` của Node.js) và script đánh số trang mục lục |

Dựng lại toàn bộ (cần `g++`, `python3` + `matplotlib`, `node` + `docx`, LibreOffice, `poppler-utils`):

```bash
build/build_all.sh      # biên dịch lời giải, vẽ hình, dựng .docx hai lượt và xuất .pdf
build/stress_all.sh 300 # đối chiếu 51 lời giải mẫu trên 300 test ngẫu nhiên mỗi bài
```

Mọi output trong phần Ví dụ của sách được sinh bằng cách chạy lời giải mẫu; mỗi lời giải mẫu đã được
đối chiếu với chương trình vét cạn (hoặc chương trình chấm, với bài nhiều đáp án) và chạy thử trên dữ liệu cỡ tối đa.
