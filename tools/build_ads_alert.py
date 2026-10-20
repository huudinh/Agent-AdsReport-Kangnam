# -*- coding: utf-8 -*-
"""
Quét dữ liệu quảng cáo Facebook theo ngày -> xuất workbook BÁO CÁO + CẢNH BÁO BẤT THƯỜNG.

Phương pháp luận (bám đúng bộ não của Agent-AdsReport-Kangnam):
    1. Quét nhóm E trước  -> số có tin được không
    2. Phân rã CPL        -> CPM / CTR / click->inbox / inbox->lead
    3. Định vị TẦNG RÒ    -> tầng ĐẦU TIÊN lệch chuẩn, các tầng dưới là hệ quả
    4. Ba cổng chặn báo động giả: ĐỦ MẪU · ĐÚNG BASELINE (median) · CÓ HƯỚNG
    5. Xếp mức 🔴🟠🟡 + gán người + SLA

Dùng:
    python tools/build_ads_alert.py template/MAU_du-lieu-ads.csv
    python tools/build_ads_alert.py du-lieu.csv --ky 7 --baseline 14 -o out/
    python tools/build_ads_alert.py du-lieu.csv --muc-tieu template/muc-tieu-zone.json

Đầu ra: 6 sheet
    1. Tổng quan   - 5 dòng tóm tắt + sức khoẻ dữ liệu
    2. Phễu        - 8 tầng, tỷ lệ chuyển tiếp, so kỳ, đánh dấu TẦNG RÒ
    3. Theo ZONE   - chi · lead · CPL · share ngân sách vs share lead
    4. Cảnh báo    - phiếu 7 ô, chỉ gồm mục đã QUA ĐỦ 3 CỔNG
    5. Theo dõi    - lệch số nhưng CHƯA qua cổng, kèm lý do không qua
    6. Luật        - ngưỡng đã dùng, để hiệu chỉnh sau 4 tuần

Chỉ dùng thư viện chuẩn + openpyxl.
"""
import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from statistics import median

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

# Console Windows mặc định cp1252 -> ép UTF-8 để in được emoji và tiếng Việt
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------- bảng màu
NAVY = "FF074E84"
NAVY_NHAT = "FFE8EFF6"
DO = "FFC0392B"
CAM = "FFE67E22"
VANG = "FFF1C40F"
XAM = "FF95A5A6"
TRANG = "FFFFFFFF"
NEN_NHAT = "FFF3F6FA"

VIEN = Border(*[Side(style="thin", color="FFDCE3EC")] * 4)

# ---------------------------------------------------------------- hằng số nghiệp vụ
ZONE_DAI_PHAU = {"MAT", "MUI", "HAMMAT", "VONG1", "LIPO"}
KV_TUYEN_BENH_VIEN = {"HN", "SG"}

# Ngưỡng khởi động — xem knowledge/ar-nguong-bat-thuong.md §9 để hiệu chỉnh
NGUONG = {
    "lech_vang": 0.20,
    "lech_cam": 0.30,
    "lech_do": 0.50,
    "mau_toi_thieu_inbox": 30,
    "mau_toi_thieu_lead": 10,
    "mau_boi_cpl": 3,          # chi tiêu >= 3 x CPL mục tiêu
    "huong_so_ngay": 2,        # lệch cùng chiều >= 2 ngày liên tiếp
    "frequency_tran": 2.5,
    "ctr_giam_bao_hoa": 0.20,
    "cpm_dai_on_dinh": 0.15,   # CPM coi là "ổn định" khi trong +-15%
    "chi_hut": 0.70,           # chi <= 70% ngân sách đặt
    "f01_boi_median": 1.30,
    "h03_lech_diem_pct": 15.0,
    "e04_lech_meta_crm": 0.30,
    "g04_ty_le_adset_cung_tang": 0.70,
}

SLA_GIO = {"🔴": 4, "🟠": 24, "🟡": 168}

# ---------------------------------------------------------------- đọc dữ liệu
# Mỗi trường chuẩn kèm các tên cột được chấp nhận (viết thường, bỏ dấu cách)
ALIAS = {
    "ngay": ["ngay", "date", "day", "ngaythang", "reportingstarts"],
    "campaign": ["campaign", "campaignname", "tencampaign", "chiendich"],
    "adset": ["adset", "adsetname", "tenadset", "nhomquangcao"],
    "ad": ["ad", "adname", "tenad"],
    "zone": ["zone", "dichvu", "nhomdichvu"],
    "khu_vuc": ["khuvuc", "kv", "region", "tinh"],
    "adnet": ["adnet", "adnetid", "nhanvien", "nguoichay"],
    "chi_tieu": ["chitieu", "spend", "amountspent", "chiphi", "cost"],
    "impression": ["impression", "impressions", "hienthi", "luothienthi"],
    "reach": ["reach", "tieptcan", "nguoitiepcan"],
    "click": ["click", "clicks", "linkclicks", "luotclick"],
    "inbox": ["inbox", "tinnhan", "messagingconversationsstarted", "hoithoai"],
    "lead_meta": ["leadmeta", "leads", "ketqua", "result"],
    "lead": ["lead", "leadhople", "leadcrm"],
    "lead_rac": ["leadrac", "racs", "leadloai"],
    "booking": ["booking", "datlich", "lichhen"],
    "den": ["den", "checkin", "luotden"],
    "chot": ["chot", "cachot", "deal"],
    "trang_thai": ["trangthai", "trangthaiad", "adstatus", "status", "deliverystatus"],
    "ngan_sach_ngay": ["ngansachngay", "dailybudget", "ngansach"],
}

SO_NGUYEN = {"impression", "reach", "click", "inbox", "lead_meta", "lead",
             "lead_rac", "booking", "den", "chot"}
SO_THUC = {"chi_tieu", "ngan_sach_ngay"}


def _chuan_hoa_ten_cot(ten):
    return "".join(ch for ch in ten.lower() if ch.isalnum())


def _map_cot(header):
    """Trả về dict {ten_cot_goc: truong_chuan}."""
    nguoc = {}
    for chuan, ds in ALIAS.items():
        for a in ds:
            nguoc[a] = chuan
    ket_qua = {}
    for cot in header:
        key = _chuan_hoa_ten_cot(cot or "")
        if key in nguoc:
            ket_qua[cot] = nguoc[key]
    return ket_qua


def _so(gia_tri, mac_dinh=0.0):
    if gia_tri is None:
        return mac_dinh
    if isinstance(gia_tri, (int, float)):
        return float(gia_tri)
    s = str(gia_tri).strip().replace(" ", "")
    if not s:
        return mac_dinh
    # 1.234.567,89  |  1,234,567.89  |  1234567
    if s.count(",") and s.count("."):
        s = s.replace("." if s.rfind(",") > s.rfind(".") else ",", "")
        s = s.replace(",", ".")
    elif s.count(","):
        s = s.replace(",", "." if len(s.split(",")[-1]) <= 2 else "")
    else:
        if s.count(".") > 1:
            s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return mac_dinh


def _ngay(gia_tri):
    if isinstance(gia_tri, datetime):
        return gia_tri.date()
    if isinstance(gia_tri, date):
        return gia_tri
    s = str(gia_tri).strip()[:10]
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    raise ValueError("Không đọc được ngày: %r — dùng định dạng YYYY-MM-DD hoặc DD/MM/YYYY" % gia_tri)


