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
