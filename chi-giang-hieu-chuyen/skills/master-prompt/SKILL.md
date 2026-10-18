---
name: master-prompt
description: Viết MASTER PROMPT chuẩn cho Muse (muse.ai) từ một ý tưởng video sản phẩm — một khối prompt tiếng Việt dán thẳng vào Muse là AI tự tạo ảnh nhân vật chuẩn, chia shot 10 giây, tạo từng shot và ghép thành video quảng cáo dọc hoàn chỉnh. Dùng khi người dùng gõ /master-prompt, hoặc nói "viết master prompt", "prompt muse cho sản phẩm X", "làm prompt video quảng cáo cho …", "đổi bối cảnh master prompt", "làm loạt prompt N bối cảnh", kể cả khi chỉ đưa tên sản phẩm + một câu ý tưởng.
argument-hint: "[ý tưởng video: sản phẩm + tình huống, ví dụ: dầu gội thảo dược, gội cho bà bán rau tóc xù ngoài chợ]"
---

# /master-prompt — từ ý tưởng ra prompt Muse chạy được ngay

Người dùng chỉ cần đưa **ý tưởng** (sản phẩm + tình huống). Bạn trả về **một khối prompt hoàn chỉnh**, dán vào Muse là chạy, không cần sửa. Khung prompt nằm ở `references/template.md` — đã chạy thật hàng chục video, nên **giữ nguyên các phần luật**, chỉ điền phần `{…}`.

## Bước 1 — Lấy ý tưởng

- Nếu lệnh đã kèm ý tưởng (sau `/master-prompt …`) → dùng luôn.
- Nếu chưa có → hỏi đúng **một** câu: *"Bạn muốn làm video cho sản phẩm gì, trong tình huống nào? (ví dụ: dầu gội thảo dược — gội cho bà bán rau tóc xù ngoài chợ)"*.
- Không hỏi thêm. Thiếu gì thì tự chọn mặc định hợp lý và ghi ở dòng "Mình đã tự chọn" phía dưới:
  - Thời lượng **30 giây** (3 shot × 10s), tỉ lệ **9:16**.
  - Bối cảnh Việt Nam đời thường, quay kiểu điện thoại cầm tay.
  - Kịch bản **"hook – xung đột – biến đổi – kết quả – phản ứng"**: 5 giây đầu sản phẩm đã đang được dùng; có một nhân vật phản đối/nghi ngờ tạo kịch tính; biến đổi diễn ra **từ từ** qua các shot; cuối cùng ngạc nhiên vui vẻ, sản phẩm trong khung.
  - 3–4 câu thoại ngắn, tiếng Việt tự nhiên (giọng miền Bắc nếu không nói khác).

Nếu người dùng có ảnh sản phẩm/ảnh nhân vật trên máy (đường dẫn), mở xem ảnh để mô tả sản phẩm chính xác (màu, hình dáng, chữ trên nhãn). Không có ảnh thì mô tả theo hiểu biết và nhắc họ đính kèm ảnh sản phẩm khi dán vào Muse.

## Bước 2 — Viết prompt

1. Đọc `references/template.md`. Tham khảo 2 ví dụ thật trong `references/` (dầu gội — chợ rau; dầu gội — ông chồng dữ) để biết mức chi tiết cần đạt.
2. Điền mọi `{…}`. Quan trọng nhất cho chất lượng video:
   - **Mô tả sản phẩm cực kỹ** (màu, chất liệu, nắp/vòi, chữ trên nhãn) — đây là thứ Muse hay vẽ sai.
   - **Diễn biến biến đổi từng nấc**, và khung cuối shot trước = khung đầu shot sau.
   - **Hook ngay khung đầu**: không có cảnh đi tới, chào hỏi.
   - Lời thoại đọc vừa trong thời lượng (~3 từ/giây), mỗi câu gắn đúng mốc giây.
   - Không người nổi tiếng thật, không nhãn hiệu của người khác, không khẳng định công dụng y khoa sai.
3. Tự soát trước khi trả: không còn `{` hay `}`, số shot = tổng giây / 10, các câu thoại ở mục 1 khớp đúng chữ với phần phân shot, tên sản phẩm thống nhất.

## Bước 3 — Trả kết quả

Trả theo đúng khuôn này:

````
**Master prompt: <tên ngắn>** — <30s, 9:16, 3 shot>
Mình đã tự chọn: <các mặc định đã chọn, 1 dòng>

Cách dùng: mở chat mới trên Muse → đính kèm **ảnh 1 = mặt nhân vật** (nếu có) và **ảnh 2 = ảnh sản phẩm** → dán toàn bộ khối dưới đây → gửi.

```text
<toàn bộ prompt>
```
````

Sau đó lưu prompt vào file `master-prompts/<slug>.md` trong thư mục hiện tại (tạo thư mục nếu chưa có) và nói đường dẫn.

Cuối cùng, nếu tool `studio_create` có sẵn, hỏi một câu: *"Muốn mình đưa thẳng vào Viral Studio chạy luôn không?"* — nếu đồng ý, gọi `studio_create` với `mode: "master"`, `project` = tên ngắn, `jobs: [{ title: <tiêu đề>, script: <toàn bộ prompt>, target_sec: <tổng giây> }]`, kèm `profiles` nếu người dùng có hồ sơ nhân vật/sản phẩm (xem `studio_profile_list`).

## Làm loạt nhiều bối cảnh

Khi người dùng muốn "N video cùng sản phẩm, khác bối cảnh": giữ nguyên SẢN PHẨM, LUẬT, DIỄN BIẾN; chỉ đổi NHÂN VẬT, BỐI CẢNH, tình huống, lời thoại cho hợp từng bối cảnh. Lưu mỗi prompt một file `master-prompts/<slug>-NN-<boi-canh>.md` và liệt kê đường dẫn; nếu đưa vào Viral Studio thì gọi `studio_create` **một lần** với N phần tử trong `jobs`.