def doc_du_lieu(duong_dan):
    """Đọc CSV hoặc XLSX -> list[dict] đã chuẩn hoá tên trường."""
    duoi = os.path.splitext(duong_dan)[1].lower()
    if duoi in (".xlsx", ".xlsm"):
        from openpyxl import load_workbook
        wb = load_workbook(duong_dan, data_only=True)
        ws = wb[wb.sheetnames[0]]
        rows = list(ws.values)
        if not rows:
            return []
        header = [str(c) if c is not None else "" for c in rows[0]]
        tho = [dict(zip(header, r)) for r in rows[1:]]
    else:
        with open(duong_dan, "r", encoding="utf-8-sig", newline="") as f:
            mau = f.read(4096)
            f.seek(0)
            try:
                dialect = csv.Sniffer().sniff(mau, delimiters=",;\t")
            except csv.Error:
                dialect = csv.excel
            tho = list(csv.DictReader(f, dialect=dialect))
        header = list(tho[0].keys()) if tho else []

    anh_xa = _map_cot(header)
    thieu = {"ngay", "chi_tieu"} - set(anh_xa.values())
    if thieu:
        sys.exit("⛔ Thiếu cột bắt buộc: %s\n   Cột đang có: %s"
                 % (", ".join(sorted(thieu)), ", ".join(str(h) for h in header)))

    ket_qua = []
    for i, r in enumerate(tho, start=2):
        if not any(str(v).strip() for v in r.values() if v is not None):
            continue
        d = {}
        for cot_goc, chuan in anh_xa.items():
            v = r.get(cot_goc)
            if chuan == "ngay":
                try:
                    d["ngay"] = _ngay(v)
                except ValueError as e:
                    sys.exit("⛔ Dòng %d: %s" % (i, e))
            elif chuan in SO_NGUYEN or chuan in SO_THUC:
                d[chuan] = _so(v)
            else:
                d[chuan] = (str(v).strip() if v is not None else "")
        d.setdefault("adset", d.get("campaign", "(không rõ)"))
        d.setdefault("campaign", d["adset"])
        for k in SO_NGUYEN | SO_THUC:
            d.setdefault(k, 0.0)
        for k in ("zone", "khu_vuc", "adnet", "trang_thai", "ad"):
            d.setdefault(k, "")
        # Lead hợp lệ: ưu tiên cột CRM, không có thì lùi về lead Meta
        d["_lead_tu_crm"] = d["lead"] > 0
        if d["lead"] == 0 and d["lead_meta"] > 0:
            d["lead"] = d["lead_meta"]
        ket_qua.append(d)
    return ket_qua


# ---------------------------------------------------------------- gộp & chỉ số
TRUONG_CONG = ("chi_tieu", "impression", "reach", "click", "inbox",
               "lead_meta", "lead", "lead_rac", "booking", "den", "chot",
               "ngan_sach_ngay")


def gop(rows):
    t = {k: 0.0 for k in TRUONG_CONG}
    for r in rows:
        for k in TRUONG_CONG:
            t[k] += r.get(k, 0.0)
    return t


def chi_so(t):
    """Tính chỉ số dẫn xuất từ một cụm đã gộp. Mẫu = 0 -> None, KHÔNG trả 0."""
    def chia(a, b, he_so=1.0):
        return (a / b * he_so) if b else None
    return {
        "chi_tieu": t["chi_tieu"],
        "cpm": chia(t["chi_tieu"], t["impression"], 1000),
        "ctr": chia(t["click"], t["impression"]),
        "cpc": chia(t["chi_tieu"], t["click"]),
        "cpi": chia(t["chi_tieu"], t["inbox"]),
        "click_inbox": chia(t["inbox"], t["click"]),
        "cpl": chia(t["chi_tieu"], t["lead"]),
        "inbox_lead": chia(t["lead"], t["inbox"]),
        "cpb": chia(t["chi_tieu"], t["booking"]),
        "lead_booking": chia(t["booking"], t["lead"]),
        "show_rate": chia(t["den"], t["booking"]),
        "den_chot": chia(t["chot"], t["den"]),
        "cac": chia(t["chi_tieu"], t["chot"]),
        "frequency": chia(t["impression"], t["reach"]),
        "pct_rac": chia(t["lead_rac"], t["lead"] + t["lead_rac"]),
        "_tho": t,
    }


# Chỉ số nào "tăng là xấu" — quyết định dấu của phép so lệch
TANG_LA_XAU = {"cpm", "cpc", "cpi", "cpl", "cpb", "cac", "pct_rac", "frequency"}

TEN_CHI_SO = {
    "cpm": "CPM", "ctr": "CTR", "cpc": "CPC", "cpi": "CPI (chi/inbox)",
    "cpl": "CPL", "cpb": "CPB", "cac": "CAC", "frequency": "Frequency",
    "click_inbox": "Click→Inbox %", "inbox_lead": "Inbox→Lead %",
    "lead_booking": "Lead→Booking %", "show_rate": "Show-rate",
    "den_chot": "Đến→Chốt %", "pct_rac": "% lead rác",
}


def lech(ky_nay, baseline, ten):
    """Trả về (lech_tuong_doi, xau_di: bool). Chuẩn hoá: duong = xau di."""
    if ky_nay is None or not baseline:
        return None, False
    tho = (ky_nay - baseline) / baseline
    xau = tho if ten in TANG_LA_XAU else -tho
    return xau, xau > 0


# ---------------------------------------------------------------- 3 cổng
def cong_du_mau(t, cpl_muc_tieu):
    """Cổng ①: chi >= 3x CPL mục tiêu, HOẶC >=30 inbox, HOẶC >=10 lead."""
    ly_do = []
    if cpl_muc_tieu and t["chi_tieu"] >= NGUONG["mau_boi_cpl"] * cpl_muc_tieu:
        return True, ""
    if t["inbox"] >= NGUONG["mau_toi_thieu_inbox"]:
        return True, ""
    if t["lead"] >= NGUONG["mau_toi_thieu_lead"]:
        return True, ""
    ly_do.append("chi %s" % tien(t["chi_tieu"]))
    ly_do.append("%d inbox" % int(t["inbox"]))
    ly_do.append("%d lead" % int(t["lead"]))
    return False, "chưa đủ mẫu (%s)" % " · ".join(ly_do)


def cong_huong(chuoi_ngay, ten, baseline, nguong):
    """Cổng ③: đếm số ngày liên tiếp CUỐI KỲ lệch cùng chiều vượt ngưỡng."""
    dem = 0
    for ngay_cs in reversed(chuoi_ngay):
        v = ngay_cs.get(ten)
        l, xau = lech(v, baseline, ten)
        if l is not None and xau and l >= nguong:
            dem += 1
        else:
            break
    return dem


def muc_tu_lech(l):
    if l >= NGUONG["lech_do"]:
        return "🔴"
    if l >= NGUONG["lech_cam"]:
        return "🟠"
    if l >= NGUONG["lech_vang"]:
        return "🟡"
    return None


# ---------------------------------------------------------------- định dạng số
def tien(v):
    if v is None:
        return "—"
    if v >= 1_000_000_000:
        return ("%.2f tỷ" % (v / 1_000_000_000)).replace(".", ",")
    if v >= 1_000_000:
        return ("%.1ftr" % (v / 1_000_000)).replace(".", ",")
    if v >= 1_000:
        return "%dk" % round(v / 1_000)
    return "%d" % round(v)


def pct(v, so_le=1):
    if v is None:
        return "—"
    return ("%.*f%%" % (so_le, v * 100)).replace(".", ",")


def so_nguyen(v):
    return "—" if v is None else "{:,}".format(int(round(v))).replace(",", ".")


def gia_tri_hien(ten, v):
    if v is None:
        return "—"
    if ten in ("cpm", "cpc", "cpi", "cpl", "cpb", "cac"):
        return tien(v)
    if ten == "frequency":
        return ("%.2f" % v).replace(".", ",")
    return pct(v, 2 if ten in ("ctr", "click_inbox") else 1)


# ---------------------------------------------------------------- bộ luật
def chan_doan_cpl(cs_ky, cs_base):
    """Phân rã CPL -> thành phần nào xấu đi nhất. Trả về (ten_thanh_phan, mo_ta)."""
    ung_vien = []
    for ten in ("cpm", "ctr", "click_inbox", "inbox_lead"):
        l, xau = lech(cs_ky.get(ten), cs_base.get(ten), ten)
        if l is not None and xau:
            ung_vien.append((l, ten))
    if not ung_vien:
        return None, "không tách được thành phần nào xấu rõ rệt — kiểm nhật ký thay đổi"
    ung_vien.sort(reverse=True)
    l, ten = ung_vien[0]
    giai_thich = {
        "cpm": "đấu giá đắt lên / tệp hẹp / trùng tệp giữa ad set (E-06)",
        "ctr": "creative yếu hoặc bão hoà",
        "click_inbox": "điểm đến hỏng: landing chậm, lời chào tự động lỗi",
        "inbox_lead": "tầng TRỰC PAGE — chậm phản hồi, thiếu ca trực, kịch bản xin số sai",
    }[ten]
    return ten, "%s lệch %s → %s" % (TEN_CHI_SO[ten], pct(l), giai_thich)


