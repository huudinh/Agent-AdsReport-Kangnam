# CÂY CHẨN ĐOÁN — TRIỆU CHỨNG → TẦNG RÒ → NGUYÊN NHÂN → AI XỬ LÝ
Version 1.0 · dùng cho MODE 2 (ô ④ ⑤ ⑥ của phiếu cảnh báo)

> Cảnh báo chỉ nói **có chuyện gì đó**. File này nói **chuyện gì, của ai, và sửa cái gì**. Không có bước này thì agent chỉ là một cái báo động khói.

---

## 0 · Quy trình chẩn đoán — 5 bước, không bỏ bước

```
① Quét nhóm E  →  số có tin được không?   (không → dừng, báo kỹ thuật)
② Phân rã CPL  →  thành phần nào xấu đi?  (CPM / CTR / click→inbox / inbox→lead)
③ Định vị tầng rò  →  tầng ĐẦU TIÊN lệch chuẩn, đi từ trên xuống
④ Tách "chất lượng vào" vs "năng lực xử lý"
⑤ Kiểm nhóm G  →  có phải mùa vụ / cuối tuần / hết khuyến mãi không?
```

Bước ⑤ đứng cuối là có chủ ý: kiểm mùa vụ **sau khi** đã định vị tầng rò, nếu không sẽ lấy "tại mùa" ra giải thích cho mọi thứ và không ai phải sửa gì cả.

---

## 1 · Bảng triệu chứng lõi

| Triệu chứng số liệu | Tầng rò | Chẩn đoán khả dĩ (xếp theo xác suất) | Ai xử lý | Hành động cụ thể |
|---|---|---|---|---|
| **CPM ↑ · CTR giữ · CPL ↑** | ② | ① đấu giá đắt lên (kiểm **G-04**) · ② tệp hẹp dần · ③ trùng tệp giữa ad set (**E-06**) | Adnet | Mở rộng/tách tệp theo vùng · hạ trần bid · gộp ad set trùng |
| **CTR ↓ · CPM giữ** | ③ | ① creative bão hoà (**D-01**) · ② hook sai giai đoạn phễu · ③ tệp lệch | Adnet | Bật challenger mới · đổi hook, giữ nguyên tệp để đọc được kết quả |
| **CTR ↑ · click→inbox ↓** | ④ | ① điểm đến hỏng (**E-07**) · ② lời chào tự động lỗi/chậm · ③ creative hứa một đằng, trang nói một nẻo | Adnet + Kỹ thuật | Bấm thử đúng luồng khách trên **điện thoại thật** · kiểm welcome message · đối chiếu lời hứa |
| **Inbox ↑ · lead ↓** | ⑤ | ① **chậm phản hồi lần đầu** · ② thiếu ca trực tối/cuối tuần · ③ kịch bản xin số quá sớm · ④ inbox toàn người hỏi giá rồi im | **Trực page** | Đo thời gian phản hồi lần đầu theo khung giờ · xếp lại ca · sửa điểm xin số trong kịch bản |
| **Lead ↑ · booking ↓** | ⑥ | ① lead rác (kiểm **C-01** trước) · ② telesales gọi chậm > 2h · ③ không có khung giờ hẹn khách muốn · ④ giá nói qua điện thoại làm khách rụng | **Telesales** | Tách lead rác ra khỏi mẫu rồi tính lại · đo độ trễ cuộc gọi đầu · rà kịch bản chốt lịch |
| **Booking ↑ · đến ↓** | ⑦ | ① không nhắc lịch · ② hẹn quá xa ngày · ③ cơ sở xa khách · ④ khách hẹn cho có để thoát cuộc gọi | **Lễ tân / CSKH** | Bật nhắc T-1 ngày và T-2h · rút ngắn khoảng cách hẹn · kiểm chất lượng booking ở tầng ⑥ |
| **Đến ↑ · chốt ↓** | ⑧ | ① lệch kỳ vọng giá do quảng cáo nói thiếu · ② tư vấn viên mới · ③ khách đến chỉ để hỏi | Tư vấn tại cơ sở | Đối chiếu thông điệp giá trên ad với giá tư vấn · rà ca tư vấn |
| **Mọi chỉ số bình thường, lead vẫn ít** | ① | ① **chi hụt (A-05)** · ② cháy ngân sách sớm (**A-06**) · ③ ad set đang học lại | Adnet | Kiểm ngân sách thực chi vs đặt · kiểm giờ hết tiền · kiểm nhật ký thay đổi 3 ngày qua |

