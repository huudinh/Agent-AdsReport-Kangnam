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
