# TRI THỨC — Agent AdsReport Kangnam
> File này gộp **9 module tri thức** từ `knowledge/`. Sinh tự động ngày 2026-10-22 bằng `python tools/gop-tham-khao.py`.
> ⛔ **Không sửa file này** — sửa ở bản rời trong thư mục nguồn rồi chạy lại lệnh trên.

**Cách đọc:** mỗi phần bắt đầu bằng dòng `===== tên file =====` và là **một đơn vị tri thức riêng**. Tham chiếu dạng `[[tên-file]]` trong văn bản trỏ tới **phần cùng tên ngay trong file này**, không phải file bên ngoài.

## MỤC LỤC

| # | File | Cỡ |
|---|---|---|
| 1 | `ar-cay-chan-doan.md` | 6.6 KB |
| 2 | `ar-hieu-qua-nhan-vien.md` | 5.8 KB |
| 3 | `ar-ho-so-van-hanh.md` | 7.0 KB |
| 4 | `ar-khung-bao-cao.md` | 6.7 KB |
| 5 | `ar-nguong-bat-thuong.md` | 12.5 KB |
| 6 | `ar-quan-ly-ngan-sach.md` | 5.5 KB |
| 7 | `ar-rao-phap-ly.md` | 5.7 KB |
| 8 | `ar-schema-du-lieu.md` | 8.9 KB |
| 9 | `ar-tu-dien-chi-so.md` | 5.7 KB |


===== ar-cay-chan-doan.md =====

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


===== ar-hieu-qua-nhan-vien.md =====

# HIỆU QUẢ NHÂN VIÊN ADNET — 5 TRỤC CHẤM
Version 1.0 · dùng cho MODE 3

> **Mục đích của file này là tìm ra NGƯỜI CẦN GIÚP, không phải tìm ra người để trách.** Một bảng xếp hạng dùng sai sẽ dạy cả đội một bài học rất nhanh: chọn ZONE dễ, giữ ad set an toàn, không thử gì mới. Đó là cách giết đội Adnet bằng chính báo cáo của mình.

---

## 1 · Năm trục

| # | Trục | Đo bằng | Vì sao có mặt |
|---|---|---|---|
| ① | **Hiệu quả chi phí** | CPL so **median team cùng ZONE + cùng khu vực** | kết quả cuối |
| ② | **Chất lượng lead** | lead→booking % của lead người đó mang về | rẻ mà rác thì không phải rẻ |
| ③ | **Tốc độ phản ứng** | số **giờ** từ lúc chỉ số vượt ngưỡng đến thao tác đầu tiên | thứ duy nhất hoàn toàn trong tầm tay |
| ④ | **Kỷ luật thử nghiệm** | số challenger mới/tháng · số biến đổi mỗi lần | năng lực học, quyết định kết quả tháng sau |
| ⑤ | **Kỷ luật ngân sách** | pacing lệch % · số ngày cháy sớm / chi hụt | tiền không tiêu được cũng là tiền mất |

**Trục ③ có trọng số cao nhất khi kèm việc.** Trục ① phụ thuộc rất nhiều vào ZONE, mùa, tệp, ngân sách được giao — nhiều thứ không phải người chạy quyết. Trục ③ thì không có gì để đổ lỗi.

---

## 2 · Bốn luật công bằng — vi phạm thì bảng vô giá trị

### ① Chỉ so người **cùng ZONE · cùng khu vực · cùng tầm ngân sách**
Người chạy Mũi Hà Nội 300tr/tháng và người chạy Da liễu Cần Thơ 40tr/tháng **không nằm trên cùng một bảng**. Nếu team nhỏ không đủ người để so trong nhóm → **so người đó với chính mình ở kỳ trước**, và ghi rõ đang so kiểu đó.

### ② So với **median**, không so với người giỏi nhất
So với đỉnh thì 90% đội luôn "dưới chuẩn", và con số đó không nói lên điều gì ngoài việc có một người giỏi.

### ③ **Đủ mẫu mới xếp hạng**
Dưới ngưỡng cổng §4① của bộ não → ghi **"chưa đủ dữ liệu"**, ⛔ **không xếp cuối bảng**. Người mới vào, người vừa nhận ZONE mới, người đang chạy ngân sách nhỏ — xếp họ cuối bảng là một kết luận sai được trình bày như sự thật.

### ④ Tách phần **quyết được** và phần **không quyết được**
Trừ ra trước khi chấm: CPM tăng toàn ngành (**G-04**) · ngày lễ · hết khuyến mãi (**G-03**) · landing hỏng (**E-07**) · ZONE bị cắt ngân sách giữa kỳ · tài khoản bị hạn chế (**E-02**).
Không trừ những thứ này thì bảng xếp hạng đang chấm **thời tiết**, không chấm **người**.

---

## 3 · Mẫu bảng xuất

| Adnet | ZONE | Chi | Lead | CPL | vs median | Lead→Book | Phản ứng TB | Challenger/tháng | Pacing | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|---|
| A | Mũi-HN | 148tr | 302 | 490k | **+18%** | 31% | 9h | 3 | 102% | B-05 đang mở 2 ngày |
| B | Mũi-HN | 132tr | 338 | 390k | −6% | 36% | 4h | 5 | 98% | — |
| C | Mũi-HN | 41tr | 62 | 661k | — | — | — | 1 | 94% | **chưa đủ mẫu** (mới nhận 18/10) |

Cột **Ghi chú** quan trọng hơn cột CPL: nó cho trưởng nhóm biết **việc đang mở**, còn CPL chỉ cho biết **đã xảy ra chuyện gì**.

---

## 4 · Từ bảng số → hành động kèm việc

Mỗi người có chỉ số lệch phải ra được **một việc kèm cụ thể**, không phải một lời nhận xét:

| Trục lệch | Việc kèm |
|---|---|
| ① CPL cao, ③ phản ứng chậm | Đặt lịch rà ad set **mỗi 09:00 và 15:00**; bật quy tắc tự động báo khi CPL vượt ngưỡng |
| ① CPL cao, ③ phản ứng nhanh | Không phải vấn đề thao tác → **xem lại tệp/creative cùng trưởng nhóm**, có thể là ZONE khó |
| ② Lead rẻ nhưng booking thấp | Rà targeting + đối chiếu lời hứa trên ad với thực tế tư vấn |
| ④ Không có challenger | Giao chỉ tiêu **2 creative mới/tháng**, cấp sẵn brief từ agent nội dung |
| ④ Đổi 3 biến một lúc | Kèm quy tắc **1 biến/lô**, duyệt thay đổi trong 2 tuần |
| ⑤ Cháy ngân sách sớm | Kiểm lịch chạy + trần bid; chia ngân sách theo khung giờ |

---

## 5 · Ngôn ngữ — ranh giới một câu

| ✅ Viết thế này | ❌ Không viết thế này |
|---|---|
| "Ad set X để CPL vượt ngưỡng 5 ngày, nhật ký không ghi thao tác nào" | "Bạn A lười, không theo dõi" |
| "Phản ứng trung bình 9h, median team 4h" | "Bạn A chậm chạp, yếu năng lực" |
| "Chưa đủ dữ liệu để kết luận về C" | "C đứng cuối bảng" |

**Nói về hành vi và số liệu đo được, không nói về con người.**

⚠️ **Dòng bắt buộc ở cuối mọi bảng xếp hạng:**
> *"Bảng này là đầu vào để trưởng nhóm kèm việc. Không dùng làm căn cứ đánh giá hay kỷ luật lao động; số liệu quảng cáo chịu ảnh hưởng của nhiều yếu tố nằm ngoài quyền quyết định của người chạy."*

---

## 6 · Hai chỉ số nên theo dõi cho **cả team**, không cho từng người

① **Tỷ lệ cảnh báo được đóng đúng SLA** — đo sức khoẻ của quy trình, không đo cá nhân.
② **Số creative mới được bật / tháng của cả team** — đo năng lực đổi mới.

Hai chỉ số này đặt ở cấp team là có chủ ý: chúng cần **hợp tác** chứ không cần **cạnh tranh**. Gán chúng cho từng người sẽ sinh ra creative bật cho có và cảnh báo đóng cho xong.


===== ar-ho-so-van-hanh.md =====

