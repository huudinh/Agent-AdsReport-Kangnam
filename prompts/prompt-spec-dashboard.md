# PROMPT — ĐẶC TẢ DASHBOARD & TỰ ĐỘNG HOÁ (MODE 5)

> Dành cho **CNTT / người dựng** Looker Studio · Google Sheet · Excel.

```
MODE 5 — SPEC

Hiện trạng:
- Nguồn số đang có: [Meta Ads Manager export tay / API / Supermetrics · Caresoft · ERP]
- Nơi muốn hiển thị: [Looker Studio / Google Sheet / Excel]
- Quy ước đặt tên campaign hiện tại: [có / chưa có / không thống nhất]
- Ai sẽ nhận cảnh báo: [___]

Xuất đủ 6 phần:
① Nguồn & trường dữ liệu + khoá nối Ads ↔ CRM (nói rõ nối được ở CẤP nào)
② Công thức từng chỉ số
③ Lịch kéo dữ liệu & trigger
④ Bảng luật cảnh báo dạng máy đọc được (mã · điều kiện · mức · người nhận · dang_bat)
⑤ Bố cục dashboard theo thứ tự ra quyết định
⑥ Ba phép đối soát bắt buộc + ngưỡng chấp nhận

Kèm lộ trình 4 giai đoạn và điều kiện mở khoá từng giai đoạn.
```

---

## Câu hỏi mở màn tốt nhất cho dự án này

```
Chúng tôi đang export tay từ Meta sang Excel mỗi tuần, muốn tiến tới cảnh báo tự động.
Cần giải những đề bài nào trước? Xếp theo mức chặn, nói rõ ai sở hữu từng cái.
```

Agent sẽ luôn nhấn hai việc đứng trước mọi thứ khác: **chốt định nghĩa chỉ số** và **chốt quy ước đặt tên**. Dashboard dựng trên định nghĩa chưa thống nhất chỉ tạo ra những cuộc họp cãi nhau về con số thay vì quyết định việc phải làm.

---

## Hai câu hỏi kỹ thuật thường gặp

```
Số lead trên Meta và số lead trong CRM đang lệch 40%. Nên tin số nào, và sửa từ đâu?
```
```
Dựng bảng luật cảnh báo dạng máy đọc được cho 10 mã đáng bật trước nhất,
kèm cột dang_bat để tắt nhanh mã gây ồn.
```

---

## Công cụ có sẵn trong repo

Trước khi dựng dashboard, chạy thử bộ luật bằng [`tools/build_ads_alert.py`](../tools/build_ads_alert.py) trên export thật **2–4 tuần**. Nó xuất đúng 6 khối báo cáo và một sheet *Luật* liệt kê ngưỡng đang dùng — dùng chính sheet đó để hiệu chỉnh trước khi đưa luật vào hệ thống.
