# 04A — Semantic Beats (EP004)
Semantic Layer duy nhất. Tuân thủ `VIDEO_CREATION_SYSTEM_SPEC.md` (Mục 2.3, Mục 3.1) và `VIDEO_CREATION_REFACTOR_BLUEPRINT.md`. Đây không phải bước tạo scene/prompt/camera — không một trường nào dưới đây quyết định cách trình bày hình ảnh.

## Nguồn (Source of Truth)

Task yêu cầu dùng `03_AUDIO_SCRIPT.md`. File duy nhất trùng tên này trong repo là `_ARCHIVE/SUPERSEDED_FILES/03_AUDIO_SCRIPT.md` (264 dòng, có header metadata). Đã đối chiếu: phần thân narration của file này **giống hệt nội dung** (chỉ khác BOM/dòng trắng đầu) với `OUTPUT/03_AUDIO_SCRIPT_TTS.txt` (255 dòng, không header) — file hiện là bản canonical đang active theo `manifest.json`/`CORE_OS/PRODUCTION_ENGINE.md`. Toàn bộ `narration_start`/`narration_end` dưới đây tham chiếu **số dòng của `OUTPUT/03_AUDIO_SCRIPT_TTS.txt`** vì đây là bản không có metadata lẫn vào, dễ tái kiểm chứng bằng `sed -n 'Np'`, và nội dung narration là một — không có sự khác biệt về ý nghĩa giữa hai file. Toàn văn narration: 255 dòng, 128 đoạn có nội dung (dòng lẻ 1, 3, 5, ..., 255), các dòng chẵn là dòng trắng phân đoạn (không phải nội dung, không thuộc bất kỳ span nào).

## Phương pháp phân đoạn (Segmentation Methodology)

Đơn vị mặc định là **mỗi đoạn văn (paragraph line) của narration gốc**, vì văn bản này được viết theo lối "một ý một đoạn" cho mục đích TTS — đối chiếu từng đoạn cho thấy phần lớn đã là một đơn vị ý nghĩa trọn vẹn, không cần chia nhỏ hơn cũng không cần gộp lại. Quyết định gộp/tách chỉ được áp dụng khi có căn cứ ngữ nghĩa rõ ràng, cụ thể:

- **Giữ tách riêng dù ngắn và song song về hình thức** (ví dụ dòng 227/229/231: "Không phải ai cũng còn cha mẹ để gọi về" / "...gia đình đủ an toàn..." / "...ký ức êm đềm...") vì mỗi câu mang một entity và một khẳng định độc lập, có thể cần evidence khác nhau ở bước sau.
- **Giữ gộp trong một dòng** khi nhiều câu tạo thành một chuỗi nhân-quả hoặc một danh sách không thể tách rời mà không phá vỡ ý (ví dụ dòng 83 — chuỗi lý do trì hoãn; dòng 89 — danh sách điều kiện sinh thành; dòng 127 — chuỗi nhân quả một lời nói; dòng 79 — bốn cảnh chia tay minh hoạ cùng một ý của một bác sĩ).
- Kết quả: **128 Semantic Beat**, ánh xạ 1-1 với 128 đoạn nguồn. Đây là kết quả của phân tích ngữ nghĩa, không phải một quy tắc cơ học áp đặt trước — không có beat nào bị ép chia đều hay gộp để đạt một số lượng mục tiêu.

## Validation Summary

| Kiểm tra | Kết quả |
|---|---|
| Tổng số đoạn nguồn (dòng lẻ 1–255) | 128 |
| Tổng số Semantic Beat | 128 |
| Mọi narration span được cover đúng 1 lần | Đạt — ánh xạ 1-1, không đoạn nào bị bỏ sót |
| Overlap giữa các beat | Không có — mỗi beat chiếm đúng 1 dòng, không dòng nào gán cho 2 beat |
| Gap giữa các beat | Không có về nội dung — các dòng chẵn (2,4,...,254) là dòng trắng cấu trúc thuần tuý của định dạng nguồn, không mang nội dung, không cần beat |
| Beat rỗng | Không có — mọi beat có `meaning`/`entities` không rỗng |
| Beat không truy vết được về narration | Không có — mọi `narration_start`/`narration_end` trỏ đúng 1 dòng có thể `sed -n` lại |
| Đoạn không thể chia rõ ràng | Không phát hiện — toàn bộ 128 đoạn đều phân tách được rõ ràng theo ranh giới đã có sẵn của tác giả gốc |

---

## ACT I — Chiếc ghế trống & câu hỏi mở đầu (BEAT_001–BEAT_012)

**BEAT_001**
- Source: L1
- Meaning: Trong nhà luôn có một chiếc ghế mà ta mặc định vẫn còn người ngồi.
- Entities: chiếc ghế, nhà, người ngồi (không đặc tả danh tính)
- Primary Action: No explicit action.
- Emotional Context: None explicit — trung tính, mở đầu quan sát.
- Causal Relation: None.
- Narrative Function: setup
- Required Evidence: chiếc ghế; giả định "vẫn còn người ngồi"
- Forbidden Hallucination: không nhân vật cụ thể; không địa điểm ngoài "nhà"; không đạo cụ khác ngoài chiếc ghế

**BEAT_002**
- Source: L3
- Meaning: Liệt kê các vị trí/gắn bó cụ thể của chiếc ghế: cạnh bàn ăn, gần cửa sổ, nơi mẹ nhặt rau, nơi cha uống trà — những nơi ta thường đi ngang mà không dừng lại.
- Entities: chiếc ghế, bàn ăn, cửa sổ, mẹ, cha, hành động "đi ngang qua"
- Primary Action: mẹ ngồi nhặt rau; cha ngồi uống trà (hành động thường lệ, không phải hành động đang diễn ra hiện tại)
- Emotional Context: None explicit ở câu này — mô tả trung tính, tiền đề cho cảm xúc ở các beat sau.
- Causal Relation: None.
- Narrative Function: setup
- Required Evidence: bàn ăn, cửa sổ, mẹ nhặt rau, cha uống trà
- Forbidden Hallucination: không thêm nhân vật khác ngoài mẹ/cha; không đặc tả ngoại hình mẹ/cha (không có trong narration)

**BEAT_003**
- Source: L5
- Meaning: Con người thường tin rằng mình vẫn còn thời gian.
- Entities: "ta" (người nói/khán giả, không đặc tả)
- Primary Action: No explicit action — trạng thái niềm tin.
- Emotional Context: None explicit (ngầm định về sự chủ quan, nhưng không được narration gọi tên cảm xúc).
- Causal Relation: Cause (tiền đề dẫn tới BEAT_005).
- Narrative Function: setup
- Required Evidence: niềm tin "còn thời gian"
- Forbidden Hallucination: không hình ảnh cụ thể minh hoạ niềm tin này ngoài phát biểu trừu tượng

**BEAT_004**
- Source: L7
- Meaning: Chuỗi lý do trì hoãn nghe hợp lý: bận nên mai gọi, tháng sau về thăm, chỉ cần chuyển khoản/mua thuốc/gửi quà đúng dịp là đã làm tròn bổn phận.
- Entities: cuộc gọi, chuyến về thăm, chuyển khoản, thuốc, quà
- Primary Action: trì hoãn (gọi về, về thăm); thực hiện các nghĩa vụ vật chất (chuyển khoản, mua thuốc, gửi quà)
- Emotional Context: None explicit — giọng tự biện minh, không được gọi tên cảm xúc.
- Causal Relation: Cause (cùng BEAT_003, dẫn tới BEAT_005).
- Narrative Function: setup
- Required Evidence: hành vi trì hoãn cụ thể (gọi/về thăm); hành vi vật chất thay thế (chuyển khoản/thuốc/quà)
- Forbidden Hallucination: không đặc tả số tiền, loại thuốc, loại quà cụ thể (không có trong narration)

**BEAT_005**
- Source: L9
- Meaning: Nhưng đời sống không báo trước ngày chiếc ghế ấy trở nên trống.
- Entities: chiếc ghế, "trở nên trống"
- Primary Action: chiếc ghế trở nên trống (sự kiện xảy ra, không phải hành động chủ động)
- Emotional Context: None explicit — nhưng là điểm bản lề cảm xúc (ngầm định mất mát), narration không gọi tên trực tiếp ở câu này.
- Causal Relation: Cause: BEAT_003 + BEAT_004 (chủ quan tin còn thời gian, trì hoãn) → Effect: BEAT_005 (ghế trống bất ngờ).
- Narrative Function: revelation
- Required Evidence: khoảnh khắc ghế trở nên trống, tính bất ngờ/không báo trước
- Forbidden Hallucination: không mô tả cụ thể việc mất mát (không có chi tiết như bệnh tật, tang lễ trong narration ở đây)

**BEAT_006**
- Source: L11
- Meaning: Khi ghế đã trống, người ta mới nhận ra có những câu nói rất ngắn, bình thường mà cả đời chưa kịp nói: "Con ăn rồi. Mẹ khỏe không. Cha có đau chỗ nào không. Con xin lỗi. Con thương cha mẹ."
- Entities: những câu nói chưa kịp nói (5 câu cụ thể được liệt kê nguyên văn)
- Primary Action: nhận ra (nhận thức); "chưa kịp nói" (hành động không xảy ra)
- Emotional Context: regret (ân hận/tiếc nuối — ngầm định mạnh qua nội dung, dù từ "ân hận" chưa xuất hiện ở câu này, cảm xúc được thể hiện rõ qua chính 5 câu nói)
- Causal Relation: Effect của BEAT_005 (ghế trống → nhận ra lời chưa nói).
- Narrative Function: revelation
- Required Evidence: đúng 5 câu nói được liệt kê nguyên văn; ý "chưa kịp nói"
- Forbidden Hallucination: không thêm câu nói nào ngoài 5 câu đã liệt kê; không đạo cụ viết tay (ghi chú/thư/note) — đây là lời nói ra miệng, không phải văn bản viết

**BEAT_007**
- Source: L13
- Meaning: Kinh Địa Tạng thường được biết đến qua địa ngục, nghiệp báo, người đã mất, cảnh giới tối tăm, và đại nguyện của Địa Tạng Bồ Tát; các tập trước đã bàn về Địa Tạng là ai, vì sao gọi là Địa Tạng, và sức lay động của đại nguyện.
- Entities: Kinh Địa Tạng, địa ngục, nghiệp báo, người đã mất, Địa Tạng Bồ Tát, đại nguyện, "những tập trước" (series liên kết)
- Primary Action: No explicit action — phát biểu nhận thức chung + hồi cố series.
- Emotional Context: None explicit.
- Causal Relation: None (recap, không phải nhân quả).
- Narrative Function: setup
- Required Evidence: liên hệ tới địa ngục/nghiệp báo/người mất/đại nguyện Địa Tạng như nhận thức phổ biến; liên kết series tới các tập trước
- Forbidden Hallucination: không mô tả cụ thể nội dung "các tập trước" ngoài các chủ đề đã nêu (Địa Tạng là ai / vì sao gọi vậy / sức lay động của nguyện) — không bịa chi tiết cốt truyện các tập trước

**BEAT_008**
- Source: L15
- Meaning: Hôm nay, chương trình trở về đầu nguồn của bản kinh.
- Entities: bản kinh (Kinh Địa Tạng), "đầu nguồn"
- Primary Action: "trở về" (hành động tường thuật, không phải hành động vật lý của nhân vật)
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: transition
- Required Evidence: ý "trở về đầu nguồn của bản kinh"
- Forbidden Hallucination: không hình ảnh cụ thể nào được narration gợi ý ở câu này

**BEAT_009**
- Source: L17
- Meaning: Điều lạ lùng: bản kinh thường gợi nghĩ đến địa ngục lại mở ra trên một cõi trời.
- Entities: bản kinh, địa ngục, cõi trời
- Primary Action: No explicit action.
- Emotional Context: None explicit (được narration gọi là "lạ lùng" — có thể ghi nhận như một sắc thái ngạc nhiên nhẹ, nhưng đây là tính từ mô tả sự kiện, không phải cảm xúc nhân vật).
- Causal Relation: None.
- Narrative Function: setup
- Required Evidence: tương phản "địa ngục" vs "cõi trời" là điểm mở đầu bản kinh
- Forbidden Hallucination: không mô tả cụ thể hình ảnh cõi trời/địa ngục ở beat này (chưa được narration đặc tả)

**BEAT_010**
- Source: L19
- Meaning: Theo truyền thống Phật giáo Đại thừa, pháp hội của Kinh Địa Tạng đặt tại Cung Trời Đao Lợi; Đức Phật thuyết pháp nơi ấy trong liên hệ với thân mẫu; chính bối cảnh này khiến kinh được nhiều truyền thống Đông Á và Việt Nam tôn kính như một bản kinh gắn liền với hiếu đạo.
- Entities: Phật giáo Đại thừa, pháp hội, Kinh Địa Tạng, Cung Trời Đao Lợi, Đức Phật, thân mẫu (Ngài), truyền thống Đông Á và Việt Nam, hiếu đạo
- Primary Action: Đức Phật thuyết pháp
- Emotional Context: None explicit.
- Causal Relation: Cause: bối cảnh pháp hội tại Đao Lợi gắn với thân mẫu → Effect: kinh được tôn kính là bản kinh về hiếu đạo.
- Narrative Function: explanation
- Required Evidence: địa điểm Cung Trời Đao Lợi; quan hệ Đức Phật – thân mẫu; nguồn gốc truyền thống (Đại thừa, Đông Á, Việt Nam); kết quả "gắn liền với hiếu đạo"
- Forbidden Hallucination: không mô tả cụ thể ngoại hình/hành động chi tiết của Đức Phật hay thân mẫu ngoài "thuyết pháp trong liên hệ với thân mẫu"; không đặc tả kiến trúc Cung Trời Đao Lợi (chưa có trong narration ở đây)

