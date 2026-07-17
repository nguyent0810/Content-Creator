# 04B — Visual Obligations (EP004)
Phase B của Video Creation Pipeline. Tuân thủ `VIDEO_CREATION_SYSTEM_SPEC.md` (Mục 2.4, Mục 3.2). Nguồn duy nhất của bước này là `04A_SEMANTIC_BEATS.md` — không đọc lại narration gốc để suy diễn thêm. Đây không phải scene, không phải prompt, không phải storyboard, không phải shot, không phải template, không phải composition. Đây chỉ là danh sách bằng chứng hình ảnh tối thiểu bắt buộc.

## Phương pháp phân loại Visualizable Type (áp dụng nhất quán cho toàn bộ 128 obligation)

- **Concrete**: Beat có một hành động/tình huống/tương tác cụ thể, có chủ thể xác định (kể cả khi chủ thể là "một người" chung chung), có thể quan sát trực tiếp trong một khoảnh khắc hình ảnh.
- **Abstract**: Beat phát biểu một khái niệm/nguyên lý/phân biệt/định nghĩa, nhưng có nêu tên ít nhất một chủ thể (dù chung chung) mà thần thái/tư thế/hành vi của chủ thể đó CÓ THỂ dùng làm dấu hiệu quan sát gián tiếp cho khái niệm — không tuyên bố dấu hiệu đó "chính là" khái niệm.
- **Symbolic**: Chính narration đã đặt tên một hình ảnh/ẩn dụ cụ thể (đèn, roi, hạt giống, hương, "địa ngục" như ẩn dụ cho một căn nhà bất hoà...) — hình ảnh đó (không phải khái niệm nó biểu trưng) trở thành evidence, có gắn nhãn rõ đây là ẩn dụ đã được narration xác nhận, không phải biểu tượng tự phát minh.
- **Non-Visual**: Beat là (a) câu bản lề/chuyển ý thuần tuý không có chủ thể ("Điều này cần được hiểu cẩn trọng"), (b) câu hỏi hướng thẳng tới khán giả ("bạn"), (c) lời rào đón về nguồn/phạm vi (disclaimer), hoặc (d) một phát biểu về trạng thái nội tâm của một chủ thể hoàn toàn không xác định, không có hành vi/bối cảnh nào được narration nêu để neo vào.

## [Bổ sung 2026-07-15] Quy tắc bàn giao cho Phase C (Shot Planning)

Các quy tắc dưới đây được bổ sung sau khi 04B đã hoàn tất, để làm rõ mối quan hệ giữa Visual Obligation (tầng này) và Shot (tầng kế tiếp) — không thay đổi bất kỳ nội dung obligation nào đã viết ở trên.

### Quan hệ Obligation ↔ Shot (không phải 1-1)

```
1 obligation không đồng nghĩa 1 shot.
Non-Visual obligation có thể không cần dedicated shot.
Một shot có thể cover nhiều obligation liền kề.
Một obligation phức tạp có thể cần nhiều shot.
Critical và High obligation không được bỏ.
```

Hệ quả trực tiếp: 128 Visual Obligation **không** kéo theo 128 shot. Phase C có toàn quyền gộp các Non-Visual obligation liền kề cùng ngữ cảnh vào một shot lân cận (không tạo shot riêng cho chúng), và có toàn quyền tách một obligation Concrete/Symbolic có nhiều evidence rời rạc (ví dụ OBL_040, OBL_045, OBL_065 — mỗi obligation này liệt kê từ 3 đến 9 evidence độc lập) thành nhiều shot. Ràng buộc duy nhất không được vi phạm: **mọi obligation có Visual Importance = Critical hoặc High phải có ít nhất một shot (dedicated hoặc shared) đại diện cho nó** — không được để trống.

### Phân biệt Source Fact / Production Fill / Forbidden Addition

Mọi nội dung xuất hiện trong một shot ở Phase C phải được phân loại vào đúng một trong ba nhóm sau — sự nhầm lẫn giữa "Production Fill" và "Source Fact" là nguồn gốc trực tiếp của hallucination đã ghi nhận trong `VIDEO_CREATION_ARCHITECTURE_AUDIT.md`.

| Nhóm | Định nghĩa | Ai quyết định | Được trình bày như thế nào |
|---|---|---|---|
| **Source Fact** | Nội dung có căn cứ trực tiếp trong `Required Subject`/`Required Action`/`Required Setting`/`Required Visual Evidence` của chính obligation — tức là bắt nguồn từ narration qua 04A→04B. | Đã được 04A/04B quyết định, Phase C chỉ kế thừa. | Trình bày như dữ kiện đã được narration xác nhận. |
| **Production Fill** | Lựa chọn dàn dựng cần thiết để một cảnh Concrete/Symbolic có thể tồn tại được về mặt hình ảnh, nhưng bản thân lựa chọn đó **không được narration chỉ định cụ thể** — ví dụ: chất liệu ghế (gỗ/tre), màu áo một nhân vật generic, bố cục không gian trong nhà, kiểu dáng chiếc đèn ở BEAT_121. | Phase C (hoặc Phase D sau này) được quyền chọn, miễn nhất quán nội bộ (không đổi giữa các shot cùng continuity thread). | **Không được trình bày như dữ kiện narration xác nhận** — phải gắn nhãn rõ là lựa chọn dàn dựng, để bất kỳ ai review sau này phân biệt được đâu là điều narration thực sự nói, đâu là điều êkíp dựng cảnh chọn thêm để hình ảnh tồn tại được. |
| **Forbidden Addition** | Bất kỳ nội dung nào đã bị chính obligation liệt kê trong `Forbidden Hallucination`, hoặc bất kỳ thực thể/sự kiện/biểu tượng mới nào không truy vết được về `Required Visual Evidence` và cũng không phải một lựa chọn dàn dựng trung tính (tức là nó mang thêm ý nghĩa/thông tin mới). | Không ai được quyết định thêm — đây là vùng cấm tuyệt đối. | Không được xuất hiện trong shot dưới bất kỳ hình thức nào. |

Ví dụ áp dụng cụ thể (không thay đổi obligation gốc, chỉ minh hoạ cách Phase C nên phân loại): ở OBL_001, "chiếc ghế trống trong nhà" là Source Fact; việc ghế làm bằng gỗ, phòng có cửa sổ ở hướng nào, ánh sáng buổi nào trong ngày là Production Fill (miễn giữ nhất quán các lần "ghế" tái xuất ở OBL_005/042/047/085/121); việc thêm một chiếc đồng hồ treo tường đang dừng lại như ẩn dụ thời gian là Forbidden Addition (một biểu tượng mới, không có trong `Required Visual Evidence`, mang thêm ý nghĩa narration không xác nhận).

## Validation Summary

| Kiểm tra | Kết quả |
|---|---|
| Tổng Semantic Beat (từ 04A) | 128 |
| Tổng Visual Obligation | 128 |
| Tỉ lệ ánh xạ | 1 Beat → đúng 1 Obligation, không gộp, không tách |
| beat_id giữ nguyên | Đạt — toàn bộ BEAT_001–BEAT_128 giữ nguyên ID |
| Obligation không truy vết được về Semantic Beat | Không có |
| Scene/camera/lighting/framing/cinematic wording xuất hiện trong file | Không có (tự kiểm tra bằng cách không dùng bất kỳ từ vựng điện ảnh nào khi soạn) |
| Continuity object tự phát minh (không có căn cứ ở 04A) | Không có — mọi continuity object trích từ chính Entities/ghi chú continuity đã có trong 04A |

---

## ACT I — BEAT_001–BEAT_012

**OBL_001** (beat_id: BEAT_001)
- Required Subject: chiếc ghế
- Required Action: No explicit visual action.
- Required Setting: Bối cảnh trong nhà (không có chi tiết cụ thể hơn được nêu ở beat này).
- Required Visual Evidence: sự hiện diện của một chiếc ghế trống; không có người ngồi trên ghế
- Visualizable Type: Concrete — có một đối tượng vật lý cụ thể (chiếc ghế) và một trạng thái quan sát được (trống, không người)
- Visualization Strategy: mô tả trực tiếp evidence — một chiếc ghế trống trong không gian nhà, không có người ngồi
- Required Continuity: object continuity — chiếc ghế được giới thiệu lần đầu tại đây, sẽ tái xuất tại BEAT_002, BEAT_042, BEAT_047, BEAT_085, BEAT_121, BEAT_125
- Forbidden Hallucination: không thêm nhân vật đang ngồi hoặc vừa rời khỏi ghế; không đặc tả chất liệu/kiểu dáng ghế (gỗ, tre...) vì 04A không xác nhận chi tiết này ở beat gốc
- Visual Importance: Critical — đây là hình ảnh mở đầu và là motif xuyên suốt toàn episode; thiếu nó sẽ mất điểm neo cảm xúc chính

**OBL_002** (beat_id: BEAT_002)
- Required Subject: chiếc ghế, bàn ăn, cửa sổ, mẹ, cha
- Required Action: mẹ nhặt rau (hành động hồi tưởng/thường lệ); cha uống trà (hành động hồi tưởng/thường lệ); một người đi ngang qua không dừng lại
- Required Setting: cạnh bàn ăn; gần cửa sổ — hai vị trí cụ thể trong không gian nhà đã thiết lập ở BEAT_001
- Required Visual Evidence: vị trí ghế tương ứng với bàn ăn và cửa sổ; tư thế mẹ khi nhặt rau; tư thế cha khi uống trà; hành vi đi ngang qua không dừng lại
- Visualizable Type: Concrete
- Visualization Strategy: mô tả trực tiếp — hai vị trí của ghế (cạnh bàn ăn, gần cửa sổ) gắn với hai hành động thường lệ (mẹ nhặt rau, cha uống trà); có thể là hình ảnh hồi tưởng, không phải khoảnh khắc hiện tại
- Required Continuity: object continuity — cùng chiếc ghế với BEAT_001; character continuity — mẹ và cha được giới thiệu lần đầu ở đây, generic/không đặc tả ngoại hình; location continuity — bàn ăn/cửa sổ thuộc cùng không gian nhà với BEAT_001
- Forbidden Hallucination: không đặt tên hay đặc tả ngoại hình mẹ/cha; không thêm nhân vật đi ngang qua có danh tính cụ thể
- Visual Importance: High — elaborates motif chính nhưng không phải hình ảnh mở đầu tuyệt đối như BEAT_001

**OBL_003** (beat_id: BEAT_003)
- Required Subject: "ta" — chủ thể chung, không xác định danh tính
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None — đây là một niềm tin nội tâm, không có hành vi/bối cảnh nào được narration nêu để neo vào
- Visualizable Type: Non-Visual — phát biểu về trạng thái nội tâm của một chủ thể hoàn toàn không xác định, không có hành vi cụ thể nào được narration cung cấp
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context (được minh hoạ gián tiếp qua các lý do trì hoãn cụ thể ở BEAT_004).
- Required Continuity: None.
- Forbidden Hallucination: không tự phát minh một cảnh hay nhân vật cụ thể để minh hoạ niềm tin này
- Visual Importance: Low — có thể gộp ý nghĩa vào evidence của BEAT_004 mà không mất nghĩa cốt lõi

**OBL_004** (beat_id: BEAT_004)
- Required Subject: cuộc gọi, chuyến về thăm, hành vi chuyển khoản, thuốc, quà
- Required Action: trì hoãn gọi điện; trì hoãn về thăm; chuyển khoản; mua thuốc; gửi quà
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hành vi thực hiện nghĩa vụ vật chất (chuyển khoản/thuốc/quà) thay thế cho hành vi hiện diện trực tiếp (gọi/về thăm)
- Visualizable Type: Concrete — có các hành vi cụ thể có thể quan sát (dù là hành vi "không làm" gọi/về thăm, được thay bằng hành vi vật chất có thể thấy)
- Visualization Strategy: mô tả trực tiếp evidence — một hành vi chuyển khoản/gửi quà/mua thuốc, như đại diện cho việc "làm tròn bổn phận" thay vì hiện diện
- Required Continuity: None.
- Forbidden Hallucination: không đặc tả số tiền, loại thuốc, loại quà cụ thể; không gán hành vi này cho cùng một nhân vật cụ thể nào đã xuất hiện trước đó
- Visual Importance: Medium — minh hoạ hữu ích cho lý lẽ nhưng bản thân không phải điểm neo cảm xúc trung tâm

**OBL_005** (beat_id: BEAT_005)
- Required Subject: chiếc ghế
- Required Action: chiếc ghế trở nên trống (sự kiện xảy ra, không phải hành động chủ động của một nhân vật)
- Required Setting: Bối cảnh trong nhà, kế thừa từ BEAT_001/002.
- Required Visual Evidence: sự chuyển đổi trạng thái của ghế — từ có gắn bó với người (BEAT_002) sang trống hẳn; tính chất bất ngờ/không báo trước không thể tự nó hiển thị bằng hình ảnh tĩnh
- Visualizable Type: Abstract — bản thân "sự trống" là Concrete (đã có ở BEAT_001), nhưng ý "không báo trước" (yếu tố thời gian/bất ngờ) là một khẳng định trừu tượng không thể hiện trực tiếp bằng một khung hình
- Visualization Strategy: mô tả dấu hiệu quan sát được — cùng chiếc ghế đã thiết lập, nay ở trạng thái trống hẳn (khác biệt với BEAT_002 vốn còn gắn với mẹ/cha); tính "bất ngờ" chỉ suy ra được từ vị trí của beat này trong mạch tường thuật, không phải từ một dấu hiệu hình ảnh riêng
- Required Continuity: object continuity — cùng chiếc ghế với BEAT_001/002, nay chuyển trạng thái
- Forbidden Hallucination: không thêm cảnh cụ thể về nguyên nhân mất mát (bệnh viện, tang lễ...) — không có trong 04A ở beat này
- Visual Importance: Critical — đây là bản lề cảm xúc của toàn bộ motif ghế

