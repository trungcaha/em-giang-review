---
name: postiz-folder-page-map
description: Folder video (viral-studio-downloads/videos/) → page FB Postiz tương ứng
metadata:
  node_type: memory
  type: project
  originSessionId: 4ec916bc-efec-44dc-8b66-539b8751256e
  modified: 2026-10-14T08:38:19.378Z
---

Folder ở D:/video-ai-aff/viral-studio-downloads/videos/ đăng lên page (Postiz, xem [[postiz-setup]]):
- suc-khoe-thay-giang → "Ông Giang Sức Khỏe" cmuo8lcts0001r07pcmzv0cv2
- giot-lanh → "Căn Bếp Nhỏ" cmtrkr9c10001r07vahsxtm3g
- gioi-tinh → "Chị Giang Hiểu Chuyện" cmup0vxri0002qxtax0kkxduf
- trong-cay → "Chuyện Hoa Quả" cmuu20kuk0044nx1swiynfof1 — script viral-studio-downloads/postiz-trong-cay.py (1 bài/giờ, caption lấy Câu 1–5 từ master-prompts/meo-lam-vuon/<slug>.md). Viral Studio cứ lưu thêm video vào folder → chạy lại script, nó nối tiếp sau slot cuối.

Bash env POSTIZ_API_KEY cũ (401) → lấy key từ User env: powershell [Environment]::GetEnvironmentVariable('POSTIZ_API_KEY','User').

Script đăng giot-lanh: viral-studio-downloads/postiz-giot-lanh.py (3h/bài, nhớ đã đăng trong videos/giot-lanh/_posted.json, log postiz-giot-lanh.log). Postiz mlabai.uk throttle ~30 request/giờ (429) → script tự chờ; mỗi bài tốn 2 request (upload + create).
