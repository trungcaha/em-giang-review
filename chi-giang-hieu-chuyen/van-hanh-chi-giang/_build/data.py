# -*- coding: utf-8 -*-
"""Nguồn dữ liệu chung cho file Excel vận hành và trang HTML của kênh Chị Giang Hiểu Chuyện.
Sửa ở đây rồi chạy lại build.py để cập nhật cả hai file."""
import re, datetime as dt
import openpyxl

ROOT = r"D:\video-ai-aff"
SRC_PRODUCTS = ROOT + r"\san-pham-kenh-chi-giang.xlsx"
SUB_PREFIX = "ChiGiang"   # tầng 1 của Sub_id trên link Shopee

PROJECT = {
    "name": "Kênh Chị Giang Hiểu Chuyện",
    "subtitle": "Hỏi đáp sinh lý – vợ chồng cho đàn ông 45+ · Affiliate Shopee · Facebook Reels",
    "goal": "8 video/ngày từ tuần 4 (≈240 video/tháng), mỗi video có link Shopee kèm Sub_id riêng",
    "start": dt.date(2026, 10, 19),
    "today": dt.date(2026, 10, 16),
    "north_star": "Hoa hồng Shopee affiliate mỗi tuần",
}

# ---------------------------------------------------------------- KÊNH (1 kênh)
CHANNEL = dict(
    code="CG", name="Chị Giang Hiểu Chuyện", page="Chị Giang Hiểu Chuyện",
    postiz_id="cmup0vxri0002qxtax0kkxduf", folder=ROOT + r"\viral-studio-downloads\videos\gioi-tinh",
    status="Đang chạy, đã có ~150 video hỏi đáp; chưa có script Postiz tự động cho page này",
    host="Chị Giang (ảnh chuẩn chi-giang-loat-2/nhan-vat-chi.png): áo scrubs xanh ngọc cổ V, tóc nâu đen dài, xưng “chị”. "
         "Vai phụ: “cô bạn lo lắng” (cùng gương mặt, kính đen tròn, áo hoa) hoặc người chồng.",
    format="Hỏi đáp “Chị ơi, cho em hỏi thầm…”: 70 giây · 7 shot · băng chữ đỏ ghi câu hỏi. "
           "Review sản phẩm: 50 giây · 5 shot · sản phẩm trong tay từ giây đầu.",
    tool="Viral Studio (studio_create, nguyên văn master prompt + ảnh nhân vật) → xuất MP4 9:16 → Postiz",
    audience=[("Giới tính", "Nam ~90%"),
              ("Tuổi", "45–54: 27,1% · 55–64: 25,3% · 65+: 20,3% · 35–44: 15,3% → 73% từ 45 tuổi"),
              ("Quốc gia", "Việt Nam 92% · Mỹ 6,2% (kiều bào, đang tăng)"),
              ("Thành phố", "TP.HCM 53,3% (tăng 5 điểm trong 3 ngày) · Hà Nội 8% · Quảng Nam 8% · Đà Nẵng 5,8% · Cà Mau 5,3%")],
    voice=["Chị xưng “chị”, gọi người xem là “mấy anh”, “anh”; người hỏi gọi “chị ơi”",
           "KHÔNG xưng hay được gọi là bác sĩ, dược sĩ, chuyên gia; không áo blouse, không ống nghe",
           "Giọng và từ ngữ miền Nam, nhịp chậm, chữ to; tránh tiếng lóng giới trẻ",
           "Nói kiểu chia sẻ kiến thức: không tục, không tả hành vi chi tiết, không hình gợi dục",
           "Sản phẩm: video hỏi đáp nhắc đúng 1 lần ở cuối; chỉ nói “hỗ trợ” + triệu chứng, không “chữa”, không “tăng sinh lý”"],
)

# ---------------------------------------------------------------- TRỤ CỘT NỘI DUNG (thay cho “kênh” của hệ Mẹ & Bé)
PILLARS = [
    dict(code="T1", name="Phong độ & tiết niệu", color="#2563eb",
         desc="Tiểu đêm, tiền liệt tuyến, ra ít, hết hứng tuổi 50, rượu thuốc, kẽm",
         examples=["Đêm dậy tiểu 3–4 lần là bị gì?", "Ngoài 50 ra ít, loãng là thiếu gì?", "Về hưu tự nhiên hết hứng, tại sao?"],
         products=[4, 1, 5, 3, 2]),
    dict(code="T2", name="Chuyện vợ chồng", color="#db2777",
         desc="Vợ mãn kinh, vợ khô, vợ né chồng, hiểu vợ, vệ sinh trước khi gần",
         examples=["Vợ mãn kinh né chồng có phải hết thương?", "Vợ nói “em mệt” là thật hay giả?", "Bao lâu không gần nhau là báo động?"],
         products=[6, 20, 23, 7, 8]),
    dict(code="T3", name="Bệnh nền & chuyện ấy", color="#ea580c",
         desc="Huyết áp, tiểu đường, mỡ máu, đau lưng, mất ngủ, chuột rút ảnh hưởng chuyện vợ chồng",
         examples=["Uống thuốc huyết áp có làm yếu chuyện ấy?", "Đau lưng thoát vị có nên gần vợ?", "Đêm chuột rút bắp chân là thiếu gì?"],
         products=[11, 19, 12, 13, 15, 14, 9, 10]),
    dict(code="T4", name="Phong độ bề ngoài", color="#16a34a",
         desc="Tóc bạc, vợ chê già, mùi – ngứa vùng kín, đồ lót, tài xế ngồi nhiều",
         examples=["Tóc bạc trắng, vợ chê già?", "Ngứa, mùi vùng kín đàn ông do đâu?", "Mặc quần lót chật ảnh hưởng gì?"],
         products=[18, 16, 17, 6]),
    dict(code="T5", name="Sống khỏe tuổi 50+", color="#7c3aed",
         desc="Mỏi lưng, cổ vai gáy, móng chân, quà cho vợ, quà Tết cho ba",
         examples=["Mỏi lưng mùa lạnh làm sao cho đỡ?", "Móng chân dày, quặp cắt sao khỏi đau?", "Quà Tết cho ba: đừng mua rượu"],
         products=[20, 19, 21, 22]),
]
PC = {p["code"]: p for p in PILLARS}
PILLAR_CODES = [p["code"] for p in PILLARS]