**OBL_006** (beat_id: BEAT_006)
- Required Subject: None — đây là các câu nói chưa kịp nói, không có chủ thể hành động cụ thể được xác định trong 04A cho beat này (chỉ có "con người ta" chung chung)
- Required Action: "chưa kịp nói" — hành động không xảy ra (một sự thiếu vắng, khó hiển thị dương tính)
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None đủ để hiển thị trực tiếp 5 câu nói cụ thể bằng hình ảnh — nội dung của beat này là ngôn ngữ (lời nói chưa được nói ra), không phải hành vi thị giác
- Visualizable Type: Non-Visual — nội dung cốt lõi là các câu nói cụ thể (ngôn ngữ), một sự vắng mặt của hành động nói, không có evidence hình ảnh trực tiếp nào được 04A xác nhận
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context (gắn liền với BEAT_005 — ghế trống — làm bối cảnh thị giác duy nhất khả dụng).
- Required Continuity: object continuity — có thể tiếp nối bối cảnh trống của chiếc ghế từ BEAT_005 nếu bước sau cần một hình ảnh nền, nhưng bản thân obligation này không yêu cầu chiếc ghế
- Forbidden Hallucination: không tạo hình ảnh "viết ra" 5 câu nói (không phải văn bản viết — 04A đã ghi rõ đây là lời nói ra miệng); không đạo cụ ghi chú/thư/note nào
- Visual Importance: Low — có thể gộp về mặt bối cảnh với evidence của BEAT_005 mà không mất nghĩa cốt lõi (nghĩa cốt lõi nằm ở lời thoại, không ở hình ảnh)

**OBL_007** (beat_id: BEAT_007)
- Required Subject: None cụ thể — đây là phát biểu nhận thức chung + hồi cố series, không có chủ thể hành động
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — nội dung là kiến thức/nhận thức phổ biến về Kinh Địa Tạng và liên kết với các tập trước
- Visualizable Type: Non-Visual — phát biểu meta về nội dung series, không có chủ thể/hành động cụ thể
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None (04A không xác nhận continuity xuyên-episode cụ thể).
- Forbidden Hallucination: không bịa cảnh cụ thể minh hoạ "địa ngục/nghiệp báo/Địa Tạng Bồ Tát" ở beat này — 04A không cung cấp evidence hình ảnh cho beat này
- Visual Importance: Low

**OBL_008** (beat_id: BEAT_008)
- Required Subject: None cụ thể.
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual — câu bản lề chuyển ý thuần tuý, không có chủ thể
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không phát minh hình ảnh minh hoạ cho "trở về đầu nguồn"
- Visual Importance: Low

**OBL_009** (beat_id: BEAT_009)
- Required Subject: None cụ thể — đây là phát biểu về một nghịch lý cấu trúc (bản kinh vs cõi trời), không có chủ thể vật lý
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — 04A ghi rõ "chưa mô tả cụ thể hình ảnh cõi trời/địa ngục" ở beat này
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không tự vẽ hình ảnh địa ngục hay cõi trời ở beat này — 04A minh thị cấm điều này (Forbidden Hallucination của chính beat gốc)
- Visual Importance: Low

**OBL_010** (beat_id: BEAT_010)
- Required Subject: Đức Phật, thân mẫu (Ngài)
- Required Action: Đức Phật thuyết pháp
- Required Setting: Cung Trời Đao Lợi — 04A xác nhận đây là địa điểm cụ thể được narration nêu tên.
- Required Visual Evidence: hành vi thuyết pháp của Đức Phật; sự hiện diện/liên hệ với thân mẫu (không đặc tả chi tiết ngoại hình)
- Visualizable Type: Concrete — có chủ thể, hành động, và địa điểm được narration xác nhận cụ thể
- Visualization Strategy: mô tả trực tiếp evidence — Đức Phật đang thuyết pháp tại Cung Trời Đao Lợi, trong liên hệ với thân mẫu; không đặc tả ngoại hình chi tiết vì 04A không cung cấp
- Required Continuity: location continuity — Cung Trời Đao Lợi sẽ được nhắc lại ở BEAT_016, BEAT_017, BEAT_076; character continuity — Đức Phật/thân mẫu tiếp tục ở BEAT_022
- Forbidden Hallucination: không đặc tả kiến trúc Cung Trời Đao Lợi (04A xác nhận chưa có mô tả); không thêm lời thoại của Đức Phật hay thân mẫu (Character Usage Plan của episode cấm invented dialogue)
- Visual Importance: Critical — đây là hình ảnh nền tảng của toàn bộ tiền đề giáo lý episode

**OBL_011** (beat_id: BEAT_011)
- Required Subject: bản kinh (biểu tượng khái niệm, không phải vật thể vật lý cụ thể), địa ngục, hành động báo ân
- Required Action: No explicit visual action — đây là câu hỏi tu từ.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None — 04A ghi rõ "không trả lời câu hỏi ở beat này", không có evidence hình ảnh được cung cấp
- Visualizable Type: Non-Visual — câu hỏi hướng tới khán giả/người nghe (dạng tu từ), không có chủ thể hành động thị giác
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không tự trả lời câu hỏi bằng hình ảnh cụ thể ở beat này
- Visual Importance: Low

**OBL_012** (beat_id: BEAT_012)
- Required Subject: cõi trời, ký ức về mẹ, trái tim con người
- Required Action: No explicit visual action — câu hỏi tu từ.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không tự trả lời câu hỏi bằng hình ảnh cụ thể ở beat này
- Visual Importance: Low

---

## ACT II — BEAT_013–BEAT_024

**OBL_013** (beat_id: BEAT_013)
- Required Subject: bài học hiếu đạo, nghi lễ, mâm cỗ, cúng bái, sự phục tùng
- Required Action: No explicit visual action — câu hỏi tu từ.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — 04A ghi rõ không trả lời câu hỏi ở beat này.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không tự trả lời câu hỏi; không minh hoạ cụ thể "mâm cỗ/cúng bái" ở beat này vì đây chỉ là liệt kê trong câu hỏi, chưa phải nội dung khẳng định
- Visual Importance: Low

**OBL_014** (beat_id: BEAT_014)
- Required Subject: None cụ thể.
- Required Action: "đi thật chậm" — đây là chỉ dẫn nhịp điệu tường thuật, không phải hành động vật lý của nhân vật (04A xác nhận rõ điều này).
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual — mặc dù có động từ "đi", 04A xác nhận đây không phải hành động vật lý mà là chỉ dẫn nhịp độ tường thuật
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không hình ảnh hoá "đi chậm" bằng một nhân vật đang đi bộ — đây sẽ là một hành động bịa đặt không có căn cứ
- Visual Importance: Low

**OBL_015** (beat_id: BEAT_015)
- Required Subject: kinh điển, truyền thống, ký ức gia đình, người mất cha mẹ, người chăm cha mẹ già, người có vết thương gia đình
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp cho từng nhóm — đây là một danh sách lý do trừu tượng, không có hành vi cụ thể nào được 04A gán cho từng nhóm
- Visualizable Type: Abstract — có nêu tên các nhóm chủ thể (người mất cha mẹ, người chăm cha mẹ già, người có vết thương gia đình) dù không có hành vi cụ thể, thần thái của các nhóm này có thể dùng làm dấu hiệu gián tiếp
- Visualization Strategy: mô tả dấu hiệu quan sát được — ví dụ thần thái mệt mỏi (nhóm chăm sóc) hoặc trầm lặng (nhóm mất mát) như dấu hiệu gián tiếp; không đặc tả nhân vật cụ thể cho từng nhóm
- Required Continuity: None.
- Forbidden Hallucination: không đặc tả nhân vật cụ thể đại diện cho từng nhóm trong 5 nhóm đã liệt kê
- Visual Importance: Medium

**OBL_016** (beat_id: BEAT_016)
- Required Subject: Cung Trời Đao Lợi
- Required Action: No explicit visual action — phát biểu giáo lý + cảnh báo cách hiểu sai.
- Required Setting: Cung Trời Đao Lợi (địa điểm được nêu tên, nhưng nội dung beat này là CẢNH BÁO về cách hiểu SAI của nó — "xa xôi, rực rỡ, tách biệt" — không phải mô tả cần thể hiện là đúng).
- Required Visual Evidence: None cần hiển thị dương tính — 04A ghi rõ "không mô tả cụ thể 'rực rỡ' bằng hình ảnh chi tiết vì đây là mô tả về cách hiểu sai cần tránh"
- Visualizable Type: Non-Visual — nội dung beat là một cảnh báo nhận thức luận (đừng hiểu sai theo cách X), không phải một cảnh cần dựng
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context (được làm rõ dương tính ở BEAT_017).
- Required Continuity: location continuity — Cung Trời Đao Lợi cùng địa điểm với BEAT_010.
- Forbidden Hallucination: không dựng cảnh "xa xôi rực rỡ tách biệt" dù đây là cụm từ xuất hiện trong beat — nó là mô tả của cách hiểu SAI, không phải nội dung cần khẳng định
- Visual Importance: Low

**OBL_017** (beat_id: BEAT_017)
- Required Subject: pháp hội, bậc Giác ngộ (Đức Phật, đã giới thiệu ở BEAT_010)
- Required Action: No explicit visual action — khẳng định giáo lý.
- Required Setting: Cung Trời Đao Lợi, kế thừa từ BEAT_010/016.
- Required Visual Evidence: None trực tiếp cho khái niệm "lòng biết ơn"; thần thái của "bậc Giác ngộ" (đã có ở BEAT_010) có thể là dấu hiệu gián tiếp
- Visualizable Type: Abstract — khái niệm "lòng biết ơn là trung tâm cảm xúc" là trừu tượng, nhưng có chủ thể cụ thể (bậc Giác ngộ) để neo dấu hiệu quan sát
- Visualization Strategy: mô tả dấu hiệu quan sát được — thần thái điềm tĩnh/tôn kính của bậc Giác ngộ hướng về thân mẫu, như dấu hiệu gián tiếp cho "không quên ân nghĩa"; không tuyên bố đây là hình ảnh trực tiếp của "lòng biết ơn"
- Required Continuity: character continuity — cùng "bậc Giác ngộ"/Đức Phật với BEAT_010; location continuity — Cung Trời Đao Lợi
- Forbidden Hallucination: không thêm hình ảnh cụ thể nào khác ngoài những gì đã có ở BEAT_010
- Visual Importance: Medium

**OBL_018** (beat_id: BEAT_018)
- Required Subject: None cụ thể.
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không phát minh hình ảnh cho câu bản lề này
- Visual Importance: Low

**OBL_019** (beat_id: BEAT_019)
- Required Subject: giác ngộ, tình nghĩa, mẹ, cha, chấp trước
- Required Action: No explicit visual action — phát biểu giáo lý theo cấu trúc phủ định kép.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — đây là một chuỗi định nghĩa phủ định trừu tượng
- Visualizable Type: Abstract — có nêu tên chủ thể liên quan (mẹ, cha) dù nội dung là định nghĩa phủ định
- Visualization Strategy: mô tả dấu hiệu quan sát được — nếu cần một dấu hiệu, đó chỉ có thể là thần thái điềm tĩnh/không lạnh lùng của một chủ thể chung chung; đây là dấu hiệu rất gián tiếp, không đủ để khẳng định là evidence mạnh
- Required Continuity: None.
- Forbidden Hallucination: không dựng cảnh minh hoạ "chấp trước/bám víu/chiếm hữu" bằng hình ảnh cụ thể — đây là khái niệm bị phủ định, không phải nội dung cần khẳng định
- Visual Importance: Low

**OBL_020** (beat_id: BEAT_020)
- Required Subject: None cụ thể.
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không phát minh hình ảnh cho câu bản lề này
- Visual Importance: Low

**OBL_021** (beat_id: BEAT_021)
- Required Subject: None cụ thể — đây là 4 định nghĩa khái niệm (chấp trước/biết ơn/báo ân/từ bi), không có chủ thể vật lý xác định trong 04A
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — 04A xác nhận "không minh hoạ bằng ví dụ cụ thể" ở beat gốc
- Visualizable Type: Non-Visual — định nghĩa khái niệm thuần tuý, không có chủ thể/hành vi neo được
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không minh hoạ 4 khái niệm bằng hình ảnh/nhân vật cụ thể — 04A đã cấm điều này ở beat gốc
- Visual Importance: Low

**OBL_022** (beat_id: BEAT_022)
- Required Subject: Đức Phật, thân mẫu, lòng tri ân
- Required Action: Đức Phật thuyết pháp (kế thừa từ BEAT_010)
- Required Setting: Cung Trời Đao Lợi, kế thừa từ BEAT_010.
- Required Visual Evidence: hành vi thuyết pháp/hiện diện của Đức Phật trong liên hệ với thân mẫu — không có hành vi mới nào ngoài những gì đã ở BEAT_010
- Visualizable Type: Concrete (phần hành động thuyết pháp) pha Abstract (phần "lòng tri ân được trí tuệ soi sáng") — ghi nhận là Concrete vì chủ thể/hành động chính đã có căn cứ cụ thể từ BEAT_010, phần diễn giải trừu tượng chỉ là khung ý nghĩa đi kèm, không phải evidence riêng
- Visualization Strategy: mô tả trực tiếp evidence — tái sử dụng chính xác hành vi/chủ thể của BEAT_010 (Đức Phật thuyết pháp trong liên hệ với thân mẫu), không thêm hành vi mới
- Required Continuity: character continuity — cùng Đức Phật/thân mẫu với BEAT_010; location continuity — Cung Trời Đao Lợi
- Forbidden Hallucination: không thêm hành động/lời thoại nào của Đức Phật ngoài "thuyết pháp trong liên hệ với thân mẫu" (04A minh thị cấm điều này)
- Visual Importance: Medium — củng cố ý nghĩa của BEAT_010 nhưng không phải điểm giới thiệu evidence mới

**OBL_023** (beat_id: BEAT_023)
- Required Subject: giác ngộ, ân nghĩa
- Required Action: No explicit visual action — luận đề khẳng định.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual — luận đề trừu tượng thuần tuý, không có chủ thể vật lý
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm cần liệt kê.
- Visual Importance: Low

**OBL_024** (beat_id: BEAT_024)
- Required Subject: trí tuệ, lòng biết ơn
- Required Action: No explicit visual action — luận đề khẳng định.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

---

## ACT III — BEAT_025–BEAT_038

