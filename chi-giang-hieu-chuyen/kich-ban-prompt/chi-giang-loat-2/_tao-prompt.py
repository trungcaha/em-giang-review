# Sinh master prompt (60–90s) cho từng chủ đề "Chị ơi, cho em hỏi thầm". Chạy: python _tao-prompt.py
# Mỗi ý = 1 shot 10s. Tổng shot = 1 (hook) + số ý + 1 (chốt) → 5 ý = 70s, 6 ý = 80s, 7 ý = 90s.
import os

SO = ["một", "hai", "ba", "bốn", "năm", "sáu", "bảy"]

# slug, băng chữ, hook vai phụ (None = chị đọc giấy), câu đọc giấy, mở ý (con số/sự thật), [(ý, giải thích)], chốt
TOPICS = [
    ("16-sang-day-tu-cuong", "Sáng ngủ dậy 'cậu nhỏ' tự đứng là sao?",
     "Chị ơi… sáng nào ngủ dậy 'cậu nhỏ' cũng tự đứng, vậy có bình thường không?", None,
     "Mỗi đêm đàn ông khỏe mạnh 'đứng' khoảng ba đến năm lần mà không hề hay biết đó em.",
     [("Đó là phản xạ khi ngủ.", "Xảy ra trong giai đoạn ngủ mơ, không liên quan suy nghĩ gì cả."),
      ("Dấu hiệu mạch máu khỏe.", "Máu lưu thông tốt thì mới có hiện tượng này."),
      ("Không phải do buồn tiểu.", "Bàng quang đầy chỉ là trùng hợp, không phải nguyên nhân chính."),
      ("Tự nhiên mất thì nên để ý.", "Nhiều tuần liền không còn có thể là dấu hiệu sớm của bệnh tim mạch, tiểu đường."),
      ("Ngủ đủ mới có.", "Thiếu ngủ, căng thẳng kéo dài sẽ làm nó ít đi.")],
     "Sáng nào cũng có là cơ thể đang khỏe đó em, mừng đi!"),
    ("17-xong-la-buon-ngu", "Vì sao đàn ông 'xong' là lăn ra ngủ?",
     None, "Em hỏi: sao chồng em cứ xong chuyện là quay ra ngủ liền vậy chị?",
     "Không phải anh ấy hết thương đâu em, là do hóa chất trong não đó.",
     [("Não tiết chất gây buồn ngủ.", "Sau cao trào cơ thể tiết ra hormone làm thư giãn và díu mắt."),
      ("Cơ thể vừa vận động mạnh.", "Tim đập nhanh, cơ căng lên rồi thả lỏng nên mệt rã rời."),
      ("Thường xảy ra vào ban đêm.", "Đã mệt sẵn cả ngày, cộng thêm là ngủ ngay."),
      ("Phụ nữ thì ngược lại.", "Nhiều chị em lại tỉnh táo, muốn được ôm và trò chuyện."),
      ("Cách dung hòa.", "Ôm nhau vài phút trước khi ngủ, cả hai đều vui.")],
     "Ngủ ngay là bình thường, nhưng nhớ ôm vợ một chút đã nha!"),
    ("18-tinh-dich-mau-vang-loang", "Tinh dịch loãng, màu vàng có sao không?",
     None, "Em hỏi: tinh dịch của em lúc loãng lúc vàng, vậy có bệnh không chị?",
     "Màu và độ đặc thay đổi theo từng lần là chuyện rất bình thường em ạ.",
     [("Màu trắng đục là chuẩn.", "Hơi ngà, đặc lúc đầu rồi loãng ra sau vài chục phút."),
      ("Loãng vì xuất nhiều lần.", "Xuất liên tục vài ngày thì loãng hơn, nghỉ vài hôm lại đặc."),
      ("Hơi vàng thường do kiêng lâu.", "Hoặc do ăn uống, uống ít nước, thường không đáng lo."),
      ("Vàng đậm kèm mùi hôi, đau buốt.", "Có thể là viêm nhiễm, nên đi khám."),
      ("Có máu, màu hồng nâu.", "Đừng chủ quan, phải gặp nam khoa sớm.")],
     "Đa số là bình thường, chỉ lo khi kèm đau hay có máu thôi em!"),
    ("19-cau-nho-bi-cong", "'Cậu nhỏ' bị cong có sao không?",
     None, "Em hỏi: 'cậu nhỏ' của em hơi cong sang một bên, có bị gì không chị?",
     "Gần như không ai thẳng tắp hoàn toàn đâu em, cong nhẹ là chuyện phổ biến.",
     [("Cong nhẹ là bẩm sinh.", "Lệch trái, lệch phải, hướng lên đều bình thường."),
      ("Không ảnh hưởng chuyện ấy.", "Không đau, không vướng thì không cần làm gì."),
      ("Cong dần theo thời gian thì lưu ý.", "Đang thẳng mà cong dần là dấu hiệu cần khám."),
      ("Kèm đau hoặc sờ thấy cục cứng.", "Có thể là bệnh lý mô sẹo, điều trị được."),
      ("Đừng tự nắn hay dùng dụng cụ.", "Dễ gây tổn thương, còn tệ hơn.")],
     "Cong nhẹ mà không đau thì cứ tự tin lên em nhé!"),
    ("20-xuat-ngoai-co-bau-khong", "Xuất ngoài có tránh thai được không?",
     "Chị ơi… tụi em toàn xuất ra ngoài, vậy có dính bầu được không?", None,
     "Cứ khoảng năm cặp dùng cách này thì có một cặp dính bầu trong một năm đó em.",
     [("Dịch tiền xuất tinh.", "Chảy ra trước cả lúc 'xong', có thể mang theo tinh trùng."),
      ("Rút không kịp.", "Chỉ cần chậm một giây là đủ chuyện."),
      ("Xuất gần cửa mình vẫn có rủi ro.", "Tinh trùng bơi rất giỏi đó em."),
      ("Không ngừa được bệnh.", "Các bệnh lây qua đường tình dục vẫn lây như thường."),
      ("Cách an toàn hơn.", "Bao cao su hoặc biện pháp lâu dài, hỏi cơ sở y tế cho phù hợp.")],
     "Xuất ngoài là đánh cược đó em, đừng phó mặc cho may rủi!"),
    ("21-kich-thuoc-trung-binh", "Kích thước trung bình thật sự là bao nhiêu?",
     None, "Em hỏi: kích thước trung bình của đàn ông Việt thật ra là bao nhiêu hả chị?",
     "Phần lớn đàn ông đều nghĩ mình nhỏ hơn người khác, mà thật ra là bình thường.",
     [("Lúc đứng khoảng mười hai, mười ba phân.", "Nghiên cứu ở người châu Á cho con số quanh mức này."),
      ("Lúc nghỉ thì không nói lên gì.", "Có người lúc nghỉ nhỏ nhưng lúc đứng tăng nhiều."),
      ("Nhìn từ trên xuống bị ngắn đi.", "Góc nhìn và mỡ bụng làm mình tưởng nhỏ."),
      ("Phụ nữ không quá quan trọng chuyện đó.", "Phần lớn cảm giác nằm ở sự quan tâm và dạo đầu."),
      ("Đừng mua thuốc tăng size.", "Không có tác dụng, lo lắng quá thì đi khám nam khoa.")],
     "Đủ là đủ rồi em, tự tin mới là size lớn nhất!"),
    ("22-di-tieu-sau-quan-he", "Vì sao nên đi tiểu ngay sau khi quan hệ?",
     None, "Em hỏi: người ta hay bảo xong chuyện phải đi tiểu ngay, có đúng không chị?",
     "Đúng đó em, đây là thói quen nhỏ mà phòng được bệnh rất hay gặp.",
     [("Đẩy vi khuẩn ra ngoài.", "Vi khuẩn dễ bị đẩy vào niệu đạo trong lúc gần nhau."),
      ("Phụ nữ càng cần.", "Niệu đạo nữ ngắn nên dễ viêm đường tiểu hơn nhiều."),
      ("Đi trong vòng ba mươi phút.", "Không cần vội chạy ngay, nhưng đừng để quá lâu."),
      ("Không tránh thai được.", "Đi tiểu không đẩy tinh trùng ra, đừng hiểu nhầm nha."),
      ("Rửa nhẹ bằng nước sạch.", "Không thụt rửa sâu, không dùng xà phòng mạnh.")],
     "Một lần đi tiểu, đỡ cả tháng khổ sở đó em!"),
    ("23-quan-he-ky-kinh", "Quan hệ trong kỳ kinh có sao không?",
     None, "Em hỏi: đến tháng mà hai vợ chồng vẫn gần nhau thì có sao không chị?",
     "Câu này nhiều chị em ngại hỏi lắm, nên chị trả lời luôn nè.",
     [("Vẫn có thể có bầu.", "Ít thôi, nhưng chu kỳ ngắn thì rủi ro không phải bằng không."),
      ("Dễ viêm nhiễm hơn.", "Cổ tử cung hé mở, vi khuẩn dễ đi vào."),
      ("Dễ lây bệnh qua máu.", "Nên dùng bao, nhất là khi chưa xét nghiệm."),
      ("Có người lại đỡ đau bụng.", "Cơ thể thư giãn có thể làm dịu cơn co thắt."),
      ("Quan trọng là cả hai thoải mái.", "Ai không muốn thì tôn trọng, chờ vài ngày cũng được.")],
     "Không cấm, nhưng sạch sẽ và an toàn phải đi đầu nha em!"),
    ("24-phu-nu-co-xuat-khong", "Phụ nữ có 'xuất' như đàn ông không?",
     None, "Em hỏi: phụ nữ lúc lên đỉnh có 'xuất' ra giống đàn ông không chị?",
     "Câu này làm bao nhiêu anh tò mò, và câu trả lời là: có thể, nhưng không phải ai cũng vậy.",
     [("Ướt là phản ứng bình thường.", "Cơ thể tự tiết dịch để thoải mái hơn, không phải 'xuất'."),
      ("Một số chị em có tiết dịch mạnh.", "Khá hiếm và hoàn toàn bình thường."),
      ("Không có nghĩa là sướng hơn.", "Không có cũng chẳng phải là chưa tới."),
      ("Đừng so với phim.", "Phim người lớn phóng đại rất nhiều."),
      ("Hỏi nhau thay vì đoán.", "Mỗi người mỗi khác, nói chuyện là cách hiểu nhau nhanh nhất.")],
     "Mỗi cơ thể một kiểu, đừng ép theo chuẩn của ai em nhé!"),
    ("25-dau-sau-quan-he", "Sau khi quan hệ bị đau, có sao không?",
     "Chị ơi… lần nào xong em cũng thấy đau rát, vậy có bình thường không?", None,
     "Đau thì không phải chuyện phải chịu đựng đâu em, cơ thể đang báo hiệu đó.",
     [("Khô quá.", "Dạo đầu chưa đủ hoặc thiếu bôi trơn rất dễ gây rát."),
      ("Quá mạnh, quá lâu.", "Cọ xát nhiều làm trầy xước nhẹ."),
      ("Dị ứng bao hoặc gel.", "Đổi loại khác xem có đỡ không."),
      ("Viêm nhiễm.", "Kèm ngứa, khí hư lạ, mùi hôi thì phải đi khám."),
      ("Đau sâu bên trong.", "Có thể liên quan buồng trứng, tử cung, đừng để lâu.")],
     "Đừng im lặng chịu đau, nói với người ấy và đi khám nếu cần nha em!"),
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
