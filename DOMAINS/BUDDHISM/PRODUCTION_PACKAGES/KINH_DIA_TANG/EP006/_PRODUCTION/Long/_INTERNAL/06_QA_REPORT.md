---
schema_version: 1.0
asset_id: AST_EP006_QA_REPORT
asset_type: qa_report
episode_id: EP_BUD_KDT_006
package_id: PKG_BUD_KDT_EP006
domain_id: BUD
series_id: SB_BUD_001
version: 0.1.0
language: vi
canonical: true
reviewed_asset: _INTERNAL/03_AUDIO_SCRIPT_MASTER.md
reviewed_asset_version: 0.1.0
qa_date: 2026-07-17
qa_role: independent_reviewer
overall_verdict: PASS
---

# 06 QA Report — EP006 "Địa Ngục Trong Kinh: Thật Hay Biểu Tượng?"

## Phương pháp

Đọc toàn bộ `03_AUDIO_SCRIPT_MASTER.md` (10.312 từ, đọc trọn vẹn, không lướt) độc lập, đối chiếu với `01_RESEARCH_BRIEF.md`, `02_EPISODE_PLANNER.md` (13 beat + Two-Layer Interweaving Map + Risk Controls), `DOMAIN_QA_POLICY.md`, `CORE_OS/BRAND_BIBLE.md`, `CONTINUITY_REGISTRY.md`, và `KP_BUD_001_Kinh_Dia_Tang.md` Chapter 5–6 (Narrative detail, Production cautions, Script-ready material). Đây là tập rủi ro cao nhất mùa (địa ngục) nên áp mức khắt khe nhất, không mặc định nội dung đúng. Đã chạy đếm từ chương trình (PowerShell) để xác minh `word_count` và quét regex để xác nhận không có ký tự markdown lọt vào khối narration.

## A. Giật gân/hù dọa — PASS

- Không có mô tả vật lý/graphic của bất kỳ hình phạt nào ở bất kỳ đâu trong 10.312 từ. Các tên địa ngục (dòng 146, 152, 158, 172) chỉ đi kèm TÊN + Ý NGHĨA NGHIỆP, không dựng cảnh, không dụng cụ hành hình, không mô tả đau đớn thể xác.
- Dòng 166: "Lưỡi bị cày, vì chính lưỡi ấy đã cày xới người khác bằng lời nói. Mắt bị hại, vì chính mắt ấy đã nhìn người khác bằng ác ý. Máu bị lấy đi, vì chính bàn tay ấy đã lấy đi máu của kẻ khác." — đây là điểm cần ghi nhận (không phải FAIL): đây là mức mô tả trừu tượng nhất có thể trong khi vẫn nêu được nguyên lý nhân quả tương ứng; không có máu me/cảnh tượng cụ thể, chỉ là câu văn nguyên lý. Trong khung "chỉ tên + ý nghĩa nghiệp" mà brief yêu cầu, câu này vẫn ở bên trong ranh giới an toàn.
- Dòng 170: kịch bản chủ động phủ định cá nhân hóa đe dọa — "đây không phải một lời cảnh báo dành riêng cho bạn, không phải một phép tính 'nếu bạn từng làm X, thì Y đang chờ.'" Khớp yêu cầu cấm tuyệt đối "if you do X you go to hell Y" của `KP_BUD_001` dòng 436 và Risk Flags của brief.
- Beat 6 (dòng 164) và các đoạn nặng khác đều có khoảng lặng chủ động được viết ngay trong lời đọc ("Xin cho phép một khoảng lặng ở đây...") — không dùng ngôn ngữ kịch tính/kinh dị, không có nhạc/hiệu ứng được gợi ý trong narration.
- Beat 7 (mô-típ lửa + thú, dòng 172–190): xử lý hoàn toàn ở tầng ẩn dụ nội tâm (cơn giận, cuồng vọng), không mô tả con thú hay lửa như một cảnh tượng — đúng "Tertiary motif" đã hoạch định.

## B. Cân bằng hai lớp đọc — PASS

