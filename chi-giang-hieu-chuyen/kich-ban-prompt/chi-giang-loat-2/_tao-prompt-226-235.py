# Sinh master prompt 70s cho loạt "Các anh ơi" (226–235): Giang thủ thỉ với đàn ông tuổi 40+.
# Khác loạt trước: xưng "Giang", gọi "các anh"; giọng nhẹ, ngọt; không vai phụ, không giấy note.
# Chạy: PYTHONUTF8=1 python _tao-prompt-226-235.py
import os

SO = ["một", "hai", "ba", "bốn", "năm", "sáu", "bảy"]

# slug, băng chữ, câu hook (nói sau "Các anh ơi…"), sự thật mở đầu, [(ý, giải thích)], chốt
def T(slug, title, hook, fact, pts, close):
    return (slug, title, hook, fact, pts, close)

TOPICS = [
    T("226-vo-thich-duoc-om-kieu-nao", "Vợ thích được ôm kiểu nào nhất?",
      "vợ thích được ôm kiểu nào nhất, các anh biết hông?",
      "Ôm liền trên hai chục giây là cơ thể tiết ra chất làm hai người thấy gắn bó đó các anh.",
      [("Ôm từ phía sau lúc vợ đang nấu ăn.", "Kiểu nhiều chị mê nhất."),
       ("Ôm cho lâu.", "Đừng ôm cái rồi buông liền."),
       ("Ôm mà không đòi gì tiếp theo.", "Vợ mới thấy được thương thật."),
       ("Ôm lúc vợ buồn, vợ mệt.", "Khỏi cần nói gì hết."),
       ("Ôm vợ trước khi ngủ.", "Dù chỉ năm phút.")],
      "Ôm vợ mỗi ngày là cách giữ lửa rẻ nhất mà hiệu quả nhất đó anh!"),
    T("227-vo-lanh-chan-kho-toi", "Vì sao vợ lạnh chân thì khó 'tới'?",
      "các anh có tin là đôi chân lạnh làm vợ khó 'tới' hông?",
      "Có nghiên cứu ở Hà Lan, chỉ cần mang vớ ấm, tỉ lệ lên đỉnh tăng từ khoảng một nửa lên tám phần mười.",
      [("Người lạnh thì khó thả lỏng.", "Không thả lỏng thì khó tới."),
       ("Phòng máy lạnh vừa phải thôi.", "Đắp chăn ấm cho vợ."),
       ("Ủ chân vợ bằng tay mình.", "Vừa ấm vừa tình."),
       ("Tắm nước ấm trước khi lên giường.", "Người ấm, mạch máu giãn."),
       ("Vợ hay lạnh tay chân quanh năm.", "Thì nên kiểm tra thiếu máu, tuyến giáp.")],
      "Ấm chân vợ là ấm luôn chuyện vợ chồng đó các anh!"),
    T("228-phu-viec-nha-vo-de-chiu", "Chồng phụ việc nhà, vợ 'dễ chịu' hơn thật không?",
      "phụ vợ rửa chén mà tối được thưởng, các anh tin hông?",
      "Lý do số một làm vợ không có hứng là mệt, chứ không phải là hết thương đâu anh.",
      [("Vợ còn việc là đầu vợ chưa nghỉ.", "Người nằm đó mà đầu đang đi phơi đồ."),
       ("Rửa chén, giặt đồ, kèm con học.", "Chọn một việc nhận luôn."),
       ("Làm mà không cần vợ nhắc.", "Đó mới là điểm cộng."),
       ("Đừng làm kiểu trả bài rồi đòi thưởng.", "Vợ thấy liền."),
       ("Vợ được nghỉ sớm một tiếng.", "Là vợ có sức thương anh.")],
      "Muốn vợ có sức thì chia bớt việc cho vợ nha các anh!"),
    T("229-ghen-mot-chut-co-nong-hon", "Ghen một chút có làm vợ chồng 'nồng' hơn?",
      "ghen một chút có làm vợ chồng 'nồng' hơn hông ta?",
      "Một chút ghen nhẹ nhắc mình là người kia vẫn còn quý giá lắm đó các anh.",
      [("Vợ ghen là vợ còn thương.", "Dỗ vợ chứ đừng cãi."),
       ("Cố tình chọc cho vợ ghen.", "Là phản tác dụng."),
       ("Đừng lấy ghen để thử lòng.", "Mất lòng tin thì khó gỡ."),
       ("Ghen tới mức kiểm soát điện thoại, đi đâu.", "Là ghen độc rồi."),
       ("Thấy vợ đẹp lên, được người khen.", "Thì anh chăm vợ hơn chứ đừng cấm.")],
      "Ghen như muối, bỏ một chút thì đậm, bỏ nhiều là mặn chát đó anh!"),
    T("230-vo-co-tu-xu-khong", "Vợ có 'tự xử' không, anh có nên buồn?",
      "các anh có bao giờ thắc mắc vợ có 'tự xử' hông?",
      "Khảo sát cho thấy nhiều phụ nữ có chồng vẫn có lúc tự xử, chuyện này bình thường lắm.",
      [("Không có nghĩa là vợ chê anh.", "Hai chuyện khác nhau."),
       ("Có khi chỉ để giải tỏa, dễ ngủ.", "Giống các anh thôi."),
       ("Nhờ vậy vợ hiểu cơ thể mình.", "Rồi chỉ lại cho anh."),
       ("Lỡ biết thì đừng tra hỏi, đừng chọc.", "Vợ xấu hổ lắm."),
       ("Vợ né anh hoàn toàn.", "Thì mới cần nói chuyện với nhau.")],
      "Vợ hiểu mình thì vợ chồng càng hiểu nhau, đừng buồn nha các anh!"),
    T("231-vo-thay-do-truoc-mat-anh", "Vợ thay đồ trước mặt anh, là có ý gì?",
      "vợ thay đồ ngay trước mặt mình, là vô tình hay cố ý vậy ta?",
      "Có khi chỉ là thay đồ, có khi là một tín hiệu, các anh phải đọc cho tinh.",
      [("Vợ thay đồ ngủ đẹp hơn mọi hôm.", "Là tín hiệu khá rõ."),
       ("Vợ chậm rãi, liếc nhìn anh.", "Là đang chờ anh lên tiếng."),
       ("Khen nhẹ một câu.", "Đừng nhìn chằm chằm."),
       ("Tuyệt đối đừng chê bụng, chê đùi.", "Lần sau vợ vô nhà tắm thay luôn."),
       ("Không chắc thì hỏi khéo.", "'Tối nay em đẹp quá nha'.")],
      "Vợ còn thay đồ trước mặt anh là vợ còn tin anh lắm đó!"),
    T("232-long-cho-do-bac-thua", "Lông 'chỗ đó' bạc, thưa dần, có sao không?",
      "dưới đó cũng có sợi bạc, các anh thấy chưa?",
      "Lông ở đâu thì cũng bạc theo tuổi giống như tóc vậy đó các anh.",
      [("Bạc là bình thường.", "Thường bạc sau tóc vài năm."),
       ("Thưa dần do nội tiết giảm theo tuổi.", "Không phải bệnh."),
       ("Rụng nhiều đột ngột, kèm mệt, giảm ham muốn.", "Thì kiểm tra nội tiết, tuyến giáp."),
       ("Đừng nhổ sợi bạc.", "Dễ viêm nang lông, đau lắm."),
       ("Tỉa gọn cho sạch sẽ.", "Vợ cũng thích hơn.")],
      "Bạc chút đỉnh mà phong độ còn là được nha các anh!"),
    T("233-trung-vit-lon-co-bo-that", "Trứng vịt lộn, nước dừa có 'bổ' thật không?",
      "trứng vịt lộn với nước dừa có 'bổ' như lời đồn hông?",
      "Trứng vịt lộn bổ thật, nhưng bổ cho cơ thể, chứ không phải thần dược cho chuyện ấy đâu.",
      [("Nhiều đạm, nhiều sắt.", "Tốt cho người đang mệt, thiếu máu."),
       ("Nhưng lại rất nhiều cholesterol.", "Mỡ máu cao thì một tuần một hai trứng thôi."),
       ("Ăn kèm rau răm, gừng.", "Cho dễ tiêu."),
       ("Nước dừa bù nước, bù khoáng.", "Không làm tăng bản lĩnh."),
       ("Người bệnh thận nên hạn chế nước dừa.", "Vì nhiều kali.")],
      "Ăn cho ngon miệng thì được, muốn sung thì vẫn phải ngủ đủ, tập đều nha anh!"),
    T("234-nhin-mat-vo-bon-phut", "Nhìn vào mắt vợ bốn phút, chuyện gì xảy ra?",
      "lần cuối các anh nhìn vào mắt vợ lâu lâu là hồi nào?",
      "Có một thí nghiệm nổi tiếng: hai người nhìn mắt nhau bốn phút thì thấy gần nhau hơn hẳn.",
      [("Vợ chồng lâu năm gần như không nhìn mắt nhau.", "Toàn nhìn điện thoại."),
       ("Phút đầu sẽ ngượng, sẽ cười.", "Cứ cười."),
       ("Tắt điện thoại, tắt ti vi.", "Ngồi đối diện vợ."),
       ("Nắm tay vợ trong lúc nhìn.", "Không cần nói gì."),
       ("Xong rồi nói một điều cảm ơn vợ.", "Vợ nhớ cả tuần.")],
      "Tối nay thử bốn phút thôi, rồi kể Giang nghe nha các anh!"),
    T("235-vo-thich-duoc-khen-gi", "Vợ thích được chồng khen gì nhất?",
      "vợ thích được khen cái gì nhất, các anh đoán trúng hông?",
      "Nhiều chị nói câu khen họ nhớ lâu nhất không phải là khen đẹp đâu các anh.",
      [("Khen công sức.", "'Em lo cho nhà này giỏi quá'."),
       ("Khen cụ thể.", "'Món canh bữa nay ngon' hơn là 'ngon'."),
       ("Khen trước mặt người khác.", "Vợ nở mũi cả tháng."),
       ("Khen đẹp cả khi vợ không trang điểm.", "Mới là thật lòng."),
       ("Đừng khen xong thêm chữ 'nhưng'.", "Một chữ 'nhưng' xóa hết câu khen.")],
      "Một lời khen mỗi ngày là vợ đẹp lên mỗi ngày đó anh!"),
]

