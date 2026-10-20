# -*- coding: utf-8 -*-
"""
Sinh file dữ liệu MẪU để chạy thử build_ads_alert.py.

Dữ liệu giả, có cài sẵn 6 tình huống để kiểm tra bộ luật bắt đúng hay không:
    1. MUI_HN_LAL3_NVA     - CPM leo 4 ngày cuối  -> A-01 (phân rã ra CPM)
    2. MAT_HN_INT_NVB      - inbox->lead tụt      -> B-02, tầng rò ⑤ TRỰC PAGE
    3. VONG1_SG_RT_NVD     - frequency cao + CTR trôi -> D-01
    4. LIPO_HN_BROAD_NVE   - chi chỉ ~55% ngân sách  -> A-05
    5. MUI_DN_LAL2_NVA     - ZONE đại phẫu chạy Đà Nẵng -> C-02 🔴 (sai TUYẾN)
    6. DALIEU_DN_BROAD_NVC - chạy bình thường, KHÔNG được bắn cảnh báo

Dùng:
    python tools/sinh_du_lieu_mau.py template/MAU_du-lieu-ads.csv
"""
import csv
import random
import sys
from datetime import date, timedelta

# Console Windows mặc định cp1252 -> ép UTF-8 để in được emoji và tiếng Việt
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

random.seed(20261020)

SO_NGAY = 28
NGAY_CUOI = date(2026, 10, 19)

# ten, zone, kv, adnet, chi/ngay, cpm, ctr, click->inbox, inbox->lead,
# lead->booking, show, den->chot, ngan_sach
CAU_HINH = [
    ("MUI_HN_LAL3_NVA",     "MUI",    "HN", "NVA", 21_000_000, 210_000, 0.019, 0.125, 0.26, 0.34, 0.68, 0.30, 21_000_000),
    ("MUI_HN_BROAD_NVB",    "MUI",    "HN", "NVB", 14_000_000, 195_000, 0.021, 0.130, 0.27, 0.35, 0.66, 0.29, 14_000_000),
    ("MAT_HN_INT_NVB",      "MAT",    "HN", "NVB", 12_000_000, 175_000, 0.024, 0.140, 0.31, 0.38, 0.70, 0.31, 12_000_000),
    ("MAT_SG_LAL2_NVC",     "MAT",    "SG", "NVC",  9_500_000, 182_000, 0.023, 0.135, 0.30, 0.36, 0.67, 0.28, 9_500_000),
    ("VONG1_SG_RT_NVD",     "VONG1",  "SG", "NVD",  8_000_000, 230_000, 0.017, 0.120, 0.25, 0.33, 0.65, 0.33, 8_000_000),
    ("LIPO_HN_BROAD_NVE",   "LIPO",   "HN", "NVE", 11_500_000, 205_000, 0.018, 0.118, 0.24, 0.32, 0.64, 0.34, 12_000_000),
    ("DALIEU_DN_BROAD_NVC", "DALIEU", "DN", "NVC",  6_000_000, 120_000, 0.031, 0.165, 0.38, 0.45, 0.74, 0.22, 6_000_000),
    ("MUI_DN_LAL2_NVA",     "MUI",    "DN", "NVA",  4_500_000, 165_000, 0.020, 0.128, 0.26, 0.30, 0.60, 0.25, 4_500_000),
]


def nhieu(x, bien=0.08):
    return x * (1 + random.uniform(-bien, bien))


def main():
    ra = sys.argv[1] if len(sys.argv) > 1 else "template/MAU_du-lieu-ads.csv"
    dong = []
    for i in range(SO_NGAY):
        ngay = NGAY_CUOI - timedelta(days=SO_NGAY - 1 - i)
        con_lai = (NGAY_CUOI - ngay).days          # 0 = ngày cuối
        cuoi_tuan = ngay.weekday() >= 5

        for (ten, zone, kv, adnet, chi, cpm, ctr, c2i, i2l, l2b, show, d2c, ns) in CAU_HINH:
            he_so_chi, he_so_cpm, he_so_ctr, he_so_i2l = 1.0, 1.0, 1.0, 1.0

            # Cuối tuần: rẻ hơn một chút nhưng ra số kém hơn — nguồn báo động giả kinh điển
            if cuoi_tuan:
                he_so_cpm *= 0.93
                he_so_i2l *= 0.88

            # ① CPM leo dần 4 ngày cuối
            if ten == "MUI_HN_LAL3_NVA" and con_lai <= 4:
                he_so_cpm *= 1.0 + (5 - con_lai) * 0.11

            # ② inbox->lead tụt 5 ngày cuối (thiếu ca trực tối)
            if ten == "MAT_HN_INT_NVB" and con_lai <= 5:
                he_so_i2l *= 0.68

            # ③ frequency cao + CTR trôi dần
            if ten == "VONG1_SG_RT_NVD" and con_lai <= 6:
                he_so_ctr *= 1.0 - (7 - con_lai) * 0.055

            # ④ chi hụt
            if ten == "LIPO_HN_BROAD_NVE" and con_lai <= 6:
                he_so_chi *= 0.55

            chi_td = nhieu(chi * he_so_chi)
            cpm_td = nhieu(cpm * he_so_cpm)
            ctr_td = nhieu(ctr * he_so_ctr)
            imp = chi_td / cpm_td * 1000
            click = imp * ctr_td
            inbox = click * nhieu(c2i)
            lead_tho = inbox * nhieu(i2l * he_so_i2l)
            rac = lead_tho * nhieu(0.17, 0.3)
            lead = max(lead_tho - rac, 0)
            booking = lead * nhieu(l2b)
            den = booking * nhieu(show)
            chot = den * nhieu(d2c)

            # Frequency: tệp retarget hẹp -> cao
            reach = imp / (nhieu(2.9) if ten == "VONG1_SG_RT_NVD" else nhieu(1.6))

            dong.append({
                "ngay": ngay.isoformat(),
                "campaign": "%s_%s_MSG_2610" % (zone, kv),
                "adset": ten,
                "zone": zone,
                "khu_vuc": kv,
                "adnet": adnet,
                "trang_thai": "active",
                "chi_tieu": round(chi_td),
                "ngan_sach_ngay": ns,
                "impression": round(imp),
                "reach": round(reach),
                "click": round(click),
                "inbox": round(inbox),
                "lead_meta": round(lead_tho),
                "lead": round(lead),
                "lead_rac": round(rac),
                "booking": round(booking),
                "den": round(den),
                "chot": round(chot),
            })

    with open(ra, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(dong[0].keys()))
        w.writeheader()
        w.writerows(dong)
    print("✅ Đã sinh %d dòng (%d ngày × %d ad set) → %s" % (len(dong), SO_NGAY, len(CAU_HINH), ra))


if __name__ == "__main__":
    main()
