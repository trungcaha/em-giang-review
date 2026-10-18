# -*- coding: utf-8 -*-
"""Sinh thong-tin-san-pham.md + prompt-<slug>.md cho 6 video review (kênh Chị Giang Hiểu Chuyện)
và file tổng kich-ban-6-video.md. Chạy: python _tao-prompt.py"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

CHI = ("Phụ nữ châu Á khoảng 30 tuổi, mặt trái xoan, da sáng hồng, mắt nâu, lông mày nâu đậm tự nhiên, "
       "môi hồng đất, tóc nâu đen dài quá vai")

V = []

# ------------------------------------------------------------------ 1
V.append(dict(
    slug="01-bo-than-dsd-sam-nhung", ten="Sâm Nhung Bổ Thận DSD",
    tieu_de="Đêm tiểu 3–4 lần, sáng lưng mỏi nhừ",
    hook_card=("ĐÊM TIỂU 3–4 LẦN", "SÁNG LƯNG MỎI NHỪ?"),
    van_de="Nam 45+ tiểu đêm nhiều lần, ngủ không tròn giấc, đau lưng mỏi gối, xuống sức, ngại nói.",
    giai_phap="Viên Sâm Nhung Bổ Thận DSD (nhung hươu, nhân sâm, đông trùng, bột hàu, ba kích, nhục thung dung).",
    ket_qua="Dùng đều: nhiều người mua phản hồi bớt tiểu đêm, lưng gối đỡ mỏi (không hứa chữa khỏi).",
    trang_phuc="áo len mỏng cổ tròn màu kem, dây chuyền vàng mảnh, tóc buộc đuôi thấp gọn sau gáy, bông tai nụ bạc nhỏ",
    boi_canh="phòng khách nhà phố buổi tối: sofa vải nâu đất, gối tựa màu be, đèn cây ánh vàng ấm bên trái, "
             "kệ tivi gỗ mờ phía sau, rèm cửa màu kem, bàn trà gỗ thấp trước mặt có ly thủy tinh nước ấm",
    am_thanh="phòng yên tĩnh, tiếng quạt máy rất nhẹ",
    san_pham="lọ nhựa nâu sẫm gần đen cao khoảng 9 cm, NẮP TRẮNG tròn; nhãn ĐỎ ĐÔ có logo \"DSD\" trong hình elip đỏ viền bạc, "
             "chữ vàng kim \"SÂM NHUNG BỔ THẬN\", dòng nhỏ \"CORDYCEP OYSTER MAX GOLD\", hình con hươu sừng lớn và củ nhân sâm vàng, "
             "vòng tròn \"60 VIÊN\". Kèm HỘP GIẤY vuông ĐỎ ĐÔ cùng thiết kế (chữ vàng kim, hươu, nhân sâm). Viên nang bên trong màu nâu",
    nhan_dang="lọ nâu nắp trắng nhãn đỏ đô chữ vàng \"SÂM NHUNG BỔ THẬN\", logo DSD",
    hook_luat="khung hình đầu tiên CHỊ đã ngồi trên sofa, tay phải giơ LỌ Sâm Nhung Bổ Thận DSD ngang má, nhãn hướng ống kính, "
              "tay trái giơ BA ngón tay; nói ngay câu đầu, không chào hỏi",
    shots=[
        dict(act="0–5s: CHỊ ngồi sofa, tay phải giơ lọ ngang má (nhãn hướng máy), tay trái giơ ba rồi bốn ngón, mắt mở to, nhướn mày: "
                 "\"Đêm dậy tiểu ba bốn lần, sáng ra lưng mỏi nhừ? Anh nào bị, ở lại với Giang.\" "
                 "5–10s: hạ tay trái, nghiêng đầu, giọng nhỏ lại tâm tình: \"Qua bốn lăm tuổi gặp nhiều lắm, mà mấy anh hay ngại nói.\"",
             lines=["Đêm dậy tiểu ba bốn lần, sáng ra lưng mỏi nhừ? Anh nào bị, ở lại với Giang.",
                    "Qua bốn lăm tuổi gặp nhiều lắm, mà mấy anh hay ngại nói."],
             end="chị đặt lọ xuống bàn trà, nhãn vẫn hướng máy"),
        dict(act="Lọ đứng trên bàn trà góc dưới phải. CHỊ đưa tay ra sau thắt lưng làm điệu bộ đau lưng, rồi xòe hai tay, lắc đầu nhẹ, cười cảm thông: "
                 "\"Ngủ không tròn giấc, sáng dậy đuối, đau lưng mỏi gối, vô chuyện vợ chồng cũng hết hứng. Vợ hỏi thì nói: anh mệt.\"",
             lines=["Ngủ không tròn giấc, sáng dậy đuối, đau lưng mỏi gối, vô chuyện vợ chồng cũng hết hứng. Vợ hỏi thì nói: anh mệt."],
             end="chị cầm lại lọ bằng tay phải, tay trái cầm hộp giấy đỏ đô"),
        dict(act="CHỊ đặt HỘP đỏ đô lên bàn (mặt chữ hướng máy), đưa LỌ ra gần ống kính rồi xoay nhẹ cho thấy nhãn, ngón tay chỉ vào hình hươu và nhân sâm: "
                 "\"Hôm nay Giang review lọ Sâm Nhung Bổ Thận DSD. Trong có nhung hươu, nhân sâm, đông trùng, bột hàu, ba kích, nhục thung dung.\"",
             lines=["Hôm nay Giang review lọ Sâm Nhung Bổ Thận DSD. Trong có nhung hươu, nhân sâm, đông trùng, bột hàu, ba kích, nhục thung dung."],
             end="chị vặn mở nắp trắng của lọ"),
        dict(act="CHỊ nghiêng lọ đổ HAI viên nang nâu ra lòng bàn tay trái, chìa tay về ống kính 2 giây, tay phải cầm ly nước ấm giơ lên: "
                 "\"Uống một đến hai viên, sau ăn ba mươi phút, với nước ấm. Dùng đều, nhiều anh phản hồi bớt tiểu đêm, lưng gối đỡ mỏi.\"",
             lines=["Uống một đến hai viên, sau ăn ba mươi phút, với nước ấm. Dùng đều, nhiều anh phản hồi bớt tiểu đêm, lưng gối đỡ mỏi."],
             end="chị đặt ly xuống, cầm lọ đã đậy nắp"),
        dict(act="CHỊ ôm lọ trước ngực, nhãn hướng máy, hộp đỏ đô nằm góc dưới khung; giơ ngón trỏ dặn dò, cuối câu cười tươi chỉ tay xuống dưới: "
                 "\"Đây là thực phẩm bảo vệ sức khỏe, không phải thuốc. Tiểu buốt, tiểu ra máu thì đi khám nha. Anh nào cần, Giang để ở phần bình luận.\"",
             lines=["Đây là thực phẩm bảo vệ sức khỏe, không phải thuốc. Tiểu buốt, tiểu ra máu thì đi khám nha. Anh nào cần, Giang để ở phần bình luận."],
             end="chị cười, lọ và hộp rõ nhãn trong khung"),
    ],
    info=dict(
        ten_day_du="TPBVSK Viên Bổ Thận DSD Sâm Nhung Bổ Thận – Hộp 1 lọ x 60 viên", pid="1734924639764579412",
        gia="niêm yết ~357.000đ · giá trung bình thực bán ~270.000đ/đơn", ban="15.418 đơn / 90 ngày (doanh thu ~4,17 tỷ) · đang tăng",
        hh="10%", danh_gia="796 đánh giá", ngay="mở bán 01/04/2026",
        cong_dung=["Hỗ trợ bổ huyết, bổ thận, dưỡng thận.", "Hỗ trợ cải thiện tóc bạc sớm, tiểu đêm, tiểu nhiều lần.",
                   "Giúp cải thiện đau lưng, mỏi gối, tay chân tê bì."],
        thanh_phan="Bột nhung hươu, nhân sâm, đông trùng hạ thảo, bột hàu, ba kích, nhục thung dung.",
        cach_dung="Người lớn 1–2 viên/lần, ngày 1–2 lần (sáng/chiều), sau ăn 30 phút, uống với nước ấm. Khuyến khích dùng liên tục 3 tháng.",
        luu_y="Không phải là thuốc. Không dùng cho người mẫn cảm với thành phần. Đang dùng thuốc khác thì hỏi bác sĩ/dược sĩ.",
        review="Đa số khen chất lượng, đóng gói, giao nhanh; một số người thấy khỏe hơn sau thời gian ngắn. Có người chưa đánh giá được vì mới dùng; có 1 phản ánh nhận hộp rỗng.",
        bao_bi="Lọ nâu sẫm nắp trắng + hộp giấy đỏ đô, chữ vàng kim \"SÂM NHUNG BỔ THẬN\", logo DSD, hình hươu và nhân sâm, \"60 VIÊN\"."),
))

# ------------------------------------------------------------------ 2
V.append(dict(
    slug="02-dau-goi-phu-bac-nezha", ten="Dầu gội phủ bạc Nezha",
    tieu_de="Tóc bạc trắng đầu, gội một lần là đen?",
    hook_card=("TÓC BẠC TRẮNG ĐẦU", "GỘI 1 LẦN LÀ ĐEN?"),
    van_de="Nam 45+ tóc bạc nhiều, bị gọi già, ngại ra tiệm nhuộm, sợ pha thuốc lỉnh kỉnh.",
    giai_phap="Dầu gội phủ bạc Nezha 3 trong 1 (gội – nhuộm – dưỡng), tự làm ở nhà như gội đầu.",
    ket_qua="Tóc bạc lên màu đen tự nhiên ngay sau một lần gội (quay thật quá trình: tóc bạc → bọt nâu → xả → đen).",
    trang_phuc="áo thun polo màu vàng mù tạt, tóc búi cao gọn bằng kẹp càng cua màu nâu, bông tai nụ bạc nhỏ, hai tay mang găng nilon ĐEN",
    boi_canh="sân sau nhà miền Tây buổi sáng nắng nhẹ: nền gạch tàu đỏ, ghế nhựa đỏ có tựa, thau nhôm và ca nhựa xanh, vòi nước gắn tường, "
             "giàn bông giấy hồng phía sau, sào phơi đồ mờ, một chiếc gương tay viền nhựa xanh để trên ghế đẩu gỗ",
    am_thanh="tiếng chim, tiếng nước chảy, tiếng gà xa xa",
    san_pham="CHAI nhựa ĐỎ TƯƠI bóng 400ml dáng thuôn, nắp bật màu đỏ; nhãn VÀNG KIM in logo \"NEZHA\" chữ xanh dương nghiêng trong hình elip, "
             "chữ đỏ đậm \"DẦU GỘI PHỦ BẠC\", băng tím \"PLANT HAIR DYE\", hình cô gái tóc nâu xoăn dài ở nửa dưới nhãn. Kèm HỘP GIẤY vàng kim cùng thiết kế. "
             "Khi bóp ra là dung dịch sánh màu nâu sẫm, xoa lên tóc tạo bọt nâu đậm",
    nhan_dang="chai đỏ tươi nhãn vàng kim chữ \"DẦU GỘI PHỦ BẠC\", logo NEZHA",
    extra_char="- CHÚ TƯ: nam Việt Nam 58 tuổi, mặt chữ điền rám nắng, nếp nhăn đuôi mắt, lông mày rậm điểm bạc, tóc ngắn; áo thun ba lỗ trắng, "
               "khăn bông màu xám choàng kín vai. Luôn ngồi trên ghế nhựa đỏ ở giữa khung, mặt hướng ống kính; CHỊ đứng ngay sau lưng chú, hơi lệch phải. Không đổi trang phục.",
    bien_doi="- DIỄN BIẾN MÁI TÓC CHÚ TƯ (bắt buộc, từ từ, không biến đổi đột ngột): tóc KHÔ bạc trắng khoảng 70%, xơ nhẹ → dung dịch nâu sẫm phủ từng mảng, "
             "vẫn lộ tóc bạc → BỌT NÂU ĐẬM phủ kín cả đầu, không còn thấy sợi bạc → đang xả, tóc ƯỚT bết, màu đen nâu, nước chảy xuống hơi nâu → "
             "tóc lau khô, ĐEN TỰ NHIÊN đều màu, hơi bóng, không đen kịt giả. Trạng thái tóc ở khung cuối mỗi shot phải đúng trạng thái đó ở khung đầu shot sau.",
    hook_luat="khung hình đầu tiên CHỊ (đã mang găng đen) đang bóp CHAI ĐỎ Nezha cho dung dịch nâu sẫm chảy lên mái tóc BẠC TRẮNG của CHÚ TƯ đang ngồi; "
              "không có cảnh đi tới, không chào hỏi",
    giong_them=" Chú Tư: nam miền Tây gần 60 tuổi, giọng trầm khàn, mộc mạc, chậm.",
    shots=[
        dict(act="0–5s: CHỊ đứng sau CHÚ TƯ, tay phải bóp chai đỏ (nhãn vàng hướng máy) cho dung dịch nâu sẫm chảy lên đỉnh đầu tóc bạc, tay trái xoa nhẹ, mắt nhìn ống kính, cười: "
                 "\"Tóc bạc trắng đầu, đi đâu cũng bị kêu bằng ông? Coi Giang gội cho chú Tư nè.\" "
                 "5–10s: CHÚ TƯ ngước mắt lên, nghi ngờ: \"Gội mà đen được hả con?\" Chị cười, tiếp tục xoa. Tóc: bạc khô → dung dịch nâu phủ từng mảng.",
             lines=["Tóc bạc trắng đầu, đi đâu cũng bị kêu bằng ông? Coi Giang gội cho chú Tư nè.", "CHÚ TƯ: Gội mà đen được hả con?"],
             end="chị đặt chai lên ghế đẩu, nhãn hướng máy; đầu chú phủ dung dịch nâu từng mảng, còn lộ tóc bạc hai bên"),
        dict(act="CHỊ dùng mười đầu ngón tay mang găng đen xoa đều khắp đầu chú như gội đầu, bọt nâu đậm nổi dần; vừa xoa vừa nhìn máy nói: "
                 "\"Dầu gội phủ bạc Nezha, ba trong một: gội, nhuộm, dưỡng. Khỏi pha, khỏi ra tiệm. Thoa lên tóc khô, mang bao tay, xoa đều như gội đầu.\" "
                 "Tóc: dung dịch từng mảng → bọt nâu phủ gần kín.",
             lines=["Dầu gội phủ bạc Nezha, ba trong một: gội, nhuộm, dưỡng. Khỏi pha, khỏi ra tiệm. Thoa lên tóc khô, mang bao tay, xoa đều như gội đầu."],
             end="bọt nâu đậm phủ kín cả đầu chú, không còn thấy sợi bạc; chị dừng tay"),
        dict(act="Đầu CHÚ TƯ phủ kín bọt nâu đậm, chú ngồi yên nhắm mắt thư giãn. CHỊ đưa hai tay găng dính bọt nâu lên cho máy thấy, rồi chỉ một ngón ra sau vành tai mình: "
                 "\"Xoa xong thì ủ theo hướng dẫn trên hộp. Nhớ thử trước một ít sau tai, không ngứa, không đỏ mới xài nha.\" Tóc: giữ nguyên bọt nâu kín đầu.",
             lines=["Xoa xong thì ủ theo hướng dẫn trên hộp. Nhớ thử trước một ít sau tai, không ngứa, không đỏ mới xài nha."],
             end="chị cầm ca nhựa xanh múc nước trong thau, giơ lên trên đầu chú"),
        dict(act="CHÚ TƯ cúi nhẹ đầu, CHỊ dội ca nước từ từ lên tóc, tay kia vuốt bọt trôi xuống; nước chảy hơi nâu, tóc ướt lộ màu đen nâu. Chị nói: "
                 "\"Giờ xả lại bằng nước sạch, tới khi nước trong.\" 6–10s: chú ngẩng lên, chị đưa gương tay viền xanh, chú soi, trố mắt: \"Ủa, đen thiệt nè!\" "
                 "Tóc: bọt nâu → ướt bết, đen nâu.",
             lines=["Giờ xả lại bằng nước sạch, tới khi nước trong.", "CHÚ TƯ: Ủa, đen thiệt nè!"],
             end="chú cầm gương, tóc ướt đen nâu sạch bọt; chị cầm khăn bông xám"),
        dict(act="0–3s: CHỊ lau khăn bông lên tóc chú vài cái rồi bỏ khăn ra: tóc khô, ĐEN TỰ NHIÊN đều màu. 3–8s: chị (đã tháo găng) vuốt nhẹ tóc chú, tay kia cầm chai đỏ giơ cạnh đầu chú, nhãn hướng máy: "
                 "\"Lên màu đen tự nhiên, không bị giả. Có đen, nâu hạt dẻ, nâu sẫm, cà phê. Anh nào cần, Giang để ở phần bình luận.\" "
                 "8–10s: chú cười hở răng, giơ ngón cái: \"Trẻ ra chục tuổi!\"",
             lines=["Lên màu đen tự nhiên, không bị giả. Có đen, nâu hạt dẻ, nâu sẫm, cà phê. Anh nào cần, Giang để ở phần bình luận.", "CHÚ TƯ: Trẻ ra chục tuổi!"],
             end="chú Tư tóc đen cười tươi giơ ngón cái, chị cầm chai Nezha rõ nhãn ở góc phải khung"),
    ],
    info=dict(
        ten_day_du="Dầu gội phủ bạc Nezha 400ml chính hãng – dầu gội nhuộm tóc đen, nâu, dưỡng tóc nam nữ", pid="1734512215880205741",
        gia="niêm yết 210.000đ–1.120.000đ tùy combo · giá trung bình thực bán ~169.000đ/đơn",
        ban="87.953 đơn / 90 ngày (doanh thu ~14,9 tỷ) · tăng mạnh · 898 nhà sáng tạo, 3.212 video đang bán",
        hh="12%", danh_gia="1.527 đánh giá", ngay="mở bán 05/03/2026",
        cong_dung=["3 trong 1: gội – nhuộm – dưỡng.", "Phủ bạc ngay sau 1 lần gội, lên màu đều từ gốc tới ngọn.", "Tự làm tại nhà, không cần pha, không cần ra tiệm."],
        thanh_phan="Chiết xuất thảo dược (ảnh hãng nêu thầu dầu, dầu dừa, nhân cọ). Hãng công bố không amoniac, không paraben. "
                   "4 màu: đen tự nhiên, nâu hạt dẻ, nâu sẫm, cà phê. Công bố mỹ phẩm số 0991/257CBMP_LA (Công ty TNHH Mỹ Phẩm Avatar, Long An).",
        cach_dung="Mang găng tay, thoa lên tóc khô, xoa đều như gội đầu, ủ theo thời gian ghi trên hộp rồi xả sạch.",
        luu_y="Thuốc nhuộm có thể gây kích ứng: thử trước một ít sau tai/mặt trong cẳng tay. Tránh dây vào da, mắt. Một số người mua phản ánh dính da đầu hoặc tóc hơi khô.",
        review="Đa số khen lên màu đẹp, dễ dùng, mùi dễ chịu, giá hợp lý, có quà tặng. Phàn nàn: giao thiếu/sai màu, thiếu quà; vài trường hợp dính da đầu, tóc hơi khô.",
        bao_bi="Chai nhựa đỏ tươi 400ml nắp đỏ, nhãn vàng kim \"DẦU GỘI PHỦ BẠC – PLANT HAIR DYE\", logo NEZHA xanh dương; hộp giấy vàng kim."),
))

# ------------------------------------------------------------------ 3
V.append(dict(
    slug="03-kem-dsd-biozinc", ten="Viên Kẽm DSD",
    tieu_de="Ngoài 40 hay mệt, rụng tóc, ăn không ngon",
    hook_card=("NGOÀI 40 HAY MỆT", "RỤNG TÓC, ĂN KHÔNG NGON?"),
    van_de="Nam trung niên hay mệt, tóc rụng, ăn kém ngon, xuống sức mà không biết do thiếu vi chất.",
    giai_phap="Viên Kẽm DSD: kẽm gluconat kèm vitamin C, selen, mangan; ngày 1 viên.",
    ket_qua="Bổ sung đủ kẽm, dùng đều vài tuần mới thấy khác (đề kháng, da–tóc–móng, sức khỏe nam giới).",
    trang_phuc="áo sơ mi sọc dọc xanh navy – trắng, tay xắn tới khuỷu, tóc xõa vén sau tai, bông tai nụ bạc nhỏ, đồng hồ dây da nâu",
    boi_canh="gian bếp nhà buổi sáng: bàn bếp mặt đá trắng, cửa sổ lớn bên trái nắng sớm chiếu vào, rổ mây đựng cam và chuối, ấm đun nước inox, "
             "kệ treo ly tách phía sau, chậu húng quế nhỏ trên bệ cửa sổ, một ly thủy tinh nước ấm trên bàn",
    am_thanh="bếp yên tĩnh, tiếng chim ngoài cửa sổ, tiếng ấm nước reo rất nhẹ",
    san_pham="LỌ nhựa nâu sẫm gần đen, NẮP VÀNG KIM; nhãn XANH DƯƠNG ĐẬM – trắng, chữ trắng lớn \"VIÊN KẼM DSD\", dòng vàng \"ZINC GLUCONATE 120mg\", \"30 VIÊN\". "
             "Kèm HỘP GIẤY chữ nhật XANH DƯƠNG ĐẬM phối TRẮNG có sóng lượn, logo \"DSD\" trong elip xanh, chữ lớn \"VIÊN KẼM DSD\", dòng \"ZINC GLUCONATE 120mg\", "
             "ba chấm tròn Mangan sulfate – Vitamin C – Selen, \"60 VIÊN\" (trong hộp có 2 lọ). Viên nang màu trắng ngà",
    nhan_dang="lọ nâu nắp vàng kim nhãn xanh dương chữ \"VIÊN KẼM DSD\", hộp xanh dương – trắng",
    hook_luat="khung hình đầu tiên CHỊ đã đứng sau bàn bếp, tay phải giơ LỌ Viên Kẽm DSD cạnh mặt, nhãn hướng ống kính, hộp xanh nằm sẵn trên bàn; nói ngay, không chào hỏi",
    shots=[
        dict(act="0–5s: CHỊ đứng sau bàn bếp, tay phải giơ lọ cạnh má (nhãn hướng máy), tay trái vuốt nhẹ tóc mai mình làm điệu \"rụng tóc\", nhíu mày: "
                 "\"Ngoài bốn mươi mà hay mệt, tóc rụng, ăn không thấy ngon? Coi chừng anh đang thiếu kẽm.\" 5–10s: gật gù, cười: \"Chuyện nhỏ mà ít anh để ý.\"",
             lines=["Ngoài bốn mươi mà hay mệt, tóc rụng, ăn không thấy ngon? Coi chừng anh đang thiếu kẽm.", "Chuyện nhỏ mà ít anh để ý."],
             end="chị đặt lọ xuống cạnh hộp xanh trên bàn bếp"),
        dict(act="Lọ và hộp đứng trên bàn góc dưới phải. CHỊ chống một tay lên bàn, tay kia đếm ngón theo từng ý, cuối câu làm điệu lau mồ hôi trán: "
                 "\"Kẽm cơ thể không tự tạo ra, phải nạp từ ăn uống. Mà mấy anh nhậu nhiều, ăn uống thất thường, làm nặng, đổ mồ hôi nhiều, là dễ hụt.\"",
             lines=["Kẽm cơ thể không tự tạo ra, phải nạp từ ăn uống. Mà mấy anh nhậu nhiều, ăn uống thất thường, làm nặng, đổ mồ hôi nhiều, là dễ hụt."],
             end="chị cầm hộp xanh bằng tay trái, lọ bằng tay phải"),
        dict(act="CHỊ đưa HỘP xanh ra gần ống kính, ngón tay chỉ vào ba chấm tròn trên hộp, rồi đưa LỌ lên cạnh hộp: "
                 "\"Giang review Viên Kẽm DSD. Mỗi viên có kẽm gluconat, thêm vitamin C, selen, mangan. Hộp sáu mươi viên, xài được hai tháng.\"",
             lines=["Giang review Viên Kẽm DSD. Mỗi viên có kẽm gluconat, thêm vitamin C, selen, mangan. Hộp sáu mươi viên, xài được hai tháng."],
             end="chị đặt hộp xuống, vặn nắp vàng của lọ"),
        dict(act="CHỊ đổ MỘT viên nang ra lòng bàn tay, giơ một ngón tay, rồi cầm ly nước ấm lên; xoa nhẹ bụng khi nói tới bụng đói: "
                 "\"Ngày một viên, sau ăn ba mươi phút, uống với nước ấm. Đừng uống lúc bụng đói, dễ cồn cào. Dùng đều vài tuần mới thấy khác.\"",
             lines=["Ngày một viên, sau ăn ba mươi phút, uống với nước ấm. Đừng uống lúc bụng đói, dễ cồn cào. Dùng đều vài tuần mới thấy khác."],
             end="chị đặt ly xuống, cầm lọ đã đậy nắp"),
        dict(act="CHỊ cầm lọ trước ngực, nhãn hướng máy, hộp xanh ở góc dưới khung; nói rõ ràng, cuối câu cười, chỉ tay xuống dưới: "
                 "\"Kẽm hỗ trợ đề kháng, da, tóc, móng và sức khỏe nam giới. Thực phẩm bảo vệ sức khỏe, không phải thuốc. Anh nào cần, Giang để ở phần bình luận.\"",
             lines=["Kẽm hỗ trợ đề kháng, da, tóc, móng và sức khỏe nam giới. Thực phẩm bảo vệ sức khỏe, không phải thuốc. Anh nào cần, Giang để ở phần bình luận."],
             end="chị cười, lọ và hộp rõ nhãn trong khung"),
    ],
    info=dict(
        ten_day_du="DSDPHARMA Viên Kẽm DSD (Biozinc) – hộp 2 lọ x 30 viên / hộp 1 lọ 30 viên, có phân loại tặng bọt vệ sinh nam", pid="1729958693491935262",
        gia="niêm yết 168.000đ–360.000đ tùy phân loại · giá trung bình thực bán ~146.000đ/đơn",
        ban="78.014 đơn / 90 ngày (doanh thu ~11,4 tỷ) · 1.567 nhà sáng tạo, 15.350 video đang bán",
        hh="10%", danh_gia="56.872 đánh giá", ngay="mở bán 16/01/2024",
        cong_dung=["Bổ sung kẽm cho cơ thể.", "Hỗ trợ tăng cường sức khỏe, đề kháng, giảm mệt mỏi.", "Hỗ trợ da, tóc, móng."],
        thanh_phan="Kẽm gluconat 120mg/150mg tùy phân loại (đây là khối lượng muối kẽm, không phải kẽm nguyên tố), Panax ginseng 50mg, vitamin B1 1,5mg, B2 2mg, B6 1,5mg, "
                   "mangan sulfate 2mg, vitamin C 20mg, selen men 10mcg.",
        cach_dung="Người lớn 1 viên/ngày, sáng hoặc chiều, sau ăn 30 phút, uống với nước ấm. Khuyến khích dùng liên tục 3 tháng.",
        luu_y="Không phải là thuốc. Listing có 2 mẫu: hộp XANH \"Viên Kẽm DSD 120mg\" và hộp CAM–TRẮNG \"Kẽm DSD Multi Ginseng B+ 150mg\" – prompt viết theo hộp xanh; "
              "nếu gắn link mẫu cam thì đổi ảnh đính kèm và mô tả sản phẩm. Không nên uống lúc đói.",
        review="Phần lớn khen chất lượng, đóng gói gọn, đúng mô tả, dùng êm. Một số ít phàn nàn hàng không đúng mô tả hoặc hiệu quả chưa rõ.",
        bao_bi="Lọ nâu sẫm nắp vàng kim, nhãn xanh dương – trắng \"VIÊN KẼM DSD – ZINC GLUCONATE 120mg\"; hộp giấy xanh dương – trắng 60 viên."),
))

# ------------------------------------------------------------------ 4
V.append(dict(
    slug="04-mieng-dan-chan-thao-duoc", ten="Miếng dán chân thảo dược",
    tieu_de="2 giờ sáng vẫn nằm đếm quạt trần",
    hook_card=("2 GIỜ SÁNG", "VẪN NẰM ĐẾM QUẠT TRẦN?"),
    van_de="Người lớn tuổi khó vô giấc, chân mỏi, chân lạnh, bứt rứt ban đêm.",
    giai_phap="Miếng dán chân thảo dược (gừng, ngải cứu, giấm tre, than tre) dán lòng bàn chân qua đêm.",
    ket_qua="Chân ấm, dễ chịu, đỡ mỏi nên dễ ngủ hơn. Nói thật: miếng dán sậm màu là do ẩm mồ hôi, không phải \"hút độc\".",
    trang_phuc="bộ pijama lụa màu xanh rêu tay dài, cổ bẻ viền trắng, tóc tết lỏng một bên vai trái, bông tai nụ bạc nhỏ, chân trần",
    boi_canh="phòng ngủ ban đêm: giường gỗ, drap và gối màu xám nhạt, tủ đầu giường có đèn ngủ chụp vải ánh vàng ấm và đồng hồ báo thức tròn, "
             "rèm cửa xanh đậm kéo kín, quạt trần mờ phía trên, ánh sáng dịu, hơi tối nhưng mặt nhân vật vẫn sáng rõ",
    am_thanh="phòng đêm yên tĩnh, tiếng quạt trần đều đều, tiếng dế xa",
    san_pham="TÚI zip dẹt nền ĐEN, nửa bên phải in hình thân TRE và lá tre xanh lá có giọt nước, chữ trắng lớn \"Deep Cleansing\", bên dưới \"FOOT PATCH\", "
             "chữ nhỏ \"QUALITY 100% Traditional Wisdom\", dải trắng ở đáy túi. Bên trong là các MIẾNG DÁN: tấm keo vải không dệt màu TRẮNG hình chữ nhật bo góc, "
             "ở giữa gắn một túi bột thảo dược VUÔNG màu VÀNG chanh có in chữ",
    nhan_dang="túi đen in hình tre xanh chữ \"Deep Cleansing FOOT PATCH\"; miếng dán trắng có túi vuông vàng ở giữa",
    hook_luat="khung hình đầu tiên CHỊ đã ngồi ở mép giường trong phòng ngủ ban đêm, tay phải giơ TÚI ĐEN Foot Patch cạnh mặt, mắt ngước nhìn lên quạt trần rồi nhìn máy; nói ngay, không chào hỏi",
    shots=[
        dict(act="0–5s: CHỊ ngồi mép giường, tay phải giơ túi đen cạnh má (mặt in tre hướng máy), mắt ngước lên trần, tay trái đếm ngón, rồi nhìn thẳng máy: "
                 "\"Hai giờ sáng còn nằm đếm quạt trần? Chân thì mỏi, người thì bứt rứt.\" 5–10s: lắc nhẹ túi, cười: \"Anh nào bị, coi Giang thử cái này.\"",
             lines=["Hai giờ sáng còn nằm đếm quạt trần? Chân thì mỏi, người thì bứt rứt.", "Anh nào bị, coi Giang thử cái này."],
             end="chị đặt túi đen lên đùi, mặt in tre hướng máy"),
        dict(act="CHỊ co một chân lên giường, tay bóp nhẹ bắp chân và gan bàn chân mình, nói giọng tâm tình; cuối câu cầm túi đen giơ lên lại: "
                 "\"Lớn tuổi, đi đứng cả ngày, tối chân lạnh, chân mỏi là khó vô giấc. Ông bà mình hay ngâm chân nước gừng. Còn lười ngâm thì có miếng dán này.\"",
             lines=["Lớn tuổi, đi đứng cả ngày, tối chân lạnh, chân mỏi là khó vô giấc. Ông bà mình hay ngâm chân nước gừng. Còn lười ngâm thì có miếng dán này."],
             end="chị cầm túi đen bằng hai tay, chuẩn bị mở miệng zip"),
        dict(act="CHỊ mở zip, rút ra MỘT miếng dán (tấm trắng, túi vuông vàng ở giữa), đưa sát ống kính 2 giây, ngón tay chỉ vào túi vàng: "
                 "\"Miếng dán chân thảo dược: có gừng, ngải cứu, giấm tre, than tre. Một túi nhiều miếng, dán ban đêm lúc đi ngủ.\"",
             lines=["Miếng dán chân thảo dược: có gừng, ngải cứu, giấm tre, than tre. Một túi nhiều miếng, dán ban đêm lúc đi ngủ."],
             end="chị bóc lớp giấy lót của miếng dán, bàn chân trái gác lên đầu gối phải, lòng bàn chân hướng máy"),
        dict(act="Cận hơn vào lòng bàn chân trái sạch sẽ của CHỊ (mặt chị vẫn trong khung phía trên). Chị áp miếng dán vào GIỮA lòng bàn chân, miết phẳng bốn mép bằng ngón cái, rồi xoa nhẹ: "
                 "\"Rửa chân lau khô, bóc ra, dán vô giữa lòng bàn chân, để qua đêm. Thấy ấm ấm, dễ chịu, chân đỡ mỏi nên dễ ngủ hơn.\"",
             lines=["Rửa chân lau khô, bóc ra, dán vô giữa lòng bàn chân, để qua đêm. Thấy ấm ấm, dễ chịu, chân đỡ mỏi nên dễ ngủ hơn."],
             end="miếng dán trắng–vàng nằm phẳng giữa lòng bàn chân trái, chị ngẩng lên nhìn máy"),
        dict(act="CHỊ thả chân xuống, ngồi thẳng, tay phải cầm túi đen giơ ngang ngực, tay trái giơ ngón trỏ, nét mặt thẳng thắn, cuối câu cười và chỉ tay xuống dưới: "
                 "\"Nói thiệt nha: sáng miếng dán sậm màu là do hút ẩm mồ hôi, không phải hút độc. Mất ngủ lâu ngày thì đi khám. Cần thì Giang để ở bình luận.\"",
             lines=["Nói thiệt nha: sáng miếng dán sậm màu là do hút ẩm mồ hôi, không phải hút độc. Mất ngủ lâu ngày thì đi khám. Cần thì Giang để ở bình luận."],
             end="chị cười, túi đen in hình tre rõ trong khung"),
    ],
    info=dict(
        ten_day_du="Miếng Dán Thảo Dược Truyền Thống Cho Chân (Deep Cleansing Foot Patch) – túi 10 / 20 miếng", pid="1735794736267888018",
        gia="niêm yết 75.000đ–107.000đ · giá trung bình thực bán ~61.000đ/đơn",
        ban="14.378 đơn / 90 ngày (doanh thu ~0,88 tỷ) · tăng mạnh (1,3k → 5,7k → 7,3k mỗi tháng) · 162 nhà sáng tạo",
        hh="14%", danh_gia="479 đánh giá", ngay="mở bán 14/06/2026 · hàng gửi từ nước ngoài (thời gian giao lâu hơn)",
        cong_dung=["Dán lòng bàn chân qua đêm, tạo cảm giác ấm, thư giãn bàn chân.", "Người mua phản hồi: dễ ngủ hơn, chân đỡ mỏi."],
        thanh_phan="Gừng, giấm tre, ngải cứu, than tre (theo thông tin listing).",
        cach_dung="Rửa chân, lau khô, bóc lớp lót, dán vào giữa lòng bàn chân trước khi ngủ, sáng bóc bỏ và rửa chân.",
        luu_y="Listing ghi \"Deep Cleansing/Detox\" nhưng KHÔNG có bằng chứng miếng dán hút độc tố; miếng dán sậm màu buổi sáng là do hút ẩm mồ hôi. "
              "Kịch bản chỉ nói đúng mức: ấm chân, dễ chịu, hỗ trợ dễ ngủ. Không dán lên da trầy xước; da kích ứng thì ngưng.",
        review="Nhiều người khen dễ dùng, ngủ ngon hơn, giảm mỏi. Một số nói không hiệu quả như quảng cáo, không thấy tác dụng rõ, có trường hợp giao thiếu.",
        bao_bi="Túi zip đen in hình tre xanh, chữ trắng \"Deep Cleansing FOOT PATCH\"; miếng dán vải trắng, túi thảo dược vuông màu vàng ở giữa."),
))

# ------------------------------------------------------------------ 5
V.append(dict(
    slug="05-xuong-khop-sao-thai-duong", ten="Xương Khớp Sao Thái Dương",
    tieu_de="Đứng lên ngồi xuống, gối kêu rắc rắc",
    hook_card=("ĐỨNG LÊN NGỒI XUỐNG", "GỐI KÊU RẮC RẮC?"),
    van_de="Nam 50+ gối kêu, nhức khi trở trời, sáng dậy tê bì tay chân, leo cầu thang phải vịn, ráng chịu.",
    giai_phap="Viên Xương Khớp Sao Thái Dương (thương hiệu Việt, lọ 90 viên) + vận động nhẹ, giữ cân nặng.",
    ket_qua="Uống đều 1–3 tháng; nhiều người mua lại, phản hồi đỡ nhức sau khoảng một hộp.",
    trang_phuc="áo khoác gió thể thao màu hồng đào kéo khóa lưng chừng, bên trong áo thun trắng, tóc cột đuôi ngựa cao, khăn bông nhỏ màu trắng vắt cổ, bông tai nụ bạc nhỏ",
    boi_canh="công viên buổi sáng sớm: ghế đá mài màu xám dưới tán cây me tây, lối đi lát gạch, thảm cỏ xanh còn sương, hồ nước lấp lánh phía xa, "
             "vài cô chú lớn tuổi tập dưỡng sinh và đi bộ mờ phía sau, nắng sớm xiên vàng nhạt",
    am_thanh="tiếng chim, tiếng lá xào xạc, tiếng nhạc dưỡng sinh rất nhỏ ở xa, tiếng bước chân",
    san_pham="LỌ thủy tinh NÂU HỔ PHÁCH dáng tròn thấp, NẮP ĐEN; nhãn TRẮNG có dòng nhỏ \"Thực phẩm bảo vệ sức khỏe\", chữ ĐỎ đậm \"XƯƠNG KHỚP\" và chữ CAM đậm \"SAO THÁI DƯƠNG\", "
             "hai gạch đầu dòng chữ đỏ nhỏ, dải ĐỎ ở chân nhãn có ngôi sao trắng và chữ \"THÁI DƯƠNG\". Kèm HỘP GIẤY TRẮNG cùng chữ đỏ – cam, in hình KHỚP GỐI màu cam đỏ, đáy hộp dải đỏ \"THÁI DƯƠNG\". "
             "Viên bên trong màu nâu",
    nhan_dang="lọ nâu hổ phách nắp đen nhãn trắng chữ đỏ \"XƯƠNG KHỚP\" chữ cam \"SAO THÁI DƯƠNG\"; hộp trắng in hình khớp gối",
    hook_luat="khung hình đầu tiên CHỊ đang từ tư thế ngồi trên ghế đá chống gối đứng lên, tay phải đã cầm LỌ Xương Khớp Sao Thái Dương nhãn hướng ống kính, mặt nhăn nhẹ giả đau gối; nói ngay, không chào hỏi",
    shots=[
        dict(act="0–5s: CHỊ chống tay trái lên gối đứng dậy khỏi ghế đá rồi ngồi xuống lại, mặt nhăn nhó vui, tay phải giơ lọ ngang vai (nhãn hướng máy): "
                 "\"Đứng lên ngồi xuống, gối kêu rắc rắc? Sáng ngủ dậy tay chân tê bì?\" 5–10s: ngồi yên, vỗ nhẹ đầu gối, nhìn thẳng máy: \"Mấy anh ngoài năm mươi nghe Giang nè.\"",
             lines=["Đứng lên ngồi xuống, gối kêu rắc rắc? Sáng ngủ dậy tay chân tê bì?", "Mấy anh ngoài năm mươi nghe Giang nè."],
             end="chị ngồi trên ghế đá, đặt lọ lên mặt ghế bên cạnh, nhãn hướng máy"),
        dict(act="Lọ đứng trên ghế đá góc dưới phải. CHỊ xoa hai đầu gối, rồi làm điệu vịn tay vào lan can tưởng tượng, cuối câu lắc ngón trỏ: "
                 "\"Trở trời là nhức, leo cầu thang phải vịn. Nhiều anh ráng chịu, tới lúc đi không nổi mới lo. Đừng để vậy.\"",
             lines=["Trở trời là nhức, leo cầu thang phải vịn. Nhiều anh ráng chịu, tới lúc đi không nổi mới lo. Đừng để vậy."],
             end="chị cầm lọ bằng tay phải, tay trái lấy hộp giấy trắng từ túi áo khoác"),
        dict(act="CHỊ dựng HỘP trắng lên mặt ghế đá (hình khớp gối hướng máy), đưa LỌ ra gần ống kính, ngón tay lướt dưới dòng chữ đỏ cam trên nhãn: "
                 "\"Giang review lọ Xương Khớp Sao Thái Dương, hàng Việt Nam, lọ chín mươi viên. Hỗ trợ thông kinh hoạt lạc, mạnh gân cốt, giảm nhức mỏi, tê bì chân tay.\"",
             lines=["Giang review lọ Xương Khớp Sao Thái Dương, hàng Việt Nam, lọ chín mươi viên. Hỗ trợ thông kinh hoạt lạc, mạnh gân cốt, giảm nhức mỏi, tê bì chân tay."],
             end="chị vặn mở nắp đen của lọ"),
        dict(act="CHỊ đổ HAI viên nâu ra lòng bàn tay trái, chìa về ống kính, tay phải giơ hai rồi ba ngón theo lời; cuối câu gật đầu chắc chắn: "
                 "\"Ngày uống hai đến ba lần, mỗi lần hai đến ba viên, uống liền một tới ba tháng. Nhiều cô chú mua lại, nói đỡ nhức sau khi xài hết một hộp.\"",
             lines=["Ngày uống hai đến ba lần, mỗi lần hai đến ba viên, uống liền một tới ba tháng. Nhiều cô chú mua lại, nói đỡ nhức sau khi xài hết một hộp."],
             end="chị đậy nắp lọ, cầm lọ bằng tay phải, chuẩn bị đứng lên"),
        dict(act="0–3s: CHỊ đứng dậy nhẹ nhàng, vươn vai, xoay nhẹ khớp gối. 3–10s: giơ lọ ngang ngực nhãn hướng máy, hộp trắng nằm trên ghế đá góc dưới khung, cuối câu cười, chỉ tay xuống dưới: "
                 "\"Kết hợp đi bộ nhẹ, giữ cân nặng nha. Thực phẩm bảo vệ sức khỏe, không phải thuốc. Sưng nóng đỏ thì đi khám. Cần thì Giang để ở bình luận.\"",
             lines=["Kết hợp đi bộ nhẹ, giữ cân nặng nha. Thực phẩm bảo vệ sức khỏe, không phải thuốc. Sưng nóng đỏ thì đi khám. Cần thì Giang để ở bình luận."],
             end="chị đứng cười giữa công viên, lọ và hộp rõ nhãn trong khung"),
    ],
    info=dict(
        ten_day_du="Xương khớp Sao Thái Dương – Hỗ trợ thông kinh hoạt lạc, mạnh gân cốt – lọ 90 viên", pid="1730099458590738955",
        gia="niêm yết 183.000đ–1.187.000đ tùy combo · giá trung bình thực bán ~295.000đ/đơn",
        ban="10.237 đơn / 90 ngày (doanh thu ~3,0 tỷ) · 460 nhà sáng tạo, 3.294 video",
        hh="15% (khoảng 44.000đ/đơn – cao nhất trong 6 sản phẩm)", danh_gia="1.307 đánh giá", ngay="mở bán 12/10/2024",
        cong_dung=["Hỗ trợ thông kinh hoạt lạc, mạnh gân cốt.", "Hỗ trợ giảm nhức mỏi xương khớp, tê bì chân tay do khí huyết ứ trệ, thoái hóa khớp, phong thấp."],
        thanh_phan="Listing không ghi chi tiết thành phần (xem trên nhãn hộp khi quay).",
        cach_dung="Ngày uống 2–3 lần, mỗi lần 2–3 viên. Đợt dùng 1–3 tháng liên tục.",
        luu_y="Không phải là thuốc. Không dùng cho phụ nữ có thai, đang cho con bú, người mẫn cảm với thành phần. Ảnh listing kèm quà tặng dầu gừng 3ml (tùy đợt).",
        review="Khen hiệu quả giảm đau, đóng gói, giao nhanh; nhiều người mua lại nhiều lần cho người lớn tuổi. Phàn nàn: giao chậm, thiếu quà, mới dùng chưa rõ hiệu quả, có người nghi ngờ nguồn gốc.",
        bao_bi="Lọ thủy tinh nâu hổ phách nắp đen, nhãn trắng chữ đỏ \"XƯƠNG KHỚP\" chữ cam \"SAO THÁI DƯƠNG\"; hộp trắng in hình khớp gối, dải đỏ \"THÁI DƯƠNG\"."),
))

# ------------------------------------------------------------------ 6
V.append(dict(
    slug="06-vuong-bao", ten="Vương Bảo",
    tieu_de="Một đêm dậy tiểu mấy lần hả mấy anh?",
    hook_card=("MỘT ĐÊM DẬY TIỂU", "MẤY LẦN HẢ MẤY ANH?"),
    van_de="Nam 50+ tiểu đêm, tiểu rắt, tia yếu, tiểu không hết do phì đại tiền liệt tuyến; mất ngủ, ngại đi khám.",
    giai_phap="Vương Bảo (Thái Minh) – thảo dược cho nam giới phì đại tiền liệt tuyến có rối loạn tiểu tiện.",
    ket_qua="Nhiều người mua lại nhiều lần, phản hồi đêm ngủ dài giấc hơn; kèm bớt trà, bia buổi tối.",
    trang_phuc="áo sơ mi linen trắng tay lỡ, khăn lụa nhỏ màu xanh cổ vịt thắt quanh cổ, tóc xõa uốn gợn nhẹ, bông tai nụ bạc nhỏ",
    boi_canh="hiên nhà vườn buổi chiều muộn: bộ bàn ghế gỗ thấp, bộ ấm trà sứ men lam và hai chén nhỏ trên bàn, nền gạch tàu, hàng chậu kiểng mai chiếu thủy và nguyệt quế, "
             "cột hiên gỗ nâu, giàn hoa giấy trắng, nắng chiều vàng mật xiên qua",
    am_thanh="tiếng chim chiều, tiếng gió qua lá, tiếng rót trà",
    san_pham="HỘP GIẤY chữ nhật dẹt nằm ngang: nửa trái nền XANH DƯƠNG, nửa phải nền XÁM NHẠT; dòng nhỏ \"Thực phẩm bảo vệ sức khỏe\", chữ TRẮNG lớn \"Vương Bảo\" kèm nhãn nhỏ cam \"NEW\", "
             "dòng \"Dùng cho nam giới bị U xơ tiền liệt tuyến\"; bên phải hình minh họa BÀNG QUANG xanh nhạt và TUYẾN TIỀN LIỆT màu vàng cam; góc dưới phải ô vuông xanh logo trái tim \"Thái Minh\"; "
             "góc dưới trái dấu \"THƯƠNG HIỆU QUỐC GIA\"; ghi \"20 viên nén\". Bên trong là vỉ nhôm bạc, viên nén tròn",
    nhan_dang="hộp dẹt xanh dương – xám nhạt chữ trắng \"Vương Bảo\", hình bàng quang và tuyến tiền liệt, logo Thái Minh",
    hook_luat="khung hình đầu tiên CHỊ đã ngồi ở bàn trà ngoài hiên, tay phải giơ HỘP Vương Bảo cạnh mặt, mặt chữ hướng ống kính, tay trái giơ HAI ngón tay; nói ngay, không chào hỏi",
    shots=[
        dict(act="0–5s: CHỊ ngồi bên bàn trà, tay phải giơ hộp xanh cạnh má (mặt chữ hướng máy), tay trái giơ một, hai, rồi ba ngón, nhướn mày hỏi: "
                 "\"Một đêm dậy đi tiểu mấy lần hả mấy anh?\" 5–10s: giữ hai ngón tay, nghiêng người tới: \"Từ hai lần trở lên, tiểu xong vẫn thấy chưa hết, thì nghe Giang nói.\"",
             lines=["Một đêm dậy đi tiểu mấy lần hả mấy anh?", "Từ hai lần trở lên, tiểu xong vẫn thấy chưa hết, thì nghe Giang nói."],
             end="chị đặt hộp đứng trên bàn trà cạnh ấm trà, mặt chữ hướng máy"),
        dict(act="Hộp đứng trên bàn góc dưới phải. CHỊ dùng hai bàn tay khum lại rồi siết nhẹ minh họa \"chèn\", sau đó xòe tay, giọng nhẹ nhàng cảm thông: "
                 "\"Ngoài năm mươi, tuyến tiền liệt hay to ra, chèn đường tiểu. Nên tiểu rắt, tia yếu, đêm dậy hoài, mất ngủ. Rất nhiều anh bị, không có gì phải ngại.\"",
             lines=["Ngoài năm mươi, tuyến tiền liệt hay to ra, chèn đường tiểu. Nên tiểu rắt, tia yếu, đêm dậy hoài, mất ngủ. Rất nhiều anh bị, không có gì phải ngại."],
             end="chị cầm hộp lên bằng hai tay"),
        dict(act="CHỊ đưa HỘP ra gần ống kính, ngón tay chỉ vào chữ \"Vương Bảo\" rồi chỉ sang logo Thái Minh, sau đó lật nhẹ cho thấy mặt bên: "
                 "\"Giang review hộp Vương Bảo của Thái Minh. Thành phần thảo dược: náng hoa trắng, ngải Nhật, tàu bay, hải trung kim. Hộp hai mươi viên nén.\"",
             lines=["Giang review hộp Vương Bảo của Thái Minh. Thành phần thảo dược: náng hoa trắng, ngải Nhật, tàu bay, hải trung kim. Hộp hai mươi viên nén."],
             end="chị mở nắp hộp, rút ra một vỉ nhôm bạc"),
        dict(act="CHỊ giơ VỈ nhôm bạc cạnh hộp, giơ hai ngón tay, rồi chỉ vào đồng hồ tưởng tượng trên cổ tay; cuối câu gật đầu, cười: "
                 "\"Ngày uống hai lần, mỗi lần hai đến ba viên, trước ăn ba mươi phút. Nhiều anh mua lại nhiều lần, phản hồi đêm ngủ được dài giấc hơn.\"",
             lines=["Ngày uống hai lần, mỗi lần hai đến ba viên, trước ăn ba mươi phút. Nhiều anh mua lại nhiều lần, phản hồi đêm ngủ được dài giấc hơn."],
             end="chị cất vỉ vào hộp, cầm hộp bằng tay phải"),
        dict(act="CHỊ giơ hộp ngang ngực, mặt chữ hướng máy; tay trái giơ ngón trỏ dặn, rồi đẩy nhẹ chén trà ra xa khi nói \"bớt trà\"; cuối câu cười, chỉ tay xuống dưới: "
                 "\"Thực phẩm bảo vệ sức khỏe, không phải thuốc. Bí tiểu, tiểu ra máu thì đi khám liền. Tối bớt trà, bớt bia nữa nha. Cần thì Giang để ở bình luận.\"",
             lines=["Thực phẩm bảo vệ sức khỏe, không phải thuốc. Bí tiểu, tiểu ra máu thì đi khám liền. Tối bớt trà, bớt bia nữa nha. Cần thì Giang để ở bình luận."],
             end="chị cười bên bàn trà, hộp Vương Bảo rõ chữ trong khung"),
    ],
    info=dict(
        ten_day_du="Vương Bảo (Thái Minh) – hỗ trợ cải thiện tiểu đêm, tiểu buốt, tiểu nhiều lần ở nam giới phì đại tiền liệt tuyến – hộp 20 viên", pid="1730109150328818298",
        gia="niêm yết 210.000đ–453.000đ · giá trung bình thực bán ~167.000đ/đơn",
        ban="1.196 đơn / 90 ngày (doanh thu ~200 triệu) · đi ngang · listing 80 viên mua 1 tặng 1 (id 1732105751941974650) bán thêm 668 đơn",
        hh="10%", danh_gia="307 đánh giá", ngay="mở bán 15/09/2024",
        cong_dung=["Dùng cho nam giới bị phì đại tiền liệt tuyến.", "Hỗ trợ cải thiện tiểu đêm, tiểu buốt, tiểu rắt, tiểu không hết, tiểu nhiều lần, tia nước tiểu yếu."],
        thanh_phan="Cao Náng hoa trắng 160mg, cao Ngải Nhật 150mg, cao Tàu bay 125mg, cao lá cây Hoa ban 80mg, cao Hải trung kim 60mg, cao Sài hồ nam 50mg, cao Đơn kim 50mg, cao Ngũ sắc 36mg.",
        cach_dung="Tăng cường: ngày 2 lần, mỗi lần 2–3 viên. Duy trì: ngày 2 lần, mỗi lần 1–2 viên. Uống trước ăn 30 phút hoặc sau ăn 1 giờ.",
        luu_y="Không phải là thuốc. Số ĐKSP 9335/2020/ĐKSP · GPQC 391/2021/XNQC-ATTP. Hộp 20 viên chỉ đủ khoảng 4–5 ngày liều tăng cường – khi gắn link nên cân nhắc listing 80 viên.",
        review="Khen chất lượng, giao nhanh; nhiều người dùng nhiều lần, thấy cải thiện tiểu đêm. Có phản hồi hàng cận/hết hạn hoặc không hiệu quả với một số người.",
        bao_bi="Hộp giấy dẹt xanh dương – xám nhạt, chữ trắng \"Vương Bảo\", hình bàng quang và tuyến tiền liệt, logo Thái Minh, dấu Thương hiệu Quốc gia, \"20 viên nén\"."),
))


# ------------------------------------------------------------------
# NHÂN VẬT + TRANG PHỤC + BỐI CẢNH lấy từ ảnh 1 người dùng đính kèm → prompt không mô tả lại.
# Hành động từng shot viết lại để không phụ thuộc bối cảnh (không sofa, bàn, ghế đá...). {0},{1} = lời thoại.
END5 = "chị cười, sản phẩm rõ nhãn trong khung"
ACTS = {
    "01-bo-than-dsd-sam-nhung": [
        ("0–5s: CHỊ ở đúng vị trí như ảnh 1, tay phải giơ lọ ngang má (nhãn hướng máy), tay trái giơ ba rồi bốn ngón, mắt mở to, nhướn mày: {0} "
         "5–10s: hạ tay trái, nghiêng đầu, giọng nhỏ lại tâm tình: {1}", "chị cầm lọ ngang ngực bằng tay phải, nhãn hướng máy"),
        ("CHỊ vẫn cầm lọ tay phải ngang ngực, tay trái đưa ra sau thắt lưng làm điệu bộ đau lưng, rồi xòe tay, lắc đầu nhẹ, cười cảm thông: {0}",
         "chị cầm lọ tay phải, tay trái cầm thêm hộp giấy đỏ đô"),
        ("CHỊ giơ HỘP đỏ đô bằng tay trái (mặt chữ hướng máy), tay phải đưa LỌ ra gần ống kính rồi xoay nhẹ cho thấy nhãn có hình hươu và nhân sâm: {0}",
         "chị kẹp hộp dưới cánh tay trái, vặn mở nắp trắng của lọ"),
        ("CHỊ nghiêng lọ đổ HAI viên nang nâu ra lòng bàn tay trái, chìa tay về ống kính 2 giây, rồi giơ hai ngón tay: {0}",
         "chị đậy nắp, cầm lọ tay phải, hộp tay trái"),
        ("CHỊ cầm lọ và hộp đỏ đô ngang ngực, nhãn hướng máy; nét mặt nghiêm túc dặn dò, cuối câu cười tươi, hất cằm nhẹ xuống dưới: {0}", END5),
    ],
    "03-kem-dsd-biozinc": [
        ("0–5s: CHỊ ở đúng vị trí như ảnh 1, tay phải giơ lọ cạnh má (nhãn hướng máy), tay trái vuốt nhẹ tóc mai mình làm điệu rụng tóc, nhíu mày: {0} "
         "5–10s: gật gù, cười: {1}", "chị cầm lọ ngang ngực, nhãn hướng máy"),
        ("CHỊ cầm lọ tay phải ngang ngực, tay trái đếm ngón theo từng ý, cuối câu làm điệu lau mồ hôi trán: {0}",
         "chị cầm hộp xanh bằng tay trái, lọ bằng tay phải"),
        ("CHỊ đưa HỘP xanh ra gần ống kính cho thấy ba chấm tròn trên hộp, rồi đưa LỌ lên cạnh hộp: {0}",
         "chị kẹp hộp dưới cánh tay trái, vặn nắp vàng của lọ"),
        ("CHỊ đổ MỘT viên nang ra lòng bàn tay trái, chìa về ống kính, giơ một ngón tay; xoa nhẹ bụng khi nói tới bụng đói: {0}",
         "chị đậy nắp, cầm lọ tay phải, hộp tay trái"),
        ("CHỊ cầm lọ và hộp xanh ngang ngực, nhãn hướng máy; nói rõ ràng, cuối câu cười, hất cằm nhẹ xuống dưới: {0}", END5),
    ],
    "04-mieng-dan-chan-thao-duoc": [
        ("0–5s: CHỊ ở đúng vị trí như ảnh 1, tay phải giơ túi đen cạnh má (mặt in tre hướng máy), mắt ngước lên cao như đang nhìn trần nhà, tay trái đếm ngón, rồi nhìn thẳng máy: {0} "
         "5–10s: lắc nhẹ túi, cười: {1}", "chị cầm túi đen ngang ngực, mặt in tre hướng máy"),
        ("CHỊ cầm túi tay phải, tay trái vỗ nhẹ lên đùi rồi chỉ xuống bàn chân mình, giọng tâm tình; cuối câu giơ túi đen lên lại: {0}",
         "chị cầm túi đen bằng hai tay, chuẩn bị mở miệng zip"),
        ("CHỊ mở zip, rút ra MỘT miếng dán (tấm trắng, túi vuông vàng ở giữa), đưa sát ống kính 2 giây, ngón tay chỉ vào túi vàng: {0}",
         "chị bóc lớp giấy lót của miếng dán, tay trái ngửa lòng bàn tay về phía máy"),
        ("CHỊ làm mẫu trên lòng bàn tay trái thay cho lòng bàn chân: áp miếng dán vào GIỮA lòng bàn tay, miết phẳng bốn mép bằng ngón cái, rồi chỉ xuống bàn chân mình: {0}",
         "miếng dán trắng–vàng nằm phẳng giữa lòng bàn tay trái đang giơ về máy"),
        ("CHỊ tay phải cầm túi đen giơ ngang ngực, tay trái giơ ngón trỏ, nét mặt thẳng thắn, cuối câu cười, hất cằm nhẹ xuống dưới: {0}", END5),
    ],
    "05-xuong-khop-sao-thai-duong": [
        ("0–5s: CHỊ ở đúng vị trí như ảnh 1, nhún gối xuống rồi đứng thẳng lên một lần, mặt nhăn nhó vui giả đau gối, tay phải giơ lọ ngang vai (nhãn hướng máy): {0} "
         "5–10s: đứng yên, tay trái vỗ nhẹ đầu gối, nhìn thẳng máy: {1}", "chị đứng thẳng, cầm lọ ngang ngực, nhãn hướng máy"),
        ("CHỊ cầm lọ tay phải, tay trái xoa đầu gối rồi làm điệu vịn lan can tưởng tượng, cuối câu lắc ngón trỏ: {0}",
         "chị cầm lọ tay phải, tay trái cầm hộp giấy trắng"),
        ("CHỊ giơ HỘP trắng bằng tay trái (hình khớp gối hướng máy), tay phải đưa LỌ ra gần ống kính cho thấy dòng chữ đỏ cam trên nhãn: {0}",
         "chị kẹp hộp dưới cánh tay trái, vặn mở nắp đen của lọ"),
        ("CHỊ đổ HAI viên nâu ra lòng bàn tay trái, chìa về ống kính, rồi giơ hai, ba ngón theo lời; cuối câu gật đầu chắc chắn: {0}",
         "chị đậy nắp, cầm lọ tay phải, hộp tay trái"),
        ("0–3s: CHỊ vươn vai, xoay nhẹ khớp gối tại chỗ. 3–10s: giơ lọ và hộp ngang ngực, nhãn hướng máy, cuối câu cười, hất cằm nhẹ xuống dưới: {0}", END5),
    ],
    "06-vuong-bao": [
        ("0–5s: CHỊ ở đúng vị trí như ảnh 1, tay phải giơ hộp xanh cạnh má (mặt chữ hướng máy), tay trái giơ một, hai, rồi ba ngón, nhướn mày hỏi: {0} "
         "5–10s: giữ hai ngón tay, nghiêng người tới: {1}", "chị cầm hộp ngang ngực bằng hai tay, mặt chữ hướng máy"),
        ("CHỊ cầm hộp tay phải, bàn tay trái khum lại rồi siết nhẹ minh họa bị chèn, sau đó xòe tay, giọng nhẹ nhàng cảm thông: {0}",
         "chị cầm hộp bằng hai tay"),
        ("CHỊ đưa HỘP ra gần ống kính, ngón tay chỉ vào chữ Vương Bảo rồi chỉ sang logo Thái Minh, sau đó xoay nhẹ cho thấy mặt bên: {0}",
         "chị mở nắp hộp, rút ra một vỉ nhôm bạc"),
        ("CHỊ giơ VỈ nhôm bạc cạnh hộp, giơ hai ngón tay, rồi chỉ vào cổ tay như xem giờ; cuối câu gật đầu, cười: {0}",
         "chị cất vỉ vào hộp, cầm hộp tay phải"),
        ("CHỊ giơ hộp ngang ngực, mặt chữ hướng máy; tay trái giơ ngón trỏ dặn, xua nhẹ tay khi nói bớt trà bớt bia; cuối câu cười, hất cằm nhẹ xuống dưới: {0}", END5),
    ],
}
for v in V:
    for k in ("trang_phuc", "boi_canh", "am_thanh"):
        v.pop(k, None)
    v["hook_luat"] = (f"khung hình đầu tiên giữ đúng nhân vật, trang phục, bối cảnh và góc máy của ảnh 1, nhưng trên tay CHỊ đã cầm {v['ten']}, "
                      "nhãn hướng ống kính; nói ngay câu đầu, không chào hỏi")
    if v["slug"] in ACTS:
        for s, (act, end) in zip(v["shots"], ACTS[v["slug"]]):
            s["act"] = act.format(*[f'"{l}"' for l in s["lines"]])
            s["end"] = end
    else:  # 02 Nezha: có thêm chú Tư và đạo cụ gội đầu (không có trong ảnh 1)
        v["hook_luat"] = ("khung hình đầu tiên giữ đúng CHỊ, trang phục, bối cảnh của ảnh 1; CHỊ (đã mang găng nilon đen) đang bóp CHAI ĐỎ Nezha cho dung dịch nâu sẫm "
                          "chảy lên mái tóc BẠC TRẮNG của CHÚ TƯ đang ngồi trước mặt chị; không có cảnh đi tới, không chào hỏi")
        v["extra_char"] = ("- CHÚ TƯ (nhân vật phụ, KHÔNG có trong ảnh 1, thêm vào đúng bối cảnh của ảnh 1): nam Việt Nam 58 tuổi, mặt chữ điền rám nắng, nếp nhăn đuôi mắt, "
                           "lông mày rậm điểm bạc, tóc ngắn; áo thun ba lỗ trắng, khăn bông màu xám choàng kín vai. Luôn ngồi trên ghế nhựa ở giữa khung, mặt hướng ống kính; "
                           "CHỊ đứng ngay sau lưng chú, hơi lệch phải. Không đổi trang phục.\n"
                           "- ĐẠO CỤ thêm vào bối cảnh ảnh 1: một ghế nhựa có tựa, một thau nước và ca nhựa, một gương tay, một khăn bông xám; CHỊ mang găng nilon đen khi gội.")
        v["shots"][0]["end"] = "chị đặt chai xuống nền cạnh chân ghế, nhãn hướng máy; đầu chú phủ dung dịch nâu từng mảng, còn lộ tóc bạc hai bên"
        for s in v["shots"]:
            s["act"] = s["act"].replace("gương tay viền xanh", "gương tay").replace("ca nhựa xanh", "ca nhựa")
            s["end"] = s["end"].replace("ca nhựa xanh", "ca nhựa")


LUAT_TU_CHAY = """## LUẬT TỰ CHẠY (bắt buộc, áp dụng cho MỌI shot và mọi bước, không được hỏi lại tôi)
1. Lỗi kỹ thuật (máy chủ tự ngắt giữa chừng, pipeline lỗi, hết thời gian chờ, tải lên thất bại, tab treo; KHÔNG phải bị từ chối nội dung): tự thử lại shot hoặc bước đó ngay, tối đa 3 lần, giữ nguyên lời thoại và bối cảnh. Sau đó LÀM TIẾP các shot còn lại, ghép video và giao. Không dừng lại hỏi anh có muốn làm tiếp không.
2. Nếu một shot vẫn hỏng sau 3 lần thử: ghi vào mục chưa đạt, làm nốt các shot còn lại, ghép những shot đã có và giao kèm lý do. Không dừng chờ tôi.
3. Nếu công cụ tạo video từ chối một shot: tự đổi sang cách minh họa nhẹ nhàng hơn cho đúng shot đó (giữ nguyên 100% lời thoại và ý nghĩa; ví dụ chỉ tay vào vị trí, làm mẫu trên cổ tay hoặc bàn tay, hoặc nhân vật nói trực diện), tạo lại tối đa 2 lần. Vẫn bị từ chối thì dùng cảnh nhân vật nói trực diện với đúng lời thoại shot đó. Sau đó làm tiếp và ghép đủ, ghi lại thay đổi vào báo cáo.
4. KIỂM CHỨNG NỘI DUNG: nếu thấy lời thoại có thông tin sức khoẻ/công dụng chưa chuẩn thì tự sửa cho đúng theo nguồn uy tín và làm tiếp, không dừng lại chờ duyệt; ghi các chỗ đã sửa vào cuối.
5. KHÔNG BAO GIỜ dừng lại hỏi tôi hay đưa ra các lựa chọn để tôi chọn. Có nhiều phương án thì tự chọn phương án an toàn và giữ đủ lời thoại nhất, làm luôn, ghi quyết định vào cuối báo cáo. Chỉ kết thúc khi đã giao video ghép hoàn chỉnh.
6. Báo cáo cuối gồm: video ghép và từng shot; chỗ đã thử lại do lỗi kỹ thuật (shot nào, mấy lần); chỗ đã tự sửa lời thoại (câu cũ, câu mới, nguồn); chỗ chưa đạt (nếu có)."""


def lines_block(v):
    out = []
    for i, s in enumerate(v["shots"], 1):
        for ln in s["lines"]:
            who, txt = ("Chú Tư", ln[len("CHÚ TƯ: "):]) if ln.startswith("CHÚ TƯ: ") else ("Chị", ln)
            assert txt in s["act"], (v["slug"], i, txt)
            out.append(f'  - Shot {i} – {who}: "{txt}"')
    return "\n".join(out)


def make_prompt(v):
    n = len(v["shots"])
    total = n * 10
    two = bool(v.get("extra_char"))
    shots = "\n".join(
        f"- **Shot {i} ({(i-1)*10}–{i*10}s):** {s['act']} Khung cuối: {s['end']}."
        for i, s in enumerate(v["shots"], 1))
    nhan_vat_anh = ("   - CHỊ và CHÚ TƯ đúng mô tả ở mục 2, cùng trong khung, nhìn gần chính diện, thấy rõ TOÀN BỘ khuôn mặt cả hai; mái tóc chú Tư ở trạng thái BAN ĐẦU: khô, bạc trắng khoảng 70%."
                    if two else
                    "   - CHỊ đúng mô tả ở mục 2, nhìn thẳng ống kính, thấy rõ TOÀN BỘ khuôn mặt (mắt, mũi, miệng, lông mày), mỉm cười tự tin, không che mặt.")
    bien_doi = (v["bien_doi"] + "\n") if two else ""
    extra = (v["extra_char"] + "\n") if two else ""
    kiem_tra_them = "trạng thái mái tóc chú Tư đúng diễn biến (không đột ngột), " if two else ""
    noi_tiep = " và **trạng thái mái tóc chú Tư**" if two else ""
    return f"""# MASTER PROMPT cho Muse: Chị Giang review – {v['ten']} – "{v['tieu_de']}"
