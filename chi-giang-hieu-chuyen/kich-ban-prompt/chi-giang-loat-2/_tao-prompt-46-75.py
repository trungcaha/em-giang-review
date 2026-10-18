# Sinh master prompt (60–90s) cho từng chủ đề "Chị ơi, cho em hỏi thầm". Chạy: python _tao-prompt.py
# Mỗi ý = 1 shot 10s. Tổng shot = 1 (hook) + số ý + 1 (chốt) → 5 ý = 70s, 6 ý = 80s, 7 ý = 90s.
import os

SO = ["một", "hai", "ba", "bốn", "năm", "sáu", "bảy"]

# slug, băng chữ, hook vai phụ (None = chị đọc giấy), câu đọc giấy, mở ý (con số/sự thật), [(ý, giải thích)], chốt
TOPICS = [
    ("46-tinh-hoan-lech", "Hai 'quả' lệch nhau có sao không?",
     "Chị ơi… em thấy hai bên 'quả' của em một cao một thấp, có bị gì không?", None,
     "Gần như đàn ông nào cũng lệch, bên trái thường thấp hơn bên phải đó em.",
     [("Lệch là bình thường.", "Giúp hai bên không cọ vào nhau khi đi lại."),
      ("To nhỏ hơi khác cũng bình thường.", "Chênh nhẹ không ảnh hưởng gì."),
      ("Tự kiểm tra mỗi tháng.", "Lúc tắm nước ấm, lăn nhẹ giữa các ngón tay."),
      ("Sờ thấy cục cứng thì đi khám.", "Dù không đau cũng không được chủ quan."),
      ("Đau đột ngột dữ dội.", "Có thể là xoắn, phải cấp cứu trong vài giờ.")],
     "Lệch thì yên tâm, có cục lạ hay đau dữ dội thì đi ngay em nhé!"),
    ("47-bao-quy-dau-co-can-cat", "Có nên cắt bao quy đầu không?",
     None, "Em hỏi: em có cần đi cắt bao quy đầu không chị?",
     "Không phải ai cũng cần cắt đâu em, chỉ một số trường hợp thôi.",
     [("Tuột lên xuống dễ dàng thì không cần.", "Chỉ cần vệ sinh sạch mỗi ngày."),
      ("Hẹp không tuột được thì nên khám.", "Dễ viêm, khó vệ sinh."),
      ("Viêm đi viêm lại.", "Đỏ, sưng, có mùi nhiều lần trong năm."),
      ("Dài quá, đọng chất bẩn.", "Bác sĩ sẽ tư vấn có nên làm hay không."),
      ("Không giúp to hơn hay bền hơn.", "Đừng tin quảng cáo kiểu đó.")],
     "Sạch sẽ là đủ, chỉ cắt khi thật sự cần thôi em!"),
    ("48-hpv-la-gi", "HPV là gì mà ai cũng nên biết?",
     None, "Em hỏi: HPV là gì vậy chị, sao ai cũng nói phải tiêm?",
     "Đa số người có quan hệ tình dục sẽ nhiễm HPV ít nhất một lần trong đời đó em.",
     [("Là virus lây qua tiếp xúc da.", "Bao cao su giảm nguy cơ nhưng không chặn hết."),
      ("Thường không có triệu chứng.", "Nhiều người mang mà không biết."),
      ("Một số chủng gây sùi mào gà.", "Mọc mụn thịt ở vùng kín."),
      ("Một số chủng gây ung thư.", "Cổ tử cung, hậu môn, vòm họng."),
      ("Tiêm vắc xin là cách tốt nhất.", "Cả nam và nữ đều tiêm được, càng sớm càng tốt.")],
     "Một mũi tiêm nhỏ, bảo vệ cả một đời đó em!"),
    ("49-xet-nghiem-benh-xa-hoi", "Khi nào nên đi xét nghiệm bệnh lây qua đường tình dục?",
     None, "Em hỏi: khi nào thì nên đi xét nghiệm mấy bệnh lây qua đường tình dục chị?",
     "Rất nhiều bệnh không có triệu chứng gì cả, nên đợi đau mới đi là muộn.",
     [("Trước khi bắt đầu mối quan hệ mới.", "Hai người cùng đi là cách yêu thương nhau."),
      ("Sau quan hệ không an toàn.", "Đợi vài tuần cho xét nghiệm chính xác."),
      ("Có nhiều bạn tình.", "Nên xét nghiệm định kỳ vài tháng một lần."),
      ("Có triệu chứng lạ.", "Ngứa, tiết dịch, loét, đau buốt là đi liền."),
      ("Trước khi có con.", "Bảo vệ cả em bé trong bụng.")],
     "Xét nghiệm không xấu hổ, giấu bệnh mới đáng lo em nhé!"),
    ("50-uong-thuoc-cuong-duong", "Tự uống thuốc 'tăng lực' có nguy hiểm không?",
     "Chị ơi… em tự mua thuốc 'tăng lực' về uống thì có sao không?", None,
     "Mỗi năm có không ít ca phải cấp cứu vì tự uống thuốc loại này đó em.",
     [("Nguy hiểm với người bệnh tim.", "Có thể tụt huyết áp đột ngột."),
      ("Hàng trôi nổi không rõ thành phần.", "Có khi trộn chất cấm hoặc quá liều."),
      ("Có thể gây cương kéo dài.", "Quá bốn tiếng là cấp cứu."),
      ("Không giải quyết gốc rễ.", "Nguyên nhân thật có thể là tiểu đường, tim mạch."),
      ("Phải đi khám để được kê.", "Đúng thuốc, đúng liều mới an toàn.")],
     "Đừng đem tính mạng ra đánh đổi một đêm vui em nhé!"),
    ("51-tu-the-de-co-con", "Có tư thế nào giúp dễ có con không?",
     None, "Em hỏi: có tư thế nào giúp dễ có em bé hơn không chị?",
     "Nói thật là chưa có nghiên cứu nào chứng minh tư thế quyết định đâu em.",
     [("Thời điểm quan trọng hơn tư thế.", "Quan hệ quanh ngày rụng trứng."),
      ("Không cần nằm gác chân.", "Tinh trùng khỏe tự bơi rất nhanh."),
      ("Nằm nghỉ vài phút cũng được.", "Thoải mái là chính, không bắt buộc."),
      ("Tránh gel bôi trơn thông thường.", "Một số loại làm giảm sức bơi tinh trùng."),
      ("Một năm chưa có thì đi khám.", "Cả vợ lẫn chồng cùng kiểm tra.")],
     "Thư giãn và đúng ngày mới là bí quyết đó em!"),
    ("52-dau-hieu-rung-trung", "Dấu hiệu nào cho biết đang rụng trứng?",
     None, "Em hỏi: làm sao biết mình đang rụng trứng vậy chị?",
     "Cơ thể phụ nữ có mấy tín hiệu nhỏ mà ít ai để ý nè em.",
     [("Dịch tiết trong và dai.", "Giống lòng trắng trứng, kéo giãn được."),
      ("Đau nhẹ một bên bụng dưới.", "Kéo dài vài giờ đến một ngày."),
      ("Ham muốn tăng lên.", "Cơ thể tự nhiên 'muốn' hơn mấy ngày này."),
      ("Thân nhiệt buổi sáng tăng nhẹ.", "Đo mỗi sáng trước khi dậy để theo dõi."),
      ("Ngực căng nhẹ.", "Do nội tiết thay đổi.")],
     "Hiểu cơ thể mình là bước đầu tiên để chủ động em nhé!"),
    ("53-kinh-nguyet-khong-deu", "Kinh nguyệt không đều có ảnh hưởng chuyện có con?",
     None, "Em hỏi: kinh của em lúc sớm lúc muộn, có khó có con không chị?",
     "Lệch vài ngày mỗi tháng là chuyện rất bình thường em ạ.",
     [("Chu kỳ từ hai mốt đến ba lăm ngày là ổn.", "Không cần đúng hai tám ngày."),
      ("Căng thẳng làm lệch kinh.", "Thi cử, công việc, mất ngủ đều ảnh hưởng."),
      ("Tăng giảm cân nhanh.", "Cũng làm rối chu kỳ."),
      ("Buồng trứng đa nang.", "Kinh thưa, mụn nhiều, lông nhiều thì nên khám."),
      ("Ba tháng không có kinh.", "Không có bầu mà mất kinh thì phải đi khám.")],
     "Lệch nhẹ không sao, lệch nhiều thì khám sớm cho yên tâm em nhé!"),
    ("54-tinh-trung-yeu", "Làm sao biết tinh trùng khỏe hay yếu?",
     None, "Em hỏi: làm sao biết tinh trùng của mình khỏe hay yếu hả chị?",
     "Nhìn bằng mắt thì không biết được đâu em, phải làm tinh dịch đồ.",
     [("Tinh dịch đồ.", "Xét nghiệm đơn giản, cho biết số lượng và sức bơi."),
      ("Kiêng hai đến năm ngày trước khi làm.", "Để kết quả chính xác."),
      ("Hút thuốc làm tinh trùng yếu.", "Bỏ thuốc là cải thiện rõ."),
      ("Nóng và béo phì cũng ảnh hưởng.", "Giảm cân, mặc đồ thoáng giúp tốt hơn."),
      ("Tinh trùng mới cần khoảng ba tháng.", "Thay đổi lối sống thì đợi ba tháng mới thấy kết quả.")],
     "Muốn có con thì khám cả chồng nữa, không phải chỉ vợ đâu em!"),
    ("55-quan-he-khi-mang-thai", "Đang mang thai có 'gần' nhau được không?",
     None, "Em hỏi: vợ đang có bầu thì hai vợ chồng gần nhau được không chị?",
     "Với thai kỳ khỏe mạnh bình thường thì câu trả lời là được em ạ.",
     [("Em bé được bảo vệ rất kỹ.", "Có nước ối và cổ tử cung đóng chặt."),
      ("Nhẹ nhàng, chọn tư thế thoải mái.", "Tránh đè lên bụng."),
      ("Ra máu, đau bụng thì dừng.", "Và đi khám ngay."),
      ("Có tiền sử sảy thai, nhau thấp.", "Phải hỏi bác sĩ sản trước."),
      ("Dùng bao nếu chưa rõ bệnh lây.", "Để bảo vệ cả mẹ và bé.")],
     "Thai khỏe thì yêu thương vẫn bình thường, chỉ cần nhẹ nhàng thôi em!"),
    ("56-mang-thai-ngoai-tu-cung", "Dấu hiệu mang thai ngoài tử cung là gì?",
     None, "Em hỏi: làm sao biết có bầu ngoài tử cung vậy chị?",
     "Đây là cấp cứu sản khoa, biết sớm có thể cứu mạng đó em.",
     [("Trễ kinh, que hai vạch.", "Nhưng siêu âm không thấy thai trong tử cung."),
      ("Đau bụng dưới một bên.", "Đau tăng dần, có khi rất dữ dội."),
      ("Ra máu bất thường.", "Lấm tấm, màu nâu đen."),
      ("Choáng, chóng mặt, ngất.", "Dấu hiệu chảy máu trong, cấp cứu ngay."),
      ("Có thai là đi siêu âm sớm.", "Để biết thai đã vào đúng chỗ chưa.")],
     "Que hai vạch là đi khám ngay, đừng đợi em nhé!"),
    ("57-khi-hu-bat-thuong", "Khí hư thế nào là bất thường?",
     None, "Em hỏi: khí hư màu gì thì là có vấn đề vậy chị?",
     "Khí hư là bạn của phụ nữ, chỉ khi đổi màu đổi mùi mới cần lo.",
     [("Trong hoặc trắng đục là bình thường.", "Nhiều hơn vào giữa chu kỳ."),
      ("Trắng vón cục như bã đậu.", "Kèm ngứa, thường là nấm."),
      ("Xám, mùi tanh.", "Thường do vi khuẩn mất cân bằng."),
      ("Vàng xanh, có bọt.", "Có thể do trùng roi, cần khám cả hai vợ chồng."),
      ("Lẫn máu ngoài kỳ kinh.", "Phải đi khám sớm.")],
     "Để ý màu và mùi là biết cơ thể đang nói gì đó em!"),
    ("58-dung-dung-dich-ve-sinh", "Dùng dung dịch vệ sinh mỗi ngày có tốt không?",
     None, "Em hỏi: ngày nào em cũng rửa bằng dung dịch vệ sinh, vậy có tốt không chị?",
     "Nhiều chị em rửa quá kỹ, mà đó lại là nguyên nhân viêm nhiễm đó.",
     [("Nước sạch là đủ mỗi ngày.", "Vùng kín tự làm sạch được."),
      ("Chỉ rửa bên ngoài.", "Không thụt rửa vào trong."),
      ("Chọn loại dịu nhẹ, không mùi.", "Nếu muốn dùng, vài lần một tuần."),
      ("Rửa từ trước ra sau.", "Tránh đưa vi khuẩn từ hậu môn lên."),
      ("Lau khô sau khi rửa.", "Ẩm ướt dễ sinh nấm.")],
     "Sạch vừa phải mới khỏe, đừng rửa quá tay em nhé!"),
    ("59-viem-duong-tieu", "Vì sao hay bị viêm đường tiểu sau khi 'gần' nhau?",
     None, "Em hỏi: lần nào gần chồng xong em cũng bị tiểu buốt, sao vậy chị?",
     "Chuyện này nhiều đến mức có tên riêng là 'viêm bàng quang tuần trăng mật' đó em.",
     [("Vi khuẩn bị đẩy vào niệu đạo.", "Phụ nữ niệu đạo ngắn nên dễ bị."),
      ("Đi tiểu sau khi xong.", "Trong vòng nửa tiếng."),
      ("Uống nhiều nước.", "Giúp rửa trôi vi khuẩn."),
      ("Vệ sinh trước cho cả hai.", "Tay và vùng kín sạch sẽ."),
      ("Sốt, đau lưng thì đi khám ngay.", "Có thể vi khuẩn đã lên thận.")],
     "Mấy thói quen nhỏ là đỡ khổ cả tháng đó em!"),
    ("60-tinh-dich-co-mau", "Tinh dịch có máu có nguy hiểm không?",
     "Chị ơi… em thấy tinh dịch có lẫn máu, em sợ quá, có sao không?", None,
     "Đa số trường hợp là lành tính và tự hết, nhưng em không được bỏ qua.",
     [("Thường do vỡ mạch máu nhỏ.", "Sau khi quan hệ mạnh hoặc kiêng lâu."),
      ("Viêm tuyến tiền liệt.", "Kèm tiểu buốt, đau vùng chậu."),
      ("Sau thủ thuật vùng kín.", "Có thể ra máu vài lần."),
      ("Trên bốn mươi tuổi thì khám kỹ.", "Để loại trừ bệnh tuyến tiền liệt."),
      ("Lặp lại nhiều lần thì đi khám.", "Kèm sốt, đau là đi ngay.")],
     "Một lần thì bình tĩnh, nhiều lần thì phải khám nam khoa em nhé!"),
    ("61-gian-tinh-mach-thung-tinh", "Giãn tĩnh mạch thừng tinh là gì?",
     None, "Em hỏi: giãn tĩnh mạch thừng tinh là bệnh gì mà nghe nhiều vậy chị?",
     "Cứ mười đàn ông thì có khoảng một người bị mà không biết đó em.",
     [("Mạch máu bị giãn quanh 'quả'.", "Sờ thấy như búi giun, hay ở bên trái."),
      ("Nặng tức khi đứng lâu.", "Nằm xuống thì đỡ."),
      ("Có thể làm tinh trùng yếu.", "Do nhiệt độ tăng."),
      ("Không phải ai cũng cần mổ.", "Nhẹ thì theo dõi."),
      ("Khó có con thì nên khám.", "Điều trị có thể cải thiện tinh trùng.")],
     "Thấy nặng tức hay sờ thấy búi lạ thì đi khám em nhé!"),
    ("62-tieu-duong-va-sinh-ly", "Tiểu đường ảnh hưởng chuyện ấy thế nào?",
     None, "Em hỏi: bị tiểu đường thì chuyện vợ chồng có bị ảnh hưởng không chị?",
     "Người tiểu đường gặp chuyện 'không lên' cao gấp nhiều lần người thường đó em.",
     [("Đường cao làm hỏng mạch máu.", "Máu tới không đủ."),
      ("Tổn thương thần kinh.", "Giảm cảm giác."),
      ("Phụ nữ dễ khô và nhiễm nấm.", "Ngứa, đau khi gần nhau."),
      ("Kiểm soát đường huyết là chìa khóa.", "Ổn định đường thì sinh lý cũng tốt hơn."),
      ("Không tự uống thuốc tăng lực.", "Hỏi bác sĩ để dùng an toàn.")],
     "Giữ đường huyết ổn là giữ luôn hạnh phúc gia đình em ạ!"),
    ("63-thuoc-la-va-sinh-ly", "Hút thuốc có làm yếu chuyện ấy không?",
     None, "Em hỏi: chồng em hút thuốc nhiều, có ảnh hưởng chuyện ấy không chị?",
     "Người hút thuốc có nguy cơ 'không lên' cao gần gấp đôi đó em.",
     [("Thuốc lá làm hẹp mạch máu.", "Máu khó dồn về."),
      ("Tinh trùng ít và yếu hơn.", "Khó có con hơn."),
      ("Hơi thở và mùi cơ thể.", "Làm vợ mất hứng."),
      ("Thuốc lá điện tử cũng không an toàn.", "Vẫn có nicotine."),
      ("Bỏ thuốc là cải thiện.", "Vài tháng sau đã thấy khác.")],
     "Bỏ thuốc là món quà cho cả hai vợ chồng đó em!"),
    ("64-cang-thang-va-sinh-ly", "Vì sao stress làm 'chuyện ấy' xuống dốc?",
     None, "Em hỏi: dạo này công việc căng quá, em thấy yếu hẳn, có liên quan không chị?",
     "Não là cơ quan sinh dục quan trọng nhất đó em, đầu căng thì dưới cũng tắt.",
     [("Stress tiết hormone ức chế.", "Làm giảm ham muốn."),
      ("Khó tập trung vào lúc đó.", "Đầu nghĩ chuyện khác là xuống ngay."),
      ("Mất ngủ đi kèm.", "Nội tiết tố nam giảm."),
      ("Tập thể dục giúp xả stress.", "Đi bộ, chạy, bơi đều tốt."),
      ("Nói chuyện với vợ.", "Chia sẻ để cùng nhau vượt qua.")],
     "Thả lỏng đầu óc trước, rồi mọi chuyện sẽ ổn em nhé!"),
    ("65-xuat-tinh-nguoc-dong", "'Xong' mà không thấy ra gì là sao?",
     None, "Em hỏi: em có cảm giác 'xong' mà không thấy ra gì cả, bị sao vậy chị?",
     "Hiện tượng này có tên là xuất tinh ngược, ít gặp nhưng có thật.",
     [("Tinh dịch đi ngược vào bàng quang.", "Nên lần tiểu sau nước tiểu đục."),
      ("Do một số thuốc.", "Thuốc tiền liệt tuyến, huyết áp."),
      ("Sau phẫu thuật vùng chậu.", "Có thể ảnh hưởng van đóng."),
      ("Tiểu đường lâu năm.", "Làm tổn thương thần kinh."),
      ("Không nguy hiểm nhưng khó có con.", "Muốn có con thì đi khám nam khoa.")],
     "Lạ thì đừng ngại, khám là biết ngay em ạ!"),
    ("66-chu-ky-an-toan", "Tránh thai bằng cách tính ngày có an toàn không?",
     None, "Em hỏi: tụi em tránh thai bằng cách tính ngày an toàn, vậy có chắc không chị?",
     "Cứ khoảng bốn cặp dùng cách này thì có một cặp lỡ dính trong năm đó em.",
     [("Rụng trứng không cố định.", "Stress, bệnh, đi xa đều làm lệch."),
      ("Tinh trùng sống đến năm ngày.", "Ngày 'an toàn' có thể không an toàn."),
      ("Cần chu kỳ rất đều.", "Ít ai đều được cả năm."),
      ("Kết hợp que thử rụng trứng.", "Chính xác hơn nhưng vẫn chưa chắc."),
      ("Cần chắc chắn thì dùng biện pháp khác.", "Bao cao su, thuốc, vòng tránh thai.")],
     "Tính ngày là đánh cược đó em, muốn chắc thì chọn cách khác nha!"),
    ("67-thuoc-tranh-thai-khan-cap", "Thuốc tránh thai khẩn cấp uống nhiều có hại không?",
     None, "Em hỏi: tháng nào em cũng uống thuốc tránh thai khẩn cấp, có hại không chị?",
     "Thuốc này là phương án cứu hộ, không phải dùng thường xuyên đâu em.",
     [("Liều nội tiết rất cao.", "Làm rối loạn kinh nguyệt."),
      ("Hiệu quả kém hơn thuốc hằng ngày.", "Nên dễ dính hơn em nghĩ."),
      ("Càng uống sớm càng hiệu quả.", "Để lâu thì giảm tác dụng."),
      ("Không ngừa bệnh lây.", "Vẫn cần bao cao su."),
      ("Chuyển sang biện pháp lâu dài.", "Hỏi cơ sở y tế để chọn phù hợp.")],
     "Thuốc khẩn cấp là phao cứu sinh, đừng dùng làm áo phao hằng ngày nha em!"),
    ("68-vong-tranh-thai", "Đặt vòng tránh thai có đau không, có bất tiện không?",
     None, "Em hỏi: đặt vòng tránh thai có đau không, chồng có cảm nhận được không chị?",
     "Vòng là một trong những cách tránh thai hiệu quả nhất hiện nay đó em.",
     [("Đặt chỉ mất vài phút.", "Có thể hơi đau như đau bụng kinh."),
      ("Hiệu quả rất cao.", "Dùng được nhiều năm."),
      ("Chồng hầu như không cảm nhận.", "Nếu vướng thì bác sĩ cắt ngắn dây."),
      ("Vài tháng đầu kinh có thể nhiều hơn.", "Sau đó thường ổn."),
      ("Khám định kỳ.", "Để chắc vòng còn đúng vị trí.")],
     "Một lần đặt, yên tâm nhiều năm, hỏi bác sĩ xem có hợp không em nhé!"),
    ("69-nam-gioi-tien-man-duc", "Đàn ông cũng có 'mãn dục' à?",
     None, "Em hỏi: đàn ông có bị mãn dục như phụ nữ mãn kinh không chị?",
     "Có đó em, nhưng nó diễn ra từ từ chứ không đột ngột như phụ nữ.",
     [("Testosterone giảm dần sau bốn mươi.", "Mỗi năm một chút."),
      ("Mệt mỏi, dễ cáu.", "Hay bị nhầm là do công việc."),
      ("Giảm ham muốn.", "Cương yếu hơn, ít buổi sáng hơn."),
      ("Tăng mỡ bụng, giảm cơ.", "Cơ thể thay đổi rõ."),
      ("Xét nghiệm máu là biết.", "Đừng tự mua thuốc nội tiết.")],
     "Đàn ông cũng cần được chăm sóc như phụ nữ đó em!"),
    ("70-tien-man-kinh", "Tiền mãn kinh ảnh hưởng chuyện vợ chồng ra sao?",
     None, "Em hỏi: vợ em sắp mãn kinh, chuyện vợ chồng có thay đổi không chị?",
     "Có thay đổi, nhưng không có nghĩa là hết hạnh phúc đâu em.",
     [("Khô và đau.", "Do nội tiết giảm, dùng gel bôi trơn giúp nhiều."),
      ("Bốc hỏa, mất ngủ.", "Làm vợ mệt và ít hứng."),
      ("Tâm trạng thất thường.", "Chồng cần kiên nhẫn hơn."),
      ("Vẫn có thể có thai.", "Chưa hết kinh mười hai tháng thì vẫn cần tránh."),
      ("Đi khám để được tư vấn.", "Có nhiều cách hỗ trợ an toàn.")],
     "Hiểu nhau thì tuổi nào cũng hạnh phúc được em nhé!"),
    ("71-dat-gel-boi-tron", "Có nên dùng gel bôi trơn không?",
     None, "Em hỏi: dùng gel bôi trơn có phải là do mình 'có vấn đề' không chị?",
     "Không đâu em, gel bôi trơn giúp rất nhiều cặp đôi thoải mái hơn.",
     [("Gốc nước là an toàn nhất.", "Dùng được với bao cao su."),
      ("Không dùng dầu ăn, kem dưỡng.", "Làm rách bao, dễ viêm."),
      ("Gốc silicon trơn lâu hơn.", "Nhưng khó rửa hơn."),
      ("Tránh loại có mùi, có màu.", "Dễ kích ứng."),
      ("Khô kéo dài thì đi khám.", "Có thể do nội tiết.")],
     "Dùng gel chẳng có gì xấu hổ, thoải mái là trên hết em nhé!"),
    ("72-ngu-chung-va-sinh-ly", "Vợ chồng ngủ riêng có ảnh hưởng tình cảm không?",
     None, "Em hỏi: vợ chồng em ngủ riêng vì con nhỏ, có ảnh hưởng không chị?",
     "Nhiều cặp ngủ riêng vẫn rất hạnh phúc, quan trọng là cách giữ kết nối.",
     [("Ngủ ngon thì tâm trạng tốt hơn.", "Ít cáu gắt với nhau."),
      ("Nhưng dễ mất những phút thân mật.", "Ôm, trò chuyện trước khi ngủ."),
      ("Hẹn giờ riêng cho hai người.", "Mỗi tuần một buổi tối."),
      ("Nhắn tin, khen nhau.", "Giữ sự quan tâm mỗi ngày."),
      ("Nói thẳng nhu cầu.", "Đừng để người kia tự đoán.")],
     "Ngủ riêng giường được, đừng để riêng lòng em nhé!"),
    ("73-xem-phim-nguoi-lon", "Xem phim người lớn nhiều có hại không?",
     None, "Em hỏi: em hay xem phim người lớn, vậy có ảnh hưởng gì không chị?",
     "Thỉnh thoảng thì không sao, nhưng xem nhiều có mấy cái bẫy em phải biết.",
     [("Kỳ vọng sai về kích thước, thời gian.", "Phim được dựng và cắt ghép."),
      ("Khó hứng thú với người thật.", "Não quen với kích thích mạnh."),
      ("Dễ 'về' nhanh hoặc khó lên.", "Do thói quen tự xử nhanh."),
      ("Tốn thời gian, mất ngủ.", "Ảnh hưởng công việc."),
      ("Giảm dần nếu thấy lệ thuộc.", "Không được thì tìm người tư vấn.")],
     "Phim là phim, đời thật mới quan trọng em nhé!"),
    ("74-yeu-qua-mang", "Có nên gửi ảnh nhạy cảm cho người yêu không?",
     "Chị ơi… người yêu em đòi gửi ảnh nhạy cảm, em có nên gửi không?", None,
     "Rất nhiều vụ tống tiền bắt đầu từ một tấm ảnh gửi cho người yêu đó em.",
     [("Ảnh gửi đi là mất kiểm soát.", "Có thể bị lưu, bị chia sẻ."),
      ("Chia tay có thể bị dọa.", "Chuyện này xảy ra rất nhiều."),
      ("Tài khoản có thể bị hack.", "Kể cả khi người yêu tốt."),
      ("Có quyền từ chối.", "Người thương thật sẽ tôn trọng em."),
      ("Bị dọa thì báo công an.", "Đừng chuyển tiền, đừng im lặng.")],
     "Yêu là tôn trọng, không phải đòi hỏi em nhé!"),
    ("75-noi-chuyen-voi-con-ve-gioi-tinh", "Nói chuyện giới tính với con thế nào?",
     None, "Em hỏi: con em mười hai tuổi rồi, nói chuyện giới tính với con sao cho đúng chị?",
     "Trẻ được bố mẹ dạy sớm thường biết tự bảo vệ mình tốt hơn đó em.",
     [("Gọi đúng tên bộ phận cơ thể.", "Không né tránh, không gọi tên lóng."),
      ("Dạy vùng riêng tư.", "Không ai được chạm vào, kể cả người quen."),
      ("Giải thích dậy thì trước khi nó đến.", "Kinh nguyệt, mộng tinh là bình thường."),
      ("Trả lời bình tĩnh.", "Con hỏi gì cũng không la mắng."),
      ("Là người con tin để kể.", "Có chuyện gì con sẽ tìm bố mẹ đầu tiên.")],
     "Bố mẹ nói trước, con sẽ không phải học sai từ ngoài kia em ạ!"),
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