**BEAT_011**
- Source: L21
- Meaning: Câu hỏi mở: vì sao một bản kinh nhiều hình ảnh địa ngục lại bắt đầu từ một hành động báo ân?
- Entities: bản kinh, địa ngục, hành động báo ân
- Primary Action: No explicit action — câu hỏi tu từ.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: setup
- Required Evidence: nội dung câu hỏi nguyên văn (tương phản địa ngục vs báo ân)
- Forbidden Hallucination: không trả lời câu hỏi ở beat này (câu trả lời chưa xuất hiện trong narration tại vị trí này)

**BEAT_012**
- Source: L23
- Meaning: Câu hỏi mở: vì sao giữa không gian cao rộng của cõi trời, điều chạm đến trái tim con người lại là ký ức về mẹ?
- Entities: cõi trời, ký ức về mẹ, trái tim con người
- Primary Action: No explicit action — câu hỏi tu từ.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: setup
- Required Evidence: nội dung câu hỏi nguyên văn (tương phản không gian cõi trời vs ký ức mẹ)
- Forbidden Hallucination: không trả lời câu hỏi ở beat này

---

## ACT II — Câu hỏi thứ ba, dẫn nhập chậm rãi, và giáo lý Đao Lợi (BEAT_013–BEAT_024)

**BEAT_013**
- Source: L25
- Meaning: Câu hỏi mở: vì sao bài học hiếu đạo không thể bị thu nhỏ thành nghi lễ, mâm cỗ, cúng bái, hay mệnh lệnh bắt con phục tùng trong im lặng.
- Entities: bài học hiếu đạo, nghi lễ, mâm cỗ, cúng bái, sự phục tùng
- Primary Action: No explicit action — câu hỏi tu từ.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: setup
- Required Evidence: bốn hình thức bị phê phán nguyên văn (nghi lễ/mâm cỗ/cúng bái/phục tùng im lặng)
- Forbidden Hallucination: không trả lời câu hỏi ở beat này

**BEAT_014**
- Source: L27
- Meaning: Lời mời đi thật chậm.
- Entities: None cụ thể (lời mời tường thuật)
- Primary Action: "đi thật chậm" (chỉ dẫn nhịp điệu tường thuật, không phải hành động vật lý của nhân vật)
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: transition
- Required Evidence: chỉ dẫn nhịp độ "chậm"
- Forbidden Hallucination: không hình ảnh cụ thể minh hoạ "đi chậm"

**BEAT_015**
- Source: L29
- Meaning: Lý do đi chậm: có kinh điển, truyền thống, ký ức gia đình, nỗi ân hận của người mất cha mẹ, sự mệt mỏi của người đang chăm cha mẹ già, và vết thương của người nghe "hiếu đạo" mà thấy tim thắt lại vì gia đình không chỉ có yêu thương mà còn đau.
- Entities: kinh điển, truyền thống, ký ức gia đình, người mất cha mẹ (ân hận), người chăm cha mẹ già (mệt mỏi), người có vết thương gia đình
- Primary Action: No explicit action — liệt kê trạng thái/nhóm người liên quan.
- Emotional Context: grief (ân hận của người mất cha mẹ); fatigue-adjacent (mệt mỏi của người chăm sóc — không có nhãn cảm xúc chuẩn hoá riêng, ghi nhận theo đúng từ narration "mệt mỏi"); pain (vết thương gia đình)
- Causal Relation: None (liệt kê lý do song song).
- Narrative Function: setup
- Required Evidence: 5 nhóm/khía cạnh được liệt kê nguyên văn
- Forbidden Hallucination: không đặc tả nhân vật cụ thể đại diện cho từng nhóm

**BEAT_016**
- Source: L31
- Meaning: Cung Trời Đao Lợi là một cõi trời theo thế giới quan Phật giáo; dễ tưởng tượng đây là nơi xa xôi rực rỡ tách biệt khỏi đời sống con người, nhưng nhìn vậy sẽ bỏ lỡ điểm sâu của pháp hội.
- Entities: Cung Trời Đao Lợi, thế giới quan Phật giáo, pháp hội
- Primary Action: No explicit action — phát biểu giáo lý + cảnh báo cách hiểu sai.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: explanation
- Required Evidence: định danh Đao Lợi là "cõi trời"; cảnh báo về cách hiểu sai (xa xôi/tách biệt)
- Forbidden Hallucination: không mô tả cụ thể "rực rỡ" bằng hình ảnh chi tiết — đây là mô tả về cách hiểu SAI cần tránh, không phải mô tả cần thể hiện

**BEAT_017**
- Source: L33
- Meaning: Bối cảnh cõi trời không làm câu chuyện xa con người mà làm nổi bật điều rất gần: dù pháp hội đặt trong vũ trụ quan rộng lớn, trung tâm cảm xúc vẫn là lòng biết ơn — một bậc Giác ngộ vẫn không quên ân nghĩa sinh thành.
- Entities: pháp hội, vũ trụ quan Phật giáo, lòng biết ơn, bậc Giác ngộ, ân nghĩa sinh thành
- Primary Action: No explicit action — khẳng định giáo lý.
- Emotional Context: gratitude
- Causal Relation: None.
- Narrative Function: explanation
- Required Evidence: đối lập "không gian rộng lớn" vs "trung tâm là lòng biết ơn"; khẳng định "bậc Giác ngộ không quên ân nghĩa"
- Forbidden Hallucination: không có hình ảnh cụ thể của "bậc Giác ngộ" ngoài phát biểu trừu tượng ở câu này

**BEAT_018**
- Source: L35
- Meaning: Cảnh báo: điều vừa nêu cần được hiểu cẩn trọng (dẫn nhập cho phần phân biệt tiếp theo).
- Entities: None cụ thể.
- Primary Action: No explicit action.
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho BEAT_019).
- Narrative Function: transition
- Required Evidence: tín hiệu chuyển ý "cần hiểu cẩn trọng"
- Forbidden Hallucination: không nội dung cụ thể — đây thuần là câu bản lề

**BEAT_019**
- Source: L37
- Meaning: Đạo Phật không nói giác ngộ là lạnh lùng hay cắt đứt tình nghĩa, không phải quên mẹ cha; nhưng cũng không nói về tình thương theo nghĩa chấp trước hẹp hòi, bám víu, chiếm hữu, hay đau khổ vì không buông được.
- Entities: giác ngộ, tình nghĩa, mẹ, cha, chấp trước, sự bám víu, sự chiếm hữu
- Primary Action: No explicit action — phát biểu giáo lý theo cấu trúc phủ định kép.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: explanation
- Required Evidence: hai vế phủ định: (a) giác ngộ ≠ lạnh lùng/quên ân nghĩa; (b) tình thương đúng nghĩa ≠ chấp trước/bám víu/chiếm hữu
- Forbidden Hallucination: không hình ảnh minh hoạ cụ thể cho "chấp trước" hay "lạnh lùng" — đây là phát biểu khái niệm trừu tượng

**BEAT_020**
- Source: L39
- Meaning: Có một sự phân biệt rất quan trọng ở đây (dẫn nhập cho định nghĩa tiếp theo).
- Entities: None cụ thể.
- Primary Action: No explicit action.
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho BEAT_021).
- Narrative Function: transition
- Required Evidence: tín hiệu chuyển ý "phân biệt quan trọng"
- Forbidden Hallucination: không nội dung cụ thể

**BEAT_021**
- Source: L41
- Meaning: Bốn định nghĩa nối tiếp: chấp trước = bám vào người khác như tài sản; biết ơn = thấy rõ mình đã nhận ân; báo ân = biết ơn trở thành hành động lành; từ bi = tình thương mở ra với mọi chúng sinh từng khổ đau, không dừng ở người thân.
- Entities: chấp trước, biết ơn, báo ân, từ bi, người thân, chúng sinh
- Primary Action: No explicit action — chuỗi định nghĩa khái niệm.
- Emotional Context: gratitude (biết ơn), compassion (từ bi)
- Causal Relation: None (định nghĩa song song, không nhân quả).
- Narrative Function: explanation
- Required Evidence: đúng 4 định nghĩa theo đúng thứ tự và nội dung: chấp trước / biết ơn / báo ân / từ bi
- Forbidden Hallucination: không gộp/đổi thứ tự 4 khái niệm; không minh hoạ bằng ví dụ cụ thể (narration chưa đưa ví dụ ở đây, chỉ định nghĩa)

**BEAT_022**
- Source: L43
- Meaning: Trong ánh sáng đó, hình ảnh Đức Phật thuyết pháp vì thân mẫu không nên hiểu như chuyện tình cảm thông thường hay còn bị trói buộc bởi nỗi nhớ thế tục, mà là biểu hiện của lòng tri ân đã được trí tuệ soi sáng.
- Entities: Đức Phật, thân mẫu, lòng tri ân, trí tuệ
- Primary Action: Đức Phật thuyết pháp (đã nêu ở BEAT_010, lặp lại trong khung diễn giải mới)
- Emotional Context: gratitude
- Causal Relation: None.
- Narrative Function: explanation
- Required Evidence: phủ định cách hiểu "chuyện tình cảm thông thường"/"nỗi nhớ thế tục"; khẳng định "tri ân được trí tuệ soi sáng"
- Forbidden Hallucination: không thêm hành động/lời thoại nào của Đức Phật ngoài "thuyết pháp trong liên hệ với thân mẫu" đã nêu trước đó

**BEAT_023**
- Source: L45
- Meaning: Giác ngộ không làm con người quên ân nghĩa.
- Entities: giác ngộ, ân nghĩa
- Primary Action: No explicit action — luận đề khẳng định.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: explanation
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_024**
- Source: L47
- Meaning: Trí tuệ sâu hơn làm lòng biết ơn trở nên rộng hơn.
- Entities: trí tuệ, lòng biết ơn
- Primary Action: No explicit action — luận đề khẳng định.
- Emotional Context: gratitude
- Causal Relation: Cause: trí tuệ sâu hơn → Effect: lòng biết ơn rộng hơn.
- Narrative Function: explanation
- Required Evidence: luận đề nguyên văn (quan hệ tỉ lệ thuận trí tuệ–biết ơn)
- Forbidden Hallucination: None thêm

---

## ACT III — Tiền bạc vs. hiện diện, hình thức vs. thực chất (BEAT_025–BEAT_038)

**BEAT_025**
- Source: L49
- Meaning: Từ pháp hội này, có thể bước vào bài học hiếu đạo theo cách khác: không bằng nỗi sợ hay câu hỏi "có bị xem là bất hiếu không", mà bằng câu hỏi yên lặng hơn: "ta đã nhận gì từ cuộc đời và đang đáp lại thế nào?"
- Entities: bài học hiếu đạo, nỗi sợ, câu hỏi mới
- Primary Action: No explicit action — tái định hướng câu hỏi.
- Emotional Context: fear (được nêu tên để phủ định — "không phải bằng nỗi sợ")
- Causal Relation: None.
- Narrative Function: transition
- Required Evidence: câu hỏi mới nguyên văn: "ta đã nhận những gì... đáp lại như thế nào"
- Forbidden Hallucination: None thêm

**BEAT_026**
- Source: L51
- Meaning: Ví dụ: người con gửi tiền đều đặn, điện thoại báo chuyển khoản thành công, mẹ nhận tiền, cha nhận thuốc — mọi thứ bên ngoài đủ đầy, nhưng nhiều năm không có cuộc gọi đủ dài để nghe mẹ kể chuyện đau lưng, nghe cha nói chuyện chiều mưa, nghe giọng hai người già đi.
- Entities: người con, tiền, điện thoại, mẹ, cha, thuốc, cuộc gọi
- Primary Action: gửi tiền (đều đặn); không gọi đủ lâu để lắng nghe
- Emotional Context: None explicit — nhưng nội dung ngầm định sự thiếu kết nối; narration không gọi tên cảm xúc trực tiếp ở câu này.
- Causal Relation: None (một ví dụ minh hoạ, không phải nhân quả giữa hai beat khác).
- Narrative Function: conflict
- Required Evidence: hành vi gửi tiền đều đặn + thông báo chuyển khoản; ba nội dung cụ thể chưa được nghe (đau lưng của mẹ, chiều mưa của cha, giọng hai người già đi)
- Forbidden Hallucination: không đặc tả số tiền cụ thể; không thêm chi tiết về nghề nghiệp/nơi ở của người con (không có trong narration)

**BEAT_027**
- Source: L53
- Meaning: Tiền có thể giúp cha mẹ mua thuốc, nhưng không thể thay việc lắng nghe.
- Entities: tiền, thuốc, sự lắng nghe
- Primary Action: No explicit action — luận đề đối lập.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: đối lập "tiền mua thuốc" vs "không thay được lắng nghe"
- Forbidden Hallucination: None thêm

**BEAT_028**
- Source: L55
- Meaning: Vật chất có thể làm nhẹ một phần đời sống, nhưng không thể thay việc có mặt.
- Entities: vật chất, sự có mặt
- Primary Action: No explicit action — luận đề đối lập.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: đối lập "vật chất" vs "sự có mặt"
- Forbidden Hallucination: None thêm

