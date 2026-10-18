---
name: viral-studio-sua-loi
description: Chẩn đoán và hướng dẫn sửa lỗi Viral Studio cho khách không rành kỹ thuật — chưa kết nối, chưa kích hoạt, "Không kết nối được máy chủ license", proxy/VPN chặn, hết lượt muse.ai, phiên đăng nhập hết hạn, lệch version server/extension, hàng đợi đứng yên, không ghép được video. Dùng skill này khi người dùng nói Viral Studio "không chạy", "bị lỗi", "đứng im", "báo đỏ", dán thông báo lỗi hoặc ảnh chụp màn hình của Viral Studio, hoặc khi một tool vs_* / studio_* trả về lỗi.
---

# Sửa lỗi Viral Studio

Khách không cần hiểu nguyên nhân kỹ thuật. Với mỗi lỗi: **tự kiểm tra những gì kiểm tra được**, rồi nói **đúng một việc** khách cần làm, bằng một hai câu. Xong việc đó mới nói việc tiếp theo.

## Bước 1 — Thu thập (tự làm, không hỏi khách)

Gọi lần lượt, bỏ qua tool nào không có:
1. `vs_status` — extension có kết nối với Claude không.
2. `studio_license` — trạng thái license.
3. `studio_status` — hàng đợi có tạm dừng / lỗi gì.

Nếu khách dán ảnh chụp màn hình hoặc câu lỗi, đọc kỹ trước — thường đã đủ để biết nguyên nhân.

## Bước 2 — Đối chiếu bảng lỗi

| Dấu hiệu | Nguyên nhân | Nói với khách |
|---|---|---|
| Không có tool `vs_*`/`studio_*` | Claude chưa nối MCP | Dùng skill `viral-studio-setup`. |
| `vs_status` hết thời gian / "extension not connected"; side panel "Chưa kết nối" | Chrome chưa mở, hoặc side panel/extension chưa chạy | "Mở Chrome và bấm icon Viral Studio để mở side panel, giữ Chrome mở, rồi thử lại." |
| "Chưa kích hoạt" | Chưa nhập key | "Mở side panel Viral Studio, dán license key, bấm Kích hoạt." |
| "Không kết nối được máy chủ license" | Máy không ra được internet tới máy chủ license — thường do **proxy hoặc VPN** | Nếu Chrome có hộp "Đăng nhập proxy": "Điền tài khoản proxy vào hộp đó — Viral Studio sẽ chạy tiếp." Nếu không: "Tắt VPN/proxy một lát, bấm Kích hoạt, rồi bật lại." Sau khi kích hoạt, dùng offline được nhiều ngày. |
| "Key đã dùng trên máy khác" | Key đã đủ số máy | "Nhắn người bán để reset máy cho key, rồi nhập lại key." |
| "Key đã bị thu hồi" | Người bán thu hồi | "Liên hệ người bán." |
| "Đang offline, còn dùng được X ngày" | Tạm mất kết nối máy chủ license | Không cần làm gì ngay; nhắc kết nối mạng (tắt VPN) trong X ngày. |
| "Server Claude đang ở bản … extension ở bản …" | Khách cập nhật extension nhưng thư mục server cũ (hoặc ngược lại) | "Chép đè cả thư mục bản mới (gồm `server.mjs` và `local-server`) rồi tắt hẳn Claude, mở lại." Nếu đường dẫn MCP trỏ tới thư mục cũ → dùng `viral-studio-setup` để trỏ lại. |
| "Có bản mới" | Có cập nhật | "Bấm **Tải về** trên thanh thông báo, giải nén, chép đè nội dung thư mục `extension` vào thư mục extension đang dùng, rồi bấm Reload ở `chrome://extensions`." |
| Hàng đợi tạm dừng: hết lượt / đạt giới hạn | Tài khoản muse.ai hết lượt | "Hàng đợi sẽ chạy tiếp khi tài khoản có lượt lại (khoảng <giờ>)." Nếu khách có nhiều tài khoản: gợi ý đổi tài khoản (`vs_accounts`, `vs_account_switch`) — hỏi trước khi đổi. |
| "Phiên đăng nhập AI đã hết hạn" | muse.ai bị đăng xuất | "Mở tab muse.ai trong Chrome, đăng nhập lại, rồi nói tôi *chạy tiếp*." Sau đó `studio_control` `resume`. |
| Đoạn video lỗi lẻ tẻ | AI từ chối / lỗi tạm | Dùng skill `viral-studio-theo-doi` để tạo lại đoạn. |
| "Không chạy được ffmpeg" | Chưa cài FFmpeg | "Mở PowerShell, gõ `winget install Gyan.FFmpeg`, xong tắt và mở lại Claude." |
| Gửi được nhưng không thấy AI trả lời / không bấm được nút | muse.ai đổi giao diện | "Lỗi này cần người bán cập nhật Viral Studio. Bấm Dashboard → Cài đặt → Tải file chẩn đoán và gửi cho người bán." |

## Bước 3 — Kiểm tra lại

Sau khi khách báo đã làm, gọi lại tool liên quan để xác nhận đã ổn, rồi nói "✓ Đã chạy lại bình thường". Nếu vẫn lỗi sau 2 lần thử, đề nghị: "Bấm Dashboard → Cài đặt → Tải file chẩn đoán và gửi cho người bán kèm ảnh chụp màn hình."

## Không làm

- Không hỏi, không in license key, mật khẩu proxy, cookie. Không tự điền tài khoản proxy.
- Không xoá hàng đợi, hồ sơ hay tài khoản khi chưa hỏi.
- Không sửa code trong thư mục cài của khách.
