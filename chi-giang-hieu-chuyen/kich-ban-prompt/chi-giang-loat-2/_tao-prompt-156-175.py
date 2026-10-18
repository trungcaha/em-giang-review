# Sinh master prompt (60–90s) cho từng chủ đề "Chị ơi, cho em hỏi thầm". Chạy: python _tao-prompt.py
# Mỗi ý = 1 shot 10s. Tổng shot = 1 (hook) + số ý + 1 (chốt) → 5 ý = 70s, 6 ý = 80s, 7 ý = 90s.
import os

SO = ["một", "hai", "ba", "bốn", "năm", "sáu", "bảy"]

# slug, băng chữ, hook vai phụ (None = chị đọc giấy), câu đọc giấy, mở ý (con số/sự thật), [(ý, giải thích)], chốt
def T(slug, title, hook, card, fact, pts, close):
    return (slug, title, hook, card, fact, pts, close)

TOPICS = [
    T("156-quan-he-cua-sau", "Đi 'cửa sau' có hại gì không?",
      None, "Em hỏi: vợ chồng em tò mò muốn thử đi 'cửa sau', có hại gì không chị?",
      "Chỗ đó không tự tiết chất nhờn, lớp lót bên trong lại mỏng hơn 'cửa trước' nhiều đó em.",
      [("Rất dễ trầy, rách, chảy máu.", "Nên phải thiệt chậm và thiệt nhiều gel."),
       ("Nguy cơ lây bệnh cao nhất trong các kiểu.", "Bắt buộc phải dùng bao."),
       ("Từ sau ra trước là phải thay bao.", "Không thì vợ dễ viêm nhiễm."),
       ("Làm thô bạo lâu ngày hại cơ giữ.", "Về già khó nhịn đi cầu."),
       ("Vợ không thích thì dừng.", "Đau hay chảy máu cũng dừng liền.")],
      "Tò mò thì được, mà phải an toàn và cả hai cùng chịu em nhé!"),
    T("157-gay-cau-nho", "'Cậu nhỏ' không có xương mà sao vẫn gãy?",
      "Chị ơi… tối qua đang gần nhau, em nghe cái 'rắc', chồng em la làng rồi ôm bụng luôn!", None,
      "Không có xương, nhưng có một lớp vỏ dai bọc bên ngoài, căng quá là rách cái 'rắc' đó em.",
      [("Nghe 'rắc', đau nhói rồi xìu liền.", "Sau đó sưng bầm tím như trái cà."),
       ("Hay bị nhất là lúc trượt ra rồi thúc trật.", "Đụng mạnh vô xương của vợ."),
       ("Vợ ở trên hoặc từ phía sau là dễ bị hơn.", "Nên đừng mạnh bạo quá."),
       ("Phải vô bệnh viện liền trong ngày.", "Mổ khâu sớm thì lành tốt."),
       ("Mắc cỡ để lâu là bị cong, bị yếu.", "Có khi yếu luôn.")],
      "Thương nhau thì từ từ, có ai rượt đâu mà gấp em nhé!"),
    T("158-yeu-bang-mieng", "'Yêu' bằng miệng có lây bệnh không?",
      None, "Em hỏi: 'yêu' bằng miệng thì có lây bệnh gì không, hay vậy là an toàn hả chị?",
      "Nhiều người tưởng vậy là an toàn tuyệt đối, mà không phải đâu em.",
      [("Lậu, giang mai, mụn rộp đều lây được.", "Qua đường miệng luôn."),
       ("Vi rút H P V lây lên họng.", "Lâu năm có thể gây ung thư vùng họng."),
       ("Miệng đang lở, chảy máu chân răng.", "Thì nên tránh."),
       ("Thấy mụn, vết loét, mùi lạ ở vùng kín.", "Thì khoan đã, đi khám trước."),
       ("Một vợ một chồng thì nguy cơ rất thấp.", "Cứ vệ sinh sạch sẽ là được.")],
      "Chung thủy là lá chắn tốt nhất đó em!"),
    T("159-diem-g-co-that-khong", "Điểm G có thật không, nằm ở đâu?",
      None, "Em hỏi: em nghe nói phụ nữ có điểm G, em kiếm hoài không thấy, có thật không chị?",
      "Tới giờ giới khoa học vẫn còn cãi nhau là có hay không đó em.",
      [("Nó không phải cái nút bấm.", "Mà là một vùng nhạy cảm, không có ranh giới rõ."),
       ("Nằm ở thành phía trước, vô vài phân.", "Phía bụng chứ không phải phía lưng."),
       ("Không phải chị em nào cũng thấy thích ở đó.", "Không thấy cũng là bình thường."),
       ("Đa số phụ nữ nhạy ở bên ngoài hơn.", "Chỗ đó mới là công tắc chính."),
       ("Hỏi vợ là nhanh nhất.", "Vợ chỉ đâu mình theo đó.")],
      "Bản đồ kho báu nằm ở vợ mình chứ không phải trên mạng em nhé!"),
    T("160-tu-the-vo-de-len-dinh", "Kiểu nào dễ làm vợ 'lên đỉnh' nhất?",
      None, "Em hỏi: em đổi đủ kiểu mà vợ vẫn chưa tới, kiểu nào dễ làm vợ lên đỉnh nhất hả chị?",
      "Phần lớn phụ nữ không tới được nếu chỉ có mỗi chuyện 'ra vô' thôi đâu em.",
      [("Để vợ ở trên.", "Vợ tự chỉnh góc và nhịp theo ý mình."),
       ("Kê cái gối dưới hông vợ.", "Đổi góc một chút là khác liền."),
       ("Áp sát, chậm và đều.", "Hiệu quả hơn nhanh và mạnh."),
       ("Kết hợp thêm bàn tay.", "Đừng giao hết cho 'cậu nhỏ'."),
       ("Kiểu nào cũng phải dạo đầu cho đủ.", "Vợ chưa sẵn sàng thì kiểu gì cũng thua.")],
      "Không có kiểu thần thánh đâu, chỉ có ông chồng chịu để ý vợ thôi em!"),
    T("161-bao-nhieu-phut-la-dat", "Một 'trận' bao nhiêu phút là đạt?",
      None, "Em hỏi: em được chừng năm phút là xong, vậy là yếu hay bình thường hả chị?",
      "Người ta bấm giờ đàng hoàng thì trung bình chỉ khoảng năm phút rưỡi thôi đó em.",
      [("Từ ba tới bảy phút là đạt.", "Bảy tới mười ba phút là đẹp."),
       ("Trên phim là cắt ghép.", "Đừng lấy đó làm chuẩn."),
       ("Lâu quá vợ cũng khô, cũng rát.", "Không phải càng lâu càng hay."),
       ("Thường xuyên dưới một phút.", "Mới gọi là xuất sớm, nên đi khám."),
       ("Dạo đầu không tính giờ.", "Mà vợ lại chấm điểm ở khúc đó.")],
      "Vợ không bấm đồng hồ đâu, vợ chỉ nhớ mình có dịu dàng không thôi em!"),
    T("162-dao-dau-bao-lau", "Dạo đầu bao lâu thì vợ mới 'sẵn sàng'?",
      "Chị ơi… chồng em cứ leo lên là vô liền, em đau mà không dám nói!", None,
      "Đàn ông cần vài phút, còn phụ nữ thường cần mười tới hai mươi phút mới sẵn sàng.",
      [("Khô là chưa sẵn sàng.", "Vô lúc đó vợ chỉ thấy đau."),
       ("Dạo đầu bắt đầu từ ban ngày.", "Một câu nói ngọt, phụ rửa chén cũng tính."),
       ("Ôm, hôn, vuốt ve trước.", "Đừng nhắm thẳng mục tiêu."),
       ("Vợ sau năm mươi cần lâu hơn nữa.", "Và nên có thêm gel bôi trơn."),
       ("Xong rồi ôm vợ thêm vài phút.", "Đừng quay lưng ngủ liền.")],
      "Nấu nước còn phải chờ sôi, huống chi là vợ mình em nhé!"),
    T("163-co-vo-van-tu-xu", "Có vợ rồi mà vẫn 'tự xử', có sao không?",
      None, "Em hỏi: em có vợ rồi mà thỉnh thoảng vẫn tự xử, vậy có bệnh hoạn gì không chị?",
      "Rất nhiều đàn ông có vợ vẫn làm vậy, và đó không phải là bệnh đâu em.",
      [("Không hại thận, không mờ mắt.", "Mấy cái đó là lời đồn."),
       ("Vợ mệt, vợ bệnh, vợ đi xa.", "Thì đây là cách giải tỏa lành mạnh."),
       ("Có vấn đề là khi mình né vợ.", "Thích tự xử hơn gần vợ."),
       ("Nắm chặt quá, coi phim nhiều quá.", "Tới lúc gần vợ lại khó ra."),
       ("Ngày nào cũng phải có, bỏ bê công việc.", "Thì nên đi tư vấn.")],
      "Giải tỏa thì được, miễn đừng để vợ thành người dự bị em nhé!"),
    T("164-vo-chong-cung-xem-phim-nguoi-lon", "Vợ chồng cùng coi phim người lớn, nên không?",
      None, "Em hỏi: em muốn rủ vợ coi phim người lớn chung cho có hứng, có nên không chị?",
      "Có cặp coi chung thấy gần nhau hơn, có cặp coi xong lại cãi nhau đó em.",
      [("Phải là cả hai cùng thoải mái.", "Vợ không thích thì đừng ép."),
       ("Phim là diễn, là cắt ghép.", "Đừng lấy đó so với vợ mình."),
       ("Đừng bắt vợ làm y như phim.", "Nhiều cảnh ngoài đời làm là đau."),
       ("Không có phim là không lên.", "Thì là đang bị lệ thuộc rồi."),
       ("Nói thẳng mình thích gì.", "Còn hiệu quả hơn mở phim.")],
      "Phim hay nhất là phim hai vợ chồng tự đóng em nhé!"),
    T("165-chai-xit-keo-dai", "Chai xịt 'kéo dài' có hại không?",
      None, "Em hỏi: em tính mua chai xịt kéo dài thời gian, xài có hại gì không chị?",
      "Bên trong đa số là thuốc tê, xịt vô cho bớt nhạy nên lâu hơn đó em.",
      [("Có tác dụng thật.", "Bác sĩ cũng có dùng loại này."),
       ("Xịt nhiều quá là tê cứng.", "Mất cảm giác rồi xìu luôn."),
       ("Xịt xong chờ mười phút rồi lau sạch.", "Không thì vợ cũng bị tê theo."),
       ("Thấy đỏ, rát, ngứa là ngưng.", "Có người bị dị ứng."),
       ("Hàng trôi nổi không biết trộn gì.", "Nên mua ở nhà thuốc đàng hoàng.")],
      "Xịt là chữa cháy thôi, bị hoài thì đi khám cho tới gốc em nhé!"),
    T("166-cay-bi-bom-to", "Cấy bi, bơm cho to 'cậu nhỏ', có nên không?",
      None, "Em hỏi: bạn nhậu rủ em đi cấy bi, bơm cho to để vợ mê, có nên không chị?",
      "Bệnh viện nam khoa năm nào cũng mổ cấp cứu cho các anh tự đi bơm, đi cấy đó em.",
      [("Bơm silicon, mỡ, dầu là nguy hiểm nhất.", "Sưng, lở loét, có khi hoại tử."),
       ("Cấy bi ở tiệm dễ nhiễm trùng.", "Dụng cụ không vô khuẩn."),
       ("Vợ không mê như lời đồn.", "Nhiều chị bị trầy, đau, sợ luôn."),
       ("Kích cỡ đàn ông Việt mình là đủ dùng.", "Vợ cần dịu dàng chứ không cần to."),
       ("Lỡ làm rồi mà sưng, đau, đổi màu.", "Thì vô bệnh viện liền, đừng mắc cỡ.")],
      "Đồ zin là đồ quý nhất, đừng độ chế em nhé!"),
    T("167-gan-nhau-duoi-nuoc", "'Gần' nhau trong bồn tắm, hồ bơi, biển có sao không?",
      None, "Em hỏi: vợ chồng em đi nghỉ mát, tính thử trong bồn tắm cho lãng mạn, có sao không chị?",
      "Ở dưới nước thì trơn, nhưng nước lại rửa trôi hết chất nhờn tự nhiên của vợ đó em.",
      [("Nên vợ dễ khô rát, trầy xước.", "Chứ không êm như mình tưởng."),
       ("Nước hồ bơi, nước biển, xà bông.", "Dễ làm vợ viêm nhiễm."),
       ("Bao dễ tuột, dễ rách dưới nước.", "Mà vẫn có thai, vẫn lây bệnh như thường."),
       ("Bồn tắm, sàn ướt rất trơn.", "Trượt té là đi cấp cứu thiệt."),
       ("Tắm chung cho tình cảm.", "Rồi lên giường là an toàn nhất.")],
      "Lãng mạn thì cứ lãng mạn, mà khúc chính nên diễn trên cạn em nhé!"),
    T("168-sang-hay-toi", "'Gần' vợ buổi sáng hay buổi tối thì tốt hơn?",
      None, "Em hỏi: em thì sung nhất buổi sáng, vợ em lại chỉ chịu buổi tối, vậy giờ nào tốt hơn hả chị?",
      "Nội tiết tố nam cao nhất là lúc sáng sớm, nên các anh hay sung giờ đó.",
      [("Phụ nữ thường có hứng hơn vào buổi tối.", "Khi xong hết việc nhà, thấy thư thả."),
       ("Buổi sáng mình khỏe vì mới ngủ dậy.", "Nhưng hay vội, vợ chưa kịp tỉnh."),
       ("Buổi tối thì thong thả.", "Nhưng đừng trễ quá, mệt là hết hứng."),
       ("Người có bệnh tim, huyết áp.", "Sáng sớm đừng bật dậy gắng sức liền."),
       ("Thử cuối tuần, ngủ dậy trễ.", "Giờ đó hai bên dễ gặp nhau nhất.")],
      "Giờ vàng là giờ cả hai cùng muốn, chứ không nằm trên đồng hồ em nhé!"),
    T("169-chuyen-ay-dot-bao-nhieu-calo", "'Chuyện ấy' có thay được tập thể dục không?",
      None, "Em hỏi: em làm biếng tập thể dục, vậy siêng gần vợ có thay được không chị?",
      "Một lần gần vợ chỉ đốt chừng một trăm ca lo, bằng đi bộ nhanh mười lăm phút thôi em.",
      [("Nên không thay tập thể dục được.", "Bụng vẫn y nguyên."),
       ("Nhưng giúp giảm căng thẳng.", "Và ngủ ngon hơn hẳn."),
       ("Còn tốt cho tim nếu đều đặn.", "Coi như bài vận động nhẹ."),
       ("Ngược lại, tập thể dục giúp chuyện ấy rất nhiều.", "Máu lưu thông tốt thì 'cậu nhỏ' khỏe."),
       ("Đi bộ, bơi, tập chân, tập mông.", "Là mấy bài hợp với đàn ông trung niên.")],
      "Tập để gần vợ cho khỏe, chứ đừng gần vợ để khỏi tập em nhé!"),
    T("170-lau-khong-dung-co-teo-khong", "Lâu không 'dùng' có bị teo, bị yếu không?",
      None, "Em hỏi: vợ em đi làm xa cả năm, em để không lâu vậy có bị teo, bị yếu luôn không chị?",
      "Câu 'dùng thì còn, bỏ thì mất' là có cơ sở khoa học đàng hoàng đó em.",
      [("Không teo liền đâu.", "Nhưng để không nhiều năm thì kém đi thật."),
       ("Mỗi lần lên là một lần bơm máu, bơm ô xy.", "Giống như tập thể dục cho 'cậu nhỏ'."),
       ("Còn 'chào cờ' ban đêm, buổi sáng.", "Là cơ thể đang tự bảo dưỡng."),
       ("Vợ đi vắng thì tự xử cũng tính.", "Không có gì phải mắc cỡ."),
       ("Lâu ngày gặp lại hơi lóng ngóng.", "Vài lần là quen lại thôi.")],
      "Máy để lâu không nổ thì khó đề, thỉnh thoảng nhớ nổ máy em nhé!"),
    T("171-chan-com-them-pho", "Vì sao đàn ông hay 'chán cơm thèm phở'?",
      "Chị ơi… cưới nhau hai chục năm, giờ chồng em nhìn em như nhìn cái tủ lạnh!", None,
      "Bộ não con người khoái cái mới, gặp cái lạ là nó tiết chất hưng phấn liền.",
      [("Quen quá thì bớt hứng.", "Chứ không phải là hết thương."),
       ("'Phở' ăn riết rồi cũng thành cơm.", "Mà cái giá phải trả là tan nhà."),
       ("Còn rước bệnh về lây cho vợ.", "Chuyện này bệnh viện gặp hoài."),
       ("Làm mới với chính vợ mình.", "Đổi chỗ, đổi giờ, đi chơi riêng hai đứa."),
       ("Nói ra mình thèm cái gì.", "Vợ không đoán được đâu.")],
      "Cơm nhà mà chịu đổi món thì ngon hơn phở nhiều em nhé!"),
    T("172-tuong-tuong-nguoi-khac", "Lúc 'gần' vợ lại nghĩ tới người khác, có tội không?",
      None, "Em hỏi: có lúc đang gần vợ mà đầu em lại nghĩ tới người khác, em có tội với vợ không chị?",
      "Khảo sát cho thấy đa số người lớn, cả nam lẫn nữ, đều từng như vậy đó em.",
      [("Nghĩ trong đầu khác với làm thật.", "Đó chưa phải là ngoại tình."),
       ("Không cần phải thú tội với vợ.", "Nói ra chỉ làm vợ buồn."),
       ("Bộ não tự bật hình ảnh lạ.", "Để tăng hưng phấn thôi."),
       ("Phải nghĩ tới người khác mới lên được.", "Thì nên coi lại chuyện vợ chồng."),
       ("Cứ ám ảnh hoài một người cụ thể.", "Là đèn vàng rồi, dừng lại.")],
      "Đầu có đi lạc một chút thì nhớ kéo nó về với vợ em nhé!"),
    T("173-lay-gi-thay-gel-boi-tron", "Dầu dừa, nước bọt thay gel bôi trơn được không?",
      None, "Em hỏi: nhà hết gel bôi trơn, em lấy dầu dừa hay nước bọt xài đỡ được không chị?",
      "Mấy thứ sẵn trong nhà coi vậy chứ thứ nào cũng có cái hại riêng đó em.",
      [("Nước bọt mau khô.", "Lại mang vi khuẩn từ miệng xuống."),
       ("Dầu dừa, dầu ăn, kem dưỡng da.", "Làm mục, rách bao cao su."),
       ("Mấy thứ dầu còn khó rửa sạch.", "Vợ dễ bị viêm, bị nấm."),
       ("Sữa tắm, xà bông là rát nhất.", "Tuyệt đối đừng xài."),
       ("Gel gốc nước chỉ vài chục ngàn.", "Mua sẵn một tuýp để đầu giường.")],
      "Vợ chồng lớn tuổi thì tuýp gel là món phải có trong nhà em nhé!"),
    T("174-massage-tuyen-tien-liet", "Massage tuyến tiền liệt là gì, có nên thử?",
      None, "Em hỏi: trên mạng quảng cáo massage tuyến tiền liệt cho khỏe, cho sung, có nên thử không chị?",
      "Tuyến này nằm sát ruột, nên muốn chạm tới nó là phải đi vô từ 'cửa sau' đó em.",
      [("Chưa có bằng chứng là trị được phì đại.", "Hay giúp mạnh hơn."),
       ("Làm mạnh tay dễ trầy, chảy máu.", "Đang viêm mà đụng vô còn nặng thêm."),
       ("Tiệm quảng cáo 'thải độc' là không có cơ sở.", "Tuyến tiền liệt không có độc để thải."),
       ("Bác sĩ khám bằng ngón tay chỉ vài giây.", "Là để kiểm tra, không phải massage."),
       ("Vợ chồng tự thử với nhau.", "Thì phải có găng, có gel, nhẹ tay.")],
      "Muốn tuyến tiền liệt khỏe thì đi bộ với đi khám, khỏi cần tới tiệm em nhé!"),
    T("175-thuoc-kich-duc-cho-vo", "Thuốc kích dục cho vợ có thật không?",
      None, "Em hỏi: trên mạng bán thuốc nhỏ vô nước, vợ uống là tự đòi, có thật không chị?",
      "Không có thứ thuốc nào uống vô vài phút là người ta tự động ham muốn hết đó em.",
      [("Loại bán trôi nổi không biết chứa gì.", "Có người uống xong phải đi cấp cứu."),
       ("Lén bỏ vô ly nước của người khác.", "Là phạm pháp, kể cả với vợ mình."),
       ("Ham muốn của phụ nữ tới từ cảm xúc.", "Được thương, được nghỉ ngơi, không bị đau."),
       ("Vợ lạnh nhạt hay do mệt, do khô rát.", "Hoặc do nội tiết thay đổi."),
       ("Đưa vợ đi khám phụ khoa.", "Có cách điều trị đàng hoàng.")],
      "Thuốc kích dục mạnh nhất là ông chồng biết thương vợ đó em!"),
]