# (mã, chỉ số, ngưỡng cam, chủ sở hữu, hành động mặc định)
LUAT_LECH = [
    ("A-01", "cpl", NGUONG["lech_cam"], "Adnet phụ trách",
     "Phân rã CPL rồi sửa đúng thành phần xấu — không đụng lung tung"),
    ("A-02", "cpm", NGUONG["lech_cam"], "Adnet phụ trách",
     "Kiểm trùng tệp giữa ad set (E-06) · mở rộng tệp · hạ trần bid"),
    ("A-03", "cpi", NGUONG["lech_cam"], "Adnet phụ trách",
     "Kiểm điểm đến + lời chào tự động trên điện thoại thật"),
    ("B-05", "ctr", NGUONG["lech_cam"], "Adnet phụ trách",
     "Bật challenger mới · đổi hook theo đúng giai đoạn phễu — chuyển brief sang Agent-AdsOptimize MODE 1"),
    ("B-01", "click_inbox", NGUONG["lech_cam"], "Adnet + Kỹ thuật",
     "Bấm thử đúng luồng khách trên điện thoại · kiểm welcome message · đối chiếu lời hứa của ad"),
    ("B-02", "inbox_lead", 0.25, "TRỰC PAGE",
     "Đo thời gian phản hồi lần đầu theo khung giờ · xếp lại ca tối/cuối tuần · rà điểm xin số"),
    ("B-03", "lead_booking", 0.25, "TELESALES",
     "Tách lead rác khỏi mẫu rồi tính lại · đo độ trễ cuộc gọi đầu · rà kịch bản chốt lịch"),
    ("B-04", "show_rate", 0.25, "LỄ TÂN / CSKH",
     "Bật nhắc T-1 ngày và T-2h · rút ngắn khoảng cách ngày hẹn"),
    ("B-06", "den_chot", 0.25, "Tư vấn tại cơ sở",
     "Đối chiếu thông điệp giá trên ad với giá tư vấn thực tế"),
    ("C-01", "pct_rac", NGUONG["lech_cam"], "Adnet (targeting)",
     "Tách rác theo LÝ DO trước khi quy trách nhiệm — sai khu vực là lỗi tầng ②, không phải tầng ⑤"),
]

# Tầng của từng chỉ số — dùng để định vị TẦNG RÒ
TANG = {"cpm": 2, "ctr": 3, "cpi": 4, "click_inbox": 4, "cpl": 5,
        "inbox_lead": 5, "lead_booking": 6, "show_rate": 7, "den_chot": 8,
        "pct_rac": 2}
TEN_TANG = {1: "① Chi phí", 2: "② Hiển thị", 3: "③ Click", 4: "④ Inbox",
            5: "⑤ Lead", 6: "⑥ Booking", 7: "⑦ Đến", 8: "⑧ Chốt"}


def quet_nhom_e(rows_ky):
    """Nhóm E — quét TRƯỚC tất cả. Trả về list cảnh báo E."""
    canh_bao = []
    xau = defaultdict(set)
    for r in rows_ky:
        tt = (r.get("trang_thai") or "").lower()
        if any(k in tt for k in ("disapprove", "tu choi", "từ chối", "reject",
                                 "limited", "han che", "hạn chế")):
            xau[r.get("trang_thai")].add(r["adset"])
    for tt, ds in xau.items():
        canh_bao.append(dict(
            ma="E-01", muc="🔴", don_vi="%d ad set: %s" % (len(ds), ", ".join(sorted(ds)[:3])),
            chi_so="trạng thái ad", ky_nay=tt, baseline="active", lech_txt="—",
            co_mau="%d ad set" % len(ds), tang_ro="① Vận hành",
            chan_doan="Ad bị từ chối/hạn chế → ad set mất phân phối, kéo theo chi hụt (A-05) và CPL méo",
            hanh_dong="Sửa cho ĐÚNG CHÍNH SÁCH rồi kháng nghị. KHÔNG né kiểm duyệt, không nick clone",
            ai="Adnet phụ trách + Trưởng nhóm", han="4 giờ làm việc"))

    # E-04: lệch Meta <-> CRM
    co_crm = [r for r in rows_ky if r.get("_lead_tu_crm")]
    if co_crm:
        lm = sum(r["lead_meta"] for r in co_crm)
        lc = sum(r["lead"] for r in co_crm)
        if lc and abs(lm - lc) / lc >= NGUONG["e04_lech_meta_crm"]:
            canh_bao.append(dict(
                ma="E-04", muc="🔴", don_vi="Toàn tài khoản",
                chi_so="lead Meta vs lead CRM", ky_nay="%d (Meta)" % lm,
                baseline="%d (CRM)" % lc, lech_txt=pct(abs(lm - lc) / lc),
                co_mau="%d dòng" % len(co_crm), tang_ro="① Vận hành",
                chan_doan="Lệch ≥30% → UTM/khoá nối sai, hoặc lọc rác hai bên khác nhau",
                hanh_dong="ĐÓNG BĂNG mọi kết luận A/B/C của kỳ này. Đối soát UTM + quy tắc lọc rác trước",
                ai="Kỹ thuật + CRM", han="4 giờ làm việc"))

    # E-03: chỉ số bỗng = 0 trọn ngày
    theo_ngay = defaultdict(list)
    for r in rows_ky:
        theo_ngay[r["ngay"]].append(r)
    for ng in sorted(theo_ngay):
        t = gop(theo_ngay[ng])
        if t["chi_tieu"] > 0 and t["impression"] == 0:
            canh_bao.append(dict(
                ma="E-03", muc="🔴", don_vi="Toàn tài khoản — ngày %s" % ng.strftime("%d/%m"),
                chi_so="impression", ky_nay="0", baseline=">0", lech_txt="—",
                co_mau="chi %s" % tien(t["chi_tieu"]), tang_ro="① Vận hành",
                chan_doan="Có chi tiêu nhưng không có hiển thị → tracking/export hỏng",
                hanh_dong="Kiểm pipeline kéo số + múi giờ tài khoản. Không phân tích trên kỳ này",
                ai="Kỹ thuật", han="4 giờ làm việc"))
    return canh_bao


def quet_c02(rows_ky):
    """C-02 — lead đại phẫu ở khu vực không có tuyến bệnh viện. Bỏ qua mọi cổng."""
    vi_pham = defaultdict(lambda: {"lead": 0.0, "chi": 0.0, "adset": set()})
    for r in rows_ky:
        z = (r.get("zone") or "").upper()
        kv = (r.get("khu_vuc") or "").upper()
        if z in ZONE_DAI_PHAU and kv and kv not in KV_TUYEN_BENH_VIEN and kv != "TOANQUOC":
            k = (z, kv)
            vi_pham[k]["lead"] += r["lead"]
            vi_pham[k]["chi"] += r["chi_tieu"]
            vi_pham[k]["adset"].add(r["adset"])
    out = []
    for (z, kv), v in sorted(vi_pham.items(), key=lambda x: -x[1]["chi"]):
        out.append(dict(
            ma="C-02", muc="🔴", don_vi="ZONE %s × khu vực %s (%d ad set)" % (z, kv, len(v["adset"])),
            chi_so="lead đại phẫu ngoài tuyến bệnh viện", ky_nay="%d lead" % int(v["lead"]),
            baseline="0 (chỉ HN · SG)", lech_txt="—", co_mau="chi %s" % tien(v["chi"]),
            tang_ro="⚠ Ràng buộc TUYẾN — không phải vấn đề hiệu suất",
            chan_doan="ZONE đại phẫu chạy ở khu vực chỉ có viện thẩm mỹ. "
                      "Nếu thông điệp mời thực hiện tại đó thì đây là rủi ro VƯỢT PHẠM VI GIẤY PHÉP",
            hanh_dong="Chọn MỘT: ① sửa thông điệp thành 'tư vấn/đặt khám tại cơ sở tỉnh, "
                      "phẫu thuật tại tuyến bệnh viện'; hoặc ② loại trừ tỉnh khỏi targeting. Không có cách thứ ba",
            ai="Adnet + Trưởng nhóm + Pháp chế", han="4 giờ làm việc"))
    return out


