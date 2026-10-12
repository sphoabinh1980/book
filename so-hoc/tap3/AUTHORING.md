# Hướng dẫn biên soạn — Số học, Tập 3: Hướng dẫn giải

Lời giải chi tiết cho 60 bài tập của Tập 2 (`../tap2`), cùng khuôn với "Lý thuyết đồ thị — Tập 3"
(`/home/user/book/ly-thuyet-do-thi/tap3`: xem `content/ch1.js`, `code/`, `tgen/ch1.py`, `figs/flows_ch1.py` ở đó để thấy
nhiều bài mẫu cùng định dạng). **Bài mẫu chuẩn của sách này: 3 lời giải 1.1–1.3 trong `content/ch1.js`**, cùng
`code/NGAYTHU*.cpp`, `code/CHUSOCUOI*.cpp`, `code/VIETLIEN*.cpp`, `tgen/ch1.py`, `figs/flows_ch1.py`. Đọc kĩ và bắt chước.

## 1. Ý tưởng cốt lõi: điểm chấm thật

Mỗi lời giải phân tích **nhiều cách làm** (ngây thơ, trung gian, "trông như đúng nhưng sai một chi tiết", lời giải mẫu).
Mỗi cách làm là một chương trình thật trong `code/`, được **chấm thật** bằng `judge/judge.py` trên bộ test theo subtask của đề
(subtask, giới hạn thời gian, bộ nhớ được lấy tự động từ `../tap2/content`; ngăn xếp 8 MB). Văn bản không bao giờ ghi điểm bằng tay:
dùng `{{S:TÊN}}` (tổng điểm) và `{{P:TÊN:k}}` (điểm subtask k); bộ dựng thay bằng điểm thật và báo lỗi nếu chương trình chưa chấm.
**Lời văn phải khớp với kết quả chấm** (subtask nào qua, vì sao trượt: TLE/WA/MLE/RTE). Nếu kết quả khác dự kiến thì
hoặc sửa văn, hoặc thiết kế lại test cho đúng ý đồ của subtask (test "bẫy" hợp lệ theo đề).

## 2. Thư mục và lệnh

| Đường dẫn | Nội dung |
|---|---|
| `content/chN.js` | `module.exports = { no, intro, solutions: [...] }` |
| `code/CODE.cpp` | Lời giải mẫu dạng **dễ đọc** (chú thích tiếng Việt, mỗi dòng ≤ 76 kí tự) — in trong sách |
| `code/CODE_<k><tên>.cpp` | Các cách làm khác, k = 1, 2, 3... theo thứ tự trình bày (vd. `NGAYTHU_1demngay`) |
| `tgen/chN.py` | `g_CODE(st, i, rng)` sinh test thứ i của subtask st (đúng ràng buộc subtask, cỡ lớn nhất, có test bẫy); `SPEC = {CODE: S(g_CODE, [số test mỗi subtask], check=None)}` |
| `figs/flows_chN.py` | Sơ đồ khối `f_<mã thường>_naive`, `f_<mã thường>_opt` (dùng `flow()` trong `figs/flow.py`) và hình riêng nếu cần |

```bash
python3 -u judge/judge.py CODE1 CODE2     # sinh test (đáp án từ ../tap2/sol), chấm mọi code/CODE*.cpp, ghi judge/scores.json
python3 build/check_code.py               # dòng code ≤ 76 kí tự
python3 figs/flows_chN.py
python3 build/preview.py N                # dựng riêng chương N → /tmp/claude-0/sh3_preview_chN/sheet_k.png
python3 build/preview.py N --pages 9-14 --dpi 80
```
Đáp án test lấy từ lời giải mẫu đã kiểm chứng của Tập 2 (`../tap2/sol/CODE.cpp`). Lời giải dễ đọc `code/CODE.cpp` phải đạt 100.
KHÔNG sửa `build/*`, `content/front.js`, `judge/judge.py`, `tgen/common.py`, `figs/flow.py`, `figs/figlib.py`, `figs/shlib.py`,
`../tap2/*`, tệp của chương khác. Khi chấm, chỉ chấm các mã bài của mình (judge ghi đè đúng phần của mã đó trong scores.json;
nhiều tác giả chạy song song — nếu scores.json bị ghi đè mất phần của mình thì chấm lại).

## 3. Cấu trúc một lời giải (7 mục, tự động đánh số)