Ảnh đã đính kèm: **ảnh 1 = nhân vật trong bối cảnh** (ảnh Chị Giang do bạn chọn: quyết định gương mặt, trang phục, không gian), **ảnh 2 = ảnh sản phẩm** (`anh-san-pham/01.png`). Prompt dùng thẳng hai ảnh này, không tạo ảnh mới, không mô tả lại nhân vật hay bối cảnh.
Hộp hook khi dựng hậu kỳ (hộp magenta, chữ trắng in hoa, 2 dòng, tĩnh 0–7s, đặt dưới cằm): **"{v['hook_card'][0]}" / "{v['hook_card'][1]}"**. Thời lượng: **{total} giây ({n} shot)**, 9:16.

---

⚠️ XƯNG HÔ: nhân vật KHÔNG được xưng hay được gọi là "bác sĩ", "dược sĩ", "chuyên gia". Nhân vật xưng "Giang", gọi người xem là "anh", "mấy anh".
⚠️ NỘI DUNG: review chia sẻ trải nghiệm và thông tin trên nhãn; không hứa chữa khỏi bệnh, không nói sản phẩm thay thuốc, không hình ảnh gợi dục, không so sánh với nhãn hàng khác.

Bạn là đạo diễn kiêm dựng phim. Hãy tự làm trọn một video review sản phẩm dọc 9:16, dài {total} giây, theo quy trình và luật dưới đây. Tôi ĐÃ ĐÍNH KÈM sẵn ảnh 1 (nhân vật CHỊ trong bối cảnh) và ảnh 2 (sản phẩm): dùng trực tiếp hai ảnh này để tạo video luôn, KHÔNG tạo thêm bất kỳ ảnh tĩnh nào, KHÔNG tự nghĩ ra nhân vật, trang phục hay bối cảnh khác. Làm theo thứ tự: (3) in bảng shot → (4) tạo từng shot → ghép thành 1 video. Không hỏi lại tôi giữa chừng; nếu gặp lỗi thì tự thử lại và làm tiếp.