# ---------------------------------------------------------------- quét chính
def quet(rows, ky_dau, ky_cuoi, base_dau, base_cuoi, muc_tieu, don_vi_cot="adset"):
    """Trả về (canh_bao, theo_doi)."""
    rows_ky = [r for r in rows if ky_dau <= r["ngay"] <= ky_cuoi]
    rows_base = [r for r in rows if base_dau <= r["ngay"] <= base_cuoi]

    canh_bao = quet_nhom_e(rows_ky)
    dong_bang = any(c["ma"] in ("E-03", "E-04") for c in canh_bao)
    canh_bao += quet_c02(rows_ky)

    theo_doi = []

    # G-04: CPM tăng đồng loạt -> mã CHẶN
    don_vi_ky = defaultdict(list)
    for r in rows_ky:
        don_vi_ky[r[don_vi_cot]].append(r)
    don_vi_base = defaultdict(list)
    for r in rows_base:
        don_vi_base[r[don_vi_cot]].append(r)

    tang_cpm, xet_cpm = 0, 0
    for dv, rs in don_vi_ky.items():
        if dv not in don_vi_base:
            continue
        a = chi_so(gop(rs))["cpm"]
        b = chi_so(gop(don_vi_base[dv]))["cpm"]
        if a and b:
            xet_cpm += 1
            if (a - b) / b >= NGUONG["lech_cam"]:
                tang_cpm += 1
    g04 = xet_cpm >= 3 and tang_cpm / xet_cpm >= NGUONG["g04_ty_le_adset_cung_tang"]

    for dv, rs_ky in sorted(don_vi_ky.items()):
        rs_base = don_vi_base.get(dv, [])
        if not rs_base:
            continue
        t_ky = gop(rs_ky)
        cs_ky = chi_so(t_ky)
        zone = (rs_ky[0].get("zone") or "").upper()
        cpl_mt = (muc_tieu.get(zone) or {}).get("cpl_muc_tieu")

        # Baseline = MEDIAN của chỉ số theo NGÀY trong cửa sổ baseline
        theo_ngay = defaultdict(list)
        for r in rs_base:
            theo_ngay[r["ngay"]].append(r)
        cs_moi_ngay = [chi_so(gop(v)) for _, v in sorted(theo_ngay.items())]

        theo_ngay_ky = defaultdict(list)
        for r in rs_ky:
            theo_ngay_ky[r["ngay"]].append(r)
        chuoi_ky = [chi_so(gop(v)) for _, v in sorted(theo_ngay_ky.items())]

        # Cửa sổ 3 ngày cuối — bắt xu hướng ĐANG LEO mà trung bình 7 ngày còn làm loãng.
        # Đây chính là cổng ③ "có hướng": 3 ngày nhích đều nguy hiểm hơn 1 ngày nhảy vọt.
        ngay_ky = sorted({r["ngay"] for r in rs_ky})
        ngay_3 = set(ngay_ky[-3:])
        rs_ky3 = [r for r in rs_ky if r["ngay"] in ngay_3]
        t_ky3 = gop(rs_ky3)
        cs_ky3 = chi_so(t_ky3)
        chuoi_ky3 = chuoi_ky[-3:]

        du_mau, ly_do_mau = cong_du_mau(t_ky, cpl_mt)
        du_mau3, ly_do_mau3 = cong_du_mau(t_ky3, cpl_mt)
        ket_dv = []

        for ma, ten_cs, nguong_cam, chu, hanh_dong in LUAT_LECH:
            gia_tri = [c[ten_cs] for c in cs_moi_ngay if c[ten_cs] is not None]
            if len(gia_tri) < 3:
                continue
            base = median(gia_tri)

            # Chọn cửa sổ: ưu tiên kỳ đầy đủ; kỳ đầy đủ chưa vượt ngưỡng thì xét 3 ngày cuối
            l7, xau7 = lech(cs_ky[ten_cs], base, ten_cs)
            l3, xau3 = lech(cs_ky3[ten_cs], base, ten_cs)
            dung_3ngay = False
            if l7 is not None and xau7 and l7 >= NGUONG["lech_vang"]:
                l, cs_dung, t_dung, chuoi_dung = l7, cs_ky, t_ky, chuoi_ky
                mau_ok, mau_ly_do = du_mau, ly_do_mau
            elif l3 is not None and xau3 and l3 >= NGUONG["lech_vang"] and len(ngay_ky) > 3:
                l, cs_dung, t_dung, chuoi_dung = l3, cs_ky3, t_ky3, chuoi_ky3
                mau_ok, mau_ly_do = du_mau3, ly_do_mau3
                dung_3ngay = True
            else:
                continue

            # B-05 chỉ đúng khi CPM ỔN ĐỊNH. CPM cũng chạy thì đó là chuyện đấu giá (A-02),
            # không phải creative — gán nhầm sẽ khiến đội đi làm creative mới một cách vô ích.
            if ten_cs == "ctr":
                cpm_base = [c["cpm"] for c in cs_moi_ngay if c["cpm"] is not None]
                if not cpm_base or cs_dung["cpm"] is None:
                    continue
                if abs(cs_dung["cpm"] - median(cpm_base)) / median(cpm_base) > NGUONG["cpm_dai_on_dinh"]:
                    continue

            so_ngay_huong = cong_huong(chuoi_dung, ten_cs, base, NGUONG["lech_vang"])
            co_huong = so_ngay_huong >= NGUONG["huong_so_ngay"] or l >= NGUONG["lech_do"]
            muc = muc_tu_lech(l)
            if l >= nguong_cam and muc == "🟡":
                muc = "🟠"

            thanh_phan, giai_thich = (None, "")
            if ten_cs == "cpl":
                base_cs = {k: (median([c[k] for c in cs_moi_ngay if c[k] is not None])
                               if any(c[k] is not None for c in cs_moi_ngay) else None)
                           for k in ("cpm", "ctr", "click_inbox", "inbox_lead")}
                thanh_phan, giai_thich = chan_doan_cpl(cs_dung, base_cs)

            # Dấu hiển thị theo CHIỀU THẬT của con số, không theo chiều "xấu"
            tho = (cs_dung[ten_cs] - base) / base
            nhan_ky = "3 ngày cuối" if dung_3ngay else "kỳ"
            phieu = dict(
                ma=ma, muc=muc, don_vi="%s%s" % (dv, (" · ZONE %s" % zone) if zone else ""),
                chi_so=TEN_CHI_SO[ten_cs] + (" (3 ngày cuối)" if dung_3ngay else ""),
                ky_nay=gia_tri_hien(ten_cs, cs_dung[ten_cs]),
                baseline=gia_tri_hien(ten_cs, base),
                lech_txt=("+" if tho >= 0 else "−") + pct(abs(tho)),
                co_mau="chi %s · %d inbox · %d lead (%s)" % (
                    tien(t_dung["chi_tieu"]), int(t_dung["inbox"]), int(t_dung["lead"]), nhan_ky),
                tang_ro=TEN_TANG[TANG[ten_cs]],
                chan_doan=giai_thich or "%s xấu đi %s so median %d ngày" % (
                    TEN_CHI_SO[ten_cs], pct(abs(l)), len(gia_tri)),
                hanh_dong=hanh_dong, ai=chu, han="",
                _tang=TANG[ten_cs], _lech=l, _ngay_huong=so_ngay_huong,
                _thanh_phan=thanh_phan,
            )
            if dung_3ngay:
                phieu["chan_doan"] = ("⚠ ĐANG LEO — 3 ngày cuối lệch %s trong khi cả kỳ %d ngày mới %s, "
                                      "trung bình kỳ đang làm loãng xu hướng. " % (
                                          pct(abs(l)), len(ngay_ky),
                                          pct(abs(l7)) if l7 is not None else "—")
                                      ) + phieu["chan_doan"]

            if g04 and ten_cs in ("cpm", "cpl"):
                phieu["muc"] = "🟡"
                phieu["chan_doan"] += " · ⚠ G-04: CPM tăng đồng loạt ở %d/%d ad set → nhiều khả năng là ĐẤU GIÁ TOÀN NGÀNH, không phải lỗi của ai" % (tang_cpm, xet_cpm)
            if dong_bang:
                phieu["muc"] = "⚪"
                phieu["chan_doan"] += " · ⛔ Đang có E-03/E-04 → số liệu chưa tin được, tạm dừng kết luận"

            ly_do_truot = []
            if not mau_ok:
                ly_do_truot.append("cổng ① " + mau_ly_do)
            if not co_huong:
                ly_do_truot.append("cổng ③ chỉ lệch %d ngày liên tiếp (cần ≥%d)"
                                   % (so_ngay_huong, NGUONG["huong_so_ngay"]))
            if dong_bang:
                ly_do_truot.append("đang có E-03/E-04")

            if ly_do_truot:
                phieu["ly_do"] = " · ".join(ly_do_truot)
                theo_doi.append(phieu)
            else:
                ket_dv.append(phieu)

        # ---- Khử trùng: A-01 (CPL) là triệu chứng TỔNG HỢP. Nếu đã tách được thành phần
        #      và thành phần đó có phiếu riêng trong cùng đơn vị thì giữ phiếu thành phần,
        #      bỏ A-01 — nếu không, một nguyên nhân bị báo hai lần dưới hai cái tên.
        MA_THEO_THANH_PHAN = {"cpm": "A-02", "ctr": "B-05",
                              "click_inbox": "B-01", "inbox_lead": "B-02"}
        ma_co_san = {p["ma"] for p in ket_dv}
        ket_dv = [p for p in ket_dv
                  if not (p["ma"] == "A-01"
                          and MA_THEO_THANH_PHAN.get(p.get("_thanh_phan")) in ma_co_san)]

        # ---- LUẬT TẦNG RÒ: trong một đơn vị, chỉ giữ phiếu có tầng NHỎ NHẤT
        if ket_dv:
            tang_min = min(p["_tang"] for p in ket_dv)
            chinh = [p for p in ket_dv if p["_tang"] == tang_min]
            he_qua = [p for p in ket_dv if p["_tang"] > tang_min]
            for p in chinh:
                if he_qua:
                    p["chan_doan"] += " · Hệ quả kéo theo: %s" % ", ".join(
                        "%s (%s)" % (q["ma"], q["chi_so"]) for q in he_qua)
                p["han"] = "%d giờ" % SLA_GIO.get(p["muc"], 168)
                canh_bao.append(p)

        # ---- D-01 bão hoà (xét cả kỳ đầy đủ và 3 ngày cuối — lấy bên xấu hơn)
        if cs_ky["frequency"] and cs_ky["frequency"] >= NGUONG["frequency_tran"]:
            ctr_base = [c["ctr"] for c in cs_moi_ngay if c["ctr"] is not None]
            if ctr_base and cs_ky["ctr"]:
                med_ctr = median(ctr_base)
                gim7 = (med_ctr - cs_ky["ctr"]) / med_ctr
                gim3 = ((med_ctr - cs_ky3["ctr"]) / med_ctr) if cs_ky3["ctr"] else gim7
                dung3 = gim3 > gim7 and du_mau3
                gim = gim3 if dung3 else gim7
                cs_d, t_d = (cs_ky3, t_ky3) if dung3 else (cs_ky, t_ky)
                if gim >= NGUONG["ctr_giam_bao_hoa"] and (du_mau3 if dung3 else du_mau):
                    canh_bao.append(dict(
                        ma="D-01", muc="🟠", don_vi=dv,
                        chi_so="Frequency + CTR" + (" (3 ngày cuối)" if dung3 else ""),
                        ky_nay=("%.2f" % cs_d["frequency"]).replace(".", ",") + " · CTR " + pct(cs_d["ctr"], 2),
                        baseline=("≤%.1f" % NGUONG["frequency_tran"]).replace(".", ",") + " · CTR " + pct(med_ctr, 2),
                        lech_txt="CTR −" + pct(gim), co_mau="chi %s" % tien(t_d["chi_tieu"]),
                        tang_ro=TEN_TANG[3],
                        chan_doan="Frequency vượt trần VÀ CTR trôi → bão hoà tệp thật "
                                  "(frequency cao mà CTR giữ nguyên thì KHÔNG phải bão hoà)",
                        hanh_dong="Bật challenger mới · mở rộng hoặc đổi tệp, giữ nguyên creative để đọc được kết quả",
                        ai="Adnet phụ trách", han="24 giờ", _tang=3, _lech=gim, _ngay_huong=0))
                    # D-01 kể câu chuyện đầy đủ hơn B-05 (có thêm frequency) -> bỏ B-05 trùng
                    canh_bao[:] = [p for p in canh_bao
                                   if not (p["ma"] == "B-05" and p["don_vi"].startswith(dv))]

        # ---- A-05 chi hụt
        if t_ky["ngan_sach_ngay"] > 0:
            ty_le = t_ky["chi_tieu"] / t_ky["ngan_sach_ngay"]
            if ty_le <= NGUONG["chi_hut"]:
                canh_bao.append(dict(
                    ma="A-05", muc="🟠", don_vi=dv, chi_so="Chi thực tế / ngân sách đặt",
                    ky_nay=pct(ty_le), baseline="≥%d%%" % int(NGUONG["chi_hut"] * 100),
                    lech_txt="−" + pct(1 - ty_le), co_mau="chi %s" % tien(t_ky["chi_tieu"]),
                    tang_ro=TEN_TANG[1],
                    chan_doan="Không tiêu hết tiền = MẤT PHỄU, nhưng không ai thấy vì 'không tốn tiền'. "
                              "Nguyên nhân thường gặp: tệp quá hẹp · bid trần thấp · ad vừa bị từ chối (kiểm E-01)",
                    hanh_dong="Kiểm E-01 trước · mở rộng tệp hoặc nâng trần bid từng bước ≤20%",
                    ai="Adnet phụ trách", han="24 giờ", _tang=1, _lech=1 - ty_le, _ngay_huong=0))

    canh_bao += quet_f01_h03(rows_ky, muc_tieu)
    thu_tu = {"🔴": 0, "🟠": 1, "🟡": 2, "⚪": 3}
    canh_bao.sort(key=lambda p: (thu_tu.get(p["muc"], 9), p.get("_tang", 9), p["ma"]))
    theo_doi.sort(key=lambda p: (p["ma"], p["don_vi"]))
    return canh_bao, theo_doi