# HỒ SƠ VẬN HÀNH — KANGNAM *(module swappable)*
Version 1.0 · đối chiếu `Agent-AdsOptimize-Kangnam/knowledge/kn-ho-so-thuong-hieu.md` v2.2 (2026-10-16)

> Đây là **module thương hiệu**. Đổi sang brand khác = thay file này + `ar-rao-phap-ly.md`, **giữ nguyên bộ não**.
> Các ô `[CHỜ CẬP NHẬT]` phải do đội Adnet/Trưởng nhóm điền trước khi chạy MODE 3 và MODE 4.

---

## 1 · Thương hiệu
Hệ thống **Bệnh viện Thẩm mỹ Kangnam** — chuẩn Hàn tại Việt Nam, nền tảng y khoa quốc tế.
Hotline chung **0968.999.777** · Zalo OA · App Kangnam Care.
Hệ sinh thái: **KPS** (Plastic Surgery) · **KBS** (Beauty & Spa) · **KDT** (Dental) · **KWN** (Wellness) · **KWL** (Weight Loss).
Agent này phụ trách báo cáo quảng cáo của mảng **thẩm mỹ – làm đẹp**. Số liệu của **Cơ Xương Khớp – Wellness** thuộc thương hiệu riêng, có agent riêng — gặp thì báo người dùng, không trộn vào báo cáo chung.

---

## 2 · ⚠️ Bảy cơ sở và TUYẾN — ràng buộc cứng

| Mã KV | Cơ sở | **TUYẾN** | Được mời đại phẫu? |
|---|---|---|---|
| **HN** | Kangnam Hà Nội — 190 Trường Chinh (GP 194/BYT-GPHĐ) | **Bệnh viện** | ✅ **CÓ** |
| **SG** | Kangnam Sài Gòn — 666 CMT8, TP.HCM (GP 287/BYT-GPHĐ) | **Bệnh viện** | ✅ **CÓ** |
| **HP** | Kangnam Hải Phòng — 378 Tô Hiệu | Viện thẩm mỹ | ❌ không |
| **NA** | Kangnam Nghệ An — 148 Nguyễn Văn Cừ, TP. Vinh | Viện thẩm mỹ | ❌ không |
| **DN** | Kangnam Đà Nẵng — 293 Hùng Vương | Viện thẩm mỹ | ❌ không |
| **CT** | Kangnam Cần Thơ — 28 Lý Tự Trọng | Viện thẩm mỹ | ❌ không |
| **TH** | Kangnam Thanh Hóa — 103 Nguyễn Trãi | Viện thẩm mỹ | ❌ không |

**Luật TUYẾN dùng cho báo cáo:** chiến dịch **ZONE đại phẫu** nhắm khu vực **không phải HN/SG** mà thông điệp **mời thực hiện tại đó** → bắn **C-02 mức 🔴**, báo Adnet + Trưởng nhóm + Pháp chế.
Hai cách đóng hợp lệ: ① sửa thông điệp thành *"tư vấn/đặt khám tại cơ sở tỉnh, phẫu thuật tại tuyến bệnh viện"*; ② loại trừ tỉnh đó khỏi targeting.

> ⚠️ Địa chỉ, tuyến và phạm vi giấy phép **đổi theo thời điểm**. Chạy local phải verify lại trước khi bật chiến dịch — và trước khi kết luận một lead là "sai tuyến".

---

## 3 · Tám ZONE dịch vụ và loại ZONE

| ZONE | Mã | Loại | CPL mục tiêu | Giá trị đơn TB | Ghi chú nhịp |
|---|---|---|---|---|---|
| Mắt | `MAT` | Đại phẫu | `[CHỜ CẬP NHẬT]` | `[CHỜ CẬP NHẬT]` | quyết định 2–8 tuần |
| Mũi | `MUI` | Đại phẫu | `[CHỜ CẬP NHẬT]` | `[CHỜ CẬP NHẬT]` | |
| Hàm mặt | `HAMMAT` | Đại phẫu | `[CHỜ CẬP NHẬT]` | `[CHỜ CẬP NHẬT]` | **quyết định 1–6 tháng, theo mùa nghỉ** |
| Vòng 1 | `VONG1` | Đại phẫu | `[CHỜ CẬP NHẬT]` | `[CHỜ CẬP NHẬT]` | |
| Lipo 360 | `LIPO` | Đại phẫu | `[CHỜ CẬP NHẬT]` | `[CHỜ CẬP NHẬT]` | |
| Trẻ hóa da | `TREHOA` | Thủ thuật | `[CHỜ CẬP NHẬT]` | `[CHỜ CẬP NHẬT]` | 2–6 tuần |
| Da liễu | `DALIEU` | Liệu trình | `[CHỜ CẬP NHẬT]` | `[CHỜ CẬP NHẬT]` | 1–3 tuần, nhạy ưu đãi |
| Kangnam Clinic | `CLINIC` | Liệu trình | `[CHỜ CẬP NHẬT]` | `[CHỜ CẬP NHẬT]` | |

**Loại ZONE quyết định cách đọc số, không phải tên dịch vụ:**

| | Đại phẫu | Thủ thuật | Liệu trình |
|---|---|---|---|
| Chu kỳ quyết định | **1–6 tháng** | 2–6 tuần | 1–3 tuần |
| **Độ trễ lead → booking** | **dài** — CPL tuần này chưa thấy booking | trung bình | ngắn |
| CPL chấp nhận được | **cao** | trung bình | **thấp** |
| Ràng buộc TUYẾN | **có** | một phần | **không** |
| Nhạy ưu đãi | yếu | trung bình | **mạnh** |

⚠️ **Hệ quả quan trọng nhất cho báo cáo:** ZONE **đại phẫu** có **độ trễ lead→booking dài**, nên đọc `lead→booking %` của tuần hiện tại là **đọc sai**. Với ZONE đại phẫu, mã **B-03** phải tính trên **cohort lead theo tuần phát sinh**, theo dõi tới 30 ngày — không tính theo booking phát sinh trong tuần.
Dùng chung một công thức cho cả 8 ZONE sẽ cho ra kết luận *"đại phẫu chốt kém hơn da liễu"*, điều này luôn đúng về mặt số học và luôn vô nghĩa về mặt vận hành.

---

## 4 · Cơ cấu đội Adnet

| Trường | Giá trị |
|---|---|
| Số người chạy | `[CHỜ CẬP NHẬT]` |
| Phân công | theo **ZONE × khu vực** · `[CHỜ CẬP NHẬT]` bảng ánh xạ `adnet_id` → ZONE/KV |
| Trưởng nhóm | `[CHỜ CẬP NHẬT]` |
| Người nhận cảnh báo 🔴 | Adnet phụ trách **+ Trưởng nhóm** |
| Người nhận mã **E** | **+ CNTT/Kỹ thuật** |
| Người nhận mã **C-02** | **+ Pháp chế/Marketing lead** |
| Giờ làm việc tính SLA | `[CHỜ CẬP NHẬT]` (vd 08:30–17:30, T2–T7) |

**Bảng ánh xạ `adnet_id` là điều kiện bắt buộc của MODE 3.** Thiếu nó thì agent chỉ chạy được MODE 1, 2, 4, 5 — và phải nói rõ điều đó thay vì đoán tên người từ tên campaign.

---

## 5 · Mặc định vận hành (điền trước khi chạy)

| Tham số | Mặc định đề xuất | Giá trị thực tế |
|---|---|---|
| Ngân sách tháng toàn hệ | — | `[CHỜ CẬP NHẬT]` |
| % ngân sách thăm dò | 10–15% | `[CHỜ CẬP NHẬT]` |
| Cửa sổ attribution | 7d click / 1d view | `[CHỜ CẬP NHẬT]` |
| Trần frequency 7 ngày | 2,5 | `[CHỜ CẬP NHẬT]` |
| Ngưỡng % lead rác bình thường | `[CHỜ CẬP NHẬT]` | |
| Khung giờ inbox mạnh nhất | 20:00–23:00 | `[CHỜ CẬP NHẬT]` |
| Công suất booking/ngày theo cơ sở | — | `[CHỜ CẬP NHẬT]` (nuôi **H-04**) |

Ô nào còn `[CHỜ CẬP NHẬT]` thì agent **vẫn chạy được**, nhưng phải ghi rõ trong output rằng kết luận liên quan đang thiếu mốc so sánh — **không tự đặt ra một con số mục tiêu rồi dùng nó như thật.**

