# Hướng dẫn biên soạn — Số học, Tập 1: Lý thuyết

Sách giáo khoa tiếng Việt cho học sinh giỏi Tin học (THCS–THPT), cùng phong cách với cuốn
"Lý thuyết đồ thị — Tập 1" (cùng tác giả Lê Thành Nam). Bài mẫu hoàn chỉnh: **Bài 1 trong
`content/ch1.js`** (code `code/SODU*.cpp`, hình `figs/ch1.py`, kiểm tra `verify/ch1.py`).
Hãy đọc kĩ Bài 1 và bắt chước cả cấu trúc, giọng văn, mật độ hình/bảng, độ dài (≈ 10–14 trang/bài).

## 1. Thư mục

| Đường dẫn | Nội dung |
|---|---|
| `content/chN.js` | Nội dung chương N (một object, xem mục 3) |
| `code/CODE.cpp` | Lời giải tối ưu của bài toán chính; `code/CODE_ngaytho.cpp` cách ngây thơ; có thể thêm `CODE_<tên>.cpp` |
| `examples/CODE/k.inp` | Ví dụ của bài toán (k = 1, 2, 3...). File `.out` được SINH TỰ ĐỘNG bằng `bin/CODE` — không viết tay |
| `verify/chN.py` | `SPEC = {CODE: {'gen': f(rng)->str, 'progs': [...], 'brute': f(inp)->str}}` để đối chiếu |
| `figs/chN.py` | Script vẽ mọi hình của chương (matplotlib), ảnh ra `figs/png/` |
| `figs/shlib.py`, `figs/figlib.py`, `figs/flow.py` | Thư viện vẽ dùng chung — KHÔNG sửa (nếu cần hàm mới, viết trong `figs/chN.py`) |
| `build/*.js`, `content/front.js` | Bộ dựng — KHÔNG sửa. Cần loại khối mới thì báo lại, đừng tự sửa |

## 2. Lệnh

```bash
python3 figs/chN.py                 # vẽ hình
python3 build/run_examples.py       # biên dịch code/*.cpp vào bin/, sinh examples/*/k.out
python3 verify/run.py CODE1 CODE2   # đối chiếu các chương trình + brute trên 300 test ngẫu nhiên
python3 build/check_code.py         # mọi dòng code ≤ 76 kí tự (sách không ngắt dòng xấu)
python3 build/preview.py N          # dựng riêng chương N → /tmp/claude-0/preview_chN/sheet_k.png (ảnh ghép 8 trang)
python3 build/preview.py N --pages 5-8 --dpi 80   # xem kĩ vài trang
```
Xem ảnh `sheet_k.png` bằng công cụ Read để kiểm tra hình, bảng, khoảng trắng.

## 3. Cấu trúc nội dung (`content/chN.js`)

```js
module.exports = { no: N, title: 'TÊN CHƯƠNG IN HOA', intro: [blocks...], lessons: [L5, L6, ...] };
const L5 = {
  no: 5, title: 'Tên bài học', sub: 'phụ đề ngắn (hiện trong khung TRONG CHƯƠNG NÀY)',
  goals: ['3–5 mục "Học xong bài này, em sẽ:"'],
  warmup: [blocks],            // khung KHỞI ĐỘNG: câu chuyện/câu đố gần gũi, 2 đoạn
  body: [blocks],              // phần chính, xem thứ tự bên dưới
  ext: [blocks],               // mục "Mở rộng" (tự đánh số tiếp), 2–4 mở rộng dạng {sub:'Mở rộng 1: ...'}
  traps: ['4–6 bẫy, mỗi bẫy bắt đầu bằng **tên ngắn in đậm:** rồi giải thích'],
  remember: ['4–5 ý cốt lõi'],
  practice: [['5.1', 'TÊN BÀI TẬP', 'gợi ý liên hệ'], ...3 bài (cơ bản, trung bình, nâng cao)],
  quiz: [['câu hỏi tự kiểm tra', 'Đáp số: ...'], ...3–4 câu, đáp số PHẢI tính lại bằng máy],
  algos: [['Tên thuật toán / công thức', 'O(...)'], ...],   // cho Phụ lục A
};
```

Thứ tự `body` chuẩn (theo Bài 1):
1. `{h: '...'}` các mục kiến thức nền (định nghĩa, định lí, hình trực quan, ví dụ tính tay) — 1 đến 3 mục.
2. `{h: 'Bài toán CODE'}`, `{problem: {...}}`, `{examples: 'CODE', explain: [...]}`.
3. `{h: 'Ý tưởng ngây thơ: ...'}` — lời dẫn, `{fig: 'fN_ngaytho'}` (sơ đồ khối), `{file: 'CODE_ngaytho', title}`, khung `count`, khung `stuck`.
4. `{h: 'Phá bế tắc: ...'}` — các `{step: '...'}` (tự đánh số Bước 1, 2...), hình chạy tay, bảng chạy tay, khung `why` (chứng minh), `{step:'Chương trình'}` + sơ đồ khối + `{file: 'CODE'}` + khung `count`.
5. (tự động) Mở rộng, BẪY THƯỜNG GẶP, GHI NHỚ, Luyện tập, Tự kiểm tra nhanh.

