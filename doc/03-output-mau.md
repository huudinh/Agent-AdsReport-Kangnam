# 03 · OUTPUT MẪU

> Toàn bộ số dưới đây là **kết quả chạy thật** của `tools/build_ads_alert.py` trên
> [`template/MAU_du-lieu-ads.csv`](../template/MAU_du-lieu-ads.csv) (dữ liệu giả, 28 ngày × 8 ad set).
> Lệnh: `python tools/build_ads_alert.py template/MAU_du-lieu-ads.csv --muc-tieu template/muc-tieu-zone.json`

---

## MODE 1 — DASHBOARD

### ① Tóm tắt

```
Kỳ báo cáo:   12/10 – 18/10/2026 (7 ngày · 2 ngày cuối tuần)
Baseline:     median theo ngày của 28/09 – 11/10/2026
Tổng chi:     576,6tr   (kỳ trước 604,5tr · −4,6%)
Lead hợp lệ:  2.051     (kỳ trước 2.250 · −8,8%)
CPL:          281k      (kỳ trước 269k · +4,6%)
Booking:      775       (kỳ trước 844 · −8,2%)

➜ KẾT LUẬN: 1 cảnh báo 🔴 phải xử lý trong 4 giờ — C-02, ZONE MUI × khu vực DN.
```

### ② Phễu 8 tầng

| Tầng | Kỳ này | Kỳ trước | Tỷ lệ chuyển tiếp | ± | Chủ sở hữu |
|---|---|---|---|---|---|
| ① Chi phí | 576,6tr | 604,5tr | — | −4,6% | Adnet / Trưởng nhóm |
| ② Hiển thị | 3.026.001 | 3.297.256 | CPM 191k | −8,2% | Adnet (tệp + bid) |
| ③ Click | 65.396 | 71.293 | CTR 2,16% | −8,3% | Adnet (creative) |
| ④ Inbox | 8.946 | 9.443 | Click→Inbox 13,68% | −5,3% | Adnet (điểm đến) |
| ⑤ Lead | 2.051 | 2.250 | Inbox→Lead 22,9% | −8,8% | TRỰC PAGE |
| ⑥ Booking | 775 | 844 | Lead→Booking 37,8% | −8,2% | TELESALES |
| ⑦ Đến | 529 | 583 | Show-rate 68,3% | −9,3% | LỄ TÂN / CSKH |
| ⑧ Chốt | 147 | 163 | Đến→Chốt 27,8% | −9,8% | Tư vấn tại cơ sở |

**Không tầng nào bị đánh dấu ⚠ ở cấp tài khoản** — mọi tỷ lệ chuyển tiếp đều giữ nguyên, số giảm đều theo chi tiêu. Đây là kết luận đúng và quan trọng: **vấn đề nằm ở cấp ad set, không nằm ở cấp phễu tổng.** Nhìn mỗi bảng này mà kết luận "cả đội đi xuống" là sai.

### ④ Theo ZONE

| ZONE | Chi | Share NS | Lead | Share lead | CPL | Mục tiêu | Đạt? | Lead→Book | Lệch NS–lead |
|---|---|---|---|---|---|---|---|---|---|
| MUI | 279,1tr | 48,4% | 719 | 35,1% | 388k | 420k | ✅ | 34,5% | **13,3 điểm %** |
| MAT | 149,4tr | 25,9% | 582 | 28,4% | 257k | 330k | ✅ | 37,3% | −2,5 điểm % |
| VONG1 | 55,3tr | 9,6% | 78 | 3,8% | 709k | 480k | ❌ | 33,3% | 5,8 điểm % |
| LIPO | 50,5tr | 8,8% | 98 | 4,8% | 515k | 520k | ✅ | 31,6% | 4,0 điểm % |
| DALIEU | 42,3tr | 7,3% | 574 | 28,0% | 74k | 120k | ✅ | 45,2% | **−20,7 điểm %** |

Hai ô đáng chú ý nằm ở **cột cuối**, không nằm ở cột CPL: DALIEU mang về 28% lead bằng 7,3% ngân sách, còn MUI ăn 48,4% ngân sách để ra 35,1% lead.

---

## MODE 2 — CẢNH BÁO (6 phiếu)

### 🔴 C-02 · ZONE MUI × khu vực DN (1 ad set)

| Ô | Nội dung |
|---|---|
| ③ Số liệu | 103 lead đại phẫu ngoài tuyến bệnh viện · baseline 0 (chỉ HN · SG) · chi 31,8tr |
| ④ Tầng rò | ⚠ Ràng buộc TUYẾN — **không phải vấn đề hiệu suất** |
| ⑤ Chẩn đoán | ZONE đại phẫu chạy ở khu vực chỉ có viện thẩm mỹ. Nếu thông điệp mời thực hiện tại đó thì đây là rủi ro **vượt phạm vi giấy phép** |
| ⑥ Hành động | Chọn MỘT: ① sửa thông điệp thành *"tư vấn/đặt khám tại cơ sở tỉnh, phẫu thuật tại tuyến bệnh viện"*; hoặc ② loại trừ tỉnh khỏi targeting. **Không có cách thứ ba** |
| ⑦ Ai + hạn | Adnet + Trưởng nhóm + Pháp chế · **4 giờ làm việc** |

