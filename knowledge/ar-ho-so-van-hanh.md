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
