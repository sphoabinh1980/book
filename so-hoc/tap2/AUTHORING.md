# Hướng dẫn biên soạn — Số học, Tập 2: Bài tập

Sách bài tập tiếng Việt cho học sinh giỏi Tin học, đi kèm "Số học — Tập 1: Lý thuyết" (`../tap1`, đã xong) và cùng
khuôn với cuốn "Lý thuyết đồ thị — Tập 2: Bài tập" (`/home/user/book/ly-thuyet-do-thi/tap2`, xem `content/ch1.js` ở đó để
thấy thêm nhiều bài mẫu cùng định dạng). **Bài mẫu chuẩn của sách này: Bài 1 (bài tập 1.1, 1.2, 1.3) trong `content/ch1.js`**,
cùng `sol/NGAYTHU.cpp`, `sol/CHUSOCUOI.cpp`, `sol/VIETLIEN.cpp`, `verify/ch1.py`, `figs/ch1.py`. Đọc kĩ và bắt chước.

Mỗi bài học của Tập 1 có đúng **3 bài tập**: cơ bản (level 1), trung bình (level 2), nâng cao (level 3).
Tên bài và ý tưởng lấy từ mục "Luyện tập" của Tập 1 (danh sách ở mục 5). Được phép chỉnh ràng buộc/chi tiết đề để bài
hay hơn, rõ ràng hơn và đúng mức độ, nhưng giữ tên bài, mã bài (tên tệp) và tinh thần.

## 1. Thư mục và lệnh

| Đường dẫn | Nội dung |
|---|---|
| `content/chN.js` | Nội dung chương N |
| `sol/CODE.cpp` | Lời giải mẫu (C++14, kiểu code thi đấu gọn gàng, có vài chú thích tiếng Việt). Biên dịch vào `bin/` |
| `examples/CODE/k.inp` | Ví dụ; `k.out` được SINH TỰ ĐỘNG khi dựng sách bằng `bin/CODE` — không viết tay |
| `verify/chN.py` | `gen_CODE(rng)`, `brute_CODE(inp)` hoặc `check_CODE(inp, out)`, `big_CODE(rng)` (test cỡ tối đa), `TL_CODE` (giây, mặc định 1) |
| `figs/chN.py` | Hình của chương (matplotlib; dùng `figs/figlib.py`, `figs/shlib.py` — KHÔNG sửa hai tệp này) |

```bash
python3 build/compile.py               # biên dịch sol/*.cpp
python3 verify/run.py CODE1 CODE2 ...  # đối chiếu với brute trên 300 test nhỏ + chạy test lớn nhất đo thời gian
python3 figs/chN.py                    # vẽ hình
python3 build/preview.py N             # dựng riêng chương N → /tmp/claude-0/sh2_preview_chN/sheet_k.png (8 trang/ảnh)
python3 build/preview.py N --pages 9-14 --dpi 80
```
KHÔNG sửa `build/*`, `content/front.js`, `figs/figlib.py`, `figs/shlib.py`, `verify/run.py`, tệp của chương khác.

## 2. Cấu trúc nội dung

```js
const L5 = {
  no: 5, title: 'Tên bài học (giống Tập 1)',
  recap: ['3–4 gạch đầu dòng ÔN NHANH KIẾN THỨC của bài học Tập 1 tương ứng (công thức, độ phức tạp, bẫy)'],
  problems: [ { id: '5.1', name: 'TÊN IN HOA', code: 'MABAI', level: 1, time?: '2 giây', mem?: '64 MB',
      topic: 'Kiến thức cần dùng (Tập 1, Bài x).', skill: 'Kĩ năng rèn luyện (ngắn, hiện trong bảng tổng hợp).',
      statement: [blocks],   // câu chuyện + yêu cầu, rõ ràng, không mơ hồ; định nghĩa mọi khái niệm
      input: [blocks], output: [blocks], limits: ['ràng buộc chung'],
      subtasks: [[điểm, 'ràng buộc thêm'], ...],   // tổng điểm = 100; subtask nhỏ cho lời giải ngây thơ
      examples: [{ explain: ['giải thích ví dụ 1 (có thể nhiều đoạn)'] }, { explain: [...] }],  // theo thứ tự examples/CODE/1.inp, 2.inp...
      after: [{ fig: 'ten_hinh', w: 5.5, cap: 'chú thích' }],   // hình minh họa (gần như bài nào cũng có)
      notes: ['khung CHÚ Ý: bẫy tràn số, số âm, trường hợp đặc biệt... 2–4 ý'],
      hints: ['khung HƯỚNG SUY NGHĨ: 2–3 gợi ý dẫn dắt, KHÔNG lộ hết lời giải'] }, ... ]
};
module.exports = { no, title, intro: 'đoạn mở đầu chương', advice: ['2–3 lời khuyên'], lessons: [...] };
```
Khối (blocks): chuỗi (định dạng `**đậm**`, `*nghiêng*`, `` `code` ``, `^mũ^`, `~chỉ số~` — không lồng nhau),
`{ul:[...]}`, `{ol:[...]}`, `{fig, w, cap}`, `{table:{cols, head, rows}}`, `{box, title, body}`, `{code, title}`, `{formula:'...'}`.