{LUAT_TU_CHAY}

## 0. ẢNH ĐÍNH KÈM (dùng trực tiếp, không tạo ảnh mới)
1. Ảnh 1 = CHỊ trong bối cảnh. Lấy NGUYÊN từ ảnh này: gương mặt, tuổi, kiểu tóc, trang phục, phụ kiện, không gian xung quanh, ánh sáng và góc máy. Giữ y hệt ở mọi shot.
2. Ảnh 2 = {v['ten']} ({v['nhan_dang']}). Sản phẩm trong video phải GIỐNG HỆT ảnh 2: màu, hình dáng, chữ trên nhãn. Chỉ lấy SẢN PHẨM từ ảnh 2, bỏ nền và chữ quảng cáo xung quanh.
3. MỌI shot video BẮT BUỘC đính kèm ảnh 1 + ảnh 2. Không được thay bằng một người khác, không đổi trang phục, không đổi bối cảnh.

## 1. NỘI DUNG
- Sản phẩm: {v['ten']}, ảnh đính kèm số 2.
- Người xem: nam giới 45–65 tuổi, miền Nam.
- VẤN ĐỀ đánh thẳng: {v['van_de']}
- GIẢI PHÁP: {v['giai_phap']}
- KẾT QUẢ nói đúng mức: {v['ket_qua']}
- Diễn biến bắt buộc theo thứ tự: [HOOK 5 giây đầu, sản phẩm đã trong tay, gọi đúng nỗi khổ → khoét sâu vấn đề → đưa sản phẩm ra review (là gì, có gì) → cách dùng + kết quả → dặn dò trung thực + kêu gọi xem bình luận, sản phẩm rõ nhãn trong khung].
- Lời thoại (nói ĐÚNG từng chữ, đúng thứ tự, tiếng Việt giọng miền Nam). Ngoài các câu này KHÔNG có lời nào khác:
{lines_block(v)}

