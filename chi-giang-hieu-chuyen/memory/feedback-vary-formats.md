---
name: feedback-vary-formats
description: "Loạt video nhiều tập phải khác hẳn nhau — màu nền, bối cảnh, thể loại kể chuyện; không lặp một khuôn"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 892684ac-be0c-49bc-ae14-0b86ca05436e
  modified: 2026-10-07T05:06:05.479Z
---

Khi làm loạt nhiều video cho cùng sản phẩm (2026-10-07, 20 video Oniiz), người dùng chê bản lặp cùng nền xanh "trong quần lót" + cùng khuôn "ai cho ở / có giấy phép không / bọt cuốn trôi". Muốn mỗi video một màu, một bối cảnh, một thể loại (tòa án, bản tin, gameshow, lớp học, thám tử, hẹn hò, bóng đá, siêu anh hùng, thời tiết, tin nhắn, review ẩm thực, môi giới, kinh dị, tour, đám cưới, hoa hậu, họp công ty, phỏng vấn, nấu ăn, radio).

**Why:** loạt video giống nhau nhìn nhàm, kênh mất hấp dẫn.
**How to apply:** dùng prompts/kit/kit_sets.js (BG `set` + key) và films_oniiz3.py (hàm mk, theme màu cho promo/guide). Chụp lưới 1 khung/phim kiểm tra độ khác trước khi render. Liên quan [[feedback-affiliate-soft-product]], [[feedback-simple-hook]].
