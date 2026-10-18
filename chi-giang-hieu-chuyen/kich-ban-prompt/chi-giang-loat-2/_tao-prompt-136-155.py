# Sinh master prompt (60–90s) cho từng chủ đề "Chị ơi, cho em hỏi thầm". Chạy: python _tao-prompt.py
# Mỗi ý = 1 shot 10s. Tổng shot = 1 (hook) + số ý + 1 (chốt) → 5 ý = 70s, 6 ý = 80s, 7 ý = 90s.
import os

SO = ["một", "hai", "ba", "bốn", "năm", "sáu", "bảy"]

# slug, băng chữ, hook vai phụ (None = chị đọc giấy), câu đọc giấy, mở ý (con số/sự thật), [(ý, giải thích)], chốt
def T(slug, title, hook, card, fact, pts, close):
    return (slug, title, hook, card, fact, pts, close)

TOPICS = [
    T("136-mo-mau-cao-va-sinh-ly", "Mỡ máu cao có làm đàn ông 'yếu' đi không?",
      None, "Em hỏi: em đi khám ra mỡ máu cao, dạo này chuyện ấy cũng đuối hẳn, có liên quan không chị?",
      "Mạch máu nuôi 'cậu nhỏ' nhỏ hơn mạch tim nhiều, nên mỡ bám là nó nghẹt trước đó em.",
      [("Mỡ bám thành mạch làm máu tới không đủ.", "Nên khó lên, lên rồi cũng mau xuống."),
       ("Yếu đi có thể báo trước bệnh tim.", "Có khi sớm hơn vài năm."),
       ("Thuốc hạ mỡ máu không làm yếu.", "Đừng nghe đồn rồi tự bỏ thuốc."),
       ("Bớt đồ chiên, nội tạng, da, mỡ.", "Ăn thêm cá, rau, đậu."),
       ("Đi bộ nhanh mỗi ngày.", "Mỡ máu xuống thì phong độ lên theo.")],
      "Thông mạch máu là thông luôn chuyện vợ chồng em nhé!"),
    T("137-thuong-ma-phong-co-that-khong", "'Thượng mã phong' có thật không, ai dễ bị?",
      None, "Em hỏi: em nghe nói đang gần vợ mà lăn ra chết, gọi là thượng mã phong, có thật không chị?",
      "Có thật, nhưng rất hiếm, và gần như chỉ gặp ở người có sẵn bệnh tim mạch.",
      [("Thực chất là nhồi máu cơ tim hoặc đột quỵ.", "Xảy ra đúng lúc đang gắng sức."),
       ("Dễ bị khi huyết áp, tim mạch chưa ổn.", "Mà lại bỏ thuốc, không tái khám."),
       ("Nhậu say rồi uống thuốc tăng lực.", "Là kiểu nguy hiểm nhất."),
       ("Đau ngực, khó thở, nhức đầu dữ dội.", "Thì dừng ngay, đừng ráng."),
       ("Gọi cấp cứu một một năm liền.", "Đừng chích kim, đừng cạo gió mất thời gian.")],
      "Bệnh nền ổn định, không quá chén thì cứ yên tâm mà thương vợ em nhé!"),
    T("138-sau-dat-stent-gan-vo", "Đặt stent tim rồi còn 'gần' vợ được không?",
      "Chị ơi… chồng em mới đặt stent tim, giờ hai vợ chồng không ai dám đụng ai hết!", None,
      "Gần vợ một lần chỉ tốn sức cỡ leo hai tầng lầu thôi đó em.",
      [("Leo hai tầng lầu không mệt, không đau ngực.", "Là thường gần vợ lại được."),
       ("Hỏi thẳng bác sĩ tim mạch khi tái khám.", "Đừng ngại, bác sĩ nghe hoài."),
       ("Đang dùng thuốc giãn mạch vành.", "Thì tuyệt đối không uống thuốc tăng lực."),
       ("Chọn lúc khỏe, đừng ngay sau ăn no.", "Và đừng sau khi uống rượu."),
       ("Đau ngực, khó thở thì dừng liền.", "Nghỉ không bớt thì gọi cấp cứu.")],
      "Tim sửa xong rồi thì vợ chồng vẫn thương nhau được, đừng sợ quá em nhé!"),
    T("139-than-yeu-co-phai-yeu-sinh-ly", "Đau lưng, 'yếu' có phải do thận yếu không?",
      None, "Em hỏi: em hay đau lưng, chuyện ấy cũng kém, người ta nói em bị thận yếu, có đúng không chị?",
      "Trái thận lo lọc máu, không phải là chỗ quyết định bản lĩnh đàn ông đâu em.",
      [("'Thận yếu' là cách nói dân gian.", "Khác với bệnh thận mà bệnh viện chẩn đoán."),
       ("Đau lưng phần lớn do cơ, xương, cột sống.", "Ngồi nhiều, mang vác, ít vận động."),
       ("Yếu đi thường do mạch máu, nội tiết.", "Tiểu đường, huyết áp, mỡ máu, căng thẳng."),
       ("Thuốc 'bổ thận' trôi nổi coi chừng hại thận.", "Uống lâu là thận yếu thật."),
       ("Muốn biết thận sao thì xét nghiệm.", "Máu với nước tiểu, rẻ mà chính xác.")],
      "Đừng đổ oan cho trái thận, đi kiểm tra cho đúng bệnh em nhé!"),
    T("140-ruou-thuoc-ngam-co-bo-khong", "Rượu thuốc ngâm có 'bổ' thật không?",
      None, "Em hỏi: em có bình rượu ngâm quý lắm, mỗi tối làm vài ly cho sung, có nên không chị?",
      "Ngâm gì thì ngâm, vô tới bụng nó vẫn là rượu đó em.",
      [("Chưa có bằng chứng nào là tăng bản lĩnh.", "Hưng phấn lúc đầu là do men rượu."),
       ("Uống đều mỗi ngày làm giảm nội tiết tố nam.", "Càng uống càng xuống."),
       ("Gan phải làm việc nhiều hơn.", "Nhất là người có sẵn men gan cao."),
       ("Ngâm rễ cây, con vật lạ dễ ngộ độc.", "Có người nhập viện vì vậy rồi."),
       ("Đang uống thuốc huyết áp, tiểu đường.", "Thì càng nên tránh.")],
      "Bình rượu để chưng cho đẹp thôi, muốn sung thì ngủ đủ với đi bộ em nhé!"),
    T("141-an-hau-co-tang-ban-linh", "Ăn hàu có tăng bản lĩnh thật không?",
      None, "Em hỏi: anh em rủ em ăn hàu sống cho mạnh, có tác dụng thật không chị?",
      "Hàu là món giàu kẽm bậc nhất, mà kẽm thì cần cho nội tiết tố nam và tinh trùng.",
      [("Chỉ có ích khi cơ thể đang thiếu kẽm.", "Đủ rồi thì ăn thêm cũng không mạnh hơn."),
       ("Không có tác dụng liền.", "Ăn tối nay không phải tối nay sung."),
       ("Hàu sống dễ nhiễm khuẩn, đau bụng.", "Nên ăn chín cho an toàn."),
       ("Người bị gút nên ăn ít.", "Ăn nhiều dễ lên cơn đau."),
       ("Thịt, trứng, đậu, hạt cũng có kẽm.", "Không nhất thiết phải là hàu.")],
      "Ăn cho ngon thì được, đừng trông vô con hàu mà quên tập thể dục em nhé!"),
    T("142-keo-sam-thuoc-tang-luc-tren-mang", "Kẹo sâm, thuốc tăng lực trên mạng có an toàn?",
      "Chị ơi… chồng em lén mua kẹo sâm tăng lực trên mạng, uống xong mặt đỏ bừng, tim đập thình thịch!", None,
      "Nhiều loại ghi là thảo dược mà kiểm nghiệm ra lại có trộn thuốc tây trị rối loạn cương.",
      [("Uống vô có tác dụng liền là đáng nghi.", "Thảo dược thật không nhanh vậy."),
       ("Không biết trộn liều bao nhiêu.", "Nên dễ nhức đầu, đỏ mặt, tụt huyết áp."),
       ("Người bệnh tim là nguy hiểm nhất.", "Gặp thuốc giãn mạch vành có thể chết người."),
       ("Hàng không rõ nguồn gốc thì đừng mua.", "Quảng cáo càng nổ càng nên tránh."),
       ("Cần thuốc thì đi khám.", "Bác sĩ kê đúng loại, đúng liều cho mình.")],
      "Rẻ vài trăm ngàn mà đánh cược trái tim thì không đáng đâu em!"),
    T("143-bo-sung-testosterone", "Có nên chích, uống bổ sung nội tiết tố nam?",
      None, "Em hỏi: em ngoài năm mươi, nghe nói chích nội tiết tố nam là trẻ lại, có nên không chị?",
      "Nội tiết tố nam giảm từ từ theo tuổi, nhưng không phải ai giảm cũng cần bổ sung.",
      [("Chỉ dùng khi xét nghiệm máu thấy thấp.", "Và có triệu chứng rõ ràng."),
       ("Xét nghiệm phải lấy máu buổi sáng.", "Thường làm hai lần cho chắc."),
       ("Tự chích làm tinh hoàn teo lại.", "Tinh trùng cũng giảm theo."),
       ("Phải theo dõi tuyến tiền liệt và máu.", "Nên cần bác sĩ kê và tái khám."),
       ("Ngủ đủ, giảm bụng, tập tạ nhẹ.", "Là cách tăng tự nhiên, an toàn nhất.")],
      "Không có mũi chích nào làm mình trẻ lại, chỉ có sống khỏe mới giữ được lửa em nhé!"),
    T("144-giua-chung-bi-xiu", "Đang giữa chừng thì 'xìu', là bị gì?",
      None, "Em hỏi: em lên được, mà giữa chừng lại xìu, quê với vợ quá, bị gì vậy chị?",
      "Đàn ông nào cũng từng bị vài lần, nhất là sau tuổi bốn mươi đó em.",
      [("Thỉnh thoảng một lần là bình thường.", "Do mệt, rượu bia, thiếu ngủ."),
       ("Càng lo thì càng dễ bị lại.", "Sợ xìu là xìu thiệt."),
       ("Bị hoài trên ba tháng thì nên đi khám.", "Có thể do mạch máu giữ máu không tốt."),
       ("Kiểm tra đường huyết, mỡ máu, huyết áp.", "Ba thứ này hay là thủ phạm."),
       ("Nói thật với vợ.", "Vợ hiểu thì mình bớt áp lực liền.")],
      "Lỡ một lần không sao hết, đừng tự chấm điểm mình khắt khe quá em nhé!"),
    T("145-lon-tuoi-ra-it-dan", "Lớn tuổi 'ra' ít dần có phải hết đạn?",
      None, "Em hỏi: hồi trẻ em ra nhiều lắm, giờ năm mươi tuổi ra có chút xíu, có phải hết đạn rồi không chị?",
      "Lượng ra giảm dần theo tuổi là chuyện tự nhiên của cơ thể đó em.",
      [("Các tuyến tiết dịch làm việc chậm lại.", "Nên ít hơn, loãng hơn hồi trẻ."),
       ("Không liên quan gì tới bản lĩnh.", "Ít hay nhiều vẫn vui như nhau."),
       ("Uống ít nước, gần nhau dày.", "Cũng làm ít đi."),
       ("Một số thuốc tuyến tiền liệt làm ra ít.", "Thấy vậy thì hỏi bác sĩ, đừng tự ngưng."),
       ("Có máu, đau, hoặc tự nhiên khô hẳn.", "Thì nên đi khám.")],
      "Không ai hết đạn đâu em, kho chỉ sản xuất chậm lại thôi!"),
    T("146-ngoai-sau-muoi-con-gan-vo", "Ngoài sáu mươi còn 'gần' vợ được không?",
      None, "Em hỏi: em sáu mươi ba tuổi rồi, còn gần vợ thì có kỳ không, có hại sức không chị?",
      "Hơn một nửa đàn ông ngoài sáu mươi vẫn còn gần vợ đều đặn đó em.",
      [("Không có tuổi nào là tuổi phải nghỉ.", "Còn khỏe, còn thương là còn được."),
       ("Cần thời gian lâu hơn mới sẵn sàng.", "Đừng vội, đừng so với hồi trẻ."),
       ("Không được như xưa vẫn là bình thường.", "Miễn hai vợ chồng thấy vui."),
       ("Vợ lớn tuổi hay bị khô rát.", "Dùng gel bôi trơn cho vợ đỡ đau."),
       ("Có bệnh tim thì hỏi bác sĩ trước.", "Bệnh ổn là yên tâm.")],
      "Nắm tay, ôm vợ mỗi ngày cũng là giữ lửa rồi đó em!"),
    T("147-tieu-xong-con-nho-giot", "Tiểu xong kéo quần lên còn rỉ vài giọt, là sao?",
      None, "Em hỏi: em tiểu xong, kéo quần lên rồi mà còn rỉ ra vài giọt, ướt quần hoài, bị gì vậy chị?",
      "Chuyện này rất hay gặp ở đàn ông từ tuổi bốn mươi trở lên đó em.",
      [("Nước tiểu còn đọng lại trong ống tiểu.", "Cơ ở đó yếu đi nên không đẩy ra hết."),
       ("Tiểu xong đừng vội.", "Đứng thêm vài giây cho ra hết."),
       ("Vuốt nhẹ từ phía sau bìu ra trước.", "Là đẩy được phần còn đọng."),
       ("Tập nhíu cơ như đang nín tiểu.", "Mỗi ngày vài chục lần, vài tuần là đỡ."),
       ("Kèm tia yếu, tiểu đêm, tiểu gắt.", "Thì đi khám tuyến tiền liệt.")],
      "Không phải thận yếu gì đâu, tập cơ đúng cách là khô ráo lại em nhé!"),
    T("148-sau-mo-tuyen-tien-liet", "Mổ tuyến tiền liệt xong còn 'gần' vợ được không?",
      "Chị ơi… chồng em sắp mổ tuyến tiền liệt, ổng sợ mổ xong là hết làm đàn ông!", None,
      "Mổ nội soi phì đại lành tính thì phần lớn các anh vẫn giữ được bản lĩnh như trước.",
      [("Thường kiêng khoảng bốn đến sáu tuần.", "Theo đúng lời dặn của bác sĩ mổ."),
       ("Hay gặp nhất là ra ít hoặc không thấy ra.", "Vì nó đi ngược vô bàng quang."),
       ("Chuyện đó không hại gì.", "Cảm giác vẫn còn, chỉ khó có con hơn."),
       ("Mổ cắt hết vì ung thư thì ảnh hưởng nhiều hơn.", "Hồi phục từ từ, có khi một hai năm."),
       ("Có nhiều cách hỗ trợ sau mổ.", "Cứ hỏi bác sĩ, đừng âm thầm chịu.")],
      "Mổ là để sống khỏe hơn, chứ không phải để chia tay chuyện vợ chồng em nhé!"),
    T("149-gut-va-sinh-ly", "Bị gút có ảnh hưởng chuyện ấy không?",
      None, "Em hỏi: em bị gút mấy năm nay, dạo này chuyện ấy cũng kém, có dính dáng gì không chị?",
      "Người bị gút dễ gặp chuyện 'trên bảo dưới không nghe' hơn người thường đó em.",
      [("Axit uric cao lâu ngày làm hư mạch máu.", "Máu tới 'cậu nhỏ' cũng kém đi."),
       ("Gút hay đi chung với huyết áp, tiểu đường.", "Mấy bệnh này cộng lại càng yếu."),
       ("Đang lên cơn đau thì nghỉ.", "Hết đau rồi tính."),
       ("Bớt bia, nội tạng, hải sản, thịt đỏ.", "Uống nhiều nước mỗi ngày."),
       ("Uống thuốc đều, đừng chỉ uống lúc đau.", "Giữ axit uric ổn thì mạch máu đỡ hư.")],
      "Trị gút cho đàng hoàng là giữ luôn phong độ đó em!"),
    T("150-dau-lung-thoat-vi-va-chuyen-ay", "Thoát vị đĩa đệm có phải kiêng 'gần' vợ?",
      None, "Em hỏi: em bị thoát vị đĩa đệm, đau lưng hoài, có phải kiêng luôn chuyện vợ chồng không chị?",
      "Phần lớn người đau lưng vẫn gần vợ được, chỉ cần biết cách thôi em.",
      [("Đang đau dữ dội thì nghỉ vài ngày.", "Bớt đau rồi mới tính."),
       ("Giữ lưng thẳng, đừng gập, đừng vặn.", "Kê thêm gối cho đỡ lưng."),
       ("Để vợ chủ động nhiều hơn.", "Mình đỡ phải gồng."),
       ("Nhẹ nhàng, chậm rãi.", "Thấy đau nhói thì dừng, đổi cách khác."),
       ("Tê vùng háng, bí tiểu, yếu chân.", "Là phải đi cấp cứu liền.")],
      "Lưng đau thì đi chậm lại chứ không cần dừng hẳn em nhé!"),
    T("151-dap-xe-nhieu-co-hai-khong", "Đạp xe nhiều có hại 'chỗ đó' không?",
      None, "Em hỏi: sáng nào em cũng đạp xe hai tiếng, đạp xong thấy tê tê ở dưới, có hại không chị?",
      "Đạp xe đúng cách thì lợi nhiều hơn hại, tim khỏe thì chuyện ấy cũng khỏe.",
      [("Yên hẹp, cứng đè lên mạch máu, thần kinh.", "Nên mới bị tê."),
       ("Tê là cơ thể đang báo động.", "Đừng ráng đạp tiếp."),
       ("Đổi yên rộng, êm, có rãnh ở giữa.", "Giảm đè thấy rõ."),
       ("Chỉnh yên nằm ngang.", "Đừng để mũi yên chúi lên."),
       ("Mười lăm phút nhổm người lên một lần.", "Cho máu lưu thông lại.")],
      "Đạp cho khỏe chứ đừng đạp cho tê, chỉnh cái yên là xong em nhé!"),
    T("152-tai-xe-ngoi-nhieu", "Lái xe, ngồi nhiều có làm 'yếu' đi không?",
      "Chị ơi… chồng em chạy xe đường dài, ngồi suốt ngày, về tới nhà là hết xí quách!", None,
      "Ngồi liền nhiều tiếng làm máu vùng chậu lưu thông kém đi đó em.",
      [("Ngồi lâu làm vùng dưới bị nóng, bí.", "Không tốt cho tinh trùng."),
       ("Hay nhịn tiểu, uống ít nước.", "Dễ viêm đường tiểu, khó chịu tuyến tiền liệt."),
       ("Ít vận động thì bụng to ra.", "Bụng to là nội tiết tố nam giảm."),
       ("Một hai tiếng xuống xe đi lại vài phút.", "Vươn vai, duỗi chân."),
       ("Mặc quần thoáng, uống đủ nước.", "Tới trạm là ghé đi tiểu, đừng nhịn.")],
      "Xe còn phải bảo dưỡng, người lái xe càng phải bảo dưỡng em nhé!"),
    T("153-ca-phe-va-chuyen-ay", "Uống cà phê có lợi hay hại chuyện ấy?",
      None, "Em hỏi: ngày nào em cũng hai ba ly cà phê, vậy có ảnh hưởng chuyện ấy không chị?",
      "Một số nghiên cứu thấy đàn ông uống hai ba ly mỗi ngày lại ít bị 'yếu' hơn đó em.",
      [("Cà phê giúp mạch máu giãn nhẹ.", "Nhưng không phải là thuốc."),
       ("Uống sau hai giờ chiều dễ mất ngủ.", "Mất ngủ thì yếu thiệt."),
       ("Cà phê sữa đá ngọt quá.", "Uống hoài thì bụng to, đường huyết lên."),
       ("Tuyến tiền liệt to thì bớt lại.", "Vì cà phê làm đi tiểu nhiều hơn."),
       ("Hồi hộp, tim đập nhanh, huyết áp cao.", "Thì đừng uống đậm.")],
      "Ly cà phê buổi sáng cứ giữ, bớt đường với đừng uống trễ là được em nhé!"),
    T("154-tuoi-nam-muoi-con-co-con-duoc-khong", "Đàn ông năm mươi còn có con được không?",
      None, "Em hỏi: em năm mươi tuổi, vợ sau còn trẻ, tụi em muốn có con, còn kịp không chị?",
      "Đàn ông mình sản xuất tinh trùng suốt đời, không có ngày nghỉ hưu đâu em.",
      [("Có con được, nhưng chất lượng giảm dần.", "Nhất là từ sau bốn mươi."),
       ("Thường lâu đậu thai hơn.", "Đừng sốt ruột mấy tháng đầu."),
       ("Tuổi của vợ vẫn quan trọng hơn.", "Vợ dưới ba mươi lăm thì dễ hơn nhiều."),
       ("Đi xét nghiệm tinh dịch trước.", "Biết sớm thì đỡ mất thời gian."),
       ("Bỏ thuốc lá, bớt rượu ba tháng trước.", "Vì tinh trùng cần chừng đó thời gian.")],
      "Muộn một chút vẫn được, chuẩn bị kỹ là con khỏe em nhé!"),
    T("155-ve-huu-het-hung", "Về hưu rồi tự nhiên hết 'hứng', vì sao?",
      "Chị ơi… chồng em từ ngày về hưu cứ lầm lì, không thèm đụng tới em luôn!", None,
      "Về hưu là cú đổi nhịp sống lớn nhất của đời đàn ông đó em.",
      [("Hết việc dễ thấy mình vô dụng.", "Tâm trạng xuống thì ham muốn xuống theo."),
       ("Ngồi nhà nhiều, ít vận động.", "Người ì ra, ngủ cũng kém."),
       ("Vợ chồng chạm mặt cả ngày dễ cằn nhằn.", "Mỗi người nên có khoảng riêng."),
       ("Kiếm việc để làm, hẹn bạn, tập thể dục.", "Có niềm vui thì có lại hứng."),
       ("Buồn chán, mất ngủ hơn hai tuần.", "Thì nên đi khám, có thể là trầm cảm.")],
      "Nghỉ hưu là nghỉ làm thôi, chứ đâu có nghỉ thương vợ em nhé!"),
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
