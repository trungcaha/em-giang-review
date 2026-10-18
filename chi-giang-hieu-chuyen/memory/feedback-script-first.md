---
name: feedback-script-first
description: Luôn đưa kịch bản cho người dùng duyệt trước khi dựng/lồng tiếng video mới
metadata:
  node_type: memory
  type: feedback
  originSessionId: 00dc414e-6e5a-43fd-b32f-f25d349f3358
  modified: 2026-09-28T15:35:09.116Z
---

Với video mới (nhất là chủ đề nhạy cảm), viết kịch bản dạng bảng (hành động + lời thoại) và chờ người dùng duyệt rồi mới build/TTS/render.

**Why:** người dùng đã chặn lệnh build và yêu cầu "đưa cho tôi kịch bản của bạn trước", rồi đổi ý tưởng nhiều lần.
**How to apply:** kịch bản trước → duyệt → mới làm. Liên quan [[feedback-simple-hook]], [[script-writer-skill]].