---

## 6 · Quan hệ với các agent anh em

| Việc | Agent phụ trách |
|---|---|
| Báo cáo · cảnh báo bất thường · hiệu quả adnet · phân bổ ngân sách | **Agent này** |
| Viết mẫu quảng cáo · dựng landing page · bộ từ khoá | `Agent-AdsOptimize-Kangnam` |
| Kịch bản chăm sóc · tái khai thác data cũ · phân loại hội thoại | `Agent-CRM-Automation` |
| Sinh agent CSKH mới · kiến trúc hệ thống trợ lý | `Kangnam-Agent-Factory` |

Agent này **chẩn đoán ra vấn đề rồi chuyển việc**, không tự làm phần nội dung. Ví dụ: chẩn đoán **B-05 creative yếu** → hành động ghi *"chuyển brief sang Agent-AdsOptimize, MODE 1 WIN-AD"*, không tự viết hook.


===== ar-khung-bao-cao.md =====

# KHUNG BÁO CÁO & DASHBOARD
Version 1.0 · dùng cho MODE 1

---

## 1 · Ba nhịp báo cáo — ba người đọc khác nhau

| Nhịp | Ai đọc | Dài | Trả lời câu hỏi |
|---|---|---|---|
| **Ngày** (sáng hôm sau) | Adnet phụ trách | ≤ 1 màn hình | *Hôm qua có gì cần sửa ngay không?* |
| **7 ngày** | Trưởng nhóm Adnet | 6 khối đầy đủ | *Tuần qua tiền chảy đi đâu, rò ở đâu, ai cần kèm?* |
| **14 ngày / tháng** | CEO dịch vụ · Marketing lead | 6 khối + xu hướng | *Có nên đổi phân bổ ngân sách và mục tiêu CPL không?* |

⛔ **Không dùng một bản báo cáo cho cả ba.** Báo cáo ngày mà có bảng so kỳ tháng thì adnet sẽ không đọc; báo cáo tháng mà liệt kê từng ad set thì CEO sẽ không đọc.

**Báo cáo ngày chỉ gồm 3 thứ:** ① chi–lead–CPL hôm qua vs median 7 ngày · ② danh sách cảnh báo 🔴🟠 · ③ việc quá hạn từ hôm trước. Hết.

---

## 2 · Sáu khối của báo cáo 7 / 14 ngày

### Khối ① — Tóm tắt 5 dòng
```
Kỳ:          07–13/10/2026 (7 ngày, 2 ngày cuối tuần, không có khuyến mãi)
Tổng chi:    412,5tr  (kỳ trước 389,0tr · +6,0%)
Lead hợp lệ: 1.043    (kỳ trước 1.118 · −6,7%)
CPL:         396k     (kỳ trước 348k · +13,8% · mục tiêu 350k)
➜ KẾT LUẬN:  CPL vượt mục tiêu chủ yếu do ZONE Mũi (+31%); 3 ZONE còn lại trong dải bình thường.
```
Dòng **➜ KẾT LUẬN** là dòng duy nhất nhiều người đọc. Nó phải nêu **một nguyên nhân cụ thể**, không được viết *"cần tối ưu thêm"*.

### Khối ② — Phễu 8 tầng
Mỗi tầng: **số tuyệt đối · tỷ lệ chuyển tiếp · ±% so kỳ trước · dấu ⚠ ở tầng rò**.

| Tầng | Kỳ này | Kỳ trước | Tỷ lệ chuyển | ± | |
|---|---|---|---|---|---|
| Chi | 412,5tr | 389,0tr | — | +6,0% | |
| Hiển thị | 18,2tr | 19,1tr | CPM 22,7k | +11,2% | |
| Click | 341k | 372k | CTR 1,87% | −4,2% | |
| Inbox | 4.210 | 4.380 | click→inbox 1,23% | −2,1% | |
| **Lead** | **1.043** | **1.118** | **inbox→lead 24,8%** | **−9,5%** | ⚠ **tầng rò** |
| Booking | 357 | 381 | lead→booking 34,2% | +0,3% | hệ quả |
| Đến | 241 | 259 | show-rate 67,5% | −0,4% | hệ quả |
| Chốt | 71 | 77 | đến→chốt 29,5% | +0,2% | hệ quả |

**Chỉ một tầng được đánh dấu ⚠.** Các tầng dưới ghi "hệ quả" — đây là cách báo cáo này ngăn bốn phòng ban cùng nhận lỗi.

### Khối ③ — CPL trung bình trượt 7 ngày
Theo ngày, kèm **dải bình thường** (median ± 20%). Vẽ hoặc kẻ bảng đều được, nhưng **phải có dải**, nếu không người đọc sẽ hoảng với mọi dao động.
Đánh dấu ngày có **sự kiện đã biết** (lễ · hết khuyến mãi · đổi landing · sự cố tài khoản) ngay trên trục — phần lớn "đỉnh lạ" đều có tên.

### Khối ④ — Diễn biến theo dịch vụ (ZONE)
| ZONE | Chi | Share NS | Lead | Share lead | CPL | ±CPL | Mục tiêu | Đạt? |
|---|---|---|---|---|---|---|---|---|
| Mũi | 148tr | 35,9% | 302 | 29,0% | 490k | **+31%** | 420k | ❌ |
| Mắt | 96tr | 23,3% | 311 | 29,8% | 309k | −4% | 330k | ✅ |

**Cột `Share NS` đặt cạnh `Share lead` là có chủ ý** — lệch ≥ 15 điểm % là mã **H-03**. Đây là bảng nhìn ra tiền chảy sai chỗ nhanh nhất.

### Khối ⑤ — So sánh các kỳ
Ba cột: **7 ngày này · 7 ngày trước · cùng kỳ tháng trước**.
**Luật so kỳ — kiểm trước khi so:** cùng độ dài · cùng số ngày cuối tuần · cùng trạng thái khuyến mãi · cùng cửa sổ attribution.
Không thoả → ghi rõ *"hai kỳ không so trực tiếp được vì [lý do]"* và **so bằng tỷ lệ (CPL, % chuyển tiếp), không so bằng số tuyệt đối**.

### Khối ⑥ — Cảnh báo
Xếp 🔴 → 🟠 → 🟡, mỗi dòng là một **phiếu 7 ô** (§10 bộ não). Dưới cùng là hai mục riêng:
- **⚪ Theo dõi** — chưa qua đủ 3 cổng, liệt kê không hành động.
- **⏰ Việc quá hạn** — cảnh báo kỳ trước chưa đóng, kèm số ngày trễ.

Mục *Việc quá hạn* là mục làm hệ thống này có răng. Không có nó, cảnh báo chỉ là thông báo.

---

## 3 · Đặc tả Dashboard (khi dựng trên Sheet / Looker Studio / Excel)

**Bộ lọc bắt buộc ở đầu trang:** `Khoảng ngày (7/14/30/tuỳ chọn)` · `ZONE` · `Khu vực` · `Cơ sở` · `Nhân viên Adnet` · `Campaign`.
Mặc định mở ra là **7 ngày gần nhất, loại 1 ngày chưa chốt số**.

**Thứ tự khối trên màn hình** — từ trên xuống, theo đúng thứ tự người ra quyết định cần:

| Vị trí | Khối | Vì sao ở đó |
|---|---|---|
| 1 | **Thẻ số lớn**: Chi · Lead · CPL · Booking (kèm ±% và mũi tên) | 5 giây đầu phải biết hôm nay ổn hay không |
| 2 | **Băng cảnh báo** 🔴🟠 | thứ cần hành động phải nằm trên phần cần suy nghĩ |
| 3 | Đường CPL trượt 7 ngày + dải bình thường | xu hướng trước chi tiết |
| 4 | Phễu 8 tầng | định vị tầng rò |
| 5 | Bảng ZONE (share NS vs share lead) | phân bổ tiền |
| 6 | Bảng nhân viên Adnet | người, đặt cuối cùng — xem mục 4 |
| 7 | Bảng chi tiết ad set (có thể gập) | chỉ mở khi cần đào |

⛔ **Không đặt bảng xếp hạng nhân viên lên đầu dashboard.** Dashboard mở ra là thấy bảng xếp hạng người thì cả đội sẽ tối ưu cho **thứ hạng**, không tối ưu cho **kết quả** — và cách dễ nhất để lên hạng là chọn ZONE dễ, chứ không phải chạy giỏi hơn.

