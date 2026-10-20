# TỪ ĐIỂN CHỈ SỐ — ĐỊNH NGHĨA BẰNG CÔNG THỨC
Version 1.0 · dùng cho mọi MODE

> **Lý do file này đứng đầu:** hai người cãi nhau về CPL suốt một tháng, cuối cùng phát hiện một người tính CPL = chi/lead-Meta, người kia tính CPL = chi/lead-CRM-đã-lọc-rác. **Không thống nhất định nghĩa thì mọi báo cáo phía sau đều vô nghĩa.**

---

## 1 · Tám tầng phễu và chỉ số của từng tầng

| # | Tầng | Chỉ số | Công thức | Nguồn |
|---|---|---|---|---|
| ① | Chi phí | **Chi tiêu** | tổng `spend` | Meta |
| | | **Pacing %** | chi thực tế ÷ (ngân sách tháng × số ngày đã qua ÷ số ngày trong tháng) | Meta + mục tiêu |
| ② | Hiển thị | **CPM** | chi ÷ impression × 1.000 | Meta |
| | | **Frequency** | impression ÷ reach | Meta |
| ③ | Click | **CTR** | click ÷ impression | Meta |
| | | **CPC** | chi ÷ click | Meta |
| ④ | Inbox | **CPI** | chi ÷ số hội thoại tin nhắn bắt đầu | Meta |
| | | **Click→Inbox %** | inbox ÷ click | Meta |
| ⑤ | Lead | **CPL** | **chi ÷ lead hợp lệ** | Meta(chi) + CRM(lead) |
| | | **Inbox→Lead %** | lead ÷ inbox | CRM |
| | | **% lead rác** | lead loại ÷ tổng lead thô | CRM |
| ⑥ | Booking | **CPB** | chi ÷ booking | Meta + CRM |
| | | **Lead→Booking %** | booking ÷ lead hợp lệ | CRM |
| ⑦ | Đến | **Show-rate** | đến ÷ booking | CRM |
| ⑧ | Chốt | **CAC** | chi ÷ ca chốt | Meta + ERP |
| | | **Đến→Chốt %** | ca chốt ÷ lượt đến | ERP |
| | | **ROAS** | doanh thu ÷ chi | ERP |

---

## 2 · Bốn định nghĩa phải chốt một lần, bằng văn bản

### ① "Lead" là gì?
**Mặc định của bộ agent này: lead = một liên hệ có SĐT dùng được + có dịch vụ quan tâm, đã qua lọc rác.**

⛔ **Lead-Meta ≠ Lead-CRM.** Meta đếm `lead`/`messaging conversation started`; CRM đếm liên hệ đã kiểm. Chênh 15–30% là bình thường, **>30% là mã E** (xem `ar-nguong-bat-thuong.md`).
Báo cáo gửi ban lãnh đạo **luôn dùng lead-CRM**. Báo cáo tối ưu trong ngày của adnet có thể dùng lead-Meta vì nó về nhanh hơn — nhưng **phải ghi rõ đang dùng loại nào**.

### ② "Lead rác" là gì?
Phải liệt kê thành **danh sách lý do đóng được**, không để "cảm thấy rác":
`số sai/không liên lạc được sau 3 lần` · `không có nhu cầu – bấm nhầm` · `spam/trêu` · `sai khu vực (không có cơ sở phục vụ)` · `sai độ tuổi (<18 không có người giám hộ)` · `trùng với lead đã có trong 30 ngày` · `đối thủ/ứng viên xin việc`.
Mỗi lý do là **một mã riêng**, vì chúng chỉ về **những tầng rò khác nhau**: *sai khu vực* là lỗi targeting (tầng ②), *bấm nhầm* là lỗi creative/placement (tầng ③), *trùng* là lỗi loại trừ tệp (tầng ②).

### ③ "Booking" là gì?
**Lịch hẹn có ngày–giờ–cơ sở cụ thể và khách đã xác nhận.** "Khách nói để em sắp xếp rồi báo lại" **không phải booking**. Đếm nhầm chỗ này làm show-rate trông thảm hại trong khi vấn đề nằm ở định nghĩa.

### ④ Mốc quy ngày
**Quy về ngày phát sinh CHI PHÍ, không phải ngày lead được xử lý.** Lead hôm nay đến từ chi phí hôm nay; nếu CRM ghi ngày telesales gọi thì CPL sẽ lệch 1–3 ngày và mọi so sánh ngày đều sai.
Cửa sổ attribution mặc định: **7 ngày click / 1 ngày view**. Đổi cửa sổ thì **mọi số lịch sử phải tính lại**, không so trực tiếp số cũ với số mới.

---

## 3 · Chỉ số nào dùng để làm gì

| Mục đích | Chỉ số chính | Chỉ số phụ để tách nguyên nhân |
|---|---|---|
| Ads có đang đắt lên không? | **CPL** | tách thành **CPM × 1/CTR × 1/(click→inbox) × 1/(inbox→lead)** |
| Creative còn sống không? | **CTR** + **frequency** | CPM (loại yếu tố đấu giá) |
| Tệp có bão hoà không? | **frequency** + CTR trôi dần | reach mới / reach tổng |
| Lead có thật không? | **% lead rác** | lead→booking % |
| Tiền có chảy đúng chỗ không? | **share ngân sách vs share lead** | CPL theo ZONE |
| Đội có phản ứng kịp không? | **số ngày chỉ số xấu không có thao tác** | nhật ký thay đổi |

### Công thức phân rã CPL — dùng mỗi khi CPL tăng
```
CPL = CPM/1000 ÷ (CTR × click→inbox% × inbox→lead%)
```
**Luôn phân rã trước khi kết luận.** CPL tăng 40% có bốn nguyên nhân hoàn toàn khác nhau, và bốn người khác nhau xử lý:

| Thành phần xấu đi | Nghĩa là | Ai xử |
|---|---|---|
| **CPM** tăng | đấu giá đắt lên / tệp hẹp / mùa cao điểm | Adnet (tệp, bid, lịch) |
| **CTR** giảm | hook/creative yếu hoặc bão hoà | Adnet (creative) |
| **click→inbox** giảm | điểm đến hỏng: landing chậm, lời chào tự động lỗi, form lỗi | Adnet + Kỹ thuật |
| **inbox→lead** giảm | **trực page** — chậm trả lời, kịch bản sai, thiếu người ca tối | **Trực page** |

⛔ Không có bước phân rã này thì mọi cảnh báo CPL đều chỉ là *"CPL tăng, xem lại đi"* — vô dụng.

---

## 4 · Quy ước ghi số trong mọi output
- Tiền: `412k` · `18,2tr` · `1,25 tỷ`. Không ghi `412000`.
- Tỷ lệ: 1 chữ số thập phân — `1,8%`, không `1,83721%`.
- Lệch: luôn ghi **cả % và số tuyệt đối** — `+40% (295k → 412k)`.
- Cỡ mẫu: luôn đi kèm — `(37 lead / 18,2tr)`.
- Kỳ: ghi rõ `07–13/10` chứ không ghi "tuần này".