**BEAT_029**
- Source: L57
- Meaning: Ví dụ: gia đình làm giỗ rất lớn (bàn thờ sáng đèn, mâm cỗ đầy, khách khứa đông) nhưng sau bữa ăn anh em không nhìn mặt nhau, câu nói cũ vẫn đâm vào lòng, hiểu lầm truyền từ năm này sang năm khác như món nợ không ai đặt xuống.
- Entities: gia đình, giỗ, bàn thờ, mâm cỗ, khách khứa, anh em, hiểu lầm
- Primary Action: làm giỗ lớn; không nhìn mặt nhau (sau bữa ăn)
- Emotional Context: None explicit — hàm ý căng thẳng/hiềm khích giữa anh em, narration không gọi tên cảm xúc trực tiếp.
- Causal Relation: None (ví dụ minh hoạ độc lập).
- Narrative Function: conflict
- Required Evidence: 3 yếu tố hình thức lớn (bàn thờ sáng đèn/mâm cỗ đầy/khách khứa đông); hệ quả anh em không nhìn mặt, hiểu lầm kéo dài
- Forbidden Hallucination: không đặc tả số lượng người cụ thể, không thêm chi tiết xung đột cụ thể (loại "câu nói cũ" không được nêu chi tiết trong narration)

**BEAT_030**
- Source: L59
- Meaning: Nếu hiếu đạo chỉ còn là hình thức, nó dễ trở thành sân khấu: người sống trình diễn nhớ thương trước người đã khuất nhưng tiếp tục làm tổn thương người còn sống bên cạnh.
- Entities: hiếu đạo, hình thức, người đã khuất, người còn sống
- Primary Action: trình diễn sự nhớ thương; làm tổn thương người còn sống
- Emotional Context: None explicit.
- Causal Relation: Cause: hiếu đạo chỉ còn hình thức → Effect: trở thành sân khấu/trình diễn.
- Narrative Function: reflection
- Required Evidence: ẩn dụ "sân khấu"; đối lập trình diễn trước người khuất vs làm tổn thương người sống
- Forbidden Hallucination: None thêm

**BEAT_031**
- Source: L61
- Meaning: Nếu hiếu đạo bị hiểu như phục tùng mù quáng, nó có thể trở thành gánh nặng rất đau.
- Entities: hiếu đạo, phục tùng mù quáng, gánh nặng
- Primary Action: No explicit action — luận đề cảnh báo.
- Emotional Context: None explicit (dù "rất đau" là mô tả mức độ, không phải nhãn cảm xúc chuẩn hoá của nhân vật cụ thể).
- Causal Relation: Cause: hiếu đạo = phục tùng mù quáng → Effect: gánh nặng đau đớn.
- Narrative Function: reflection
- Required Evidence: luận đề "phục tùng mù quáng → gánh nặng"
- Forbidden Hallucination: None thêm

**BEAT_032**
- Source: L63
- Meaning: Ví dụ: người chăm mẹ già nhiều năm (thay áo, đút cháo, đưa đi khám, lau vết đau) nhưng trong lòng có mệt mỏi, oán giận, tủi thân, cảm giác bị kẹt lại; rồi xấu hổ vì nghĩ người con hiếu thảo không được mệt/buồn/muốn trốn đi thở.
- Entities: người chăm sóc, mẹ già, các hành động chăm sóc cụ thể
- Primary Action: thay áo, đút cháo, đưa đi khám, lau vết đau (chăm sóc); cảm thấy xấu hổ
- Emotional Context: fatigue (mệt mỏi), resentment (oán giận), shame (tủi thân/xấu hổ)
- Causal Relation: None (ví dụ minh hoạ).
- Narrative Function: conflict
- Required Evidence: 4 hành động chăm sóc cụ thể; 4 trạng thái nội tâm (mệt mỏi/oán giận/tủi thân/cảm giác bị kẹt); niềm tin sai lệch bị xấu hổ vì nghĩ "hiếu thảo thì không được mệt"
- Forbidden Hallucination: không đặc tả bệnh cụ thể của mẹ già; không thêm chi tiết thời gian biểu ngoài các hành động đã nêu

**BEAT_033**
- Source: L65
- Meaning: Trấn an: mệt mỏi không làm bạn thành người bất hiếu; kiệt sức không có nghĩa thiếu thương; người chăm sóc cũng cần được chăm sóc; lòng hiếu có trí tuệ không bắt con người đốt cạn mình rồi gọi đó là tình thương.
- Entities: người chăm sóc, lòng hiếu có trí tuệ
- Primary Action: No explicit action — lời trấn an trực tiếp.
- Emotional Context: reassurance-adjacent (narration dùng khung "xin hãy nghe thật rõ" — ghi nhận theo đúng tinh thần văn bản: đây là hành động trấn an, không phải một nhãn cảm xúc chuẩn trong danh sách ví dụ của brief, nên ghi "compassion" hướng tới người nghe làm nhãn gần nhất)
- Causal Relation: Effect (phản hồi trực tiếp cho BEAT_032).
- Narrative Function: reflection
- Required Evidence: 4 luận điểm trấn an nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_034**
- Source: L67
- Meaning: Có người khi nghe "cha", "mẹ" không thấy ấm áp — tuổi thơ có thể có bạo lực, lạnh lùng, câu nói tổn thương kéo dài, bị bỏ mặc, vết thương người ngoài không thấy nên dễ nói "cha mẹ mà, bỏ qua đi."
- Entities: người nghe (chủ thể trải nghiệm), cha, mẹ, bạo lực, sự lạnh lùng, vết thương
- Primary Action: bị bỏ mặc; bị tổn thương bởi lời nói
- Emotional Context: pain (đau, ngầm định qua "vết thương")
- Causal Relation: None.
- Narrative Function: conflict
- Required Evidence: 4 dạng tổn thương cụ thể (bạo lực/lạnh lùng/lời nói tổn thương/bị bỏ mặc); câu thoại "cha mẹ mà, bỏ qua đi" là lời của người ngoài, không phải của người kể chuyện chính
- Forbidden Hallucination: không đặc tả chi tiết cụ thể của "bạo lực" (loại hình, mức độ không được nêu); không gán câu thoại "cha mẹ mà, bỏ qua đi" cho nhân vật cha/mẹ trong câu chuyện — đây là lời của "người ngoài" nói với nạn nhân

**BEAT_035**
- Source: L69
- Meaning: Đạo hiếu không nên được dùng để bịt miệng nỗi đau.
- Entities: đạo hiếu, nỗi đau
- Primary Action: No explicit action — luận đề cảnh báo.
- Emotional Context: pain
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_036**
- Source: L71
- Meaning: Hiếu đạo có từ bi/trí tuệ không bắt người phải quay lại nơi không an toàn, không bắt cho phép tổn thương tiếp tục, không bắt gọi sự chịu đựng là đức hạnh; giữ khoảng cách có thể là để không nuôi hận thù; ranh giới bình an có thể là cách duy nhất để cả hai bên không tạo thêm nghiệp đau khổ.
- Entities: hiếu đạo, từ bi, trí tuệ, khoảng cách, ranh giới, nghiệp đau khổ
- Primary Action: giữ khoảng cách; đặt ranh giới
- Emotional Context: None explicit ở câu này (dù chủ đề là bảo vệ khỏi tổn thương).
- Causal Relation: Cause: giữ ranh giới bình an → Effect: cả hai bên không tạo thêm nghiệp đau khổ.
- Narrative Function: explanation
- Required Evidence: 3 điều "không bắt buộc" (quay lại nơi không an toàn / cho phép tổn thương tiếp tục / gọi chịu đựng là đức hạnh); vai trò của ranh giới/khoảng cách
- Forbidden Hallucination: None thêm

**BEAT_037**
- Source: L73
- Meaning: Điều này không làm mất lòng biết ơn — nó làm lòng biết ơn trở nên thật hơn.
- Entities: lòng biết ơn
- Primary Action: No explicit action — luận đề khẳng định.
- Emotional Context: gratitude
- Causal Relation: Effect của BEAT_036.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_038**
- Source: L75
- Meaning: Bốn phân biệt: biết ơn ≠ phủ nhận điều đã xảy ra; tôn trọng ≠ để người khác tiếp tục làm hại mình; chăm sóc ≠ đánh mất thân tâm; tha thứ (nếu có) không thể bị ép bằng lời giảng.
- Entities: biết ơn, tôn trọng, chăm sóc, tha thứ
- Primary Action: No explicit action — 4 định nghĩa phủ định song song.
- Emotional Context: None explicit.
- Causal Relation: None (song song, không nhân quả).
- Narrative Function: explanation
- Required Evidence: đúng 4 phân biệt theo đúng thứ tự
- Forbidden Hallucination: None thêm

---

## ACT IV — Bác sĩ hồi sức, sự trì hoãn, và nguồn gốc của thân mạng (BEAT_039–BEAT_048)

**BEAT_039**
- Source: L77
- Meaning: Bài học hiếu đạo của Kinh Địa Tạng cần được nghe bằng trái tim trưởng thành; nó không phải cây roi đánh vào người con, mà là ngọn đèn soi lại mối quan hệ giữa ân nghĩa, trách nhiệm, nghiệp và sự chuyển hoá.
- Entities: bài học hiếu đạo, Kinh Địa Tạng, ân nghĩa, trách nhiệm, nghiệp, sự chuyển hoá
- Primary Action: No explicit action — ẩn dụ định hướng ("cây roi" vs "ngọn đèn").
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: hai ẩn dụ đối lập (cây roi / ngọn đèn); bốn khái niệm được soi rọi (ân nghĩa/trách nhiệm/nghiệp/chuyển hoá)
- Forbidden Hallucination: None thêm

**BEAT_040**
- Source: L79
- Meaning: Một bác sĩ khoa hồi sức chứng kiến nhiều cuộc chia tay: người con nắm tay cha khóc; người mẹ thở yếu vẫn hỏi con ăn gì chưa; người cha nghiêm khắc cả đời đến phút cuối mới nói lời xin lỗi nhỏ; có người không kịp đến, không phải vì không thương mà vì tưởng còn ngày mai.
- Entities: bác sĩ, khoa hồi sức, người con, người cha (nắm tay), người mẹ (thở yếu), người cha nghiêm khắc, người không kịp đến
- Primary Action: nắm tay cha và khóc; hỏi con đã ăn gì; nói lời xin lỗi; không kịp đến
- Emotional Context: grief
- Causal Relation: None (bốn ví dụ song song trong một khung quan sát của bác sĩ).
- Narrative Function: conflict
- Required Evidence: đúng 4 cảnh chia tay được liệt kê; khung "bác sĩ khoa hồi sức chứng kiến"; lý do "không kịp đến" là vì tưởng còn ngày mai, không phải vì không thương
- Forbidden Hallucination: không đặt tên/danh tính cụ thể cho bác sĩ hay các bệnh nhân; không thêm cảnh chia tay ngoài 4 cảnh đã liệt kê; không đặc tả bệnh lý cụ thể

**BEAT_041**
- Source: L81
- Meaning: Đời sống làm ta trì hoãn tình thương bằng những lý do nghe rất hợp lý.
- Entities: đời sống, tình thương, lý do trì hoãn
- Primary Action: trì hoãn
- Emotional Context: None explicit.
- Causal Relation: Cause (dẫn nhập cho BEAT_042).
- Narrative Function: reflection
- Required Evidence: luận đề "lý do nghe hợp lý"
- Forbidden Hallucination: None thêm

**BEAT_042**
- Source: L83
- Meaning: Chuỗi lý do bận: kiếm tiền, lo con, trả nợ, chứng minh mình đúng, giận, chờ người kia mở lời trước — và cứ vậy những chiếc ghế trong nhà lặng lẽ cũ đi.
- Entities: chiếc ghế (lặp lại motif mở đầu), 6 lý do bận cụ thể
- Primary Action: bận kiếm tiền/lo con/trả nợ/chứng minh đúng/giận/chờ người kia mở lời; ghế "cũ đi"
- Emotional Context: None explicit ở chuỗi lý do, nhưng kết quả "ghế cũ đi" mang sắc thái tiếc nuối ngầm định giống BEAT_005.
- Causal Relation: Cause: 6 lý do bận rộn tích luỹ → Effect: ghế trong nhà lặng lẽ cũ đi.
- Narrative Function: reflection
- Required Evidence: đúng 6 lý do theo thứ tự; hệ quả "ghế cũ đi" — đây là một callback thị giác tới BEAT_001/BEAT_002, cần ghi nhận liên kết motif (không phải quan hệ nhân quả xuyên beat, mà là lặp lại hình ảnh)
- Forbidden Hallucination: không thêm lý do bận nào ngoài 6 lý do đã liệt kê

**BEAT_043**
- Source: L85
- Meaning: Khi Kinh Địa Tạng mở ra bằng hình ảnh Đức Phật hướng về thân mẫu, có thể quán chiếu rằng đạo hiếu trước hết là sự tỉnh thức trước ân nghĩa — không phải ân nghĩa để mắc nợ trong sợ hãi, mà để nhận ra thân mạng này không tự nhiên mà có.
- Entities: Kinh Địa Tạng, Đức Phật, thân mẫu, đạo hiếu, ân nghĩa, thân mạng
- Primary Action: No explicit action — quán chiếu/diễn giải.
- Emotional Context: fear (được nêu tên để phủ định — "không phải để mắc nợ trong sợ hãi")
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: định nghĩa "đạo hiếu = tỉnh thức trước ân nghĩa"; phủ định "ân nghĩa trong sợ hãi"
- Forbidden Hallucination: None thêm

