---
name: feedback-muse-send-nowait
description: "Khi gửi Muse, dùng vs_send wait=false rồi vs_read khi user hỏi \"sao rồi\""
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5a274b2b-87a6-4db6-b019-b1a431083f3a
  modified: 2026-09-29T16:36:09.224Z
---

User hay ngắt (reject) muse_send khi nó chờ lâu, nhưng tin nhắn vẫn đã gửi và Muse vẫn tạo video. Sau đó user hỏi "sao rồi".

**Why:** muse_send chờ reply video (vài phút) làm user sốt ruột; rejection không có nghĩa là không muốn gửi.
**How to apply:** gửi bằng vs_send wait=false (hoặc studio_create cho video nhiều shot), báo đã gửi; khi user hỏi "sao rồi" thì vs_read vài tin cuối và báo link video.

Cũng áp dụng cho muse_wait_reply: KHÔNG dùng idle_sec lớn (vd 400s) với tác vụ Muse tự chạy nhiều bước — Muse xong rồi nhưng tool vẫn chờ, user phải ngắt (2026-09-30). Dùng idle_sec ~60 + timeout ngắn, rồi muse_read kiểm tra tin cuối; video ghép cuối Muse trả dạng link muse.ai/files (muse_download_media tải được "via link").
