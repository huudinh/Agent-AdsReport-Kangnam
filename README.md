# 📊 Agent-AdsReport-Kangnam

> Version 1.0 · AI **đọc số Meta + CRM → dựng báo cáo 7/14 ngày → phát hiện bất thường → chỉ đúng người phải xử lý và hạn bao lâu** cho **đội Adnet** của Hệ thống Bệnh viện Thẩm mỹ Kangnam.

Kiến trúc **lõi brand-neutral** ([`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md)) + **module thương hiệu tách riêng** ([`knowledge/ar-ho-so-van-hanh.md`](knowledge/ar-ho-so-van-hanh.md)) → đổi thương hiệu chỉ cần thay 2 file, không sửa bộ não.

Gói anh em dùng chung kiến trúc: [`Agent-AdsOptimize-Kangnam`](../Agent-AdsOptimize-Kangnam/) (viết quảng cáo · landing · từ khoá) · [`Agent-CRM-Automation`](../Agent-CRM-Automation/) (chăm sóc · tái khai thác).

---

## Nguyên tắc tối thượng

> **LỆCH SỐ CHƯA PHẢI BẤT THƯỜNG.**
> Bất thường là lệch số **vượt ngưỡng · đủ mẫu · có hướng** — và **chỉ ra được ai phải làm gì.**

```
❌ "CPL hôm nay 450k, hôm qua 310k → cảnh báo CPL tăng 45%!"
   (1 ngày · 4 lead · Chủ nhật — đây là nhiễu, không phải tín hiệu)

✅ "Ad set [Mui-HN-LAL3] · CPM 3 ngày cuối 282k vs median 14 ngày 207k (+36,4%)
   · cả kỳ 7 ngày mới +15,3% → trung bình đang làm loãng xu hướng ĐANG LEO.
   CTR giữ nguyên → đấu giá đắt lên, KHÔNG phải creative hỏng.
   → Adnet: kiểm trùng tệp, mở rộng tệp, hạ trần bid. Hạn 24h."
```

**Phép thử trước khi xuất mọi cảnh báo:** *"Người nhận sáng mai mở máy lên thì bấm vào đâu, sửa cái gì?"* — không trả lời được thì đó chưa phải cảnh báo, đó mới là một con số.

**Thà bỏ sót một bất thường nhỏ còn hơn bắn 20 cảnh báo mỗi sáng.** Một hệ cảnh báo chết không phải vì bỏ sót, mà vì bắn quá nhiều: sau hai tuần, cả đội tắt thông báo.

---

## Agent này KHÔNG làm gì

Nó **không viết mẫu quảng cáo, không dựng landing page, không viết kịch bản tư vấn**. Nó chẩn đoán ra vấn đề rồi **chuyển brief** sang agent phụ trách.
Nó cũng **không ra quyết định nhân sự** — bảng hiệu quả adnet là đầu vào để trưởng nhóm kèm việc, kèm dòng miễn trừ bắt buộc.

---

## ⚠️ Ba cổng chặn báo động giả — chạy trước mọi cảnh báo

| Cổng | Điều kiện | Vì sao |
|---|---|---|
| ① **ĐỦ MẪU** | chi ≥ 3× CPL mục tiêu **hoặc** ≥30 inbox / ≥10 lead | Tắt một ad set đang tốt vì 2 ngày đầu xui là **lỗi tốn tiền nhất** |
| ② **ĐÚNG BASELINE** | **trung vị** 7 ngày của chính đơn vị đó, cuối tuần so cuối tuần | Một ngày CPL 2tr do hết ngân sách sẽ kéo lệch trung bình và làm hỏng mọi so sánh sau đó |
| ③ **CÓ HƯỚNG** | lệch ≥2 kỳ liên tiếp **hoặc** ≥50% ngay 1 kỳ | Một ngày nhảy rồi về chỗ cũ là nhiễu. **Ba ngày nhích đều mỗi ngày 10% nguy hiểm hơn nhiều** |

Không qua đủ 3 cổng → xuống mục **⚪ Theo dõi**, không được gọi là cảnh báo.
⛔ Số Meta **1–2 ngày gần nhất chưa chốt** → không ra cảnh báo trên ngày đó.

---

## Phễu 8 tầng — và cột quan trọng nhất

```
① Chi phí → ② Hiển thị → ③ Click → ④ Inbox → ⑤ Lead → ⑥ Booking → ⑦ Đến → ⑧ Chốt
└──────────────── ADS ────────────────┘ └──────── KHÔNG PHẢI ADS ────────┘
```

| Tầng | Chỉ số gác cổng | **Ai sở hữu** |
|---|---|---|
| ① Chi phí | chi tiêu · pacing | Adnet / Trưởng nhóm |
| ② Hiển thị | CPM · frequency | Adnet (tệp + bid) |
| ③ Click | CTR · CPC | Adnet (creative) |
| ④ Inbox | CPI · click→inbox | Adnet (điểm đến) |
| ⑤ Lead | **CPL · inbox→lead** | **Trực page** |
| ⑥ Booking | CPB · lead→booking | **Telesales** |
| ⑦ Đến | show-rate | **Lễ tân / CSKH** |
| ⑧ Chốt | CAC · đến→chốt | **Tư vấn tại cơ sở** |

**Luật quy trách nhiệm:** đi **từ trên xuống**, tìm **tầng ĐẦU TIÊN** lệch chuẩn. Mọi tầng dưới là **hệ quả** và **không được ra cảnh báo riêng**.

```
⛔ SAI LẦM KINH ĐIỂN
   "Booking giảm 30% → cắt ngân sách ads."
   Trong khi: inbox +12% · lead +8% · lead→booking tụt 34% → 19%.
   Tầng rò là ⑥ telesales; ads đang chạy TỐT HƠN tháng trước.
   Cắt ads = ít lead hơn mà tỷ lệ vẫn hỏng = mất doanh thu hai lần.
```

**Phân rã CPL trước khi kết luận** — bốn nguyên nhân, bốn người xử lý khác nhau:
```
CPL = CPM/1000 ÷ (CTR × click→inbox% × inbox→lead%)
```
| Thành phần xấu đi | Nghĩa là | Ai xử |
|---|---|---|
| CPM ↑ | đấu giá đắt lên / tệp hẹp / trùng tệp | Adnet (tệp, bid) |
| CTR ↓ | hook/creative yếu hoặc bão hoà | Adnet (creative) |
| click→inbox ↓ | điểm đến hỏng | Adnet + Kỹ thuật |
| inbox→lead ↓ | chậm trả lời, thiếu ca tối, kịch bản sai | **Trực page** |

---

## Tám nhóm bất thường · 30 mã

| Mã | Nhóm | Ví dụ |
|---|---|---|
| **A** | Chi phí | CPL/CPM/CPI vọt · vượt pacing · **chi hụt** |
| **B** | Rò phễu | CTR cao–inbox thấp · inbox nhiều–lead ít · booking nhiều–không đến |
| **C** | Chất lượng lead | lead rác tăng · **C-02 sai TUYẾN** 🔴 · lead trùng |
| **D** | Creative & bão hoà | frequency vượt trần + CTR trôi · thiếu challenger |
| **E** | Vận hành & kỹ thuật | ad bị từ chối · tracking chết · **lệch Meta ↔ CRM** |
| **F** | Nhân sự Adnet | CPL lệch median team · **ad set bị bỏ rơi** · tiền chảy về chỗ kém |
| **G** | Kỳ & mùa vụ | **hai mã CHẶN**: hiệu ứng cuối tuần · CPM toàn ngành |
| **H** | Dịch vụ & phân bổ | đổ tiền vào ZONE xấu · **bỏ đói ZONE tốt** |

**Nhóm E xử lý trước tất cả** — số sai thì mọi phân tích phía sau đều sai.
**Nhóm G không bắn, nó CHẶN** — đó là cách phân biệt *"đội mình làm hỏng"* với *"cả thị trường đắt lên"*.

Chi tiết ngưỡng: [`knowledge/ar-nguong-bat-thuong.md`](knowledge/ar-nguong-bat-thuong.md).

---

## Ba mức cảnh báo & SLA

| Mức | Điều kiện | SLA | Báo cho |
|---|---|---|---|
| 🔴 **ĐỎ** | ≥50% · hoặc 🟠 lặp 2 kỳ · hoặc **mọi mã E** · hoặc **C-02** | **4 giờ làm việc** | Adnet + Trưởng nhóm |
| 🟠 **CAM** | 30–50%, qua đủ 3 cổng | 24 giờ | Adnet phụ trách |
| 🟡 **VÀNG** | 20–30% | rà ở phiên 7 ngày | ghi nhận |
| ⚪ **THEO DÕI** | chưa qua đủ 3 cổng | không hành động | chỉ liệt kê |

**Cảnh báo không có tên người và hạn cụ thể = chưa xuất xong.** *"Đội adnet xem lại"* không phải là một người.

---

## Năm chế độ

| Mode | Làm gì | Input tối thiểu | Đầu ra |
|---|---|---|---|
| **1 · DASHBOARD** | Báo cáo 7/14 ngày | bảng số theo ngày | 6 khối: tóm tắt · phễu · CPL trượt · theo ZONE · so kỳ · cảnh báo |
| **2 · CẢNH BÁO** | Quét bất thường | ≥14 ngày × ad set | phiếu 7 ô, xếp 🔴→🟠→🟡 + mục Theo dõi |
| **3 · NHÂN SỰ** | Hiệu quả adnet | bảng có cột nhân viên | 5 trục + việc kèm cặp + dòng miễn trừ |
| **4 · NGÂN SÁCH** | Phân bổ / điều chuyển | ngân sách + CPL mục tiêu | đề xuất 6 ô, có ô **RỦI RO** |
| **5 · SPEC** | Đặc tả dashboard tự động | mô tả nguồn số | schema · công thức · trigger · bảng luật máy đọc được |

Mở phiên agent luôn hỏi chạy mode nào. Không nói thì nó tự suy và báo lại.

---

## Công cụ: quét dữ liệu → file Excel 6 sheet

```bash
pip install openpyxl
python tools/sinh_du_lieu_mau.py template/MAU_du-lieu-ads.csv          # dữ liệu mẫu để chạy thử
python tools/build_ads_alert.py template/MAU_du-lieu-ads.csv --muc-tieu template/muc-tieu-zone.json
```

```
✅ Đã xuất: out/BaoCao-CanhBao_Ads_1210_1810.xlsx
   Kỳ 12/10–18/10 · baseline 28/09–11/10
   Cảnh báo: 🔴 1 · 🟠 3 · 🟡 2   |   Theo dõi: 0
   ➜ 1 cảnh báo 🔴 phải xử lý trong 4 giờ — ưu tiên: C-02 (ZONE MUI × khu vực DN).
```

Tool cài đúng bộ luật của bộ não: quét nhóm E trước · ba cổng chặn · phân rã CPL · luật tầng rò · khử phiếu trùng. Nó đọc được **cả export tiếng Anh của Meta Ads Manager** lẫn file tiếng Việt.
Dữ liệu mẫu cài sẵn **6 tình huống**, trong đó tình huống thứ 6 là ad set **chạy bình thường** — có mặt để kiểm điều ngược lại: bộ luật **không được** bắn cảnh báo cho nó.

Kết quả chạy thật: [`doc/03-output-mau.md`](doc/03-output-mau.md).

---

## ⚠️ Ràng buộc cứng — kiểm trước mọi output

### ① TUYẾN cơ sở
**Đại phẫu chỉ tại tuyến bệnh viện:** Kangnam Hà Nội (190 Trường Chinh) · Kangnam Sài Gòn (666 CMT8). Năm viện thẩm mỹ tỉnh (Hải Phòng · Nghệ An · Đà Nẵng · Cần Thơ · Thanh Hóa) chỉ **tư vấn/tái khám + da/spa/tiểu phẫu**.

Chiến dịch ZONE đại phẫu nhắm tỉnh chỉ có viện thẩm mỹ, mà thông điệp vẫn mời thực hiện tại đó → **C-02 mức 🔴**, vì đây là **rủi ro vượt phạm vi giấy phép**, không phải chuyện lead kém.
Đây là **mã duy nhất bỏ qua mọi điều kiện cỡ mẫu — một lead cũng bắn**. Trớ trêu là ad set loại này thường có CPL rẻ, và đó chính là lý do nó tồn tại lâu mà không ai hỏi.

### ② Dữ liệu khách hàng
Output **không chứa tên · SĐT · ảnh · tình trạng bệnh**. Dịch vụ thẩm mỹ gắn với cơ thể một người cụ thể là **dữ liệu sức khoẻ**, không phải dữ liệu marketing thường. Cần ví dụ thì ẩn danh `KH-001`.

### ③ Nói về số, không nói về người
✅ *"Ad set X để CPL vượt ngưỡng 5 ngày, nhật ký không ghi thao tác nào"*
❌ *"bạn A lười / yếu / không có năng lực"*
Mọi bảng xếp hạng kết bằng dòng miễn trừ: **không dùng làm căn cứ đánh giá hay kỷ luật lao động.**

### ④ Không lách chính sách
Ad bị từ chối → **sửa cho đúng chính sách**. Không nick clone, không né kiểm duyệt, không lách quy định quảng cáo y tế. Ranh giới không thương lượng, kể cả khi được yêu cầu trực tiếp.

---

## Tài liệu

| File | Nội dung | Upload vào Knowledge? |
|---|---|---|
| [SYSTEM-PROMPT.md](SYSTEM-PROMPT.md) | **Bộ não** 19 mục | ✅ (ChatGPT: upload cả như file Knowledge) |
| [SYSTEM-PROMPT-NGAN.md](SYSTEM-PROMPT-NGAN.md) | Bản ngắn cho ChatGPT · **6.441 / 8.000 ký tự** | — dán vào Instructions |
| [knowledge/](knowledge/) | **9 file tri thức** | ✅ |
| [prompts/](prompts/) | **5 prompt vận hành** — câu lệnh để copy | ❌ |
| [tools/build_ads_alert.py](tools/build_ads_alert.py) | **Quét dữ liệu → workbook 6 sheet** | ❌ |
| [tools/sinh_du_lieu_mau.py](tools/sinh_du_lieu_mau.py) | Sinh dữ liệu mẫu có 6 tình huống cài sẵn | ❌ |
| [template/](template/) | File CSV mẫu · mục tiêu CPL theo ZONE · mô tả trường dữ liệu | ❌ |
| [goi/](goi/) | **Bản gộp dự phòng** — 1 file thay cho 9 file rời, dùng khi chạm trần số file của nền tảng | ✅ |
| [doc/01-cai-dat.md](doc/01-cai-dat.md) | Cài lên Claude / ChatGPT / Gemini + **7 câu thử** | ❌ |
| [doc/02-cau-lenh.md](doc/02-cau-lenh.md) | Công thức ra lệnh + 12 câu nói lời thường | ❌ |
| [doc/03-output-mau.md](doc/03-output-mau.md) | **Output chạy thật** trên dữ liệu mẫu | ❌ |
| [doc/04-prompt-nguoi-moi.md](doc/04-prompt-nguoi-moi.md) | 14 câu cho người chưa quen số liệu quảng cáo | ❌ |
| [doc/CHANGELOG.md](doc/CHANGELOG.md) | Lý do 10 quyết định thiết kế + **Việc còn treo** + giới hạn đã biết | ❌ |

**Chín file tri thức**

| File | Dùng để |
|---|---|
| `ar-rao-phap-ly.md` | **Checklist 10 ô — rà mọi output.** Dữ liệu khách · đánh giá người · phạm vi giấy phép |
| `ar-ho-so-van-hanh.md` | 7 cơ sở + **TUYẾN** · 8 ZONE + loại ZONE · cơ cấu đội Adnet · mục tiêu CPL |
| `ar-tu-dien-chi-so.md` | **Định nghĩa từng chỉ số bằng công thức** · 4 định nghĩa phải chốt bằng văn bản |
| `ar-nguong-bat-thuong.md` | **8 nhóm · 30 mã · ngưỡng · 3 mức · SLA** + quy trình hiệu chỉnh 4 tuần |
| `ar-cay-chan-doan.md` | **Triệu chứng → tầng rò → nguyên nhân → ai xử lý** + 4 cặp dễ nhầm nhất |
| `ar-khung-bao-cao.md` | 3 nhịp báo cáo · 6 khối · **đặc tả bố cục dashboard** |
| `ar-hieu-qua-nhan-vien.md` | 5 trục · **4 luật công bằng** · ngôn ngữ bắt buộc |
| `ar-quan-ly-ngan-sach.md` | Pacing · 4 luật cứng · công thức điểm ZONE · mẫu đề xuất 6 ô |
| `ar-schema-du-lieu.md` | Trường dữ liệu · **quy ước đặt tên** · bảng luật máy đọc được · lộ trình 4 giai đoạn |

---

## Bắt đầu

1. Cài theo [`doc/01-cai-dat.md`](doc/01-cai-dat.md) — khoảng 10 phút.
2. Chạy **7 câu thử** ở mục 6 của file đó để biết cài đúng chưa. Câu 1, 3 và 4 là ba câu quan trọng nhất.
3. Điền các ô `[CHỜ CẬP NHẬT]` trong [`knowledge/ar-ho-so-van-hanh.md`](knowledge/ar-ho-so-van-hanh.md) — ưu tiên **CPL mục tiêu theo ZONE** và **bảng ánh xạ adnet_id**.
4. Gõ `MODE 2` kèm export 14 ngày, hoặc nói bằng lời thường: *"Tuần này có gì bất thường không? Dữ liệu đây."*

Chưa quen số liệu quảng cáo → vào [`doc/04-prompt-nguoi-moi.md`](doc/04-prompt-nguoi-moi.md) trước.
Muốn dựng dashboard tự động → đọc [`knowledge/ar-schema-du-lieu.md`](knowledge/ar-schema-du-lieu.md) §9 và **đừng nhảy từ giai đoạn 1 sang giai đoạn 4**.

---

## Tự kiểm — 6 tiêu chí agent chạy trước khi trả

① Mọi số **truy được về dữ liệu người dùng đưa**? · ② Cảnh báo **qua đủ 3 cổng**? · ③ Đã xác định **tầng rò** trước khi quy trách nhiệm? · ④ Mỗi cảnh báo có **người + hạn + việc cụ thể**? · ⑤ Đã rà **TUYẾN + dữ liệu khách + ngôn ngữ về người**? · ⑥ Đã nói rõ **thiếu gì, chưa kết luận được gì**?

**Tiêu chí ① hoặc ⑤ không đạt → loại thẳng**, không bù bằng việc phân tích hay.
"# Agent-AdsReport-Kangnam" 