**BEAT_044**
- Source: L87
- Meaning: Ta được sinh ra từ rất nhiều điều kiện.
- Entities: "ta", điều kiện sinh thành (chưa liệt kê chi tiết ở câu này)
- Primary Action: được sinh ra
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho BEAT_045).
- Narrative Function: setup
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_045**
- Source: L89
- Meaning: Danh sách điều kiện: thân thể của mẹ, công sức của cha, chén cơm của người trồng lúa, bàn tay người may áo, thầy cô, hàng xóm, người xa lạ, bác sĩ, người quét đường — những người giữ một phần thế giới này cho ta sống; thấy cha mẹ là bước đầu, nhìn sâu sẽ thấy đằng sau cha mẹ là vô số chúng sinh đã nâng đỡ đời mình.
- Entities: mẹ, cha, người trồng lúa, người may áo, thầy cô, hàng xóm, người xa lạ, bác sĩ, người quét đường, chúng sinh
- Primary Action: No explicit action — liệt kê nguồn nâng đỡ.
- Emotional Context: gratitude
- Causal Relation: None (danh sách song song).
- Narrative Function: explanation
- Required Evidence: đúng 9 nguồn nâng đỡ được liệt kê (mẹ/cha/người trồng lúa/người may áo/thầy cô/hàng xóm/người xa lạ/bác sĩ/người quét đường); kết luận "đằng sau cha mẹ là vô số chúng sinh"
- Forbidden Hallucination: không thêm nghề nghiệp/nhóm người nào ngoài 9 nhóm đã liệt kê; không đặc tả danh tính cụ thể cho từng nhóm

**BEAT_046**
- Source: L91
- Meaning: Tinh thần Đại thừa đi theo hướng ấy.
- Entities: tinh thần Đại thừa
- Primary Action: No explicit action.
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho BEAT_047).
- Narrative Function: transition
- Required Evidence: liên kết tới "hướng ấy" (mở rộng lòng biết ơn, từ BEAT_045)
- Forbidden Hallucination: None thêm

**BEAT_047**
- Source: L93
- Meaning: Từ lòng hiếu với một người mẹ, tâm biết ơn có thể mở rộng — không làm loãng tình thương gia đình mà làm nó sâu hơn; khi thật sự hiểu công ơn một người, ta hiểu rằng bất kỳ ai cũng từng được thương, từng có mẹ, từng có nỗi sợ, từng có một chiếc ghế để trở về hoặc từng mất chiếc ghế ấy.
- Entities: lòng hiếu, mẹ, tâm biết ơn, tình thương gia đình, chiếc ghế (callback motif)
- Primary Action: mở rộng (tâm biết ơn)
- Emotional Context: gratitude, compassion
- Causal Relation: Cause: hiểu sâu công ơn một người → Effect: nhận ra ai cũng từng được thương/có mẹ/có ghế để trở về hoặc mất ghế.
- Narrative Function: reflection
- Required Evidence: quá trình mở rộng từ một mẹ → mọi người; callback "chiếc ghế" (liên kết motif với BEAT_001/BEAT_002/BEAT_042, không phải quan hệ nhân quả mà là lặp lại hình ảnh biểu tượng)
- Forbidden Hallucination: None thêm

**BEAT_048**
- Source: L95
- Meaning: Đó là nơi Địa Tạng Bồ Tát xuất hiện trong mạch cảm xúc của series này.
- Entities: Địa Tạng Bồ Tát, series (mạch cảm xúc)
- Primary Action: xuất hiện (trong mạch cảm xúc — mang tính ẩn dụ tường thuật, không phải xuất hiện vật lý)
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: transition
- Required Evidence: liên kết Địa Tạng Bồ Tát với chủ đề vừa mở rộng (lòng biết ơn phổ quát)
- Forbidden Hallucination: không mô tả hình tướng Địa Tạng Bồ Tát ở beat này (chưa được đặc tả trong narration tại vị trí này)

---

## ACT V — Đại nguyện, sự ích kỷ cần gột rửa, và câu hỏi tự vấn (BEAT_049–BEAT_058)

**BEAT_049**
- Source: L97
- Meaning: Ở tập trước đã nói về đại nguyện không bỏ rơi chúng sinh nơi tối tăm nhất; hôm nay là một nhánh mềm của đại nguyện đó — lòng từ bi lớn có thể bắt đầu từ nỗi thương gần: thương mẹ, nhớ cha, đau khi thấy người thân khổ — rồi trái tim học nhìn mọi chúng sinh như người thân từng lạc trong vô minh.
- Entities: đại nguyện, chúng sinh, lòng từ bi, mẹ, cha, vô minh
- Primary Action: No explicit action — diễn giải quá trình mở rộng từ bi.
- Emotional Context: compassion
- Causal Relation: Cause: nỗi thương gần (mẹ/cha/người thân) → Effect: trái tim học nhìn mọi chúng sinh như người thân.
- Narrative Function: explanation
- Required Evidence: liên kết đại nguyện (series trước) với chủ đề hôm nay; chuỗi mở rộng "thương mẹ → nhớ cha → đau vì người thân khổ → nhìn mọi chúng sinh như người thân"
- Forbidden Hallucination: không mô tả chi tiết nội dung "đại nguyện" ngoài "không bỏ rơi chúng sinh nơi tối tăm nhất" đã có

**BEAT_050**
- Source: L99
- Meaning: Nhưng để lòng hiếu trở thành từ bi, nó phải được thanh lọc khỏi sự ích kỷ.
- Entities: lòng hiếu, từ bi, sự ích kỷ
- Primary Action: thanh lọc
- Emotional Context: None explicit.
- Causal Relation: Cause (điều kiện) cho quá trình lòng hiếu → từ bi.
- Narrative Function: conflict
- Required Evidence: luận đề "cần thanh lọc khỏi ích kỷ" là điều kiện để hiếu trở thành từ bi
- Forbidden Hallucination: None thêm

**BEAT_051**
- Source: L101
- Meaning: Ba cảnh báo: thương cha mẹ mình mà khinh cha mẹ người khác → lòng hiếu còn hẹp; lo đẹp mặt gia đình mình mà chà đạp gia đình khác → chưa có trí tuệ; cúng giỗ tổ tiên lớn nhưng bất công với người làm việc cho mình → chưa chạm đến đạo.
- Entities: cha mẹ mình, cha mẹ người khác, gia đình mình, gia đình khác, tổ tiên, người làm việc cho mình
- Primary Action: khinh thường; chà đạp; bất công
- Emotional Context: None explicit (nội dung phê phán, không có nhãn cảm xúc của chủ thể).
- Causal Relation: 3 cặp Cause→Effect độc lập, mỗi cặp: hành vi ích kỷ → hệ quả đánh giá (hẹp / chưa trí tuệ / chưa chạm đạo).
- Narrative Function: conflict
- Required Evidence: đúng 3 cặp hành vi–hệ quả theo đúng thứ tự
- Forbidden Hallucination: None thêm

**BEAT_052**
- Source: L103
- Meaning: Hiếu đạo trong đạo Phật không dừng ở việc nhớ người đã khuất — nó hỏi ta đang sống ra sao.
- Entities: hiếu đạo, người đã khuất
- Primary Action: No explicit action — luận đề định hướng.
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho 3 câu hỏi tự vấn ở BEAT_053–055).
- Narrative Function: transition
- Required Evidence: luận đề "không dừng ở nhớ người khuất — hỏi ta đang sống ra sao"
- Forbidden Hallucination: None thêm

**BEAT_053**
- Source: L105
- Meaning: Câu hỏi tự vấn 1: ta có đang tiếp tục gieo những nhân đau khổ mà cha mẹ từng vô tình truyền lại không?
- Entities: nhân đau khổ, cha mẹ
- Primary Action: No explicit action — câu hỏi tu từ.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: câu hỏi nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_054**
- Source: L107
- Meaning: Câu hỏi tự vấn 2: ta có đang nói với con mình bằng chính những câu từng làm mình tổn thương không?
- Entities: con mình, những câu tổn thương
- Primary Action: No explicit action — câu hỏi tu từ.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: câu hỏi nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_055**
- Source: L109
- Meaning: Câu hỏi tự vấn 3: ta có đang biến áp lực thành bạo lực, lo lắng thành kiểm soát, tình thương thành điều kiện, rồi gọi đó là vì muốn tốt cho con không?
- Entities: áp lực, bạo lực, lo lắng, kiểm soát, tình thương, điều kiện, con
- Primary Action: No explicit action — câu hỏi tu từ.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: đúng 3 phép biến đổi được nêu (áp lực→bạo lực; lo lắng→kiểm soát; tình thương→điều kiện)
- Forbidden Hallucination: None thêm

---

## ACT VI — Câu chuyện người cha phá vỡ vòng lặp (BEAT_056–BEAT_063)

**BEAT_056**
- Source: L111
- Meaning: Một người cha nhận ra mình đang la con bằng giọng của cha mình ngày trước; câu nói vừa bật ra, đứa trẻ cúi mặt xuống; ông nhìn thấy chính mình nhiều năm trước — một đứa trẻ cũng từng cúi mặt, im lặng, và tự hứa lớn lên sẽ không bao giờ nói những lời ấy với con mình.
- Entities: người cha, con (đứa trẻ hiện tại), cha của người cha (không xuất hiện trực tiếp, chỉ qua "giọng của cha mình"), đứa trẻ trong quá khứ (chính ông)
- Primary Action: la con; đứa trẻ cúi mặt xuống; ông nhận ra/nhìn thấy chính mình; (quá khứ) từng cúi mặt, im lặng, tự hứa
- Emotional Context: realization
- Causal Relation: None (đây là bối cảnh dẫn tới BEAT_057/058/059 — vòng lặp tiếp diễn dù đã nhận ra).
- Narrative Function: conflict
- Required Evidence: hành động la con bằng "giọng của cha mình"; phản ứng cúi mặt của đứa trẻ; sự nhận ra bản thân trong quá khứ; lời tự hứa thời thơ ấu "sẽ không bao giờ nói những lời ấy"
- Forbidden Hallucination: không đặt tên nhân vật; không đặc tả bối cảnh không gian cụ thể (nhà, phòng...) — không có trong narration; không mô tả hành vi bạo lực thể chất (chỉ có "la", không có mô tả đánh đập ở beat này)

**BEAT_057**
- Source: L113
- Meaning: Nhưng vòng lặp vẫn quay.
- Entities: vòng lặp
- Primary Action: quay (tiếp diễn)
- Emotional Context: None explicit.
- Causal Relation: Effect của BEAT_056 (nhận ra nhưng chưa đủ để dừng lại).
- Narrative Function: conflict
- Required Evidence: luận đề "vòng lặp vẫn quay" — nhấn mạnh việc nhận thức chưa dẫn tới thay đổi ngay
- Forbidden Hallucination: None thêm

**BEAT_058**
- Source: L115
- Meaning: Cho đến một ngày, ông dừng lại.
- Entities: người cha (ông)
- Primary Action: dừng lại
- Emotional Context: None explicit — điểm bản lề (climax) của câu chuyện.
- Causal Relation: Effect: điểm chuyển hoá, dẫn tới hành động ở BEAT_059.
- Narrative Function: climax
- Required Evidence: khoảnh khắc "dừng lại" — bước ngoặt của câu chuyện
- Forbidden Hallucination: không mô tả nguyên nhân cụ thể khiến ông dừng lại (narration không nêu lý do cụ thể ngoài "một ngày")

**BEAT_059**
- Source: L117
- Meaning: Ông không thể thay đổi tuổi thơ mình, không thể làm quá khứ dịu dàng hơn, không thể làm người cha đã mất quay lại xin lỗi; nhưng ông có thể quỳ xuống trước con và nói: "ba xin lỗi, câu vừa rồi làm con đau. Ba sẽ học cách nói khác."
- Entities: người cha (ông), tuổi thơ, người cha đã mất (của ông), con (của ông)
- Primary Action: quỳ xuống; nói lời xin lỗi (nguyên văn)
- Emotional Context: realization, compassion (thể hiện qua hành động chuộc lỗi)
- Causal Relation: Effect của BEAT_058 ("dừng lại" → hành động quỳ xuống xin lỗi).
- Narrative Function: resolution
- Required Evidence: 3 điều "không thể" (thay đổi tuổi thơ / làm quá khứ dịu hơn / làm cha đã mất xin lỗi); hành động quỳ xuống; câu thoại nguyên văn "ba xin lỗi, câu vừa rồi làm con đau. Ba sẽ học cách nói khác."
- Forbidden Hallucination: không đổi/diễn giải lại câu thoại; không thêm phản ứng của đứa con sau lời xin lỗi (narration không mô tả phản ứng này)

**BEAT_060**
- Source: L119
- Meaning: Ở tầng ứng dụng hiện đại, đây có thể là một hình thức báo hiếu rất sâu.
- Entities: tầng ứng dụng hiện đại, báo hiếu
- Primary Action: No explicit action — khái quát hoá câu chuyện thành nguyên lý.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: luận đề khái quát hoá hành động của người cha (BEAT_059) thành "hình thức báo hiếu hiện đại"
- Forbidden Hallucination: None thêm

**BEAT_061**
- Source: L121
- Meaning: Không phải vì ông quên cha mình, mà vì ông quyết định không truyền tiếp vết thương của cha mình sang thế hệ sau.
- Entities: người cha (ông), cha của ông, vết thương, thế hệ sau
- Primary Action: quyết định không truyền tiếp vết thương
- Emotional Context: None explicit.
- Causal Relation: Effect của BEAT_059/060 — giải thích ý nghĩa của hành động quỳ xuống xin lỗi.
- Narrative Function: reflection
- Required Evidence: phủ định "quên cha mình"; khẳng định "không truyền tiếp vết thương"
- Forbidden Hallucination: None thêm