**OBL_025** (beat_id: BEAT_025)
- Required Subject: bài học hiếu đạo, câu hỏi mới
- Required Action: No explicit visual action — tái định hướng câu hỏi.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_026** (beat_id: BEAT_026)
- Required Subject: người con, mẹ, cha, điện thoại
- Required Action: gửi tiền đều đặn (chuyển khoản); không gọi đủ lâu để lắng nghe
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hành vi chuyển khoản/thông báo trên điện thoại; một cuộc gọi ngắn/vội (đại diện cho việc "không đủ dài để nghe"); ba nội dung chưa được nghe (đau lưng của mẹ, chiều mưa của cha, giọng hai người già đi) — bản thân ba nội dung này không thể hiển thị dương tính (chúng là sự VẮNG MẶT của một cuộc trò chuyện), chỉ có thể suy ra gián tiếp qua độ ngắn của cuộc gọi
- Visualizable Type: Concrete — có chủ thể (người con, mẹ, cha) và hành vi cụ thể (chuyển khoản, cuộc gọi ngắn) có thể quan sát trực tiếp trong một khoảnh khắc, đại diện cho một mẫu hình lặp lại nhiều năm mà narration mô tả
- Visualization Strategy: mô tả trực tiếp evidence — hành vi chuyển khoản và một cuộc gọi ngắn/kết thúc nhanh, như đại diện cho mẫu hình đã narration mô tả; ba nội dung chưa được nghe không được hiển thị trực tiếp mà chỉ ngụ ý qua độ ngắn của tương tác
- Required Continuity: character continuity — "người con", "mẹ", "cha" là các chủ thể mới, generic, không liên kết với mẹ/cha ở BEAT_002 (04A không xác nhận đây là cùng gia đình)
- Forbidden Hallucination: không đặc tả số tiền cụ thể; không thêm chi tiết nghề nghiệp/nơi ở của người con; không hiển thị "đau lưng của mẹ" hay "chiều mưa của cha" như hình ảnh dương tính — đây là nội dung KHÔNG xảy ra
- Visual Importance: High — ví dụ cụ thể hoá luận điểm cốt lõi "tiền không thay được lắng nghe"

**OBL_027** (beat_id: BEAT_027)
- Required Subject: tiền, thuốc, sự lắng nghe
- Required Action: No explicit visual action — luận đề đối lập.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — đây là một aphorism đối lập hai khái niệm
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context (được minh hoạ cụ thể ở BEAT_026).
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low — nội dung đã được BEAT_026 minh hoạ cụ thể hơn, obligation này có thể gộp về ý nghĩa mà không mất nghĩa cốt lõi

**OBL_028** (beat_id: BEAT_028)
- Required Subject: vật chất, sự có mặt
- Required Action: No explicit visual action — luận đề đối lập.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_029** (beat_id: BEAT_029)
- Required Subject: gia đình, bàn thờ, mâm cỗ, khách khứa, anh em
- Required Action: làm giỗ lớn (bàn thờ sáng đèn, mâm cỗ đầy, khách khứa đông); không nhìn mặt nhau (sau bữa ăn, giữa anh em)
- Required Setting: không gian tổ chức giỗ (không có chi tiết cụ thể hơn — trong nhà hoặc nơi thờ cúng, 04A không xác định rõ hơn "làm giỗ").
- Required Visual Evidence: hình thức lớn của buổi giỗ (bàn thờ sáng đèn, mâm cỗ đầy, khách khứa đông); tương phản — anh em không nhìn mặt nhau sau bữa ăn
- Visualizable Type: Concrete
- Visualization Strategy: mô tả trực tiếp evidence — cảnh giỗ hình thức lớn, sau đó là khoảnh khắc anh em tránh nhìn nhau
- Required Continuity: None (nhân vật/gia đình mới, không liên kết với các beat khác).
- Forbidden Hallucination: không đặc tả số lượng người cụ thể; không thêm chi tiết nội dung xung đột cụ thể (loại "câu nói cũ" không được nêu trong 04A)
- Visual Importance: High — ví dụ cụ thể hoá luận điểm "hình thức vs thực chất"

**OBL_030** (beat_id: BEAT_030)
- Required Subject: hiếu đạo, người đã khuất, người còn sống
- Required Action: trình diễn sự nhớ thương (trước người đã khuất); làm tổn thương (người còn sống)
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hành vi "trình diễn" (nghi lễ/thái độ hướng tới người đã khuất) đối lập với hành vi gây tổn thương người sống — cả hai đều trừu tượng ở mức khái quát, không có chủ thể cụ thể
- Visualizable Type: Abstract — có nêu hành động (trình diễn, làm tổn thương) nhưng chủ thể hoàn toàn chung chung ("người sống"), ẩn dụ "sân khấu" là ẩn dụ do chính narration đặt tên
- Visualization Strategy: mô tả dấu hiệu quan sát được — một hành vi tưởng niệm mang tính phô diễn, đối lập ngầm với một tương tác căng thẳng giữa người sống; đây là dấu hiệu gián tiếp, không phải cảnh cụ thể có nhân vật xác định
- Required Continuity: None.
- Forbidden Hallucination: không đặc tả nhân vật cụ thể; không dựng "sân khấu" theo nghĩa đen (rạp hát, ánh đèn sân khấu) — đây là ẩn dụ về hành vi phô diễn, không phải một địa điểm sân khấu thật
- Visual Importance: Medium

**OBL_031** (beat_id: BEAT_031)
- Required Subject: hiếu đạo, phục tùng mù quáng, gánh nặng
- Required Action: No explicit visual action — luận đề cảnh báo.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_032** (beat_id: BEAT_032)
- Required Subject: người chăm sóc, mẹ già
- Required Action: thay áo; đút cháo; đưa đi khám; lau vết đau
- Required Setting: Setting intentionally unspecified (không gian chăm sóc tại nhà được ngụ ý nhưng không đặc tả cụ thể trong 04A).
- Required Visual Evidence: 4 hành động chăm sóc cụ thể (thay áo/đút cháo/đưa đi khám/lau vết đau); dấu hiệu mệt mỏi/căng thẳng trên thần thái người chăm sóc (đại diện cho oán giận/tủi thân/cảm giác bị kẹt — các trạng thái nội tâm không thể hiển thị trực tiếp)
- Visualizable Type: Concrete (phần hành động chăm sóc) — 4 hành động cụ thể có thể quan sát trực tiếp; các trạng thái nội tâm (mệt mỏi/oán giận/tủi thân/xấu hổ) chỉ có dấu hiệu gián tiếp qua thần thái
- Visualization Strategy: mô tả trực tiếp evidence cho 4 hành động chăm sóc; mô tả dấu hiệu quan sát được (thần thái căng thẳng/kiệt sức) cho các trạng thái nội tâm đi kèm
- Required Continuity: None (nhân vật mới, không liên kết beat khác).
- Forbidden Hallucination: không đặc tả bệnh cụ thể của mẹ già; không thêm chi tiết thời gian biểu ngoài 4 hành động đã nêu
- Visual Importance: High

**OBL_033** (beat_id: BEAT_033)
- Required Subject: người chăm sóc (tiếp nối BEAT_032), lòng hiếu có trí tuệ
- Required Action: No explicit visual action — lời trấn an trực tiếp, hướng tới khán giả.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — đây là lời trấn an bằng ngôn ngữ, không có hành vi thị giác mới
- Visualizable Type: Non-Visual — lời trấn an trực tiếp tới người nghe, không có evidence hình ảnh riêng ngoài những gì đã có ở BEAT_032
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context (evidence hình ảnh, nếu có, tiếp tục dùng chủ thể của BEAT_032).
- Required Continuity: character continuity — có thể là cùng người chăm sóc ở BEAT_032 nếu bước sau muốn nối cảnh, nhưng bản thân obligation này không yêu cầu evidence hình ảnh riêng
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_034** (beat_id: BEAT_034)
- Required Subject: người nghe (chủ thể trải nghiệm), cha, mẹ
- Required Action: bị bỏ mặc; bị tổn thương bởi lời nói
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: dấu hiệu của một tuổi thơ khó khăn — thần thái phòng thủ/căng thẳng khi nghe từ "cha mẹ"; 04A không cung cấp hành vi cụ thể nào để hiển thị "bạo lực/lạnh lùng/lời nói tổn thương/bị bỏ mặc" một cách trực tiếp
- Visualizable Type: Abstract — có chủ thể ("người nghe") nhưng nội dung là trải nghiệm nội tâm/quá khứ không có hành vi cụ thể nào được 04A xác nhận
- Visualization Strategy: mô tả dấu hiệu quan sát được — thần thái căng thẳng/né tránh của một người khi nghe nhắc đến "cha mẹ", như dấu hiệu gián tiếp cho tổn thương quá khứ
- Required Continuity: None.
- Forbidden Hallucination: không đặc tả chi tiết cụ thể của "bạo lực" (loại hình, mức độ không được nêu trong 04A); không gán câu thoại "cha mẹ mà, bỏ qua đi" cho nhân vật cha/mẹ trong câu chuyện — đây là lời của người ngoài
- Visual Importance: Medium

**OBL_035** (beat_id: BEAT_035)
- Required Subject: đạo hiếu, nỗi đau
- Required Action: No explicit visual action — luận đề cảnh báo.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_036** (beat_id: BEAT_036)
- Required Subject: hiếu đạo, khoảng cách, ranh giới
- Required Action: giữ khoảng cách; đặt ranh giới
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hành vi giữ khoảng cách (thể chất hoặc quan hệ) — 04A không cung cấp chủ thể cụ thể, chỉ có hành động khái quát
- Visualizable Type: Abstract — có hành động được nêu tên (giữ khoảng cách/đặt ranh giới) nhưng không có chủ thể cụ thể nào được 04A xác định
- Visualization Strategy: mô tả dấu hiệu quan sát được — một khoảng cách vật lý/tư thế giữa hai người chung chung, như dấu hiệu gián tiếp cho khái niệm ranh giới, không gán cho nhân vật cụ thể nào đã xuất hiện
- Required Continuity: None.
- Forbidden Hallucination: không đặc tả nhân vật cụ thể hay lý do xung đột cụ thể — 04A không cung cấp chi tiết này
- Visual Importance: Medium

**OBL_037** (beat_id: BEAT_037)
- Required Subject: lòng biết ơn
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_038** (beat_id: BEAT_038)
- Required Subject: biết ơn, tôn trọng, chăm sóc, tha thứ
- Required Action: No explicit visual action — 4 định nghĩa phủ định song song.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

---

## ACT IV — BEAT_039–BEAT_048

**OBL_039** (beat_id: BEAT_039)
- Required Subject: bài học hiếu đạo, Kinh Địa Tạng
- Required Action: No explicit visual action — ẩn dụ định hướng ("cây roi" vs "ngọn đèn").
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hình ảnh ẩn dụ do chính narration đặt tên: "cây roi" (bị phủ định) và "ngọn đèn" (được khẳng định)
- Visualizable Type: Symbolic — narration tự đặt tên hai hình ảnh ẩn dụ cụ thể (cây roi, ngọn đèn) để đối lập
- Visualization Strategy: sử dụng đúng hai hình ảnh ẩn dụ đã được narration đặt tên — ngọn đèn (khẳng định) đối lập cây roi (phủ định); không mở rộng thêm ẩn dụ mới ngoài hai hình ảnh này
- Required Continuity: None chính thức. **[Sửa 2026-07-15]** Đã rà soát lại toàn văn `04A_SEMANTIC_BEATS.md` bằng grep — từ "đèn" chỉ xuất hiện ở đúng 3 vị trí: BEAT_039 (chính beat này — ẩn dụ "cây roi" vs "ngọn đèn"), BEAT_117 (ẩn dụ "nghe như một ngọn đèn nhỏ" — chỉ dẫn cách tiếp nhận thông điệp, xem OBL_117), và BEAT_121 (hành động cụ thể "thắp một ngọn đèn" trong nghi thức khép lại). Beat trước đó dẫn "BEAT_125" là sai — 04A xác nhận BEAT_125 liệt kê 4 hình ảnh khả dĩ (gương mặt/chiếc ghế/bàn tay/câu chưa kịp nói), không có "đèn"; "BEAT_157" không tồn tại (episode chỉ có BEAT_001–BEAT_128) — cả hai đã được sửa. Ba lần dùng "đèn" (039/117/121) là ba lần **dùng độc lập cùng một từ/hình ảnh ẩn dụ**, không phải cùng một object vật lý tái xuất — 04A không xác nhận đây là cùng một ngọn đèn cụ thể, nên **không được gán object continuity** giữa chúng ở Phase C; chỉ có thể ghi nhận như cộng hưởng chủ đề (thematic echo), không phải continuity thread chính thức theo 4 loại (character/object/location/timeline).
- Forbidden Hallucination: không dựng cảnh đánh roi theo nghĩa đen — đây là ẩn dụ bị phủ định, không phải hành động cần khẳng định; không thêm chi tiết đèn (loại đèn, ánh sáng màu gì) ngoài việc nó là "ngọn đèn"
- Visual Importance: High — hai ẩn dụ này định hình tông cảm xúc cho toàn bộ cách tiếp cận bài học hiếu đạo trong episode

**OBL_040** (beat_id: BEAT_040)
- Required Subject: bác sĩ, khoa hồi sức, người con (nắm tay cha), người cha (nắm tay), người mẹ (thở yếu), người cha nghiêm khắc, người không kịp đến
- Required Action: nắm tay cha và khóc; hỏi con đã ăn gì; nói lời xin lỗi; không kịp đến
- Required Setting: khoa hồi sức (bệnh viện) — narration nêu tên địa điểm cụ thể.
- Required Visual Evidence: đúng 4 cảnh chia tay: (1) người con nắm tay cha khóc; (2) người mẹ thở yếu hỏi con ăn gì; (3) người cha nghiêm khắc nói lời xin lỗi nhỏ ở phút cuối; (4) một người không kịp đến (biểu hiện qua sự vắng mặt/khoảng trống, khó hiển thị dương tính)
- Visualizable Type: Concrete (3 cảnh đầu) pha Non-Visual (cảnh thứ 4 — "không kịp đến" là một sự vắng mặt, không thể hiển thị dương tính bằng một khoảnh khắc, chỉ có thể ngụ ý qua một ghế/giường trống hoặc một người đến muộn nhìn thấy tình huống đã kết thúc)
- Visualization Strategy: mô tả trực tiếp evidence cho 3 cảnh đầu; cho cảnh thứ 4 ("không kịp đến"), ghi nhận: No direct visual representation cho riêng khoảnh khắc "không kịp" — chỉ có thể ngụ ý qua kết quả (một khoảng trống), không phải hành động "không đến" tự nó
- Required Continuity: location continuity — khoa hồi sức là bối cảnh chung cho cả 4 cảnh trong beat này
- Forbidden Hallucination: không đặt tên/danh tính cụ thể cho bác sĩ hay bệnh nhân; không thêm cảnh chia tay ngoài 4 cảnh đã liệt kê; không đặc tả bệnh lý cụ thể
- Visual Importance: High