def quet_f01_h03(rows_ky, muc_tieu):
    """F-01 CPL lệch median team cùng ZONE · H-03 share ngân sách lệch share lead."""
    out = []
    # F-01
    theo_zone = defaultdict(lambda: defaultdict(list))
    for r in rows_ky:
        if r.get("adnet"):
            theo_zone[(r.get("zone") or "").upper()][r["adnet"]].append(r)
    for zone, nguoi in theo_zone.items():
        cpl_nguoi = {}
        for nv, rs in nguoi.items():
            cs = chi_so(gop(rs))
            if cs["cpl"]:
                cpl_nguoi[nv] = (cs["cpl"], gop(rs))
        if len(cpl_nguoi) < 3:
            continue
        med = median([v[0] for v in cpl_nguoi.values()])
        for nv, (cpl, t) in sorted(cpl_nguoi.items(), key=lambda x: -x[1][0]):
            du_mau, ly_do = cong_du_mau(t, (muc_tieu.get(zone) or {}).get("cpl_muc_tieu"))
            if not du_mau:
                continue
            if cpl >= NGUONG["f01_boi_median"] * med:
                out.append(dict(
                    ma="F-01", muc="🟡", don_vi="Adnet %s · ZONE %s" % (nv, zone or "—"),
                    chi_so="CPL so median team", ky_nay=tien(cpl), baseline="median %s" % tien(med),
                    lech_txt="+" + pct((cpl - med) / med),
                    co_mau="chi %s · %d lead" % (tien(t["chi_tieu"]), int(t["lead"])),
                    tang_ro="— (chỉ số nhân sự)",
                    chan_doan="CPL cao hơn median team cùng ZONE. CPL chịu ảnh hưởng của ZONE, mùa, "
                              "tệp được giao — kiểm F-02 (bỏ rơi ad set) trước khi kết luận về người",
                    hanh_dong="Trưởng nhóm rà cùng: tệp · creative · nhật ký thao tác 7 ngày",
                    ai="Trưởng nhóm (kèm việc)", han="7 ngày", _tang=9, _lech=(cpl - med) / med,
                    _ngay_huong=0))
    # H-03
    tong_chi = sum(r["chi_tieu"] for r in rows_ky)
    tong_lead = sum(r["lead"] for r in rows_ky)
    if tong_chi and tong_lead:
        theo_z = defaultdict(lambda: {"chi": 0.0, "lead": 0.0})
        for r in rows_ky:
            z = (r.get("zone") or "KHAC").upper()
            theo_z[z]["chi"] += r["chi_tieu"]
            theo_z[z]["lead"] += r["lead"]
        for z, v in sorted(theo_z.items(), key=lambda x: -x[1]["chi"]):
            s_chi = v["chi"] / tong_chi * 100
            s_lead = v["lead"] / tong_lead * 100
            if abs(s_chi - s_lead) >= NGUONG["h03_lech_diem_pct"]:
                out.append(dict(
                    ma="H-03", muc="🟡", don_vi="ZONE %s" % z, chi_so="Share ngân sách vs share lead",
                    ky_nay=("NS %.1f%% · lead %.1f%%" % (s_chi, s_lead)).replace(".", ","),
                    baseline=("lệch <%.0f điểm %%" % NGUONG["h03_lech_diem_pct"]),
                    lech_txt=("%.1f điểm %%" % abs(s_chi - s_lead)).replace(".", ","),
                    co_mau="chi %s · %d lead" % (tien(v["chi"]), int(v["lead"])),
                    tang_ro="— (phân bổ)",
                    chan_doan="Tiền và kết quả lệch nhau. Có thể là CHỦ Ý (đẩy ZONE chiến lược) "
                              "hoặc QUÁN TÍNH — phải hỏi, đừng đoán",
                    hanh_dong="Trả lời: chủ ý hay quán tính? Chủ ý → ghi vào dim_su_kien để kỳ sau không bắn lại. "
                              "Quán tính → xem luật điều chuyển MODE 4",
                    ai="Trưởng nhóm", han="7 ngày", _tang=9, _lech=abs(s_chi - s_lead) / 100,
                    _ngay_huong=0))
    return out


