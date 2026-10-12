// SỐ HỌC — TẬP 2. CHƯƠNG 1. CHIA HẾT VÀ ƯỚC SỐ
const L1 = {
  no: 1, title: 'Phép chia có dư và đồng dư',
  recap: [
    '**Phép chia có dư:** a = b · q + r với 0 ≤ r < b. Trong C++, `a % b` mang dấu của a; số dư không âm là `((a % m) + m) % m`.',
    '**Đồng dư:** a ≡ b (mod m) khi m chia hết a − b. Đồng dư giữ nguyên qua cộng, trừ, nhân và lũy thừa: được thay một số bằng số dư của nó ở bất kì bước nào.',
    '**Sơ đồ Horner:** đọc số từ trái sang phải, r ← (r · 10 + c) mod m cho số dư của số rất lớn trong O(độ dài).',
    'Chỉ có hữu hạn số dư, nên mọi dãy số dư "tính từ số dư trước" sớm muộn đều **lặp lại tuần hoàn**.',
  ],
  problems: [
    {
      id: '1.1', name: 'NGÀY TRONG TUẦN', code: 'NGAYTHU', level: 1, topic: 'Phép chia có dư với số âm, đồng dư theo mô-đun 7 (Tập 1, Bài 1).',
      skill: 'Lấy số dư không âm; tránh vòng lặp đếm từng ngày.',
      statement: [
        'Người Việt gọi các ngày trong tuần là thứ Hai, thứ Ba, ..., thứ Bảy và Chủ nhật. Trong bài này ta viết chúng lần lượt bằng các số **2, 3, 4, 5, 6, 7** và **8** (số 8 là Chủ nhật).',
        'Bạn An có Q câu hỏi. Câu hỏi thứ i cho biết hôm nay là thứ t và một số nguyên k: nếu k > 0, An muốn biết **k ngày nữa** là thứ mấy; nếu k < 0, An muốn biết **|k| ngày trước** là thứ mấy; nếu k = 0 thì đó chính là hôm nay.',
        'Hãy trả lời mọi câu hỏi của An.',
      ],
      input: ['Dòng đầu chứa số nguyên Q. Mỗi dòng trong Q dòng tiếp theo chứa hai số nguyên t và k.'],
      output: ['Gồm Q dòng, dòng thứ i là thứ (một số từ 2 tới 8) ứng với câu hỏi thứ i.'],
      limits: ['1 ≤ Q ≤ 10^5^;  2 ≤ t ≤ 8;  |k| ≤ 10^18^.'],
      subtasks: [[30, '0 ≤ k ≤ 10^6^.'], [30, 'k ≥ 0.'], [40, 'Không có ràng buộc gì thêm.']],
      examples: [
        { explain: ['1000 = 7 · 142 + 6: sau 1000 ngày, thứ Hai tiến thêm 6 ngày là **Chủ nhật** (8).', '−100 = 7 · (−15) + 5: 100 ngày trước thứ Hai là **thứ Bảy** (7).', '10^18^ chia 7 dư 1: **thứ Ba** (3).'] },
        { explain: ['k = 0: chính hôm nay, Chủ nhật.', 'Một tuần trước thứ Năm vẫn là **thứ Năm**.'] },
      ],
      after: [{ fig: 'ngaythu', w: 6.2, cap: 'Mỗi ngày là một "ngăn" trên vòng tròn 7 ngăn; đi k bước theo chiều kim đồng hồ (k < 0: ngược chiều).' }],
      notes: ['Với k tới 10^18^, vòng lặp "đếm từng ngày" chạy cả nghìn năm. Chỉ có 7 kết quả có thể xảy ra: hãy dùng phép chia có dư.',
        'Trong C++, `-100 % 7` bằng −2. Nếu em in thẳng (t − 2 + k) % 7 + 2 thì có thể ra số 0 hoặc số âm.',
        'Biểu thức t − 2 + k vẫn nằm trong phạm vi `long long`, nhưng nếu em cộng thêm 7 · 10^18^ "cho chắc chắn dương" thì sẽ tràn số.'],
      hints: ['Đánh số lại các ngày: thứ Hai là 0, ..., Chủ nhật là 6. Khi đó câu trả lời là (d + k) mod 7, rồi đổi ngược lại.',
        'Số dư không âm trong C++: `((x % 7) + 7) % 7`.'],
    },
    {
      id: '1.2', name: 'CHỮ SỐ CUỐI', code: 'CHUSOCUOI', level: 2, topic: 'Đồng dư theo mô-đun 10, tính tuần hoàn của lũy thừa, số dư của số rất lớn (Tập 1, Bài 1).',
      skill: 'Tìm chu kì của dãy số dư; xử lí số cho dưới dạng xâu.',
      statement: [
        'Thầy giáo viết lên bảng hai số tự nhiên a và b **rất lớn**, mỗi số có tới một trăm nghìn chữ số, rồi hỏi: "Chữ số tận cùng của a^b^ là chữ số nào?"',
        'Không máy tính nào tính nổi a^b^ (nó có thể có tới 10^100000^ chữ số!). Nhưng chỉ cần chữ số cuối, em có trả lời được không? Quy ước 0^0^ = 1.',
      ],
      input: ['Dòng đầu chứa số nguyên T là số câu hỏi. Mỗi dòng trong T dòng tiếp theo chứa hai số tự nhiên a và b, viết trong hệ thập phân, không có chữ số 0 thừa ở đầu.'],
      output: ['Gồm T dòng, mỗi dòng một chữ số là chữ số tận cùng của a^b^.'],
      limits: ['1 ≤ T ≤ 10;  a và b có không quá 10^5^ chữ số.'],
      subtasks: [[20, 'a, b ≤ 10^6^.'], [30, 'a, b ≤ 10^18^.'], [50, 'Không có ràng buộc gì thêm.']],
      examples: [
        { explain: ['2^2026^: dãy chữ số cuối của 2^b^ là 2, 4, 8, 6 lặp lại; 2026 chia 4 dư 2 nên chữ số cuối giống 2^2^ = 4.', '7^3^ = 343.', 'Quy ước 0^0^ = 1.'] },
        { explain: ['Chữ số cuối của a là 9; dãy 9, 1, 9, 1, ... có chu kì 2. Số mũ chẵn nên đáp số là **1**.'] },
      ],
      after: [{ fig: 'chusocuoi', w: 6.0, cap: 'Chữ số tận cùng của a^b^ chỉ phụ thuộc vào chữ số cuối của a và lặp lại tuần hoàn theo b; ô vàng là một chu kì.' }],
      notes: ['a và b phải đọc vào **xâu**: 10^5^ chữ số vượt xa mọi kiểu số nguyên.',
        'Cẩn thận khi b chia hết cho 4: số dư là 0 nhưng chữ số cuối ứng với số mũ 4 (chẳng hạn 2^4^ = 16 tận cùng 6, không phải 2^0^ = 1). Riêng b = 0 thì đáp số là 1.',
        'Đừng quên trường hợp a = 0 với b > 0 (đáp số 0).'],
      hints: ['Chữ số tận cùng của a^b^ là a^b^ mod 10, và theo tính chất đồng dư, chỉ phụ thuộc vào a mod 10.',
        'Nhìn bảng ở hình: mọi chu kì đều là ước của 4. Vậy chỉ cần biết b mod 4, mà số dư của một số rất lớn thì tính được bằng sơ đồ Horner (hoặc chỉ cần hai chữ số cuối, vì 100 chia hết cho 4).'],
    },
    {
      id: '1.3', name: 'VIẾT LIỀN', code: 'VIETLIEN', level: 3, mem: '64 MB', topic: 'Sơ đồ Horner theo từng khối chữ số, lũy thừa của 10 theo mô-đun (Tập 1, Bài 1).',
      skill: 'Mở rộng sơ đồ Horner cho những "chữ số" có độ dài thay đổi; tiết kiệm bộ nhớ.',
      statement: [
        'Bé Na tập viết số. Bé viết liền nhau các số tự nhiên từ 1 tới n, không có dấu cách, được một số rất dài. Chẳng hạn với n = 12, bé viết được số **123456789101112**.',
        'Hãy cho biết số mà bé Na viết được chia cho m dư bao nhiêu.',
      ],
      input: ['Một dòng chứa hai số nguyên n và m.'],
      output: ['Một số nguyên là số dư cần tìm.'],
      limits: ['1 ≤ n ≤ 10^7^;  1 ≤ m ≤ 10^9^.'],
      subtasks: [[30, 'n ≤ 9.'], [30, 'n ≤ 1000.'], [40, 'Không có ràng buộc gì thêm.']],
      examples: [
        { explain: ['123456789101112 = 1000 · 123456789101 + 112.'] },
        { explain: ['Số 123456789101112131415 chia 7 dư 2.'] },
      ],
      after: [{ fig: 'vietlien', w: 6.4, cap: 'Viết thêm số i vào bên phải giống như "dịch trái" phần đã viết đi số chữ số của i rồi cộng i.' }],
      notes: ['Với n = 10^7^, số bé Na viết có 68 888 897 chữ số. Lưu cả xâu ấy đã tốn khoảng 69 MB, vượt giới hạn bộ nhớ 64 MB của bài.',
        'r · 10^k^ với r < m ≤ 10^9^ và 10^k^ mod m < 10^9^ có thể tới 10^18^: vẫn vừa `long long`, nhưng không vừa `int`.',
        'Đừng tính lũy thừa của 10 bằng `pow`: gọi k là số chữ số của i, hãy duy trì 10^k^ mod m và chỉ cập nhật khi i tăng thêm một chữ số (i = 10, 100, 1000, ...).'],
      hints: ['Ở bài SODU (Tập 1, Bài 1), mỗi bước thêm **một** chữ số: r ← r · 10 + c. Ở đây mỗi bước thêm cả **một số** i có k chữ số: r ← r · 10^k^ + i.',
        'Từ 1 tới 9 ta nhân 10, từ 10 tới 99 nhân 100, ... Số chữ số chỉ thay đổi 7 lần với n ≤ 10^7^.'],
    },
  ],
};

module.exports = {
  no: 1, title: 'CHIA HẾT VÀ ƯỚC SỐ',
  intro: 'Mười hai bài tập đầu tiên rèn luyện những kĩ năng nền móng của số học trong lập trình: lấy số dư (kể cả với số âm và số rất lớn), duyệt ước tới √n, thuật toán Euclid và Euclid mở rộng. Các bài không khó về ý tưởng, nhưng rất nhiều "bẫy" nhỏ đang chờ: tràn số, số dư âm, đếm trùng, trường hợp n = 1... Hãy đọc kĩ khung CHÚ Ý của từng bài.',
  advice: ['Trước khi code, hãy ghi ra giá trị lớn nhất của mọi đại lượng (tích, tổng, BCNN...) để chọn đúng kiểu dữ liệu.', 'Số cho dưới dạng xâu thì xử lí theo từng chữ số; đừng cố đổi ra kiểu số.', 'Với mỗi bài, tự tạo vài test "góc": n = 1, số nguyên tố, số chính phương, số âm, số 0.'],
  lessons: [L1],
};
