---
name: feedback-hook-card
description: "Hook title card spec for talking-head videos — big magenta box, static 0–7s, below chin"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 83f2f726-b60c-409f-9681-319ef363864b
  modified: 2026-10-11T10:15:27.461Z
---

Hook title card (video "người nói", e.g. mat-mo-bam-huyet/overlay2.py `draw_hook`): 2 dòng chữ trắng in hoa (seguibl, stroke 5 tối), font tự co để dòng dài nhất ≤ W−90 (~100px @720w), hộp chữ nhật magenta (225,10,170) rộng W−44, không bo góc. Đặt dưới cằm: yc = max(chin+40+CH/2, 0.70·H). Hiện NGAY giây 0, KHÔNG pop-in/scale, tĩnh suốt 0–7s; ẩn karaoke + card khác trong 7s đó.

**Why:** user muốn giống video viral gốc (hộp hồng, chữ trắng to) — hút ngay, không che mặt.
**Ngoại lệ (11/10/2026):** với video hoạt hình nhân vật biết nói (remake-video-hoat-hinh, vd giao-nham-khan-giay), user bảo "bỏ cái text card đỏ này, từ giờ đừng tự thêm vào nữa" → KHÔNG tự thêm hộp tiêu đề (`CONFIG.hook = null`), chỉ thêm khi user yêu cầu rõ. (Diễn giải của tôi: áp dụng cho video hoạt hình; talking-head chưa được nhắc lại.)
**How to apply:** chỉ video talking-head có hook tiêu đề; hoạt hình thì không tự thêm. Liên quan [[feedback-simple-hook]].
