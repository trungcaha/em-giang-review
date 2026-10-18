---
name: feedback-viral-studio-queue
description: Video nhiều shot phải chạy qua studio_create (hiện trong bảng Studio), không vs_send thẳng chat
metadata:
  type: feedback
---

Khi user bảo "chạy qua Viral Studio", dùng studio_create (hàng đợi Studio, tự chia shot/nối frame/ghép/lưu) chứ không vs_send master prompt vào chat Muse. Muse Bridge đã gỡ hẳn 2026-10-01, chỉ dùng viral-studio.

**Why:** 2026-10-01 mình vs_send master prompt Sói & Heo, user thắc mắc sao task không hiện trong bảng Studio.
**How to apply:** tạo profile ảnh nhân vật (studio_profile_create) rồi studio_create với consistency + segments; theo dõi bằng studio_status. Liên quan [[feedback-muse-send-nowait]], [[viral-studio-desktop-helper]].