# ---------------------------------------------------------------- LỘ TRÌNH SẢN LƯỢNG (video/ngày theo trụ cột)
WEEKS = []
_ramp = {  # tuần: (T1,T2,T3,T4,T5, sự kiện)
    1: (2, 1, 1, 1, 0, "Chạy lại nhịp đăng bằng Postiz · 20/10 Ngày Phụ nữ VN: quà cho vợ"),
    2: (2, 1, 1, 1, 1, "Đo giữ chân 3 giây và click theo trụ cột"),
    3: (3, 1, 1, 1, 1, "Kịch bản sale 11.11"),
    4: (3, 2, 1, 1, 1, "11.11 (thứ Tư) · ĐỦ 8 video/ngày"),
    5: (3, 2, 1, 1, 1, "19/11 Ngày Quốc tế Nam giới · review tháng 1"),
    6: (3, 2, 1, 1, 1, "Black Friday 27/11: sản phẩm giá cao"),
    7: (3, 2, 1, 1, 1, "Trời lạnh: tiểu đêm, đau khớp tăng"),
    8: (3, 2, 1, 1, 1, "12.12 (thứ Bảy)"),
    9: (3, 2, 1, 1, 1, "Tất niên, nhậu nhiều: kẽm, bổ thận"),
    10: (3, 2, 1, 1, 1, "Noel 24–25/12"),
    11: (3, 2, 1, 1, 1, "Tết Dương lịch · lên kịch bản Tết"),
    12: (3, 2, 1, 1, 1, "Review quý · quà Tết cho ba, phủ bạc đón Tết"),
}
for w, r in _ramp.items():
    s = PROJECT["start"] + dt.timedelta(days=7 * (w - 1))
    row = dict(week=w, start=s, end=s + dt.timedelta(days=6), event=r[5])
    row.update({c: r[i] for i, c in enumerate(PILLAR_CODES)})
    row["total"] = sum(r[:5])
    WEEKS.append(row)
MAX_DAY = max(w["total"] for w in WEEKS)

PHASES = [
    dict(phase="Giai đoạn 0 – Dựng nền móng", time="16/10 – 18/10",
         goal="Link Shopee sạch kèm Sub_id, script Postiz cho page, khuôn prompt hỏi đáp gắn sản phẩm + review, đệm 2 ngày video",
         gate="Chạy thử trọn 1 video hỏi đáp gắn SP và 1 video review: Viral Studio → QC → Postiz → link ở bình luận gốc"),
    dict(phase="Giai đoạn 1 – Chạy lại nhịp đăng", time="19/10 – 01/11 (tuần 1–2)",
         goal="5–6 video/ngày đúng giờ. Đo giữ chân 3 giây, click link, đơn theo Sub_id từng video",
         gate="Page không bị cảnh báo hay hạn chế · QC đạt ≥ 90% · đăng đúng lịch ≥ 90%"),
    dict(phase="Giai đoạn 2 – Đủ 8 video/ngày", time="02/11 – 15/11 (tuần 3–4)",
         goal="Lên 7 rồi 8 video/ngày. Chạy chiến dịch 11.11",
         gate="Có đơn đầu tiên qua Sub_id · đệm video ≥ 2 ngày"),
    dict(phase="Giai đoạn 3 – Tối ưu", time="16/11 – 29/11 (tuần 5–6)",
         goal="Nhân bản top 3 video/tuần. Ngày Quốc tế Nam giới 19/11, Black Friday 27/11",
         gate="Biết trụ cột và sản phẩm nào ra đơn; cắt sản phẩm hạng C không đơn"),
    dict(phase="Giai đoạn 4 – Mùa cuối năm & Tết", time="30/11 – 10/01 (tuần 7–12)",
         goal="12.12, Noel, tất niên, chuẩn bị Tết 2027 (06/02): quà Tết cho ba, phủ bạc tóc",
         gate="Review quý: đủ số liệu thì cân nhắc mở kênh thứ hai cho cùng tệp (ví dụ page Ông Giang Sức Khỏe)"),
]

