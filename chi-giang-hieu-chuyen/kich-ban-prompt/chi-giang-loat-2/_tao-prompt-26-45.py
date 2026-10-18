# Sinh master prompt (60–90s) cho từng chủ đề "Chị ơi, cho em hỏi thầm". Chạy: python _tao-prompt.py
# Mỗi ý = 1 shot 10s. Tổng shot = 1 (hook) + số ý + 1 (chốt) → 5 ý = 70s, 6 ý = 80s, 7 ý = 90s.
import os

SO = ["một", "hai", "ba", "bốn", "năm", "sáu", "bảy"]

# slug, băng chữ, hook vai phụ (None = chị đọc giấy), câu đọc giấy, mở ý (con số/sự thật), [(ý, giải thích)], chốt
TOPICS = [
    ("26-mot-dem-may-lan", "Một đêm 'mấy hiệp' mới là bình thường?",
     "Chị ơi… một đêm phải được mấy lần mới gọi là khỏe hả chị?", None,
     "Đa số đàn ông sau ba mươi tuổi chỉ một lần mỗi đêm, và vẫn hoàn toàn khỏe mạnh.",
     [("Một lần là đủ chuẩn.", "Chất lượng quan trọng hơn số lần nhiều."),
      ("Cần thời gian hồi phục.", "Sau khi xong, cơ thể cần nghỉ từ vài phút đến vài tiếng tùy tuổi."),
      ("Tuổi càng cao, nghỉ càng lâu.", "Đó là sinh lý tự nhiên, không phải yếu."),
      ("Cố quá dễ đau và mệt.", "Ép bản thân chỉ làm áp lực thêm."),
      ("Lo khi giảm đột ngột.", "Đang bình thường mà giảm hẳn thì nên đi kiểm tra.")],
     "Một lần mà cả hai vui còn hơn ba lần qua loa đó em!"),
    ("27-bao-cao-su-bi-rach", "Bao cao su bị rách thì phải làm sao?",
     None, "Em hỏi: đang dùng mà bao bị rách thì phải làm gì liền hả chị?",
     "Bình tĩnh nha em, có những việc cần làm trong vài ngày đầu là kịp.",
     [("Dừng lại ngay.", "Kiểm tra bao, thay bao mới nếu muốn tiếp tục."),
      ("Vệ sinh nhẹ nhàng.", "Rửa bằng nước sạch, không thụt rửa sâu."),
      ("Hỏi về thuốc tránh thai khẩn cấp.", "Càng sớm càng hiệu quả, hỏi dược sĩ hoặc cơ sở y tế."),
      ("Nghĩ tới chuyện lây bệnh.", "Với người chưa rõ, nên đi xét nghiệm sau vài tuần."),
      ("Lần sau chọn đúng size và hạn dùng.", "Bao chật hoặc hết hạn rất dễ rách.")],
     "Sự cố không đáng sợ, đáng sợ là không làm gì hết em ạ!"),
    ("28-co-thai-ngay-nao", "Ngày nào trong tháng dễ có thai nhất?",
     None, "Em hỏi: ngày nào trong chu kỳ thì dễ có bầu nhất hả chị?",
     "Mỗi tháng chỉ có khoảng sáu ngày là dễ có thai thôi em.",
     [("Ngày rụng trứng.", "Thường khoảng giữa chu kỳ, chu kỳ hai tám ngày thì quanh ngày mười bốn."),
      ("Năm ngày trước đó.", "Tinh trùng sống được vài ngày trong cơ thể nữ."),
      ("Dấu hiệu nhận biết.", "Dịch tiết trong và dai như lòng trắng trứng."),
      ("Que thử rụng trứng.", "Giúp đoán chính xác hơn, mua ở nhà thuốc."),
      ("Chu kỳ không đều thì khó tính.", "Đừng dựa vào đếm ngày để tránh thai.")],
     "Muốn có con thì canh ngày, muốn tránh thì đừng tin vào đếm ngày nha em!"),
    ("29-thu-thai-khi-nao", "Quan hệ bao lâu thì thử thai mới chính xác?",
     None, "Em hỏi: quan hệ xong bao lâu thì thử que mới biết chính xác chị?",
     "Thử sớm quá là nguyên nhân số một khiến que báo sai đó em.",
     [("Đợi đến ngày trễ kinh.", "Lúc này que thử mới đủ nhạy."),
      ("Ít nhất mười bốn ngày.", "Tính từ lần quan hệ nghi ngờ."),
      ("Thử bằng nước tiểu buổi sáng.", "Nồng độ hormone đậm nhất."),
      ("Một vạch chưa chắc đã không.", "Vài ngày sau thử lại nếu vẫn trễ."),
      ("Xét nghiệm máu chính xác hơn.", "Có thể biết sớm hơn que thử.")],
     "Đừng thử vội rồi lo lắng, đúng thời điểm mới có kết quả chuẩn em nhé!"),
    ("30-ban-tinh-ve-dem", "Mộng tinh có hại không?",
     None, "Em hỏi: em hay bị 'xuất' trong lúc ngủ, vậy có hại không chị?",
     "Đây là chuyện xảy ra với hầu hết con trai, nhất là tuổi dậy thì.",
     [("Là cách cơ thể tự 'xả'.", "Tinh trùng cũ được thay thế, hoàn toàn tự nhiên."),
      ("Không gây yếu sinh lý.", "Lời đồn mất sức, hao thận là sai."),
      ("Hay gặp khi kiêng lâu.", "Càng ít xuất thì càng dễ xảy ra."),
      ("Không cần chữa.", "Không phải bệnh nên không cần thuốc."),
      ("Lo khi kèm đau hoặc quá dày.", "Đêm nào cũng bị kèm mệt mỏi thì nên khám.")],
     "Mộng tinh là bình thường, đừng xấu hổ và đừng tin lời đồn nha em!"),
    ("31-lan-dau-co-dau-khong", "Lần đầu có đau không, có chảy máu không?",
     "Chị ơi… lần đầu tiên có đau lắm không, có chảy máu không chị?", None,
     "Không phải ai lần đầu cũng chảy máu đâu em, đó là hiểu lầm rất lâu đời.",
     [("Màng trinh mỗi người mỗi khác.", "Có người mỏng, có người co giãn tốt nên không chảy máu."),
      ("Đau chủ yếu do căng thẳng.", "Sợ hãi làm cơ siết lại."),
      ("Dạo đầu thật lâu.", "Giúp cơ thể thả lỏng và tự tiết dịch."),
      ("Có quyền dừng lại.", "Thấy đau thì nói, không cần cố."),
      ("Đau nhiều, chảy máu nhiều thì đi khám.", "Không nên chịu đựng.")],
     "Lần đầu nên là lúc em sẵn sàng và thoải mái nhất nha!"),
    ("32-xo-khuyen-vung-kin", "Đeo nhẫn, cài khuyên 'chỗ đó' có nguy hiểm không?",
     None, "Em hỏi: bạn em xỏ khuyên 'chỗ đó', có nguy hiểm gì không chị?",
     "Nhìn thì cá tính nhưng rủi ro thì nhiều hơn em nghĩ.",
     [("Dễ nhiễm trùng.", "Vùng ẩm, nhiều vi khuẩn, vết xỏ lâu lành."),
      ("Rách bao cao su.", "Kim loại cọ xát làm bao dễ thủng."),
      ("Gây đau cho bạn tình.", "Có thể làm trầy xước người kia."),
      ("Phải làm ở nơi uy tín.", "Dụng cụ vô trùng, chất liệu không gây dị ứng."),
      ("Sưng đỏ, chảy mủ thì đi khám.", "Không tự tháo ra khi đang viêm.")],
     "Đẹp thì đẹp, nhưng an toàn của cả hai vẫn là trên hết nha em!"),
    ("33-cuong-qua-lau", "'Đứng' hoài không xuống có nguy hiểm không?",
     None, "Em hỏi: 'cậu nhỏ' đứng mấy tiếng không chịu xuống thì có sao không chị?",
     "Cái này nghe thì vui, nhưng quá bốn tiếng là cấp cứu thật đó em.",
     [("Quá bốn tiếng là nguy hiểm.", "Máu ứ lại, mô có thể bị tổn thương vĩnh viễn."),
      ("Hay do thuốc tăng cường.", "Nhất là thuốc trôi nổi, dùng quá liều."),
      ("Đau nhức kèm theo.", "Là dấu hiệu phải đi ngay."),
      ("Không tự xử lý.", "Chườm đá hay chờ đợi có thể làm lỡ thời gian vàng."),
      ("Đến cấp cứu ngay.", "Đừng ngại, bác sĩ gặp chuyện này nhiều rồi.")],
     "Lâu quá không phải chuyện để khoe, mà là chuyện phải đi viện đó em!"),
    ("34-tinh-trung-song-bao-lau", "Tinh trùng sống được bao lâu?",
     None, "Em hỏi: tinh trùng ra ngoài rồi thì sống được bao lâu chị?",
     "Câu trả lời khác nhau rất nhiều tùy nơi tụi nó 'đáp xuống' đó em.",
     [("Trong cơ thể nữ đến năm ngày.", "Vì vậy quan hệ trước ngày rụng trứng vẫn có thể có thai."),
      ("Ngoài không khí vài phút.", "Khô đi là gần như chết hết."),
      ("Trong nước nóng bồn tắm rất ngắn.", "Lời đồn có bầu ở hồ bơi là gần như không thể."),
      ("Trên tay, trên vải.", "Còn ướt thì vẫn có thể sống ít phút."),
      ("Đông lạnh thì sống nhiều năm.", "Đó là cách ngân hàng tinh trùng lưu trữ.")],
     "Đừng xem thường mấy anh bơi lội này nha em!"),
    ("35-ham-muon-giam", "Vì sao tự nhiên hết ham muốn?",
     None, "Em hỏi: dạo này em chẳng còn hứng thú chuyện ấy, có phải bệnh không chị?",
     "Gần như ai cũng có giai đoạn này, và thường có lý do rõ ràng.",
     [("Căng thẳng công việc.", "Đầu óc mệt thì cơ thể cũng tắt máy."),
      ("Thiếu ngủ kéo dài.", "Ảnh hưởng thẳng tới hormone."),
      ("Chuyện tình cảm.", "Giận nhau, ít trò chuyện thì khó có hứng."),
      ("Một số loại thuốc.", "Thuốc chống trầm cảm, huyết áp có thể làm giảm."),
      ("Nội tiết thay đổi.", "Sau sinh, tiền mãn kinh, hay testosterone thấp ở nam."),
      ("Kéo dài thì đi khám.", "Vài tháng không cải thiện nên gặp chuyên khoa.")],
     "Không phải em hết yêu đâu, cơ thể đang cần được nghỉ thôi!"),
    ("36-mui-vung-kin", "Vùng kín có mùi thế nào là bình thường?",
     None, "Em hỏi: vùng kín có mùi hơi chua thì có sao không chị?",
     "Vùng kín khỏe mạnh vốn có mùi nhẹ, không phải không mùi đâu em.",
     [("Hơi chua là bình thường.", "Do môi trường axit bảo vệ tự nhiên."),
      ("Mùi tanh cá thì lưu ý.", "Hay gặp khi viêm do vi khuẩn."),
      ("Kèm ngứa, khí hư vón cục.", "Có thể là nấm, cần đi khám."),
      ("Đừng thụt rửa sâu.", "Làm mất lợi khuẩn, mùi càng nặng hơn."),
      ("Mặc đồ lót cotton thoáng.", "Thay hằng ngày, tránh đồ bó.")],
     "Sạch vừa đủ là khỏe, rửa quá kỹ lại hại đó em!"),
    ("37-bot-trong-nuoc-tieu", "Nước tiểu có bọt sau khi quan hệ có sao không?",
     None, "Em hỏi: xong chuyện đi tiểu thấy có bọt, vậy có bị gì không chị?",
     "Đa phần là chuyện vô hại, nhưng có một trường hợp phải để ý.",
     [("Do còn sót tinh dịch.", "Lẫn vào nước tiểu tạo bọt, hoàn toàn bình thường."),
      ("Đi tiểu mạnh, nhanh.", "Dòng chảy mạnh cũng tạo bọt."),
      ("Uống ít nước.", "Nước tiểu đặc dễ có bọt hơn."),
      ("Bọt nhiều, lâu tan, ngày nào cũng có.", "Có thể là dấu hiệu thận, nên xét nghiệm."),
      ("Kèm phù chân, mệt mỏi.", "Đi khám sớm, đừng chủ quan.")],
     "Thỉnh thoảng có bọt thì yên tâm, ngày nào cũng có thì đi khám nha em!"),
    ("38-tre-hay-xuat-som", "Vì sao lần đầu với người mới hay 'về' sớm?",
     None, "Em hỏi: sao với người mới thì em lại 'về' nhanh hơn hẳn vậy chị?",
     "Chuyện này xảy ra với rất nhiều anh, và lý do nằm ở cái đầu.",
     [("Hồi hộp quá mức.", "Tim đập nhanh, cơ thể lên đỉnh nhanh hơn."),
      ("Sợ làm không tốt.", "Càng lo càng mất kiểm soát."),
      ("Lâu rồi không gần ai.", "Kiêng lâu thì nhạy cảm hơn."),
      ("Hít thở và chậm lại.", "Đừng vội, cứ tận hưởng từng chút."),
      ("Vài lần sau sẽ ổn.", "Quen nhau rồi tự nhiên bền hơn.")],
     "Lần đầu nhanh chẳng sao, quan trọng là lần sau em nhé!"),
    ("39-ngua-vung-kin-nam", "Con trai bị ngứa vùng kín là bị gì?",
     None, "Em hỏi: em là con trai mà 'chỗ đó' cứ ngứa hoài, bị gì vậy chị?",
     "Phần lớn là do vệ sinh và nấm, dễ chữa nếu đi khám sớm.",
     [("Nấm bẹn.", "Ngứa, đỏ, viền rõ ở háng, hay gặp khi ra mồ hôi nhiều."),
      ("Mặc đồ bó, ẩm.", "Tạo môi trường cho nấm phát triển."),
      ("Viêm bao quy đầu.", "Đỏ, rát, có mùi, do vệ sinh chưa kỹ."),
      ("Dị ứng xà phòng, bao cao su.", "Đổi loại khác xem có đỡ không."),
      ("Có mụn nước, vết loét.", "Có thể là bệnh lây qua đường tình dục, đi khám ngay.")],
     "Đừng tự mua thuốc bôi lung tung, khám đúng mới hết đúng em nhé!"),
    ("40-sau-sinh-bao-lau", "Sau sinh bao lâu thì 'gần' nhau lại được?",
     None, "Em hỏi: vợ em sinh xong thì bao lâu hai vợ chồng mới gần nhau được chị?",
     "Câu này nhiều ông chồng hỏi lắm, chị trả lời luôn cho cả nhà nghe nè.",
     [("Thường sau sáu tuần.", "Để tử cung và vết thương hồi phục."),
      ("Hết sản dịch đã.", "Còn ra huyết là chưa nên."),
      ("Sinh mổ cũng cần chờ.", "Vết mổ bên trong lành chậm hơn bên ngoài."),
      ("Vẫn có thể có thai lại.", "Kể cả chưa có kinh, nên tránh thai từ lần đầu."),
      ("Quan trọng là vợ sẵn sàng.", "Mệt mỏi, mất ngủ, đau thì cần thêm thời gian.")],
     "Thương vợ thì chờ thêm chút, cả nhà đều vui em ạ!"),
    ("41-ruou-bia-va-chuyen-ay", "Uống bia rượu có làm 'lâu' hơn không?",
     None, "Em hỏi: người ta nói uống vài lon bia thì 'lâu' hơn, có đúng không chị?",
     "Một chút thì có thể bớt hồi hộp, nhưng nhiều là phản tác dụng ngay.",
     [("Rượu làm tê liệt cảm giác.", "Lâu hơn nhưng kém cảm nhận."),
      ("Say thì khó 'đứng'.", "Rượu làm giãn mạch, máu không dồn đủ."),
      ("Uống lâu ngày giảm nội tiết.", "Testosterone đi xuống, ham muốn cũng giảm."),
      ("Dễ quên biện pháp an toàn.", "Say là hay bỏ qua bao cao su."),
      ("Muốn bền thì tập luyện.", "Ngủ đủ, tập thể dục tốt hơn nhiều.")],
     "Bia rượu không phải thuốc bền, đừng tin lời đồn nha em!"),
    ("42-gym-va-sinh-ly", "Tập gym có làm khỏe chuyện ấy không?",
     None, "Em hỏi: tập gym thì chuyện ấy có khỏe hơn không chị?",
     "Có đó em, nhưng tập sai cách thì lại làm yếu đi.",
     [("Tim mạch khỏe hơn.", "Máu lưu thông tốt thì 'đứng' tốt."),
      ("Tăng nội tiết tố nam.", "Tập tạ vừa phải giúp testosterone tốt hơn."),
      ("Tự tin hơn.", "Cơ thể đẹp, tinh thần cũng thoải mái."),
      ("Tập quá sức lại phản tác dụng.", "Mệt kiệt sức thì ham muốn giảm."),
      ("Tránh thuốc tăng cơ trôi nổi.", "Có thể làm teo tinh hoàn, vô sinh.")],
     "Tập vừa đủ, ăn ngủ điều độ là khỏe toàn diện em nhé!"),
    ("43-dien-thoai-trong-tui-quan", "Để điện thoại túi quần có hại 'chuyện ấy' không?",
     "Chị ơi… em hay để điện thoại túi quần, nghe nói hại tinh trùng, có thật không?", None,
     "Câu này khoa học vẫn đang nghiên cứu, nhưng có vài điều em nên biết.",
     [("Nhiệt là thủ phạm chính.", "Tinh hoàn cần mát hơn thân nhiệt vài độ."),
      ("Ngồi lâu, mặc quần bó.", "Làm nóng vùng kín, ảnh hưởng tinh trùng."),
      ("Đặt laptop trên đùi.", "Cũng làm tăng nhiệt đáng kể."),
      ("Tắm nước quá nóng thường xuyên.", "Nên hạn chế nếu đang muốn có con."),
      ("Để điện thoại túi áo, túi xách.", "Cẩn thận vẫn hơn em ạ.")],
     "Giữ mát cho 'hai em' là cách đơn giản nhất để khỏe đó!"),
    ("44-yeu-xa-co-sao", "Lâu không quan hệ có bị 'teo' không?",
     None, "Em hỏi: lâu lắm rồi em không gần ai, vậy có bị teo hay yếu đi không chị?",
     "Nghe nhiều người lo câu này lắm, nhưng sự thật thì nhẹ nhàng hơn em nghĩ.",
     [("Không bị teo.", "Kích thước không thay đổi vì kiêng."),
      ("Cơ thể vẫn tự duy trì.", "Cương cứng ban đêm giúp mô khỏe mạnh."),
      ("Có thể nhạy cảm hơn.", "Lần đầu quay lại dễ 'về' sớm, bình thường thôi."),
      ("Lối sống mới là quan trọng.", "Ngủ, ăn, tập luyện quyết định sức khỏe sinh lý."),
      ("Mất hẳn cương ban đêm thì đi khám.", "Đó mới là dấu hiệu đáng lo.")],
     "Kiêng không làm em yếu đâu, lười vận động mới làm em yếu!"),
    ("45-thuoc-tranh-thai-tang-can", "Uống thuốc tránh thai có béo không?",
     None, "Em hỏi: uống thuốc tránh thai hằng ngày có bị tăng cân không chị?",
     "Đây là nỗi lo hàng đầu của chị em, và phần lớn là hiểu lầm đó.",
     [("Thuốc thế hệ mới ít gây tăng cân.", "Nghiên cứu không thấy khác biệt rõ ràng."),
      ("Tháng đầu có thể giữ nước.", "Hơi nặng người, thường hết sau vài tuần."),
      ("Có thể thèm ăn hơn.", "Ở một số người, cần để ý chế độ ăn."),
      ("Không hợp thì đổi loại.", "Có nhiều loại khác nhau, hỏi cơ sở y tế."),
      ("Không ngừa bệnh lây.", "Vẫn cần bao cao su với người mới.")],
     "Đừng vì sợ béo mà bỏ tránh thai, chọn đúng loại là ổn em nhé!"),
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