**OBL_041** (beat_id: BEAT_041)
- Required Subject: đời sống, tình thương, lý do trì hoãn
- Required Action: trì hoãn
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — đây là luận đề dẫn nhập cho danh sách cụ thể ở BEAT_042
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context (minh hoạ cụ thể ở BEAT_042).
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_042** (beat_id: BEAT_042)
- Required Subject: chiếc ghế (callback motif); "ta" — chủ thể chung cho 6 lý do bận
- Required Action: bận kiếm tiền/lo con/trả nợ/chứng minh đúng/giận/chờ người kia mở lời; ghế "cũ đi" (biến đổi vật lý theo thời gian)
- Required Setting: Bối cảnh trong nhà, kế thừa từ BEAT_001/002/005 cho phần liên quan tới ghế.
- Required Visual Evidence: dấu hiệu cũ đi của chiếc ghế theo thời gian (bụi, màu sắc phai, hao mòn) — đây là evidence Concrete duy nhất chắc chắn của beat; 6 lý do bận là trừu tượng, không có hành vi cụ thể riêng biệt nào được 04A gán cho từng lý do
- Visualizable Type: Concrete (cho phần "ghế cũ đi") — chiếc ghế là vật thể cụ thể có thể hiển thị trạng thái hao mòn theo thời gian; 6 lý do bận bản thân là Abstract/Non-Visual nhưng không cần evidence riêng vì chúng đã hội tụ vào một hệ quả thị giác chung (ghế cũ đi)
- Visualization Strategy: mô tả trực tiếp evidence — tập trung vào chiếc ghế với dấu hiệu thời gian trôi qua (không cần hiển thị riêng lẻ 6 lý do bận, vì bản thân các lý do đó không có evidence hình ảnh và hệ quả chung của chúng đã được cô đọng vào hình ảnh chiếc ghế)
- Required Continuity: object continuity — cùng chiếc ghế với BEAT_001/002/005, nay ở trạng thái "cũ đi" theo thời gian — đây là bước phát triển thứ ba của motif ghế
- Forbidden Hallucination: không hiển thị riêng biệt 6 lý do bận bằng 6 cảnh khác nhau — 04A không cung cấp evidence hình ảnh cho từng lý do; không thêm nhân vật cụ thể "ta" có danh tính
- Visual Importance: Critical — bước phát triển quan trọng của motif ghế xuyên suốt episode

**OBL_043** (beat_id: BEAT_043)
- Required Subject: Đức Phật, thân mẫu (kế thừa từ BEAT_010/022), đạo hiếu
- Required Action: (kế thừa hành động thuyết pháp từ BEAT_010/022, không có hành động mới)
- Required Setting: Cung Trời Đao Lợi, kế thừa từ các beat trước liên quan Đức Phật.
- Required Visual Evidence: None trực tiếp mới — nội dung là quán chiếu/diễn giải trừu tượng ("đạo hiếu = tỉnh thức trước ân nghĩa", phủ định "sợ hãi")
- Visualizable Type: Non-Visual — mặc dù có nhắc lại chủ thể Đức Phật/thân mẫu, nội dung cốt lõi của beat này là một luận đề trừu tượng không thêm evidence hình ảnh mới nào ngoài BEAT_010
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context (evidence hình ảnh, nếu cần, dùng lại của BEAT_010).
- Required Continuity: character continuity — Đức Phật/thân mẫu, cùng với BEAT_010/022 nếu cần
- Forbidden Hallucination: không thêm hành động/biểu cảm mới cho Đức Phật ngoài BEAT_010
- Visual Importance: Low

**OBL_044** (beat_id: BEAT_044)
- Required Subject: "ta" — chủ thể chung
- Required Action: được sinh ra
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — luận đề dẫn nhập cho danh sách cụ thể ở BEAT_045
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_045** (beat_id: BEAT_045)
- Required Subject: mẹ, cha, người trồng lúa, người may áo, thầy cô, hàng xóm, người xa lạ, bác sĩ, người quét đường
- Required Action: các hành vi lao động ngụ ý theo nghề (trồng lúa, may áo, dạy học, làm bác sĩ, quét đường) — không có hành động cụ thể tức thời nào được narration mô tả cho từng người, chỉ có vai trò/nghề nghiệp được nêu tên
- Required Setting: Setting intentionally unspecified — 9 nhóm người này không gắn với một bối cảnh chung cụ thể nào.
- Required Visual Evidence: sự hiện diện của 9 nhóm người/vai trò đã liệt kê, mỗi người gắn với công việc/vai trò tương ứng
- Visualizable Type: Concrete — có 9 chủ thể cụ thể (dù chung chung, không tên) với vai trò/nghề nghiệp được nêu rõ, đủ để hiển thị trực tiếp
- Visualization Strategy: mô tả trực tiếp evidence — 9 vai trò được liệt kê, mỗi vai trò gắn với một hoạt động nghề nghiệp điển hình tương ứng (không cần đồng thời trong một khung hình)
- Required Continuity: None (9 nhóm người độc lập, không liên kết continuity với các beat khác — trừ mẹ/cha có thể liên kết khái niệm với mẹ/cha ở BEAT_002, nhưng 04A không xác nhận đây là CÙNG một mẹ/cha cụ thể, nên không ép buộc character continuity)
- Forbidden Hallucination: không thêm nghề nghiệp/nhóm người nào ngoài 9 nhóm đã liệt kê; không đặc tả danh tính cụ thể cho từng nhóm
- Visual Importance: High — danh sách cụ thể hoá luận điểm "ta được sinh ra từ vô số điều kiện", nền tảng cho sự mở rộng lòng biết ơn ở các beat sau

**OBL_046** (beat_id: BEAT_046)
- Required Subject: tinh thần Đại thừa
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_047** (beat_id: BEAT_047)
- Required Subject: lòng hiếu, mẹ, tâm biết ơn, chiếc ghế (callback motif)
- Required Action: mở rộng (tâm biết ơn) — hành động trừu tượng, không có biểu hiện vật lý cụ thể
- Required Setting: Setting intentionally unspecified cho phần khái niệm "mở rộng tâm biết ơn"; chiếc ghế kế thừa bối cảnh trong nhà đã thiết lập.
- Required Visual Evidence: chiếc ghế (callback), như một phương tiện thị giác duy nhất cụ thể trong beat này để neo khái niệm trừu tượng "từng có ghế để trở về hoặc từng mất ghế"
- Visualizable Type: Concrete (cho phần chiếc ghế) — chủ đề trừu tượng "mở rộng lòng biết ơn" không có evidence riêng, nhưng narration tự neo nó vào hình ảnh chiếc ghế đã thiết lập
- Visualization Strategy: mô tả trực tiếp evidence — dùng lại chiếc ghế đã thiết lập (không cần dựng cảnh mới); phần khái niệm mở rộng lòng biết ơn không có evidence hình ảnh riêng, được truyền tải qua chính sự lặp lại của hình ảnh ghế
- Required Continuity: object continuity — cùng chiếc ghế với BEAT_001/002/005/042 — đây là lần callback thứ tư của motif
- Forbidden Hallucination: không dựng cảnh mới minh hoạ "mọi chúng sinh từng được thương" bằng nhân vật/đám đông cụ thể — 04A không cung cấp evidence cho việc này ngoài hình ảnh chiếc ghế
- Visual Importance: Medium

**OBL_048** (beat_id: BEAT_048)
- Required Subject: Địa Tạng Bồ Tát
- Required Action: xuất hiện (trong mạch cảm xúc — mang tính ẩn dụ tường thuật, không phải xuất hiện vật lý, theo đúng ghi chú của 04A)
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — 04A xác nhận rõ "không mô tả hình tướng Địa Tạng Bồ Tát ở beat này"
- Visualizable Type: Non-Visual — đây là một câu chuyển ý ẩn dụ ("xuất hiện trong mạch cảm xúc"), không phải sự xuất hiện vật lý cần hiển thị
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: character continuity — Địa Tạng Bồ Tát được nhắc tên lần đầu ở đây trong nhóm beat này, sẽ cần hình tướng cụ thể ở các beat sau nếu có (không ép buộc ở đây)
- Forbidden Hallucination: không mô tả hình tướng/y phục cụ thể của Địa Tạng Bồ Tát ở beat này — 04A minh thị cấm điều này
- Visual Importance: Low

---

## ACT V — BEAT_049–BEAT_058

**OBL_049** (beat_id: BEAT_049)
- Required Subject: đại nguyện, chúng sinh, lòng từ bi, mẹ, cha
- Required Action: No explicit visual action — diễn giải quá trình mở rộng từ bi.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — chuỗi mở rộng "thương mẹ → nhớ cha → đau vì người thân khổ → nhìn mọi chúng sinh như người thân" là một quá trình nội tâm, không có hành vi cụ thể
- Visualizable Type: Abstract — có nêu tên các chủ thể liên quan (mẹ, cha) làm điểm neo, dù quá trình mở rộng bản thân là trừu tượng
- Visualization Strategy: mô tả dấu hiệu quan sát được — thần thái trắc ẩn hướng về gia đình như điểm khởi đầu, không mở rộng thành hình ảnh "mọi chúng sinh" cụ thể vì 04A không cung cấp evidence cho điều này
- Required Continuity: None.
- Forbidden Hallucination: không mô tả chi tiết nội dung "đại nguyện" ngoài "không bỏ rơi chúng sinh nơi tối tăm nhất" đã có ở 04A; không dựng cảnh đám đông "mọi chúng sinh"
- Visual Importance: Medium

**OBL_050** (beat_id: BEAT_050)
- Required Subject: lòng hiếu, từ bi, sự ích kỷ
- Required Action: thanh lọc
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — "thanh lọc" ở đây là một quá trình nội tâm trừu tượng
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context (minh hoạ cụ thể ở BEAT_051).
- Required Continuity: None.
- Forbidden Hallucination: không dựng cảnh "thanh lọc" bằng hình ảnh nghi lễ/nước/lửa tượng trưng — không có căn cứ trong 04A
- Visual Importance: Low

**OBL_051** (beat_id: BEAT_051)
- Required Subject: cha mẹ mình, cha mẹ người khác, gia đình mình, gia đình khác, tổ tiên, người làm việc cho mình
- Required Action: khinh thường; chà đạp; bất công
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None cụ thể cho từng hành vi — đây là 3 cảnh báo trừu tượng về thái độ, không có hành vi vật lý cụ thể nào được narration mô tả (không có cử chỉ/tương tác cụ thể)
- Visualizable Type: Abstract — có nêu tên các cặp chủ thể liên quan nhưng không có hành vi cụ thể để hiển thị trực tiếp
- Visualization Strategy: mô tả dấu hiệu quan sát được — nếu cần, một cử chỉ coi thường/phân biệt đối xử chung chung giữa hai nhóm người, không gán cho cá nhân cụ thể
- Required Continuity: None.
- Forbidden Hallucination: không dựng cảnh cụ thể cho "chà đạp gia đình khác" hay "bất công với người làm việc" — quá cụ thể so với những gì 04A xác nhận
- Visual Importance: Low

**OBL_052** (beat_id: BEAT_052)
- Required Subject: hiếu đạo, người đã khuất
- Required Action: No explicit visual action — luận đề định hướng.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_053** (beat_id: BEAT_053)
- Required Subject: nhân đau khổ, cha mẹ
- Required Action: No explicit visual action — câu hỏi tu từ hướng tới khán giả.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_054** (beat_id: BEAT_054)
- Required Subject: con mình, những câu tổn thương
- Required Action: No explicit visual action — câu hỏi tu từ hướng tới khán giả.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_055** (beat_id: BEAT_055)
- Required Subject: áp lực, bạo lực, lo lắng, kiểm soát, tình thương, điều kiện, con
- Required Action: No explicit visual action — câu hỏi tu từ hướng tới khán giả.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_056** (beat_id: BEAT_056)
- Required Subject: người cha, con (đứa trẻ hiện tại của ông)
- Required Action: la con; đứa trẻ cúi mặt xuống; ông nhận ra/nhìn thấy chính mình
- Required Setting: Setting intentionally unspecified (04A xác nhận không có mô tả không gian cụ thể).
- Required Visual Evidence: hành vi la con (giọng điệu/tư thế); phản ứng cúi mặt của đứa trẻ; biểu cảm nhận ra (realization) trên gương mặt người cha
- Visualizable Type: Concrete
- Visualization Strategy: mô tả trực tiếp evidence — người cha đang la con, đứa trẻ cúi mặt, và một khoảnh khắc biểu cảm chuyển sang nhận ra trên gương mặt người cha; phần hồi tưởng "nhìn thấy chính mình nhiều năm trước" và "lời tự hứa thời thơ ấu" là nội dung nội tâm không hiển thị trực tiếp được, chỉ ngụ ý qua biểu cảm
- Required Continuity: character continuity — người cha và con được giới thiệu lần đầu ở đây, sẽ tiếp tục xuyên suốt BEAT_057–061 (character continuity thread độc lập, KHÔNG liên kết với gia đình ở các beat khác như BEAT_002/026/029/032)
- Forbidden Hallucination: không đặt tên nhân vật; không đặc tả bối cảnh không gian cụ thể (nhà, phòng...); không mô tả hành vi bạo lực thể chất (chỉ có "la", không có mô tả đánh đập); không hiển thị "đứa trẻ trong quá khứ" như một nhân vật riêng biệt xuất hiện đồng thời — đây là hồi tưởng nội tâm của người cha, không phải hai nhân vật cùng khung hình
- Visual Importance: Critical — mở đầu continuity thread quan trọng của episode

**OBL_057** (beat_id: BEAT_057)
- Required Subject: vòng lặp (khái niệm, không phải vật thể)
- Required Action: quay (tiếp diễn) — hành động trừu tượng
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — "vòng lặp vẫn quay" là một nhận định tường thuật khái quát hoá, không mô tả một hành vi cụ thể mới nào của người cha
- Visualizable Type: Non-Visual — đây là một câu bình luận tường thuật tóm tắt tình trạng tiếp diễn, không có hành vi mới để hiển thị
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context (tiếp nối trực tiếp từ BEAT_056, dẫn tới BEAT_058).
- Required Continuity: character continuity — vẫn là người cha của BEAT_056, dù không có evidence hình ảnh riêng cho beat này
- Forbidden Hallucination: không dựng cảnh minh hoạ mới cho "vòng lặp quay" (ví dụ: hình ảnh vòng tròn biểu tượng) — không có căn cứ trong 04A
- Visual Importance: Low