**Mỗi dòng khi xuất phải kèm đủ 4 thứ:** ① ngưỡng cụ thể đang vi phạm · ② lý do dựa trên số · ③ hành động tiếp theo · ④ **chỉ số cần theo dõi sau khi sửa**.

---

## 2 · Bốn cặp dễ chẩn đoán nhầm nhất

### ① "CPL tăng" ≠ "quảng cáo kém đi"
CPL là **tích của bốn tỷ lệ** (`ar-tu-dien-chi-so.md` §3). Ba trong bốn thành phần nằm ngoài tay Ads sau tầng ④.
**Cách kiểm trong 30 giây:** tính CPI (chi/inbox). CPI giữ nguyên mà CPL tăng → **toàn bộ vấn đề nằm từ tầng ⑤ trở xuống**, Ads không phải sửa gì.

### ② "Lead rác nhiều" ≠ "trực page lọc ẩu"
Rác do **sai khu vực / sai độ tuổi / spam** là lỗi **targeting tầng ②**. Rác do **không liên lạc được** mới có thể là lỗi tầng ⑤.
→ Luôn hỏi: *"Rác theo lý do nào?"* trước khi gán người.

### ③ "Ad set này CPL cao → tắt đi"
Trước khi tắt phải trả lời: **đã đủ mẫu chưa** (cổng §4①) · **đang trong learning phase không** · **có phải nó đang gánh tệp mà ad set khác không chạm tới không**.
Tắt một ad set CPL cao nhưng đang mở tệp mới = tháng sau cả tài khoản bão hoà. **Tắt là quyết định không hoàn tác được trong ngắn hạn** vì bật lại phải học lại từ đầu.

### ④ "Tuần này tệ hơn tuần trước"
Kiểm trước ba thứ, theo đúng thứ tự: **số ngày cuối tuần trong hai kỳ có bằng nhau không** · **kỳ nào có khuyến mãi** · **kỳ nào có ngày lễ**.
Ba thứ này giải thích phần lớn các "biến động bí ẩn" theo tuần của ngành thẩm mỹ.

---

## 3 · Khi không tách được nguyên nhân

Ghi **≥ 2 giả thuyết** kèm **cách kiểm rẻ nhất cho từng cái**, rồi giao việc **kiểm**, không giao việc **sửa**.

```
⑤ CHẨN ĐOÁN
   GT1 (60%) · Tệp bão hoà — frequency 2,8 (median 1,9), CTR trôi 3 ngày.
       Kiểm: tách 10% ngân sách sang tệp mới cùng creative, đọc CTR sau 48h.
   GT2 (40%) · Đấu giá đắt lên theo mùa — CPM +34% nhưng mới 1 ad set.
       Kiểm: đối chiếu CPM của 5 ad set khác cùng khu vực. Cùng tăng → G-04.
   → Chạy GT2 trước: tốn 0 đồng, có đáp án trong 10 phút.
```

**Luôn chạy giả thuyết rẻ trước**, kể cả khi nó ít khả năng hơn. Một phép đối chiếu 10 phút loại được 40% khả năng là món hời so với một thử nghiệm 48h.

---

## 4 · Mẫu câu kết cho mỗi phiếu

> **"Chỉ số cần theo dõi: `[chỉ số]` · kỳ vọng về `[mức]` trong `[số]` ngày. Không đạt thì quay lại giả thuyết `[GT2]`."**

Câu này biến cảnh báo thành **một vòng lặp đóng**: có hành động, có mốc, có phương án B. Thiếu nó thì mọi cảnh báo đều kết thúc bằng *"đã xem"* và không ai biết việc sửa có tác dụng không.
