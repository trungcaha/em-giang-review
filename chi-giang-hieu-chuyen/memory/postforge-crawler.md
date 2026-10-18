---
name: postforge-crawler
description: "PostForge crawl link Shopee affiliate qua điện thoại ADB – skill ở .gemini, cách sửa ADB, lỗi link trùng do clipboard"
metadata:
  node_type: memory
  type: reference
  originSessionId: ebee44ce-633c-435d-a3cf-5b99270b9a31
  modified: 2026-10-16T08:18:03.524Z
---

Skill `postforge-shopee-crawler`: `C:\Users\PC\.gemini\config\skills\postforge-shopee-crawler\` (SKILL.md + scripts/crawl_batch_to_excel.py); bản trong dự án `.agents/skills/` chỉ trỏ tới đó. Server `http://127.0.0.1:8765`, code ở `shopee-aff-crawler/`. Mỗi sản phẩm ~2,5 phút.

- adb không có trong PATH: `C:\Users\PC\AppData\Local\Android\Sdk\platform-tools\adb.exe`. Lỗi "protocol fault" → `adb kill-server` rồi `start-server`; S24 Ultra serial R5CWC2TMHWL.
- Lỗi đã gặp 16/10/2026: khi nút "Sao chép" không bấm được (hàng nhạy cảm như gel bôi trơn), crawler đọc clipboard cũ → **link trùng sản phẩm trước**, và ảnh bị ghi đè vào thư mục của link đó (thư mục ảnh đặt theo mã link). Shopee tạo link mới mỗi lần chia sẻ, nên link trùng = chắc chắn sai.
- Cách xử lý: `research/chi-giang-sp/gop-va-kiem-tra.py <file chính> <file crawl lại>` gộp và tự bỏ link trùng; kiểm tra giờ sửa img_01 trong thư mục ảnh.
- Giá crawl có thể là phân loại rẻ nhất (vd. bao cao su 20k, trà 7,2k).
