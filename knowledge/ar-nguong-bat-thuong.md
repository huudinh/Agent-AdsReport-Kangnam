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
