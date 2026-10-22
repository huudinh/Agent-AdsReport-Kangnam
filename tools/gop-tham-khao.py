#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gộp các file tham khảo thành file dự phòng trong `goi/`.

Vì sao cần: Gemini Gems chỉ cho **tối đa 10 file** tri thức, ChatGPT Custom GPT
cho 20 nhưng upload hàng chục file một lượt rất hay lỗi. Bản gộp là **đường dự
phòng** — upload ít file hơn mà **không mất nội dung nào**. Bản rời trong thư
mục nguồn vẫn là bản chính; bộ não biết cả hai cách.

Mỗi phần trong file gộp bắt đầu bằng dòng

    ===== ten-file.md =====

nên trợ lý vẫn biết đang đọc module nào, và mọi tham chiếu chéo dạng
`[[ten-file]]` trong văn bản vẫn trỏ đúng — chỉ đổi chỗ nằm, không đổi mã.

⛔ KHÔNG sửa tay file trong `goi/` — sửa ở thư mục nguồn rồi chạy lại:

    python tools/gop-tham-khao.py

Đánh đổi phải biết trước: dùng bản gộp thì **mất khả năng thay riêng một
module** (ví dụ file chiến dịch tháng) — phải sinh lại và upload lại cả file.
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
GOC = Path(__file__).resolve().parent.parent
RA = GOC / "goi"

# ---------------------------------------------------------------------------
# CẤU HÌNH — sửa ở đây khi thêm/bớt thư mục nguồn.
#   ra      : tên file sinh ra trong goi/
#   tieu_de : dòng H1 của file gộp
#   mo_ta   : đơn vị đếm, điền vào câu "File này gộp N <mo_ta>"
#   nguon   : danh sách (thư mục, mẫu glob) — giữ đúng thứ tự muốn trợ lý đọc
# ---------------------------------------------------------------------------
GOI = [{'ra': 'GOP-tri-thuc.md',
  'tieu_de': 'TRI THỨC — Agent AdsReport Kangnam',
  'mo_ta': 'module tri thức',
  'nguon': [('knowledge', 'ar-*.md')]}]

# File trong thư mục nguồn nhưng KHÔNG upload — xem doc/01-cai-dat.md.
BO_QUA = []


def thu_file(goi: dict) -> list[Path]:
    ds: list[Path] = []
    for thu_muc, mau in goi["nguon"]:
        for f in sorted((GOC / thu_muc).glob(mau)):
            if f.name in BO_QUA:
                continue
            ds.append(f)
    return ds


def kb(n: int) -> str:
    return f"{n / 1024:.1f} KB"


def dung(goi: dict) -> tuple[Path, int, int]:
    ds = thu_file(goi)
    if not ds:
        raise SystemExit(f"Không thấy file nguồn nào cho {goi['ra']} — kiểm lại mẫu glob")

    thu_mucs = sorted({f.parent.name for f in ds})
    d = [
        f"# {goi['tieu_de']}",
        f"> File này gộp **{len(ds)} {goi['mo_ta']}** từ "
        + " · ".join(f"`{t}/`" for t in thu_mucs)
        + f". Sinh tự động ngày {date.today().isoformat()} bằng "
        "`python tools/gop-tham-khao.py`.",
        "> ⛔ **Không sửa file này** — sửa ở bản rời trong thư mục nguồn rồi chạy lại lệnh trên.",
        "",
        "**Cách đọc:** mỗi phần bắt đầu bằng dòng `===== tên file =====` và là "
        "**một đơn vị tri thức riêng**. Tham chiếu dạng `[[tên-file]]` trong văn bản trỏ tới "
        "**phần cùng tên ngay trong file này**, không phải file bên ngoài.",
        "",
        "## MỤC LỤC",
        "",
        "| # | File | Cỡ |",
        "|---|---|---|",
    ]
    tong = 0
    than: list[str] = []
    for i, f in enumerate(ds, 1):
        noi = f.read_text(encoding="utf-8").strip()
        tong += len(noi.encode("utf-8"))
        d.append(f"| {i} | `{f.name}` | {kb(len(noi.encode('utf-8')))} |")
        than += ["", f"===== {f.name} =====", "", noi, ""]
        print(f"  {f.parent.name}/{f.name}  ·  {kb(len(noi.encode('utf-8')))}")

    d.append("")
    dich = RA / goi["ra"]
    dich.write_text("\n".join(d + than) + "\n", encoding="utf-8")
    return dich, len(ds), tong


def main() -> int:
    RA.mkdir(exist_ok=True)
    tao = []
    for goi in GOI:
        print(goi["ra"])
        dich, n, tong = dung(goi)
        print(f"=> {dich.name}  —  {kb(dich.stat().st_size)}  ({n} file nguồn, {kb(tong)} nội dung)\n")
        tao.append((dich.name, n))

    nguon = sum(n for _, n in tao)
    print(f"UPLOAD đường dự phòng: {' + '.join(t for t, _ in tao)} "
          f"= **{len(tao)} file**  (bản rời là {nguon} file)")
    print("Bản rời vẫn là bản chính. Chỉ dùng bản gộp khi chạm trần số file hoặc upload hay lỗi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