- Câu neo chuyển lớp xuất hiện nhất quán, đúng mẫu planner yêu cầu: "Ở lớp tín ngưỡng truyền thống..." (dòng 72), "bên cạnh vị trí vũ trụ luận này..." (dòng 94), "Ở lớp tín ngưỡng... Ở lớp tâm lý..." (dòng 148, 152–156, 158–162), "Bên cạnh ý nghĩa tín ngưỡng..." (dòng 178).
- Không tìm thấy câu nào dùng cấu trúc cấm "thực ra chỉ là..." để hạ một lớp xuống hàng phụ. Dòng 130 chủ động phủ định chính cấu trúc đó: "Đây không phải một cách nói giảm nhẹ, không phải một lối thoát được thêm vào để xoa dịu người không tin, không phải một sự nhượng bộ hiện đại..."
- Dòng 64: "Không cách đọc nào bị coi là 'thật ra chỉ là' cách đọc kia. Đó là nguyên tắc duy nhất tập này giữ chặt từ đầu đến cuối." — tuyên ngôn biên tập được đặt ngay từ Beat 1 và được giữ xuyên suốt.
- Kiểm tra 2 chiều nghiêng: không có đoạn nào ngụ ý người tin nghĩa đen là mê tín (đối lập lại còn có dòng 86, 130 khẳng định lớp tín ngưỡng "không kém phần thật"); không có đoạn nào ngụ ý lớp tâm lý là "dành cho người không đủ đức tin" (dòng 140 khẳng định "hữu danh vô hình" "xác nhận điều đó, không phủ nhận nó" đối với người tin nghĩa đen, và mở lớp tâm lý như một lựa chọn hợp lệ song song).
- Beat 13 (dòng 290) đóng tập bằng cách đặt cả hai lớp đọc cạnh nhau minh bạch, không chọn phe: "Với người tin theo nghĩa đen... Với người đọc theo hướng tâm lý, biểu tượng..." — đúng payoff callback đã hoạch định.

## C. Beat 11 (risk control giới tính/địa vị) — PASS

- Vị trí: dòng 244–263 (~850 từ theo ước tính), khớp planner (~850–950 từ), không bị nén thành mệnh đề phụ.
- Cấu trúc đúng 3 bước bắt buộc: (1) nêu lợi ích chọn lọc ít rủi ro trước, gắn khung "theo truyền thống mô tả... không phải một cam kết cơ học" (dòng 246); (2) nêu đoạn thân nữ/thuộc hạ tiện ngắn gọn (dòng 250); (3) khung lịch sử-xã hội gắn NGAY LẬP TỨC, không trì hoãn — dòng 252: "Xin được nói điều này thật rõ ràng, thật chắc chắn, không mập mờ: đoạn kinh này phản ánh vũ trụ luận và bối cảnh xã hội của Ấn Độ và Đông Á thời cổ đại... Đây không phải, và không nên được đọc như, một giáo lý về giá trị nội tại của giới tính, hay giá trị nội tại của địa vị xã hội, trong Phật học đương đại."
- Dòng 254 nói thẳng, không mập mờ: "kinh không dạy rằng thân nữ có giá trị thấp hơn thân nam. Kinh không dạy rằng một người ở địa vị thấp kém trong xã hội có giá trị con người thấp hơn người ở địa vị cao." — không đọc được như khẳng định nữ giới/địa vị thấp kém là thật, ngược lại chủ động bác bỏ cách đọc đó hai lần liên tiếp (dòng 252, 254, 256).
- Dòng 262 có một câu trực tiếp trấn an người xem có thể mang giới hạn xã hội tương tự ("Nếu bạn là người mang trong mình một phần của những giới hạn ấy...") — vượt yêu cầu tối thiểu của planner, tăng cường an toàn thay vì chỉ đủ mức.
- Giọng "nói thẳng, ít ẩn dụ" đúng Audio Direction cho Beat 11 — câu ngắn hơn, dứt khoát hơn so với phần còn lại của tập, dễ phân biệt bằng tai khi nghe.
- Mục thai nhi/trẻ sơ sinh trong danh sách Ch.6 KHÔNG được dùng (đúng Editorial Notes dòng 31 — quyết định biên tập chủ động để giữ Beat 11 gọn, tránh mở chủ đề mất mát thai sản không cần thiết cho luận điểm chính) — xác nhận qua toàn văn, không tìm thấy nội dung cầu nguyện cho thai nhi/trẻ sơ sinh ở đâu trong narration.

## D. Độ chính xác giáo lý (đối chiếu KP_BUD_001 Chapter 5–6) — PASS, có 1 ghi nhận nhỏ

