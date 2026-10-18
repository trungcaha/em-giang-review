# -*- coding: utf-8 -*-
"""Gộp kết quả crawl lại vào san-pham-kenh-chi-giang.xlsx và kiểm tra link trùng.
Link trùng = crawler đọc nhầm clipboard cũ (Shopee tạo link mới mỗi lần chia sẻ), nên dòng trùng bị xóa link.
Chạy: python gop-va-kiem-tra.py <file chính> <file crawl lại> [<file crawl lại 2> ...]"""
import sys, importlib.util
from collections import Counter
import openpyxl

spec = importlib.util.spec_from_file_location(
    "cb", r"C:\Users\PC\.gemini\config\skills\postforge-shopee-crawler\scripts\crawl_batch_to_excel.py")
cb = importlib.util.module_from_spec(spec); spec.loader.exec_module(cb)
from pathlib import Path

KEYS = ["stt", "group", "req_name", "title", "price_text", "commission_text", "aff_link", "sub_link", "folder_path", "image_count"]


def read(path):
    ws = openpyxl.load_workbook(path).active
    return [dict(zip(KEYS, r)) for r in ws.iter_rows(min_row=2, values_only=True) if r[0] is not None]


main_path = Path(sys.argv[1])
rows = read(main_path)
by_name = {r["req_name"]: r for r in rows}
for i, r in enumerate(rows):
    r["_order"] = i            # dòng gốc: theo thứ tự crawl
# Trong đợt gốc, dòng thứ hai trở đi của một link trùng chắc chắn sai – đánh dấu trước khi gộp
_seen = set()
for r in rows:
    r["_bad"] = bool(r["aff_link"]) and r["aff_link"] in _seen
    _seen.add(r["aff_link"])
n = 0
for extra in sys.argv[2:]:
    for r in read(extra):
        if r["req_name"] in by_name and r["aff_link"]:
            old = by_name[r["req_name"]]
            for k in KEYS[3:]:
                old[k] = r[k]
            n += 1
            old["_order"] = 1000 + n   # dòng crawl lại: xếp sau mọi dòng gốc
            old["_bad"] = False
            print("Thay:", r["req_name"], "->", r["aff_link"], "|", (r["title"] or "")[:60])

for r in rows:
    if r["_bad"]:
        print("BỎ link trùng (đợt gốc, chưa crawl lại được):", r["req_name"], r["aff_link"])
        r.update(title="(Không lấy được link affiliate – trùng link sản phẩm khác)", price_text="", commission_text="",
                 aff_link="", folder_path="", image_count=0)
# Mỗi link chỉ đúng với dòng lấy được nó sớm nhất; các dòng sau có cùng link là đọc nhầm clipboard.
cnt = Counter(r["aff_link"] for r in rows if r["aff_link"])
for link, c in cnt.items():
    if c < 2:
        continue
    holders = sorted([r for r in rows if r["aff_link"] == link], key=lambda r: r["_order"])
    print("Giữ:", holders[0]["req_name"], link)
    for r in holders[1:]:
        print("BỎ link trùng:", r["req_name"], link)
        r.update(title="(Không lấy được link affiliate – trùng link sản phẩm khác)", price_text="", commission_text="",
                 aff_link="", folder_path="", image_count=0)

out = []
for r in rows:
    out.append(dict(group=r["group"], req_name=r["req_name"], title=r["title"], price_text=r["price_text"],
                    commission_text=r["commission_text"], aff_link=r["aff_link"] or "", folder_path=r["folder_path"] or "",
                    image_count=r["image_count"] or 0, sub_channel="ChiGiang"))
cb.save_to_excel(out, main_path, sub_prefix="ChiGiang")