## 2. KHỐI ĐỒNG NHẤT (chép y nguyên vào đầu prompt của MỌI shot)
- NHÂN VẬT CHỊ, TRANG PHỤC, BỐI CẢNH: đúng y như ảnh 1 đính kèm, không đổi ở bất kỳ shot nào.
{extra}- SẢN PHẨM: đúng ảnh 2. {v['san_pham']}. Không vẽ lại thành sản phẩm hay bao bì khác; chữ trên nhãn giữ đúng chính tả tiếng Việt có dấu.
{bien_doi}- PHONG CÁCH: như video quay thật bằng điện thoại dựng trên chân máy, giữ đúng khung hình và góc máy của ảnh 1, nhân vật nhìn thẳng ống kính, máy gần như đứng yên, rung rất nhẹ tự nhiên. Biểu cảm sinh động: nhướn mày, mắt tròn, cười lộ răng, nghiêng đầu, gật đầu. Hành động theo tốc độ người thật. Không tua nhanh. Mỗi shot là MỘT cú máy liền, không đổi góc bên trong shot. Âm thanh thật, nhẹ, phù hợp với bối cảnh trong ảnh 1. Không nhạc, không chữ, không phụ đề, không logo kênh. Mặt người nói luôn nhìn thấy rõ khi nói.
- GIỌNG: Chị: nữ miền Nam khoảng 30 tuổi, trong, ấm, tự tin, nhanh vừa, hóm hỉnh, thân tình như em gái nói chuyện với anh trai.{v.get('giong_them', '')} Mỗi người giữ đúng một giọng cho mọi shot. Khẩu hình khớp lời.