- Mục đích thỉnh cầu của Phổ Hiền (dòng 70–72) khớp chính xác KP dòng 418, 442: vì lợi ích tám bộ chúng và chúng sinh hiện tại/tương lai, để "biết sợ nghiệp ác mà quy y Tam Bảo."
- Câu "dù trải qua kiếp số cũng không nói hết" (dòng 106) khớp nguyên văn tinh thần KP dòng 449 ("could not be finished even in an eon").
- Vị trí vũ trụ luận (dòng 84): núi Đại Thiết Vi, phía Đông Tu Di, Diêm Phù Đề, ánh sáng mặt trời/mặt trăng không chiếu tới — khớp KP dòng 442 nguyên văn.
- Vô Gián/Đại A Tỳ + hàng chục địa ngục phụ + vô số tiểu ngục (dòng 88) khớp cấu trúc KP dòng 427, 442 (Avici, Maha Avici, dozens of named sub-hells, uncountable smaller hells).
- Ba tên địa ngục được chọn (Cày Lưỡi/Kéo Lưỡi, Mổ Mắt, Uống Máu, dòng 146–162) và mô-típ lửa+thú (chó lửa, ngựa lửa, trâu lửa, voi lửa, dòng 172) đều nằm trong đúng danh sách KP dòng 442 (Plowing Tongues, Pecking Eyes, Drinking Blood, fire dog/horse/ox/elephant) — không có tên bịa đặt.
- Nguyên lý "hữu danh vô hình": được gắn nhãn nguồn rõ ràng ngay tại lần giới thiệu đầu tiên (dòng 122): "trong truyền thống chú giải kinh Địa Tạng — cụ thể là một dòng giảng giải rất được trân trọng, gắn liền với Hòa thượng Tuyên Hóa và đạo tràng Vạn Phật Thánh Thành... không phải một câu được trích nguyên văn trực tiếp từ chính văn bản kinh." Khớp chính xác KP dòng 428, 437 ("Commentarial tradition (notably Hsuan Hua's teaching)... an interpretive option").
- **Ghi nhận nhỏ (không phải FAIL):** Editorial Notes (dòng 25) tuyên bố việc gắn nhãn nguồn chú giải "never dropped in later callbacks (Beat 10, Beat 12)". Trên thực tế, các lần gọi lại nguyên lý ở Beat 10 (dòng 240: "cùng một logic đã gặp ở phần trước, khi nói về 'hữu danh vô hình'") và Beat 12 (dòng 264: "nguyên lý trung tâm của tập này — 'hữu danh vô hình'") không lặp lại cụm từ gắn nhãn nguồn ("theo truyền thống chú giải Tuyên Hóa/Vạn Phật Thánh Thành") — chỉ tham chiếu ngược về khái niệm đã lập nền ở Beat 5. Vì đây là narration tuyến tính (người xem đã nghe Beat 5 trước khi tới Beat 10/12), rủi ro hiểu lầm là thấp, nhưng câu tuyên bố trong Editorial Notes hơi quá so với thực tế văn bản. Không cần sửa bắt buộc — chỉ nêu để hồ sơ QA chính xác.
- Danh sách lợi ích Ch.6 dùng (30 kiếp, trai giới bảo hộ gia trạch, thân nữ, thuộc hạ tiện — dòng 246, 250) khớp đúng nội dung và số liệu KP dòng 477 (thirty kalpas, protects household, women avoiding female rebirth, humble/servile standing). Không có số liệu bịa.
- Không dùng "Diêm La Vương", không nhắc "Mục Kiền Liên Thánh", không kể lại Thánh Nữ/Quang Mục trong khối narration (đã grep toàn văn xác nhận — các tên này chỉ xuất hiện trong Editorial Notes, không tính).

## E. Không lặp motif — PASS

- "Ngưỡng cửa" — grep toàn file: chỉ xuất hiện trong Editorial Notes (dòng 27, nói về việc KHÔNG dùng nó), không xuất hiện một lần nào trong khối narration.
- Trục ánh sáng/bóng tối và "hơi sương ngưng thành hình" được dùng đúng như planner hoạch định: "sương" xuất hiện có chủ đích ở Beat 5 (dòng 134–138, giới thiệu), một câu callback ngắn ở Beat 8 (dòng 204, phần tổng hợp — hợp lý vì đang tổng kết các hình ảnh đã dùng) và callback đầy đủ ở Beat 12 (dòng 278–280) — đúng cấu trúc "gieo một lần, gọi lại có chủ đích" của Callback and Payoff map, không phải lặp ngẫu nhiên.
- Không tìm thấy ẩn dụ nào khác được dùng lặp quá mức ngoài kế hoạch (tích trượng/minh châu của EP001 không xuất hiện; không có ẩn dụ mới nào bị lặp lại 3 lần+ ngoài trục sáng/tối và sương đã được hoạch định).

## F. Nhịp điệu/chất lượng cho 10K từ — PASS