```js
{ id: '5.1', key: 'chìa khóa một câu (hiện ở bảng đầu chương và Phụ lục A)',
  understand: [blocks],      // 1. Hiểu bài toán: diễn đạt lại bằng số học, đại lượng lớn tới đâu, hình 'tap2:<tên hình của Tập 2>'
  naive: { title: 'Cách ngây thơ: ...', body: [lời dẫn, {fig:'f_x_naive', w:3}, {file:'CODE_1...', title}, {cx:'...'}] },
  stuck: [blocks],           // 3. Bế tắc: {ul:['**Subtask 1** ...: **{{P:CODE_1x:1}} điểm**.', ...]}, các cách "trông như đúng" với {{S:...}},
                             //    kết thúc bằng { box: 'warn', title: 'ĐIỂM BẾ TẮC', body: [...] }
  breakthrough: [blocks],    // 4. Phá bế tắc: {step:'...'} (Bước 1, 2...), công thức, chạy tay bằng bảng (số liệu chạy bằng máy), box 'theorem' VÌ SAO ĐÚNG?
  optimal: [{fig:'f_x_opt'}, {file:'CODE', title:'CODE.CPP: ...'}, {cx:'...'}, (tùy chọn box 'def' MỞ RỘNG)],
  traps: ['**Tên bẫy:** giải thích', ...],   // 6. Bẫy thường gặp (3–5)
  approaches: [['CODE_1x', 'mô tả ngắn'], ..., ['CODE', 'lời giải mẫu']],   // 7. Bảng điểm (dòng CODE tô xanh)
  link?: 'Bài 7' }           // nếu dùng thêm bài học khác của Tập 1
```
Khối: chuỗi (`**đậm**`, `*nghiêng*`, `` `code` ``, `^mũ^`, `~chỉ số~`, không lồng nhau), `{ul}`, `{ol}`, `{fig, w, cap}`, `{table:{cols,head,rows,aligns}}`,
`{box: 'warn'|'theorem'|'note'|'def'|'hint'|'remember', title, body}`, `{code, title}`, `{file, title}`, `{cx}`, `{formula}`, `{step}`, `{sub}`.

## 4. Quy tắc bắt buộc

- Mỗi bài có **ít nhất 3 cách làm** được chấm: (1) ngây thơ đúng nhưng chậm — đạt đúng các subtask nhỏ; (2) ít nhất một cách
  "trông như đúng" (thuật toán tốt nhưng sai một chi tiết: tràn số, số âm, quên trường hợp, dùng `int`, `sqrt` số thực, quên `__int128`,
  đọc số vào kiểu số...) hoặc một cách trung gian; (3) lời giải mẫu 100 điểm. Mục tiêu: bảng điểm có **bậc thang** rõ ràng.
- Bộ test (`tgen`) phải tuân thủ đúng ràng buộc chung + ràng buộc subtask của đề Tập 2, có test cỡ lớn nhất và test bẫy (biên, số
  nguyên tố lớn, số chính phương, b chia hết 4, m = 1, số âm...). Thường 2–5 test mỗi subtask. Test lớn nên sinh nhanh (vài giây).
- Mọi số liệu trong bảng chạy tay / giải thích đều phải được tính bằng máy. Chạy tay trên ví dụ của đề Tập 2 (examples ở `../tap2/examples/CODE`).
- Code: C++14 (`__int128` được), mẫu "có tệp thì đọc tệp", thụt 4 cách, tên biến ngắn, chú thích tiếng Việt ngắn, **≤ 76 kí tự mỗi dòng**.
- Giọng văn: thầy giảng cho "em", giải thích **vì sao**; tiếng Việt chuẩn, "lí", "kĩ", "mô-đun"; dấu "·", "−", "≤", "≡", 10^9^. Không emoji.
- Kiểm tra trực quan bằng preview: sơ đồ khối và bảng không vỡ, không trang trắng vô lí, không chữ chồng chữ.

## 5. Mã bài theo chương (60 bài, đề ở `../tap2/content/chN.js`)

- Chương 1: NGAYTHU, CHUSOCUOI, VIETLIEN (xong) · XEPHANG, UOCTANG, BANBE · CATGACH, BOMOTSO, DENNHAY · DONGNUOC, MUAHANG, DONGHO
- Chương 2: NTGANNHAT, GOLDBACH, NT64 · DEMNGUYENTO, SINHDOI, BAUOC · SOUOC, CHUSO0, BCNNDAY · NTDOAN, KHOANGCACH, UOCDOAN
- Chương 3: LUYTHUAQ, SOMULON, TONGLT · XACSUAT, NGHICHDAO, PTDONGDU · PHI, PHANSO, THAPLT · DIEMBINH, HAIDEN, CANCHI
- Chương 4: CHIAKEO, DUONGLUOI, TOHOPLON · BOISO, NTCN, TANGQUA · LATGACH, TRIBO, DUONGK · TONGSIGMA, TONGDU, HAITHUONG
- Chương 5: TONGLON, LUYTHUALON, TICHLON · DOICOSO, BITDOAN, KBIT · TONG0, DOANDAI, HCNCHIAHET · TRONGCAY, DAGIAC, TAMGIAC

Lí thuyết tương ứng: `../tap1/content/chN.js`. Đề, ví dụ, hình của Tập 2: `../tap2/content/chN.js`, `../tap2/examples/`, `../tap2/figs/png/`.
Lời giải tham khảo đã kiểm chứng: `../tap2/sol/CODE.cpp`; bộ vét cạn: `../tap2/verify/chN.py`.
