# HANDOFF — Kênh "Chị Giang Hiểu Chuyện"

Repo này chứa đủ để sang máy khác vận hành kênh Facebook **Chị Giang Hiểu Chuyện** (hỏi đáp sinh lý – vợ chồng cho đàn ông 45+, affiliate Shopee) **đúng style cũ, không cần dặn lại**. Claude ở máy mới: đọc hết file này + `memory/` trước khi làm.

## 1. Cài đặt trên máy mới (Windows)

```bash
git clone https://github.com/trungcaha888-art/video-ai-chi-giang-hieu-chuyen.git D:/video-ai-chi-giang-hieu-chuyen
```

1. **Skills** → copy các thư mục trong `skills/` vào `C:\Users\<user>\.claude\skills\`:
   - `master-prompt` — viết master prompt cho Viral Studio (muse.ai)
   - `viral-studio-tao-video`, `viral-studio-theo-doi`, `viral-studio-sua-loi` — xếp hàng, theo dõi, sửa lỗi Viral Studio (`studio_create`…)
   - `kalodata` — số liệu TikTok Shop (cần `PYTHONUTF8=1`; key KaloData KHÔNG có trong repo, đặt ở `~/.config/kalodata/config.toml`)
   - `postforge-shopee-crawler` — crawl link Shopee affiliate qua điện thoại ADB (bản gốc ở `C:\Users\<user>\.gemini\config\skills\`)
2. **Thư mục làm việc**: file vận hành và skill trỏ `D:\video-ai-aff\…`. Copy `van-hanh-chi-giang/` và `san-pham-kenh-chi-giang.xlsx` vào `D:\video-ai-aff\`; `kich-ban-prompt/chi-giang-loat-2` → `D:\video-ai-aff\chi-giang-loat-2`; `kich-ban-prompt/review-san-pham` → `D:\video-ai-aff\chi-giang-review-san-pham`; `anh-san-pham/<mã>` → `D:\video-ai-aff\shopee-aff-crawler\storage\images\<mã>`.
3. **Memory** → copy `memory/*.md` vào `C:\Users\<user>\.claude\projects\D--video-ai-aff\memory\` và thêm dòng vào `MEMORY.md` (hoặc bảo Claude: "đọc HANDOFF.md và memory/ rồi nạp vào memory").
4. **Không có trong repo**: key Postiz (biến môi trường User `POSTIZ_API_KEY`, Postiz ở https://mlabai.uk), key KaloData, đăng nhập muse.ai/Viral Studio, code PostForge (`shopee-aff-crawler/`), video thành phẩm đầy đủ (1,1 GB ở `viral-studio-downloads/videos/gioi-tinh/`).
5. Phần mềm: Python 3 (openpyxl, httpx), Viral Studio + extension Chrome (skill `viral-studio-setup`), Android SDK platform-tools (adb) cho PostForge, Excel (kiểm công thức).

## 2. Nội dung repo

| Thư mục | Nội dung |
|---|---|
| `van-hanh-chi-giang/` | **Masterplan**: `van-hanh-kenh-chi-giang.xlsx` (16 sheet, số liệu sống) + `du-an-chi-giang.html` (11 tab). Sinh từ `_build/data.py`: `python build.py` chỉ làm mới HTML; `python build.py excel` tạo lại Excel = **xóa số liệu đã nhập** |
| `san-pham-kenh-chi-giang.xlsx` | 22 link Shopee affiliate (tên, giá, hoa hồng theo link, link kèm Sub_id, thư mục ảnh) |
| `anh-san-pham/<mã link>/` | Ảnh sản phẩm của 22 link |
| `kich-ban-prompt/chi-giang-loat-2/` | ~220 master prompt "Chị ơi, cho em hỏi thầm" (prompt-17 … 235), script sinh prompt `_tao-prompt-*.py`, file `create-*.json` cho `studio_create`, **ảnh nhân vật chuẩn `nhan-vat-chi.png`** |
| `kich-ban-prompt/review-san-pham/` | 6 kịch bản + prompt review sản phẩm 50s (sâm nhung DSD, Nezha, kẽm DSD, miếng dán chân, xương khớp, Vương Bảo) kèm video hoàn chỉnh |
| `video-mau/` | 3 video hỏi đáp thành phẩm làm mẫu |
| `nghien-cuu/` | KaloData 30 ngày theo từ khóa, danh sách crawl, script `gop-va-kiem-tra.py` (gộp crawl + bỏ link trùng), báo cáo video |
| `postiz/` | Mẫu script đăng Postiz (của page Căn Bếp Nhỏ) để nhân bản thành `postiz-gioi-tinh.py` |
| `skills/`, `memory/` | Như mục 1 – **memory là luật bắt buộc** |

## 3. Style bắt buộc (đừng hỏi lại người dùng)

- **Khán giả**: nam ~90%, 73% từ 45 tuổi, VN 92% (Mỹ 6%), TP.HCM 53% → giọng miền Nam, gọi "anh", "mấy anh", nhịp chậm, không tiếng lóng.
- **Nhân vật**: Chị Giang theo `nhan-vat-chi.png` (scrubs xanh ngọc cổ V, tóc nâu đen dài). Xưng "chị". **KHÔNG xưng/được gọi bác sĩ, dược sĩ, chuyên gia**; không blouse, không ống nghe. Vai phụ: "cô bạn lo lắng" (cùng mặt, kính đen tròn, áo hoa).
- **Định dạng**: hỏi đáp 70s/7 shot, băng chữ đỏ ghi câu hỏi; review 50s/5 shot, sản phẩm trong tay từ giây đầu.
- **Nội dung nhạy cảm**: chia sẻ kiến thức, không tục, không tả hành vi, không hình gợi dục (kể cả ảnh bìa). Thực phẩm chức năng chỉ nói "hỗ trợ" + triệu chứng, có câu "không phải là thuốc"; cấm "chữa", "tăng sinh lý".
- **Viral Studio**: dùng `studio_create`, đưa **nguyên văn** master prompt làm script, không tách, không chat; không sửa file `muse-master-prompt.md`.
- **Affiliate nhẹ nhàng**: video hỏi đáp nhắc sản phẩm đúng 1 lần ở cuối; link ở bình luận gốc.
- **Kịch bản trước, video sau**: đưa người dùng duyệt rồi mới chạy. Mỗi video đổi bối cảnh, không lặp khuôn.

## 4. Sản phẩm & link (Shopee là tham chiếu duy nhất)

- Hoa hồng Shopee khác TikTok. Hạng A (≥20k/đơn): Viên Thận Botamax (17,5%), quần boxer thông hơi (17%), máy đo Omron, Viên Bổ Thận DSD Sâm Nhung (17,5%), gối massage Kingtech, đai lưng Kazumi. Vương Bảo, Phục Thể An chỉ 2,5%.
- **Mỗi video một Sub_id**: cột I của KHO_KICH_BAN tự tạo `…?sub_id=ChiGiang-<ID video>-FBReels-SP<mã>` → báo cáo Shopee biết video nào ra đơn.
- PostForge có lỗi: khi không bấm được "Sao chép", nó đọc clipboard cũ → **link trùng sản phẩm trước** và ghi đè ảnh. Link trùng = sai (Shopee tạo link mới mỗi lần chia sẻ). Gel bôi trơn chưa lấy được link. Giá crawl có thể là phân loại rẻ nhất.

## 5. Quy trình một video (chi tiết ở sheet QUY_TRINH)

1. Chọn ý tưởng ở KHO_KICH_BAN (52 ý tưởng nạp sẵn, 5 trụ cột T1–T5).
2. Viết master prompt theo khuôn trong `chi-giang-loat-2/` hoặc `review-san-pham/` → người dùng duyệt.
3. `studio_create` với nguyên văn prompt + `nhan-vat-chi.png` → soát mặt từng shot, làm lại shot lỗi → MP4 9:16.
4. QC 10 điểm → lưu `viral-studio-downloads/videos/gioi-tinh/CG-<YYYYMMDD>-<giờ>-<ID>-<slug>.mp4`.
5. Postiz: page "Chị Giang Hiểu Chuyện" id `cmup0vxri0002qxtax0kkxduf`, Reel + link Sub_id ở bình luận gốc.
6. Nhập số liệu THEO_DOI_NGAY trước 10:00; review Chủ nhật theo đơn từng Sub_id.

Việc còn mở (sheet CONG_VIEC): T03 lấy link gel bằng tay, T06 viết `postiz-gioi-tinh.py`, T08 lấy số liệu nền của page để thay giả định ở DU_BAO.