**OBL_058** (beat_id: BEAT_058)
- Required Subject: người cha (ông) — cùng nhân vật với BEAT_056/057
- Required Action: dừng lại
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: khoảnh khắc "dừng lại" — một sự thay đổi trạng thái/tư thế/biểu cảm đánh dấu bước ngoặt, đối lập với hành vi la con ở BEAT_056
- Visualizable Type: Concrete — có chủ thể xác định (người cha, cùng nhân vật BEAT_056) và một khoảnh khắc chuyển đổi có thể hiển thị qua tư thế/biểu cảm, dù nguyên nhân bên trong không thể hiển thị
- Visualization Strategy: mô tả trực tiếp evidence — một khoảnh khắc người cha dừng lại (tư thế/biểu cảm thay đổi), không cần giải thích nguyên nhân cụ thể vì 04A xác nhận narration không nêu lý do cụ thể
- Required Continuity: character continuity — cùng người cha với BEAT_056/057
- Forbidden Hallucination: không mô tả nguyên nhân cụ thể khiến ông dừng lại (04A xác nhận không có lý do cụ thể trong narration)
- Visual Importance: Critical — đây là climax của continuity thread người cha, bản lề của toàn bộ câu chuyện minh hoạ

**OBL_059** (beat_id: BEAT_059)
- Required Subject: người cha (ông), con (của ông) — cùng nhân vật với BEAT_056–058
- Required Action: quỳ xuống; nói lời xin lỗi (nguyên văn: "ba xin lỗi, câu vừa rồi làm con đau. Ba sẽ học cách nói khác.")
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: tư thế quỳ xuống của người cha trước mặt con; tương tác trực tiếp giữa hai người (đối diện nhau); hành vi nói (miệng mở, hướng về con) — nội dung lời nói cụ thể (câu thoại) là ngôn ngữ, không phải evidence hình ảnh, nhưng hành vi "đang nói với con, ở tư thế quỳ" là evidence hình ảnh hợp lệ
- Visualizable Type: Concrete
- Visualization Strategy: mô tả trực tiếp evidence — người cha quỳ xuống trước con, đối diện, trong tư thế đang nói; 3 điều "không thể" (thay đổi tuổi thơ/làm quá khứ dịu hơn/làm cha đã mất xin lỗi) là nội dung nội tâm không hiển thị trực tiếp
- Required Continuity: character continuity — cùng người cha và con với BEAT_056–058; đây là điểm resolution của continuity thread này
- Forbidden Hallucination: không đổi/diễn giải lại câu thoại; không thêm phản ứng của đứa con sau lời xin lỗi (04A xác nhận narration không mô tả phản ứng này — không được tự bịa phản ứng của con)
- Visual Importance: Critical — resolution của continuity thread người cha

**OBL_060** (beat_id: BEAT_060)
- Required Subject: tầng ứng dụng hiện đại, báo hiếu
- Required Action: No explicit visual action — khái quát hoá câu chuyện thành nguyên lý.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp mới — đây là bình luận khái quát hoá về ý nghĩa của BEAT_059
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context (evidence hình ảnh, nếu cần, dùng lại của BEAT_059).
- Required Continuity: character continuity — có thể tiếp tục hình ảnh người cha/con của BEAT_059 nếu cần bối cảnh, nhưng không bắt buộc evidence riêng
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

---

## ACT VI (tiếp) — BEAT_061–BEAT_069

**OBL_061** (beat_id: BEAT_061)
- Required Subject: người cha (ông), cha của ông, vết thương, thế hệ sau
- Required Action: quyết định không truyền tiếp vết thương — hành động nội tâm/quyết định, không có biểu hiện thị giác riêng
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp mới — đây là diễn giải ý nghĩa, không thêm hành vi mới ngoài BEAT_059
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: character continuity — vẫn là người cha của BEAT_056–059
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_062** (beat_id: BEAT_062)
- Required Subject: nén hương, bàn thờ, tổ tiên; "một người" — chủ thể MỚI, chung chung (04A xác nhận narration chuyển từ câu chuyện cụ thể của người cha sang phát biểu tổng quát "một người" — không được coi là cùng nhân vật với BEAT_056–059)
- Required Action: dừng bàn tay nóng giận; dừng lời mắng nhục; dừng im lặng trừng phạt; dừng cơn say; dừng yêu thương có điều kiện; dừng vòng lặp ba đời
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hình ảnh ẩn dụ "nén hương" và "bàn thờ" do narration đặt tên (dùng để phủ định — nén hương chân thành nhất KHÔNG nằm trên bàn thờ); 6 hành động "dừng lại" là trừu tượng, không có chủ thể cụ thể
- Visualizable Type: Symbolic — narration tự đặt tên hình ảnh "nén hương"/"bàn thờ" làm ẩn dụ (dù là ẩn dụ bị phủ định về vị trí — ý nghĩa thật nằm ở hành động dừng lại, không nằm trên bàn thờ)
- Visualization Strategy: sử dụng hình ảnh ẩn dụ đã được narration đặt tên (bàn thờ/nén hương) nhưng đúng với vai trò PHỦ ĐỊNH của nó (nén hương chân thành không nằm ở đó); 6 hành động "dừng lại" không có evidence hình ảnh cụ thể, không ép buộc minh hoạ riêng cho từng hành động
- Required Continuity: **Không liên kết character continuity với người cha ở BEAT_056–059** — đây là chủ thể mới, chung chung ("một người"), theo đúng ghi chú của 04A
- Forbidden Hallucination: không thêm hành động "dừng" nào ngoài 6 hành động đã liệt kê; **không mặc định đây là cùng người cha của BEAT_056–059** — đây là lỗi hallucination continuity cụ thể cần tránh
- Visual Importance: Medium

**OBL_063** (beat_id: BEAT_063)
- Required Subject: câu kinh, Đức Phật, nhân quả, sự chuyển hoá
- Required Action: No explicit visual action — tuyên bố ranh giới nguồn (disclaimer).
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None — đây là một disclaimer về nguồn gốc nội dung, không phải nội dung cần hình ảnh hoá
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context. **Ràng buộc quan trọng kế thừa từ 04A: disclaimer này áp dụng ngược lại cho toàn bộ OBL_056–062 — các obligation đó không được trình bày như trích dẫn kinh điển hay lời Đức Phật.**
- Required Continuity: None.
- Forbidden Hallucination: không thể hiện Đức Phật đang nói câu chuyện người cha (BEAT_056-062) như một sự kiện trong kinh điển
- Visual Importance: Low

**OBL_064** (beat_id: BEAT_064)
- Required Subject: nhân quả, bữa cơm tối nay, lời nói, đứa trẻ, thói quen, nỗi sợ
- Required Action: gieo xuống (lời nói); nhận lấy (đứa trẻ); hình thành (thói quen); đi vào thân thể (nỗi sợ); trở thành cách yêu/giận/làm cha mẹ (20 năm sau)
- Required Setting: bữa cơm tối nay — narration nêu bối cảnh cụ thể cho điểm khởi đầu chuỗi nhân quả.
- Required Visual Evidence: một khoảnh khắc tại bữa cơm (lời nói được nói ra, một đứa trẻ ở đó) làm điểm khởi đầu Concrete; 4 bước còn lại của chuỗi (hình thành thói quen, nỗi sợ nhập thân, kết quả 20 năm sau) là quá trình trừu tượng trải dài thời gian, không thể hiển thị trong một khung hình
- Visualizable Type: Abstract — có điểm khởi đầu cụ thể (bữa cơm, một lời nói, một đứa trẻ) nhưng toàn bộ chuỗi nhân quả kéo dài 20 năm không thể hiển thị trực tiếp bằng một hoặc vài khoảnh khắc
- Visualization Strategy: mô tả dấu hiệu quan sát được — chỉ khoảnh khắc khởi đầu (bữa cơm, lời nói, đứa trẻ tiếp nhận) được hiển thị trực tiếp như đại diện cho toàn chuỗi; phần "20 năm sau" không hiển thị được bằng hình ảnh, chỉ tồn tại như ý nghĩa được hiểu ngầm
- Required Continuity: timeline continuity — bản thân beat này chứa một khoảng thời gian nội tại (bữa cơm hôm nay → 20 năm sau), cần được bước sau xử lý như một đơn vị không tách rời nếu muốn giữ đúng ý nghĩa chuỗi nhân quả
- Forbidden Hallucination: không tách rời các bước thành sự kiện độc lập không liên quan; không gán chuỗi này cho một nhân vật cụ thể có tên; không hiển thị "20 năm sau" như một cảnh riêng có nhân vật trưởng thành cụ thể — narration không mô tả nhân vật đó
- Visual Importance: High

**OBL_065** (beat_id: BEAT_065)
- Required Subject: hiếu đạo, nhắn tin, điện thoại, người già, ranh giới, con, lời xin lỗi
- Required Action: nhắn tin; nghe điện thoại; chăm sóc người già; đặt ranh giới; nuôi dạy con; nói lời xin lỗi
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: đúng 6 hành vi hiện đại được liệt kê — mỗi hành vi có thể hiển thị bằng một cử chỉ/tương tác cụ thể (nhắn tin trên điện thoại, nghe điện thoại, một hành động chăm sóc người già, một cử chỉ đặt ranh giới, một tương tác nuôi dạy con, một cử chỉ xin lỗi)
- Visualizable Type: Concrete — 6 hành vi đều có thể hiển thị trực tiếp bằng cử chỉ/tương tác đơn giản
- Visualization Strategy: mô tả trực tiếp evidence — 6 hành vi độc lập, mỗi hành vi là một cử chỉ/tương tác cụ thể tương ứng đúng tên gọi của nó, không cần diễn ra đồng thời
- Required Continuity: None (6 hành vi độc lập, không có chủ thể chung được 04A xác định).
- Forbidden Hallucination: không thêm hành vi nào ngoài 6 hành vi đã liệt kê
- Visual Importance: Medium

**OBL_066** (beat_id: BEAT_066)
- Required Subject: người mất mẹ, ân hận, mẹ, người già khác, con
- Required Action: mang ân hận; chăm sóc người già khác; nói với con những lời chưa kịp nói
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: dấu hiệu ân hận (thần thái trầm lặng) như điểm khởi đầu; hành vi chăm sóc người già khác; hành vi nói với con — 3 khả năng chuyển hoá được liệt kê, không bắt buộc đồng thời
- Visualizable Type: Abstract (cho phần "ân hận") pha Concrete (cho 2 hành vi chuyển hoá cụ thể: chăm sóc người già khác, nói với con)
- Visualization Strategy: mô tả dấu hiệu quan sát được cho trạng thái ân hận (thần thái); mô tả trực tiếp evidence cho 2 hành vi chuyển hoá cụ thể nếu được chọn thể hiện
- Required Continuity: None (chủ thể "người mất mẹ" không xác nhận là cùng nhân vật với các beat khác).
- Forbidden Hallucination: None thêm ngoài phạm vi đã liệt kê.
- Visual Importance: Medium

**OBL_067** (beat_id: BEAT_067)
- Required Subject: người đã mất, sự tự trách
- Required Action: No explicit visual action — luận đề khẳng định.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_068** (beat_id: BEAT_068)
- Required Subject: món quà, ký ức, đời sống
- Required Action: học cách sáng hơn
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — 04A minh thị "món quà" là ẩn dụ trừu tượng, không phải vật thể vật lý
- Visualizable Type: Non-Visual — mặc dù có từ "món quà", 04A xác nhận đây không phải một vật thể vật lý cụ thể, không có evidence hình ảnh nào được cung cấp
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không đặc tả "món quà" bằng vật thể cụ thể (hộp quà, gói quà...) — 04A minh thị cấm điều này
- Visual Importance: Low

**OBL_069** (beat_id: BEAT_069)
- Required Subject: nghi lễ
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

---

## ACT VIII — BEAT_070–BEAT_075

**OBL_070** (beat_id: BEAT_070)
- Required Subject: tụng kinh, làm phước, hồi hướng, tưởng niệm, người mất
- Required Action: tụng kinh; làm phước; hồi hướng; tưởng niệm
- Required Setting: Setting intentionally unspecified — 04A xác nhận không có mô tả không gian nghi lễ cụ thể ở beat này.
- Required Visual Evidence: hành vi thực hiện 4 thực hành nghi lễ được nêu tên (tụng kinh/làm phước/hồi hướng/tưởng niệm)
- Visualizable Type: Concrete — 4 thực hành có tên gọi cụ thể, có thể hiển thị bằng hành vi tương ứng (dù không có bối cảnh không gian cụ thể)
- Visualization Strategy: mô tả trực tiếp evidence — hành vi tụng kinh/làm phước/hồi hướng/tưởng niệm, không đặc tả không gian (chùa, nhà...) vì 04A không xác nhận
- Required Continuity: None.
- Forbidden Hallucination: không mô tả nghi lễ bằng hình ảnh cụ thể về không gian (chùa, tượng Phật...) — 04A xác nhận chưa có mô tả hình ảnh trong narration ở đây; không tự thêm địa điểm "chùa" nếu narration không nêu
- Visual Importance: Medium

**OBL_071** (beat_id: BEAT_071)
- Required Subject: nghi lễ, cảnh giới, nỗi thương, sợ hãi, tiền, thời gian, nghi thức
- Required Action: No explicit visual action — 4 cảnh báo phủ định song song.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — đây là 4 cảnh báo về CÁCH KHÔNG NÊN làm, không phải nội dung cần khẳng định bằng hình ảnh
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không dựng cảnh minh hoạ "bán sợ hãi" hay "nghi lễ như cái máy" — đây là các hành vi bị phê phán, không phải nội dung cần hình ảnh hoá dương tính
- Visual Importance: Low