**Ba lỗi dashboard hay gặp:**
① **Quá nhiều chỉ số** — màn hình 30 ô thì không ô nào được nhìn. Giữ ≤ 8 ô ở tầng 1.
② **Không có baseline** — con số đứng một mình không nói được gì; mọi số phải có `± so với` cạnh nó.
③ **Không ghi thời điểm cập nhật** — người đọc không biết số đã chốt chưa, rồi ra quyết định trên số còn đang chạy về.

---

## 4 · Dòng chân trang bắt buộc
Mọi báo cáo, mọi dashboard đều kết bằng:
> *"Số liệu tính trên kỳ **[__]** · nguồn **[Meta / CRM / ERP]** · cửa sổ attribution **[7d click / 1d view]** · cập nhật lúc **[__]**. Ngày **[__]** chưa chốt số."*

Thiếu dòng này thì sáu tháng sau không ai dựng lại được con số, và hai bản báo cáo khác nhau sẽ cãi nhau mà không ai biết bản nào đúng.


===== ar-nguong-bat-thuong.md =====

# NGƯỠNG BẤT THƯỜNG — 8 NHÓM · 30 MÃ
Version 1.0 · **file quan trọng nhất của agent này**

> **Ngưỡng dưới đây là ngưỡng KHỞI ĐỘNG, không phải chân lý.** Chạy tay 2–4 tuần, đếm xem mã nào bắn nhiều mà không ai xử lý được → **nới ngưỡng mã đó hoặc bỏ**. Ngưỡng tốt là ngưỡng mà **≥ 70% cảnh báo dẫn đến một thao tác thật**.
>
> **Mọi mã đều phải qua 3 cổng §4 của bộ não trước khi được gọi là cảnh báo.** File này chỉ cho ngưỡng; cổng mới quyết định có bắn hay không.

---

## 0 · Cách đọc bảng

| Cột | Nghĩa |
|---|---|
| **Mã** | gắn vào mọi phiếu cảnh báo, dùng để đếm thống kê |
| **Điều kiện** | so với **median 7 ngày cùng đơn vị, cùng loại ngày** |
| **Mức mặc định** | có thể bị đẩy lên theo luật lặp 2 kỳ (§8 bộ não) |
| **Chủ sở hữu** | người **phải hành động**, theo tầng rò — không phải người báo cáo |

**Đơn vị xét mặc định:** Ad set. Chỉ gộp lên Campaign/ZONE khi **≥ 3 ad set cùng lệch một chiều** — gộp sớm sẽ giấu mất ad set hỏng duy nhất.

---

## A · CHI PHÍ

| Mã | Tên | Điều kiện | Mức | Chủ sở hữu |
|---|---|---|---|---|
| **A-01** | CPL vọt | CPL ≥ +30% median 7 ngày, đủ mẫu, ≥2 ngày cùng chiều | 🟠 (≥+50% → 🔴) | Adnet |
| **A-02** | CPM vọt | CPM ≥ +30% median 7 ngày | 🟡 (≥+50% → 🟠) | Adnet |
| **A-03** | CPI vọt | chi/inbox ≥ +30% median | 🟠 | Adnet |
| **A-04** | Vượt pacing | chi luỹ kế ≥ 110% mốc pacing tháng | 🟠 (≥125% → 🔴) | Trưởng nhóm |
| **A-05** | Chi hụt | chi ≤ 70% ngân sách đặt, ≥2 ngày liên tiếp | 🟠 | Adnet |
| **A-06** | Cháy sớm trong ngày | hết ngân sách trước **18:00** | 🟡 | Adnet |

**A-02 không bao giờ là cảnh báo độc lập đáng hành động.** CPM tăng mà CPL giữ nguyên thì **không có vấn đề gì** — chỉ ghi nhận. CPM chỉ có ý nghĩa khi dùng để **giải thích** A-01.
**A-05 nguy hiểm hơn A-04 và hay bị bỏ qua:** tiền không tiêu được nghĩa là mất phễu, nhưng không ai nhìn thấy vì "không tốn tiền". Nguyên nhân thường gặp: tệp quá hẹp · bid trần quá thấp · ad set đang học lại · creative vừa bị từ chối (→ kiểm **E-01** trước).
**A-06** làm mất khung 20:00–23:00 — khung inbox mạnh nhất của ngành thẩm mỹ.

---

## B · RÒ PHỄU

| Mã | Tên | Điều kiện | Mức | Chủ sở hữu |
|---|---|---|---|---|
| **B-01** | Click vào nhưng không nhắn | CTR ≥ median nhưng **click→inbox ≤ −30%** median | 🟠 | Adnet + Kỹ thuật |
| **B-02** | Inbox nhiều, lead ít | **inbox→lead ≤ −25%** median, inbox ≥ 30 | 🟠 | **Trực page** |
| **B-03** | Lead nhiều, booking ít | **lead→booking ≤ −25%** median, lead ≥ 20 | 🟠 | **Telesales** |
| **B-04** | Booking nhiều, không đến | **show-rate ≤ −25%** median, booking ≥ 15 | 🟠 | **Lễ tân / CSKH** |
| **B-05** | Creative yếu | **CTR ≤ −30%** median **và** CPM trong dải ±15% | 🟠 | Adnet |
| **B-06** | Đến nhiều, chốt ít | **đến→chốt ≤ −25%** median, đến ≥ 10 | 🟡 | Tư vấn tại cơ sở |

**Luật tầng rò (§6 bộ não) áp dụng mạnh nhất ở nhóm B.** Khi nhiều mã B cùng bắn, **chỉ xuất phiếu cho mã có tầng NHỎ NHẤT**; các mã còn lại ghi vào ô *"hệ quả kéo theo"* của phiếu đó.
Ví dụ: B-01 + B-02 + B-03 cùng bắn → xuất **một** phiếu B-01, ghi B-02/B-03 là hệ quả. Bắn ba phiếu cho ba phòng ban là cách nhanh nhất để ba phòng đổ lỗi cho nhau trong hai tuần.

**B-02 kiểm hai việc trước khi kết luận là lỗi trực page:** ① **thời gian phản hồi lần đầu** — quá 5 phút thì tỷ lệ ra số tụt rất nhanh; ② **ca trực tối/cuối tuần** có người không. Phần lớn B-02 là **lỗi xếp ca, không phải lỗi kỹ năng**.

---

## C · CHẤT LƯỢNG LEAD

| Mã | Tên | Điều kiện | Mức | Chủ sở hữu |
|---|---|---|---|---|
| **C-01** | Lead rác tăng | % lead rác ≥ +10 điểm % so median | 🟠 | Adnet (targeting) |
| **C-02** | **Lead sai TUYẾN** | lead đại phẫu từ tỉnh **không có tuyến bệnh viện**, và landing/ad **có mời thực hiện tại đó** | 🔴 **luôn luôn** | Adnet + Trưởng nhóm + Pháp chế |
| **C-03** | Lead trùng | % trùng 30 ngày ≥ 15% | 🟡 | Adnet (loại trừ tệp) |
| **C-04** | Sai chân dung | ≥ 30% lead lệch ngoài dải tuổi/giới mục tiêu | 🟡 | Adnet |
| **C-05** | Cụm lead bất thường | ≥ 40% lead trong ngày rơi vào 1 khung 2 giờ đêm (00:00–06:00) | 🟠 | Adnet + Kỹ thuật |

**C-02 là mã duy nhất bỏ qua mọi điều kiện cỡ mẫu — một lead cũng bắn.** Đây không phải vấn đề hiệu suất mà là **rủi ro vượt phạm vi giấy phép**. Hai cách đóng hợp lệ: ① sửa thông điệp thành *"tư vấn/đặt khám tại cơ sở tỉnh, phẫu thuật tại tuyến bệnh viện"*; hoặc ② đưa tỉnh đó vào loại trừ của chiến dịch. **Không có cách thứ ba.**

**C-01 phải tách theo lý do rác** (xem `ar-tu-dien-chi-so.md` §2②) trước khi quy trách nhiệm — *sai khu vực* và *bấm nhầm* là hai vấn đề của hai tầng khác nhau.

---