# ---------------------------------------------------------------- xuất Excel
def _tieu_de(ws, hang, cot, text, rong=None):
    c = ws.cell(row=hang, column=cot, value=text)
    c.font = Font(bold=True, color=TRANG, size=10)
    c.fill = PatternFill("solid", fgColor=NAVY)
    c.alignment = Alignment(vertical="center", wrap_text=True)
    c.border = VIEN
    if rong:
        ws.column_dimensions[get_column_letter(cot)].width = rong


def _o(ws, hang, cot, text, dam=False, mau=None, wrap=True):
    c = ws.cell(row=hang, column=cot, value=text)
    c.font = Font(bold=dam, size=10, color=mau or "FF0E2338")
    c.alignment = Alignment(vertical="top", wrap_text=wrap)
    c.border = VIEN
    return c


MAU_MUC = {"🔴": DO, "🟠": CAM, "🟡": VANG, "⚪": XAM}


def xuat(duong_dan, ctx):
    wb = Workbook()

    # ---------- Sheet 1: Tổng quan
    ws = wb.active
    ws.title = "1. Tổng quan"
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 30
    ws.column_dimensions["C"].width = 30
    ws.column_dimensions["D"].width = 60
    h = 1
    c = ws.cell(row=h, column=1, value="BÁO CÁO & CẢNH BÁO QUẢNG CÁO FACEBOOK")
    c.font = Font(bold=True, size=14, color=NAVY)
    h += 2
    for nhan, gt in ctx["tom_tat"]:
        _o(ws, h, 1, nhan, dam=True)
        _o(ws, h, 2, gt)
        h += 1
    h += 1
    _o(ws, h, 1, "➜ KẾT LUẬN", dam=True, mau=DO)
    _o(ws, h, 2, ctx["ket_luan"])
    ws.merge_cells(start_row=h, start_column=2, end_row=h, end_column=4)
    h += 2
    _tieu_de(ws, h, 1, "SỨC KHOẺ DỮ LIỆU")
    _tieu_de(ws, h, 2, "Giá trị")
    _tieu_de(ws, h, 3, "Ngưỡng")
    _tieu_de(ws, h, 4, "Ghi chú")
    h += 1
    for dong in ctx["suc_khoe"]:
        for i, v in enumerate(dong, start=1):
            _o(ws, h, i, v)
        h += 1

    # ---------- Sheet 2: Phễu
    ws = wb.create_sheet("2. Phễu")
    cot = [("Tầng", 16), ("Kỳ này", 14), ("Kỳ trước", 14), ("Tỷ lệ chuyển tiếp", 22),
           ("± so kỳ trước", 16), ("Chủ sở hữu tầng", 22), ("", 14)]
    for i, (t, w) in enumerate(cot, start=1):
        _tieu_de(ws, 1, i, t, w)
    for j, dong in enumerate(ctx["pheu"], start=2):
        for i, v in enumerate(dong, start=1):
            cc = _o(ws, j, i, v)
            if "TẦNG RÒ" in str(dong[-1]):
                cc.fill = PatternFill("solid", fgColor="FFFDEBD0")

    # ---------- Sheet 3: Theo ZONE
    ws = wb.create_sheet("3. Theo ZONE")
    cot = [("ZONE", 14), ("Chi", 12), ("Share NS", 11), ("Lead", 10), ("Share lead", 11),
           ("CPL", 12), ("CPL mục tiêu", 13), ("Đạt?", 8), ("Booking", 10),
           ("Lead→Book", 12), ("Lệch NS–lead", 14)]
    for i, (t, w) in enumerate(cot, start=1):
        _tieu_de(ws, 1, i, t, w)
    for j, dong in enumerate(ctx["zone"], start=2):
        for i, v in enumerate(dong, start=1):
            _o(ws, j, i, v)

    # ---------- Sheet 4: Cảnh báo
    ws = wb.create_sheet("4. Cảnh báo")
    cot = [("Mức", 7), ("Mã", 8), ("② Đơn vị", 34), ("③ Chỉ số", 16), ("Kỳ này", 14),
           ("Baseline", 14), ("Lệch", 10), ("Cỡ mẫu", 26), ("④ Tầng rò", 16),
           ("⑤ Chẩn đoán", 58), ("⑥ Hành động", 52), ("⑦ Ai", 24), ("Hạn", 12),
           ("Theo dõi sau khi sửa", 34)]
    for i, (t, w) in enumerate(cot, start=1):
        _tieu_de(ws, 1, i, t, w)
    for j, p in enumerate(ctx["canh_bao"], start=2):
        gia_tri = [p["muc"], p["ma"], p["don_vi"], p["chi_so"], p["ky_nay"], p["baseline"],
                   p["lech_txt"], p["co_mau"], p["tang_ro"], p["chan_doan"], p["hanh_dong"],
                   p["ai"], p["han"],
                   "%s · kỳ vọng về %s trong 3–5 ngày" % (p["chi_so"], p["baseline"])]
        for i, v in enumerate(gia_tri, start=1):
            cc = _o(ws, j, i, v)
            if i == 1:
                cc.fill = PatternFill("solid", fgColor=MAU_MUC.get(p["muc"], XAM))
                cc.font = Font(bold=True, size=12, color=TRANG)
                cc.alignment = Alignment(horizontal="center", vertical="center")
        ws.row_dimensions[j].height = 58
    if not ctx["canh_bao"]:
        _o(ws, 2, 1, "Không có cảnh báo nào qua đủ 3 cổng trong kỳ này.", dam=True)

    # ---------- Sheet 5: Theo dõi
    ws = wb.create_sheet("5. Theo dõi")
    _o(ws, 1, 1, "Các mục LỆCH SỐ nhưng CHƯA qua đủ 3 cổng — liệt kê để theo dõi, KHÔNG hành động.",
       dam=True)
    cot = [("Mã", 8), ("Đơn vị", 34), ("Chỉ số", 16), ("Kỳ này", 14), ("Baseline", 14),
           ("Lệch", 10), ("Cỡ mẫu", 26), ("Trượt cổng nào", 56)]
    for i, (t, w) in enumerate(cot, start=1):
        _tieu_de(ws, 2, i, t, w)
    for j, p in enumerate(ctx["theo_doi"], start=3):
        for i, v in enumerate([p["ma"], p["don_vi"], p["chi_so"], p["ky_nay"], p["baseline"],
                               p["lech_txt"], p["co_mau"], p.get("ly_do", "")], start=1):
            _o(ws, j, i, v)

    # ---------- Sheet 6: Luật
    ws = wb.create_sheet("6. Luật")
    _o(ws, 1, 1, "NGƯỠNG ĐÃ DÙNG — đây là ngưỡng KHỞI ĐỘNG, hiệu chỉnh sau 4 tuần "
                 "(xem knowledge/ar-nguong-bat-thuong.md §9)", dam=True)
    _tieu_de(ws, 3, 1, "Tham số", 34)
    _tieu_de(ws, 3, 2, "Giá trị", 16)
    _tieu_de(ws, 3, 3, "Ý nghĩa", 70)
    y_nghia = {
        "lech_vang": "Ngưỡng 🟡 — lệch tối thiểu để được ghi nhận",
        "lech_cam": "Ngưỡng 🟠",
        "lech_do": "Ngưỡng 🔴 — qua ngay cổng ③ mà không cần lặp",
        "mau_toi_thieu_inbox": "Cổng ① — số inbox tối thiểu để kết luận",
        "mau_toi_thieu_lead": "Cổng ① — số lead tối thiểu để kết luận",
        "mau_boi_cpl": "Cổng ① — chi tiêu tối thiểu = bội số này × CPL mục tiêu ZONE",
        "huong_so_ngay": "Cổng ③ — số ngày liên tiếp lệch cùng chiều",
        "frequency_tran": "D-01 — trần frequency 7 ngày",
        "ctr_giam_bao_hoa": "D-01 — CTR phải giảm bao nhiêu mới coi là bão hoà thật",
        "cpm_dai_on_dinh": "B-05 — dải coi CPM là ổn định",
        "chi_hut": "A-05 — chi/ngân sách dưới mức này là chi hụt",
        "f01_boi_median": "F-01 — bội số median team",
        "h03_lech_diem_pct": "H-03 — lệch share ngân sách vs share lead (điểm %)",
        "e04_lech_meta_crm": "E-04 — lệch lead Meta vs CRM",
        "g04_ty_le_adset_cung_tang": "G-04 — tỷ lệ ad set cùng tăng CPM để coi là đấu giá toàn ngành",
    }
    h = 4
    for k, v in NGUONG.items():
        _o(ws, h, 1, k, dam=True)
        _o(ws, h, 2, str(v).replace(".", ","))
        _o(ws, h, 3, y_nghia.get(k, ""))
        h += 1
    h += 1
    _o(ws, h, 1, "Cách tính baseline", dam=True)
    _o(ws, h, 3, "MEDIAN của chỉ số tính theo NGÀY, trên cửa sổ %d ngày ngay trước kỳ báo cáo. "
                 "Dùng trung vị để một ngày bất thường không kéo lệch mốc so sánh." % ctx["so_ngay_base"])
    h += 1
    _o(ws, h, 1, "Luật tầng rò", dam=True)
    _o(ws, h, 3, "Trong mỗi đơn vị, chỉ xuất phiếu cho tầng NHỎ NHẤT bị lệch; "
                 "các tầng dưới ghi vào ô Chẩn đoán như 'hệ quả kéo theo'.")
    h += 2
    _o(ws, h, 1, ctx["chan_trang"], dam=True)
    ws.merge_cells(start_row=h, start_column=1, end_row=h, end_column=3)

    for s in wb.worksheets:
        s.freeze_panes = "A2"
        s.sheet_view.showGridLines = False
    wb.save(duong_dan)
    return duong_dan