CTA = "Còn câu hỏi thầm kín nào thì bình luận cho chị, video sau chị trả lời!"

HEAD = """# MASTER PROMPT cho Muse: "Chị ơi, cho em hỏi thầm" – {title}
Đính kèm ảnh 1 = `nhan-vat-chi.png` (cùng thư mục).
Băng chữ đỏ khi dựng: **"{title}"** (cả video, chữ trắng nền đỏ bo góc, ~1/4 trên màn hình). Thời lượng: **{dur} giây ({shots} shot)**.

---

⚠️ XƯNG HÔ: nhân vật KHÔNG được xưng hay được gọi là "bác sĩ", "dược sĩ", "chuyên gia". Người hỏi chỉ gọi "chị ơi", nhân vật xưng "chị", gọi người xem là "em". Không ống nghe, không bảng tên, không áo blouse trắng.
⚠️ NỘI DUNG: nói kiểu chia sẻ kiến thức, không tục, không mô tả hành vi chi tiết, không hình ảnh gợi dục, không hứa chữa khỏi.

Bạn là đạo diễn kiêm dựng phim. Hãy tự làm trọn một video dọc 9:16, dài {dur} giây, dạng chị tâm sự trả lời câu hỏi người xem, theo quy trình và luật dưới đây. Làm theo thứ tự: (0) tạo và gửi ẢNH NHÂN VẬT CHUẨN → (3) in bảng shot → (4) tạo từng shot → ghép thành 1 video. Không hỏi lại tôi giữa chừng; nếu gặp lỗi thì tự thử lại và làm tiếp.

⚠️ VIỆC ĐẦU TIÊN, BẮT BUỘC: tạo ẢNH NHÂN VẬT CHUẨN (mục 0) và gửi vào chat. CHƯA có ảnh này thì KHÔNG in bảng shot, KHÔNG tạo video.

## 0. ẢNH NHÂN VẬT CHUẨN – LÀM ĐẦU TIÊN
1. Dựa trên ảnh 1 (đính kèm), tạo ẢNH tĩnh dọc 9:16 như ảnh chụp điện thoại thật, trong BỐI CẢNH mục 2:
   - Ảnh A – CHỊ: nhìn thẳng ống kính, thấy rõ toàn bộ mặt, mỉm cười tự tin, áo scrubs xanh ngọc cổ chữ V, tóc nâu đen dài xõa, bông tai nụ nhỏ.
{imgB}2. Tự kiểm tra: giống 100% gương mặt ảnh 1 (mắt, mũi, môi, lông mày, màu da); trang phục đúng. Sai thì tạo lại (tối đa 2 lần).
3. GỬI ảnh vào chat với dòng "ẢNH NHÂN VẬT CHUẨN". Mọi shot sau dùng ảnh này.
4. Không chờ tôi duyệt: gửi xong tự làm tiếp mục 3 và 4.

## 1. NỘI DUNG
- Chủ đề: {title}
- Khung bắt buộc: câu hỏi của người xem ngay giây đầu → một sự thật/con số gây tò mò → chị nói trước "có {n} điều" → mỗi ý một shot (giơ số ngón + giải thích) → câu chốt + CTA.
- Lời thoại (nói ĐÚNG từng chữ, tiếng Việt, giọng chị gái thân thiện, hóm hỉnh):
{lines}

## 2. KHỐI ĐỒNG NHẤT (chép y nguyên vào đầu prompt của MỌI shot)
- NHÂN VẬT CHỊ: đúng người trong ẢNH NHÂN VẬT CHUẨN A. Phụ nữ châu Á khoảng 30 tuổi, mặt trái xoan, da sáng hồng, mắt nâu, lông mày nâu đậm tự nhiên, môi hồng đất; tóc nâu đen dài quá vai, rẽ ngôi lệch, gợn sóng nhẹ; bông tai nụ bạc nhỏ; áo scrubs xanh ngọc cổ chữ V, túi ngực trái. Không đổi trang phục, kiểu tóc ở bất kỳ shot nào.
{vaiphu}- BỐI CẢNH: quầy mỹ phẩm thảo dược sáng sủa: kệ gỗ sáng có đèn LED ấm, chai lọ trắng–xanh lá, hộp giấy xanh, dây trầu bà rủ, bình hoa cúc vàng nhỏ, lọ thủy tinh thảo mộc khô bên trái; cửa kính lớn phía sau ra đường có cây xanh, ánh sáng ban ngày. Giữ nguyên bố cục kệ giữa các shot.
- ĐẠO CỤ: tờ giấy note màu vàng chanh cỡ lòng bàn tay (không in chữ); cốc sứ trắng.
- PHONG CÁCH: như tự quay bằng camera trước điện thoại dựng trên chân, khung ngang ngực, mặt ở 1/3 trên, nhìn thẳng ống kính. Máy gần như đứng yên. Biểu cảm mạnh liên tục: nhướn mày, mắt tròn, cười lộ răng, nghiêng đầu, gật đầu. Mỗi shot thay đổi nhẹ tư thế (nghiêng người, tay xòe, tay đặt ngực) để không nhàm. Không tua nhanh. Mỗi shot MỘT cú máy liền{jc}. Âm thanh phòng yên tĩnh, KHÔNG nhạc, KHÔNG chữ, KHÔNG phụ đề, KHÔNG logo.
- GIỌNG: Chị: nữ miền Nam khoảng 30 tuổi, trong, tự tin, nhanh vừa, hóm hỉnh.{giongphu} Khẩu hình khớp lời.

## 3. LUẬT CHIA SHOT
1. Mỗi shot đúng 10 giây; {shots} shot, tổng {dur} giây.
2. HOOK 2 GIÂY ĐẦU: {hookrule} Không chào hỏi, không giới thiệu.
3. Mỗi ý bắt đầu bằng số thứ tự, tay giơ đúng số ngón cạnh mặt (ý 5 xòe cả bàn tay; ý 6, 7 giơ 5 ngón + thêm ngón tay kia).
4. Lời mỗi shot vừa đủ 10 giây nói thong thả; nếu thiếu thời gian thì thêm biểu cảm/gật đầu, KHÔNG thêm lời khác.
5. Mỗi shot ghi rõ: vai, mốc giây, lời, động tác tay, biểu cảm, KHUNG CUỐI.

Phân shot {dur} giây:
{shotlist}

In bảng phân shot (shot, giây, vai, lời, động tác, khung cuối) rồi tự làm luôn, không chờ duyệt.

## 4. QUY TRÌNH TẠO
1. Shot 1: tạo từ KHỐI ĐỒNG NHẤT + mô tả shot + ẢNH NHÂN VẬT CHUẨN.
2. Từ shot 2: lấy KHUNG CUỐI shot trước làm ảnh khởi đầu, luôn kèm ẢNH NHÂN VẬT CHUẨN, dán lại KHỐI ĐỒNG NHẤT. Khung đầu shot mới trùng bố cục, ánh sáng, kệ thảo dược với khung cuối shot trước.
3. Sau mỗi shot tự kiểm tra 5 điểm: gương mặt giống ảnh chuẩn, scrubs xanh ngọc, bối cảnh quầy thảo dược, số ngón tay đúng ý, lời đúng từng chữ và khớp miệng; nhân vật KHÔNG xưng bác sĩ. Sai thì làm lại (tối đa 2 lần).
4. Ghép theo thứ tự, cắt nối thẳng, giữ âm thanh từng shot.
5. BĂNG CHỮ HOOK (BẮT BUỘC, làm lúc ghép, KHÔNG để công cụ tạo video tự vẽ chữ): chèn đè lên TOÀN BỘ video ngay từ khung hình đầu tiên (0s đến hết) một băng chữ cố định: "{title}" – chữ trắng đậm, nền đỏ tươi bo góc, căn giữa, rộng khoảng 90% khung, đặt ở khoảng 1/4 trên màn hình, không che mặt. Đúng chính tả tiếng Việt có dấu. Video giao KHÔNG có băng chữ này là chưa đạt, phải ghép lại.
6. Gửi tôi: video ghép, từng shot lẻ, danh sách chỗ đã làm lại.
"""