## D · CREATIVE & BÃO HOÀ

| Mã | Tên | Điều kiện | Mức | Chủ sở hữu |
|---|---|---|---|---|
| **D-01** | Bão hoà tệp | frequency 7 ngày ≥ **2,5** **và** CTR giảm ≥ 20% so median | 🟠 | Adnet |
| **D-02** | Thiếu challenger | ≥ **14 ngày** không có creative mới được bật trong ad set đang tiêu ≥ 20% ngân sách ZONE | 🟡 | Adnet |
| **D-03** | Phụ thuộc 1 creative | 1 ad chiếm ≥ **60%** chi tiêu ad set trong 7 ngày | 🟡 | Adnet |
| **D-04** | Trôi dần | CTR giảm liên tiếp **3 ngày**, tổng mức giảm ≥ 15% | 🟡 | Adnet |

**D-01 chỉ có nghĩa khi đi kèm CTR giảm.** Frequency 3,0 mà CTR giữ nguyên là **tệp trung thành, không phải bão hoà** — tắt đi là mất một ad set tốt.
**D-02 là mã "phòng bệnh" duy nhất trong cả bộ** — nó cảnh báo một việc **chưa xảy ra**. Không có challenger thì khi winner xuống sức sẽ không có gì thay thế, và lúc đó mới làm creative mới là đã chậm 7–10 ngày.

---

## E · VẬN HÀNH & KỸ THUẬT — **QUÉT TRƯỚC TẤT CẢ**

| Mã | Tên | Điều kiện | Mức | Chủ sở hữu |
|---|---|---|---|---|
| **E-01** | Ad bị từ chối/hạn chế | có bất kỳ ad `disapproved` / `limited` đang thuộc ad set chạy | 🔴 | Adnet |
| **E-02** | Tài khoản lỗi | tài khoản `disabled` / lỗi thanh toán / vượt hạn mức chi | 🔴 | Trưởng nhóm |
| **E-03** | Tracking chết | một chỉ số bình thường > 0 bỗng = 0 trọn 1 ngày | 🔴 | Kỹ thuật |
| **E-04** | Lệch Meta ↔ CRM | \|lead-Meta − lead-CRM\| ÷ lead-CRM ≥ **30%** | 🔴 | Kỹ thuật + CRM |
| **E-05** | Tắt ngoài kế hoạch | campaign/ad set `off` mà không có dòng trong nhật ký thay đổi | 🟠 | Adnet |
| **E-06** | Tự đấu giá với mình | ≥ 2 ad set cùng ZONE, cùng khu vực, trùng tệp ≥ 50%, cùng chạy | 🟠 | Adnet |
| **E-07** | Điểm đến hỏng | landing lỗi / thời gian tải ≥ 5s / form không submit được | 🔴 | Kỹ thuật |

**Quy trình bắt buộc:** quét E **trước**, A–H **sau**. Nếu có **E-03** hoặc **E-04** đang mở → **đóng băng mọi cảnh báo A/B/C của kỳ đó** và ghi *"số liệu chưa tin được, tạm dừng kết luận"*. Phân tích trên số sai còn tệ hơn không phân tích: nó làm người ta sửa nhầm thứ đang chạy tốt.

---

## F · NHÂN SỰ ADNET

| Mã | Tên | Điều kiện | Mức | Chủ sở hữu |
|---|---|---|---|---|
| **F-01** | CPL lệch team | CPL ≥ **1,3× median team** cùng ZONE + cùng khu vực, đủ mẫu | 🟡 | Trưởng nhóm (kèm việc) |
| **F-02** | Ad set bị bỏ rơi | CPL vượt ngưỡng ≥ **3 ngày** mà nhật ký không có thao tác nào | 🟠 | Trưởng nhóm |
| **F-03** | Tiền chảy về chỗ kém | người có CPL cao nhất đang giữ share ngân sách lớn nhất ZONE | 🟠 | Trưởng nhóm |
| **F-04** | Đổi nhiều biến cùng lúc | ≥ 3 thay đổi (bid + tệp + creative) trên cùng ad set trong 24h | 🟡 | Adnet |
| **F-05** | Không ghi nhật ký | ad set có chỉ số đổi ≥ 30% mà nhật ký trống | 🟡 | Adnet |

**F-02 quan trọng hơn F-01 rất nhiều.** CPL cao có thể do ZONE khó, mùa, tệp cạn — nhiều thứ ngoài tầm tay người chạy. Nhưng **ba ngày nhìn thấy số xấu mà không làm gì** là thứ hoàn toàn trong tầm tay. Khi phải chọn một mã F để theo dõi, chọn F-02.
**F-04 không phải lỗi đạo đức, là lỗi phương pháp:** đổi ba biến cùng lúc thì dù kết quả tốt lên cũng **không học được gì**, lần sau lặp lại không ra.
⚠️ Mọi mã F đi kèm câu: *"Đây là đầu vào để trưởng nhóm kèm việc, không phải căn cứ đánh giá kỷ luật."*

---

## G · KỲ & MÙA VỤ — nhóm **chống** báo động giả

| Mã | Tên | Điều kiện | Mức | Dùng để |
|---|---|---|---|---|
| **G-01** | Lệch so kỳ | tổng lead hoặc CPL kỳ này lệch ≥ 20% kỳ trước | 🟡 | báo cáo, không bắn riêng |
| **G-02** | **Hiệu ứng cuối tuần** | đang so ngày cuối tuần với ngày thường | — | **CHẶN cảnh báo** |
| **G-03** | Vách sau khuyến mãi | ngày đầu sau khi ưu đãi kết thúc, CPL tăng ≥ 30% | 🟡 | **giải thích**, không quy trách nhiệm |
| **G-04** | Sự kiện toàn ngành | CPM tăng ≥ 30% đồng loạt ≥ 70% ad set trong tài khoản | 🟡 | **giải thích** |

**G-02 và G-04 là hai mã CHẶN, không phải mã BẮN.** Khi chúng đúng, agent phải **hạ mức hoặc huỷ** cảnh báo A/B tương ứng và ghi lý do.
G-04 là cách phân biệt *"đội mình làm hỏng"* với *"cả thị trường đắt lên"*: một ad set tăng CPM là chuyện của ad set đó; **70% tài khoản cùng tăng là chuyện của thị trường** — và không ai trong team sửa được bằng cách đổi creative.

---

## H · DỊCH VỤ & PHÂN BỔ

| Mã | Tên | Điều kiện | Mức | Chủ sở hữu |
|---|---|---|---|---|
| **H-01** | Đổ tiền vào chỗ xấu | ZONE có CPL ≥ +20% median **và** share ngân sách vẫn tăng so kỳ trước | 🟠 | Trưởng nhóm |
| **H-02** | Bỏ đói ZONE tốt | ZONE có CPL ≤ −15% median **và** share ngân sách giảm | 🟡 | Trưởng nhóm |
| **H-03** | Lệch tiền–kết quả | \|share ngân sách − share lead\| ≥ **15 điểm %** | 🟡 | Trưởng nhóm |
| **H-04** | Dồn tải một cơ sở | ≥ 60% booking của ZONE đổ về 1 cơ sở vượt công suất đã khai | 🟠 | Vận hành |

**H-02 bị bỏ sót thường xuyên hơn H-01** vì không ai đi báo cáo một thứ *đang tốt*. Nhưng ZONE giá trị cao bị bỏ đói là **mất doanh thu âm thầm** — và chỉ nhìn ra khi đặt share ngân sách cạnh share lead.
**H-01 không tự động nghĩa là sai.** Có thể đang chủ ý đẩy một ZONE chiến lược. → Phiếu H-01 luôn hỏi: *"Đây là quyết định chủ ý hay là quán tính?"* Nếu chủ ý thì đóng phiếu và **ghi vào danh sách sự kiện đã biết** để kỳ sau không bắn lại.

---

## 9 · Hiệu chỉnh ngưỡng — quy trình 4 tuần

| Tuần | Việc |
|---|---|
| 1–2 | Chạy **tay**, ghi mọi cảnh báo vào một bảng: mã · có ai xử lý không · xử lý xong có cải thiện không |
| 3 | Mã nào **< 50% dẫn tới thao tác** → nới ngưỡng +10 điểm % hoặc hạ mức |
| 4 | Mã nào **chưa bao giờ bắn** → kiểm xem ngưỡng có quá lỏng, hay dữ liệu không có trường đó |
| Sau đó | Mới bật tự động (§13 bộ não) |

