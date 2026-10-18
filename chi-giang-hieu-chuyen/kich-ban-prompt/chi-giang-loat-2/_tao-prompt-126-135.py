# Sinh master prompt (60–90s) cho từng chủ đề "Chị ơi, cho em hỏi thầm". Chạy: python _tao-prompt.py
# Mỗi ý = 1 shot 10s. Tổng shot = 1 (hook) + số ý + 1 (chốt) → 5 ý = 70s, 6 ý = 80s, 7 ý = 90s.
import os

SO = ["một", "hai", "ba", "bốn", "năm", "sáu", "bảy"]

# slug, băng chữ, hook vai phụ (None = chị đọc giấy), câu đọc giấy, mở ý (con số/sự thật), [(ý, giải thích)], chốt
def T(slug, title, hook, card, fact, pts, close):
    return (slug, title, hook, card, fact, pts, close)

TOPICS = [
    T("126-dem-day-tieu-nhieu-lan", "Đêm dậy tiểu ba bốn lần là bị gì?",
      "Chị ơi… chồng em đêm nào cũng dậy đi tiểu ba bốn lần, em lo quá!", None,
      "Ngoài năm mươi, cứ hai anh thì có một anh tuyến tiền liệt bắt đầu to ra.",
      [("Dậy từ hai lần trở lên là nên để ý.", "Một lần thì chưa đáng lo."),
       ("Tuyến tiền liệt to chèn đường tiểu.", "Nên tiểu rắt, tia yếu, tiểu không hết."),
       ("Tối bớt nước, trà, bia.", "Nhất là hai tiếng trước khi ngủ."),
       ("Cũng có thể do tiểu đường.", "Khát nhiều, tiểu nhiều thì thử đường huyết."),
       ("Bí tiểu, tiểu ra máu.", "Thì đi khám ngay, đừng ráng chịu.")],
      "Tiểu đêm không phải chuyện tuổi già phải chịu, đi khám sớm cho ngủ ngon em nhé!"),
    T("127-phi-dai-tien-liet-tuyen-va-chuyen-ay", "Tuyến tiền liệt to có làm 'yếu' không?",
      None, "Em hỏi: em bị phì đại tuyến tiền liệt, vậy chuyện vợ chồng có bị ảnh hưởng không chị?",
      "Phì đại tuyến tiền liệt là lành tính, không phải ung thư đâu em.",
      [("Bản thân nó không làm mất bản lĩnh.", "Nhiều anh vẫn sinh hoạt bình thường."),
       ("Tiểu đêm làm mất ngủ.", "Mất ngủ lâu ngày mới làm xuống sức."),
       ("Một số thuốc điều trị có ảnh hưởng.", "Giảm ham muốn hoặc xuất ra ít hơn."),
       ("Thấy khác thì nói với bác sĩ.", "Có thể đổi thuốc, đừng tự ngưng."),
       ("Đừng mua thuốc trôi nổi trên mạng.", "Tiền mất mà bệnh không bớt.")],
      "Bệnh này sống chung được, đừng vì ngại mà bỏ luôn chuyện vợ chồng em nhé!"),
    T("128-mat-chao-co-buoi-sang", "Sáng dậy không còn 'chào cờ' có đáng lo?",
      None, "Em hỏi: em năm mươi hai tuổi, dạo này sáng dậy không còn 'chào cờ' nữa, có sao không chị?",
      "Buổi sáng còn 'chào cờ' là dấu hiệu mạch máu và thần kinh còn tốt đó em.",
      [("Thưa dần theo tuổi là bình thường.", "Không còn đều như thời hai mươi."),
       ("Mất hẳn nhiều tuần thì nên để ý.", "Có thể do mạch máu hoặc nội tiết."),
       ("Có khi báo trước bệnh tim mạch.", "Mạch máu ở đó nhỏ nên tắc sớm hơn."),
       ("Thiếu ngủ, rượu bia, căng thẳng.", "Cũng làm mất tạm thời."),
       ("Đi kiểm tra tổng quát.", "Đường huyết, mỡ máu, huyết áp, nội tiết tố nam.")],
      "Cơ thể đang nhắn tin cho mình đó, đừng lơ nó em nhé!"),
    T("129-thuoc-huyet-ap-va-sinh-ly", "Uống thuốc huyết áp có bị 'yếu' đi không?",
      "Chị ơi… chồng em nói uống thuốc huyết áp bị yếu nên đòi bỏ thuốc, phải làm sao?", None,
      "Chính huyết áp cao mới làm hư mạch máu, hại chuyện ấy nhiều hơn thuốc đó em.",
      [("Không phải thuốc nào cũng ảnh hưởng.", "Chỉ một số loại, và không phải ai cũng bị."),
       ("Tuyệt đối không tự bỏ thuốc.", "Bỏ thuốc dễ đột quỵ."),
       ("Nói thật với bác sĩ.", "Bác sĩ đổi sang loại khác phù hợp hơn."),
       ("Không tự uống thuốc tăng lực.", "Đang dùng thuốc tim mạch thì rất nguy hiểm."),
       ("Bớt mặn, đi bộ, giảm cân.", "Huyết áp ổn thì chuyện ấy cũng ổn theo.")],
      "Giữ được mạng trước rồi mới giữ được lửa, đừng bỏ thuốc em nhé!"),
    T("130-bung-bia-va-sinh-ly", "Bụng bia có làm đàn ông 'xuống sức' không?",
      None, "Em hỏi: bụng em ngày càng to, chuyện ấy ngày càng đuối, có liên quan không chị?",
      "Đàn ông mình vòng bụng quá chín mươi phân là nên bắt đầu lo rồi đó em.",
      [("Mỡ bụng làm giảm nội tiết tố nam.", "Bụng càng to, ham muốn càng giảm."),
       ("Hay kéo theo tiểu đường, mỡ máu.", "Làm hư mạch máu nuôi 'cậu nhỏ'."),
       ("Giảm năm đến mười phần trăm cân nặng.", "Là đã thấy cải thiện rõ."),
       ("Bớt bia, bớt cơm tối.", "Không cần nhịn đói khổ sở."),
       ("Đi bộ nhanh ba mươi phút mỗi ngày.", "Rẻ mà hiệu quả hơn thuốc bổ.")],
      "Bụng nhỏ lại một chút là phong độ lên một chút em nhé!"),
    T("131-that-ong-dan-tinh-co-yeu-khong", "Thắt ống dẫn tinh xong có bị 'yếu' không?",
      None, "Em hỏi: vợ chồng em đủ con rồi, em tính đi thắt ống dẫn tinh mà sợ yếu, có sao không chị?",
      "Thắt ống dẫn tinh chỉ chặn đường đi của tinh trùng, không đụng gì tới nội tiết.",
      [("Không làm yếu đi.", "Ham muốn và độ cứng vẫn như cũ."),
       ("Vẫn xuất ra bình thường.", "Tinh trùng chỉ chiếm một phần rất nhỏ."),
       ("Thủ thuật nhỏ, về trong ngày.", "Làm khoảng mười lăm đến hai mươi phút."),
       ("Chưa có tác dụng ngay.", "Khoảng ba tháng, xét nghiệm lại mới yên tâm."),
       ("Không ngừa được bệnh lây.", "Cần thì vẫn phải dùng bao.")],
      "Đàn ông chủ động ngừa thai là thương vợ đó em!"),
    T("132-vo-man-kinh-ne-chong", "Vợ qua tuổi năm mươi cứ né chồng, vì sao?",
      None, "Em hỏi: vợ em qua tuổi năm mươi là cứ né chồng, có phải bả hết thương em không chị?",
      "Phần lớn không phải hết thương đâu em, mà là cơ thể phụ nữ đang đổi khác.",
      [("Mãn kinh làm nội tiết giảm mạnh.", "Gây khô, rát, đau khi gần nhau."),
       ("Bốc hỏa, mất ngủ.", "Người mệt thì không còn hứng thú."),
       ("Gel bôi trơn giúp rất nhiều.", "Và dạo đầu lâu hơn hồi trẻ."),
       ("Hỏi han chứ đừng trách.", "Càng trách vợ càng né."),
       ("Đưa vợ đi khám phụ khoa.", "Có cách điều trị khô rát hiệu quả.")],
      "Hiểu vợ thêm một chút là vợ chồng gần lại liền em nhé!"),
    T("133-ngu-ngay-va-sinh-ly", "Ngủ ngáy to có liên quan chuyện 'yếu' không?",
      "Chị ơi… chồng em ngáy như sấm, có lúc nín thở luôn, mà dạo này ổng cũng yếu hẳn!", None,
      "Ngáy to rồi ngưng thở từng cơn làm cơ thể thiếu ô xy suốt cả đêm đó em.",
      [("Thiếu ô xy làm giảm nội tiết tố nam.", "Ngủ đủ giờ mà vẫn xuống sức."),
       ("Sáng dậy mệt, ban ngày buồn ngủ.", "Là dấu hiệu rất hay gặp."),
       ("Tăng nguy cơ huyết áp, tim mạch.", "Không chỉ là chuyện ồn ào."),
       ("Giảm cân, nằm nghiêng, tối bớt rượu.", "Giúp đỡ ngáy thấy rõ."),
       ("Có cơn ngưng thở thì đi đo giấc ngủ.", "Điều trị xong nhiều anh khỏe lại hẳn.")],
      "Ngủ cho ngon thì ban ngày lẫn ban đêm đều khỏe em nhé!"),
    T("134-tuoi-nam-muoi-bao-lau-mot-lan", "Tuổi năm mươi, bao lâu 'gần' vợ một lần là vừa?",
      None, "Em hỏi: em năm mươi lăm tuổi, một tuần gần vợ mấy lần là vừa sức hả chị?",
      "Không có con số chuẩn nào cho mọi cặp vợ chồng hết đó em.",
      [("Mỗi tuần một lần hay mỗi tháng vài lần.", "Ở tuổi này đều là bình thường."),
       ("Chất lượng hơn số lượng.", "Cả hai vui là được."),
       ("Cần nghỉ lâu hơn hồi trẻ.", "Có khi một hai ngày mới sẵn sàng lại."),
       ("Đều đặn tốt hơn dồn dập.", "Giữ nhịp thì bền lâu."),
       ("Hôm sau mệt lả, đau lưng.", "Là đang quá sức, nên giãn ra.")],
      "Vừa sức mình, vui lòng vợ, vậy là đúng số rồi em!"),
    T("135-tam-soat-tuyen-tien-liet", "Tuổi nào nên đi tầm soát tuyến tiền liệt?",
      None, "Em hỏi: em năm mươi tuổi, chưa thấy gì lạ, có cần đi kiểm tra tuyến tiền liệt không chị?",
      "Ung thư tuyến tiền liệt lúc mới bị gần như không có dấu hiệu gì hết đó em.",
      [("Từ năm mươi tuổi nên hỏi bác sĩ.", "Về chuyện tầm soát định kỳ."),
       ("Cha hoặc anh em ruột từng bị.", "Thì nên đi sớm hơn, từ bốn mươi lăm tuổi."),
       ("Chỉ cần xét nghiệm máu.", "Gọi là chỉ số P S A, làm rất nhanh."),
       ("Chỉ số cao chưa chắc là ung thư.", "Viêm hay phì đại cũng làm tăng."),
       ("Tiểu ra máu, đau xương kéo dài.", "Thì đi khám ngay, đừng chờ.")],
      "Một lần xét nghiệm đổi lấy nhiều năm yên tâm, đáng lắm em nhé!"),
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
