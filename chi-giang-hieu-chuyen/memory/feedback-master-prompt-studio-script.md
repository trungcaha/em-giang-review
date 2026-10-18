---
name: feedback-master-prompt-studio-script
description: "Đẩy master prompt sang Viral Studio" = studio_create, mỗi master prompt nguyên văn làm job.script; không tách shot, không vs_send chat
metadata:
  type: feedback
---
Khi user bảo đẩy/dựng master prompt qua Viral Studio: gọi studio_create, mỗi file master prompt = 1 job, `script` = nguyên văn khối prompt (từ "Bạn là đạo diễn…"), target_sec theo prompt, profile sản phẩm (vd "Giọt Lành Dừa Oliu"). KHÔNG tự tách segments/consistency, KHÔNG gửi qua vs_send/vs_new_chat.

**Why:** user ngắt 2 lần (2026-10-01): "không cách tách, mỗi master prompt chạy trực tiếp thành 1 câu lệnh", "phải chạy qua viral studio task chứ, không chạy qua chat".

**How to apply:** liên quan [[feedback-viral-studio-queue]], [[feedback-muse-means-viral-studio]].
