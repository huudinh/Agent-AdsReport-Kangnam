# 02 · CÂU LỆNH — công thức ra lệnh từng mode

---

## Công thức chung

```
MODE [số] + KỲ + DỮ LIỆU + SỰ KIỆN ĐÃ BIẾT + MỤC TIÊU
```

Hai thành phần hay bị bỏ và chính chúng quyết định chất lượng câu trả lời:

| Bỏ cái gì | Hậu quả |
|---|---|
| **Sự kiện đã biết** | Baseline sai → agent bắn báo động giả cho mỗi dịp lễ và mỗi lần hết khuyến mãi |
| **Nhật ký thay đổi** | Mọi câu "vì sao CPL tăng" chỉ còn là tương quan, không phải nguyên nhân |

---

## Năm mode — input tối thiểu

| Mode | Gõ gì | Input tối thiểu |
|---|---|---|
| **1 · DASHBOARD** | `MODE 1` + kỳ + dữ liệu | bảng số theo ngày |
| **2 · CẢNH BÁO** | `MODE 2` + dữ liệu | bảng số theo ngày × ad set, ≥ 14 ngày |
| **3 · NHÂN SỰ** | `MODE 3` + kỳ + dữ liệu | bảng có cột nhân viên |
| **4 · NGÂN SÁCH** | `MODE 4` + ngân sách + mục tiêu | ngân sách tháng + CPL mục tiêu |
| **5 · SPEC** | `MODE 5` + hiện trạng hệ thống | mô tả nguồn số đang có |

Không gọi mode thì agent **tự suy và nói rõ đã chọn mode nào**.

---

## Mười hai câu nói lời thường — dùng được ngay

Không cần nhớ mã mode. Agent tự suy.

**Nhóm "có chuyện gì không"**
```
1. Tuần này có gì bất thường không? Dữ liệu đây.
2. Cho mình ba việc đáng làm nhất sáng mai, xếp theo thiệt hại nếu không làm.
3. Tuần này tệ hơn tuần trước thật, hay chỉ do lệch ngày cuối tuần?
```

**Nhóm "lỗi của ai"**
```
4. CPL ZONE Mũi tăng 38%. Xấu ở thành phần nào, ai phải xử lý?
5. Booking giảm mà inbox tăng. Tầng rò nằm ở đâu?
6. Lead nhiều hơn mà chốt ít hơn. Lead rác hay tư vấn?
```

**Nhóm "quyết định"**
```
7. Ad set này CPL cao gấp rưỡi, nên tắt hay nên sửa? Dữ liệu 10 ngày đây.
8. Mình định tăng ngân sách từ 10tr lên 25tr/ngày. Có nên không?
9. ZONE nào đang bị bỏ đói dù CPL tốt?
```

**Nhóm "đội ngũ và hệ thống"**
```
10. Ad set nào đang để chỉ số xấu nhiều ngày mà không ai động vào?
11. Số lead Meta và CRM lệch 40%, nên tin số nào?
12. Muốn tiến tới cảnh báo tự động thì cần giải đề bài nào trước?
```

---

## Ba cách ra lệnh làm hỏng câu trả lời

| ❌ Hỏi thế này | Vì sao hỏng | ✅ Hỏi thế này |
|---|---|---|
| *"Phân tích file này giúp mình"* | Không có kỳ, không có mục tiêu, không có sự kiện → agent phải hỏi lại hoặc đoán | *"MODE 2, kỳ 07–13/10, mục tiêu CPL Mũi 420k, trong kỳ có khuyến mãi từ 08/10"* |
| *"Ad này tốt hay xấu?"* | Thiếu mốc so sánh | *"Ad này so với median 7 ngày của chính nó thì thế nào?"* |
| *"Ai chạy kém nhất tháng này?"* | Ra một cái tên và một cuộc trò chuyện khó, không ra việc sửa được | *"Ad set nào bị bỏ rơi lâu nhất? Ngân sách lớn nhất đang nằm ở người CPL tốt hay kém?"* |

---

## Mẹo: luôn hỏi ngược lại agent một câu

Sau khi nhận cảnh báo, hỏi:
```
Nếu chẩn đoán này sai thì nó sai ở đâu? Cách kiểm rẻ nhất là gì?
```
Agent sẽ nêu giả thuyết thay thế và phép kiểm tốn ít tiền nhất. Nhiều lần, phép kiểm 10 phút đó đã loại được một kế hoạch sửa kéo dài hai ngày.