CTA = "Anh nào còn thắc mắc thầm kín thì bình luận nha, video sau Giang trả lời riêng cho anh!"

HEAD = """# MASTER PROMPT cho Muse: "Các anh ơi" – {title}
Đính kèm ảnh 1 = `nhan-vat-chi.png` (cùng thư mục).
Băng chữ đỏ khi dựng: **"{title}"** (cả video, chữ trắng nền đỏ bo góc, ~1/4 trên màn hình). Thời lượng: **{dur} giây ({shots} shot)**.

---

⚠️ XƯNG HÔ: nhân vật xưng "Giang", gọi người xem là "các anh" hoặc "anh". KHÔNG xưng "chị", KHÔNG gọi người xem là "em". KHÔNG được xưng hay được gọi là "bác sĩ", "dược sĩ", "chuyên gia". Không ống nghe, không bảng tên, không áo blouse trắng.
⚠️ GIỌNG ĐIỆU: nhẹ nhàng, ngọt, thủ thỉ như đang nói nhỏ chuyện riêng với người thân; chậm rãi, có ngắt nghỉ, hay cười mỉm. Duyên dáng nhưng đứng đắn: không õng ẹo, không khêu gợi, không đổi trang phục.
⚠️ NỘI DUNG: nói kiểu chia sẻ kiến thức vợ chồng, không tục, không mô tả hành vi chi tiết, không hình ảnh gợi dục, không hứa chữa khỏi.

Bạn là đạo diễn kiêm dựng phim. Hãy tự làm trọn một video dọc 9:16, dài {dur} giây, dạng Giang thủ thỉ chia sẻ với các anh, theo quy trình và luật dưới đây. Làm theo thứ tự: (0) tạo và gửi ẢNH NHÂN VẬT CHUẨN → (3) in bảng shot → (4) tạo từng shot → ghép thành 1 video. Không hỏi lại tôi giữa chừng; nếu gặp lỗi thì tự thử lại và làm tiếp.

⚠️ VIỆC ĐẦU TIÊN, BẮT BUỘC: tạo ẢNH NHÂN VẬT CHUẨN (mục 0) và gửi vào chat. CHƯA có ảnh này thì KHÔNG in bảng shot, KHÔNG tạo video.

## 0. ẢNH NHÂN VẬT CHUẨN – LÀM ĐẦU TIÊN
1. Dựa trên ảnh 1 (đính kèm), tạo ẢNH tĩnh dọc 9:16 như ảnh chụp điện thoại thật, trong BỐI CẢNH mục 2:
   - GIANG: nhìn thẳng ống kính, thấy rõ toàn bộ mặt, mỉm cười dịu dàng, áo scrubs xanh ngọc cổ chữ V, tóc nâu đen dài xõa, bông tai nụ nhỏ.
2. Tự kiểm tra: giống 100% gương mặt ảnh 1 (mắt, mũi, môi, lông mày, màu da); trang phục đúng. Sai thì tạo lại (tối đa 2 lần).
3. GỬI ảnh vào chat với dòng "ẢNH NHÂN VẬT CHUẨN". Mọi shot sau dùng ảnh này.
4. Không chờ tôi duyệt: gửi xong tự làm tiếp mục 3 và 4.

## 1. NỘI DUNG
- Chủ đề: {title}
- Khung bắt buộc: gọi "Các anh ơi" + câu hỏi gây tò mò ngay giây đầu → một sự thật bất ngờ → Giang nói trước "có {n} điều" → mỗi ý một shot (giơ số ngón + giải thích) → câu chốt + CTA.
- Lời thoại (nói ĐÚNG từng chữ, tiếng Việt, giọng miền Nam nhẹ nhàng, thủ thỉ):
{lines}

## 2. KHỐI ĐỒNG NHẤT (chép y nguyên vào đầu prompt của MỌI shot)
- NHÂN VẬT GIANG: đúng người trong ẢNH NHÂN VẬT CHUẨN. Phụ nữ châu Á khoảng 30 tuổi, mặt trái xoan, da sáng hồng, mắt nâu, lông mày nâu đậm tự nhiên, môi hồng đất; tóc nâu đen dài quá vai, rẽ ngôi lệch, gợn sóng nhẹ; bông tai nụ bạc nhỏ; áo scrubs xanh ngọc cổ chữ V, túi ngực trái. Không đổi trang phục, kiểu tóc ở bất kỳ shot nào.
- BỐI CẢNH: quầy mỹ phẩm thảo dược sáng sủa: kệ gỗ sáng có đèn LED ấm, chai lọ trắng–xanh lá, hộp giấy xanh, dây trầu bà rủ, bình hoa cúc vàng nhỏ, lọ thủy tinh thảo mộc khô bên trái; cửa kính lớn phía sau ra đường có cây xanh, ánh sáng ban ngày. Giữ nguyên bố cục kệ giữa các shot.
- ĐẠO CỤ: cốc sứ trắng đặt trên quầy.
- PHONG CÁCH: như tự quay bằng camera trước điện thoại dựng trên chân, khung ngang ngực, mặt ở 1/3 trên, nhìn thẳng ống kính. Máy gần như đứng yên. Biểu cảm dịu dàng, ấm áp: cười mỉm, ánh mắt trìu mến, nghiêng đầu nhẹ, gật đầu chậm, thỉnh thoảng hơi chồm người tới như nói nhỏ chuyện riêng. Mỗi shot thay đổi nhẹ tư thế (nghiêng người, tay xòe, tay đặt ngực) để không nhàm. Không tua nhanh. Mỗi shot MỘT cú máy liền. Âm thanh phòng yên tĩnh, KHÔNG nhạc, KHÔNG chữ, KHÔNG phụ đề, KHÔNG logo.
- GIỌNG: Giang: nữ miền Nam khoảng 30 tuổi, giọng ngọt, mềm, ấm, nói chậm vừa, thủ thỉ, có tiếng cười nhẹ trong giọng; giữ đúng một giọng cho mọi shot. Khẩu hình khớp lời.

## 3. LUẬT CHIA SHOT
1. Mỗi shot đúng 10 giây; {shots} shot, tổng {dur} giây.
2. HOOK 2 GIÂY ĐẦU: khung đầu tiên là GIANG đã chồm nhẹ về phía ống kính, một tay che hờ bên miệng như nói nhỏ, mắt cười, gọi "Các anh ơi…" ngay. Không chào hỏi, không giới thiệu.
3. Mỗi ý bắt đầu bằng số thứ tự, tay giơ đúng số ngón cạnh mặt (ý 5 xòe cả bàn tay).
4. Lời mỗi shot vừa đủ 10 giây nói thong thả; nếu thiếu thời gian thì thêm cười mỉm/gật đầu, KHÔNG thêm lời khác.
5. Mỗi shot ghi rõ: mốc giây, lời, động tác tay, biểu cảm, KHUNG CUỐI.

Phân shot {dur} giây:
{shotlist}

In bảng phân shot (shot, giây, lời, động tác, khung cuối) rồi tự làm luôn, không chờ duyệt.

## 4. QUY TRÌNH TẠO
1. Shot 1: tạo từ KHỐI ĐỒNG NHẤT + mô tả shot + ẢNH NHÂN VẬT CHUẨN.
2. Từ shot 2: lấy KHUNG CUỐI shot trước làm ảnh khởi đầu, luôn kèm ẢNH NHÂN VẬT CHUẨN, dán lại KHỐI ĐỒNG NHẤT. Khung đầu shot mới trùng bố cục, ánh sáng, kệ thảo dược với khung cuối shot trước.
3. Sau mỗi shot tự kiểm tra 5 điểm: gương mặt giống ảnh chuẩn, scrubs xanh ngọc, bối cảnh quầy thảo dược, số ngón tay đúng ý, lời đúng từng chữ và khớp miệng; xưng "Giang", gọi "các anh", KHÔNG xưng bác sĩ; giọng nhẹ nhàng. Sai thì làm lại (tối đa 2 lần).
4. Ghép theo thứ tự, cắt nối thẳng, giữ âm thanh từng shot.
5. BĂNG CHỮ HOOK (BẮT BUỘC, làm lúc ghép, KHÔNG để công cụ tạo video tự vẽ chữ): chèn đè lên TOÀN BỘ video ngay từ khung hình đầu tiên (0s đến hết) một băng chữ cố định: "{title}" – chữ trắng đậm, nền đỏ tươi bo góc, căn giữa, rộng khoảng 90% khung, đặt ở khoảng 1/4 trên màn hình, không che mặt. Đúng chính tả tiếng Việt có dấu. Video giao KHÔNG có băng chữ này là chưa đạt, phải ghép lại.
6. Gửi tôi: video ghép, từng shot lẻ, danh sách chỗ đã làm lại.
"""

