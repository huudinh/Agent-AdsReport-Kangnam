# MẪU DỮ LIỆU ĐẦU VÀO

File mẫu: [`MAU_du-lieu-ads.csv`](MAU_du-lieu-ads.csv) — 28 ngày × 8 ad set, sinh bằng
`python tools/sinh_du_lieu_mau.py`.

## Một dòng = một NGÀY × một AD SET

| Cột | Bắt buộc | Nguồn | Ghi chú |
|---|---|---|---|
| `ngay` | ✅ | Meta | `YYYY-MM-DD` hoặc `DD/MM/YYYY`. **Quy về ngày phát sinh CHI PHÍ** |
| `chi_tieu` | ✅ | Meta | VND |
| `campaign` · `adset` | nên có | Meta | thiếu `adset` thì script dùng `campaign` |
| `zone` · `khu_vuc` | nên có | parse từ tên | **thiếu → mất khối ZONE và mã C-02 / H** |
| `adnet` | nên có | parse từ tên | **thiếu → không chạy được MODE 3 và mã F** |
| `impression` · `reach` · `click` | nên có | Meta | thiếu `reach` → không có frequency → mất D-01 |
| `inbox` | nên có | Meta | messaging conversations started |
| `lead_meta` | tuỳ | Meta | dùng để đối soát E-04 |
| `lead` | nên có | **CRM** | lead hợp lệ đã lọc rác. Không có → script lùi về `lead_meta` và ghi rõ trong sheet *Tổng quan* |
| `lead_rac` | tuỳ | CRM | thiếu → mất mã C-01 |
| `booking` · `den` · `chot` | tuỳ | CRM/ERP | thiếu → chỉ phân tích được tầng ①–④ |
| `trang_thai` | tuỳ | Meta | `active` / `disapproved` / `limited` → nuôi mã E-01 |
| `ngan_sach_ngay` | tuỳ | Meta | thiếu → mất mã A-05 (chi hụt) |

## Tên cột tiếng Anh cũng đọc được

Script tự nhận các tên thường gặp trong export của Meta Ads Manager:
`Reporting starts` · `Ad set name` · `Amount spent` · `Impressions` · `Reach` ·
`Link clicks` · `Messaging conversations started` · `Results` · `Delivery status` · `Daily budget`.

Export thuần Meta vẫn chạy được, nhưng báo cáo sẽ ghi rõ: *chưa có lead CRM → không kết luận tầng ⑤–⑧*.

## Mục tiêu CPL theo ZONE

[`muc-tieu-zone.json`](muc-tieu-zone.json) — ⚠️ **số trong file mẫu là số giả để chạy thử.**
Thay bằng mục tiêu thật trước khi dùng, nếu không cột *Đạt?* trong báo cáo sẽ vô nghĩa.

## Chạy thử

```bash
python tools/sinh_du_lieu_mau.py template/MAU_du-lieu-ads.csv
python tools/build_ads_alert.py template/MAU_du-lieu-ads.csv --muc-tieu template/muc-tieu-zone.json
```

Dữ liệu mẫu cài sẵn **6 tình huống** để kiểm bộ luật có bắt đúng không — xem phần đầu
[`tools/sinh_du_lieu_mau.py`](../tools/sinh_du_lieu_mau.py). Tình huống thứ 6 (`DALIEU_DN_BROAD_NVC`)
là ad set **chạy bình thường** — nó có mặt để kiểm điều ngược lại: bộ luật **không được** bắn cảnh báo cho nó.
