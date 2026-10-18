---
name: van-hanh-chi-giang-project
description: "Masterplan vận hành 1 kênh Chị Giang Hiểu Chuyện (5 trụ cột) – Excel + HTML ở van-hanh-chi-giang/, sinh từ _build/"
metadata:
  node_type: memory
  type: project
  originSessionId: ebee44ce-633c-435d-a3cf-5b99270b9a31
  modified: 2026-10-16T08:17:57.618Z
---

Lập 16/10/2026, tuần 1 bắt đầu 19/10/2026, 8 video/ngày từ tuần 4. Người dùng chọn **chỉ 1 kênh** (không mở hệ nhiều kênh như Mẹ & Bé), trục chia việc là 5 trụ cột T1–T5 (phong độ & tiết niệu, chuyện vợ chồng, bệnh nền, bề ngoài, sống khỏe 50+).

- File: `D:\video-ai-aff\van-hanh-chi-giang\van-hanh-kenh-chi-giang.xlsx` (16 sheet) + `du-an-chi-giang.html`. Sinh từ `_build/data.py`; `python build.py` chỉ làm mới HTML, `python build.py excel` tạo lại Excel = XÓA số liệu đã nhập (giống [[van-hanh-me-be-project]]).
- Sản phẩm: `D:\video-ai-aff\san-pham-kenh-chi-giang.xlsx` crawl bằng PostForge ([[postforge-crawler]]); link Shopee là tham chiếu duy nhất. Mỗi video có link riêng `?sub_id=ChiGiang-<IDvideo bỏ gạch>-FBReels-SP<mã>` (cột I KHO_KICH_BAN) để báo cáo Shopee chỉ ra video nào ra đơn.
- Hoa hồng Shopee khác hẳn TikTok: hạng A = Botamax 17,5%, boxer thông hơi 17%, Omron, sâm nhung DSD 17,5%, gối massage Kingtech, đai lưng Kazumi; Vương Bảo, Phục Thể An chỉ 2,5%; gel bôi trơn không lấy được link.

**Why:** người dùng affiliate qua Shopee, giao việc cho nhân viên theo file này.
**How to apply:** sửa kế hoạch → sửa data.py → build HTML; chỉ build Excel khi người dùng đồng ý. Liên quan [[chi-giang-audience]].