**OBL_072** (beat_id: BEAT_072)
- Required Subject: lòng thành, sự phô trương
- Required Action: No explicit visual action — luận đề khẳng định.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_073** (beat_id: BEAT_073)
- Required Subject: người nghèo, nén hương, người chăm mẹ còn sống, người tổn thương với cha, con
- Required Action: thắp một nén hương; sống bớt hận thù; chăm sóc mẹ còn sống (bữa cơm ấm/đưa đi khám/trò chuyện); không biến vết thương thành bạo lực với con
- Required Setting: Setting intentionally unspecified cho từng ví dụ cụ thể (không gian nhà ngụ ý nhưng không đặc tả).
- Required Visual Evidence: đúng 3 ví dụ theo đúng nội dung: (1) người nghèo thắp một nén hương; (2) người chăm mẹ còn sống qua bữa cơm/đưa khám/trò chuyện; (3) người kiềm chế không biến vết thương thành bạo lực với con (hành động "không làm" — khó hiển thị dương tính, chỉ có thể ngụ ý qua một khoảnh khắc kiềm chế/bình tĩnh)
- Visualizable Type: Concrete (ví dụ 1 và 2) pha Abstract (ví dụ 3 — hành động kiềm chế là trạng thái nội tâm, chỉ có dấu hiệu gián tiếp)
- Visualization Strategy: mô tả trực tiếp evidence cho ví dụ 1 và 2; mô tả dấu hiệu quan sát được (thần thái bình tĩnh/kiềm chế) cho ví dụ 3
- Required Continuity: None (3 ví dụ độc lập, không liên kết continuity với các beat khác).
- Forbidden Hallucination: không thêm ví dụ thứ 4; không đặc tả danh tính cụ thể cho 3 người này; không dựng bàn thờ lớn cho ví dụ người nghèo — narration minh thị đối lập "nén hương đơn sơ" với sự phô trương
- Visual Importance: High

**OBL_074** (beat_id: BEAT_074)
- Required Subject: chữ hiếu
- Required Action: No explicit visual action — lời cảnh báo trực tiếp tới khán giả.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_075** (beat_id: BEAT_075)
- Required Subject: hiếu đạo, từ bi, cha mẹ, người đã mất, người chăm sóc, chính mình
- Required Action: No explicit visual action — luận đề tổng hợp.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

---

## ACT IX — BEAT_076–BEAT_086

**OBL_076** (beat_id: BEAT_076)
- Required Subject: Cung Trời Đao Lợi, pháp hội, ký ức về mẹ, đại nguyện, Địa Tạng
- Required Action: No explicit visual action — hình ảnh tổng kết ba tầng.
- Required Setting: Cung Trời Đao Lợi, kế thừa từ BEAT_010/016/017/022.
- Required Visual Evidence: cấu trúc ba tầng "trên cao / trong sâu / rộng hơn" — 04A xác nhận đây là hình ảnh tổng kết, không phải cảnh hành động mới; pháp hội (đã có evidence từ BEAT_010) là phần Concrete duy nhất còn lại; "ký ức về mẹ" và "đại nguyện" là trừu tượng
- Visualizable Type: Abstract — cấu trúc ẩn dụ ba tầng không gian (cao/sâu/rộng) là một cách tổ chức ý niệm, không phải một cảnh vật lý đơn nhất; phần pháp hội có căn cứ Concrete từ BEAT_010
- Visualization Strategy: mô tả dấu hiệu quan sát được — dùng lại hình ảnh pháp hội tại Cung Trời Đao Lợi (từ BEAT_010) làm điểm neo Concrete duy nhất; không dựng thêm hình ảnh cụ thể cho "ký ức về mẹ" hay "đại nguyện" vì đây là tầng ý nghĩa trừu tượng đi kèm
- Required Continuity: location continuity — Cung Trời Đao Lợi, cùng địa điểm với BEAT_010/016/017/022
- Forbidden Hallucination: không dựng cảnh minh hoạ trực tiếp riêng cho "đại nguyện của Địa Tạng" ở beat này — 04A không cung cấp evidence hình ảnh cho nội dung này tại vị trí này
- Visual Importance: Medium

**OBL_077** (beat_id: BEAT_077)
- Required Subject: Kinh Địa Tạng, sợ hãi
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_078** (beat_id: BEAT_078)
- Required Subject: địa ngục, nghiệp báo, hiếu đạo, đại bi, lòng biết ơn, trách nhiệm, ánh sáng
- Required Action: No explicit visual action — câu hỏi tu từ khép lại phần lý giải.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không tự vẽ hình ảnh địa ngục ở beat này — 04A không cung cấp evidence, và các beat trước (BEAT_009) đã minh thị cấm điều này
- Visual Importance: Low

**OBL_079** (beat_id: BEAT_079)
- Required Subject: Địa Tạng Bồ Tát, gia đình
- Required Action: No explicit visual action — định nghĩa lại vai trò Địa Tạng, dẫn nhập cho danh sách thực hành nhỏ.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — 04A xác nhận không mô tả hình tướng Địa Tạng ở beat này
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context (dẫn nhập cho evidence cụ thể ở BEAT_080–085).
- Required Continuity: character continuity — Địa Tạng Bồ Tát, cùng lần nhắc tên như BEAT_048, vẫn chưa có evidence hình ảnh cụ thể nào được cung cấp
- Forbidden Hallucination: không mô tả hình tướng/y phục cụ thể của Địa Tạng Bồ Tát (04A minh thị cấm)
- Visual Importance: Low

**OBL_080** (beat_id: BEAT_080)
- Required Subject: cuộc gọi
- Required Action: gọi điện (không vội)
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hành vi thực hiện một cuộc gọi điện thoại, không vội vàng (tư thế thư thái)
- Visualizable Type: Concrete
- Visualization Strategy: mô tả trực tiếp evidence — một người thực hiện cuộc gọi điện thoại với tư thế/nhịp điệu thư thái
- Required Continuity: None.
- Forbidden Hallucination: không đặc tả người gọi/người nhận cụ thể
- Visual Importance: Medium

**OBL_081** (beat_id: BEAT_081)
- Required Subject: bữa cơm
- Required Action: dùng bữa (không cáu gắt)
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hành vi dùng bữa với thần thái điềm tĩnh (không cáu gắt)
- Visualizable Type: Concrete
- Visualization Strategy: mô tả trực tiếp evidence — một bữa cơm với thần thái điềm tĩnh
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Medium

**OBL_082** (beat_id: BEAT_082)
- Required Subject: lời xin lỗi
- Required Action: xin lỗi (chủ động, không chờ đối phương)
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hành vi chủ động xin lỗi (cử chỉ/tư thế hướng về đối phương)
- Visualizable Type: Concrete
- Visualization Strategy: mô tả trực tiếp evidence — một cử chỉ chủ động xin lỗi
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Medium

**OBL_083** (beat_id: BEAT_083)
- Required Subject: ranh giới
- Required Action: nói ra ranh giới (bằng giọng bình tĩnh)
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hành vi nói với thần thái/tư thế bình tĩnh, không căng thẳng
- Visualizable Type: Concrete
- Visualization Strategy: mô tả trực tiếp evidence — một người đang nói với thần thái bình tĩnh
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Medium

**OBL_084** (beat_id: BEAT_084)
- Required Subject: trị liệu, tu học, sự giúp đỡ, đời con
- Required Action: quyết định đi trị liệu/tu học/tìm giúp đỡ
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hành vi tìm kiếm/tiếp nhận sự giúp đỡ (một trong ba hình thức: trị liệu/tu học/giúp đỡ) — 04A không xác định hình thức nào là ưu tiên
- Visualizable Type: Concrete — có hành động cụ thể (dù là một trong ba lựa chọn không xác định hình thức chính xác)
- Visualization Strategy: mô tả trực tiếp evidence — một hành vi tìm kiếm sự giúp đỡ (không cần xác định cụ thể là trị liệu/tu học/hỗ trợ nào, vì 04A không ưu tiên hình thức nào)
- Required Continuity: None.
- Forbidden Hallucination: không xác định hình thức trị liệu/tu học cụ thể (loại hình, địa điểm) nếu 04A không nêu rõ
- Visual Importance: Medium

**OBL_085** (beat_id: BEAT_085)
- Required Subject: chiếc ghế (callback motif)
- Required Action: nhìn vào chiếc ghế; tự hỏi (hành động nội tâm)
- Required Setting: Bối cảnh trong nhà, kế thừa từ BEAT_001/002/005/042/047.
- Required Visual Evidence: hành vi nhìn vào chiếc ghế (hướng ánh mắt, tư thế); câu hỏi nội tâm không hiển thị trực tiếp được
- Visualizable Type: Concrete (cho phần "nhìn vào ghế") — có chủ thể (một người, chung chung) và hành vi cụ thể (nhìn) gắn với vật thể đã thiết lập (chiếc ghế)
- Visualization Strategy: mô tả trực tiếp evidence — một người nhìn vào chiếc ghế quen thuộc; câu hỏi nội tâm không hiển thị bằng hình ảnh, chỉ ngụ ý qua ánh mắt/thần thái suy tư
- Required Continuity: object continuity — cùng chiếc ghế với BEAT_001/002/005/042/047 — đây là lần callback thứ năm, dùng làm công cụ tự vấn
- Forbidden Hallucination: None thêm ngoài các ràng buộc đã có cho motif ghế.
- Visual Importance: High

**OBL_086** (beat_id: BEAT_086)
- Required Subject: hiếu đạo, cha mẹ, sự mong manh
- Required Action: nhận ra (muộn)
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — luận đề dẫn nhập cho câu chuyện cụ thể ở BEAT_087
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

---

## ACT X — BEAT_087–BEAT_096

**OBL_087** (beat_id: BEAT_087)
- Required Subject: mẹ, cha, bếp, bóng đèn, cánh cửa, chén
- Required Action: mẹ biết bếp còn gì (thời trẻ, hồi tưởng); cha sửa bóng đèn/vá cửa/đi nắng mưa (thời trẻ, hồi tưởng); mẹ hỏi lại một câu nhiều lần (hiện tại, dấu hiệu suy yếu); cha không nghe rõ (hiện tại); bàn tay run khi cầm chén (hiện tại)
- Required Setting: Bối cảnh trong nhà (không gian sinh hoạt gia đình, không có chi tiết cụ thể hơn).
- Required Visual Evidence: hai hình ảnh hồi tưởng về sự "luôn ở đó" của cha mẹ (mẹ biết bếp, cha sửa đồ); đúng 3 dấu hiệu suy yếu hiện tại (hỏi lại nhiều lần / không nghe rõ / tay run khi cầm chén)
- Visualizable Type: Concrete
- Visualization Strategy: mô tả trực tiếp evidence — có thể cần hai lớp thời gian (hồi tưởng thời trẻ vs hiện tại suy yếu) để giữ đúng cấu trúc tương phản của beat; 3 dấu hiệu suy yếu là evidence cụ thể, dễ quan sát (tay run khi cầm chén, hỏi lại câu, không nghe rõ)
- Required Continuity: character continuity — mẹ, cha là chủ thể mới trong beat này (04A không xác nhận đây là cùng mẹ/cha với BEAT_002); timeline continuity — bản thân beat chứa hai mốc thời gian (thời trẻ của người kể chuyện vs hiện tại), cần giữ đúng trình tự nếu tách
- Forbidden Hallucination: không đặc tả bệnh lý cụ thể (không tên bệnh — narration chỉ mô tả triệu chứng chung)
- Visual Importance: High

**OBL_088** (beat_id: BEAT_088)
- Required Subject: cha mẹ, lòng hiếu, thời gian
- Required Action: No explicit visual action — luận đề cảnh báo.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — ẩn dụ "cuộc chạy đua với thời gian" không có hình ảnh cụ thể được narration đặt tên thêm (không có hình ảnh cuộc đua/đồng hồ cụ thể trong 04A)
- Visualizable Type: Non-Visual — mặc dù có cụm ẩn dụ, 04A không xác nhận đây là một hình ảnh được narration mô tả cụ thể (chỉ là cách nói, không phải hình ảnh thị giác được chỉ định)
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không tự dựng hình ảnh "cuộc đua"/đồng hồ đếm ngược — đây là một cách nói ẩn dụ bằng ngôn ngữ, không phải hình ảnh được narration chỉ định
- Visual Importance: Low

**OBL_089** (beat_id: BEAT_089)
- Required Subject: cha mẹ, bữa cơm tối nay, cuộc gọi cuối tuần, câu chuyện cũ
- Required Action: tỉnh lại; nghe bằng lòng nhẫn nại (thay vì cắt ngang)
- Required Setting: Setting intentionally unspecified cho từng ví dụ.
- Required Visual Evidence: 3 ví dụ cụ thể: một bữa cơm (không có sự lạnh nhạt); một cuộc gọi cuối tuần (không mang tính nghĩa vụ); hành vi nghe kiên nhẫn khi cha mẹ kể chuyện cũ (đối lập với cắt ngang)
- Visualizable Type: Concrete
- Visualization Strategy: mô tả trực tiếp evidence — 3 ví dụ tương ứng có thể hiển thị bằng hành vi/tương tác cụ thể
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Medium

**OBL_090** (beat_id: BEAT_090)
- Required Subject: hiếu đạo, sự có mặt
- Required Action: No explicit visual action — luận đề dẫn nhập.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_091** (beat_id: BEAT_091)
- Required Subject: sự có mặt, người ở xa quê, mẹ, cha, cuộc trò chuyện
- Required Action: gọi về (có thật sự nghe không); gửi tiền (có hỏi mẹ cần gì không); đưa cha đi khám (có để cha không thấy là gánh nặng không)
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: 3 tương tác cụ thể — gọi điện chăm chú lắng nghe; gửi tiền kèm hỏi han; đưa cha đi khám với thái độ tôn trọng — 4 hoàn cảnh không thể có mặt bằng thân (ở xa quê/làm nhiều giờ/nước ngoài/không đủ điều kiện) là bối cảnh trừu tượng, không có evidence hình ảnh riêng
- Visualizable Type: Concrete (cho 3 tương tác) — 4 hoàn cảnh không đủ điều kiện là Non-Visual/Abstract, không cần evidence riêng
- Visualization Strategy: mô tả trực tiếp evidence cho 3 tương tác cụ thể; không hiển thị riêng 4 hoàn cảnh địa lý/công việc vì 04A không cung cấp evidence hình ảnh cho chúng
- Required Continuity: None.
- Forbidden Hallucination: không đặc tả quốc gia/địa điểm cụ thể cho "ở nước ngoài"
- Visual Importance: Medium

**OBL_092** (beat_id: BEAT_092)
- Required Subject: người con, cha mẹ, tiền, cảm giác được nhìn thấy, điện thoại
- Required Action: không để cha mẹ thiếu tiền; (thiếu) cảm giác được nhìn thấy
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hành vi chu cấp tài chính (đối lập); 3 nhu cầu cụ thể (nói chuyện không sợ phiền/được hỏi ý kiến/biết mình không chỉ là trách nhiệm tài chính) — phần nhu cầu tình cảm khó hiển thị dương tính, chỉ có dấu hiệu gián tiếp
- Visualizable Type: Abstract — có chủ thể cụ thể (người con, cha mẹ) nhưng nội dung cốt lõi ("thiếu cảm giác được nhìn thấy") là trạng thái nội tâm, chỉ có dấu hiệu gián tiếp (ví dụ thần thái cô đơn dù đủ đầy vật chất)
- Visualization Strategy: mô tả dấu hiệu quan sát được — thần thái cô đơn/thiếu kết nối của cha mẹ dù được chu cấp đầy đủ vật chất
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Medium

