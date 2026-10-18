---
name: viral-studio-tao-video
description: Tạo video AI hàng loạt bằng Viral Studio từ ý tưởng của người dùng — viết kịch bản tiếng Việt, cho duyệt, tạo hồ sơ nhân vật/sản phẩm để giữ đồng nhất, rồi xếp hàng bằng studio_create. Dùng skill này khi người dùng nói "làm video…", "tạo N video…", "viết kịch bản rồi đưa vào Viral Studio", "video review sản phẩm có nhân vật X", "làm video TikTok/Reels/Shorts", hoặc đưa ảnh nhân vật/sản phẩm và muốn ra video — kể cả khi họ không nhắc tên Viral Studio nhưng tool studio_create đang có.
---

# Tạo video với Viral Studio

Người dùng là người bán hàng / làm nội dung, muốn có video nhanh, không muốn học kỹ thuật. Bạn là "đạo diễn": hiểu ý → viết kịch bản → **cho duyệt** → xếp hàng → báo cách theo dõi. Nói tiếng Việt, ngắn gọn.

## Vì sao phải duyệt trước

Mỗi video tốn lượt tạo của tài khoản muse.ai (có giới hạn mỗi giờ/ngày). Kịch bản sai ý = mất lượt + mất thời gian chờ. Vì vậy **luôn đưa kịch bản cho người dùng xem và chờ họ đồng ý** trước khi gọi `studio_create`. Ngoại lệ duy nhất: họ nói rõ "không cần duyệt, làm luôn".

## Quy trình

### 1. Kiểm tra nhanh

Gọi `studio_license` (không key). Chưa kích hoạt hoặc tool không tồn tại → chuyển sang skill `viral-studio-setup` / `viral-studio-sua-loi`, đừng viết kịch bản trước.

### 2. Hiểu yêu cầu — hỏi tối đa một lần

Cần biết: **số video**, **chủ đề/sản phẩm**, **độ dài** (mặc định 30–40 giây), **tỉ lệ** (mặc định 9:16), **phong cách** (người thật / hoạt hình 3D / …), **nhân vật hoặc sản phẩm cố định** (có ảnh không). Thiếu gì quan trọng thì gom thành **một** câu hỏi kèm gợi ý mặc định; phần còn lại tự chọn hợp lý và nói ra.

Nếu người dùng muốn video hài y khoa kiểu "nhân vật biết nói" và skill `kich-ban-hoat-hinh-hai` có sẵn, dùng nó để viết kịch bản đúng giọng văn đó.

### 3. Hồ sơ nhân vật / sản phẩm (để các cảnh giống nhau)

- Gọi `studio_profile_list`. Có hồ sơ trùng tên → dùng lại.
- Người dùng đưa ảnh (đường dẫn tuyệt đối trên máy) → `studio_profile_create` với `name`, `kind` (`character` | `product` | `scene`), `description` mô tả cố định bằng tiếng Việt (khuôn mặt, tuổi, tóc, trang phục / hình dáng, màu, nhãn sản phẩm), `images` (tối đa 4 ảnh có tác dụng).
- Không có ảnh vẫn làm được: chỉ cần `description` chi tiết.

### 4. Viết kịch bản và trình duyệt

Mỗi video là chuỗi **shot ≤ 10 giây** trong cùng một chat AI. Trình bày cho người dùng dạng dễ đọc:

```
🎬 Video 1: <tiêu đề> (~36s, 9:16)
Shot 1 (0–10s): <hành động, góc máy> — Lời thoại: "<…>"
Shot 2 (10–20s): …
```

Kèm 1 dòng **khối đồng nhất** (nhân vật, bối cảnh, sản phẩm, phong cách quay, giọng nói) — dòng này sẽ lặp lại ở mọi shot để AI vẽ nhất quán.

Hỏi: "Bạn duyệt các kịch bản này chứ? Muốn sửa video nào cứ nói." Chờ trả lời.

### 5. Xếp hàng

Khi đã duyệt, gọi **một lần** `studio_create` cho cả lô:

- `project`: tên lô dễ nhận (vd "Review son tháng 10").
- `profiles`: tên các hồ sơ dùng chung.
- `ratio`, `style`, `consistency` (khối đồng nhất ở trên).
- `jobs[]`: mỗi video một phần tử, `title`, `genre`, và **hoặc** `segments[]` (`prompt` có mốc giờ "0–4s: … 4–10s: …", `dialogue`, `end_frame`, `duration` ≤ 10) **hoặc** chỉ `script` + `target_sec` để AI tự chia. Ưu tiên tự viết `segments` vì kết quả ổn định hơn.
- `review: true` chỉ khi người dùng muốn duyệt từng đoạn sau khi tạo.

### 6. Báo kết quả

Nói ngắn: đã xếp hàng mấy video, ước lượng thời gian (khoảng 3–6 phút mỗi shot, chạy tuần tự), và cách theo dõi: "Hỏi tôi *video sao rồi* bất cứ lúc nào, hoặc xem Dashboard Viral Studio." Không gọi `studio_status` liên tục để chờ — video chạy nền.

## Gợi ý chất lượng

- Lời thoại tiếng Việt tự nhiên, câu ngắn, đọc được trong thời lượng shot (~3 từ/giây).
- `end_frame` của shot trước mô tả khung cuối để shot sau nối tiếp mượt.
- Tránh nội dung vi phạm chính sách của muse.ai (bạo lực, người nổi tiếng có thật, thương hiệu giả mạo) — sẽ bị từ chối và tốn lượt.
