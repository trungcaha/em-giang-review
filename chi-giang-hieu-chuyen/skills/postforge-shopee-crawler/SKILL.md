---
name: postforge-shopee-crawler
description: Use when the user asks to crawl Shopee Affiliate products, control PostForge (http://127.0.0.1:8765/), extract s.shopee.vn shortlinks, download product images, attach Sub_id tracking, export product lists to Excel, or deploy the product catalog to Vercel (https://postforge-shopee-aff.vercel.app).
---

# PostForge Shopee Affiliate Crawler & Excel/Vercel Pipeline

Tự động điều khiển **PostForge Studio (`http://127.0.0.1:8765/`)** kết nối với điện thoại Android thật qua ADB (ưu tiên cáp USB như `Samsung S24 Ultra` hoặc `MaxCloudPhone`) để tìm sản phẩm trên App Shopee, lấy **Tên sản phẩm**, **Giá**, **Hoa hồng (`%`)**, **Link rút gọn chính thức (`https://s.shopee.vn/XXXX`)**, tải **bộ ảnh HD sản phẩm** về thư mục riêng trên PC, gắn **Sub_id**, xuất **file Excel** và đồng bộ lên **Vercel Cloud (`https://postforge-shopee-aff.vercel.app`)**.

---

## Khi nào kích hoạt Skill này (Triggers)

Kích hoạt ngay khi người dùng yêu cầu:
- "Crawl sản phẩm Shopee", "tìm các sản phẩm này trên Shopee", "điều khiển PostForge", "lấy link affiliate Shopee".
- Đưa một danh sách sản phẩm hoặc file `.md` / `.xlsx` (ví dụ: Kalodata, Content Plan kênh Mẹ & Bé, Tinh Trùng & Trứng, Gia dụng, Làm đẹp...) và yêu cầu tìm link Shopee Affiliate + tải ảnh + xuất Excel.
- Yêu cầu gắn `Sub_id` vào link `s.shopee.vn`, mở thư mục ảnh trên PC, hoặc đẩy/cập nhật kho sản phẩm lên Vercel.

---

## Quy tắc Cốt lõi (Bắt buộc tuân thủ)

1. **TUYỆT ĐỐI KHÔNG chạy `emulator.exe`** (BlueStacks/LDPlayer) khi chưa được người dùng yêu cầu rõ ràng. Hệ thống ưu tiên kết nối điện thoại Android vật lý đang cắm cáp USB (`adb devices -l`, ví dụ `R5CWC2TMHWL` — `SM_S928B`) hoặc `MaxCloudPhone` WebSocket Bridge.
2. **Mỗi sản phẩm lưu ảnh vào 1 thư mục riêng theo mã shortlink**:
   - Đường dẫn chuẩn: `D:\video-ai-aff\shopee-aff-crawler\storage\images\<mã_shortlink_s.shopee.vn>\` (ví dụ: `D:\video-ai-aff\shopee-aff-crawler\storage\images\50Zs81PNEq\img_01.jpg`).
3. **Luôn lọc tab "Bán chạy" trên Shopee**:
   - Khi tìm từ khóa trên App Shopee, luôn bấm tab **Bán chạy** (`x=460, y=278`) để lấy đúng sản phẩm top lượt bán có hoa hồng tiếp thị liên kết.

---

## Cấu trúc Thư mục & File Hệ thống

- **Thư mục gốc PostForge**: `D:\video-ai-aff\shopee-aff-crawler`
- **Backend Server (`port 8765`)**: `D:\video-ai-aff\shopee-aff-crawler\server.py`
- **ADB Crawler Engine**: `D:\video-ai-aff\shopee-aff-crawler\adb_crawler.py`
- **Cơ sở dữ liệu SQLite**: `D:\video-ai-aff\shopee-aff-crawler\storage\products.db` (`D:\video-ai-aff\shopee-aff-crawler\database.py`)
- **Kho ảnh sản phẩm trên PC**: `D:\video-ai-aff\shopee-aff-crawler\storage\images\<item_id>\`
- **Giao diện Web**: `D:\video-ai-aff\shopee-aff-crawler\static\index.html`
- **Script đóng gói & đẩy Vercel**: `D:\video-ai-aff\shopee-aff-crawler\build_and_deploy_vercel.py`
- **Script mẫu crawl danh sách lớn & xuất Excel**:
  - `D:\video-ai-aff\shopee-aff-crawler\crawl_tinh_trung_va_trung.py`
  - `D:\video-ai-aff\shopee-aff-crawler\crawl_missing_content_plan.py`
  - `D:\video-ai-aff\shopee-aff-crawler\crawl_kalodata_lam_dep.py`

---

## Quy trình Thực thi Chuẩn (Step-by-Step)

### Bước 1: Kiểm tra kết nối ADB & PostForge Server (`http://127.0.0.1:8765/`)

1. Kiểm tra xem `http://127.0.0.1:8765/api/status` đã chạy chưa:
   ```powershell
   Invoke-RestMethod -Uri "http://127.0.0.1:8765/api/status"
   ```
2. Nếu server chưa chạy, khởi động `server.py` dưới dạng Daemon trong `D:\video-ai-aff\shopee-aff-crawler`:
   ```powershell
   python server.py
   ```
3. Đảm bảo `adb_connected: True` (điện thoại đang cắm USB và bật USB Debugging). Nếu màn hình điện thoại đang tắt, `adb_crawler.py` sẽ tự động gửi `input keyevent KEYCODE_WAKEUP` và `wm dismiss-keyguard`.

### Bước 2: Gọi API Crawl theo từng sản phẩm hoặc chạy Script Batch

- **Cách 1 — Crawl 1 từ khóa qua API**:
  ```powershell
  Invoke-RestMethod -Uri "http://127.0.0.1:8765/api/crawl" -Method Post -ContentType "application/json; charset=utf-8" -Body '{"keyword": "Kem đánh răng Marvis", "max_items": 1, "must_contain": "Marvis"}'
  ```
  Sau đó theo dõi tiến độ qua `GET http://127.0.0.1:8765/api/status` cho đến khi `crawler_running == false`.

- **Cách 2 — Crawl danh sách nhiều sản phẩm & xuất file Excel**:
  Sử dụng script `C:\Users\PC\.gemini\config\skills\postforge-shopee-crawler\scripts\crawl_batch_to_excel.py` (hoặc dựa theo mẫu `D:\video-ai-aff\shopee-aff-crawler\crawl_tinh_trung_va_trung.py`):
  - Với mỗi sản phẩm trong danh sách:
    1. Gọi `POST /api/crawl` với `keyword` + `must_contain` (`max_items: 1`).
    2. Nếu lượt đầu không khớp `must_contain`, tự động fallback gọi lại với `must_contain: ""` và `fallback_keyword` ngắn gọn hơn để đảm bảo 100% sản phẩm đều lấy được link và ảnh.
    3. Lưu ngay tiến độ vào file Excel sau mỗi sản phẩm để không mất dữ liệu.

### Bước 3: Quy tắc Gắn `Sub_id` vào Link Affiliate (`s.shopee.vn`)

Mọi link rút gọn `https://s.shopee.vn/XXXX` đều gắn được tối đa 5 tầng `Sub_id` bằng tham số `?sub_id=`:
```text
https://s.shopee.vn/<mã_link>?sub_id=<Sub1>-<Sub2>-<Sub3>-<Sub4>-<Sub5>
```
- Chỉ dùng chữ cái và số không dấu (`A-Z`, `a-z`, `0-9`, `_`), phân tách các tầng bằng dấu gạch ngang `-`.
- Ví dụ theo hệ thống 5 kênh:
  - Kênh 1 (Chuẩn bị mang thai): `TinhTrungTrung-Tap01-FBReels-<MaSP>`
  - Kênh 2 (Mang bầu): `MeBauThongThai-Tap01-FBReels-<MaSP>`
  - Kênh 3 (Sau sinh): `MeBimSua24h-Tap01-FBReels-<MaSP>`
  - Kênh 4 (Em bé 0–3 tuổi): `BeKhoeMeVui-Tap01-FBReels-<MaSP>`
  - Kênh 5 (Gia đình / Chung): `GiaDinhNho-Tap01-FBReels-<MaSP>`

### Bước 4: Định dạng File Excel Xuất ra (`openpyxl`)

Khi xuất file Excel cho người dùng, luôn bao gồm đầy đủ 10 cột chuẩn:
1. `STT`
2. `Nhóm sản phẩm`
3. `Tên sản phẩm yêu cầu`
4. `Tên sản phẩm Shopee`
5. `Giá` (ví dụ: `215.000đ`)
6. `Hoa hồng` (ví dụ: `HH 10%`)
7. `Link Shopee Affiliate` (ví dụ: `https://s.shopee.vn/8fObefjH03`)
8. `Link Affiliate kèm Sub_id (Theo Kênh)` (ví dụ: `https://s.shopee.vn/8fObefjH03?sub_id=TinhTrungTrung-Tap01-FBReels-8fObefjH03`)
9. `Đường dẫn Folder Ảnh` (ví dụ: `D:\video-ai-aff\shopee-aff-crawler\storage\images\8fObefjH03`)
10. `Số ảnh` (ví dụ: `6`)

### Bước 5: Đồng bộ lên Vercel Production (`https://postforge-shopee-aff.vercel.app`)

Sau khi crawl xong đợt sản phẩm mới hoặc khi người dùng yêu cầu đẩy lên web online:
```powershell
python build_and_deploy_vercel.py
npx vercel --prod --yes --cwd vercel-app
```
Lệnh này sẽ đóng gói toàn bộ cơ sở dữ liệu sản phẩm (`products.json`, `runs.json`, `status.json`) cùng toàn bộ thư mục ảnh `storage/images/*` lên địa chỉ cố định `https://postforge-shopee-aff.vercel.app`.
