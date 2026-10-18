---
name: feedback-analyze-viral-before-script
description: "Khi đưa link video viral và bảo viết kịch bản tương tự: tải video, tách lời, phân tích kịch bản + cách chọn chủ đề rồi mới viết kịch bản mới"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 9507cf1e-f3b0-4e4c-b284-7f2a7f7f6b0d
  modified: 2026-10-10T02:24:29.415Z
---

Ngày 2026-10-10, người dùng gửi 3 link TikTok @trungrealai và bảo "tạo kịch bản tương tự". Tôi chỉ đưa một kịch bản mới (hai trứng) kèm tóm tắt ngắn; người dùng sửa lại: muốn **phân tích kịch bản 3 video viral, cách chọn chủ đề, rồi kịch bản chi tiết** — kịch bản mới phải hài, nhiều tình tiết, hay ngang video gốc.

**Why:** họ muốn hiểu vì sao video viral để lặp lại được, không chỉ nhận một kịch bản. (Diễn giải của tôi: kịch bản đầu chọn chủ đề "chuyện lạ" chứ không phải câu ngại hỏi nên chưa thuyết phục.)

**How to apply:** với yêu cầu "làm tương tự video viral này": yt-dlp tải về `downloads/<kenh>/`, Whisper tách lời, đọc số liệu (share/view quan trọng hơn view thô), mổ từng video theo mốc giây + nguồn cười + điểm yếu, rút công thức, chấm điểm chủ đề, rồi mới viết kịch bản và đối chiếu lại công thức. Mẫu đã làm: `prompts/dien-tap-thoi.md` (có thước chấm chủ đề 5 câu A–E). Liên quan [[script-writer-skill]], [[feedback-simple-hook]], [[feedback-script-first]].