# ---------------------------------------------------------------- SẢN PHẨM (stt = STT trong file crawl Shopee)
G1, G2, G3, G4 = "1. Sinh lý & tiết niệu", "2. Bệnh nền", "3. Ngoại hình & tự tin", "4. Đời sống"
# Nguồn sự thật = sản phẩm trong link Shopee: tên, giá, hoa hồng lấy theo link. KaloData chỉ để xem nhu cầu.
# stt: (tên ngắn theo link Shopee, nhóm, trụ cột chính, trụ cột phụ, hạng (None = tự xếp theo HH/đơn), góc nội dung, ghi chú)
PRODUCT_META = {
    1: ("Kẽm DSD Multi Ginseng B+ Plus 150mg (60 viên)", G1, "T1", "", None, "Đàn ông nhậu nhiều, ra mồ hôi nhiều dễ hụt kẽm: hay mệt, rụng tóc, ra ít", ""),
    2: ("Viên Bổ Thận DSD Sâm Nhung", G1, "T1", "T5", None, "Đêm tiểu nhiều, sáng lưng mỏi nhừ, chiều về hết hứng", "Đợt đầu crawl nhầm “Sâm Nhung Bổ Thận New” 35k – đã crawl lại đúng hàng DSD"),
    3: ("Vương Bảo Thái Minh (tiền liệt tuyến)", G1, "T1", "", None, "Đêm dậy tiểu 3–4 lần, tiểu xong còn nhỏ giọt", ""),
    4: ("Viên Thận Botamax", G1, "T1", "", None, "Thận yếu có phải yếu sinh lý? – lưng mỏi, tiểu đêm", ""),
    5: ("Kẽm ADA 150mg", G1, "T1", "", None, "Kẽm uống lúc nào cho đúng, uống bao lâu mới thấy khác", ""),
    6: ("Bọt vệ sinh nam Oniiz (combo)", G1, "T4", "T2", None, "Ngứa, mùi, mồ hôi vùng kín; vệ sinh trước khi gần vợ", ""),
    7: ("Gel bôi trơn", G1, "T2", "", None, "Vợ tuổi mãn kinh khô rát, đừng nghĩ vợ hết thương", "Crawl 2 lần không sao chép được link affiliate – chưa dùng"),
    8: ("Bao cao su Durex Performa", G1, "T2", "", None, "Vợ chồng lớn tuổi có cần dùng bao không", "Giá trên link là phân loại nhỏ nhất – kiểm tra giá hộp 12 trước khi làm video"),
    9: ("Gel xoa bóp xương khớp Phục Thể An (Musecos)", G2, "T3", "T5", None, "Đau lưng, mỏi gối mùa lạnh – thoa tại chỗ", "Giá trên link là phân loại nhỏ nhất"),
    10: ("Linh Chi Thiên Ma Thấu Cốt Hoàn", G2, "T3", "", None, "Đau khớp gối khi trời trở lạnh", ""),
    11: ("Máy đo huyết áp Omron HEM-7180", G2, "T3", "T5", None, "Uống thuốc huyết áp có làm yếu chuyện ấy? – tự đo ở nhà; quà Tết cho ba", ""),
    12: ("Máy đo huyết áp AICARE X1 có giọng nói", G2, "T3", "T5", None, "Ba mẹ mắt kém tự đo, máy đọc to kết quả", "Rẻ hơn Omron nhưng hoa hồng 2,5%"),
    13: ("Viên dây thìa canh Diabetna (tiểu đường)", G2, "T3", "", None, "Tiểu đường và chuyện ấy", ""),
    14: ("Miếng dán chân Ông Lão Bắc Kinh", G2, "T3", "T5", None, "2 giờ sáng vẫn nằm đếm quạt trần", ""),
    15: ("Viên magie hữu cơ + B6", G2, "T3", "", None, "Đêm chuột rút bắp chân, ngủ không sâu", ""),
    16: ("Dầu gội phủ bạc Nezha 400ml", G3, "T4", "T5", None, "Tóc bạc trắng đầu, vợ chê già – gội 1 lần là đen", ""),
    17: ("Dầu gội phủ bạc thảo dược Kim Thảo (nâu coffee)", G3, "T4", "", None, "Ngại ra tiệm nhuộm: gội phủ bạc tại nhà, màu nâu tự nhiên", "Crawl tìm bút phủ bạc nhưng ra dầu gội Kim Thảo – vẫn hợp chủ đề"),
    18: ("Quần boxer nam thông hơi Natural Breath (combo 3)", G3, "T4", "", None, "Tài xế, ngồi nhiều: vùng kín nóng bí, quần chật", ""),
    19: ("Đai lưng tự nóng Kazumi", G4, "T3", "T5", None, "Đau lưng, thoát vị, mỏi lưng mùa lạnh", ""),
    20: ("Gối massage hồng ngoại Kingtech KP-315", G4, "T5", "T2", None, "Cổ vai gáy cứng đơ; quà cho ba, chồng tặng vợ", ""),
    21: ("Máy massage cầm tay mini", G4, "T5", "T2", None, "Chồng massage cho vợ – quà 20/10", ""),
    22: ("Kềm cắt móng Kềm Nghĩa M.401", G4, "T5", "", None, "Móng chân dày, quặp, cắt không nổi", ""),
    23: ("Trà mâm xôi sâm tố nữ A Nam", G4, "T2", "", None, "Vợ tiền mãn kinh hay cáu, bốc hỏa – chồng mua tặng vợ", ""),
}
TIER_A, TIER_B = 20000, 10000   # hoa hồng/đơn (đ) để tự xếp hạng khi chưa đặt tay


def _num(s):
    return int(re.sub(r"[^0-9]", "", str(s)) or 0)


def _pct(s):
    m = re.search(r"([0-9]+(?:[.,][0-9]+)?)", str(s))
    return round(float(m.group(1).replace(",", ".")) / 100, 4) if m else 0


def load_products():
    """Đọc file crawl Shopee (10 cột: STT, Nhóm, Tên yêu cầu, Tên Shopee, Giá, Hoa hồng, Link, Link Sub_id, Thư mục ảnh, Số ảnh).
    Bỏ qua dòng chưa có link."""
    wb = openpyxl.load_workbook(SRC_PRODUCTS, data_only=True)
    ws = wb.active
    out = []
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0] is None or not r[6]:
            continue
        stt = int(r[0])
        name, group, ch, ch2, tier, angle, note = PRODUCT_META.get(stt, (r[3], r[1], "", "", None, "", ""))
        price, hh = _num(r[4]), _pct(r[5])
        per = round(price * hh)
        if tier is None:
            tier = "A" if per >= TIER_A else "B" if per >= TIER_B else "C"
        link = str(r[6]).strip()
        code = link.rstrip("/").split("/")[-1]
        out.append(dict(stt=stt, group=group, name=name, shopee=r[3], price=price, hh=hh, per_order=per,
                        link=link, code=code, sublink=f"{link}?sub_id={SUB_PREFIX}-Chung-FBReels-SP{stt:02d}",
                        folder=r[8] or "", images=r[9] or 0, ch=ch, ch2=ch2, tier=tier, angle=angle, note=note))
    return out