# ---------------------------------------------------------------- dựng ngữ cảnh
def dung_ngu_canh(rows, ky_dau, ky_cuoi, base_dau, base_cuoi, muc_tieu, canh_bao, theo_doi):
    rows_ky = [r for r in rows if ky_dau <= r["ngay"] <= ky_cuoi]
    so_ngay = (ky_cuoi - ky_dau).days + 1
    truoc_cuoi = ky_dau - timedelta(days=1)
    truoc_dau = truoc_cuoi - timedelta(days=so_ngay - 1)
    rows_truoc = [r for r in rows if truoc_dau <= r["ngay"] <= truoc_cuoi]

    t, tt = gop(rows_ky), gop(rows_truoc)
    cs, cst = chi_so(t), chi_so(tt)

    def dpct(a, b):
        if a is None or b in (None, 0):
            return "—"
        return ("+" if a >= b else "−") + pct(abs(a - b) / b)

    cuoi_tuan = sum(1 for i in range(so_ngay) if (ky_dau + timedelta(days=i)).weekday() >= 5)
    tom_tat = [
        ("Kỳ báo cáo", "%s – %s (%d ngày · %d ngày cuối tuần)"
         % (ky_dau.strftime("%d/%m"), ky_cuoi.strftime("%d/%m/%Y"), so_ngay, cuoi_tuan)),
        ("Baseline", "median theo ngày của %s – %s"
         % (base_dau.strftime("%d/%m"), base_cuoi.strftime("%d/%m/%Y"))),
        ("Tổng chi", "%s  (kỳ trước %s · %s)" % (tien(t["chi_tieu"]), tien(tt["chi_tieu"]),
                                                 dpct(t["chi_tieu"], tt["chi_tieu"]))),
        ("Lead hợp lệ", "%s  (kỳ trước %s · %s)" % (so_nguyen(t["lead"]), so_nguyen(tt["lead"]),
                                                    dpct(t["lead"], tt["lead"]))),
        ("CPL", "%s  (kỳ trước %s · %s)" % (tien(cs["cpl"]), tien(cst["cpl"]),
                                            dpct(cs["cpl"], cst["cpl"]))),
        ("Booking", "%s  (kỳ trước %s · %s)" % (so_nguyen(t["booking"]), so_nguyen(tt["booking"]),
                                                dpct(t["booking"], tt["booking"]))),
    ]

    do = [p for p in canh_bao if p["muc"] == "🔴"]
    cam = [p for p in canh_bao if p["muc"] == "🟠"]
    if do:
        ket_luan = "%d cảnh báo 🔴 phải xử lý trong 4 giờ — ưu tiên: %s (%s)." % (
            len(do), do[0]["ma"], do[0]["don_vi"])
    elif cam:
        ket_luan = "%d cảnh báo 🟠 trong 24h — ưu tiên: %s tại %s." % (
            len(cam), cam[0]["ma"], cam[0]["don_vi"])
    else:
        ket_luan = "Không có bất thường nào qua đủ 3 cổng. %d mục đang ở diện theo dõi." % len(theo_doi)

    # ---- sức khoẻ dữ liệu
    co_crm = any(r.get("_lead_tu_crm") for r in rows_ky)
    co_adnet = any(r.get("adnet") for r in rows_ky)
    co_zone = any(r.get("zone") for r in rows_ky)
    khac = sum(r["chi_tieu"] for r in rows_ky if not r.get("zone"))
    suc_khoe = [
        ["Nguồn lead", "CRM" if co_crm else "Meta (chưa có CRM)", "CRM",
         "Chưa có cột lead CRM → chỉ phân tích được tầng ①–④; kết luận tầng ⑤–⑧ KHÔNG đưa ra"
         if not co_crm else "Dùng lead CRM cho mọi kết luận"],
        ["Cột ZONE", "có" if co_zone else "THIẾU", "có",
         "Thiếu ZONE → không chạy được khối 'Theo dịch vụ' và mã H" if not co_zone else ""],
        ["Cột Adnet", "có" if co_adnet else "THIẾU", "có",
         "Thiếu mã nhân viên → KHÔNG chạy được MODE 3 và mã F" if not co_adnet else ""],
        ["Chi rơi vào nhóm KHAC", "%s (%s)" % (tien(khac), pct(khac / t["chi_tieu"]) if t["chi_tieu"] else "—"),
         "< 5%", "Nhóm KHAC phình to = quy ước đặt tên đang bị vi phạm"],
        ["Số dòng đọc được", so_nguyen(len(rows_ky)), "—", ""],
    ]

    # ---- phễu
    ten_tang = [
        ("① Chi phí", t["chi_tieu"], tt["chi_tieu"], "—", "Adnet / Trưởng nhóm", "chi_tieu"),
        ("② Hiển thị", t["impression"], tt["impression"], "CPM " + tien(cs["cpm"]), "Adnet (tệp + bid)", "cpm"),
        ("③ Click", t["click"], tt["click"], "CTR " + pct(cs["ctr"], 2), "Adnet (creative)", "ctr"),
        ("④ Inbox", t["inbox"], tt["inbox"], "Click→Inbox " + pct(cs["click_inbox"], 2), "Adnet (điểm đến)", "click_inbox"),
        ("⑤ Lead", t["lead"], tt["lead"], "Inbox→Lead " + pct(cs["inbox_lead"]), "TRỰC PAGE", "inbox_lead"),
        ("⑥ Booking", t["booking"], tt["booking"], "Lead→Booking " + pct(cs["lead_booking"]), "TELESALES", "lead_booking"),
        ("⑦ Đến", t["den"], tt["den"], "Show-rate " + pct(cs["show_rate"]), "LỄ TÂN / CSKH", "show_rate"),
        ("⑧ Chốt", t["chot"], tt["chot"], "Đến→Chốt " + pct(cs["den_chot"]), "Tư vấn tại cơ sở", "den_chot"),
    ]
    # tầng rò = tầng đầu tiên có tỷ lệ chuyển tiếp xấu đi >= ngưỡng vàng
    tang_ro_idx = None
    for idx, (_, _, _, _, _, key) in enumerate(ten_tang):
        if key in ("chi_tieu",):
            continue
        l, xau = lech(cs.get(key), cst.get(key), key)
        if l is not None and xau and l >= NGUONG["lech_vang"]:
            tang_ro_idx = idx
            break
    pheu = []
    for idx, (ten, a, b, ty_le, chu, key) in enumerate(ten_tang):
        hien_a = tien(a) if key == "chi_tieu" else so_nguyen(a)
        hien_b = tien(b) if key == "chi_tieu" else so_nguyen(b)
        nhan = ""
        if tang_ro_idx is not None:
            nhan = "⚠ TẦNG RÒ" if idx == tang_ro_idx else ("hệ quả" if idx > tang_ro_idx else "")
        pheu.append([ten, hien_a, hien_b, ty_le, dpct(a, b), chu, nhan])

    # ---- theo ZONE
    theo_z = defaultdict(list)
    for r in rows_ky:
        theo_z[(r.get("zone") or "KHAC").upper()].append(r)
    bang_zone = []
    for z, rs in sorted(theo_z.items(), key=lambda x: -gop(x[1])["chi_tieu"]):
        tz = gop(rs)
        csz = chi_so(tz)
        s_chi = tz["chi_tieu"] / t["chi_tieu"] * 100 if t["chi_tieu"] else 0
        s_lead = tz["lead"] / t["lead"] * 100 if t["lead"] else 0
        mt = (muc_tieu.get(z) or {}).get("cpl_muc_tieu")
        dat = "—" if not (mt and csz["cpl"]) else ("✅" if csz["cpl"] <= mt else "❌")
        bang_zone.append([
            z, tien(tz["chi_tieu"]), ("%.1f%%" % s_chi).replace(".", ","), so_nguyen(tz["lead"]),
            ("%.1f%%" % s_lead).replace(".", ","),
            tien(csz["cpl"]), tien(mt) if mt else "[CHỜ CẬP NHẬT]", dat,
            so_nguyen(tz["booking"]), pct(csz["lead_booking"]),
            ("%.1f điểm %%" % (s_chi - s_lead)).replace(".", ","),
        ])

    chan_trang = ("Số liệu tính trên kỳ %s–%s · nguồn %s · cập nhật %s. "
                  "Ngày chưa chốt số đã được loại khỏi kỳ báo cáo."
                  % (ky_dau.strftime("%d/%m"), ky_cuoi.strftime("%d/%m/%Y"),
                     "Meta + CRM" if co_crm else "Meta",
                     datetime.now().strftime("%d/%m/%Y %H:%M")))

    return dict(tom_tat=tom_tat, ket_luan=ket_luan, suc_khoe=suc_khoe, pheu=pheu,
                zone=bang_zone, canh_bao=canh_bao, theo_doi=theo_doi,
                so_ngay_base=(base_cuoi - base_dau).days + 1, chan_trang=chan_trang)


