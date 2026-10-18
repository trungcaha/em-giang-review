# -*- coding: utf-8 -*-
"""python build.py         → làm mới file HTML (giữ nguyên file Excel và số liệu đã nhập)
python build.py excel   → tạo lại file Excel từ đầu (XÓA số liệu đã nhập – chỉ dùng khi chưa nhập gì)
python build.py all     → cả hai"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mode = (sys.argv[1] if len(sys.argv) > 1 else "html").lower()
XLSX = os.path.join(OUT, "van-hanh-kenh-chi-giang.xlsx")
if mode in ("excel", "all") or not os.path.exists(XLSX):
    import build_xlsx
    print(build_xlsx.build(XLSX))
if mode in ("html", "all"):
    import build_html
    print(build_html.build(os.path.join(OUT, "du-an-chi-giang.html")))