**BEAT_062**
- Source: L123
- Meaning: Nén hương chân thành nhất cho tổ tiên không nằm trên bàn thờ — nó nằm trong khoảnh khắc một người dừng bàn tay nóng giận, dừng lời mắng nhục, dừng thói quen im lặng trừng phạt, dừng cơn say, dừng cách yêu thương có điều kiện, dừng một vòng lặp đã qua ba đời mà không ai đủ tỉnh để gọi tên.
- Entities: nén hương, bàn thờ, tổ tiên, hành động "dừng lại" (6 dạng cụ thể), ba đời (thế hệ)
- Primary Action: dừng bàn tay nóng giận; dừng lời mắng nhục; dừng im lặng trừng phạt; dừng cơn say; dừng yêu thương có điều kiện; dừng vòng lặp ba đời
- Emotional Context: None explicit — ẩn dụ tâm linh, không phải cảm xúc trực tiếp của nhân vật.
- Causal Relation: None (danh sách ẩn dụ song song).
- Narrative Function: reflection
- Required Evidence: ẩn dụ "nén hương chân thành nhất không nằm trên bàn thờ"; đúng 6 hành động "dừng" theo đúng thứ tự; "ba đời" là phạm vi thời gian được nêu
- Forbidden Hallucination: không thêm hành động "dừng" nào ngoài 6 hành động đã liệt kê

**BEAT_063**
- Source: L125
- Meaning: Đây không phải một câu kinh gán vào miệng Đức Phật — đây là cách quán chiếu hiện đại từ tinh thần nhân quả và chuyển hoá.
- Entities: câu kinh, Đức Phật, nhân quả, sự chuyển hoá
- Primary Action: No explicit action — tuyên bố ranh giới nguồn (disclaimer).
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: explanation
- Required Evidence: phủ định rõ ràng "không phải lời Đức Phật"; khẳng định đây là "quán chiếu hiện đại" từ tinh thần nhân quả/chuyển hoá — **đây là ràng buộc quan trọng cho các bước sau: không được thể hiện đoạn BEAT_056–062 như một trích dẫn kinh điển hay lời Đức Phật**
- Forbidden Hallucination: không thể hiện câu chuyện người cha (BEAT_056-062) như một sự kiện trong kinh điển hoặc lời dạy trực tiếp của Đức Phật

---

## ACT VII — Nhân quả đời thường và sự tha thứ cho người đã mất (BEAT_064–BEAT_069)

**BEAT_064**
- Source: L127
- Meaning: Nhân quả không chỉ ở chuyện xa xôi sau khi chết, mà nằm trong bữa cơm tối nay: một lời nói gieo xuống → một đứa trẻ nhận lấy → một thói quen hình thành → một nỗi sợ đi vào thân thể → hai mươi năm sau nó trở thành cách người ấy yêu, giận, làm cha, làm mẹ.
- Entities: nhân quả, bữa cơm tối nay, lời nói, đứa trẻ, thói quen, nỗi sợ
- Primary Action: gieo xuống (lời nói); nhận lấy (đứa trẻ); hình thành (thói quen); đi vào thân thể (nỗi sợ); trở thành cách yêu/giận/làm cha mẹ (20 năm sau)
- Emotional Context: fear
- Causal Relation: Chuỗi nhân quả nội tại 5 bước: lời nói → đứa trẻ nhận → thói quen hình thành → nỗi sợ nhập thân → cách yêu/giận/làm cha mẹ (20 năm sau). Đây là một causal chain hoàn chỉnh nằm trong một beat duy nhất.
- Narrative Function: explanation
- Required Evidence: đúng chuỗi 5 bước nhân quả theo đúng thứ tự; khung thời gian "hai mươi năm sau"
- Forbidden Hallucination: không tách rời các bước thành sự kiện độc lập không liên quan; không gán chuỗi này cho một nhân vật cụ thể có tên

**BEAT_065**
- Source: L129
- Meaning: Nếu hiểu vậy, hiếu đạo không phải chuyện cũ — nó đang diễn ra trong cách ta nhắn tin, nghe điện thoại, chăm sóc người già, đặt ranh giới, nuôi dạy con, nói lời xin lỗi.
- Entities: hiếu đạo, nhắn tin, điện thoại, người già, ranh giới, con, lời xin lỗi
- Primary Action: nhắn tin; nghe điện thoại; chăm sóc người già; đặt ranh giới; nuôi dạy con; nói lời xin lỗi
- Emotional Context: None explicit.
- Causal Relation: Effect của BEAT_064 (nhân quả đời thường → hiếu đạo là chuyện hiện tại).
- Narrative Function: reflection
- Required Evidence: đúng 6 hành vi hiện đại được liệt kê (nhắn tin/nghe điện thoại/chăm sóc người già/đặt ranh giới/nuôi dạy con/xin lỗi)
- Forbidden Hallucination: không thêm hành vi nào ngoài 6 hành vi đã liệt kê

**BEAT_066**
- Source: L131
- Meaning: Người mất mẹ khi chưa kịp xin lỗi có thể mang ân hận lâu, nhưng ân hận không nhất thiết thành nhà tù — có thể thành lời nhắc: sống bớt cứng/nóng/vô tâm hơn, chăm sóc người già khác bằng tử tế, nói với con mình những lời chưa kịp nói ngày xưa.
- Entities: người mất mẹ, ân hận, mẹ, người già khác, con
- Primary Action: mang ân hận; chăm sóc người già khác; nói với con những lời chưa kịp nói
- Emotional Context: grief
- Causal Relation: Cause: ân hận không xử lý → có thể thành nhà tù (khả năng tiêu cực); Effect mong muốn: ân hận → chuyển hoá thành lời nhắc sống tử tế hơn (khả năng tích cực). Narration trình bày cả hai nhánh khả năng.
- Narrative Function: reflection
- Required Evidence: hai khả năng chuyển hoá của ân hận (nhà tù vs lời nhắc); 3 cách sống cụ thể được đề xuất (bớt cứng/nóng/vô tâm; chăm sóc người già khác; nói lời chưa kịp nói với con)
- Forbidden Hallucination: None thêm

**BEAT_067**
- Source: L133
- Meaning: Người đã mất không cần ta chìm mãi trong tự trách.
- Entities: người đã mất, sự tự trách
- Primary Action: No explicit action — luận đề khẳng định.
- Emotional Context: grief
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_068**
- Source: L135
- Meaning: Nếu có một món quà đẹp dâng lên ký ức họ, có lẽ đó là một đời sống đang học cách sáng hơn.
- Entities: món quà, ký ức, đời sống
- Primary Action: học cách sáng hơn
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: ẩn dụ "món quà = đời sống học cách sáng hơn"
- Forbidden Hallucination: không đặc tả "món quà" bằng vật thể cụ thể — đây là ẩn dụ trừu tượng, không phải một vật thể vật lý

**BEAT_069**
- Source: L137
- Meaning: Ở đây, cần nói rõ về nghi lễ (dẫn nhập cho phần tiếp theo).
- Entities: nghi lễ
- Primary Action: No explicit action.
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho BEAT_070–074).
- Narrative Function: transition
- Required Evidence: tín hiệu chuyển ý "cần nói rõ về nghi lễ"
- Forbidden Hallucination: None thêm

---

## ACT VIII — Nghi lễ, lòng thành, và giới hạn của hình thức (BEAT_070–BEAT_075)

**BEAT_070**
- Source: L139
- Meaning: Trong truyền thống Phật giáo, tụng kinh, làm phước, hồi hướng, tưởng niệm người mất đều có vị trí riêng — nâng đỡ tâm người sống, nuôi dưỡng lòng thành, nhắc sống thiện lành hơn, trong khung niềm tin về công đức và hồi hướng.
- Entities: tụng kinh, làm phước, hồi hướng, tưởng niệm, người mất, công đức
- Primary Action: tụng kinh; làm phước; hồi hướng; tưởng niệm
- Emotional Context: None explicit.
- Causal Relation: Cause: các thực hành nghi lễ → Effect: nâng đỡ tâm, nuôi dưỡng lòng thành, nhắc sống thiện lành.
- Narrative Function: explanation
- Required Evidence: đúng 4 thực hành nghi lễ được nêu; đúng 3 tác dụng được nêu (nâng đỡ tâm/nuôi dưỡng lòng thành/nhắc sống thiện lành)
- Forbidden Hallucination: không mô tả nghi lễ bằng hình ảnh cụ thể (không gian, vật phẩm...) — chỉ có tên gọi thực hành, chưa có mô tả hình ảnh trong narration ở đây

**BEAT_071**
- Source: L141
- Meaning: Cảnh báo: không nên biến nghi lễ thành cái máy bảo đảm kết quả; không nên nói làm một việc là chắc chắn người mất chuyển cảnh giới; không nên dùng nỗi thương để bán sợ hãi; không nên khiến ai tin rằng không đủ tiền/thời gian/nghi thức thì là bất hiếu.
- Entities: nghi lễ, cảnh giới, nỗi thương, sợ hãi, tiền, thời gian, nghi thức
- Primary Action: No explicit action — 4 cảnh báo phủ định song song.
- Emotional Context: fear (được nêu tên để cảnh báo việc lợi dụng — "bán sợ hãi")
- Causal Relation: None.
- Narrative Function: conflict
- Required Evidence: đúng 4 cảnh báo theo đúng thứ tự
- Forbidden Hallucination: None thêm

**BEAT_072**
- Source: L143
- Meaning: Lòng thành không đo bằng sự phô trương.
- Entities: lòng thành, sự phô trương
- Primary Action: No explicit action — luận đề khẳng định.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_073**
- Source: L145
- Meaning: Ba ví dụ hiếu đạo sâu không cần phô trương: người nghèo thắp một nén hương với tâm lành rồi sống bớt hận thù; người không có bàn thờ lớn nhưng chăm mẹ còn sống bằng bữa cơm ấm/đưa đi khám/trò chuyện không gắt gỏng; người không thể gặp lại cha vì tổn thương quá lớn nhưng quyết không biến vết thương thành bạo lực với con mình.
- Entities: người nghèo, nén hương, người chăm mẹ còn sống, người tổn thương với cha, con (của người thứ ba)
- Primary Action: thắp một nén hương; sống bớt hận thù; chăm sóc mẹ còn sống (bữa cơm/đưa đi khám/trò chuyện); không biến vết thương thành bạo lực với con
- Emotional Context: compassion
- Causal Relation: None (ba ví dụ song song).
- Narrative Function: reflection
- Required Evidence: đúng 3 ví dụ theo đúng thứ tự và nội dung
- Forbidden Hallucination: không thêm ví dụ thứ 4; không đặc tả danh tính cụ thể cho 3 người này

**BEAT_074**
- Source: L147
- Meaning: Đừng để ai dùng chữ hiếu làm bạn thấy mình không còn đường thở.
- Entities: chữ hiếu
- Primary Action: No explicit action — lời cảnh báo trực tiếp tới khán giả.
- Emotional Context: None explicit (dù hình ảnh "không còn đường thở" hàm ý ngột ngạt).
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn, hướng tới khán giả ("bạn")
- Forbidden Hallucination: None thêm

**BEAT_075**
- Source: L149
- Meaning: Hiếu đạo có trí tuệ phải đi cùng từ bi — từ bi với cha mẹ, người đã mất, người đang chăm sóc, và với chính mình (một con người cũng có giới hạn, cần chữa lành, cần học từng chút).
- Entities: hiếu đạo, từ bi, cha mẹ, người đã mất, người chăm sóc, chính mình
- Primary Action: No explicit action — luận đề tổng hợp.
- Emotional Context: compassion
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: đúng 4 đối tượng của từ bi (cha mẹ/người đã mất/người chăm sóc/chính mình)
- Forbidden Hallucination: None thêm

---

## ACT IX — Tổng kết Đao Lợi, Địa Tạng, và các thực hành nhỏ (BEAT_076–BEAT_086)

**BEAT_076**
- Source: L151
- Meaning: Nhìn lại Cung Trời Đao Lợi: trên cao là pháp hội, trong sâu là ký ức về mẹ, rộng hơn là đại nguyện của Địa Tạng — từ một mối ân tình riêng, cánh cửa mở ra thành lòng thương không biên giới.
- Entities: Cung Trời Đao Lợi, pháp hội, ký ức về mẹ, đại nguyện, Địa Tạng, lòng thương không biên giới
- Primary Action: No explicit action — hình ảnh tổng kết ba tầng (cao/sâu/rộng).
- Emotional Context: compassion
- Causal Relation: None (tổng kết, không phải nhân quả mới).
- Narrative Function: reflection
- Required Evidence: đúng cấu trúc ba tầng "trên cao / trong sâu / rộng hơn nữa" gắn với ba nội dung tương ứng (pháp hội / ký ức mẹ / đại nguyện Địa Tạng)
- Forbidden Hallucination: None thêm