# ---------------------------------------------------------------- KHO KỊCH BẢN (ý tưởng khởi đầu)
# (trụ cột, loại, tiêu đề / câu hỏi, hook 3 giây, bối cảnh gợi ý, mã SP)
IDEAS = [
    ("T1", "Hỏi đáp gắn SP", "Đêm dậy tiểu 3–4 lần là bị gì?", "Mấy anh ngoài năm mươi, đêm dậy mấy lần?", "Phòng ngủ đèn vàng, 2 giờ sáng", 3),
    ("T1", "Review sản phẩm", "Review Viên Thận Botamax: lưng mỏi, tiểu đêm", "Anh nào đêm dậy tiểu, sáng lưng mỏi nhừ, coi hết video này", "Bàn trà phòng khách", 4),
    ("T1", "Hỏi đáp gắn SP", "Tiểu xong còn nhỏ giọt có sao không?", "Kéo khóa rồi mà vẫn còn… anh có bị vậy không?", "Hành lang nhà, ánh sáng sáng sớm", 3),
    ("T1", "Hỏi đáp gắn SP", "Thận yếu có phải yếu sinh lý?", "Ai nói thận yếu là yếu chuyện ấy? Chị nói thiệt nè", "Quán cà phê cóc vỉa hè", 4),
    ("T1", "Review sản phẩm", "Review sâm nhung bổ thận", "Sáng dậy lưng mỏi nhừ, chiều về hết hứng?", "Phòng khách có tủ thờ", 2),
    ("T1", "Hỏi đáp gắn SP", "Ngoài 50 ra ít, loãng là thiếu gì?", "Lớn tuổi ra ít là bình thường hay thiếu chất?", "Ban công nhiều cây", 1),
    ("T1", "Review sản phẩm", "Review Kẽm DSD: đàn ông nhậu nhiều dễ thiếu kẽm", "Ngoài 40 hay mệt, rụng tóc, ăn không ngon?", "Bàn nhậu sau bữa tiệc", 1),
    ("T1", "Hỏi đáp gắn SP", "Về hưu tự nhiên hết hứng, tại sao?", "Nghỉ hưu rảnh rang mà sao chuyện ấy lại nguội?", "Sân nhà, ghế bố", 1),
    ("T1", "Hỏi đáp", "Sáng thức dậy không còn “chào cờ” có đáng lo?", "Mấy anh để ý buổi sáng chưa?", "Phòng ngủ buổi sáng, rèm mở", None),
    ("T1", "Hỏi đáp gắn SP", "Rượu thuốc ngâm có bổ thật không?", "Bình rượu ngâm trong nhà anh có gì trong đó?", "Góc tủ rượu", 2),
    ("T1", "Hỏi đáp", "Trứng vịt lộn, hàu có tăng bản lĩnh thật không?", "Ăn hột vịt lộn mỗi tối có được gì?", "Quán ốc vỉa hè Sài Gòn", None),
    ("T1", "Hỏi đáp gắn SP", "19/11 Quốc tế Nam giới: 3 việc đàn ông 50 nên làm", "Hôm nay ngày của mấy anh, chị hỏi thiệt", "Phòng khách trang trí nhẹ", 3),
    ("T1", "Tình huống vợ chồng", "Vợ hỏi: sao dạo này anh dậy đêm hoài?", "Anh đi đâu mà đêm nào cũng dậy vậy?", "Phòng ngủ, vợ ngồi dậy bật đèn", 3),
    ("T1", "Hỏi đáp gắn SP", "Kẽm uống lúc nào cho đúng?", "Uống kẽm lúc đói là sai rồi nha", "Bếp buổi sáng", 5),
    ("T1", "Hỏi đáp", "Ngoài 50 bao lâu gần vợ một lần là vừa?", "Câu này mấy anh hỏi chị nhiều nhất", "Ghế đá công viên", None),
    ("T2", "Hỏi đáp gắn SP", "Vợ mãn kinh né chồng, đừng vội nghĩ hết thương", "Vợ né anh có phải vì hết thương?", "Phòng khách buổi tối", 23),
    ("T2", "Hỏi đáp", "Vợ khô có phải hết thương?", "Câu này nhiều anh hiểu sai lắm", "Phòng ngủ đèn ngủ", None),
    ("T2", "Tình huống vợ chồng", "20/10 tặng vợ tuổi 50 cái gì cho vợ vui?", "Hai mươi tháng mười rồi, anh mua gì cho vợ chưa?", "Chợ hoa, cầm bó hoa", 23),
    ("T2", "Hỏi đáp", "Vợ nói “em mệt” là thật hay giả?", "Vợ nói em mệt, anh hiểu sao?", "Bếp tối, vợ rửa chén", None),
    ("T2", "Hỏi đáp gắn SP", "Vợ chồng lớn tuổi có cần dùng bao?", "Vợ mãn kinh rồi thì khỏi cần, đúng không?", "Phòng khách", 8),
    ("T2", "Hỏi đáp", "Bao lâu không gần nhau là báo động?", "Một tháng, ba tháng hay một năm?", "Quán cà phê sân vườn", None),
    ("T2", "Hỏi đáp gắn SP", "Vệ sinh trước khi gần vợ – điều vợ ngại nói", "Có một chuyện vợ anh không dám nói", "Phòng tắm sạch sẽ, khăn treo", 6),
    ("T2", "Tình huống vợ chồng", "Chồng massage cho vợ, vợ cảm động", "Ba chục năm mới thấy ổng làm vậy", "Phòng khách, sofa", 21),
    ("T2", "Hỏi đáp", "Vì sao vợ đòi tắt đèn?", "Vợ đòi tắt đèn là vì ngại hay vì giận?", "Phòng ngủ", None),
    ("T2", "Hỏi đáp", "Vợ thích được khen điều gì nhất?", "Khen vợ đẹp là chưa đủ đâu mấy anh", "Bữa cơm gia đình", None),
    ("T3", "Hỏi đáp gắn SP", "Uống thuốc huyết áp có làm yếu chuyện ấy?", "Uống thuốc huyết áp xong anh thấy khác không?", "Bàn làm việc có hộp thuốc", 11),
    ("T3", "Review sản phẩm", "Review máy đo huyết áp Omron: tự đo ở nhà", "Đo huyết áp ở nhà mà số nhảy lung tung?", "Phòng khách nhà ba mẹ", 11),
    ("T3", "Hỏi đáp gắn SP", "Tiểu đường và chuyện ấy", "Đường huyết cao thì chuyện ấy ra sao?", "Bếp, bữa sáng", 13),
    ("T3", "Hỏi đáp gắn SP", "Đau lưng thoát vị có nên gần vợ?", "Lưng đau mà vợ rủ, làm sao đây?", "Phòng ngủ, gối tựa lưng", 19),
    ("T3", "Review sản phẩm", "Review đai lưng tự nóng Kazumi: đau lưng mùa lạnh", "Trời trở lạnh, lưng nhức hả mấy anh?", "Ghế bố ngoài hiên", 19),
    ("T3", "Hỏi đáp gắn SP", "Đêm chuột rút bắp chân là thiếu gì?", "Đang ngủ bị vọp bẻ, anh làm gì đầu tiên?", "Phòng ngủ ban đêm", 15),
    ("T3", "Hỏi đáp gắn SP", "Ngủ không sâu thì bản lĩnh cũng xuống", "Hai giờ sáng vẫn nằm đếm quạt trần?", "Phòng ngủ quạt trần", 14),
    ("T3", "Hỏi đáp gắn SP", "Mỡ máu cao ảnh hưởng chuyện ấy ra sao?", "Bụng to, mỡ máu cao, chuyện ấy có sao không?", "Quán bún bò buổi sáng", 11),
    ("T3", "Hỏi đáp gắn SP", "Đau khớp gối mùa lạnh", "Gối kêu lục cục mỗi lần đứng dậy?", "Cầu thang nhà", 10),
    ("T3", "Hỏi đáp", "Sau đặt stent gần vợ được không?", "Mới đặt stent, bao lâu mới được gần vợ?", "Phòng khách", None),
    ("T3", "Hỏi đáp", "Gút và chuyện ấy", "Gút sưng chân, chuyện ấy có bị gì không?", "Bàn nhậu hải sản", None),
    ("T4", "Review sản phẩm", "Review dầu gội phủ bạc Nezha: gội một lần tóc đen", "Tóc bạc trắng đầu, gội một lần là đen?", "Phòng tắm, chú Tư làm mẫu", 16),
    ("T4", "Hỏi đáp gắn SP", "Tóc bạc sớm, vợ chê già", "Vợ nói anh nhìn già hơn tuổi?", "Tiệm hớt tóc", 16),
    ("T4", "Hỏi đáp gắn SP", "Ngại ra tiệm nhuộm: gội phủ bạc tại nhà", "Ra tiệm nhuộm mất cả buổi, ở nhà gội mười lăm phút?", "Trước gương phòng tắm", 17),
    ("T4", "Hỏi đáp gắn SP", "Ngứa, mùi vùng kín đàn ông do đâu?", "Ngứa mà không dám gãi trước mặt ai?", "Phòng tắm", 6),
    ("T4", "Review sản phẩm", "Review bọt vệ sinh nam Oniiz", "Đàn ông cũng cần dung dịch vệ sinh riêng?", "Phòng tắm", 6),
    ("T4", "Hỏi đáp gắn SP", "Mặc quần lót chật ảnh hưởng gì?", "Quần lót mấy năm chưa thay, anh có không?", "Phòng ngủ, tủ đồ", 18),
    ("T4", "Hỏi đáp gắn SP", "Tài xế ngồi nhiều: vùng kín nóng bí", "Chạy xe cả ngày, chỗ đó nóng như lò?", "Cabin xe tải / xe ôm công nghệ", 18),
    ("T4", "Review sản phẩm", "Review quần boxer thông hơi: tài xế, ngồi nhiều", "Quần lót mặc cả ngày mà không bí, có không?", "Cabin xe, tủ đồ", 18),
    ("T4", "Hỏi đáp", "Bụng bia và chuyện ấy", "Bụng to che mất tầm nhìn rồi mấy anh", "Quán nhậu", None),
    ("T5", "Review sản phẩm", "Review gối massage hồng ngoại: cổ vai gáy", "Cổ vai gáy cứng đơ, mười lăm phút là nhẹ người?", "Sofa phòng khách", 20),
    ("T5", "Hỏi đáp gắn SP", "Mỏi cổ vai gáy vì coi điện thoại nhiều", "Coi điện thoại cả ngày, cổ cứng đơ?", "Ghế bố, điện thoại", 20),
    ("T5", "Tình huống vợ chồng", "Quà cho ba dịp cuối năm: gối massage hồng ngoại", "Ba nói không cần gì, nhưng ba cần cái này", "Phòng khách, con trai tặng quà", 20),
    ("T5", "Hỏi đáp gắn SP", "Móng chân dày, quặp: cắt sao cho khỏi đau?", "Móng chân dày như vỏ ốc, cắt không nổi?", "Hiên nhà, ghế đẩu", 22),
    ("T5", "Tình huống vợ chồng", "Quà Tết cho ba: đừng mua rượu", "Tết này mua gì cho ba ngoài rượu?", "Phòng khách ngày Tết", 11),
    ("T5", "Hỏi đáp", "Đàn ông 50 nên đi bộ bao nhiêu mỗi ngày?", "Mười ngàn bước hay ba ngàn bước?", "Công viên sáng sớm", None),
    ("T5", "Từ bình luận", "Hỏi đáp từ bình luận tuần này (Chủ nhật)", "Tuần này mấy anh hỏi chị nhiều nhất câu này", "Quán cà phê, cầm điện thoại đọc bình luận", None),
]
STATUSES = ["Ý tưởng", "Đang viết", "Chờ duyệt", "Cần sửa", "Đã duyệt", "Đang sản xuất", "QC", "Sẵn sàng đăng", "Đã đăng", "Hủy"]
VIDEO_TYPES = ["Hỏi đáp", "Hỏi đáp gắn SP", "Review sản phẩm", "Tình huống vợ chồng", "Từ bình luận"]