## 3. LUẬT CHIA SHOT (tự làm trước khi tạo video)
1. Chia video thành {n} shot, mỗi shot đúng 10 giây, tổng {total} giây.
2. **HOOK 5 GIÂY ĐẦU:** {v['hook_luat']}. Trong 5 giây đầu phải nghe trọn câu gọi đúng nỗi khổ của người xem và thấy rõ sản phẩm.
3. Mỗi shot chỉ có MỘT hành động chính, tối đa 2–3 động tác nhỏ liền nhau.
4. Lời thoại đúng từng chữ như mục 1; nói thong thả cho vừa 10 giây, nếu dư thời gian thì thêm biểu cảm, gật đầu, KHÔNG thêm lời khác.
5. Lời thoại và hành động phải khớp nhau đúng giây.
6. Shot cuối: dặn dò trung thực + câu kêu gọi xem bình luận; {v['ten']} nằm rõ trong khung, nhãn hướng về ống kính.
7. Mỗi shot ghi rõ: góc máy, mốc giây, động tác chi tiết, trạng thái đầu và cuối shot, lời thoại, và KHUNG CUỐI (mô tả khung hình kết thúc để shot sau nối vào).

Phân shot {total} giây:
{shots}

Trước khi tạo video, hãy in ra bảng phân shot (shot, giây, hành động, trạng thái, lời, khung cuối) rồi tự bắt đầu làm luôn, không chờ tôi duyệt.