## 3. Quy tắc bắt buộc

- Đề bài như đề thi thật: tên tệp `CODE.INP/OUT`, khuôn dạng vào/ra chính xác, ràng buộc đầy đủ (kể cả số âm, 0, đáp số
  lớn cỡ nào, có mô-đun không), subtask tổng 100, đáp án DUY NHẤT (nếu nhiều đáp án: đề phải chỉ rõ cách chọn — ví dụ nhỏ nhất —
  để so sánh được; tránh dùng checker trừ khi thật cần thiết, khi đó viết `check_CODE`).
- Ví dụ: 2–3 ví dụ mỗi bài (ví dụ 1 nhỏ, dễ chạy tay; một ví dụ "góc" bẫy), giải thích cụ thể, có số liệu. Output tự sinh.
- Hình: bài nào minh họa được thì có hình (bảng số, trục số, lưới, sơ đồ...), cùng bảng màu (ô vàng viền đỏ = đáp số/đang xét,
  xanh dương = bình thường/đã xong, cam nhạt = dữ liệu vào, xám = bị loại). Chữ trong hình đọc được (≥ 9pt khi in), không chồng lên nhau.
  Tên file hình: theo tên bài viết thường, vd. `xephang`, `uoctang`.
- Lời giải mẫu `sol/CODE.cpp`: đúng, đủ nhanh cho test lớn nhất (`big_CODE` phải có cho mọi bài, chạy dưới giới hạn thời gian đề ghi),
  dùng "có tệp thì đọc tệp", C++14 (cho phép `__int128`, `__builtin_*`), mỗi dòng ≤ 100 kí tự.
- `brute_CODE` viết bằng Python, ĐỘC LẬP với lời giải (vét cạn trực tiếp theo định nghĩa, dùng số nguyên lớn của Python).
  `gen_CODE` sinh test nhỏ đa dạng, có trường hợp biên. `verify/run.py` phải in OK cho mọi bài.
- Mọi con số trong đề/giải thích phải được tính bằng máy. Tiếng Việt chuẩn, giọng thân thiện ("em"), dùng "lí", "kĩ", "mô-đun".
  Dấu "·", "−", "≤", "≡", 10^9^. Không dùng emoji.
- Kiểm tra trực quan bằng preview: không chữ chồng chữ trong hình, bảng gọn, không để lại trang gần trắng vô lí.

## 4. Mức độ
- ★☆☆ Cơ bản: áp dụng gần trực tiếp bài học; trọng tâm cài đặt đúng, đủ nhanh.
- ★★☆ Trung bình: cần thêm một quan sát / biến đổi / chi tiết cài đặt quan trọng.
- ★★★ Nâng cao: kết hợp kĩ thuật, mô hình hóa khó; tương đương bài khó cấp tỉnh/quốc gia.

## 5. Danh sách 60 bài (mã tệp in đậm)

Chương 1. CHIA HẾT VÀ ƯỚC SỐ — 1.1 NGÀY TRONG TUẦN **NGAYTHU**, 1.2 CHỮ SỐ CUỐI **CHUSOCUOI**, 1.3 VIẾT LIỀN **VIETLIEN** (xong);
2.1 XẾP HÀNG **XEPHANG**, 2.2 ƯỚC TĂNG DẦN **UOCTANG**, 2.3 SỐ BẠN BÈ **BANBE**; 3.1 CẮT GẠCH **CATGACH**, 3.2 BỎ MỘT SỐ **BOMOTSO**,
3.3 ĐÈN NHÁY **DENNHAY**; 4.1 ĐONG NƯỚC **DONGNUOC**, 4.2 MUA HÀNG **MUAHANG**, 4.3 ĐỒNG HỒ HỎNG **DONGHO**.

