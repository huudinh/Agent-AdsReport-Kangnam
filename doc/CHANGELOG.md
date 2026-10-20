# CHANGELOG & LÝ DO THIẾT KẾ

---

## v1.0 — 2026-10-20 · bản đầu

Dựng từ bản vẽ tay yêu cầu: *báo cáo FB / dashboard → nhận biết vấn đề*, chọn kỳ 7/14 ngày, theo dõi Inbox · Lead · Booking · Chi phí, CPL trung bình 7 ngày gần nhất, diễn biến theo dịch vụ, so sánh các kỳ, hiệu quả nhân viên, cảnh báo bất thường, quản lý ngân sách, và lộ trình **Meta → Excel → báo cáo / Data Studio → lấy tự động bằng trigger**.

Kiến trúc theo đúng chuẩn các agent anh em: **lõi brand-neutral** (`SYSTEM-PROMPT.md`) + **module thương hiệu tách riêng** (`ar-ho-so-van-hanh.md`, `ar-rao-phap-ly.md`) → đổi thương hiệu chỉ thay 2 file.

---

## Mười quyết định thiết kế và lý do

### ① Ba cổng chặn báo động giả đứng TRƯỚC bộ luật ngưỡng
Một hệ cảnh báo chết không phải vì bỏ sót, mà vì **bắn quá nhiều**. Sau hai tuần nhận 20 thông báo mỗi sáng, cả đội sẽ tắt thông báo — và lúc đó hệ thống coi như đã chết dù code vẫn chạy.
→ Chỉ số sức khoẻ của chính hệ cảnh báo: **tỷ lệ cảnh báo dẫn tới thao tác thật ≥ 50%**.

### ② Baseline dùng TRUNG VỊ, không dùng trung bình
Một ngày CPL 2 triệu do hết ngân sách sẽ kéo lệch trung bình và làm hỏng **mọi so sánh sau đó**. Trung vị miễn nhiễm với chuyện này.

### ③ Thêm cửa sổ "3 ngày cuối" bên cạnh kỳ 7 ngày
Phát hiện khi chạy thử: ad set có CPM leo đều 4 ngày cuối chỉ hiện **+15,3%** trên trung bình 7 ngày — **dưới mọi ngưỡng**, không bắn gì. Nhưng 3 ngày cuối đã **+36,4%**.
Trung bình kỳ làm loãng đúng thứ nguy hiểm nhất: **xu hướng đang leo**. Doctrine §4③ đã nói *"ba ngày nhích đều mỗi ngày 10% nguy hiểm hơn một ngày nhảy vọt"* — cửa sổ 3 ngày là cách thực thi câu đó bằng số.

### ④ Luật tầng rò: mỗi đơn vị chỉ MỘT phiếu
Khi inbox→lead tụt, thì CPL, CPB, CAC đều xấu theo. Bắn bốn phiếu cho bốn phòng ban là cách nhanh nhất để bốn phòng đổ lỗi cho nhau trong hai tuần.
→ Chỉ phiếu của **tầng đầu tiên** được xuất; các tầng dưới ghi là *"hệ quả kéo theo"*.

### ⑤ Khử phiếu A-01 khi đã tách được thành phần
CPL là **triệu chứng tổng hợp**. Phân rã xong mà vẫn giữ cả phiếu CPL lẫn phiếu thành phần thì **một nguyên nhân bị báo hai lần dưới hai cái tên** — và người nhận sẽ sửa hai chỗ cho một vấn đề.

### ⑥ C-02 (sai TUYẾN) bỏ qua mọi điều kiện cỡ mẫu
Đây là mã duy nhất như vậy. Nó không phải vấn đề hiệu suất mà là **rủi ro vượt phạm vi giấy phép**. Và trớ trêu là ad set loại này thường có **CPL rẻ** — đó chính là lý do nó tồn tại lâu mà không ai hỏi.

### ⑦ Nhóm E quét trước tất cả, và có quyền đóng băng mọi kết luận khác
Phân tích trên số sai **còn tệ hơn không phân tích**: nó khiến người ta đi sửa thứ đang chạy tốt.