**BEAT_077**
- Source: L153
- Meaning: Đó là điều làm Kinh Địa Tạng không bị kẹt trong sợ hãi.
- Entities: Kinh Địa Tạng, sợ hãi
- Primary Action: No explicit action.
- Emotional Context: fear (nêu tên để phủ định)
- Causal Relation: Effect của BEAT_076.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_078**
- Source: L155
- Meaning: Nếu chỉ nhìn địa ngục dễ sợ, chỉ nhìn nghiệp báo dễ nặng lòng; nhưng nhìn từ hiếu đạo và đại bi, bản kinh hỏi câu khác: giữa nơi tối tăm nhất, con người còn có thể khơi dậy lòng biết ơn, trách nhiệm và ánh sáng hay không?
- Entities: địa ngục, nghiệp báo, hiếu đạo, đại bi, lòng biết ơn, trách nhiệm, ánh sáng
- Primary Action: No explicit action — câu hỏi tu từ khép lại phần lý giải.
- Emotional Context: fear (địa ngục gây sợ), gratitude (câu hỏi hướng tới)
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: đối lập hai cách nhìn (chỉ địa ngục/nghiệp báo vs hiếu đạo/đại bi); câu hỏi cuối nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_079**
- Source: L157
- Meaning: Địa Tạng Bồ Tát không nên bị nhìn như vị thần cai quản cõi âm — Ngài là hình ảnh của một hạnh nguyện, lời nhắc rằng không nơi nào quá tối để từ bi không thể vào; muốn học tinh thần ấy trong gia đình, không cần bắt đầu bằng điều lớn lao.
- Entities: Địa Tạng Bồ Tát, cõi âm, hạnh nguyện, gia đình
- Primary Action: No explicit action — định nghĩa lại vai trò Địa Tạng, dẫn nhập cho danh sách thực hành nhỏ.
- Emotional Context: compassion
- Causal Relation: None (dẫn nhập cho BEAT_080–085).
- Narrative Function: transition
- Required Evidence: phủ định "vị thần cai quản cõi âm"; khẳng định "hình ảnh của một hạnh nguyện"; dẫn nhập "không cần bắt đầu bằng điều lớn lao"
- Forbidden Hallucination: không mô tả hình tướng/y phục cụ thể của Địa Tạng Bồ Tát (không có trong narration tại vị trí này)

**BEAT_080**
- Source: L159
- Meaning: Thực hành nhỏ 1: một cuộc gọi không vội.
- Entities: cuộc gọi
- Primary Action: gọi điện (không vội)
- Emotional Context: None explicit.
- Causal Relation: None (một trong các ví dụ minh hoạ cho nguyên lý ở BEAT_079).
- Narrative Function: reflection
- Required Evidence: hành vi "cuộc gọi không vội"
- Forbidden Hallucination: không đặc tả người gọi/người nhận cụ thể

**BEAT_081**
- Source: L161
- Meaning: Thực hành nhỏ 2: một bữa cơm không cáu gắt.
- Entities: bữa cơm
- Primary Action: dùng bữa (không cáu gắt)
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: hành vi "bữa cơm không cáu gắt"
- Forbidden Hallucination: None thêm

**BEAT_082**
- Source: L163
- Meaning: Thực hành nhỏ 3: một lời xin lỗi không chờ người kia xin lỗi trước.
- Entities: lời xin lỗi
- Primary Action: xin lỗi (chủ động, không chờ đối phương)
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: hành vi "chủ động xin lỗi trước"
- Forbidden Hallucination: None thêm

**BEAT_083**
- Source: L165
- Meaning: Thực hành nhỏ 4: một ranh giới được nói bằng giọng bình tĩnh.
- Entities: ranh giới
- Primary Action: nói ra ranh giới (bằng giọng bình tĩnh)
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: hành vi "đặt ranh giới bằng giọng bình tĩnh"
- Forbidden Hallucination: None thêm

**BEAT_084**
- Source: L167
- Meaning: Thực hành nhỏ 5: một quyết định đi trị liệu, đi tu học, hoặc tìm sự giúp đỡ, để những gì mình chịu đựng không tiếp tục rơi xuống đời con.
- Entities: trị liệu, tu học, sự giúp đỡ, đời con
- Primary Action: quyết định đi trị liệu/tu học/tìm giúp đỡ
- Emotional Context: None explicit.
- Causal Relation: Cause: tìm trị liệu/giúp đỡ → Effect: ngăn sự chịu đựng rơi xuống đời con.
- Narrative Function: reflection
- Required Evidence: 3 hình thức tìm giúp đỡ (trị liệu/tu học/sự giúp đỡ); mục đích "không để rơi xuống đời con"
- Forbidden Hallucination: None thêm

**BEAT_085**
- Source: L169
- Meaning: Thực hành nhỏ 6: nhìn vào chiếc ghế quen thuộc trong nhà và tự hỏi "nếu một ngày nơi ấy trống đi, điều gì hôm nay mình vẫn còn có thể làm?"
- Entities: chiếc ghế (callback motif)
- Primary Action: nhìn vào chiếc ghế; tự hỏi
- Emotional Context: None explicit — nhưng đây là một callback trực tiếp tới motif mở đầu (BEAT_001).
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: hành vi "nhìn chiếc ghế và tự hỏi"; câu hỏi nguyên văn; **ghi nhận liên kết motif rõ ràng với BEAT_001/BEAT_002/BEAT_042/BEAT_047 — đây là lần narration chủ động gọi lại hình ảnh chiếc ghế như một công cụ tự vấn**
- Forbidden Hallucination: None thêm

**BEAT_086**
- Source: L171
- Meaning: Có một điều khó trong hiếu đạo: ta thường chỉ nhận ra sự mong manh của cha mẹ khi họ đã yếu đi quá nhiều.
- Entities: hiếu đạo, cha mẹ, sự mong manh
- Primary Action: nhận ra (muộn)
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho câu chuyện ở BEAT_087).
- Narrative Function: setup
- Required Evidence: luận đề "chỉ nhận ra mong manh khi cha mẹ đã yếu"
- Forbidden Hallucination: None thêm

---

## ACT X — Sự mong manh của cha mẹ, sự có mặt, và người chăm sóc vô hình (BEAT_087–BEAT_096)

**BEAT_087**
- Source: L173
- Meaning: Ngày còn trẻ, ta nhìn cha mẹ như người lúc nào cũng ở đó (mẹ luôn biết bếp còn gì, cha luôn sửa bóng đèn/vá cửa/đi nắng mưa không than) — tưởng đó là tự nhiên; cho đến ngày mẹ hỏi lại một câu nhiều lần, cha không còn nghe rõ, bàn tay từng chắc bỗng run khi cầm chén — lúc đó mới giật mình thấy người từng bồng mình giờ cần được bồng đỡ bằng giọng dịu hơn.
- Entities: cha mẹ (khi còn trẻ được nhìn), mẹ, cha, bếp, bóng đèn, cánh cửa, chén
- Primary Action: mẹ biết bếp còn gì; cha sửa bóng đèn/vá cửa/đi nắng mưa; mẹ hỏi lại một câu nhiều lần; cha không nghe rõ; bàn tay run khi cầm chén
- Emotional Context: realization
- Causal Relation: Cause: các dấu hiệu suy yếu (hỏi lại nhiều lần, không nghe rõ, tay run) → Effect: nhận ra người từng bồng mình cần được bồng đỡ.
- Narrative Function: revelation
- Required Evidence: hình ảnh cha mẹ "luôn ở đó" thời trẻ (đúng 2 ví dụ: mẹ biết bếp, cha sửa đồ); đúng 3 dấu hiệu suy yếu (hỏi lại nhiều lần / không nghe rõ / tay run khi cầm chén); hình ảnh kết "người từng bồng mình cần được bồng đỡ bằng giọng dịu hơn"
- Forbidden Hallucination: không đặc tả bệnh lý cụ thể (không nói tên bệnh Alzheimer/Parkinson... — narration chỉ mô tả triệu chứng chung)

**BEAT_088**
- Source: L175
- Meaning: Nếu chỉ đợi đến lúc cha mẹ yếu, lòng hiếu có thể biến thành cuộc chạy đua với thời gian.
- Entities: cha mẹ, lòng hiếu, thời gian
- Primary Action: No explicit action — luận đề cảnh báo.
- Emotional Context: None explicit.
- Causal Relation: Cause: đợi đến lúc cha mẹ yếu → Effect: lòng hiếu thành cuộc chạy đua với thời gian.
- Narrative Function: reflection
- Required Evidence: ẩn dụ "cuộc chạy đua với thời gian"
- Forbidden Hallucination: None thêm

**BEAT_089**
- Source: L177
- Meaning: Tập này không muốn làm ta sợ mất cha mẹ, chỉ muốn mời tỉnh lại trước khi quá muộn — tỉnh lại để bữa cơm tối nay bớt lạnh, cuộc gọi cuối tuần không còn là nghĩa vụ, và nghe câu chuyện cũ lần thứ mười bằng lòng nhẫn nại thay vì cắt ngang.
- Entities: cha mẹ, bữa cơm tối nay, cuộc gọi cuối tuần, câu chuyện cũ
- Primary Action: tỉnh lại; nghe bằng lòng nhẫn nại (thay vì cắt ngang)
- Emotional Context: fear (được nêu để phủ định — "không muốn làm ta sợ")
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: mục đích tập phim (phủ định "làm sợ", khẳng định "mời tỉnh lại"); 3 ví dụ cụ thể "tỉnh lại để..." (bữa cơm bớt lạnh / cuộc gọi không còn nghĩa vụ / nghe chuyện cũ lần mười bằng nhẫn nại)
- Forbidden Hallucination: None thêm

**BEAT_090**
- Source: L179
- Meaning: Với nhiều người, hiếu đạo bắt đầu bằng sự có mặt.
- Entities: hiếu đạo, sự có mặt
- Primary Action: No explicit action — luận đề dẫn nhập.
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho BEAT_091).
- Narrative Function: setup
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_091**
- Source: L181
- Meaning: Có mặt không phải lúc nào cũng là có mặt bằng thân (có người ở xa, làm việc nhiều giờ, ở nước ngoài, không đủ điều kiện về thăm) — nhưng có mặt còn là đặt tâm vào cuộc trò chuyện: có thật sự nghe khi gọi về, có nhớ hỏi mẹ cần gì khi gửi tiền, có để cha không cảm thấy là gánh nặng khi đưa đi khám.
- Entities: sự có mặt, người ở xa quê, mẹ, cha, cuộc trò chuyện
- Primary Action: gọi về (có thật sự nghe không); gửi tiền (có hỏi mẹ cần gì không); đưa cha đi khám (có để cha không thấy là gánh nặng không)
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: explanation
- Required Evidence: 4 hoàn cảnh không thể có mặt bằng thân (ở xa quê/làm nhiều giờ/nước ngoài/không đủ điều kiện); 3 câu hỏi tự vấn cụ thể (nghe thật khi gọi/hỏi mẹ cần gì khi gửi tiền/không để cha thấy gánh nặng khi đưa khám)
- Forbidden Hallucination: None thêm

**BEAT_092**
- Source: L183
- Meaning: Nhiều người con tưởng mình báo hiếu vì không để cha mẹ thiếu tiền — nhưng cha mẹ đôi khi không thiếu tiền bằng thiếu cảm giác được nhìn thấy; cần được nói chuyện không sợ làm phiền, được hỏi ý kiến việc nhỏ, biết mình không chỉ là trách nhiệm tài chính trong điện thoại của con.
- Entities: người con, cha mẹ, tiền, cảm giác được nhìn thấy, điện thoại
- Primary Action: không để cha mẹ thiếu tiền; (thiếu) cảm giác được nhìn thấy
- Emotional Context: None explicit.
- Causal Relation: Cause: chỉ chú trọng tài chính → Effect: cha mẹ vẫn thiếu cảm giác được nhìn thấy.
- Narrative Function: conflict
- Required Evidence: đối lập "không thiếu tiền" vs "thiếu cảm giác được nhìn thấy"; 3 nhu cầu cụ thể (nói chuyện không sợ phiền/được hỏi ý kiến/biết mình không chỉ là trách nhiệm tài chính)
- Forbidden Hallucination: None thêm

**BEAT_093**
- Source: L185
- Meaning: Và người con cũng cần được nhìn thấy.
- Entities: người con
- Primary Action: No explicit action.
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho BEAT_094).
- Narrative Function: transition
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_094**
- Source: L187
- Meaning: Người chăm mẹ bệnh nhiều năm (ngày đi làm, chiều nấu ăn, tối thay thuốc, đêm thức khi nghe mẹ trở mình); người ngoài khen "con hiếu quá" nhưng không ai thấy người ấy khóc trong nhà tắm với nước chảy nhỏ, hay cảm giác tội lỗi khi thoáng nghĩ "mình mệt quá, mình muốn được nghỉ".
- Entities: người chăm sóc, mẹ (bệnh), người ngoài, nhà tắm
- Primary Action: đi làm; nấu ăn; thay thuốc; thức đêm khi mẹ trở mình; khóc trong nhà tắm; thoáng nghĩ muốn được nghỉ
- Emotional Context: fatigue, shame (cảm giác tội lỗi)
- Causal Relation: None.
- Narrative Function: conflict
- Required Evidence: đúng 4 hoạt động chăm sóc theo trình tự ngày/chiều/tối/đêm; hành vi ẩn giấu (khóc trong nhà tắm, nước chảy nhỏ); ý nghĩ thoáng qua nguyên văn "mình mệt quá, mình muốn được nghỉ"; lời khen bề ngoài của người ngoài ("con hiếu quá") đối lập với thực tế bị che giấu
- Forbidden Hallucination: không đặc tả bệnh cụ thể của mẹ; không đặt tên nhân vật

**BEAT_095**
- Source: L189
- Meaning: Nếu giảng hiếu đạo mà không nhìn thấy người chăm sóc, bài giảng ấy chưa đủ từ bi.
- Entities: hiếu đạo, người chăm sóc, bài giảng
- Primary Action: No explicit action — luận đề đánh giá.
- Emotional Context: compassion
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_096**
- Source: L191
- Meaning: Lòng hiếu trưởng thành phải hỏi: làm sao chăm sóc mà không tự huỷ hoại, thương mà không tích oán hận, nhờ anh chị em chia sẻ, tìm hỗ trợ y tế/tinh thần/cộng đồng thay vì một mình gánh rồi gọi đó là đạo đức.
- Entities: lòng hiếu trưởng thành, anh chị em, hỗ trợ y tế/tinh thần/cộng đồng
- Primary Action: No explicit action — 4 câu hỏi tự vấn song song.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: đúng 4 câu hỏi theo đúng thứ tự (không tự huỷ hoại / không tích oán hận / chia sẻ với anh chị em / tìm hỗ trợ thay vì gánh một mình)
- Forbidden Hallucination: None thêm