> Mã này **bỏ qua mọi điều kiện cỡ mẫu** — một lead cũng bắn. CPL của ad set đó đang rẻ, và đó chính là lý do nó tồn tại lâu mà không ai hỏi.

### 🟠 A-02 · MUI_HN_LAL3_NVA — **đang leo**

| Ô | Nội dung |
|---|---|
| ③ Số liệu | CPM **(3 ngày cuối)** 282k vs median 14 ngày 207k · **+36,4%** · chi 63,5tr · 522 inbox · 107 lead |
| ④ Tầng rò | ② Hiển thị |
| ⑤ Chẩn đoán | ⚠ **ĐANG LEO** — 3 ngày cuối lệch 36,4% trong khi cả kỳ 7 ngày mới 15,3%: trung bình kỳ đang làm loãng xu hướng. Hệ quả kéo theo: A-03 (CPI) |
| ⑥ Hành động | Kiểm trùng tệp giữa ad set (E-06) · mở rộng tệp · hạ trần bid |
| ⑦ Ai + hạn | Adnet phụ trách · 24 giờ |

> Đây là phiếu minh hoạ rõ nhất giá trị của cửa sổ 3 ngày: nhìn trung bình 7 ngày thì chỉ +15,3%, **chưa chạm ngưỡng cảnh báo nào**. Nhưng ba ngày gần nhất đang leo đều và sẽ thành vấn đề thật trong tuần tới.
> **Phiếu A-01 (CPL) của chính ad set này đã bị khử** — phân rã CPL chỉ về đúng CPM, nên giữ phiếu nguyên nhân, bỏ phiếu triệu chứng.

### 🟠 D-01 · VONG1_SG_RT_NVD

| Ô | Nội dung |
|---|---|
| ③ Số liệu | Frequency **2,83** (trần 2,5) · CTR 1,24% vs 1,67% · **CTR −25,6%** · chi 23,2tr |
| ⑤ Chẩn đoán | Frequency vượt trần **VÀ** CTR trôi → bão hoà tệp thật *(frequency cao mà CTR giữ nguyên thì **không** phải bão hoà)* |
| ⑥ Hành động | Bật challenger mới · mở rộng hoặc đổi tệp, **giữ nguyên creative** để đọc được kết quả |
| ⑦ Ai + hạn | Adnet phụ trách · 24 giờ |

### 🟠 A-05 · LIPO_HN_BROAD_NVE — chi hụt

| Ô | Nội dung |
|---|---|
| ③ Số liệu | Chi thực tế / ngân sách đặt = **60,1%** (ngưỡng ≥70%) · chi 50,5tr |
| ⑤ Chẩn đoán | Không tiêu hết tiền = **mất phễu**, nhưng không ai thấy vì "không tốn tiền". Thường do: tệp quá hẹp · bid trần thấp · ad vừa bị từ chối |
| ⑥ Hành động | Kiểm **E-01 trước** · mở rộng tệp hoặc nâng trần bid từng bước ≤20% |

### 🟡 B-02 · MAT_HN_INT_NVB — tầng rò ⑤

| Ô | Nội dung |
|---|---|
| ③ Số liệu | Inbox→Lead **19,1%** vs median 25,2% · **−24,0%** · chi 82,6tr · 1.600 inbox · 306 lead |
| ④ Tầng rò | **⑤ Lead — TRỰC PAGE**, không phải Ads |
| ⑥ Hành động | Đo thời gian phản hồi lần đầu theo khung giờ · xếp lại ca tối/cuối tuần · rà điểm xin số trong kịch bản |
| ⑦ Ai + hạn | **TRỰC PAGE** · rà ở phiên 7 ngày |

> Ad set này cũng có CPL tăng, nhưng **phiếu A-01 đã bị khử**: phân rã CPL chỉ thẳng về `inbox→lead`. Gửi cảnh báo "CPL tăng" cho Adnet ở đây là gửi sai người — họ sẽ đi sửa creative cho một vấn đề nằm ở xếp ca trực page.

### 🟡 H-03 · ZONE DALIEU

Share ngân sách **7,3%** · share lead **28,0%** · lệch **20,7 điểm %**.
Chẩn đoán kết bằng một câu hỏi, không bằng một kết luận: ***"Đây là chủ ý hay quán tính?"*** Chủ ý thì ghi vào `dim_su_kien` để kỳ sau không bắn lại.

---

## Mục ⚪ THEO DÕI

Kỳ này trống. Khi có, mỗi dòng ghi rõ **trượt cổng nào** — ví dụ:
```
A-01 · MUI_SG_RT_NVF · CPL +34% · cổng ① chưa đủ mẫu (chi 4,1tr · 11 inbox · 3 lead)
```
Dòng này **không phải cảnh báo**. Nó ở đây để tuần sau, khi đủ mẫu, không ai ngạc nhiên.

---

## Điều quan trọng nhất trong output mẫu này

Dữ liệu mẫu có **8 ad set**, trong đó `DALIEU_DN_BROAD_NVC` chạy hoàn toàn bình thường.
**Nó không nhận cảnh báo nào.** Một bộ luật bắn vào cả ad set đang chạy tốt thì sau hai tuần sẽ không còn ai đọc cảnh báo nữa — và lúc đó hệ thống coi như đã chết, dù code vẫn chạy mỗi sáng.