**Chỉ số sức khoẻ của chính hệ cảnh báo:** *tỷ lệ cảnh báo dẫn tới thao tác thật*. Dưới **50%** thì hệ đang tạo ồn — sửa hệ trước khi trách người không đọc.


===== ar-quan-ly-ngan-sach.md =====

# QUẢN LÝ NGÂN SÁCH — PACING · ĐIỀU CHUYỂN · TRẦN RỦI RO
Version 1.0 · dùng cho MODE 4

---

## 1 · Pacing — ba câu hỏi mỗi ngày

```
Mốc pacing hôm nay = Ngân sách tháng × (số ngày đã qua ÷ số ngày trong tháng)
Pacing %           = Chi luỹ kế ÷ Mốc pacing
```

| Pacing % | Nghĩa | Việc |
|---|---|---|
| **< 90%** | **chi hụt** — đang mất phễu | Kiểm **A-05**: tệp hẹp? bid trần thấp? ad vừa bị từ chối (**E-01**)? |
| 90–110% | bình thường | — |
| 110–125% | vượt | Rà ZONE nào đang ăn vượt, có đáng không (**H-01**) |
| **> 125%** | **cháy** | 🔴 Hạ ngân sách ZONE CPL xấu trước, giữ ZONE CPL tốt |

**Chi hụt bị bỏ qua nhiều hơn chi vượt** vì nó không gây đau ngay. Nhưng cuối tháng nhìn lại thì "tiết kiệm được 60 triệu" thực ra là **mất 150 lead**.

**Pacing phải tính theo ZONE, không chỉ theo tài khoản.** Tổng tài khoản đúng 100% hoàn toàn có thể che một ZONE chạy 160% và một ZONE chạy 55%.

---

## 2 · Bốn luật cứng khi đổi ngân sách

### ① Trần thay đổi: **±20–30% mỗi lần, cách nhau ≥ 48h**
Nhảy ngân sách gấp đôi làm ad set **vào lại learning phase** — CPL xấu đi 2–4 ngày **trước khi** tốt lên. Người không biết luật này sẽ thấy CPL xấu, hoảng, hạ ngân sách xuống, và ad set lại học lại lần nữa. Đó là vòng xoáy đốt tiền phổ biến nhất của đội mới.

### ② Chỉ scale đơn vị **đã qua cổng đủ mẫu** và **CPL ổn định ≥ 3 ngày**
Ổn định nghĩa là dao động trong dải **median ± 20%**, không phải "hôm qua rẻ".

### ③ Luôn giữ **10–15% ngân sách thăm dò**
Dành cho tệp mới · creative mới · ZONE đang test. Dồn 100% vào winner là **vay của tương lai**: mọi winner đều bão hoà, và lúc nó bão hoà mà không có gì thay thế thì cả ZONE đứng hình 1–2 tuần.
Ngân sách thăm dò **không bị chấm bằng CPL ngắn hạn** — chấm nó bằng *"tháng này tìm ra được bao nhiêu tệp/creative dùng được"*. Chấm nhầm bằng CPL thì sẽ không ai dám test nữa.

### ④ **Cắt ngân sách là hành động CUỐI**
Trước khi cắt phải trả lời: **tầng rò nằm ở đâu** (§6 bộ não)? Nếu tầng rò **từ ⑤ trở xuống** thì cắt ads **làm vấn đề tệ hơn** — ít lead hơn mà tỷ lệ vẫn hỏng.

---

## 3 · Luật điều chuyển giữa các ZONE

Điều chuyển dựa trên **ba chỉ số cùng lúc**, không chỉ CPL:

| Chỉ số | Vì sao cần |
|---|---|
| **CPL so mục tiêu ZONE** | mỗi ZONE có mục tiêu khác nhau — CPL 500k của đại phẫu tốt hơn CPL 200k của da liễu |
| **Lead→Booking %** | ZONE CPL rẻ nhưng không ra booking là ZONE đang lừa chính mình |
| **Giá trị đơn trung bình** | ZONE giá trị cao chịu được CPL cao hơn nhiều |

**Công thức ưu tiên thực dụng:**
```
Điểm ZONE = (Giá trị đơn TB × Lead→Booking % × Booking→Chốt %) ÷ CPL
```
→ Chuyển tiền **từ ZONE điểm thấp sang ZONE điểm cao**, mỗi lần **≤ 20% ngân sách ZONE nguồn**.

⚠️ **Hai thứ phải kiểm trước khi chuyển tiền sang một ZONE:**
① **Công suất cơ sở** — ZONE đó có đủ bác sĩ/phòng/lịch để nhận thêm booking không (**H-04**). Đổ tiền vào ZONE đã kín lịch chỉ tạo ra booking không được phục vụ và khách bực.
② **TUYẾN** — ZONE đại phẫu chỉ chạy được ở khu vực có tuyến bệnh viện; đẩy ngân sách đại phẫu về tỉnh chỉ có viện thẩm mỹ là tạo ra **C-02** hàng loạt.

---

## 4 · Mẫu đề xuất điều chuyển (bắt buộc đủ 6 ô)

```
① CHUYỂN       : 30tr (20% ngân sách ZONE Mũi tuần tới)
② TỪ           : ZONE Mũi — CPL 490k / mục tiêu 420k · lead→booking 31% · điểm 2,1
③ SANG         : ZONE Mắt — CPL 309k / mục tiêu 330k · lead→booking 38% · điểm 4,6
④ KỲ VỌNG      : CPL chung kỳ tới về ~370k; lead tổng +4–6%
⑤ RỦI RO       : Mắt đang chạy frequency 2,2 — tăng tiền có thể đẩy lên bão hoà (D-01)
                 → chia 30tr thành 2 lần ×15tr, cách 48h, theo dõi CTR
⑥ ĐÁNH GIÁ LẠI : sau 5 ngày · chỉ số: CPL Mắt + CTR Mắt + tổng lead
```

Ô ⑤ là ô hay bị bỏ nhất và là ô có giá trị nhất: **mọi lần tăng tiền đều có rủi ro đẩy đơn vị nhận tiền vào bão hoà**. Đề xuất không nêu rủi ro là đề xuất chưa xong.

---

## 5 · Ngân sách và mùa vụ

| Tình huống | Luật |
|---|---|
| Trước đợt khuyến mãi | Tăng ngân sách **trước 3–5 ngày** để ad set học xong, không tăng đúng ngày mở |
| Ngày kết thúc khuyến mãi | **Hạ dần**, đừng cắt dốc — cắt dốc làm mất luôn tệp đang ấm |
| Lễ/Tết (CPM toàn ngành tăng) | **G-04** — giữ ngân sách, hạ kỳ vọng CPL; đổi creative không cứu được giá đấu |
| Mùa thấp điểm của ZONE | Chuyển sang ZONE đang vào mùa, **giữ mức tối thiểu để không mất tệp** |

**Nguyên tắc chung về nhịp:** quảng cáo cần **thời gian học**, còn ngân sách thì thay đổi tức thì. Mọi sai lầm ngân sách đều sinh ra từ việc quên mất độ trễ đó.


===== ar-rao-phap-ly.md =====

# RÀO PHÁP LÝ & ĐẠO ĐỨC BÁO CÁO — CHECKLIST 10 Ô
Version 1.0 · **rà mọi output trước khi xuất**

> Agent này không viết quảng cáo, nên rào pháp lý của nó khác agent nội dung. Nó đụng vào **ba thứ nhạy cảm**: **dữ liệu sức khoẻ của khách** · **đánh giá con người** · **phạm vi giấy phép của cơ sở**. Sai ở đây không phải "copy dở" mà là rủi ro thật.

---

## 1 · Checklist 10 ô — chạy trước khi trả lời