---

## ACT XI — Trung đạo, ranh giới an toàn, và gia đình tổn thương (BEAT_097–BEAT_106)

**BEAT_097**
- Source: L193
- Meaning: Đạo Phật nói về trung đạo — trong gia đình, trung đạo cụ thể: không bỏ mặc cha mẹ nhưng cũng không kiệt sức đến mất dịu dàng; không dùng bận rộn để trốn tránh nhưng cũng không dùng chữ hiếu để xoá giới hạn thân tâm.
- Entities: trung đạo, cha mẹ, chữ hiếu
- Primary Action: No explicit action — hai cặp phủ định song song định nghĩa trung đạo.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: explanation
- Required Evidence: đúng 2 cặp đối lập (không bỏ mặc / không kiệt sức; không dùng bận để trốn / không dùng hiếu để xoá giới hạn)
- Forbidden Hallucination: None thêm

**BEAT_098**
- Source: L195
- Meaning: Với gia đình có tổn thương, trung đạo càng cần trí tuệ.
- Entities: gia đình có tổn thương, trung đạo, trí tuệ
- Primary Action: No explicit action.
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho BEAT_099).
- Narrative Function: transition
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_099**
- Source: L197
- Meaning: Có người muốn hiếu kính nhưng mỗi lần về nhà bị nhục mạ/kiểm soát/kéo vào vùng đau cũ; có người căng cứng toàn thân khi nghe chuông điện thoại cha mẹ; có người đã cố tha thứ nhiều lần nhưng tổn hại vẫn tiếp tục — lời khuyên "hãy về đi, cha mẹ mà" có thể thành một nhát dao.
- Entities: người muốn hiếu kính, nhục mạ, kiểm soát, điện thoại, cha mẹ, sự tha thứ, lời khuyên "hãy về đi, cha mẹ mà"
- Primary Action: bị nhục mạ/kiểm soát/kéo vào vùng đau cũ; căng cứng khi nghe chuông điện thoại; cố tha thứ nhiều lần
- Emotional Context: pain, fear (căng thẳng khi nghe chuông điện thoại)
- Causal Relation: Cause: tổn hại lặp lại dù đã tha thứ → Effect: lời khuyên thông thường trở thành gây hại ("nhát dao").
- Narrative Function: conflict
- Required Evidence: 3 trải nghiệm cụ thể (bị nhục mạ khi về nhà / căng cứng khi nghe chuông điện thoại / tha thứ nhiều lần nhưng tổn hại tiếp tục); câu thoại nguyên văn "hãy về đi, cha mẹ mà" là lời khuyên phổ biến bị phê phán, không phải lời khuyên được ủng hộ
- Forbidden Hallucination: không đặc tả hình thức nhục mạ/kiểm soát cụ thể (không có chi tiết trong narration)

**BEAT_100**
- Source: L199
- Meaning: Hiếu đạo không nên là con đường đưa một người trở lại nguy hiểm.
- Entities: hiếu đạo, nguy hiểm
- Primary Action: No explicit action — luận đề khẳng định.
- Emotional Context: None explicit.
- Causal Relation: Effect của BEAT_099.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_101**
- Source: L201
- Meaning: Nếu quan hệ chưa đủ an toàn: có thể bắt đầu bằng không nuôi thù hận nhưng vẫn giữ khoảng cách; bằng lời cầu nguyện thầm nhưng không mở cửa cho bạo lực; bằng nhìn nhận cha mẹ cũng là con người với vô minh/khổ đau nhưng điều đó không làm hành vi gây hại trở thành đúng.
- Entities: mối quan hệ chưa an toàn, thù hận, khoảng cách, lời cầu nguyện thầm, bạo lực, cha mẹ, vô minh
- Primary Action: giữ khoảng cách; cầu nguyện thầm; nhìn nhận cha mẹ cũng là con người với vô minh/khổ đau
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: đúng 3 cách thực hành khi quan hệ chưa an toàn (không thù hận nhưng giữ khoảng cách / cầu nguyện thầm không mở cửa bạo lực / nhìn nhận vô minh của cha mẹ không đồng nghĩa hợp lý hoá hành vi gây hại)
- Forbidden Hallucination: None thêm

**BEAT_102**
- Source: L203
- Meaning: Đây là điểm rất quan trọng (dẫn nhập nhấn mạnh cho phần phân biệt tiếp theo).
- Entities: None cụ thể.
- Primary Action: No explicit action.
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho BEAT_103).
- Narrative Function: transition
- Required Evidence: tín hiệu nhấn mạnh
- Forbidden Hallucination: None thêm

**BEAT_103**
- Source: L205
- Meaning: Thấy nỗi khổ của người gây tổn thương không có nghĩa cho phép họ tiếp tục gây tổn thương; từ bi không phải mở cửa cho bạo lực; trí tuệ không phải chịu đựng đến cạn kiệt; hiếu đạo không phải sự im lặng của người bị thương.
- Entities: người gây tổn thương, từ bi, bạo lực, trí tuệ, hiếu đạo, người bị thương
- Primary Action: No explicit action — 4 phân biệt phủ định song song.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: explanation
- Required Evidence: đúng 4 phân biệt theo đúng thứ tự (thấy khổ ≠ cho phép tổn thương tiếp tục; từ bi ≠ mở cửa bạo lực; trí tuệ ≠ chịu đựng cạn kiệt; hiếu đạo ≠ im lặng của người bị thương)
- Forbidden Hallucination: None thêm

**BEAT_104**
- Source: L207
- Meaning: Khi nói báo hiếu, ta thường quên một chiều khác: cha mẹ cũng có thể báo hiếu với con bằng cách sống tỉnh thức hơn.
- Entities: báo hiếu, cha mẹ, con
- Primary Action: No explicit action — mở ra chiều ngược của khái niệm báo hiếu.
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho BEAT_105).
- Narrative Function: transition
- Required Evidence: luận đề "cha mẹ cũng có thể báo hiếu với con"
- Forbidden Hallucination: None thêm

**BEAT_105**
- Source: L209
- Meaning: Nếu hiếu là nhớ ân và không phụ lòng nhau, cha mẹ cũng có trách nhiệm không nhân danh tình thương để làm con tổn thương; cha biết xin lỗi con không mất uy nghiêm; mẹ biết lắng nghe con không mất vai trò làm mẹ — sự khiêm cung ấy có thể thành bài học đạo đức lớn trong gia đình.
- Entities: cha, mẹ, con, tình thương, uy nghiêm, sự khiêm cung
- Primary Action: cha xin lỗi con; mẹ lắng nghe con
- Emotional Context: None explicit.
- Causal Relation: Cause: cha mẹ khiêm cung (xin lỗi/lắng nghe) → Effect: trở thành bài học đạo đức lớn trong gia đình.
- Narrative Function: explanation
- Required Evidence: trách nhiệm của cha mẹ "không nhân danh tình thương làm con tổn thương"; 2 hành vi cụ thể (cha xin lỗi không mất uy nghiêm; mẹ lắng nghe không mất vai trò)
- Forbidden Hallucination: None thêm

**BEAT_106**
- Source: L211
- Meaning: Có những đứa trẻ cả đời chỉ chờ một câu: "mẹ hiểu là ngày xưa mẹ đã làm con đau. Cha hiểu là cha đã quá nóng." — không phải để kết tội, mà để vết thương được gọi đúng tên.
- Entities: đứa trẻ, mẹ, cha, vết thương
- Primary Action: chờ đợi một câu nói (cả đời)
- Emotional Context: grief
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: hai câu thoại nguyên văn ("mẹ hiểu là ngày xưa mẹ đã làm con đau" / "cha hiểu là cha đã quá nóng"); mục đích "gọi đúng tên vết thương", không phải "kết tội"
- Forbidden Hallucination: không đổi/diễn giải lại 2 câu thoại nguyên văn

---

## ACT XII — Trách nhiệm hai chiều & ẩn dụ địa ngục hiện đại (BEAT_107–BEAT_113)

**BEAT_107**
- Source: L213
- Meaning: Nếu một người cha/mẹ đang nghe, bài học cũng hỏi họ: đang để lại điều gì trong lòng con — không chỉ tiền bạc/nhà cửa/bằng cấp, mà là cách yêu thương, cách nói năng, cách đối diện lỗi lầm, cách xin lỗi, cách dừng lại trước khi giận biến thành nghiệp truyền đời.
- Entities: cha, mẹ, con, tiền bạc, nhà cửa, bằng cấp, cơn giận, nghiệp
- Primary Action: để lại (điều gì trong lòng con); dừng lại (trước khi giận biến thành nghiệp)
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: phủ định 3 giá trị vật chất (tiền bạc/nhà cửa/bằng cấp); khẳng định 5 giá trị phi vật chất (cách yêu thương/nói năng/đối diện lỗi lầm/xin lỗi/dừng cơn giận)
- Forbidden Hallucination: None thêm

**BEAT_108**
- Source: L215
- Meaning: Hiếu đạo không chỉ đi từ con lên cha mẹ — là dòng trách nhiệm hai chiều: con học biết ơn, cha mẹ học khiêm cung, người già học buông kiểm soát, người trẻ học bớt vô tâm; mỗi người bớt cố chấp thì căn nhà bớt một chút địa ngục.
- Entities: hiếu đạo, con, cha mẹ, người già, người trẻ, căn nhà, địa ngục (ẩn dụ)
- Primary Action: con học biết ơn; cha mẹ học khiêm cung; người già học buông kiểm soát; người trẻ học bớt vô tâm
- Emotional Context: None explicit.
- Causal Relation: Cause: mỗi thành viên bớt cố chấp → Effect: căn nhà bớt "địa ngục".
- Narrative Function: explanation
- Required Evidence: đúng 4 vai học tập tương ứng (con/cha mẹ/người già/người trẻ); ẩn dụ "địa ngục" cho căn nhà — cần lưu ý đây là ẩn dụ tâm lý, không phải cảnh giới địa ngục theo giáo lý (phân biệt với BEAT_009/BEAT_078)
- Forbidden Hallucination: không thể hiện "địa ngục" ở đây như cảnh giới siêu hình/tôn giáo — đây là ẩn dụ cho một căn nhà bất hoà

**BEAT_109**
- Source: L217
- Meaning: Đây là chỗ Kinh Địa Tạng chạm vào đời sống hiện đại rất sâu.
- Entities: Kinh Địa Tạng, đời sống hiện đại
- Primary Action: No explicit action.
- Emotional Context: None explicit.
- Causal Relation: None (dẫn nhập cho BEAT_110).
- Narrative Function: transition
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_110**
- Source: L219
- Meaning: Địa ngục không chỉ là hình ảnh đáng sợ trong kinh — ở tầng quán chiếu, địa ngục có thể là căn nhà không ai chịu nghe ai, bàn ăn mỗi người cầm một nỗi giận, căn phòng có mẹ già nằm đó nhưng con tranh phần thiệt hơn, đứa trẻ học rằng tình thương luôn có điều kiện, người lớn không biết ôm con vì chưa từng được ôm.
- Entities: địa ngục (ẩn dụ), căn nhà, bàn ăn, mẹ già, con (tranh giành), đứa trẻ, người lớn
- Primary Action: không ai chịu nghe ai; mỗi người cầm một nỗi giận; con tranh phần thiệt hơn; đứa trẻ học tình thương có điều kiện; người lớn không biết ôm con
- Emotional Context: None explicit (dù nội dung mô tả bất hoà gia đình sâu sắc).
- Causal Relation: None (5 hình ảnh ẩn dụ song song).
- Narrative Function: explanation
- Required Evidence: đúng 5 hình ảnh ẩn dụ "địa ngục hiện đại" theo đúng thứ tự; **bắt buộc thể hiện như ẩn dụ tâm lý về bất hoà gia đình, không phải cảnh giới địa ngục Phật giáo theo nghĩa đen**
- Forbidden Hallucination: không hình tượng hoá "địa ngục" bằng biểu tượng tôn giáo/siêu nhiên (lửa, quỷ, hình phạt...) — narration đang nói về một căn nhà đời thường

**BEAT_111**
- Source: L221
- Meaning: Nếu địa ngục có thể bắt đầu từ tâm đầy sân hận, một cõi lành cũng có thể bắt đầu từ tâm biết dừng.
- Entities: địa ngục (ẩn dụ), sân hận, cõi lành, tâm biết dừng
- Primary Action: No explicit action — luận đề đối lập.
- Emotional Context: None explicit.
- Causal Relation: Cause: tâm sân hận → Effect: địa ngục (ẩn dụ); Cause: tâm biết dừng → Effect: cõi lành (đối lập song song, cùng cấu trúc).
- Narrative Function: reflection
- Required Evidence: cấu trúc đối lập nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_112**
- Source: L223
- Meaning: Dừng lại trước một lời cay độc, một cái tát, thói quen so sánh con mình với con người ta, việc lấy công lao sinh thành để buộc người khác sống theo ý mình, sự vô tâm nguỵ trang bằng chữ "bận".
- Entities: lời cay độc, cái tát, con mình, con người ta, công lao sinh thành, sự vô tâm
- Primary Action: dừng lại (trước 5 hành vi cụ thể)
- Emotional Context: None explicit.
- Causal Relation: None (danh sách song song, cụ thể hoá BEAT_111).
- Narrative Function: reflection
- Required Evidence: đúng 5 hành vi cần dừng theo đúng thứ tự
- Forbidden Hallucination: không thêm hành vi nào ngoài 5 hành vi đã liệt kê