Chương 2. SỐ NGUYÊN TỐ — 5.1 NGUYÊN TỐ GẦN NHẤT **NTGANNHAT**, 5.2 TỔNG HAI SỐ NGUYÊN TỐ **GOLDBACH**, 5.3 NGUYÊN TỐ 64 BIT **NT64**;
6.1 ĐẾM SỐ NGUYÊN TỐ **DEMNGUYENTO**, 6.2 SỐ NGUYÊN TỐ SINH ĐÔI **SINHDOI**, 6.3 SỐ CÓ ĐÚNG BA ƯỚC **BAUOC**; 7.1 SỐ ƯỚC **SOUOC**,
7.2 CHỮ SỐ 0 CỦA GIAI THỪA **CHUSO0**, 7.3 BCNN CỦA DÃY **BCNNDAY**; 8.1 NGUYÊN TỐ TRÊN ĐOẠN **NTDOAN**, 8.2 KHOẢNG CÁCH LỚN NHẤT
**KHOANGCACH**, 8.3 SỐ ƯỚC TRÊN ĐOẠN **UOCDOAN**.

Chương 3. SỐ HỌC ĐỒNG DƯ — 9.1 LŨY THỪA **LUYTHUAQ**, 9.2 SỐ MŨ KHỔNG LỒ **SOMULON**, 9.3 TỔNG LŨY THỪA **TONGLT**; 10.1 XÁC SUẤT
**XACSUAT**, 10.2 NGHỊCH ĐẢO DÃY **NGHICHDAO**, 10.3 PHƯƠNG TRÌNH ĐỒNG DƯ **PTDONGDU**; 11.1 PHI **PHI**, 11.2 PHÂN SỐ TỐI GIẢN **PHANSO**,
11.3 THÁP LŨY THỪA **THAPLT**; 12.1 ĐIỂM BINH **DIEMBINH**, 12.2 HAI NGỌN ĐÈN **HAIDEN**, 12.3 LỊCH CAN CHI **CANCHI**.

Chương 4. TỔ HỢP VÀ ĐẾM — 13.1 CHIA KẸO **CHIAKEO**, 13.2 ĐƯỜNG ĐI TRÊN LƯỚI **DUONGLUOI**, 13.3 TỔ HỢP KHỔNG LỒ **TOHOPLON**;
14.1 BỘI SỐ **BOISO**, 14.2 NGUYÊN TỐ CÙNG NHAU **NTCN**, 14.3 TẶNG QUÀ **TANGQUA**; 15.1 LÁT GẠCH **LATGACH**, 15.2 TRIBONACCI **TRIBO**,
15.3 ĐƯỜNG ĐI ĐỘ DÀI K **DUONGK**; 16.1 TỔNG ƯỚC **TONGSIGMA**, 16.2 TỔNG DƯ **TONGDU**, 16.3 HAI THƯƠNG **HAITHUONG**.

Chương 5. KĨ THUẬT SỐ HỌC TRONG LẬP TRÌNH — 17.1 TỔNG LỚN **TONGLON**, 17.2 LŨY THỪA ĐẦY ĐỦ **LUYTHUALON**, 17.3 TÍCH LỚN **TICHLON**;
18.1 ĐỔI CƠ SỐ **DOICOSO**, 18.2 BIT TRONG ĐOẠN **BITDOAN**, 18.3 SỐ CÓ K BIT 1 **KBIT**; 19.1 TỔNG BẰNG KHÔNG **TONG0**, 19.2 ĐOẠN DÀI NHẤT
**DOANDAI**, 19.3 HÌNH CHỮ NHẬT CHIA HẾT **HCNCHIAHET**; 20.1 TRỒNG CÂY **TRONGCAY**, 20.2 ĐA GIÁC LƯỚI **DAGIAC**, 20.3 TAM GIÁC NGUYÊN **TAMGIAC**.

Ý tưởng chi tiết của từng bài: xem mục `practice` cuối mỗi bài học trong `../tap1/content/chN.js` (cột "Gợi ý liên hệ"),
và nội dung bài học tương ứng để viết `recap` và `topic` chính xác (trích đúng số bài Tập 1).