# ---------------------------------------------------------------- NHÂN SỰ (kênh đơn – đội nhỏ, kiêm nhiệm)
ROLES = [
    dict(code="R1", role="Điều phối kiêm trưởng nội dung", count="1", cap=None,
         duty="Chọn chủ đề tuần, duyệt prompt trong 4 giờ, giữ giọng Chị Giang và luật xưng hô, bảng từ cấm, quyết định nhân bản hay cắt sản phẩm",
         output="Duyệt 8–12 prompt/ngày; 56 ý tưởng/tuần vào KHO_KICH_BAN",
         kpi="Hoa hồng/tuần · giữ chân 3 giây ≥ 30% · prompt đạt ngay lần đầu ≥ 80%",
         tools="File vận hành này, báo cáo Shopee affiliate, FB Insights", report="—"),
    dict(code="R2", role="Biên kịch – master prompt", count="=ROUNDUP(B4/B5,0)", cap="kb",
         duty="Viết master prompt theo khuôn “Chị ơi, cho em hỏi thầm” (70s/7 shot) hoặc review (50s/5 shot), trước ngày đăng 2 ngày; sản phẩm nhắc đúng 1 lần",
         output="15 prompt/người/ngày",
         kpi="Prompt đạt duyệt/ngày · tỷ lệ phải sửa", tools="Skill master-prompt, chi-giang-loat-2/_tao-prompt-*.py, chi-giang-review-san-pham", report="R1"),
    dict(code="R3", role="Sản xuất video (Viral Studio)", count="=ROUNDUP(B4/B6,0)", cap="dung",
         duty="Xếp hàng studio_create (nguyên văn master prompt + ảnh nhân vật), soát mặt nhân vật từng shot, tạo lại shot lỗi, xuất MP4 9:16, đặt tên đúng quy tắc",
         output="10 video đạt QC/người/ngày",
         kpi="Video đạt QC/ngày · tỷ lệ phải làm lại ≤ 10%", tools="Skill viral-studio-tao-video, viral-studio-theo-doi", report="R1"),
    dict(code="R4", role="Đăng bài, cộng đồng & dữ liệu", count="=ROUNDUP(B4/B7,0)", cap="qc",
         duty="QC 10 điểm, lên lịch Postiz 8 khung giờ, link kèm Sub_id ở bình luận gốc, trực bình luận/inbox, kiểm tra link thứ Hai, nhập số liệu ngày",
         output="8 bài/ngày đúng giờ, đúng link; số liệu trước 10:00",
         kpi="Đúng lịch 100% · 0 bài sai link · phản hồi bình luận trong 12 giờ", tools="Postiz (mlabai.uk), Shopee affiliate, Meta Business Suite, PostForge", report="R1"),
]
CAPACITY = dict(target=MAX_DAY, kb=15, dung=10, qc=40)