here = os.path.dirname(os.path.abspath(__file__))
for slug, title, hook, card, fact, pts, close in TOPICS:
    n = SO[len(pts) - 1]
    shots = len(pts) + 2
    dur = shots * 10
    intro = f"{fact} Có {n} điều em cần biết nè."
    if hook:
        q = f'  - Vai phụ (hook, sát máy, che miệng ngại): "{hook}"\n'
        imgB = ('   - Ảnh B – VAI PHỤ "CÔ BẠN LO LẮNG": CÙNG gương mặt đó hóa trang hài: kính gọng đen tròn to, '
                'áo sơ mi hoa sặc sỡ hồng–cam, tóc hơi rối, mặt nhăn nhó ngại ngùng.\n')
        vaiphu = '- VAI PHỤ: đúng người trong ảnh B (cùng gương mặt chị), kính gọng đen tròn to, áo sơ mi hoa hồng–cam. Xuất hiện 0–3s và 1 giây cuối video.\n'
        jc = " (trừ jump cut giữa vai phụ và chị)"
        giongphu = " Vai phụ: cùng giọng nhưng cao, the thé, ngại."
        hookrule = "khung đầu tiên là VAI PHỤ sát ống kính, che miệng hỏi ngay."
        s1 = f'0–3s VAI PHỤ hỏi câu hook. 3–10s jump cut CHỊ xua tay, mắt tròn: "{intro}" Khung cuối: chị giơ tay chuẩn bị đếm.'
        end_extra = ' 58–59s jump cut VAI PHỤ thở phào: "Vậy là em yên tâm rồi!", cắt lại chị cười nháy mắt.'
        end_line = '\n  - Vai phụ (1 giây cuối): "Vậy là em yên tâm rồi!"'
    else:
        q = f'  - Chị (cầm giấy note vàng, đọc giọng tấu hài): "{card}"\n'
        imgB = vaiphu = jc = giongphu = end_extra = end_line = ""
        hookrule = "khung đầu tiên là CHỊ đang cầm giấy note vàng trước ngực, tay kia cầm cốc sứ, mắt liếc giấy, đọc câu hỏi ngay."
        s1 = f'0–4s CHỊ cầm giấy note vàng + cốc, đọc câu hỏi, nhướn mày. 4–10s hạ giấy, nhìn thẳng máy: "{intro}" Khung cuối: chị giơ tay chuẩn bị đếm.'
    lines = q + f'  - Chị (hạ giấy, nhìn thẳng máy): "{intro}"\n'
    shotlist = [f"- Shot 1 (0–10s): {s1}"]
    for i, (h, ex) in enumerate(pts):
        lab = SO[i].capitalize()
        lines += f'  - Chị: "{lab}: {h} {ex}"\n'
        a, b = (i + 1) * 10, (i + 2) * 10
        shotlist.append(f'- Shot {i+2} ({a}–{b}s): giơ {i+1} ngón: "{lab}: {h} {ex}" Biểu cảm theo ý, xòe tay giải thích. Khung cuối: chị gật đầu, tay hạ.')
    lines += f'  - Chị chốt: "{close} {CTA}"' + end_line
    last = f'- Shot {shots} ({dur-10}–{dur}s): nắm tay trước ngực chốt: "{close}" Cười tươi nói CTA: "{CTA}" Nháy mắt.'
    if hook:
        last += end_extra.replace("58–59s", f"{dur-2}–{dur-1}s")
    shotlist.append(last)
    body = HEAD.format(title=title, dur=dur, shots=shots, imgB=imgB, n=n, lines=lines, vaiphu=vaiphu,
                       jc=jc, giongphu=giongphu, hookrule=hookrule, shotlist="\n".join(shotlist))
    with open(os.path.join(here, f"prompt-{slug}.md"), "w", encoding="utf-8") as f:
        f.write(body)
    print(f"{slug}: {dur}s / {shots} shot")