### ⑧ Nhóm G là nhóm CHẶN, không phải nhóm BẮN
G-02 (cuối tuần) và G-04 (CPM toàn ngành) tồn tại để **hạ mức hoặc huỷ** cảnh báo khác. Chúng là cách phân biệt *"đội mình làm hỏng"* với *"cả thị trường đắt lên"* — và không ai sửa được chuyện thứ hai bằng cách đổi creative.

### ⑨ Bảng xếp hạng nhân sự đặt CUỐI dashboard, kèm dòng miễn trừ
Dashboard mở ra là thấy bảng xếp hạng người thì cả đội sẽ tối ưu cho **thứ hạng**, không tối ưu cho **kết quả** — và cách dễ nhất để lên hạng là **chọn ZONE dễ**, không phải chạy giỏi hơn.
Ngôn ngữ bắt buộc: nói về **hành vi và số liệu**, không nói về **con người**.

### ⑩ Không bật trigger tự động trước 2 tuần chạy tay
Luật chưa hiệu chỉnh mà đã tự động = giết niềm tin vào hệ thống ngay từ tuần đầu. Trình tự: ghi vào Sheet 2 tuần → gửi riêng trưởng nhóm 2 tuần → mới gửi thẳng adnet.

---

## Việc còn treo

| # | Việc | Ai chốt | Chặn cái gì |
|---|---|---|---|
| 1 | **CPL mục tiêu thật theo 8 ZONE** — hiện là `[CHỜ CẬP NHẬT]`, file `muc-tieu-zone.json` đang để **số giả** | Trưởng nhóm Adnet + CEO dịch vụ | Cột *Đạt?* trong báo cáo; cổng đủ mẫu theo bội số CPL |
| 2 | **Bảng ánh xạ `adnet_id` → ZONE/khu vực** | Trưởng nhóm Adnet | **Toàn bộ MODE 3** và mã F |
| 3 | **Quy ước đặt tên campaign** — chốt rồi áp từ ngày X, lập bảng ánh xạ cho campaign cũ | Adnet + CNTT | Khối ZONE, mã C-02, mã F, mã H |
| 4 | **Công suất booking/ngày theo cơ sở** | Vận hành | Mã H-04; luật điều chuyển ngân sách |
| 5 | **Danh sách lý do lead rác, dạng mã đóng** | CRM + Trực page | Mã C-01 (hiện không tách được rác theo lý do) |
| 6 | **Cửa sổ attribution đang dùng** (7d click / 1d view?) | CNTT | Mọi so sánh lịch sử — đổi cửa sổ là phải tính lại hết |
| 7 | **Hiệu chỉnh ngưỡng sau 4 tuần chạy tay** | Trưởng nhóm | Chất lượng toàn bộ hệ cảnh báo |
| 8 | Ngưỡng B-03 cho **ZONE đại phẫu** phải tính theo **cohort lead 30 ngày**, chưa cài trong tool | Adnet + CNTT | Mã B-03 đang đọc sai cho ZONE chu kỳ dài |

**Việc 8 là hạn chế đã biết của `build_ads_alert.py` v1.0:** tool tính `lead→booking` theo booking phát sinh trong kỳ. Với ZONE đại phẫu (chu kỳ quyết định 1–6 tháng) cách tính này làm tỷ lệ trông thấp giả tạo. Đến khi sửa, **đọc B-03 của ZONE đại phẫu như một chỉ báo, không như một kết luận** — `ar-ho-so-van-hanh.md` §3 có ghi cảnh báo này.

---

## Giới hạn đã biết của bản v1.0

| Giới hạn | Ảnh hưởng |
|---|---|
| Tool không đọc trực tiếp Meta API | Phải export tay hoặc qua Supermetrics; MODE 5 có đặc tả để tự động hoá |
| Chưa có `log_thay_doi` | Mã F-02 · F-04 · F-05 · E-05 **chưa chạy được bằng tool**, chỉ chạy được khi hỏi agent và đính kèm nhật ký |
| Chưa có GA/landing data | Mã E-07 (điểm đến hỏng) phải kiểm tay |
| B-03 chưa theo cohort | Xem việc còn treo #8 |
| Chưa đối soát đa tài khoản | Tool gộp mọi dòng trong file; nhiều tài khoản thì tách file hoặc thêm cột và lọc trước |