SOP = [
    ("1", "Lên kho ý tưởng tuần", "Chủ nhật", "R1", "R4", "Bình luận hay, báo cáo đơn theo Sub_id, top video, KaloData", "56 ý tưởng trong KHO_KICH_BAN (trạng thái “Ý tưởng”), đủ 5 trụ cột"),
    ("2", "Viết master prompt", "Trước ngày đăng 2 ngày", "R2", "R1", "Ý tưởng + khuôn hỏi đáp hoặc review + ảnh nhân vật", "File prompt .md, trạng thái “Chờ duyệt”"),
    ("3", "Duyệt prompt", "Trong 4 giờ", "R1", "R2", "Prompt chờ duyệt + bảng từ cấm", "“Đã duyệt” hoặc “Cần sửa” kèm góp ý"),
    ("4", "Xếp hàng Viral Studio", "Trước ngày đăng 1 ngày", "R3", "R1", "Prompt đã duyệt, nhan-vat-chi.png", "studio_create; trạng thái “Đang sản xuất”"),
    ("5", "Soát shot & xuất video", "Trong ngày", "R3", "R4", "Video Viral Studio", "Làm lại shot lỗi; MP4 1080×1920, trạng thái “QC”"),
    ("6", "Kiểm tra chất lượng (QC)", "Trong ngày sản xuất", "R4", "R1", "Video + checklist 10 điểm", "Đạt → “Sẵn sàng đăng”; lỗi → trả R3"),
    ("7", "Lên lịch đăng", "Trước 17:00 ngày trước", "R4", "R1", "Video sẵn sàng + link kèm Sub_id (cột I của KHO_KICH_BAN)", "Postiz: Reel + link ở bình luận gốc, trạng thái “Đã đăng”"),
    ("8", "Trực bình luận, inbox", "10:00 và 21:00", "R4", "R1", "Bài đã đăng", "Ghim link, trả lời, ẩn bình luận tục, gom câu hỏi"),
    ("9", "Nhập số liệu", "Mỗi ngày trước 10:00", "R4", "R1", "Shopee affiliate (lọc theo Sub_id) + FB Insights", "THEO_DOI_NGAY và cột View/Click/Đơn của KHO_KICH_BAN"),
    ("10", "Review tuần", "Chủ nhật 19:00", "R1", "Cả team", "TONG_QUAN, top 3 video, đơn theo Sub_id", "5 biến thể cho mỗi top video; danh sách cắt/nhân sản phẩm"),
]
QC_CHECK = [
    "Hook 3 giây: câu hỏi nóng, băng chữ đỏ ghi đúng câu hỏi",
    "Gương mặt Chị Giang đúng ảnh chuẩn, đồng nhất mọi shot; trang phục đúng",
    "Không xưng hay được gọi bác sĩ, dược sĩ, chuyên gia; không áo blouse, ống nghe",
    "Không tục, không tả hành vi chi tiết, không hình gợi dục (kể cả ảnh bìa)",
    "Không cam kết y tế: không “chữa”, “trị dứt”, “tăng sinh lý”; thực phẩm chức năng có câu “không phải là thuốc”",
    "Sản phẩm nhắc đúng 1 lần (video hỏi đáp), đúng sản phẩm của link sẽ gắn",
    "Giọng miền Nam, gọi “anh”, “mấy anh”; nhịp chậm, rõ",
    "Tiếng rõ, khớp miệng, không đứt giữa các shot; chữ không sai chính tả",
    "Đúng 1080×1920, đúng thời lượng (70s hỏi đáp, 50s review), không đen hình đầu/cuối",
    "Bối cảnh khác video hôm trước (không lặp khuôn); tên file đúng quy tắc",
]
DAILY_RHYTHM = [
    ("08:30", "Họp nhanh 10 phút", "Cả team", "Hôm qua xong gì, hôm nay làm gì, vướng gì"),
    ("09:00 – 11:00", "Viết lô prompt T+2 · xếp hàng Viral Studio lô T+1", "R2, R3", ""),
    ("10:00", "Nhập số liệu hôm qua · trực bình luận lần 1", "R4", ""),
    ("11:00 – 11:30", "Duyệt prompt đợt 1", "R1", ""),
    ("13:30 – 16:00", "Soát shot, xuất video · QC", "R3, R4", ""),
    ("16:00", "Duyệt prompt đợt 2", "R1", ""),
    ("17:00", "Chốt lịch đăng ngày mai trên Postiz", "R4", "Đủ 8 bài, link kèm Sub_id"),
    ("21:00", "Trực bình luận lần 2", "R4", "Giờ tệp nam 45+ lướt nhiều"),
]
RITUALS = [
    ("Hằng ngày", "Họp nhanh 08:30", "R1"),
    ("Chủ nhật", "Review tuần: top 3 video → 5 biến thể; cắt sản phẩm 20 video không đơn", "R1"),
    ("Thứ Hai", "Kiểm tra toàn bộ link Shopee, giá, hoa hồng (đổi theo chiến dịch)", "R4"),
    ("Thứ Sáu", "Lọc NGUON_CONTENT: nguồn “Mới” → chọn 10 ý tưởng sang KHO_KICH_BAN", "R1"),
    ("Ngày 1 hằng tháng", "Review tháng: trụ cột, sản phẩm; tìm sản phẩm mới bằng KaloData + crawl Shopee", "R1"),
    ("Trước mỗi đợt sale", "Kịch bản sale riêng: 11.11, 19/11, Black Friday, 12.12, Tết", "R1"),
]
RACI_ROLES = ["R1", "R2", "R3", "R4"]
RACI = {
    "1": dict(R1="A", R2="C", R4="C"),
    "2": dict(R1="A", R2="R"),
    "3": dict(R1="R", R2="I"),
    "4": dict(R1="I", R3="R"),
    "5": dict(R1="A", R3="R", R4="I"),
    "6": dict(R1="A", R3="I", R4="R"),
    "7": dict(R1="I", R4="R"),
    "8": dict(R1="I", R4="R"),
    "9": dict(R1="I", R4="R"),
    "10": dict(R1="A", R2="C", R3="C", R4="R"),
}