- Không phát hiện đoạn nào bị loãng/lặp ý thuần túy không thêm thông tin. Các điểm có vẻ "lặp lại" (Beat 8 tổng hợp bốn lăng kính, Beat 10 nhắc lại "hữu danh vô hình") đều là các điểm tổng hợp/ứng dụng có chủ đích cấu trúc theo planner (NP039 Nuance→Relevance), không phải padding.
- Khoảng thở: có điểm dừng tường minh trong lời đọc sau đoạn nặng nhất (dòng 164, sau ba tên địa ngục Beat 6: "Xin cho phép một khoảng lặng ở đây...") và một điểm lùi lại rõ ràng mở đầu Beat 8 (dòng 192: "có lẽ là lúc nên dừng lại một chút, lùi ra xa..."), phục vụ đúng cả Beat 6 lẫn Beat 7 theo yêu cầu Audio Direction ("pause after difficult truths... đặc biệt sau Beat 6 và Beat 7").
- Cấu trúc 13 beat của planner được bám sát đúng thứ tự, đúng nội dung cốt lõi từng beat (đối chiếu Beat 1→13 với `02_EPISODE_PLANNER.md` — không có beat nào bị bỏ, đảo thứ tự, hay trộn lẫn).
- Không có đoạn nào rơi vào giọng kịch tính/rộn ràng không phù hợp — toàn bộ giữ đúng "chậm, gần, chiêm nghiệm" kể cả ở đoạn ánh sáng Ch.6 (đúng ghi chú Audio Direction "không chuyển sang hào hứng/rộn ràng").

## G. Format kỹ thuật — PASS

- `<!-- NARRATION_START -->` (dòng 42) và `<!-- NARRATION_END -->` (dòng 306) có mặt, đúng cặp, bao trọn nội dung đọc.
- Đếm từ bằng script (PowerShell, whitespace split) trên đúng khối narration: **10.312 từ**, khớp chính xác `word_count: 10312` khai báo trong frontmatter. Nằm trong khung mục tiêu 9500–11500 từ.
- Quét regex `[#*_\[\]` ` ]` trên khối narration: **0 kết quả** — không có ký tự/cú pháp markdown nào lọt vào lời đọc.
- Không có nhãn "Beat n" hay chú thích sản xuất nào lọt vào trong khối narration (toàn bộ nằm trong Editorial Notes, đúng yêu cầu "Do not place production notes inside the narration markers").

## Tổng kết

Không phát hiện FAIL ở bất kỳ mục nào trong 7 mục kiểm tra (A–G), kể cả ba mục rủi ro cao nhất của tập (A — giật gân/hù dọa, B — cân bằng hai lớp đọc, C — Beat 11 giới tính/địa vị). Kịch bản tuân thủ chặt các ranh giới bắt buộc: không mô tả graphic bạo lực, không cá nhân hóa đe dọa, giữ cả hai lớp đọc song song xuyên suốt không thiên lệch, xử lý đoạn nữ giới/địa vị với khung lịch sử gắn ngay lập tức và không rút gọn, không bịa số liệu/tên địa ngục, không lặp ẩn dụ "ngưỡng cửa" đã dùng ở 3 tập trước, word_count khớp và không có markdown lọt vào narration.

Một ghi nhận nhỏ duy nhất (mục D) về việc Editorial Notes hơi phóng đại mức độ lặp lại nhãn nguồn "hữu danh vô hình" ở các callback — không đạt ngưỡng cần sửa bắt buộc (không phải sai giáo lý, không gây hiểu lầm nghiêm trọng trong ngữ cảnh narration tuyến tính).

**Không thực hiện sửa đổi nào lên `03_AUDIO_SCRIPT_MASTER.md`.** Kịch bản đạt yêu cầu để tiến sang bước kế tiếp trong pipeline QA (Research QA cần xác nhận bản dịch Việt ngữ chuẩn cho tên các tiểu ngục trước khi khóa kịch bản cuối, theo giới hạn (a) đã ghi trong Research Confidence Summary của `01_RESEARCH_BRIEF.md` — đây là việc của Research QA, không phải một lỗi an toàn/nội dung cần sửa ở vòng này).

### Ghi chú không bắt buộc (không phải lỗi QA)

1. Nếu muốn hồ sơ nội bộ tuyệt đối khớp 100% với tuyên bố trong Editorial Notes, có thể cân nhắc (không bắt buộc) thêm một cụm ngắn nhắc lại nguồn chú giải tại Beat 10 hoặc Beat 12 (ví dụ chèn "theo dòng chú giải đã nhắc ở trên" trước "hữu danh vô hình"). Không làm cũng không sai giáo lý.
2. Research QA cần xác nhận bản dịch Việt ngữ chuẩn cho "Cày Lưỡi/Kéo Lưỡi", "Mổ Mắt", "Uống Máu" trước khi khóa kịch bản cuối, theo đúng giới hạn đã ghi sẵn trong brief — không phải phát hiện mới của QA này.