## 4. QUY TRÌNH TẠO (lặp cho từng shot)
1. Shot 1: tạo video trực tiếp từ KHỐI ĐỒNG NHẤT, mô tả shot 1, ảnh 1 (mặt) và ảnh 2 (sản phẩm); nhân vật trong shot 1 phải là đúng người trong ảnh 1.
2. Từ shot 2 trở đi: lấy KHUNG HÌNH CUỐI của video shot trước làm khung khởi đầu, luôn kèm ảnh 1 (mặt) và ảnh 2 (sản phẩm), dán lại KHỐI ĐỒNG NHẤT và mô tả shot mới. Khung đầu của shot mới phải trùng bố cục, ánh sáng, bối cảnh{noi_tiep} với khung cuối shot trước.
3. Sau mỗi shot, tự kiểm tra: gương mặt, trang phục và bối cảnh (so với ảnh 1), sản phẩm ({v['nhan_dang']}), {kiem_tra_them}lời thoại đúng từng chữ và khớp miệng; nhân vật KHÔNG xưng bác sĩ. Nếu sai điểm nào thì tự tạo lại shot đó (tối đa 2 lần) trước khi sang shot tiếp.
4. Làm xong tất cả các shot thì ghép theo thứ tự thành một video, cắt nối thẳng (không hiệu ứng chuyển cảnh), giữ nguyên âm thanh từng shot. KHÔNG tự vẽ chữ, băng tiêu đề hay phụ đề lên video.
5. Gửi tôi: video ghép hoàn chỉnh, từng shot lẻ, và danh sách các chỗ bạn đã tự làm lại.
"""


def make_info(v):
    i = v["info"]
    imgs = sorted(os.listdir(os.path.join(ROOT, v["slug"], "anh-san-pham")))
    cd = "\n".join(f"- {x}" for x in i["cong_dung"])
    return f"""# {v['ten']} – thông tin sản phẩm