**OBL_093** (beat_id: BEAT_093)
- Required Subject: người con
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_094** (beat_id: BEAT_094)
- Required Subject: người chăm sóc, mẹ (bệnh), người ngoài, nhà tắm
- Required Action: đi làm; nấu ăn; thay thuốc; thức đêm khi mẹ trở mình; khóc trong nhà tắm; thoáng nghĩ muốn được nghỉ
- Required Setting: nhà tắm (địa điểm cụ thể được narration nêu tên cho khoảnh khắc bị che giấu); các hoạt động khác (đi làm/nấu ăn/thay thuốc) không có địa điểm cụ thể ngoài "tại nhà" ngụ ý.
- Required Visual Evidence: đúng 4 hoạt động chăm sóc theo trình tự ngày/chiều/tối/đêm; hành vi khóc trong nhà tắm với nước chảy nhỏ (chi tiết cụ thể được narration nêu); ý nghĩ thoáng qua "mình mệt quá, mình muốn được nghỉ" (nội dung nội tâm, không hiển thị trực tiếp được bằng hình ảnh, chỉ ngụ ý qua biểu cảm)
- Visualizable Type: Concrete (cho các hoạt động chăm sóc và cảnh khóc trong nhà tắm) — có chủ thể, hành vi, và địa điểm cụ thể
- Visualization Strategy: mô tả trực tiếp evidence — trình tự 4 hoạt động chăm sóc; cảnh khóc trong nhà tắm với chi tiết "nước chảy thật nhỏ" (để không ai nghe thấy) đúng như narration nêu; ý nghĩ thoáng qua không hiển thị trực tiếp, chỉ ngụ ý qua biểu cảm gương mặt
- Required Continuity: location continuity nội tại — nhà tắm là địa điểm riêng biệt cho khoảnh khắc bị che giấu, khác với không gian sinh hoạt chung của các hoạt động chăm sóc khác
- Forbidden Hallucination: không đặc tả bệnh cụ thể của mẹ; không đặt tên nhân vật; không hiển thị lời khen "con hiếu quá" của người ngoài bằng một nhân vật cụ thể có mặt trực tiếp trong cùng khung hình với cảnh khóc (đây là hai thời điểm/góc nhìn khác nhau theo narration — lời khen là nhận xét bên ngoài, cảnh khóc là điều "không ai thấy")
- Visual Importance: High

**OBL_095** (beat_id: BEAT_095)
- Required Subject: hiếu đạo, người chăm sóc, bài giảng
- Required Action: No explicit visual action — luận đề đánh giá.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_096** (beat_id: BEAT_096)
- Required Subject: lòng hiếu trưởng thành, anh chị em, hỗ trợ y tế/tinh thần/cộng đồng
- Required Action: No explicit visual action — 4 câu hỏi tự vấn song song.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

---

## ACT XI — BEAT_097–BEAT_106

**OBL_097** (beat_id: BEAT_097)
- Required Subject: trung đạo, cha mẹ, chữ hiếu
- Required Action: No explicit visual action — hai cặp phủ định song song định nghĩa trung đạo.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_098** (beat_id: BEAT_098)
- Required Subject: gia đình có tổn thương, trung đạo, trí tuệ
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_099** (beat_id: BEAT_099)
- Required Subject: người muốn hiếu kính, nhục mạ, kiểm soát, điện thoại, cha mẹ, sự tha thứ
- Required Action: bị nhục mạ/kiểm soát/kéo vào vùng đau cũ; căng cứng khi nghe chuông điện thoại; cố tha thứ nhiều lần
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: dấu hiệu căng thẳng cơ thể khi nghe chuông điện thoại (evidence cụ thể nhất, dễ quan sát); các hành vi "bị nhục mạ/kiểm soát" là trừu tượng, không có hình thức cụ thể được nêu
- Visualizable Type: Abstract — có chủ thể xác định và một dấu hiệu quan sát cụ thể (căng cứng cơ thể khi nghe chuông điện thoại), nhưng phần lớn nội dung (nhục mạ/kiểm soát) không có evidence hình ảnh cụ thể
- Visualization Strategy: mô tả dấu hiệu quan sát được — phản ứng căng cứng cơ thể/né tránh khi nghe chuông điện thoại, như dấu hiệu chính cho toàn bộ trạng thái được mô tả
- Required Continuity: None.
- Forbidden Hallucination: không đặc tả hình thức nhục mạ/kiểm soát cụ thể; không hình ảnh hoá câu thoại "hãy về đi, cha mẹ mà" bằng một nhân vật cụ thể đang nói câu này — đây là một lời khuyên phổ biến được trích dẫn để phê phán, không phải lời thoại của một nhân vật trong câu chuyện
- Visual Importance: Medium

**OBL_100** (beat_id: BEAT_100)
- Required Subject: hiếu đạo, nguy hiểm
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_101** (beat_id: BEAT_101)
- Required Subject: mối quan hệ chưa an toàn, thù hận, khoảng cách, lời cầu nguyện thầm, bạo lực, cha mẹ, vô minh
- Required Action: giữ khoảng cách; cầu nguyện thầm; nhìn nhận cha mẹ cũng là con người với vô minh/khổ đau
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: dấu hiệu giữ khoảng cách (vật lý/quan hệ); tư thế cầu nguyện thầm lặng — 04A không cung cấp chủ thể cụ thể
- Visualizable Type: Abstract — có hành động được nêu tên (giữ khoảng cách, cầu nguyện thầm) nhưng chủ thể hoàn toàn chung chung
- Visualization Strategy: mô tả dấu hiệu quan sát được — một khoảng cách vật lý giữa hai người chung chung; một tư thế cầu nguyện thầm lặng, không gán cho nhân vật cụ thể
- Required Continuity: None.
- Forbidden Hallucination: không đặc tả nhân vật cụ thể hay lý do xung đột cụ thể
- Visual Importance: Medium

**OBL_102** (beat_id: BEAT_102)
- Required Subject: None cụ thể.
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_103** (beat_id: BEAT_103)
- Required Subject: người gây tổn thương, từ bi, bạo lực, trí tuệ, hiếu đạo, người bị thương
- Required Action: No explicit visual action — 4 phân biệt phủ định song song.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_104** (beat_id: BEAT_104)
- Required Subject: báo hiếu, cha mẹ, con
- Required Action: No explicit visual action — mở ra chiều ngược của khái niệm báo hiếu.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_105** (beat_id: BEAT_105)
- Required Subject: cha, mẹ, con, tình thương, uy nghiêm, sự khiêm cung
- Required Action: cha xin lỗi con; mẹ lắng nghe con
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: cử chỉ cha xin lỗi con; cử chỉ mẹ lắng nghe con
- Visualizable Type: Concrete
- Visualization Strategy: mô tả trực tiếp evidence — một cử chỉ xin lỗi từ cha, một cử chỉ lắng nghe từ mẹ (có thể là hai khoảnh khắc riêng biệt)
- Required Continuity: None (nhân vật mới, không liên kết với gia đình ở các beat khác — 04A không xác nhận).
- Forbidden Hallucination: None thêm.
- Visual Importance: Medium

**OBL_106** (beat_id: BEAT_106)
- Required Subject: đứa trẻ, mẹ, cha, vết thương
- Required Action: chờ đợi một câu nói (cả đời) — hành động kéo dài, khó hiển thị trong một khoảnh khắc
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hai câu thoại nguyên văn ("mẹ hiểu là ngày xưa mẹ đã làm con đau" / "cha hiểu là cha đã quá nóng") — đây là nội dung ngôn ngữ, không phải evidence hình ảnh; hành động "chờ đợi cả đời" không thể hiển thị trực tiếp bằng một khung hình
- Visualizable Type: Non-Visual — nội dung cốt lõi là lời thoại (ngôn ngữ) và một trạng thái chờ đợi kéo dài suốt đời, không có một khoảnh khắc hình ảnh cụ thể nào đại diện được cho toàn bộ ý nghĩa
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không đổi/diễn giải lại 2 câu thoại nguyên văn nếu được trích dẫn ở bước sau
- Visual Importance: Low

---

## ACT XII — BEAT_107–BEAT_113

**OBL_107** (beat_id: BEAT_107)
- Required Subject: cha, mẹ, con, tiền bạc, nhà cửa, bằng cấp, cơn giận, nghiệp
- Required Action: để lại (điều gì trong lòng con); dừng lại (trước khi giận biến thành nghiệp)
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: dấu hiệu kiềm chế cơn giận (tư thế/biểu cảm dừng lại) — evidence Concrete duy nhất; phần "để lại điều gì trong lòng con" là trừu tượng, không hiển thị trực tiếp
- Visualizable Type: Abstract — có chủ thể (cha/mẹ/con) và một hành động cụ thể (dừng lại trước cơn giận) làm dấu hiệu quan sát, phần còn lại là khái niệm trừu tượng
- Visualization Strategy: mô tả dấu hiệu quan sát được — một khoảnh khắc kiềm chế/dừng lại trước khi biểu lộ giận dữ
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Medium

**OBL_108** (beat_id: BEAT_108)
- Required Subject: hiếu đạo, con, cha mẹ, người già, người trẻ, căn nhà, địa ngục (ẩn dụ)
- Required Action: con học biết ơn; cha mẹ học khiêm cung; người già học buông kiểm soát; người trẻ học bớt vô tâm
- Required Setting: căn nhà — narration nêu địa điểm ẩn dụ cụ thể ("căn nhà bớt một chút địa ngục").
- Required Visual Evidence: hình ảnh ẩn dụ "địa ngục" do chính narration đặt tên cho một căn nhà bất hoà — **04A minh thị đây là ẩn dụ tâm lý, không phải cảnh giới địa ngục Phật giáo theo nghĩa đen**; 4 hành vi học tập (biết ơn/khiêm cung/buông kiểm soát/bớt vô tâm) là trừu tượng, không có hành vi cụ thể riêng
- Visualizable Type: Symbolic — narration tự đặt tên "địa ngục" làm ẩn dụ cho một căn nhà bất hoà, với ràng buộc rõ ràng về cách diễn giải
- Visualization Strategy: sử dụng hình ảnh ẩn dụ "căn nhà" ở trạng thái bất hoà/căng thẳng (không phải cảnh giới địa ngục siêu nhiên) làm evidence chính; không minh hoạ riêng 4 hành vi học tập vì không có evidence cụ thể
- Required Continuity: None (mặc dù liên kết ý nghĩa với BEAT_110 sau đó — cùng ẩn dụ "địa ngục hiện đại"; không phải continuity object/character theo 4 loại chính thức, chỉ là liên kết chủ đề).
- Forbidden Hallucination: **không thể hiện "địa ngục" ở đây như cảnh giới siêu hình/tôn giáo (lửa, quỷ, hình phạt...) — đây là ẩn dụ cho một căn nhà bất hoà đời thường, đúng như ràng buộc đã ghi trong 04A**
- Visual Importance: Medium

**OBL_109** (beat_id: BEAT_109)
- Required Subject: Kinh Địa Tạng, đời sống hiện đại
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_110** (beat_id: BEAT_110)
- Required Subject: địa ngục (ẩn dụ), căn nhà, bàn ăn, mẹ già, con (tranh giành), đứa trẻ, người lớn
- Required Action: không ai chịu nghe ai; mỗi người cầm một nỗi giận; con tranh phần thiệt hơn; đứa trẻ học tình thương có điều kiện; người lớn không biết ôm con
- Required Setting: căn nhà; bàn ăn; căn phòng (ba bối cảnh cụ thể được narration nêu cho 3 trong 5 hình ảnh).
- Required Visual Evidence: đúng 5 hình ảnh ẩn dụ theo đúng thứ tự: (1) căn nhà không ai nghe ai; (2) bàn ăn mỗi người cầm một nỗi giận; (3) căn phòng có mẹ già, con tranh phần thiệt hơn; (4) đứa trẻ học tình thương có điều kiện; (5) người lớn không biết ôm con
- Visualizable Type: Symbolic — 04A xác nhận rõ đây là ẩn dụ tâm lý về bất hoà gia đình do chính narration đặt tên bằng từ "địa ngục", không phải cảnh giới tôn giáo theo nghĩa đen
- Visualization Strategy: sử dụng đúng 5 hình ảnh ẩn dụ đã narration đặt tên, thể hiện như những khoảnh khắc đời thường bất hoà (không phải siêu nhiên); mỗi hình ảnh có thể là một khoảnh khắc riêng
- Required Continuity: None chính thức (liên kết chủ đề với BEAT_108, không phải continuity object/character/location/timeline theo 4 loại).
- Forbidden Hallucination: **không hình tượng hoá "địa ngục" bằng biểu tượng tôn giáo/siêu nhiên (lửa, quỷ, hình phạt...) — đây là ràng buộc minh thị từ 04A, vi phạm nghiêm trọng nếu bỏ qua**
- Visual Importance: High

**OBL_111** (beat_id: BEAT_111)
- Required Subject: địa ngục (ẩn dụ), sân hận, cõi lành, tâm biết dừng
- Required Action: No explicit visual action — luận đề đối lập.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp mới — đây là một phát biểu đối lập khái quát, evidence cụ thể được cung cấp ở BEAT_112 (danh sách hành vi "dừng lại")
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context (minh hoạ cụ thể ở OBL_112).
- Required Continuity: None.
- Forbidden Hallucination: không hình tượng hoá "địa ngục"/"cõi lành" bằng biểu tượng tôn giáo/siêu nhiên
- Visual Importance: Low