Các loại khối (block):
- `'chuỗi'` đoạn văn. Định dạng nội dòng: `**đậm**`, `*nghiêng*`, `` `code` ``, `^mũ^` (10^9^), `~chỉ số dưới~` (a~i~).
- `{h}` đề mục cấp 1 trong bài (tự đánh số) · `{step}` "Bước k" · `{sub}` tiêu đề nhỏ màu đỏ.
- `{formula: '...'}` công thức một dòng, căn giữa, đậm.
- `{ul: [...]}`, `{ol: [...]}`.
- `{box: KIND, title?: '...', body: [blocks]}` với KIND ∈ `def` (ĐỊNH NGHĨA), `theorem` (ĐỊNH LÍ), `algo` (THUẬT TOÁN),
  `count` (ĐẾM SỐ PHÉP TÍNH), `stuck` (BẾ TẮC), `why` (VÌ SAO ĐÚNG?), `imagine` (HÃY HÌNH DUNG), `example` (VÍ DỤ),
  `note` (LƯU Ý), `hint` (GỢI Ý). Tiêu đề có thể ghi rõ: `title: 'ĐỊNH LÍ (BÉZOUT)'`.
- `{fig: 'tên', w: inch, cap: 'chú thích'}` — tự đánh số "Hình N.k." theo số bài. w: 2.6–3.0 cho sơ đồ khối, 4.5–6.3 cho hình rộng.
- `{table: {cols: [DXA...] (tổng ≤ 8618), head: [...], rows: [[...]], aligns: ['center',...]}}`.
- `{problem: {code, statement: [blocks], input: '...', output: '...', limits?: '...'}}` · `{examples: 'CODE', explain: ['...', ...]}`.
- `{file: 'TÊN', title: 'TÊN.CPP: mô tả'}` in mã nguồn `code/TÊN.cpp` · `{cx: '...'}` dòng "Độ phức tạp: ...".

## 4. Quy tắc nội dung (BẮT BUỘC)

- Tiếng Việt chuẩn, xưng "em", giọng thầy giảng: dẫn dắt bằng câu hỏi, giải thích **vì sao**, không liệt kê khô.
  Dùng "lí" (định lí, lí thuyết), "kĩ", "mô-đun", "ƯCLN/BCNN" (trong công thức viết gcd, lcm). Dấu nhân "·", dấu trừ "−", "≤ ≥ ≠ ≡".
  Số lớn viết nhóm 3: 1 000 000 hoặc 10^6^. Không dùng emoji.
- **Mọi con số** trong ví dụ, bảng chạy tay, đáp số tự kiểm tra phải được TÍNH BẰNG MÁY (Python) trước khi viết. Bảng chạy tay
  nên được sinh bằng chạy đúng thuật toán (in ra rồi chép vào).
- Mỗi bài có: ≥ 1 hình trực quan "hãy hình dung" (không chỉ sơ đồ khối), 2 sơ đồ khối (ngây thơ + tối ưu), ≥ 2 bảng, ≥ 1 chứng minh
  (khung why/theorem), ví dụ tính tay, Mở rộng 2–4 mục (có công thức/code ngắn nếu cần).
- Code: C++14, `#include <bits/stdc++.h>`, mẫu "có tệp thì đọc tệp" như `code/SODU.cpp`, thụt 4 dấu cách, tên biến ngắn kiểu thi đấu,
  chú thích tiếng Việt ngắn, **mỗi dòng ≤ 76 kí tự**, dùng `long long`/`__int128` khi cần, không dùng tính năng C++17.
  Ngây thơ phải ĐÚNG (chỉ chậm), trừ khi bài cố ý minh họa lỗi (tràn số...) — khi đó ghi rõ trong text và loại khỏi đối chiếu.
- Ví dụ trong `examples/` nhỏ, dễ chạy tay; ví dụ 1 chính là ví dụ dùng cho bảng chạy tay.
- `verify/chN.py`: mỗi bài toán chính phải có `gen` (test nhỏ + vừa, cả trường hợp biên) và đối chiếu ngây thơ ↔ tối ưu
  (và `brute` Python nếu được). Chạy `verify/run.py` phải in OK cho mọi bài.
