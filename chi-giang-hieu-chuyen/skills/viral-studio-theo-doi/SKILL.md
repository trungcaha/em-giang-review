---
name: viral-studio-theo-doi
description: Theo dõi và xử lý hàng đợi video Viral Studio — xem tiến độ, tạo lại đoạn lỗi, tạm dừng/chạy tiếp, xuất và ghép video hoàn chỉnh. Dùng skill này khi người dùng hỏi "video sao rồi", "hàng đợi thế nào", "xong chưa", "đoạn 3 bị lỗi/xấu, làm lại", "tạm dừng", "chạy tiếp", "xuất video", "ghép video", "thêm nhạc/phụ đề", hoặc nhắc tới một video đã tạo bằng Viral Studio.
---

# Theo dõi và hoàn thiện video Viral Studio

Người dùng muốn biết **video của họ đang ở đâu** và **lấy được file**. Trả lời bằng lời thường, không đổ nguyên JSON.

## Xem tiến độ

Gọi `studio_status` (không tham số) để có tổng quan. Tóm tắt:

```
📊 Hàng đợi: 2 xong · 1 đang làm · 1 lỗi · 3 chờ
✅ Dưa leo đi khám — 4/4 đoạn
⏳ Review son Ruby — 2/4 đoạn (đang làm đoạn 3)
❌ Bánh mì sáng — đoạn 2 lỗi: AI báo hết lượt
```

Cần chi tiết một video → `studio_status` với `job_id`. Người dùng gọi video bằng tên → khớp theo tiêu đề trong danh sách, không bắt họ đưa id.

Nếu hàng đợi đang tạm dừng, nói rõ lý do (có trong kết quả) và việc cần làm, ví dụ hết lượt thì "chờ tới <giờ> hoặc đổi tài khoản".

## Sửa đoạn lỗi hoặc chưa ưng

- Một đoạn: `studio_segment_retry` với `job_id`, `idx` (**tính từ 0** — "đoạn 3" của người dùng là `idx: 2`), và `fix` mô tả ngắn cần sửa gì ("0–4s: cuộn giấy màu xanh, đổi thành màu ngà; giữ nguyên 4–10s"). Chỉ đổi `prompt`/`dialogue` khi người dùng muốn viết lại cả đoạn.
- Mọi đoạn lỗi của một video / cả lô: `studio_control` `action: "retry_failed"` với `job_id` hoặc `project_id`.

Đoạn được làm lại sẽ lên đầu hàng đợi; báo người dùng điều đó.

## Điều khiển hàng đợi

`studio_control` với `action`:
- `pause` / `resume` — cả hàng đợi.
- `cancel` / `uncancel` — một video (`job_id`) hoặc một lô (`project_id`).
- `approve` — khi tạo với `review: true`, duyệt các đoạn nháp để chạy.
- `delete` — **xác nhận với người dùng trước**, vì không lấy lại được.

## Xuất và ghép video

- `studio_export_all` (tuỳ chọn `project_id` hoặc `job_ids`) → tải **hết** video đã xong về máy trong 1 lần gọi; dùng khi khách nói "tải hết video".
- `studio_export` với `job_id` → lưu từng đoạn ra `…/studio/<video>/canh-NN.mp4` và trả đường dẫn.
- `merge: true` → ghép thành `<video>-final.mp4`. Cần FFmpeg; nếu báo "Không chạy được ffmpeg" → hướng dẫn `winget install Gyan.FFmpeg` rồi mở lại Claude.
- Chỉ xuất khi mọi đoạn đã xong; nếu chưa, nói còn thiếu đoạn nào.

Báo đường dẫn file cuối cùng để người dùng mở.

### Dựng thêm (nhạc, phụ đề, logo, giọng đọc)

Khi người dùng muốn, dùng FFmpeg trên các file đã xuất. Làm vào file mới (vd `<video>-final-nhac.mp4`), **không ghi đè** file gốc. Hỏi file nhạc/logo nằm đâu nếu chưa có. Phụ đề có thể lấy từ lời thoại các đoạn trong `studio_status` chi tiết.

## Khi có lỗi lạ

Mất kết nối, chưa kích hoạt, báo lệch version, extension không phản hồi → dùng skill `viral-studio-sua-loi`.
