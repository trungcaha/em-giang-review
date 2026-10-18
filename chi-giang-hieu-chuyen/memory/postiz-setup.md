---
name: postiz-setup
description: "Postiz tự host ở mlabai.uk — cách gọi CLI, kênh, mẫu đăng Reel FB kèm link sản phẩm ở bình luận"
metadata:
  node_type: memory
  type: reference
  originSessionId: fe9845e1-7536-44d0-8507-7e7121b78a1b
  modified: 2026-09-30T17:25:43.620Z
---

- API: POSTIZ_API_URL=https://mlabai.uk/api (env cũ trỏ tailscale chết). Key đã setx; phiên cũ có thể còn key cũ → luôn set lại trong lệnh/script.
- Page "Ông Giang Sức Khỏe" (FB) id cmuo8lcts0001r07pcmzv0cv2; TikTok "Hoạt Hình Tấu Hài" cmuobi7wc0007qx7tp9aq2nim.
- Mẫu đã chạy tốt: bam-huyet-series/postiz/schedule.py — upload → JSON settings {"__type":"facebook","post_type":"reel","commentStrategy":"root"}, value[1..] là bình luận chứa link Shopee (delay 1). Link trong bình luận hiện ra sau vài phút — không phải lỗi.
- Dùng JSON mode (tiếng Việt an toàn), không truyền caption qua tham số PowerShell.