- Hình: dùng bảng màu trong `figs/figlib.py` (NAVY, RED, GREEN, AMBER, TEAL, PURPLE...), kiểu ô `cellbox` trong `shlib.py`:
  ô vàng viền đỏ = đang xét/kết quả, xanh dương = đã xong, cam nhạt = dữ liệu vào, xám = khởi tạo/đã loại.
  Chữ trong hình ≥ 9pt khi in ở bề rộng đã chọn; không để chữ đè lên nhau (kiểm tra bằng preview).
  Tên file hình: `f<số bài>_<tên>` (vd. `f6_sang`), sơ đồ khối `f6_ngaytho`, `f6_toiuu` bằng `flow()` trong `figs/flow.py`
  (xem cách gọi ở cuối `figs/ch1.py`: các bước 'term','io','proc','dec'(có nhánh),'loop' ... 'end').
- Mỗi bài học bắt đầu trang mới (tự động). Không viết tiêu đề "Bẫy thường gặp/Ghi nhớ/Luyện tập" thủ công.

## 5. Đề cương (20 bài, đánh số liên tục)

### Chương 1. CHIA HẾT VÀ ƯỚC SỐ
1. Phép chia có dư và đồng dư — SODU (xong, làm mẫu).
2. Ước số: liệt kê, đếm, tính tổng — DEMUOC: n ≤ 10^12^, in số ước và tổng các ước. Ngây thơ O(n) → cặp ước (d, n/d), d ≤ √n.
   Mở rộng: liệt kê ước tăng dần; số ước của mọi số 1..N bằng "sàng điều hòa" O(N log N); số hoàn hảo.
3. Ước chung lớn nhất và bội chung nhỏ nhất — UCLN: gcd của 2 số ≤ 10^18^ (rồi dãy). Ngây thơ thử giảm dần → Euclid,
   chứng minh, số bước (Lamé, Fibonacci), lcm tránh tràn (a / gcd · b). Mở rộng: gcd dãy, gcd đoạn con, phép trừ/chẵn lẻ (binary gcd).
4. Thuật toán Euclid mở rộng và phương trình ax + by = c — PTNGUYEN. Ngây thơ thử x → Bézout, Euclid mở rộng (chạy tay bảng),
   họ nghiệm, đếm nghiệm không âm.

### Chương 2. SỐ NGUYÊN TỐ
5. Số nguyên tố và kiểm tra nguyên tố — KTNT: Q ≤ 10^4^ số ≤ 10^12^, trả lời có nguyên tố không. Ngây thơ thử 2..n−1 → √n
   (chứng minh: hợp số có ước ≤ √n), bỏ số chẵn, 6k ± 1. Mở rộng: Miller–Rabin cho 10^18^ (code ngắn, cơ sở cố định), vô số số nguyên tố (Euclid).
6. Sàng Eratosthenes — DEMNT: Q ≤ 10^6^ truy vấn đếm số nguyên tố trong [a, b], b ≤ 10^7^. Ngây thơ kiểm tra từng số → sàng
   (hình lưới 1..100 qua từng lượt gạch), bắt đầu gạch từ p², độ phức tạp n log log n, mảng tiền tố. Mở rộng: sàng tuyến tính, sàng chỉ số lẻ / bitset.
7. Phân tích thừa số nguyên tố — PTTS: Q ≤ 10^5^ số ≤ 10^7^, in phân tích. Ngây thơ thử chia √n mỗi số → sàng ước nguyên tố nhỏ
   nhất (spf), phân tích O(log n). Hình cây phân tích. Định lí cơ bản của số học. Mở rộng: d(n), σ(n) từ phân tích; gcd/lcm theo số mũ;
   Legendre: số mũ của p trong n!, số chữ số 0 tận cùng của n!.
8. Sàng trên đoạn — SANGDOAN: đếm/liệt kê số nguyên tố trong [L, R], R ≤ 10^12^, R − L ≤ 10^6^. Ngây thơ √ từng số → sàng các
   p ≤ √R rồi gạch bội trong đoạn (bắt đầu từ max(p², ⌈L/p⌉·p)). Mở rộng: khoảng cách giữa hai số nguyên tố liên tiếp; đếm số không có ước nguyên tố nhỏ.

### Chương 3. SỐ HỌC ĐỒNG DƯ
9. Lũy thừa nhanh — LUYTHUA: a^b^ mod m, a, b, m ≤ 10^18^. Ngây thơ nhân b lần → bình phương liên tiếp (hình cây/bảng bit của b),
   bản đệ quy và vòng lặp, nhân tràn số (`__int128`, nhân Ấn Độ). Mở rộng: lũy thừa ma trận (giới thiệu), tổng cấp số nhân mod m.