SLOTS = [
    ("05:45", "Hỏi đáp (không sản phẩm)", "Kéo view giờ cà phê sáng", "Không"),
    ("07:30", "Review sản phẩm – hạng A", "Ra đơn", "Có (1 sản phẩm)"),
    ("11:30", "Hỏi đáp gắn SP – T3 bệnh nền", "Ra đơn giờ nghỉ trưa", "Có (nhắc 1 lần)"),
    ("13:00", "Tình huống vợ chồng", "Bình luận, chia sẻ", "Tùy tập"),
    ("17:30", "Hỏi đáp gắn SP – T1 phong độ", "Ra đơn giờ tan làm", "Có (nhắc 1 lần)"),
    ("20:00", "Review sản phẩm – hạng A khác buổi sáng", "Ra đơn giờ vàng", "Có (1 sản phẩm)"),
    ("21:30", "Hỏi đáp gắn SP – T2 chuyện vợ chồng", "Giờ vàng chủ đề nhạy cảm", "Có (nhắc 1 lần)"),
    ("22:45", "Hỏi đáp (không sản phẩm)", "Giữ lượt tiếp cận cuối ngày", "Không"),
]
WEEKDAY_THEMES = [
    ("Thứ 2", "Sai lầm đàn ông hay mắc", "Quán cà phê cóc vỉa hè", "Kẽm DSD / Kẽm ADA"),
    ("Thứ 3", "Hiểu vợ (T2)", "Phòng khách buổi tối", "Gối massage (chồng tặng vợ) / Oniiz"),
    ("Thứ 4", "Bệnh nền & chuyện ấy (T3)", "Bàn làm việc, hộp thuốc", "Máy đo Omron / đai lưng tự nóng"),
    ("Thứ 5", "Tiểu đêm, thận, tiền liệt tuyến (T1)", "Phòng ngủ đèn vàng", "Botamax / Vương Bảo"),
    ("Thứ 6", "Phong độ bề ngoài (T4)", "Tiệm hớt tóc, phòng tắm", "Quần boxer thông hơi / phủ bạc Nezha"),
    ("Thứ 7", "Tình huống vợ chồng cuối tuần", "Bữa cơm gia đình, quán nhậu", "Combo 2 sản phẩm"),
    ("Chủ nhật", "Hỏi đáp từ bình luận", "Quán cà phê sân vườn", "Sản phẩm bán tốt nhất tuần"),
]
SEASON = [
    ("20/10", "Ngày Phụ nữ Việt Nam", "“Tặng vợ tuổi 50 cái gì”: gối massage hồng ngoại, trà sâm tố nữ"),
    ("Tháng 10–12", "Trời trở lạnh", "Tiểu đêm tăng, đau khớp: Botamax, đai lưng tự nóng, gối massage"),
    ("10–11/11", "Sale 11.11", "3 ngày trước sale: tăng review lên 3/8 video; máy đo Omron, gối massage (giá cao)"),
    ("19/11", "Ngày Quốc tế Nam giới", "Tuần sức khỏe đàn ông: Botamax, kẽm, tiền liệt tuyến, tầm soát"),
    ("27/11", "Black Friday", "Sản phẩm giá cao: máy đo Omron, gối massage hồng ngoại, combo quần boxer"),
    ("12/12", "Sale 12.12 (thứ Bảy)", "Như 11.11; thêm combo quà cho ba"),
    ("Cuối năm", "Tất niên, nhậu nhiều", "“Rượu bia và chuyện ấy”: kẽm, Botamax"),
    ("24–25/12", "Noel", "Tình huống vợ chồng: quà cuối năm cho nhau"),
    ("Tháng 1/2027", "Chuẩn bị Tết 2027 (Tết 06/02)", "Quà Tết cho ba (máy đo Omron, gối massage), phủ bạc Nezha đón Tết"),
]
KPI_RULES = [
    ("Giữ chân 3 giây", "Từng video", "< 30%", "Viết lại câu hỏi mở đầu, đổi băng chữ đỏ"),
    ("Click link / lượt xem", "Từng sản phẩm", "< 0,3%", "Đổi góc kể, đổi khung giờ, đổi câu dẫn link ở bình luận"),
    ("Đơn / sản phẩm / tuần (theo Sub_id)", "Báo cáo Shopee", "Top 3", "Tăng gấp đôi số video cho sản phẩm đó"),
    ("Đơn / trụ cột / 3 tuần", "Từng trụ cột", "0 đơn sau ~40 video", "Đổi sản phẩm của trụ cột, giữ trụ cột nếu view tốt"),
    ("Sản phẩm hạng C", "Từng sản phẩm", "20 video không đơn", "Bỏ khỏi kế hoạch"),
    ("Đăng đúng lịch", "Từng ngày", "< 90%", "R1 kiểm tra nút thắt: prompt hay Viral Studio"),
    ("QC đạt", "Toàn team", "< 90%", "Siết checklist, sửa khuôn prompt"),
    ("Cảnh báo/hạn chế từ Facebook", "Page", "Bất kỳ", "Dừng tăng sản lượng, rà lời thoại và ảnh bìa 7 ngày gần nhất"),
]
RISKS = [
    ("Facebook gắn cờ nội dung tình dục, hạn chế page", "Cao", "Giọng chia sẻ kiến thức; bảng từ cấm; không hình gợi dục kể cả ảnh bìa; QC điểm 4. Đây là page duy nhất – mất page là mất hết", "R1"),
    ("Quảng cáo thực phẩm chức năng sai luật (“tăng sinh lý”, “chữa”)", "Cao", "Chỉ nói “hỗ trợ” + triệu chứng; câu “không phải là thuốc”; QC điểm 5", "R4"),
    ("Nhân vật bị hiểu là bác sĩ thật", "Cao", "Luật xưng hô trong mọi prompt; không blouse, ống nghe; QC điểm 3", "R1"),
    ("Hoa hồng Shopee của thực phẩm chức năng thấp (2,5–7,5%)", "Trung bình", "Xếp hạng theo hoa hồng/đơn trên Shopee, không theo TikTok; ưu tiên sản phẩm đơn cao (máy đo, massage); kiểm tra lại mỗi thứ Hai", "R4"),
    ("Nhóm hàng nhạy cảm bị chặn link", "Trung bình", "Gel bôi trơn: crawl 2 lần không lấy được link nên chưa dùng; bao cao su Durex lấy được (13,5%). Thử lấy link gel bằng tay trên app (việc T03); không được thì chỉ làm video kiến thức", "R4"),
    ("Viral Studio hết lượt, phiên đăng nhập hết hạn, hàng đợi đứng", "Trung bình", "Đệm video 2 ngày; skill viral-studio-sua-loi; theo dõi bằng viral-studio-theo-doi", "R3"),
    ("Gương mặt nhân vật lệch giữa các video", "Trung bình", "Luôn đính kèm nhan-vat-chi.png; prompt bắt tạo ẢNH NHÂN VẬT CHUẨN trước; QC điểm 2", "R3"),
    ("Link affiliate hết hạn hoặc sản phẩm hết hàng", "Trung bình", "Kiểm tra link thứ Hai; có sản phẩm thay thế cùng nhóm", "R4"),
    ("Bình luận tục, spam, tranh cãi", "Trung bình", "Ẩn bình luận theo từ khóa; trực 2 lần/ngày", "R4"),
    ("Postiz giới hạn ~30 request/giờ", "Thấp", "8 bài × 2 request/ngày, script tự chờ", "R4"),
    ("Đăng dày làm giảm reach", "Thấp", "Tăng sản lượng theo lộ trình, có điều kiện qua cửa", "R1"),
]
RESOURCES = [
    ("Kho master prompt Chị Giang (prompt 17–235)", ROOT + r"\chi-giang-loat-2", "Mẫu giọng văn, khuôn hỏi đáp 70s, script _tao-prompt-*.py"),
    ("Ảnh nhân vật chuẩn", ROOT + r"\chi-giang-loat-2\nhan-vat-chi.png", "Đính kèm mọi lần chạy Viral Studio"),
    ("6 kịch bản review sản phẩm", ROOT + r"\chi-giang-review-san-pham\kich-ban-6-video.md", "Khuôn review 50s"),
    ("Danh sách sản phẩm + link Shopee + ảnh", SRC_PRODUCTS, "Nguồn của sheet SAN_PHAM (crawl bằng PostForge)"),
    ("Ảnh sản phẩm", ROOT + r"\shopee-aff-crawler\storage\images", "Mỗi sản phẩm 1 thư mục"),
    ("Số liệu KaloData 30 ngày (TikTok)", ROOT + r"\research\chi-giang-sp\kalodata-tu-khoa-30ngay.txt", "Chỉ tham khảo nhu cầu – giá, hoa hồng dùng theo Shopee"),
    ("Thư mục video của kênh", CHANNEL["folder"], "Video xuất xong lưu ở đây"),
    ("Mẫu script đăng Postiz", ROOT + r"\viral-studio-downloads\postiz-giot-lanh.py", "Nhân bản thành postiz-gioi-tinh.py"),
    ("Postiz", "https://mlabai.uk", "Page Chị Giang: " + CHANNEL["postiz_id"]),
    ("PostForge (crawl Shopee)", "http://127.0.0.1:8765", "Lấy link s.shopee.vn, ảnh, hoa hồng"),
    ("Skill viết prompt", "master-prompt", "Gọi trong Claude Code"),
    ("Skill tạo và theo dõi video", "viral-studio-tao-video, viral-studio-theo-doi", "Gọi trong Claude Code"),
    ("Skill dữ liệu TikTok Shop", "kalodata", "Tìm sản phẩm mới"),
    ("Skill crawl Shopee", "postforge-shopee-crawler", "Tìm link affiliate + ảnh"),
]