# ---------------------------------------------------------------- CLI
def main():
    ap = argparse.ArgumentParser(
        description="Quét dữ liệu ads theo ngày -> workbook báo cáo + cảnh báo bất thường.")
    ap.add_argument("du_lieu", help="File CSV hoặc XLSX, mỗi dòng = 1 ngày × 1 ad set")
    ap.add_argument("--ky", type=int, default=7, help="Số ngày của kỳ báo cáo (mặc định 7)")
    ap.add_argument("--baseline", type=int, default=14,
                    help="Số ngày trước kỳ dùng làm baseline (mặc định 14)")
    ap.add_argument("--bo-ngay-cuoi", type=int, default=1,
                    help="Bỏ N ngày cuối vì số Meta chưa chốt (mặc định 1)")
    ap.add_argument("--den-ngay", default=None, help="Ngày cuối dữ liệu, YYYY-MM-DD")
    ap.add_argument("--muc-tieu", default=None, help="JSON mục tiêu CPL theo ZONE")
    ap.add_argument("-o", "--out", default="out", help="Thư mục xuất (mặc định out/)")
    args = ap.parse_args()

    rows = doc_du_lieu(args.du_lieu)
    if not rows:
        sys.exit("⛔ Không đọc được dòng dữ liệu nào.")

    muc_tieu = {}
    if args.muc_tieu:
        with open(args.muc_tieu, "r", encoding="utf-8") as f:
            muc_tieu = {k.upper(): v for k, v in json.load(f).items()}

    ngay_max = max(r["ngay"] for r in rows)
    if args.den_ngay:
        ngay_max = _ngay(args.den_ngay)
    ky_cuoi = ngay_max - timedelta(days=args.bo_ngay_cuoi)
    ky_dau = ky_cuoi - timedelta(days=args.ky - 1)
    base_cuoi = ky_dau - timedelta(days=1)
    base_dau = base_cuoi - timedelta(days=args.baseline - 1)

    ngay_min = min(r["ngay"] for r in rows)
    if base_dau < ngay_min:
        print("⚠ Dữ liệu chỉ có từ %s — baseline bị cắt ngắn, kết luận yếu hơn."
              % ngay_min.strftime("%d/%m/%Y"))
        base_dau = ngay_min

    canh_bao, theo_doi = quet(rows, ky_dau, ky_cuoi, base_dau, base_cuoi, muc_tieu)
    ctx = dung_ngu_canh(rows, ky_dau, ky_cuoi, base_dau, base_cuoi, muc_tieu, canh_bao, theo_doi)

    os.makedirs(args.out, exist_ok=True)
    ten = "BaoCao-CanhBao_Ads_%s_%s.xlsx" % (ky_dau.strftime("%d%m"), ky_cuoi.strftime("%d%m"))
    duong_dan = os.path.join(args.out, ten)
    xuat(duong_dan, ctx)

    print("✅ Đã xuất: %s" % duong_dan)
    print("   Kỳ %s–%s · baseline %s–%s"
          % (ky_dau.strftime("%d/%m"), ky_cuoi.strftime("%d/%m"),
             base_dau.strftime("%d/%m"), base_cuoi.strftime("%d/%m")))
    dem = defaultdict(int)
    for p in canh_bao:
        dem[p["muc"]] += 1
    print("   Cảnh báo: 🔴 %d · 🟠 %d · 🟡 %d   |   Theo dõi: %d"
          % (dem["🔴"], dem["🟠"], dem["🟡"], len(theo_doi)))
    print("   ➜ %s" % ctx["ket_luan"])


if __name__ == "__main__":
    main()