**OBL_112** (beat_id: BEAT_112)
- Required Subject: lời cay độc, cái tát, con mình, con người ta, công lao sinh thành, sự vô tâm
- Required Action: dừng lại (trước 5 hành vi cụ thể: lời cay độc, cái tát, so sánh con mình với con người ta, dùng công lao sinh thành để buộc người khác, vô tâm nguỵ trang bằng "bận")
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: khoảnh khắc kiềm chế/dừng lại trước một trong 5 hành vi — mỗi hành vi có thể minh hoạ bằng một khoảnh khắc kiềm chế tương ứng
- Visualizable Type: Abstract — hành động "dừng lại" là một trạng thái kiềm chế nội tâm, có dấu hiệu quan sát được (tư thế/biểu cảm) nhưng không phải một hành động dương tính rõ ràng
- Visualization Strategy: mô tả dấu hiệu quan sát được — một khoảnh khắc kiềm chế/dừng lại (ví dụ: tay dừng giữa chừng, biểu cảm chuyển từ căng thẳng sang bình tĩnh), không cần minh hoạ cả 5 hành vi đồng thời
- Required Continuity: None.
- Forbidden Hallucination: không thêm hành vi nào ngoài 5 hành vi đã liệt kê; không hiển thị hành vi TIÊU CỰC dương tính (ví dụ không hiển thị cảnh đang tát) — nội dung là hành vi kiềm chế/dừng lại TRƯỚC khi hành vi tiêu cực xảy ra, không phải chính hành vi tiêu cực đó
- Visual Importance: Medium

**OBL_113** (beat_id: BEAT_113)
- Required Subject: dòng truyền thừa, khổ đau
- Required Action: cứu (một khoảnh khắc; một dòng truyền thừa) — hành động trừu tượng ở mức ẩn dụ
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp mới — đây là bình luận khái quát hoá ý nghĩa của hành động "dừng lại" ở OBL_112
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: không dựng hình ảnh "dòng truyền thừa" bằng biểu tượng phả hệ/cây gia phả — không có căn cứ trong 04A
- Visual Importance: Low

---

## ACT XIII — BEAT_114–BEAT_122

**OBL_114** (beat_id: BEAT_114)
- Required Subject: cha mẹ
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — phát biểu về sự thiếu vắng khả năng liên lạc
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_115** (beat_id: BEAT_115)
- Required Subject: gia đình an toàn
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_116** (beat_id: BEAT_116)
- Required Subject: ký ức êm đềm
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_117** (beat_id: BEAT_117)
- Required Subject: cha mẹ (còn sống/đã mất), gia đình, sự an toàn, nỗi nhớ; **[Sửa 2026-07-15] "ngọn đèn nhỏ"** — narration tự đặt tên hình ảnh này làm khung cảm xúc cho toàn bộ 3 nhánh hướng dẫn ("xin đừng nghe tập này như lời trách, hãy nghe như một ngọn đèn nhỏ")
- Required Action: chăm sóc bằng sự có mặt thật hơn; biến nỗi nhớ thành đời sống tử tế hơn; giữ an toàn cho mình
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: 3 nhánh hướng dẫn tương ứng 3 hoàn cảnh — mỗi nhánh là một hành vi/thái độ trừu tượng (chăm sóc thật hơn, sống tử tế hơn, giữ an toàn), không có hành vi cụ thể duy nhất nào được narration chỉ định; hình ảnh ẩn dụ "ngọn đèn nhỏ" có thể dùng làm khung mở/đóng cho cả 3 nhánh nếu Phase C cần một hình ảnh thống nhất
- Visualizable Type: Abstract (cho 3 nhánh hướng dẫn cụ thể) pha Symbolic (cho khung ẩn dụ "ngọn đèn nhỏ" bao trùm) — có chủ thể (cha mẹ, khán giả ngầm định) và một hình ảnh ẩn dụ được chính narration đặt tên
- Visualization Strategy: mô tả dấu hiệu quan sát được — nếu cần, một cử chỉ chăm sóc ấm áp (nhánh 1), một khoảnh khắc suy tư tử tế (nhánh 2), một tư thế giữ khoảng cách an toàn nhưng không thù hận (nhánh 3) — ba dấu hiệu độc lập, không bắt buộc đồng thời; nếu dùng ẩn dụ "ngọn đèn nhỏ" làm khung, đây là Symbolic evidence tuỳ chọn, không bắt buộc phải xuất hiện dưới dạng vật lý (không nhất thiết phải là một ngọn đèn thật — 04A không xác nhận đây là hành động vật lý như ở BEAT_121, chỉ là cách nói ẩn dụ về giọng điệu tiếp nhận thông điệp)
- Required Continuity: **Không object continuity chính thức với "ngọn đèn" ở BEAT_039/BEAT_121** — xem ghi chú sửa đổi tại OBL_039; đây là lần dùng độc lập thứ ba của cùng một từ/hình ảnh ẩn dụ, không phải cùng một vật thể tái xuất
- Forbidden Hallucination: None thêm ngoài phạm vi 3 nhánh đã liệt kê; không dựng cảnh "thắp đèn" vật lý ở beat này nếu không được Phase C chủ động chọn làm khung ẩn dụ tuỳ chọn — 04A không xác nhận đây là một hành động vật lý bắt buộc tại vị trí này (khác với BEAT_121)
- Visual Importance: Medium

**OBL_118** (beat_id: BEAT_118)
- Required Subject: món nợ ân tình, tiền
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_119** (beat_id: BEAT_119)
- Required Subject: mất mát, lễ lớn
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_120** (beat_id: BEAT_120)
- Required Subject: lời xin lỗi, hạt giống (ẩn dụ)
- Required Action: trở thành (hạt giống)
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: hình ảnh ẩn dụ "hạt giống" do chính narration đặt tên
- Visualizable Type: Symbolic — narration tự đặt tên hình ảnh "hạt giống" làm ẩn dụ cho một lời xin lỗi muộn có giá trị chuyển hoá
- Visualization Strategy: sử dụng hình ảnh ẩn dụ "hạt giống" đã được narration đặt tên; không mở rộng thêm ẩn dụ nông nghiệp khác (đất, mầm cây, mùa vụ...) ngoài "hạt giống" nếu 04A không xác nhận
- Required Continuity: None.
- Forbidden Hallucination: không mở rộng ẩn dụ hạt giống thành một cảnh trồng trọt đầy đủ (đất, tay người trồng, cây nảy mầm) — 04A chỉ xác nhận từ "hạt giống", không xác nhận thêm chi tiết
- Visual Importance: Low

**OBL_121** (beat_id: BEAT_121)
- Required Subject: chiếc ghế trống (callback motif), ngọn đèn, sự thành thật
- Required Action: ngồi xuống trước chiếc ghế; thắp một ngọn đèn; chắp tay; nói trong lòng (câu nguyên văn)
- Required Setting: Bối cảnh trong nhà, kế thừa từ toàn bộ chuỗi motif ghế (BEAT_001/002/005/042/047/085).
- Required Visual Evidence: hành động ngồi xuống trước chiếc ghế; hành động thắp một ngọn đèn; hành động chắp tay — 3 hành vi cụ thể theo đúng thứ tự đã nêu; nội dung câu nói trong lòng là ngôn ngữ nội tâm, không phải evidence hình ảnh
- Visualizable Type: Concrete (cho 3 hành vi) pha Symbolic (ngọn đèn — cùng hình ảnh ẩn dụ với "ngọn đèn" ở BEAT_039, dù 04A không ép buộc xác nhận đây là continuity object chặt chẽ giữa hai lần dùng)
- Visualization Strategy: mô tả trực tiếp evidence — ngồi xuống trước chiếc ghế, thắp đèn, chắp tay, theo đúng thứ tự; câu nói trong lòng không hiển thị bằng chữ viết trên màn hình (vi phạm chính sách không văn bản), chỉ ngụ ý qua thần thái
- Required Continuity: object continuity — chiếc ghế, đây là điểm **giải quyết (resolution)** của toàn bộ motif ghế xuyên suốt episode (BEAT_001→002→042→047→085→121)
- Forbidden Hallucination: không đổi nội dung câu nói nguyên văn nếu được trích dẫn; không thêm hành động nghi lễ khác ngoài thắp đèn và chắp tay (không thêm nhang, không thêm bàn thờ nếu 04A không xác nhận — 04A chỉ nêu "ngọn đèn" và "chắp tay", không nêu bàn thờ ở beat này cụ thể)
- Visual Importance: Critical — điểm giải quyết motif trung tâm của toàn episode

**OBL_122** (beat_id: BEAT_122)
- Required Subject: cha mẹ, khán giả ("bạn")
- Required Action: No explicit visual action — câu hỏi trực tiếp.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

---

## ACT XIV — BEAT_123–BEAT_128

**OBL_123** (beat_id: BEAT_123)
- Required Subject: khán giả ("bạn"), nỗi nhớ
- Required Action: No explicit visual action — câu hỏi trực tiếp.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_124** (beat_id: BEAT_124)
- Required Subject: tập tiếp theo, người sống, người đã mất, Kinh Địa Tạng, hồi hướng, thế giới vô hình, nhân quả, từ bi
- Required Action: No explicit visual action — giới thiệu nội dung tập sau.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None — 04A minh thị đây là nội dung của TẬP KHÁC, không phải nội dung chính của EP004
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context. **Ràng buộc kế thừa từ 04A: nội dung này thuộc tập tiếp theo — nếu bước sau cần một hình ảnh chuyển tiếp/teaser, nó không được xây dựng như nội dung chính thức của EP004.**
- Required Continuity: None.
- Forbidden Hallucination: không mở rộng/diễn giải trước nội dung tập sau bằng hình ảnh cụ thể
- Visual Importance: Low

**OBL_125** (beat_id: BEAT_125)
- Required Subject: khán giả, gương mặt, chiếc ghế (callback motif), bàn tay, câu chưa kịp nói
- Required Action: giữ nhẹ; không biến thành tội lỗi; để trở thành lời nhắc
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: 4 hình ảnh khả dĩ được liệt kê như các khả năng ngang hàng (gương mặt/chiếc ghế/bàn tay/câu chưa kịp nói) — 04A minh thị không ưu tiên hình ảnh nào trong 4 khả năng này
- Visualizable Type: Abstract — có 4 chủ thể/vật thể được nêu tên làm khả năng minh hoạ, nhưng nội dung cốt lõi (hướng dẫn cảm xúc "giữ nhẹ, đừng biến thành tội lỗi") là trừu tượng
- Visualization Strategy: mô tả dấu hiệu quan sát được — CHỈ ĐƯỢC chọn evidence từ trong 4 khả năng đã liệt kê (gương mặt/chiếc ghế/bàn tay/câu chưa kịp nói), không được ưu tiên một khả năng làm "chính thức" duy nhất nếu bước sau cần chọn
- Required Continuity: object continuity — nếu "chiếc ghế" được chọn làm evidence, đây là lần callback thứ sáu và cuối cùng của motif ghế, liên kết với BEAT_001/002/042/047/085/121
- Forbidden Hallucination: không chọn một trong 4 hình ảnh làm hình ảnh "chính thức" duy nhất khi 04A xác nhận đây là các khả năng ngang hàng — đây là ràng buộc minh thị kế thừa từ 04A
- Visual Importance: Medium

**OBL_126** (beat_id: BEAT_126)
- Required Subject: tình thương
- Required Action: nói (tình thương, khi còn có thể)
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp — đây là một luận đề/lời nhắc bằng ngôn ngữ
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_127** (beat_id: BEAT_127)
- Required Subject: biết ơn, trí tuệ
- Required Action: No explicit visual action.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context.
- Required Continuity: None.
- Forbidden Hallucination: None thêm.
- Visual Importance: Low

**OBL_128** (beat_id: BEAT_128)
- Required Subject: hiếu đạo, mặc cảm, khổ đau, thế gian
- Required Action: No explicit visual action — luận đề khép lại toàn bộ episode.
- Required Setting: Setting intentionally unspecified.
- Required Visual Evidence: None trực tiếp.
- Visualizable Type: Non-Visual
- Visualization Strategy: No direct visual representation. Requires neighboring semantic context. Đây là beat cuối cùng của episode — nếu bước sau cần một hình ảnh khép lại, nên tái sử dụng evidence đã thiết lập ở OBL_121 (điểm giải quyết motif ghế) thay vì phát minh evidence mới, để giữ tính nhất quán của kết luận.
- Required Continuity: None chính thức, nhưng khuyến nghị liên kết chủ đề với OBL_121/OBL_050/OBL_064/OBL_111-113 (chủ đề "dừng khổ đau truyền tiếp") nếu bước sau cần bối cảnh hình ảnh.
- Forbidden Hallucination: không phát minh hình ảnh mới cho câu kết — nên tái sử dụng evidence đã có (chiếc ghế) hơn là tạo evidence riêng
- Visual Importance: Low

---

## Đối soát tổng hợp (đếm lại bằng `grep` trực tiếp trên chính file này, không phải ước lượng)

| Trường | Giá trị / Phân bố |
|---|---|
| Tổng Visual Obligation | 128 |
| Ánh xạ beat_id BEAT_001→BEAT_128 | Đúng thứ tự, 1-1, không thiếu không trùng (đã kiểm chứng bằng script) |

**Visualizable Type:**

| Loại | Số lượng | Tỉ lệ |
|---|---:|---:|
| Non-Visual | 74 | 57.8% |
| Concrete | 30 | 23.4% |
| Abstract | 19 | 14.8% |
| Symbolic | 5 | 3.9% |
| **Tổng** | **128** | **100%** |

**Visual Importance:**

| Mức | Số lượng | Tỉ lệ |
|---|---:|---:|
| Low | 77 | 60.2% |
| Medium | 30 | 23.4% |
| High | 13 | 10.2% |
| Critical | 8 | 6.2% |
| **Tổng** | **128** | **100%** |

**Nhận xét về phân bố:** Hơn một nửa số obligation (57.8%) là Non-Visual — đây là hệ quả trực tiếp của bản chất narration (một bài giảng suy ngẫm dày đặc luận đề/aphorism, đã ghi nhận ở `04A_SEMANTIC_BEATS.md`), không phải dấu hiệu phân tích sai. Chỉ 8 obligation (6.2%) là Critical — tập trung vào: motif chiếc ghế (OBL_001, OBL_005, OBL_042, OBL_121), continuity thread người cha (OBL_056, OBL_058, OBL_059), và pháp hội Đao Lợi (OBL_010). Đây là những điểm bắt buộc không được bỏ sót ở Phase C (Shot Planning) vì thiếu chúng sẽ làm mất trục cảm xúc/giáo lý chính của episode. 5 obligation Symbolic (OBL_039, OBL_062, OBL_108, OBL_110, OBL_120) đều dùng đúng ẩn dụ do chính narration đặt tên (ngọn đèn/cây roi, nén hương/bàn thờ, địa ngục-căn nhà, hạt giống) — không có ẩn dụ nào tự phát minh ở bước này.