TASKS = [
    ("T01", "Chốt người làm R1–R4, điền tên vào NHAN_SU", "R1", dt.date(2026, 10, 16), "Giai đoạn 0"),
    ("T02", "Kiểm tra 22 link Shopee: còn hàng, đúng giá và hoa hồng; đổi “Trạng thái link” sang OK", "R4", dt.date(2026, 10, 17), "Giai đoạn 0"),
    ("T03", "Thử lấy link gel bôi trơn bằng tay trên app Shopee (crawler không sao chép được); kiểm tra giá hộp 12 của bao cao su Durex", "R4", dt.date(2026, 10, 17), "Giai đoạn 0"),
    ("T04", "Viết khuôn master prompt “hỏi đáp gắn SP” (nhắc sản phẩm 1 lần cuối video) và khuôn review 50s", "R1", dt.date(2026, 10, 17), "Giai đoạn 0"),
    ("T05", "Bảng từ cấm + câu bắt buộc cho thực phẩm chức năng", "R1", dt.date(2026, 10, 17), "Giai đoạn 0"),
    ("T06", "Tạo script postiz-gioi-tinh.py: 8 khung giờ, link kèm Sub_id ở bình luận gốc", "R4", dt.date(2026, 10, 18), "Giai đoạn 0"),
    ("T07", "Đệm 2 ngày: 12 video (lô 20/10 có video quà cho vợ)", "R3", dt.date(2026, 10, 18), "Giai đoạn 0"),
    ("T08", "Lấy số liệu nền 30 ngày của page: view TB/video, click, đơn → thay giả định ở DU_BAO", "R4", dt.date(2026, 10, 18), "Giai đoạn 0"),
    ("T09", "Chạy thử trọn 1 video hỏi đáp gắn SP + 1 review → qua cửa giai đoạn 0", "R1", dt.date(2026, 10, 18), "Giai đoạn 0"),
    ("T10", "Đăng video 20/10 “tặng vợ tuổi 50 cái gì”", "R4", dt.date(2026, 10, 20), "Giai đoạn 1"),
    ("T11", "Kịch bản 11.11 (review giá cao, combo)", "R1", dt.date(2026, 11, 5), "Giai đoạn 2"),
    ("T12", "Kịch bản tuần 19/11 Ngày Quốc tế Nam giới", "R1", dt.date(2026, 11, 14), "Giai đoạn 3"),
    ("T13", "Review tháng 1: chọn top sản phẩm theo Sub_id, cắt sản phẩm C yếu", "R1", dt.date(2026, 11, 16), "Giai đoạn 3"),
    ("T14", "Kịch bản Black Friday 27/11", "R1", dt.date(2026, 11, 22), "Giai đoạn 3"),
    ("T15", "Kịch bản 12.12 + Noel + tất niên", "R1", dt.date(2026, 12, 3), "Giai đoạn 4"),
    ("T16", "Kế hoạch nội dung Tết 2027: quà Tết cho ba, phủ bạc tóc", "R1", dt.date(2026, 12, 20), "Giai đoạn 4"),
    ("T17", "Review quý: quyết định mở kênh thứ hai cho cùng tệp nam 45+", "R1", dt.date(2027, 1, 10), "Giai đoạn 4"),
]

# Giả định dự báo (thay bằng số thực của page sau 2 tuần – việc T08)
FORECAST = dict(views=5000, ctr=0.005, cr=0.03, cost=8000000)

# ---------------------------------------------------------------- NGUỒN CONTENT
import json as _json, os as _os
SOURCES_FILE = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "nguon-content.json")
try:
    SOURCES = _json.load(open(SOURCES_FILE, encoding="utf-8"))
except FileNotFoundError:
    SOURCES = []
SOURCE_TYPES = ["Video viral", "Kênh tham khảo", "Hook hay", "Ý tưởng", "Sản phẩm bán chạy", "Đối thủ"]
SOURCE_STATUSES = ["Mới", "Đã phân tích", "Đã thành kịch bản", "Bỏ qua"]