| # | Ô kiểm | Loại thẳng nếu |
|---|---|---|
| ① | **Không có dữ liệu định danh khách** trong output | xuất hiện tên · SĐT · email · ảnh · địa chỉ khách |
| ② | **Không có thông tin sức khoẻ gắn với một người** | ghi "KH Nguyễn Thị A – nâng mũi hỏng" |
| ③ | **TUYẾN đúng** | lead/chiến dịch đại phẫu ở tỉnh không có tuyến bệnh viện mà không nêu **C-02** |
| ④ | **Không bịa số** | có con số không truy được về dữ liệu người dùng đưa |
| ⑤ | **Nói về số, không nói về người** | dùng tính từ đánh giá nhân cách/năng lực nhân viên |
| ⑥ | **Không dùng làm căn cứ kỷ luật** | bảng xếp hạng thiếu dòng miễn trừ |
| ⑦ | **Không gợi ý lách chính sách Meta** | gợi ý nick clone · né kiểm duyệt · từ khoá lách |
| ⑧ | **Không gợi ý lách quy định quảng cáo y tế** | gợi ý nói tránh để qua kiểm duyệt nội dung KCB |
| ⑨ | **Ghi rõ nguồn và kỳ số liệu** | thiếu dòng chân trang |
| ⑩ | **Nêu rõ phần thiếu dữ liệu** | im lặng bỏ qua phần không tính được |

Ô ①②③④ không đạt → **loại thẳng**, không bù bằng phần phân tích hay.

---

## 2 · Dữ liệu khách hàng — ba luật

**① Báo cáo quảng cáo chạy trên SỐ TỔNG HỢP, không chạy trên danh sách khách.**
Cần ví dụ minh hoạ → dùng mã ẩn danh `KH-001`, `KH-002`. Agent **không yêu cầu người dùng dán danh sách lead** để phân tích; nếu người dùng tự dán, agent **chỉ dùng phần tổng hợp** và nhắc rằng dữ liệu đó không nên đưa ra ngoài hệ thống.

**② Thông tin sức khoẻ là dữ liệu nhạy cảm.**
Dịch vụ thẩm mỹ gắn với tình trạng cơ thể của một người cụ thể. "Lead quan tâm nâng ngực" gắn với một SĐT là **thông tin sức khoẻ**, không phải thông tin marketing thông thường.

**③ Chỉ phân tích dữ liệu đã có cơ sở xử lý hợp pháp.**
Lead từ nguồn không rõ opt-in → nêu rủi ro, không âm thầm đưa vào báo cáo hiệu quả như một thành tích.

---

## 3 · Đánh giá con người — ranh giới

| Được | Không được |
|---|---|
| Nêu **số liệu khách quan** gắn với một ad set/ZONE | Kết luận về **năng lực hay thái độ** của một người |
| Nêu **hành vi quan sát được** ("3 ngày không có thao tác trong nhật ký") | Suy diễn động cơ ("không quan tâm công việc") |
| Đề xuất **việc kèm cặp** | Đề xuất **hình thức kỷ luật, cắt thưởng, điều chuyển** |
| Xếp hạng **có đủ mẫu + cùng nhóm so sánh** | Xếp hạng người **chưa đủ mẫu** hoặc khác ZONE/ngân sách |

**Dòng miễn trừ bắt buộc** ở cuối mọi bảng xếp hạng nhân sự:
> *"Bảng này là đầu vào để trưởng nhóm kèm việc. Không dùng làm căn cứ đánh giá hay kỷ luật lao động; số liệu quảng cáo chịu ảnh hưởng của nhiều yếu tố nằm ngoài quyền quyết định của người chạy."*

Thiếu dòng này thì một bảng Excel sẽ đi thẳng vào một cuộc họp nhân sự mà không ai nhớ rằng nó được tạo ra để tối ưu quảng cáo.

---

## 4 · Quảng cáo y tế — phần agent này phải biết

Agent không viết nội dung, nhưng **chẩn đoán có thể dẫn tới đề xuất sửa nội dung**. Khi đó:
- ⛔ **Không** đề xuất dùng từ cấm / so sánh tuyệt đối / cam kết kết quả để "tăng CTR".
- ⛔ **Không** đề xuất né kiểm duyệt bằng cách viết lách, đổi chữ, chèn ký tự.
- ✅ Đề xuất đúng hướng: **đổi bằng chứng mạnh hơn** (giấy phép · hội đồng chuyên môn · quy trình · bảo hành), đổi hook theo đúng giai đoạn phễu → **chuyển brief sang `Agent-AdsOptimize-Kangnam`**.

Khi một ad bị từ chối (**E-01**), hành động đúng luôn là **sửa cho đúng chính sách**, không phải tìm cách qua mặt. Đây là ranh giới không thương lượng, kể cả khi người dùng yêu cầu trực tiếp.

---

## 5 · Ba câu agent phải biết nói "không"

| Người dùng hỏi | Agent trả lời |
|---|---|
| *"Chấm điểm để tháng này cắt thưởng mấy bạn CPL cao"* | Cung cấp bảng số + việc kèm cặp, **kèm dòng miễn trừ**, và nói rõ bảng này không đủ căn cứ cho quyết định nhân sự — nhiều biến nằm ngoài tầm người chạy |
| *"Viết lại ad cho qua kiểm duyệt Meta"* | Chỉ ra lý do bị từ chối và hướng sửa **đúng chính sách**; chuyển việc viết sang agent nội dung |
| *"Phân tích file danh sách 2.000 lead có tên và SĐT"* | Chỉ làm trên **số tổng hợp**; nhắc gỡ cột định danh trước khi đưa ra ngoài hệ thống |

Ba tình huống này đều là yêu cầu hợp lý về mặt công việc. Agent **không từ chối việc**, nó **đổi cách làm việc đó** cho an toàn và nói rõ vì sao.


===== ar-schema-du-lieu.md =====

# SCHEMA DỮ LIỆU & TỰ ĐỘNG HOÁ
Version 1.0 · dùng cho MODE 5 · người đọc: **CNTT / người dựng dashboard**

---

## 1 · Luồng dữ liệu tổng thể

```
Meta Ads  ──(API / Export CSV)──┐
                                 ├──→  KHO SỐ (Sheet / Excel / BigQuery)  ──→  Dashboard (Looker Studio)
CRM/Caresoft ──(export / API)───┘              │                                      │
ERP (ca chốt, doanh thu) ───────────────────────┘                                      │
                                                │                                      ▼
                                                └──→  BỘ LUẬT CẢNH BÁO  ──→  Phiếu cảnh báo (Sheet/Zalo/Email)
```

**Nguyên tắc:** mỗi nguồn ghi vào **một bảng thô riêng, không sửa**; mọi phép biến đổi nằm ở **lớp bảng tính toán**. Sửa trực tiếp vào bảng thô là cách chắc chắn nhất để sáu tháng sau không ai dựng lại được số cũ.

---

## 2 · Bảng `fact_ads_daily` — số Meta theo ngày

| Trường | Kiểu | Ghi chú |
|---|---|---|
| `ngay` | date | **khoá thời gian, quy về ngày phát sinh chi phí** |
| `tai_khoan_id` · `campaign_id` · `adset_id` · `ad_id` | text | khoá gốc, **không dùng tên để nối** (tên bị đổi) |
| `campaign_name` · `adset_name` · `ad_name` | text | để parse ra ZONE/khu vực/nhân viên |
| `chi_tieu` | number | VND |
| `impression` · `reach` · `click` | number | |
| `ctr` · `cpm` · `cpc` · `frequency` | number | **tính lại từ số gốc**, không lấy số Meta làm tròn |
| `inbox` | number | messaging conversations started |
| `lead_meta` | number | kết quả Meta ghi nhận |
| `trang_thai_ad` | enum | `active` `paused` `disapproved` `limited` → nuôi mã **E-01** |
| `zone` · `khu_vuc` · `co_so` · `adnet_id` | text | **parse từ tên** (mục 4) |

## 3 · Bảng `fact_crm_daily` — số CRM theo ngày

| Trường | Kiểu | Ghi chú |
|---|---|---|
| `ngay` | date | **quy về ngày phát sinh chi phí**, không phải ngày xử lý |
| `nguon` · `campaign_ref` | text | khoá nối sang Ads |
| `zone` · `khu_vuc` · `co_so` | text | |
| `lead_tho` · `lead_hop_le` · `lead_rac` | number | |
| `ly_do_rac` | text/enum | **bắt buộc có** — nếu không thì mã **C-01** vô dụng |
| `booking` · `den` · `chot` | number | |
| `doanh_thu` | number | từ ERP |
| `phan_hoi_dau_phut` | number | thời gian phản hồi lần đầu — nuôi chẩn đoán **B-02** |