Nguồn: KaloData (TikTok Shop Việt Nam), số liệu 90 ngày tính đến 13/10/2026.

- **Tên trên sàn:** {i['ten_day_du']}
- **Mã sản phẩm TikTok Shop:** {i['pid']} — https://shop.tiktok.com/view/product/{i['pid']}?region=VN
- **Giá:** {i['gia']}
- **Lượt bán:** {i['ban']}
- **Hoa hồng affiliate:** {i['hh']}
- **Đánh giá:** {i['danh_gia']} · {i['ngay']}

## Công dụng (theo nhà bán công bố)
{cd}

## Thành phần
{i['thanh_phan']}

## Cách dùng
{i['cach_dung']}

## Lưu ý khi làm nội dung
{i['luu_y']}

## Người mua nói gì
{i['review']}

## Bao bì (để đối chiếu khi AI vẽ)
{i['bao_bi']}

## Ảnh thật đã tải ({len(imgs)} ảnh, thư mục `anh-san-pham/`)
{chr(10).join(f"- anh-san-pham/{x}" for x in imgs)}

Dữ liệu gốc: `kalodata.json`. Master prompt: `prompt-{v['slug'][3:]}.md`.
"""


def make_overview():
    out = ["# 6 kịch bản review – kênh Chị Giang Hiểu Chuyện",
           "",
           "Người xem: nam 45–65 tuổi, miền Nam. Chị Giang xưng \"Giang\", gọi \"anh / mấy anh\". Mỗi video 50 giây (5 shot × 10s), 9:16.",
           "Khung chung: HOOK 5 giây (sản phẩm đã trong tay) → khoét vấn đề → review sản phẩm → cách dùng + kết quả → dặn dò thật + \"Giang để ở bình luận\".",
           ""]
    for n, v in enumerate(V, 1):
        out += [f"## {n}. {v['ten']} — \"{v['tieu_de']}\"", "",
                f"- **Hộp hook:** {v['hook_card'][0]} / {v['hook_card'][1]}",
                f"- **Vấn đề:** {v['van_de']}",
                f"- **Giải pháp:** {v['giai_phap']}",
                f"- **Kết quả:** {v['ket_qua']}",
                "- **Nhân vật, trang phục, bối cảnh:** theo ảnh 1 đính kèm khi chạy Muse",
                f"- **File:** `{v['slug']}/prompt-{v['slug'][3:]}.md` · `{v['slug']}/thong-tin-san-pham.md` · `{v['slug']}/anh-san-pham/`",
                "", "| Giây | Lời thoại |", "|---|---|"]
        for i, s in enumerate(v["shots"], 1):
            txt = " ".join((f"*(Chú Tư)* {l[8:]}" if l.startswith("CHÚ TƯ: ") else l) for l in s["lines"])
            out.append(f"| {(i-1)*10}–{i*10}s | {txt} |")
        out.append("")
    return "\n".join(out)


for v in V:
    d = os.path.join(ROOT, v["slug"])
    p = make_prompt(v)
    assert "{" not in p and "}" not in p, v["slug"]
    open(os.path.join(d, f"prompt-{v['slug'][3:]}.md"), "w", encoding="utf-8").write(p)
    open(os.path.join(d, "thong-tin-san-pham.md"), "w", encoding="utf-8").write(make_info(v))
    for i, s in enumerate(v["shots"], 1):
        n = sum(len(l.replace("CHÚ TƯ: ", "").split()) for l in s["lines"])
        print(v["slug"], "shot", i, "so tieng:", n, "!!" if n > 34 else "")
open(os.path.join(ROOT, "kich-ban-6-video.md"), "w", encoding="utf-8").write(make_overview())
print("OK")