**BEAT_113**
- Source: L225
- Meaning: Mỗi lần dừng như vậy không chỉ cứu một khoảnh khắc — mà đang cứu một dòng truyền thừa của khổ đau khỏi đi xa hơn.
- Entities: dòng truyền thừa, khổ đau
- Primary Action: cứu (một khoảnh khắc; một dòng truyền thừa)
- Emotional Context: None explicit.
- Causal Relation: Effect của BEAT_111/112 (hành động dừng lại → hệ quả ngăn khổ đau truyền tiếp).
- Narrative Function: reflection
- Required Evidence: luận đề "cứu một khoảnh khắc" và "cứu một dòng truyền thừa" — hai tầng ý nghĩa của cùng một hành động
- Forbidden Hallucination: None thêm

---

## ACT XIII — Không phải ai cũng có; lời nhắn nhủ nhẹ nhàng (BEAT_114–BEAT_122)

**BEAT_114**
- Source: L227
- Meaning: Không phải ai cũng còn cha mẹ để gọi về.
- Entities: cha mẹ
- Primary Action: No explicit action — phát biểu về sự thiếu vắng khả năng liên lạc với cha mẹ.
- Emotional Context: grief
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_115**
- Source: L229
- Meaning: Không phải ai cũng có một gia đình đủ an toàn để quay lại.
- Entities: gia đình an toàn
- Primary Action: No explicit action.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_116**
- Source: L231
- Meaning: Không phải ai cũng có một ký ức êm đềm để nương tựa.
- Entities: ký ức êm đềm
- Primary Action: No explicit action.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_117**
- Source: L233
- Meaning: Xin đừng nghe tập này như lời trách, hãy nghe như ngọn đèn nhỏ: nếu cha mẹ còn sống và quan hệ còn chăm sóc được, hãy có mặt thật hơn; nếu cha mẹ đã mất, hãy biến nỗi nhớ thành đời sống tử tế hơn; nếu gia đình từng làm bạn đau, hãy giữ an toàn cho mình nhưng đừng biến vết thương thành việc làm đau người khác.
- Entities: cha mẹ (còn sống/đã mất), gia đình, sự an toàn, nỗi nhớ
- Primary Action: chăm sóc bằng sự có mặt thật hơn; biến nỗi nhớ thành đời sống tử tế; giữ an toàn cho mình
- Emotional Context: compassion
- Causal Relation: None (3 nhánh hướng dẫn song song theo 3 hoàn cảnh khác nhau).
- Narrative Function: resolution
- Required Evidence: đúng 3 nhánh hướng dẫn theo đúng 3 hoàn cảnh (cha mẹ còn sống & quan hệ chăm sóc được / cha mẹ đã mất / gia đình từng gây đau)
- Forbidden Hallucination: None thêm

**BEAT_118**
- Source: L235
- Meaning: Có những món nợ ân tình không thể trả bằng tiền.
- Entities: món nợ ân tình, tiền
- Primary Action: No explicit action.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_119**
- Source: L237
- Meaning: Có những mất mát không thể sửa bằng một lễ lớn.
- Entities: mất mát, lễ lớn
- Primary Action: No explicit action.
- Emotional Context: grief
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_120**
- Source: L239
- Meaning: Có những lời xin lỗi đến muộn, nhưng vẫn có thể trở thành hạt giống cho một cách sống khác.
- Entities: lời xin lỗi, hạt giống (ẩn dụ)
- Primary Action: trở thành (hạt giống)
- Emotional Context: None explicit.
- Causal Relation: Cause: lời xin lỗi muộn → Effect (tiềm năng): hạt giống cho cách sống khác.
- Narrative Function: reflection
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_121**
- Source: L241
- Meaning: Những chiếc ghế trống không còn là lời buộc tội nếu ta biết ngồi xuống trước nó bằng sự thành thật — có thể thắp một ngọn đèn, chắp tay, nói trong lòng: "con không hoàn hảo, cha mẹ cũng không hoàn hảo, nhưng từ hôm nay, con xin học cách sống bớt gây khổ hơn."
- Entities: chiếc ghế trống (callback motif), ngọn đèn, sự thành thật
- Primary Action: ngồi xuống trước chiếc ghế; thắp một ngọn đèn; chắp tay; nói trong lòng (câu nguyên văn)
- Emotional Context: realization, compassion
- Causal Relation: None. **Đây là điểm giải quyết (resolution) trực tiếp cho motif mở đầu tại BEAT_001 — cần ghi nhận rõ liên kết motif chiếc ghế xuyên suốt: BEAT_001/002 (mở) → BEAT_042/047/085 (nhắc lại) → BEAT_121 (khép lại) — đây là quan hệ callback/motif, không phải causal_relation theo nghĩa cause→effect.**
- Narrative Function: resolution
- Required Evidence: hành động cụ thể (ngồi xuống/thắp đèn/chắp tay); câu nói trong lòng nguyên văn
- Forbidden Hallucination: không đổi nội dung câu nói nguyên văn; không thêm hành động nghi lễ khác ngoài thắp đèn và chắp tay

**BEAT_122**
- Source: L243
- Meaning: Câu hỏi trực tiếp tới khán giả: nếu cha mẹ còn ở đây, điều gì bạn vẫn đang chờ một ngày thích hợp mới nói?
- Entities: cha mẹ, khán giả ("bạn")
- Primary Action: No explicit action — câu hỏi trực tiếp.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: câu hỏi nguyên văn
- Forbidden Hallucination: None thêm

---

## ACT XIV — Kết & bắc cầu sang tập sau (BEAT_123–BEAT_128)

**BEAT_123**
- Source: L245
- Meaning: Câu hỏi trực tiếp tới khán giả: nếu họ đã đi xa, bạn có thể biến nỗi nhớ ấy thành một đời sống tử tế hơn như thế nào?
- Entities: khán giả ("bạn"), nỗi nhớ
- Primary Action: No explicit action — câu hỏi trực tiếp.
- Emotional Context: grief
- Causal Relation: None.
- Narrative Function: reflection
- Required Evidence: câu hỏi nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_124**
- Source: L247
- Meaning: Tập tiếp theo sẽ đi sâu vào: người sống có thể làm gì cho người đã mất, và vì sao trong Kinh Địa Tạng, hồi hướng không phải giao dịch với thế giới vô hình mà là cách chuyển hoá tâm người sống trong ánh sáng nhân quả và từ bi.
- Entities: tập tiếp theo, người sống, người đã mất, Kinh Địa Tạng, hồi hướng, thế giới vô hình, nhân quả, từ bi
- Primary Action: No explicit action — giới thiệu nội dung tập sau.
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: setup
- Required Evidence: chủ đề tập sau (người sống làm gì cho người mất; hồi hướng ≠ giao dịch, = chuyển hoá tâm) — **ràng buộc quan trọng: đây là nội dung của TẬP KHÁC (episode tiếp theo), không được lẫn vào nội dung chính của EP004 ở các bước sau**
- Forbidden Hallucination: không mở rộng/diễn giải trước nội dung tập sau ngoài những gì đã nêu ở đây

**BEAT_125**
- Source: L249
- Meaning: Nếu hôm nay trong lòng khán giả hiện lên một gương mặt, một chiếc ghế, một bàn tay, hay một câu chưa kịp nói, hãy giữ nó thật nhẹ — đừng biến nó thành tội lỗi, hãy để nó trở thành một lời nhắc.
- Entities: khán giả, gương mặt, chiếc ghế (callback motif), bàn tay, câu chưa kịp nói, tội lỗi, lời nhắc
- Primary Action: giữ nhẹ; không biến thành tội lỗi; để trở thành lời nhắc
- Emotional Context: compassion
- Causal Relation: None.
- Narrative Function: resolution
- Required Evidence: 4 hình ảnh có thể hiện lên trong lòng khán giả (gương mặt/chiếc ghế/bàn tay/câu chưa kịp nói) — đây là các khả năng mở, không phải khẳng định cụ thể một hình ảnh nào là "đúng"; chỉ dẫn cảm xúc (giữ nhẹ, không tội lỗi, thành lời nhắc)
- Forbidden Hallucination: không chọn một trong 4 hình ảnh làm hình ảnh "chính thức" duy nhất — narration liệt kê như các khả năng ngang hàng, không ưu tiên hình ảnh nào

**BEAT_126**
- Source: L251
- Meaning: Lời nhắc 1: tình thương cần được nói khi còn có thể.
- Entities: tình thương
- Primary Action: nói (tình thương, khi còn có thể)
- Emotional Context: None explicit.
- Causal Relation: None.
- Narrative Function: resolution
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_127**
- Source: L253
- Meaning: Lời nhắc 2: biết ơn cần đi cùng trí tuệ.
- Entities: biết ơn, trí tuệ
- Primary Action: No explicit action.
- Emotional Context: gratitude
- Causal Relation: None.
- Narrative Function: resolution
- Required Evidence: luận đề nguyên văn
- Forbidden Hallucination: None thêm

**BEAT_128**
- Source: L255
- Meaning: Lời nhắc 3 (khép lại toàn tập): hiếu đạo sâu nhất không phải sống trong mặc cảm, mà là sống sao cho từ mình, bớt đi một chút khổ đau truyền tiếp vào thế gian.
- Entities: hiếu đạo, mặc cảm, khổ đau, thế gian
- Primary Action: No explicit action — luận đề khép lại toàn bộ episode.
- Emotional Context: None explicit (câu kết mang tính tổng hợp, không gọi tên một cảm xúc cụ thể).
- Causal Relation: None. **Đây là câu kết thúc toàn episode — tổng hợp lại các luận đề đã xây dựng xuyên suốt (đặc biệt liên kết với BEAT_050, BEAT_064, BEAT_111-113 về việc "dừng khổ đau truyền tiếp").**
- Narrative Function: resolution
- Required Evidence: luận đề khép lại nguyên văn; đây là câu cuối cùng của toàn bộ narration
- Forbidden Hallucination: None thêm

---

## Ghi chú tổng hợp cho các bước sau (không phải chỉ dẫn hình ảnh)

Các mục dưới đây là quan sát về cấu trúc ngữ nghĩa xuyên suốt narration, phục vụ Visual Obligation/Continuity Planning ở bước kế tiếp — **không phải chỉ định về scene, camera, hay vật thể cụ thể**:

1. **Motif "chiếc ghế trống"** xuất hiện có chủ đích tại: BEAT_001, BEAT_002 (thiết lập), BEAT_042, BEAT_047 (nhắc lại giữa phim), BEAT_085 (dùng làm công cụ tự vấn), BEAT_121 (giải quyết/callback), BEAT_125 (liệt kê như một trong bốn khả năng gợi nhớ ở đoạn kết). Đây là continuity object hợp lệ vì có căn cứ tường minh, lặp lại theo chủ đích tường thuật rõ ràng — không phải một vật thể tự phát sinh không có nguồn gốc.
2. **Câu chuyện người cha phá vỡ vòng lặp** (BEAT_056–BEAT_063) là một đơn vị tường thuật liên tục có nhân vật/hành động/lời thoại cụ thể — bắt buộc được các bước sau xử lý như MỘT continuity thread xuyên suốt 8 beat này, không tách rời thành các hình ảnh không liên quan nhau.
3. **Cảnh báo nguồn gốc tại BEAT_063** áp dụng ngược lại cho toàn bộ BEAT_056–062: không được trình bày như trích dẫn kinh điển hay lời Đức Phật.
4. **BEAT_124** thuộc về tập tiếp theo (không phải nội dung của EP004) — các bước sau không được coi đây là một obligation cần thể hiện như nội dung chính, chỉ có thể thể hiện như một "teaser/chuyển tiếp", nếu có.
5. **31 beat có `causal_relation` tường minh** (dạng Cause↓Effect hoặc chuỗi nhân quả nội tại) — đây là các điểm bắt buộc giữ nguyên quan hệ nhân quả nếu bước sau tách beat thành nhiều đơn vị nhỏ hơn.
6. **Narrative Function được dùng đúng 8 giá trị cho phép**, không có category tự tạo nào ngoài danh sách đã cho — xem bảng đối soát bên dưới (đếm lại trực tiếp bằng `grep` trên chính file này, không phải số ước lượng).

## Bảng đối soát Narrative Function (đếm lại trực tiếp từ 128 beat, đã kiểm chứng bằng `grep -o`)

| Narrative Function | Số lượng beat |
|---|---:|
| reflection | 54 |
| explanation | 21 |
| transition | 15 |
| setup | 14 |
| conflict | 13 |
| resolution | 7 |
| revelation | 3 |
| climax | 1 |
| **Tổng** | **128** |

*(Phân bố nghiêng mạnh về `reflection` phản ánh đúng bản chất narration: đây là một bài giảng suy ngẫm liên tục với rất nhiều luận đề/aphorism độc lập, không phải một kịch bản nhiều biến cố — số lượng lớn beat "reflection" không phải dấu hiệu phân loại sai, mà là đặc điểm thật của thể loại nội dung này. Chỉ có 1 `climax` (BEAT_058 — khoảnh khắc người cha "dừng lại") vì đây là episode duy nhất có một cấu trúc truyện lồng bên trong (BEAT_056–063) với đúng một điểm bản lề; phần còn lại của narration là tiểu luận suy ngẫm nối tiếp, không có climax kịch tính theo nghĩa cổ điển.)*