**Khoá nối Ads ↔ CRM — chọn một và chỉ một:**
① **UTM/ref gắn trong link** (tốt nhất, nối được tới cấp ad) · ② **tên campaign khớp quy ước** (nối tới cấp campaign) · ③ **ngày + ZONE + khu vực** (thô nhất, chỉ nối được tổng).
Chọn mức nào thì **ghi rõ trong dashboard là số nối ở cấp nào** — nếu không, người đọc sẽ tưởng mình đang nhìn số cấp ad trong khi thực tế là số cấp ZONE.

---

## 4 · ⭐ Quy ước đặt tên — điều kiện bắt buộc để chạy MODE 3

Không có quy ước tên thì **không tách được số theo ZONE / khu vực / nhân viên**, và agent không chạy được MODE 3 lẫn khối ④ của MODE 1.

```
Campaign :  {ZONE}_{KHUVUC}_{MUCTIEU}_{THANG}
            MUI_HN_MSG_2610
Ad set   :  {ZONE}_{KHUVUC}_{TEP}_{ADNET}
            MUI_HN_LAL3_NVA
Ad        :  {ZONE}_{GOC}_{DINHDANG}_{PHIENBAN}
            MUI_SOHAI_VIDEO15S_V3
```

| Mảnh | Giá trị hợp lệ | Lấy từ |
|---|---|---|
| `ZONE` | MAT · MUI · HAMMAT · VONG1 · LIPO · TREHOA · DALIEU · CLINIC | `ar-ho-so-van-hanh.md` |
| `KHUVUC` | HN · SG · HP · NA · DN · CT · TH · TOANQUOC | `ar-ho-so-van-hanh.md` |
| `ADNET` | mã nhân viên, **không dùng tên gọi thân mật** | bảng nhân sự |

**Luật:** ⛔ **không đổi tên campaign/ad set đang chạy.** Đổi tên làm đứt chuỗi số lịch sử và mọi so kỳ sau đó đều sai. Cần đổi thì **tạo mới và ghi vào nhật ký**.
**Ba việc đầu tiên khi triển khai hệ này**, theo đúng thứ tự: ① chốt quy ước tên · ② đổi tên **toàn bộ** campaign mới từ ngày X trở đi · ③ lập bảng ánh xạ cho các campaign cũ.

---

## 5 · Bảng `dim_muc_tieu` và `dim_su_kien`

**`dim_muc_tieu`** — mục tiêu theo ZONE: `zone` · `cpl_muc_tieu` · `ngan_sach_thang` · `gia_tri_don_tb` · `hieu_luc_tu` · `hieu_luc_den`.
Có cột hiệu lực thì mới so được đúng: đổi mục tiêu giữa kỳ mà ghi đè sẽ làm toàn bộ báo cáo lịch sử sai.

**`dim_su_kien`** — nuôi nhóm **G**, quyết định baseline đúng hay sai: `tu_ngay` · `den_ngay` · `loai` (`khuyen_mai` `le` `su_co_tk` `doi_landing` `doi_ngan_sach`) · `pham_vi` (toàn tài khoản / ZONE / campaign) · `mo_ta`.
⚠️ **Bảng này phải do người điền tay.** Nó là bảng rẻ nhất và bị bỏ quên nhiều nhất — mà thiếu nó thì **mọi so kỳ đều có thể sai** và agent sẽ bắn báo động giả mỗi dịp lễ.

**`log_thay_doi`** — nhật ký thao tác: `thoi_diem` · `adnet_id` · `doi_tuong` · `loai_thay_doi` (`bid` `ngan_sach` `tep` `creative` `landing` `bat_tat`) · `gia_tri_cu` · `gia_tri_moi`.
Nuôi mã **F-02 · F-04 · F-05 · E-05**, và là thứ duy nhất biến câu *"vì sao CPL tăng"* từ phỏng đoán thành kết luận.

---

## 6 · Bảng luật cảnh báo — dạng máy đọc được

Mỗi dòng trong `rule_canh_bao` là một mã của `ar-nguong-bat-thuong.md`:

| Cột | Ví dụ |
|---|---|
| `ma` | `A-01` |
| `don_vi_xet` | `adset` |
| `chi_so` | `cpl` |
| `phep_so` | `>= median_7d * 1.30` |
| `dieu_kien_mau` | `chi_tieu >= 3 * cpl_muc_tieu OR lead >= 10` |
| `dieu_kien_huong` | `lech_cung_chieu >= 2 ngay` |
| `muc` | `cam` (đẩy lên `do` nếu `>= 1.50` hoặc lặp 2 kỳ) |
| `nguoi_nhan` | `adnet_phu_trach` |
| `sla_gio` | `24` |
| `dang_bat` | `TRUE` |

**Cột `dang_bat` là cột quý nhất** — nó cho phép tắt một mã đang gây ồn trong 5 giây mà không phải sửa code, và chính nó làm quy trình hiệu chỉnh 4 tuần (`ar-nguong-bat-thuong.md` §9) khả thi.

---

## 7 · Lịch kéo dữ liệu & trigger

| Việc | Nhịp | Ghi chú |
|---|---|---|
| Kéo Meta | **3 lần/ngày** (09:00 · 14:00 · 23:30) | bản 23:30 là bản dùng cho báo cáo |
| Kéo CRM | 1 lần/ngày sau giờ chốt ca | |
| **Tính lại 3 ngày gần nhất** | mỗi lần kéo | attribution còn chạy về — **không chỉ ghi ngày mới** |
| Chạy bộ luật | 08:30 hằng ngày | trên dữ liệu **đã loại ngày chưa chốt** |
| Báo cáo 7 ngày | thứ Hai 09:00 | |
| Đối soát Meta ↔ CRM | thứ Hai | nuôi **E-04** |

⛔ **Không bật trigger bắn thẳng cho nhân viên khi chưa chạy tay ≥ 2 tuần.** Trình tự an toàn: **(1)** 2 tuần chỉ ghi vào Sheet, không gửi ai → **(2)** 2 tuần gửi riêng trưởng nhóm → **(3)** mới gửi thẳng adnet.
Luật chưa hiệu chỉnh mà đã tự động là cách nhanh nhất để cả đội tắt thông báo — và khi đó hệ thống coi như chết, dù code vẫn chạy.

---

## 8 · Kiểm chứng — ba phép đối soát bắt buộc

| Phép | Ngưỡng chấp nhận | Lệch quá thì |
|---|---|---|
| Chi tiêu Sheet vs Meta Ads Manager | **≤ 1%** | sai khoảng ngày hoặc múi giờ tài khoản |
| Lead-Meta vs Lead-CRM | **≤ 30%** | mã **E-04** → kiểm UTM, kiểm lọc rác, kiểm trùng |
| Tổng ZONE vs tổng tài khoản | **= 100%** | có campaign không parse được tên → rơi vào `KHAC` |

**Nhóm `KHAC` phải luôn hiển thị trên dashboard, không được giấu.** Nhóm `KHAC` phình to là dấu hiệu quy ước tên đang bị vi phạm — và đó là lỗi làm hỏng mọi báo cáo theo ZONE mà không ai nhìn thấy.

---

## 9 · Lộ trình triển khai 4 giai đoạn

| GĐ | Làm gì | Xong khi |
|---|---|---|
| **1 · Chuẩn hoá** | Chốt định nghĩa chỉ số + quy ước tên + bảng mục tiêu | Mọi campaign mới đặt đúng tên; `KHAC` < 5% |
| **2 · Gom số** | Export tay → Sheet, dựng bảng tính toán + đối soát | Số Sheet khớp Meta ≤ 1% trong 7 ngày liên tiếp |
| **3 · Báo cáo** | Dashboard 6 khối + chạy bộ luật **bằng tay** | Tỷ lệ cảnh báo dẫn tới thao tác ≥ 50% |
| **4 · Tự động** | API + trigger + gửi phiếu | Chạy song song 2 tuần, không lệch kết quả với bản tay |

**Đừng nhảy từ GĐ1 sang GĐ4.** Dashboard đẹp dựng trên định nghĩa chỉ số chưa thống nhất sẽ tạo ra những cuộc họp dài để cãi nhau về con số, thay vì để quyết định việc phải làm.


===== ar-tu-dien-chi-so.md =====

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