here = os.path.dirname(os.path.abspath(__file__))
for slug, title, hook, fact, pts, close in TOPICS:
    n = SO[len(pts) - 1]
    shots = len(pts) + 2
    dur = shots * 10
    q = f"Các anh ơi… {hook}"
    intro = f"{fact} Có {n} điều, Giang nói nhỏ các anh nghe nè."
    lines = f'  - Giang (chồm tới, nói nhỏ): "{q}"\n  - Giang (ngồi thẳng lại, cười mỉm): "{intro}"\n'
    shotlist = [f'- Shot 1 (0–10s): 0–4s GIANG chồm nhẹ tới ống kính, tay che hờ bên miệng, thì thầm: "{q}" '
                f'4–10s ngồi thẳng lại, cười mỉm, nhìn thẳng máy: "{intro}" Khung cuối: Giang giơ tay chuẩn bị đếm.']
    for i, (h, ex) in enumerate(pts):
        lab = SO[i].capitalize()
        lines += f'  - Giang: "{lab}: {h} {ex}"\n'
        a, b = (i + 1) * 10, (i + 2) * 10
        shotlist.append(f'- Shot {i+2} ({a}–{b}s): giơ {i+1} ngón: "{lab}: {h} {ex}" Nói chậm, dịu, xòe tay giải thích. Khung cuối: Giang gật đầu nhẹ, tay hạ.')
    lines += f'  - Giang chốt: "{close} {CTA}"'
    shotlist.append(f'- Shot {shots} ({dur-10}–{dur}s): tay đặt nhẹ lên ngực, chốt: "{close}" Cười dịu nói CTA: "{CTA}" Nghiêng đầu, mỉm cười.')
    body = HEAD.format(title=title, dur=dur, shots=shots, n=n, lines=lines, shotlist="\n".join(shotlist))
    with open(os.path.join(here, f"prompt-{slug}.md"), "w", encoding="utf-8") as f:
        f.write(body)
    print(f"{slug}: {dur}s / {shots} shot")