10. Nghịch đảo mô-đun — CHIAMOD: Q truy vấn (a / b) mod p, p nguyên tố ~10^9^+7. Ngây thơ thử x từ 1..p−1 → Fermat nhỏ
    (chứng minh bằng hoán vị các số dư), Euclid mở rộng khi m không nguyên tố, điều kiện tồn tại gcd(b, m) = 1, nghịch đảo 1..n trong O(n).
11. Hàm phi Euler và định lí Euler — PHIEULER: φ(n), n ≤ 10^12^. Ngây thơ đếm gcd = 1 → công thức tích (1 − 1/p), sàng φ cho 1..N.
    Định lí Euler, rút gọn số mũ a^(b^c) mod m (m nguyên tố). Mở rộng: Σ_{d|n} φ(d) = n; đếm phân số tối giản.
12. Định lí số dư Trung Hoa — CRT: hệ x ≡ a~i~ (mod m~i~), k ≤ 10, m~i~ ≤ 10^9^ (không nhất thiết nguyên tố cùng nhau), x nhỏ nhất ≤ 10^18^
    hoặc −1. Ngây thơ duyệt x (nhảy theo bước m~1~) → gộp từng cặp bằng Euclid mở rộng. Mở rộng: bài toán "Hàn Tín điểm binh".

### Chương 4. TỔ HỢP VÀ ĐẾM
13. Tổ hợp và hệ số nhị thức — TOHOP: Q ≤ 10^5^ truy vấn C(n, k) mod 10^9^+7, n ≤ 10^6^. Ngây thơ tam giác Pascal O(n²) → giai
    thừa + nghịch đảo giai thừa. Hình tam giác Pascal. Mở rộng: chia kẹo Euler (stars and bars), định lí Lucas (p nhỏ, n ≤ 10^18^).
14. Nguyên lí bù trừ — BUTRU: đếm số trong [1, N] (N ≤ 10^18^) chia hết cho ít nhất một trong k ≤ 20 số a~i~. Ngây thơ duyệt
    1..N → bù trừ 2^k^ tập con với lcm (chặn tràn khi lcm > N). Hình Venn. Mở rộng: đếm số nguyên tố cùng nhau với n trong [1, N]; số hoán vị không điểm cố định (derangement).
15. Dãy truy hồi và lũy thừa ma trận — FIBO: F~n~ mod m, n ≤ 10^18^. Ngây thơ lặp n lần → ma trận [[1,1],[1,0]]^n^.
    Mở rộng: truy hồi tuyến tính bậc k, đếm đường đi độ dài n trên đồ thị nhỏ, chu kì Pisano, số Catalan.
16. Kĩ thuật chia khối ⌊n/i⌋ — TONGUOC: tính S(n) = Σ_{i=1}^{n}⌊n/i⌋ (= tổng số ước của 1..n), n ≤ 10^12^. Ngây thơ O(n) →
    ⌊n/i⌋ chỉ có ≤ 2√n giá trị, gom khối [i, n/(n/i)]. Hình bậc thang. Mở rộng: Σ i·⌊n/i⌋ (tổng σ), Σ n mod i.

### Chương 5. KĨ THUẬT SỐ HỌC TRONG LẬP TRÌNH
17. Số nguyên lớn — GIAITHUA: in chính xác n!, n ≤ 2000. Ngây thơ `unsigned long long` tràn từ 21! → mảng chữ số, nhân với số nhỏ,
    cơ số 10^9^ để nhanh. Mở rộng: cộng, trừ, nhân hai số lớn, so sánh, chia số lớn cho số nhỏ.
18. Hệ cơ số và biểu diễn nhị phân — DEMBIT: tổng số bit 1 của các số 1..n, n ≤ 10^18^. Ngây thơ đếm từng số → đếm theo từng
    bit (chu kì 2^k+1^). Đổi cơ số, phép toán bit. Mở rộng: cơ số −2, XOR 1..n theo n mod 4, liệt kê tập con bằng bit.
19. Tổng tiền tố và số dư — DOANCHIA: đếm đoạn con có tổng chia hết cho k (n ≤ 10^6^, a~i~ có thể âm). Ngây thơ O(n²) →
    S[r] ≡ S[l−1] (mod k), đếm theo số dư. Mở rộng: nguyên lí Dirichlet (luôn có đoạn con chia hết cho n), tìm chu kì dãy x~i+1~ = f(x~i~) mod m.
20. Điểm nguyên và hình học số nguyên — DIEMNGUYEN: số điểm nguyên trên đoạn thẳng nối hai điểm nguyên (tọa độ ≤ 10^9^).
    Ngây thơ duyệt x → gcd(|dx|, |dy|) + 1. Mở rộng: công thức diện tích (shoelace), định lí Pick đếm điểm bên trong đa giác.
