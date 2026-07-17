# 04C — Shot Plan (EP004)
Phase C của Video Creation Pipeline, **đã cập nhật ở Phase C.1 (Hold Decomposition / Short-Shot Resolution / Domain Approval Gate)**. Tuân thủ `VIDEO_CREATION_SYSTEM_SPEC.md` (Mục 2.5) và các quy tắc bàn giao bổ sung tại `04B_VISUAL_OBLIGATIONS.md` (mục "[Bổ sung 2026-07-15]"). Nguồn: `04A_SEMANTIC_BEATS.md` + `04B_VISUAL_OBLIGATIONS.md` (đã sửa). Đây không phải video prompt — không có camera, lens, ánh sáng chi tiết, hay câu chữ điện ảnh hoa mỹ ở bất kỳ đâu trong file này.

Số lượng shot **không bị ép theo 128 obligation hay 402 clip cố định** — được xác định từ nhu cầu thực tế truyền tải evidence, giữ nhịp, tránh lặp, giữ continuity. Kết quả sau Phase C.1: **100 shot** cho 128 obligation (tăng từ 90 shot ở Phase C gốc, sau khi tách 3 hold quá dài và sáp nhập 1 shot quá ngắn — xem Changelog bên dưới). *(Ghi chú tự sửa: bản Phase C gốc từng ghi nhầm "101 shot" trong câu mở đầu này dù số shot thực tế luôn là 90 — lỗi đánh máy chưa từng được một script nào đối chiếu; nay đã sửa và mọi con số trong tài liệu này đều được xác minh lại bằng script trước khi công bố.)*

---

## Quy trình đã áp dụng

```
Visual Obligations (128, từ 04B)
   → group neighboring obligations theo cùng continuity/setting/thời điểm
   → identify required evidence (chỉ dùng Required Subject/Action/Setting/Evidence đã có ở 04B)
   → decide dedicated / shared / hold / no-visual cho từng obligation
   → build visual sequence (thứ tự shot theo đúng thứ tự beat, không đảo)
   → assign continuity (chỉ 4 thread Critical đã xác nhận + continuity trong-scene cục bộ)
   → define production fills (tách bạch khỏi Source Fact, theo khung đã bổ sung ở 04B)
   → validate coverage (mục cuối file)
   → [Phase C.1] hold decomposition + short-shot resolution + domain approval gate
```

## Continuity Threads chính thức (chỉ những gì 04A/04B xác nhận — không đổi ở Phase C.1)

| Thread | Loại | Obligation liên quan | Ghi chú |
|---|---|---|---|
| **T1 — Chiếc ghế** | object | OBL_001, 002, 005, 042, 047, 085, 121 | Object continuity đầy đủ — cùng một chiếc ghế xuyên suốt, đã xác nhận ở 04A/04B. OBL_125 KHÔNG được ép vào thread này (04A liệt kê ghế chỉ là 1 trong 4 khả năng ngang hàng, không khẳng định). Ở cấp shot (sau Phase C.1), thread này chạy qua: S001,S002,S003,S005,S042(callback qua S033-cũ),S067,S095,S096,S099. |
| **T2 — Đức Phật/thân mẫu/Cung Trời Đao Lợi** | character + location | OBL_010, 017, 022, 076 | Character continuity (Đức Phật/thân mẫu) + location continuity (Đao Lợi), cùng một pháp hội xuyên suốt các lần nhắc lại. Ở cấp shot: S009,S010,S012-S017,S034,S059,S060. |
| **T3 — Người cha BEAT_056–059** | character + event | OBL_056, 057, 058, 059 | Character continuity chặt — cùng người cha, cùng con, cùng sự kiện liên tục. **Không mở rộng sang OBL_062** (04B đã xác nhận OBL_062 là chủ thể mới "một người", không phải cùng nhân vật). Ở cấp shot: S042(gộp BEAT_056+057),S043,S044. |
| **T4 — "Ngọn đèn"** | *không phải continuity chính thức* | OBL_039, 117, 121 | Theo sửa đổi tại 04B: đây là 3 lần dùng độc lập cùng một từ/ẩn dụ, **không** phải cùng một vật thể — không lập continuity thread thật. Ở cấp shot: S028, S092/S093, S095. |

Ngoài 4 thread trên, mọi continuity khác trong file này là **continuity cục bộ trong-scene** — không được coi là motif xuyên suốt episode, không được tái dùng ở scene khác.

---

## Phase C.1 Changelog — Hold Decomposition / Short-Shot Resolution

### 1. Ba hold quá dài đã được tách (không còn shot nào ≥ 60s)

| Hold cũ | Thời lượng cũ | Tách thành | Căn cứ tách |
|---|---:|---|---|
| **S005 (cũ)** | 76.62s, 5 beat | **S005→S008 (mới, 4 shot)**: S005 REVEAL (ghế trống hẳn) → S006 HOLD (5 câu chưa nói) → S007 HOLD (hồi cố series) → S008 TRANSITION (mờ dần sang Đao Lợi) | Semantic progression thật: khoảnh khắc trống → im lặng đau buồn → chuyển sang meta-narrative → bắc cầu sang bối cảnh mới. Không tách bằng camera — mỗi shot có Shot Function khác nhau phản ánh đúng bước ngoặt nội dung. |
| **S009 (cũ)** | 162.46s, 9 beat | **S012→S017 (mới, 6 shot)**: S012 HOLD (khung rộng, sửa nhận thức sai) → S013 DEVELOP (cử chỉ hướng về thân mẫu, khung gần — evidence có sẵn ở OBL_017) → S014 HOLD (doctrine phần 1) → S015 HOLD (doctrine phần 2) → S016 CALLBACK (khung rộng, tái hiện đúng evidence BEAT_010, khớp OBL_022) → S017 HOLD (luận đề khép) | Semantic progression dựa trên 2 trạng thái hình ảnh đã có căn cứ trong 04B: khung rộng (thuyết pháp, từ OBL_010/022) và khung gần (cử chỉ hướng về thân mẫu, từ OBL_017) — luân phiên đúng theo diễn biến nội dung, không phát minh hình ảnh mới. |
| **S018 (cũ)** | 70.62s, 3 beat | **S026→S027 (mới, 2 shot)**: S026 DEVELOP (giữ khoảng cách/ranh giới — evidence OBL_036) → S027 HOLD (hệ quả + 4 phân biệt) | Một evidence thật (OBL_036) tách khỏi phần thuần luận đề còn lại (OBL_037/038, không evidence). |

Tổng: 90 - 3 (hold cũ) + 4+6+2 (12 shot mới) = **99**, cộng thêm 2 shot khác (S044, S050) cũng được tách vì lý do khác (mục 3) và trừ 1 shot bị sáp nhập (mục 2) → **100 shot cuối cùng**.

### 2. Hai shot quá ngắn đã được xử lý

| Shot cũ | Thời lượng | Resolution | Lý do |
|---|---:|---|---|
| **S034 (cũ)**, BEAT_057 "vòng lặp vẫn quay" | 2.77s | **MERGE_WITH_NEIGHBOR** — sáp nhập vào S033(cũ), nay là **S042 (mới)** | Đây là continuation hold thuần tuý (0 evidence riêng, cùng nhân vật T3, cùng khung hình với shot trước) — không phải một khoảnh khắc thị giác độc lập, sáp nhập trung thực hơn là giữ một shot ID riêng cho 0 nội dung mới. |
| **S053 (cũ)**, BEAT_081 "một bữa cơm không cáu gắt" | 2.77s | **KEEP_WITH_JUSTIFICATION** — vẫn là **S063 (mới)**, không đổi | Thuộc chuỗi 6 "thực hành nhỏ" nhịp nhanh có chủ đích (S062–S067 mới); shot đơn giản (một hành động tĩnh, dễ đọc); rút ngắn nhân tạo nhịp điệu đã thiết kế sẽ phá vỡ hiệu ứng dồn dập của cả chuỗi. Không có hành động phức tạp nào cần thêm thời gian để đọc. |

### 3. Vùng 40–60s: 11 shot đã review, 2 shot được tách (có evidence hợp lệ), 9 shot giữ nguyên (có justification)

| Shot cũ | Thời lượng cũ | Quyết định | Căn cứ |
|---|---:|---|---|
| S044 (cũ) | 59.08s | **TÁCH** → S052 (DEVELOP, evidence OBL_066) + S053 (HOLD, phần còn lại) | Evidence chiếm 72% thời lượng (92/128 từ), phần hold còn lại đủ lớn (36w≈16.6s) để là một shot riêng có ý nghĩa, không phải mảnh vụn. |
| S050 (cũ) | 57.69s | **TÁCH** → S059 (CALLBACK, evidence OBL_076) + S060 (HOLD, phần còn lại) | Tương tự — evidence 42%, phần hold còn lại 73w≈33.7s đủ lớn, và 3 beat có nội dung khác biệt rõ (tổng kết/không sợ hãi/câu hỏi tương phản). |
| S029 (cũ, BEAT_046-048) | 45.23s | **GIỮ NGUYÊN** (nay S038) | Một continuity thread liên tục (callback chiếc ghế T1) không có điểm ngắt tự nhiên — tách sẽ phá continuity thay vì phục vụ nó. |
| S030 (cũ, BEAT_049-050) | 48.92s | **GIỮ NGUYÊN** (nay S039) | Evidence (OBL_049) chiếm 84% thời lượng; phần non-visual còn lại chỉ 17w≈7.85s — quá nhỏ để tách có ý nghĩa. |
| S046 (cũ, BEAT_071-072) | 41.08s | **GIỮ NGUYÊN** (nay S055) | Cả hai beat đều Non-Visual (0% evidence) — không có căn cứ để dựng một trạng thái hình ảnh thứ hai; đây là pure hold tiếp nối S054(mới), không thể tách có căn cứ. |
| S061 (cũ, BEAT_088-089) | 49.85s | **GIỮ NGUYÊN** (nay S071) | Evidence (OBL_089) chiếm 78%; phần non-visual đầu (OBL_088) chỉ 23w≈10.6s — dưới ngưỡng 15s để đáng tách. |
| S062 (cũ, BEAT_090-091) | 46.62s | **GIỮ NGUYÊN** (nay S072) | Evidence (OBL_091) chiếm 88%; phần non-visual đầu chỉ 12w≈5.5s — quá nhỏ. |
| S063 (cũ, BEAT_092-093) | 41.08s | **GIỮ NGUYÊN** (nay S073) | Evidence (OBL_092) chiếm 91%; phần non-visual cuối chỉ 8w≈3.7s — quá nhỏ. |
| S069 (cũ, BEAT_100-101) | 43.85s | **GIỮ NGUYÊN** (nay S079) | Evidence (OBL_101) chiếm 85%; phần non-visual đầu chỉ 14w≈6.5s — quá nhỏ. |
| S071 (cũ, BEAT_104-105) | 48.00s | **GIỮ NGUYÊN** (nay S081) | Evidence (OBL_105) chiếm 74%; phần non-visual đầu 27w≈12.5s — dưới ngưỡng 15s, borderline nhưng chưa đủ để tách. |

**Ngưỡng áp dụng nhất quán:** một shot 2-beat chỉ được tách khi phần "còn lại" (evidence hoặc non-visual, bên nào nhỏ hơn) đạt tối thiểu ~15 giây (~32 từ) — dưới ngưỡng này, tách chỉ tạo ra một mảnh vụn không đáng có một Shot ID riêng. **Không chia máy móc theo ngưỡng thời gian tổng (40-60s)** — quyết định dựa hoàn toàn trên tỉ trọng evidence thực tế của từng beat, tính bằng script từ số từ narration gốc, không ước lượng cảm tính.

### 4. Domain Approval Gate

Xem mục "Domain Approval Gate (Phase D.1)" đầy đủ tại `04D_SHOT_TIMING_AND_PRODUCTION_FILL.md` — tóm tắt: 26/26 shot (mở rộng từ 20 shot cũ do S009/S050 bị tách) đã chuyển từ `DOMAIN_REVIEW_REQUIRED` sang **`APPROVED_WITH_CONSTRAINTS`** (0 `REVISION_REQUIRED`).

---

---

## ACT I

**S001**
- Covered Beat IDs: BEAT_001 | Covered Obligation IDs: OBL_001 (DEDICATED_SHOT)
- Shot Function: ESTABLISH
- Required Source Evidence: chiếc ghế trống; không người ngồi
- Visual Subject: chiếc ghế trống | One Visible Action: (tĩnh) ghế đứng yên, không người
- Setting: trong nhà (Source Fact: "trong nhà"; Production Fill: bố cục phòng, hướng ánh sáng cụ thể — không phải điều narration xác nhận)
- Continuity In: — (mở đầu thread T1) | Continuity Out: → S002 (cùng ghế)
- Production Fills: chất liệu ghế (gỗ), không gian phòng cụ thể, thời điểm trong ngày
- Forbidden Additions: không người ngồi/vừa rời ghế; không đạo cụ phụ trợ (ảnh, hoa, đồ vật khác) chưa được 04A/04B xác nhận
- Estimated Duration: 7.85s (00:00:00.000 → 00:00:07.846)

**S002**
- Covered Beat IDs: BEAT_002 | Covered Obligation IDs: OBL_002 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: ghế cạnh bàn ăn; mẹ nhặt rau (hồi tưởng/thường lệ)
- Visual Subject: mẹ (generic, không đặc tả) ngồi ở ghế cạnh bàn ăn | One Visible Action: nhặt rau
- Setting: cạnh bàn ăn, cùng không gian nhà với S001
- Continuity In: ← S001 (cùng ghế, cùng nhà) | Continuity Out: → S003
- Production Fills: trang phục mẹ, loại rau, ánh sáng
- Forbidden Additions: không đặc tả danh tính/ngoại hình cụ thể của mẹ; không thêm nhân vật khác
- Estimated Duration: 8.49s (00:00:07.846 → 00:00:16.338)

**S003**
- Covered Beat IDs: BEAT_002 | Covered Obligation IDs: OBL_002 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: ghế gần cửa sổ; cha uống trà (hồi tưởng/thường lệ)
- Visual Subject: cha (generic) ngồi ở ghế gần cửa sổ | One Visible Action: uống trà
- Setting: gần cửa sổ, cùng không gian nhà
- Continuity In: ← S002 | Continuity Out: → S004
- Production Fills: trang phục cha, loại tách trà, ánh sáng cửa sổ
- Forbidden Additions: không đặc tả danh tính/ngoại hình cụ thể của cha
- Estimated Duration: 12.74s (00:00:16.338 → 00:00:29.077)

**S004**
- Covered Beat IDs: BEAT_003, BEAT_004 | Covered Obligation IDs: OBL_003, OBL_004 (NO_DEDICATED_VISUAL, DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: hành vi chuyển khoản đại diện cho nghĩa vụ vật chất thay thế hiện diện
- Visual Subject: một người con (generic) | One Visible Action: hoàn tất một giao dịch chuyển khoản trên điện thoại
- Setting: unspecified (Production Fill: không gian riêng tư nhẹ, có thể là góc làm việc/phòng khách của người con)
- Continuity In: — (nhân vật mới, không liên kết T1/T2/T3) | Continuity Out: —
- Production Fills: không gian, trang phục, kiểu điện thoại/giao diện chuyển khoản (không hiển thị chữ/UI theo policy)
- Forbidden Additions: không số tiền cụ thể; không thêm cảnh gọi điện/về thăm (đây là các hành vi KHÔNG xảy ra, không được hiển thị dương tính)
- Estimated Duration: 23.54s (00:00:29.077 → 00:00:52.615)

**S005**
- Covered Beat IDs: BEAT_005 | Covered Obligation IDs: OBL_005 (DEDICATED_SHOT)
- Shot Function: REVEAL
- Required Source Evidence: chiếc ghế chuyển sang trạng thái trống hẳn (không còn gắn với mẹ/cha)
- Visual Subject: cùng chiếc ghế (thread T1) | One Visible Action: (tĩnh) bụi lắng nhẹ trên ghế, không ai hiện diện
- Setting: cùng không gian nhà, thread T1
- Continuity In: S003 (cùng ghế) | Continuity Out: S006
- Production Fills: mức độ bụi, ánh sáng buổi chiều muộn
- Forbidden Additions: không cảnh nguyên nhân mất mát (bệnh viện, tang lễ...)
- Estimated Duration: 6.46s (00:00:52.615 → 00:00:59.077)
- **Ghi chú Phase C.1:** REVEAL chiếc ghế trống hẳn (tách từ S005 cũ)

**S006**
- Covered Beat IDs: BEAT_006 | Covered Obligation IDs: OBL_006 (CONTINUATION_HOLD)
- Shot Function: HOLD
- Required Source Evidence: 5 câu chưa kịp nói (chỉ mang qua giọng đọc, không hiển thị chữ)
- Visual Subject: cùng chiếc ghế (thread T1) | One Visible Action: (tĩnh) giữ nguyên khung ghế trống, không đổi
- Setting: cùng không gian nhà, thread T1
- Continuity In: S005 (T1) | Continuity Out: S007
- Production Fills: —
- Forbidden Additions: không hiển thị chữ cho 5 câu chưa kịp nói
- Estimated Duration: 21.69s (00:00:59.077 → 00:01:20.769)
- **Ghi chú Phase C.1:** HOLD cùng ghế, 5 câu chưa kịp nói (tách từ S005 cũ)

**S007**
- Covered Beat IDs: BEAT_007 | Covered Obligation IDs: OBL_007 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: — (04B xác nhận Non-Visual)
- Visual Subject: cùng chiếc ghế (thread T1) | One Visible Action: (tĩnh) giữ nguyên khung ghế, không đổi
- Setting: cùng không gian nhà, thread T1
- Continuity In: S006 (T1) | Continuity Out: S008
- Production Fills: —
- Forbidden Additions: không dựng cảnh minh hoạ cho nội dung hồi cố series (địa ngục/nghiệp báo/Địa Tạng) — không có evidence
- Estimated Duration: 33.23s (00:01:20.769 → 00:01:54.000)
- **Ghi chú Phase C.1:** HOLD cùng ghế, hồi cố series (tách từ S005 cũ)

**S008**
- Covered Beat IDs: BEAT_008, BEAT_009 | Covered Obligation IDs: OBL_008, OBL_009 (NO_DEDICATED_VISUAL)
- Shot Function: TRANSITION
- Required Source Evidence: — (04B xác nhận Non-Visual cho cả hai beat)
- Visual Subject: cùng chiếc ghế (thread T1), hình ảnh bắt đầu mờ dần | One Visible Action: (tĩnh→mờ dần) khung ghế mờ dần, chuẩn bị chuyển cảnh
- Setting: cùng không gian nhà, thread T1, chuyển tiếp
- Continuity In: S007 (T1) | Continuity Out: S009 (chuyển sang Đao Lợi, T2)
- Production Fills: tốc độ/kiểu mờ dần — kỹ thuật chuyển cảnh, không phải nội dung mới; Source Fact vẫn là chiếc ghế đã thiết lập
- Forbidden Additions: không dựng hình ảnh mới nào đại diện cho Đao Lợi ở shot này — việc mờ dần chỉ là kỹ thuật chuyển cảnh trên Source Fact đã có (chiếc ghế), không phải nội dung Đao Lợi được vẽ trước
- Estimated Duration: 15.23s (00:01:54.000 → 00:02:09.231)
- **Ghi chú Phase C.1:** TRANSITION mờ dần sang Đao Lợi (tách từ S005 cũ)

**S009**
- Covered Beat IDs: BEAT_010 | Covered Obligation IDs: OBL_010 (DEDICATED_SHOT)
- Shot Function: ESTABLISH
- Required Source Evidence: Đức Phật thuyết pháp tại Cung Trời Đao Lợi, trong liên hệ với thân mẫu
- Visual Subject: Đức Phật (medium-wide/silhouette theo ràng buộc an toàn tôn giáo đã có sẵn trong dự án) | One Visible Action: thuyết pháp
- Setting: Cung Trời Đao Lợi (Source Fact — tên địa điểm do narration nêu)
- Continuity In: — (mở đầu thread T2) | Continuity Out: → S010
- Production Fills: kiến trúc/không gian cụ thể của Đao Lợi (04A/04B không đặc tả — đây hoàn toàn là Production Fill, phải giữ mức biểu tượng/khiêm tốn theo chính sách an toàn tôn giáo của dự án, không tuyên bố là tái dựng lịch sử chính xác); sự hiện diện của một nhóm người dự pháp hội ở khoảng cách tôn kính (Production Fill cần thiết để hình ảnh hoá khái niệm "pháp hội" — bản thân từ "pháp hội" hàm ý một cuộc tụ họp, không thể hình ảnh hoá "pháp hội" mà không có ít nhất một gợi ý về người tham dự; số lượng/danh tính người tham dự không được đặc tả cụ thể)
- Forbidden Additions: không lời thoại của Đức Phật/thân mẫu; không đặc tả khuôn mặt cận cảnh của các nhân vật thiêng liêng; không kiến trúc được tuyên bố là tái hiện lịch sử chính xác
- Estimated Duration: 31.85s (00:02:09.231 → 00:02:41.077)

**S010**
- Covered Beat IDs: BEAT_011, BEAT_012, BEAT_013 | Covered Obligation IDs: OBL_011, OBL_012, OBL_013 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: (không có evidence riêng — 04B xác nhận cả 3 obligation Non-Visual)
- Visual Subject: giữ nguyên khung Đao Lợi từ S009 | One Visible Action: (tĩnh) không thay đổi
- Setting: Cung Trời Đao Lợi, thread T2
- Continuity In: ← S009 | Continuity Out: → S011
- Production Fills: không có mới (kế thừa S009)
- Forbidden Additions: không tự trả lời 3 câu hỏi tu từ bằng hình ảnh mới
- Estimated Duration: 38.77s (00:02:41.077 → 00:03:19.846)


---

## ACT II

**S011**
- Covered Beat IDs: BEAT_014, BEAT_015 | Covered Obligation IDs: OBL_014, OBL_015 (NO_DEDICATED_VISUAL, DEDICATED_SHOT)
- Shot Function: TRANSITION
- Required Source Evidence: dấu hiệu gián tiếp cho các lý do "đi chậm" (mệt mỏi/trầm lặng — theo đúng Visualization Strategy Abstract của 04B)
- Visual Subject: một người (generic, không xác định vai trò cụ thể trong 5 nhóm) | One Visible Action: ngồi yên lặng, tay khép hờ
- Setting: unspecified (Production Fill: không gian trung tính, có thể là góc nhà hoặc không gian tưởng niệm nhẹ)
- Continuity In: — (không liên kết thread nào) | Continuity Out: —
- Production Fills: không gian, trang phục
- Forbidden Additions: không đặc tả nhân vật cụ thể đại diện cho 1 trong 5 nhóm đã liệt kê (kinh điển/truyền thống/người mất cha mẹ/người chăm sóc/người tổn thương) — chỉ dùng MỘT dấu hiệu chung (trầm lặng) đại diện tổng quát, không chọn thiên vị một nhóm
- Estimated Duration: 38.31s (00:03:19.846 → 00:03:58.154)

**S012**
- Covered Beat IDs: BEAT_016 | Covered Obligation IDs: OBL_016 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: — (04B: cảnh báo nhận thức sai, không evidence dương tính)
- Visual Subject: Đức Phật, khung rộng (cùng continuity T2, kế thừa S009) | One Visible Action: (tĩnh) giữ nguyên khung rộng pháp hội đã thiết lập
- Setting: Cung Trời Đao Lợi, thread T2
- Continuity In: S009 (T2) | Continuity Out: S013
- Production Fills: không có mới
- Forbidden Additions: không dựng cảnh 'xa xôi rực rỡ tách biệt' (cách hiểu sai bị phê phán)
- Estimated Duration: 25.38s (00:03:58.154 → 00:04:23.538)
- **Ghi chú Phase C.1:** HOLD khung rộng Đao Lợi đã thiết lập (S009), sửa nhận thức sai (tách từ S009 cũ)

**S013**
- Covered Beat IDs: BEAT_017 | Covered Obligation IDs: OBL_017 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: thần thái điềm tĩnh/tôn kính của Đức Phật hướng về thân mẫu
- Visual Subject: Đức Phật (T2), cử chỉ hướng về phía thân mẫu — khung gần hơn S012 | One Visible Action: cử chỉ hướng về phía thân mẫu (nhẹ, không đặc tả khuôn mặt)
- Setting: Cung Trời Đao Lợi, thread T2
- Continuity In: S012 (T2) | Continuity Out: S014
- Production Fills: không có mới ngoài Production Fill đã dùng ở S009
- Forbidden Additions: không cận cảnh khuôn mặt thiêng liêng; không lời thoại
- Estimated Duration: 28.62s (00:04:23.538 → 00:04:52.154)
- **Ghi chú Phase C.1:** DEVELOP cử chỉ Đức Phật hướng về thân mẫu (khung gần) (tách từ S009 cũ)

**S014**
- Covered Beat IDs: BEAT_018, BEAT_019 | Covered Obligation IDs: OBL_018, OBL_019 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: — (04B: luận đề trừu tượng, không minh hoạ)
- Visual Subject: Đức Phật (T2), giữ khung gần từ S013 | One Visible Action: (tĩnh) giữ nguyên cử chỉ hướng về thân mẫu
- Setting: Cung Trời Đao Lợi, thread T2
- Continuity In: S013 (T2) | Continuity Out: S015
- Production Fills: —
- Forbidden Additions: không minh hoạ 'chấp trước/bám víu/chiếm hữu' (khái niệm bị phủ định)
- Estimated Duration: 33.69s (00:04:52.154 → 00:05:25.846)
- **Ghi chú Phase C.1:** HOLD khung gần, doctrine phần 1 (giác ngộ không lạnh lùng/chấp trước) (tách từ S009 cũ)

**S015**
- Covered Beat IDs: BEAT_020, BEAT_021 | Covered Obligation IDs: OBL_020, OBL_021 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: — (04B: 4 định nghĩa khái niệm thuần tuý, không minh hoạ)
- Visual Subject: Đức Phật (T2), giữ khung gần | One Visible Action: (tĩnh) giữ nguyên cử chỉ hướng về thân mẫu
- Setting: Cung Trời Đao Lợi, thread T2
- Continuity In: S014 (T2) | Continuity Out: S016
- Production Fills: —
- Forbidden Additions: không minh hoạ 4 khái niệm (chấp trước/biết ơn/báo ân/từ bi) bằng hình ảnh/nhân vật cụ thể
- Estimated Duration: 36.46s (00:05:25.846 → 00:06:02.308)
- **Ghi chú Phase C.1:** HOLD khung gần, doctrine phần 2 (4 định nghĩa) (tách từ S009 cũ)

**S016**
- Covered Beat IDs: BEAT_022 | Covered Obligation IDs: OBL_022 (SHARED_WITH_NEIGHBOR)
- Shot Function: CALLBACK
- Required Source Evidence: hành vi thuyết pháp/hiện diện của Đức Phật trong liên hệ với thân mẫu — TÁI HIỆN đúng evidence đã có ở S009, không thêm hành vi mới
- Visual Subject: Đức Phật (T2), khung rộng — tái hiện chính xác S009 | One Visible Action: thuyết pháp (giống hệt S009, không có hành động mới)
- Setting: Cung Trời Đao Lợi, thread T2
- Continuity In: S015 (T2) | Continuity Out: S017
- Production Fills: không có mới — dùng lại chính xác Production Fill của S009
- Forbidden Additions: không thêm hành động/lời thoại mới cho Đức Phật ngoài những gì đã ở S009
- Estimated Duration: 28.62s (00:06:02.308 → 00:06:30.923)
- **Ghi chú Phase C.1:** CALLBACK khung rộng (tái hiện đúng evidence BEAT_010) (tách từ S009 cũ)

**S017**
- Covered Beat IDs: BEAT_023, BEAT_024 | Covered Obligation IDs: OBL_023, OBL_024 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: — (2 luận đề khẳng định, không evidence hình ảnh)
- Visual Subject: Đức Phật (T2), giữ khung rộng từ S016 | One Visible Action: (tĩnh) giữ nguyên khung rộng
- Setting: Cung Trời Đao Lợi, thread T2
- Continuity In: S016 (T2) | Continuity Out: S018
- Production Fills: —
- Forbidden Additions: None thêm
- Estimated Duration: 9.69s (00:06:30.923 → 00:06:40.615)
- **Ghi chú Phase C.1:** HOLD khung rộng, luận đề khép (tách từ S009 cũ)


---

## ACT III

**S018**
- Covered Beat IDs: BEAT_025 | Covered Obligation IDs: OBL_025 (NO_DEDICATED_VISUAL)
- Shot Function: TRANSITION
- Required Source Evidence: —
- Visual Subject: (bắc cầu, không có evidence riêng — dùng đầu shot S019 làm điểm chuyển) | One Visible Action: —
- Setting: —
- Continuity In: — | Continuity Out: → S019
- Production Fills: —
- Forbidden Additions: —
- Estimated Duration: 31.85s (00:06:40.615 → 00:07:12.462)

**S019**
- Covered Beat IDs: BEAT_026 | Covered Obligation IDs: OBL_026 (DEDICATED_SHOT)
- Shot Function: CONTRAST
- Required Source Evidence: hành vi chuyển khoản + cuộc gọi ngắn, đại diện mẫu hình nhiều năm thiếu lắng nghe
- Visual Subject: người con (generic, KHÔNG liên kết với người con ở S004 — 04B không xác nhận cùng nhân vật) | One Visible Action: kết thúc nhanh một cuộc gọi điện thoại
- Setting: unspecified
- Continuity In: — | Continuity Out: →S020 (cùng ví dụ, tiếp nối luận điểm, không phải continuity nhân vật)
- Production Fills: không gian, trang phục
- Forbidden Additions: không hiển thị "đau lưng của mẹ"/"chiều mưa của cha" như hình ảnh dương tính — đây là nội dung KHÔNG xảy ra; không số tiền cụ thể
- Estimated Duration: 33.69s (00:07:12.462 → 00:07:46.154)

**S020**
- Covered Beat IDs: BEAT_027, BEAT_028 | Covered Obligation IDs: OBL_027, OBL_028 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ nguyên khung S019 | One Visible Action: (tĩnh, cuộc gọi vừa kết thúc, điện thoại đặt xuống)
- Setting: cùng S019
- Continuity In: ← S019 | Continuity Out: → S021
- Production Fills: —
- Forbidden Additions: —
- Estimated Duration: 16.15s (00:07:46.154 → 00:08:02.308)

**S021**
- Covered Beat IDs: BEAT_029 | Covered Obligation IDs: OBL_029 (DEDICATED_SHOT)
- Shot Function: CONTRAST
- Required Source Evidence: bàn thờ sáng đèn, mâm cỗ đầy, khách khứa đông; anh em không nhìn mặt nhau sau bữa ăn
- Visual Subject: một buổi giỗ đông người | One Visible Action: hai anh em (generic) tránh nhìn nhau
- Setting: không gian tổ chức giỗ (Production Fill: trong nhà hoặc nơi thờ cúng — 04B không xác định rõ hơn)
- Continuity In: — (nhân vật/gia đình mới) | Continuity Out: —
- Production Fills: quy mô mâm cỗ, số lượng khách, trang phục
- Forbidden Additions: không số lượng người cụ thể; không nội dung xung đột cụ thể (loại "câu nói cũ" không được nêu)
- Estimated Duration: 27.23s (00:08:02.308 → 00:08:29.538)

**S022**
- Covered Beat IDs: BEAT_030, BEAT_031 | Covered Obligation IDs: OBL_030, OBL_031 (DEDICATED_SHOT, NO_DEDICATED_VISUAL)
- Shot Function: DEVELOP
- Required Source Evidence: hành vi tưởng niệm mang tính phô diễn, đối lập ngầm với căng thẳng người sống
- Visual Subject: một người (generic) trước bàn thờ/di ảnh | One Visible Action: cử chỉ tưởng niệm mang tính trình diễn (trang trọng thái quá)
- Setting: unspecified
- Continuity In: — | Continuity Out: —
- Production Fills: không gian tưởng niệm, trang phục
- Forbidden Additions: không dựng "sân khấu" nghĩa đen (rạp hát, ánh đèn sân khấu) — đây là ẩn dụ hành vi, không phải địa điểm; không đặc tả nhân vật cụ thể
- Estimated Duration: 29.08s (00:08:29.538 → 00:08:58.615)

**S023**
- Covered Beat IDs: BEAT_032 | Covered Obligation IDs: OBL_032 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: 4 hành động chăm sóc (thay áo/đút cháo/đưa đi khám/lau vết đau); dấu hiệu mệt mỏi/căng thẳng
- Visual Subject: người chăm sóc (generic) và mẹ già | One Visible Action: đút cháo cho mẹ già (chọn 1 trong 4 hành động làm đại diện chính, theo quy tắc "một hành động đọc được"; 3 hành động còn lại được narration mang qua voiceover trong lúc hold)
- Setting: unspecified (Production Fill: không gian chăm sóc tại nhà)
- Continuity In: — (nhân vật mới) | Continuity Out: → S024 (cùng nhân vật)
- Production Fills: không gian, trang phục, đạo cụ chăm sóc (bát cháo, thìa)
- Forbidden Additions: không đặc tả bệnh cụ thể của mẹ già; không thêm chi tiết thời gian biểu ngoài 4 hành động đã nêu
- Estimated Duration: 36.92s (00:08:58.615 → 00:09:35.538)

**S024**
- Covered Beat IDs: BEAT_033 | Covered Obligation IDs: OBL_033 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: cùng người chăm sóc từ S023 | One Visible Action: (tĩnh) một khoảnh khắc dừng tay, thở ra nhẹ
- Setting: cùng S023
- Continuity In: ← S023 (character continuity cục bộ) | Continuity Out: —
- Production Fills: —
- Forbidden Additions: —
- Estimated Duration: 26.31s (00:09:35.538 → 00:10:01.846)

**S025**
- Covered Beat IDs: BEAT_034, BEAT_035 | Covered Obligation IDs: OBL_034, OBL_035 (DEDICATED_SHOT, NO_DEDICATED_VISUAL)
- Shot Function: DEVELOP
- Required Source Evidence: dấu hiệu căng thẳng/né tránh khi nghe nhắc "cha mẹ"
- Visual Subject: một người (generic, nhân vật mới) | One Visible Action: thần thái căng thẳng/né tránh khi nghe nhắc đến cha mẹ
- Setting: unspecified
- Continuity In: — | Continuity Out: —
- Production Fills: không gian, trang phục
- Forbidden Additions: không đặc tả chi tiết cụ thể của "bạo lực" quá khứ; không gán câu thoại "cha mẹ mà, bỏ qua đi" cho một nhân vật cha/mẹ xuất hiện trong khung hình
- Estimated Duration: 38.77s (00:10:01.846 → 00:10:40.615)

**S026**
- Covered Beat IDs: BEAT_036 | Covered Obligation IDs: OBL_036 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: hành vi giữ khoảng cách/đặt ranh giới giữa hai người chung chung
- Visual Subject: hai người (generic) | One Visible Action: một người lùi lại một bước, giữ khoảng cách bình tĩnh (không xung đột thể chất)
- Setting: unspecified
- Continuity In: S025 | Continuity Out: S027
- Production Fills: không gian, trang phục
- Forbidden Additions: không đặc tả nhân vật cụ thể hay lý do xung đột cụ thể
- Estimated Duration: 37.85s (00:10:40.615 → 00:11:18.462)
- **Ghi chú Phase C.1:** DEVELOP giữ khoảng cách/ranh giới (tách từ S018 cũ)

**S027**
- Covered Beat IDs: BEAT_037, BEAT_038 | Covered Obligation IDs: OBL_037, OBL_038 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: — (luận đề + 4 phân biệt, không evidence hình ảnh mới)
- Visual Subject: giữ khung S026 | One Visible Action: (tĩnh) hai người vẫn ở khoảng cách đã thiết lập, thần thái lắng lại
- Setting: cùng S026
- Continuity In: S026 | Continuity Out: S028
- Production Fills: —
- Forbidden Additions: không dựng cảnh cụ thể cho 4 phân biệt (biết ơn/tôn trọng/chăm sóc/tha thứ)
- Estimated Duration: 32.77s (00:11:18.462 → 00:11:51.231)
- **Ghi chú Phase C.1:** HOLD cùng khung, hệ quả + 4 phân biệt (tách từ S018 cũ)


---

## ACT IV

**S028**
- Covered Beat IDs: BEAT_039 | Covered Obligation IDs: OBL_039 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: hình ảnh ẩn dụ "ngọn đèn" (khẳng định) đối lập "cây roi" (phủ định)
- Visual Subject: một ngọn đèn nhỏ trong không gian tối dịu | One Visible Action: (tĩnh) ánh sáng đèn ổn định, không nhấp nháy
- Setting: unspecified
- Continuity In: — (đây là lần dùng độc lập thứ nhất của từ "đèn" — KHÔNG lập continuity thread với OBL_117/OBL_121, theo sửa đổi 04B) | Continuity Out: —
- Production Fills: kiểu dáng đèn, chất liệu, không gian xung quanh
- Forbidden Additions: không dựng cảnh đánh roi theo nghĩa đen (ẩn dụ bị phủ định); không thêm chi tiết đèn ngoài việc nó là "ngọn đèn" ổn định, ấm áp
- Estimated Duration: 22.62s (00:11:51.231 → 00:12:13.846)

**S029**
- Covered Beat IDs: BEAT_040 | Covered Obligation IDs: OBL_040 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: người con nắm tay cha khóc
- Visual Subject: người con, người cha (trên giường bệnh) | One Visible Action: nắm tay, khóc
- Setting: khoa hồi sức (Source Fact)
- Continuity In: — (mở đầu chuỗi 3 shot cục bộ, không phải thread episode) | Continuity Out: → S030 (cùng bối cảnh khoa hồi sức, khác nhân vật)
- Production Fills: nội thất phòng bệnh, trang phục bệnh nhân/người nhà
- Forbidden Additions: không đặt tên nhân vật; không đặc tả bệnh lý cụ thể
- Estimated Duration: 13.41s (00:12:13.846 → 00:12:27.254)

**S030**
- Covered Beat IDs: BEAT_040 | Covered Obligation IDs: OBL_040 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: người mẹ thở yếu vẫn hỏi con đã ăn gì
- Visual Subject: người mẹ (trên giường bệnh), người con | One Visible Action: hỏi (miệng cử động nhẹ, hướng mắt về con)
- Setting: khoa hồi sức, cùng bối cảnh S029
- Continuity In: ← S029 (cùng bối cảnh khoa hồi sức, location continuity cục bộ) | Continuity Out: → S031
- Production Fills: nội thất phòng bệnh
- Forbidden Additions: không hiển thị nội dung câu hỏi bằng chữ; không đặc tả bệnh lý
- Estimated Duration: 6.90s (00:12:27.254 → 00:12:34.149)

**S031**
- Covered Beat IDs: BEAT_040 | Covered Obligation IDs: OBL_040 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: người cha nghiêm khắc cả đời, phút cuối nói lời xin lỗi nhỏ
- Visual Subject: người cha lớn tuổi (trên giường bệnh) | One Visible Action: nói (khẽ, hướng về một người đứng cạnh)
- Setting: khoa hồi sức
- Continuity In: ← S030 | Continuity Out: → S032
- Production Fills: nội thất phòng bệnh
- Forbidden Additions: không hiển thị nội dung lời xin lỗi bằng chữ
- Estimated Duration: 8.81s (00:12:34.149 → 00:12:42.960)

**S032**
- Covered Beat IDs: BEAT_040 | Covered Obligation IDs: OBL_040 (DEDICATED_SHOT)
- Shot Function: HOLD
- Required Source Evidence: sự vắng mặt của một người không kịp đến (chỉ có thể ngụ ý, không hiển thị dương tính)
- Visual Subject: hành lang khoa hồi sức | One Visible Action: (tĩnh) hành lang vắng, không có người
- Setting: khoa hồi sức
- Continuity In: ← S031 | Continuity Out: → S033
- Production Fills: nội thất hành lang, ánh sáng
- Forbidden Additions: **không dùng hình ảnh "ghế trống" cho cảnh này** — dù chủ đề gần với motif chiếc ghế, đây KHÔNG phải continuity thread T1 và việc mượn hình ảnh ghế ở đây sẽ tạo một sự cộng hưởng ngoài ý định, gây nhầm lẫn continuity (đúng tinh thần chống scene-pool của yêu cầu Phase C — không tái dùng vật thể phụ chỉ vì nó "tiện"); chỉ dùng hành lang vắng, không thêm đồ vật biểu tượng nào
- Estimated Duration: 9.19s (00:12:42.960 → 00:12:52.154)

**S033**
- Covered Beat IDs: BEAT_041, BEAT_042 | Covered Obligation IDs: OBL_041, OBL_042 (NO_DEDICATED_VISUAL, DEDICATED_SHOT)
- Shot Function: REVEAL
- Required Source Evidence: chiếc ghế với dấu hiệu hao mòn/cũ đi theo thời gian
- Visual Subject: cùng chiếc ghế (thread T1) | One Visible Action: (tĩnh, chuỗi thời gian) lớp bụi dày thêm, màu gỗ phai nhẹ
- Setting: cùng không gian nhà (thread T1)
- Continuity In: ← S008 (cùng ghế, quay lại motif sau một khoảng episode dài — có chức năng narrative mới: đánh dấu thời gian trôi qua do 6 lý do bận rộn) | Continuity Out: → S047 (lần tái xuất kế tiếp)
- Production Fills: mức độ hao mòn cụ thể
- Forbidden Additions: không hiển thị riêng biệt 6 lý do bận bằng 6 cảnh khác nhau (04B xác nhận không có evidence hình ảnh cho từng lý do)
- Estimated Duration: 27.23s (00:12:52.154 → 00:13:19.385)

**S034**
- Covered Beat IDs: BEAT_043, BEAT_044 | Covered Obligation IDs: OBL_043, OBL_044 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: quay lại khung Đao Lợi (thread T2, mượn từ S009/S012) | One Visible Action: (tĩnh)
- Setting: Cung Trời Đao Lợi
- Continuity In: ← S017 (thread T2) | Continuity Out: → S035
- Production Fills: —
- Forbidden Additions: không thêm hành động/biểu cảm mới cho Đức Phật ngoài đã có
- Estimated Duration: 30.46s (00:13:19.385 → 00:13:49.846)

**S035**
- Covered Beat IDs: BEAT_045 | Covered Obligation IDs: OBL_045 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: mẹ, cha (2 trong 9 nhóm) — nguồn nâng đỡ gần nhất
- Visual Subject: mẹ và cha (generic, KHÔNG liên kết với mẹ/cha ở S002/S003 — 04B không xác nhận cùng nhân vật) | One Visible Action: hiện diện, không hành động cụ thể (chân dung tĩnh)
- Setting: unspecified
- Continuity In: — | Continuity Out: → S036
- Production Fills: trang phục, không gian
- Forbidden Additions: không đặc tả danh tính cụ thể
- Estimated Duration: 4.15s (00:13:49.846 → 00:13:54.000)

**S036**
- Covered Beat IDs: BEAT_045 | Covered Obligation IDs: OBL_045 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: người trồng lúa, người may áo, thầy cô — nhóm lao động/tri thức trực tiếp phục vụ đời sống
- Visual Subject: người trồng lúa (đại diện, 1 trong 3) | One Visible Action: đang làm việc trên đồng ruộng (đại diện cho cả nhóm; 2 vai trò còn lại mang bởi voiceover trong lúc hold ngắn, không dựng riêng để tránh nhồi shot)
- Setting: đồng ruộng (Production Fill)
- Continuity In: ← S035 | Continuity Out: → S037
- Production Fills: không gian đồng ruộng, trang phục lao động
- Forbidden Additions: không thêm nghề nghiệp nào ngoài 9 nhóm đã liệt kê ở 04A/04B
- Estimated Duration: 6.23s (00:13:54.000 → 00:14:00.231)

**S037**
- Covered Beat IDs: BEAT_045 | Covered Obligation IDs: OBL_045 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: hàng xóm, người xa lạ, bác sĩ, người quét đường — nhóm cộng đồng rộng hơn
- Visual Subject: người quét đường (đại diện, 1 trong 4) | One Visible Action: quét đường vào sáng sớm
- Setting: đường phố (Production Fill)
- Continuity In: ← S036 | Continuity Out: → S038
- Production Fills: không gian đường phố, trang phục lao động
- Forbidden Additions: không thêm nhóm người nào ngoài 9 nhóm đã liệt kê
- Estimated Duration: 24.23s (00:14:00.231 → 00:14:24.462)

**S038**
- Covered Beat IDs: BEAT_046, BEAT_047, BEAT_048 | Covered Obligation IDs: OBL_046, OBL_047, OBL_048 (NO_DEDICATED_VISUAL, DEDICATED_SHOT)
- Shot Function: CALLBACK
- Required Source Evidence: cùng chiếc ghế (thread T1), làm điểm neo cho ý "mở rộng lòng biết ơn"
- Visual Subject: cùng chiếc ghế | One Visible Action: (tĩnh) — không đổi so với S033
- Setting: cùng không gian nhà, thread T1
- Continuity In: ← S033 | Continuity Out: → S047
- Production Fills: —
- Forbidden Additions: không dựng cảnh đám đông "mọi chúng sinh"; không mô tả hình tướng Địa Tạng Bồ Tát (OBL_048 minh thị cấm)
- Estimated Duration: 45.23s (00:14:24.462 → 00:15:09.692)


---

## ACT V/VI

**S039**
- Covered Beat IDs: BEAT_049, BEAT_050 | Covered Obligation IDs: OBL_049, OBL_050 (DEDICATED_SHOT, NO_DEDICATED_VISUAL)
- Shot Function: DEVELOP
- Required Source Evidence: thần thái trắc ẩn hướng về gia đình (mẹ/cha) làm điểm khởi đầu của lòng từ bi mở rộng
- Visual Subject: một người (generic) | One Visible Action: thần thái trắc ẩn, ánh mắt hướng xa xăm
- Setting: unspecified
- Continuity In: — | Continuity Out: —
- Production Fills: không gian, trang phục
- Forbidden Additions: không dựng cảnh đám đông "mọi chúng sinh"; không mô tả chi tiết "đại nguyện" ngoài đã có
- Estimated Duration: 48.92s (00:15:09.692 → 00:15:58.615)

**S040**
- Covered Beat IDs: BEAT_051, BEAT_052 | Covered Obligation IDs: OBL_051, OBL_052 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ khung S039 | One Visible Action: (tĩnh)
- Setting: cùng S039
- Continuity In: ← S039 | Continuity Out: → S041
- Production Fills: —
- Forbidden Additions: không dựng cảnh cụ thể cho "chà đạp gia đình khác"/"bất công với người làm việc" — quá cụ thể so với 04B xác nhận
- Estimated Duration: 41.54s (00:15:58.615 → 00:16:40.154)

**S041**
- Covered Beat IDs: BEAT_053, BEAT_054, BEAT_055 | Covered Obligation IDs: OBL_053, OBL_054, OBL_055 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ khung S039 (kéo dài) | One Visible Action: (tĩnh)
- Setting: cùng S039
- Continuity In: ← S040 | Continuity Out: → S042
- Production Fills: —
- Forbidden Additions: —
- Estimated Duration: 30.92s (00:16:40.154 → 00:17:11.077)

**S042**
- Covered Beat IDs: BEAT_056, BEAT_057 | Covered Obligation IDs: OBL_056, OBL_057 (DEDICATED_SHOT, NO_DEDICATED_VISUAL)
- Shot Function: ESTABLISH
- Required Source Evidence: người cha la con; đứa trẻ cúi mặt xuống; biểu cảm nhận ra trên gương mặt cha (giữ nguyên qua BEAT_057 — 'vòng lặp vẫn quay' không có evidence riêng, mang bằng giữ nguyên khung căng thẳng)
- Visual Subject: người cha, con | One Visible Action: la con, đứa trẻ cúi mặt (một hành động-phản ứng liên tục, đọc được trong một nhịp)
- Setting: unspecified (Production Fill: không gian nhà đơn giản)
- Continuity In: S041 (mở đầu thread T3) | Continuity Out: S043
- Production Fills: không gian, trang phục
- Forbidden Additions: không đặt tên nhân vật; không mô tả hành vi bạo lực thể chất; không hiển thị "đứa trẻ trong quá khứ" như nhân vật riêng cùng khung hình; không dựng biểu tượng 'vòng lặp' (vòng tròn...) cho phần BEAT_057 vừa sáp nhập
- Estimated Duration: 36.92s (00:17:11.077 → 00:17:48.000)
- **Ghi chú Phase C.1:** sáp nhập S034 cũ (short-shot resolution: MERGE_WITH_NEIGHBOR)

**S043**
- Covered Beat IDs: BEAT_058 | Covered Obligation IDs: OBL_058 (DEDICATED_SHOT)
- Shot Function: REVEAL
- Required Source Evidence: khoảnh khắc "dừng lại" — thay đổi tư thế/biểu cảm
- Visual Subject: cùng người cha (T3) | One Visible Action: dừng lại (chuyển từ căng thẳng sang tĩnh lặng)
- Setting: cùng S042
- Continuity In: ← S042 (T3) | Continuity Out: → S044
- Production Fills: —
- Forbidden Additions: không mô tả nguyên nhân cụ thể khiến ông dừng lại
- Estimated Duration: 3.23s (00:17:48.000 → 00:17:51.231)

**S044**
- Covered Beat IDs: BEAT_059 | Covered Obligation IDs: OBL_059 (DEDICATED_SHOT)
- Shot Function: RESOLUTION
- Required Source Evidence: người cha quỳ xuống trước con; đang nói (câu nguyên văn)
- Visual Subject: người cha, con (T3) | One Visible Action: quỳ xuống, nói với con
- Setting: cùng S042–S043
- Continuity In: ← S043 (T3) | Continuity Out: → S045
- Production Fills: —
- Forbidden Additions: không đổi/diễn giải lại câu thoại; không thêm phản ứng của con
- Estimated Duration: 27.23s (00:17:51.231 → 00:18:18.462)

**S045**
- Covered Beat IDs: BEAT_060, BEAT_061 | Covered Obligation IDs: OBL_060, OBL_061 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ khung S044 (T3) | One Visible Action: (tĩnh, khoảnh khắc sau lời xin lỗi)
- Setting: cùng S044
- Continuity In: ← S044 (T3) | Continuity Out: —
- Production Fills: —
- Forbidden Additions: —
- Estimated Duration: 18.92s (00:18:18.462 → 00:18:37.385)

**S046**
- Covered Beat IDs: BEAT_062 | Covered Obligation IDs: OBL_062 (DEDICATED_SHOT)
- Shot Function: CONTRAST
- Required Source Evidence: hình ảnh ẩn dụ bàn thờ/nén hương (bị phủ định vị trí); một khoảnh khắc "dừng lại" chung chung
- Visual Subject: một người (generic — **KHÔNG phải người cha ở T3**, theo đúng sửa đổi 04B) | One Visible Action: bàn tay dừng lại giữa chừng (đại diện chung cho 6 hành động "dừng", không dựng riêng từng hành động)
- Setting: unspecified (Production Fill: có thể thoáng qua một góc bàn thờ ở hậu cảnh làm điểm đối chiếu bị phủ định, không phải trọng tâm)
- Continuity In: — (chủ thể mới, không nối thread T3) | Continuity Out: —
- Production Fills: không gian, trang phục, chi tiết bàn thờ hậu cảnh
- Forbidden Additions: **không mặc định đây là cùng người cha của S042–S044** — ràng buộc minh thị kế thừa từ 04B; không thêm hành động "dừng" nào ngoài phạm vi ý nghĩa chung đã nêu
- Estimated Duration: 32.77s (00:18:37.385 → 00:19:10.154)

**S047**
- Covered Beat IDs: BEAT_063 | Covered Obligation IDs: OBL_063 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ khung S046 | One Visible Action: (tĩnh)
- Setting: cùng S046
- Continuity In: ← S046 | Continuity Out: → S048
- Production Fills: —
- Forbidden Additions: không thể hiện Đức Phật đang kể câu chuyện S042–S046 như một sự kiện kinh điển — ràng buộc disclaimer áp dụng ngược cho toàn bộ S042-038
- Estimated Duration: 13.38s (00:19:10.154 → 00:19:23.539)


---

## ACT VII

**S048**
- Covered Beat IDs: BEAT_064 | Covered Obligation IDs: OBL_064 (DEDICATED_SHOT)
- Shot Function: ESTABLISH
- Required Source Evidence: khoảnh khắc bữa cơm — lời nói được nói ra, một đứa trẻ tiếp nhận
- Visual Subject: một gia đình tại bữa cơm (generic, mới — không nối T3) | One Visible Action: một người lớn nói, một đứa trẻ lắng nghe/tiếp nhận
- Setting: bữa cơm tối nay (Source Fact)
- Continuity In: — | Continuity Out: —
- Production Fills: không gian bếp/bàn ăn, món ăn, trang phục
- Forbidden Additions: không tách rời chuỗi 5 bước nhân quả thành cảnh riêng; không nhân vật cụ thể có tên; không hiển thị "20 năm sau" bằng nhân vật trưởng thành cụ thể
- Estimated Duration: 30.46s (00:19:23.539 → 00:19:54.000)

**S049**
- Covered Beat IDs: BEAT_065 | Covered Obligation IDs: OBL_065 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: nhắn tin (1/6 hành vi — "nghe điện thoại" chuyển sang mang bằng giọng đọc, xem sửa lỗi bên dưới)
- Visual Subject: một người (generic) | One Visible Action: gõ tin nhắn trên điện thoại
- Setting: unspecified
- Continuity In: — | Continuity Out: → S050
- Production Fills: không gian, trang phục
- Forbidden Additions: không hiển thị nội dung tin nhắn bằng chữ
- Estimated Duration: 7.85s (00:19:54.000 → 00:20:01.846)

**S050**
- Covered Beat IDs: BEAT_065 | Covered Obligation IDs: OBL_065 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: đặt ranh giới (1/6 hành vi — "chăm sóc người già" chuyển sang mang bằng giọng đọc, xem sửa lỗi bên dưới)
- Visual Subject: một người (generic) | One Visible Action: một cử chỉ đặt ranh giới bình tĩnh (tay giơ nhẹ, giữ khoảng cách)
- Setting: unspecified
- Continuity In: ← S049 | Continuity Out: → S051
- Production Fills: không gian, trang phục
- Forbidden Additions: None thêm.
- Estimated Duration: 7.62s (00:20:01.846 → 00:20:09.462)

**S051**
- Covered Beat IDs: BEAT_065 | Covered Obligation IDs: OBL_065 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: nuôi dạy con; nói lời xin lỗi
- Visual Subject: một người lớn và một đứa trẻ (generic) | One Visible Action: cúi xuống ngang tầm mắt trẻ, nói lời xin lỗi
- Setting: unspecified
- Continuity In: ← S050 | Continuity Out: —
- Production Fills: không gian, trang phục
- Forbidden Additions: không thêm hành vi nào ngoài 6 hành vi đã liệt kê ở 04A/04B
- Estimated Duration: 7.62s (00:20:09.462 → 00:20:17.077)

**S052**
- Covered Beat IDs: BEAT_066 | Covered Obligation IDs: OBL_066 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: hành vi chăm sóc người già khác (cử chỉ ấm áp); dấu hiệu ân hận (thần thái trầm lặng) làm điểm khởi đầu
- Visual Subject: một người (generic, mới) và một người già khác | One Visible Action: chăm sóc một người già không phải cha mẹ ruột (cử chỉ ấm áp)
- Setting: unspecified
- Continuity In: S051 | Continuity Out: S053
- Production Fills: không gian, trang phục
- Forbidden Additions: None thêm ngoài phạm vi đã liệt kê
- Estimated Duration: 42.46s (00:20:17.077 → 00:20:59.539)
- **Ghi chú Phase C.1:** DEVELOP chăm sóc người già khác (tách từ S044 cũ)

**S053**
- Covered Beat IDs: BEAT_067, BEAT_068 | Covered Obligation IDs: OBL_067, OBL_068 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: — (2 luận đề khẳng định, không evidence hình ảnh mới)
- Visual Subject: giữ khung S052 | One Visible Action: (tĩnh) giữ nguyên cử chỉ chăm sóc, lắng lại
- Setting: cùng S052
- Continuity In: S052 | Continuity Out: S054
- Production Fills: —
- Forbidden Additions: None thêm
- Estimated Duration: 16.62s (00:20:59.539 → 00:21:16.154)
- **Ghi chú Phase C.1:** HOLD cùng khung, 2 luận đề khép (tách từ S044 cũ)

**S054**
- Covered Beat IDs: BEAT_069, BEAT_070 | Covered Obligation IDs: OBL_069, OBL_070 (NO_DEDICATED_VISUAL, DEDICATED_SHOT)
- Shot Function: ESTABLISH
- Required Source Evidence: hành vi tụng kinh (đại diện cho 4 thực hành: tụng kinh/làm phước/hồi hướng/tưởng niệm)
- Visual Subject: một người (generic) | One Visible Action: tụng kinh (tư thế ngồi, tay chắp — đại diện; 3 thực hành còn lại mang bằng giọng đọc)
- Setting: unspecified (Production Fill: không gian tu tập đơn giản)
- Continuity In: — | Continuity Out: —
- Production Fills: không gian, trang phục, đạo cụ tối thiểu (không đặc tả tượng Phật/kiến trúc chùa cụ thể nếu 04B không xác nhận)
- Forbidden Additions: không mô tả không gian "chùa" cụ thể — 04B minh thị cấm; không tự thêm địa điểm chùa nếu narration không nêu
- Estimated Duration: 30.92s (00:21:16.154 → 00:21:47.077)


---

## ACT VIII

**S055**
- Covered Beat IDs: BEAT_071, BEAT_072 | Covered Obligation IDs: OBL_071, OBL_072 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ khung S054 | One Visible Action: (tĩnh)
- Setting: cùng S054
- Continuity In: ← S054 | Continuity Out: → S056
- Production Fills: —
- Forbidden Additions: không dựng cảnh minh hoạ "bán sợ hãi"/"nghi lễ như cái máy" — hành vi bị phê phán, không hình ảnh hoá dương tính
- Estimated Duration: 41.08s (00:21:47.077 → 00:22:28.154)

**S056**
- Covered Beat IDs: BEAT_073 | Covered Obligation IDs: OBL_073 (DEDICATED_SHOT)
- Shot Function: CONTRAST
- Required Source Evidence: người nghèo thắp một nén hương với tâm lành
- Visual Subject: một người (rõ ràng đơn sơ, không phô trương) | One Visible Action: thắp một nén hương đơn lẻ
- Setting: unspecified (Production Fill: không gian đơn sơ, đối lập rõ với S021 — buổi giỗ phô trương)
- Continuity In: — | Continuity Out: → S057
- Production Fills: không gian, trang phục đơn sơ
- Forbidden Additions: không dựng bàn thờ lớn — narration minh thị đối lập với sự phô trương
- Estimated Duration: 12.72s (00:22:28.154 → 00:22:40.874)

**S057**
- Covered Beat IDs: BEAT_073 | Covered Obligation IDs: OBL_073 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: người chăm mẹ còn sống bằng bữa cơm ấm/đưa đi khám/trò chuyện; người kiềm chế không biến vết thương thành bạo lực với con
- Visual Subject: một người (generic, mới) và mẹ còn sống | One Visible Action: dọn một bữa cơm ấm cho mẹ (đại diện cho cụm ví dụ 2; ví dụ 3 — kiềm chế — mang bởi sắc thái điềm tĩnh của cùng shot, không dựng riêng vì là trạng thái nội tâm)
- Setting: unspecified
- Continuity In: ← S056 (liền kề chủ đề, không phải continuity nhân vật — 2 nhân vật khác nhau trong cùng ví dụ nhóm 3 trường hợp) | Continuity Out: —
- Production Fills: không gian bếp, món ăn
- Forbidden Additions: không thêm ví dụ thứ 4; không đặc tả danh tính cụ thể
- Estimated Duration: 36.20s (00:22:40.874 → 00:23:17.077)

**S058**
- Covered Beat IDs: BEAT_074, BEAT_075 | Covered Obligation IDs: OBL_074, OBL_075 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ khung S057 | One Visible Action: (tĩnh)
- Setting: cùng S057
- Continuity In: ← S057 | Continuity Out: → S059
- Production Fills: —
- Forbidden Additions: —
- Estimated Duration: 30.92s (00:23:17.077 → 00:23:48.000)


---

## ACT IX

**S059**
- Covered Beat IDs: BEAT_076 | Covered Obligation IDs: OBL_076 (DEDICATED_SHOT)
- Shot Function: CALLBACK
- Required Source Evidence: pháp hội tại Cung Trời Đao Lợi (thread T2)
- Visual Subject: cùng khung Đao Lợi (T2, mượn từ S009/S012-S017) | One Visible Action: (tĩnh, chức năng mới: hình ảnh tổng kết) — không phải thiết lập lần đầu
- Setting: Cung Trời Đao Lợi, thread T2
- Continuity In: S058 | Continuity Out: S060
- Production Fills: —
- Forbidden Additions: không dựng cảnh riêng cho 'đại nguyện của Địa Tạng'; không tự vẽ hình ảnh địa ngục
- Estimated Duration: 24.00s (00:23:48.000 → 00:24:12.000)
- **Ghi chú Phase C.1:** CALLBACK khung Đao Lợi (T2) (tách từ S050 cũ)

**S060**
- Covered Beat IDs: BEAT_077, BEAT_078 | Covered Obligation IDs: OBL_077, OBL_078 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: — (luận đề + câu hỏi tu từ khép đoạn, không evidence hình ảnh mới)
- Visual Subject: giữ khung S059 (T2) | One Visible Action: (tĩnh) giữ nguyên khung Đao Lợi
- Setting: Cung Trời Đao Lợi, thread T2
- Continuity In: S059 (T2) | Continuity Out: S061
- Production Fills: —
- Forbidden Additions: không tự vẽ hình ảnh địa ngục ở beat này
- Estimated Duration: 33.69s (00:24:12.000 → 00:24:45.692)
- **Ghi chú Phase C.1:** HOLD cùng khung, luận đề khép + câu hỏi (tách từ S050 cũ)

**S061**
- Covered Beat IDs: BEAT_079 | Covered Obligation IDs: OBL_079 (NO_DEDICATED_VISUAL)
- Shot Function: TRANSITION
- Required Source Evidence: —
- Visual Subject: — (bắc cầu sang chuỗi thực hành nhỏ) | One Visible Action: —
- Setting: —
- Continuity In: ← S060 | Continuity Out: → S062
- Production Fills: —
- Forbidden Additions: không mô tả hình tướng Địa Tạng Bồ Tát
- Estimated Duration: 30.46s (00:24:45.692 → 00:25:16.154)

**S062**
- Covered Beat IDs: BEAT_080 | Covered Obligation IDs: OBL_080 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: thực hành nhỏ 1/6: hành vi thực hiện một cuộc gọi điện thoại, không vội vàng (tư thế thư thái)
- Visual Subject: một người | One Visible Action: gọi điện, tư thế thư thái
- Setting: unspecified
- Continuity In: — | Continuity Out: →S063 (chuỗi liền mạch cùng chủ đề "thực hành nhỏ", không phải continuity nhân vật)
- Production Fills: không gian
- Forbidden Additions: không đặc tả người gọi/nhận cụ thể
- Estimated Duration: 5.08s (00:25:16.154 → 00:25:21.231)

**S063**
- Covered Beat IDs: BEAT_081 | Covered Obligation IDs: OBL_081 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: thực hành nhỏ 2/6: hành vi dùng bữa với thần thái điềm tĩnh (không cáu gắt)
- Visual Subject: một gia đình (generic) | One Visible Action: dùng bữa, thần thái điềm tĩnh
- Setting: unspecified
- Continuity In: ←S062 | Continuity Out: →S064
- Production Fills: món ăn, không gian
- Forbidden Additions: None thêm.
- Estimated Duration: 2.77s (00:25:21.231 → 00:25:24.000)

**S064**
- Covered Beat IDs: BEAT_082 | Covered Obligation IDs: OBL_082 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: thực hành nhỏ 3/6: hành vi chủ động xin lỗi (cử chỉ/tư thế hướng về đối phương)
- Visual Subject: một người | One Visible Action: cử chỉ chủ động xin lỗi
- Setting: unspecified
- Continuity In: ←S063 | Continuity Out: →S065
- Production Fills: không gian
- Forbidden Additions: None thêm.
- Estimated Duration: 5.08s (00:25:24.000 → 00:25:29.077)

**S065**
- Covered Beat IDs: BEAT_083 | Covered Obligation IDs: OBL_083 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: thực hành nhỏ 4/6: hành vi nói với thần thái/tư thế bình tĩnh, không căng thẳng
- Visual Subject: một người | One Visible Action: nói với thần thái bình tĩnh (đặt ranh giới)
- Setting: unspecified
- Continuity In: ←S064 | Continuity Out: →S066
- Production Fills: không gian
- Forbidden Additions: None thêm.
- Estimated Duration: 4.15s (00:25:29.077 → 00:25:33.231)

**S066**
- Covered Beat IDs: BEAT_084 | Covered Obligation IDs: OBL_084 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: thực hành nhỏ 5/6: hành vi tìm kiếm/tiếp nhận sự giúp đỡ (một trong ba hình thức: trị liệu/tu học/giúp đỡ)
- Visual Subject: một người | One Visible Action: bước vào một không gian hỗ trợ (trị liệu/tu học — không xác định hình thức cụ thể)
- Setting: unspecified
- Continuity In: ←S065 | Continuity Out: →S067
- Production Fills: không gian (không xác định loại hình cụ thể)
- Forbidden Additions: không xác định hình thức trị liệu/tu học cụ thể
- Estimated Duration: 12.46s (00:25:33.231 → 00:25:45.692)

**S067**
- Covered Beat IDs: BEAT_085 | Covered Obligation IDs: OBL_085 (DEDICATED_SHOT)
- Shot Function: CALLBACK
- Required Source Evidence: thực hành nhỏ 6/6, Critical: hành vi nhìn vào chiếc ghế; câu hỏi nội tâm không hiển thị trực tiếp
- Visual Subject: cùng chiếc ghế (T1) + một người | One Visible Action: nhìn vào chiếc ghế
- Setting: cùng không gian nhà, thread T1
- Continuity In: ←S038 (T1, callback thứ năm) | Continuity Out: →S068
- Production Fills: không gian (kế thừa T1)
- Forbidden Additions: None thêm ngoài ràng buộc T1.
- Estimated Duration: 13.85s (00:25:45.692 → 00:25:59.539)

**S068**
- Covered Beat IDs: BEAT_086 | Covered Obligation IDs: OBL_086 (NO_DEDICATED_VISUAL)
- Shot Function: TRANSITION
- Required Source Evidence: —
- Visual Subject: — | One Visible Action: —
- Setting: —
- Continuity In: ← S067 | Continuity Out: → S069
- Production Fills: —
- Forbidden Additions: —
- Estimated Duration: 12.46s (00:25:59.539 → 00:26:12.000)


---

## ACT X

**S069**
- Covered Beat IDs: BEAT_087 | Covered Obligation IDs: OBL_087 (DEDICATED_SHOT)
- Shot Function: ESTABLISH
- Required Source Evidence: mẹ biết bếp còn gì, cha sửa bóng đèn/vá cửa (hồi tưởng thời trẻ — hình ảnh cha mẹ "luôn ở đó")
- Visual Subject: mẹ, cha (generic, nhân vật mới — không nối các mẹ/cha khác trong episode) | One Visible Action: cha đang sửa một bóng đèn (đại diện; mẹ biết bếp còn gì mang bằng giọng đọc)
- Setting: unspecified (không gian nhà)
- Continuity In: — | Continuity Out: → S070
- Production Fills: không gian, trang phục, dụng cụ sửa chữa
- Forbidden Additions: không đặc tả bệnh lý
- Estimated Duration: 20.68s (00:26:12.000 → 00:26:32.677)

**S070**
- Covered Beat IDs: BEAT_087 | Covered Obligation IDs: OBL_087 (DEDICATED_SHOT)
- Shot Function: REVEAL
- Required Source Evidence: 3 dấu hiệu suy yếu hiện tại (hỏi lại nhiều lần/không nghe rõ/tay run khi cầm chén)
- Visual Subject: cùng mẹ/cha, nay lớn tuổi hơn (location continuity cục bộ, cùng ví dụ) | One Visible Action: tay run khi cầm chén (đại diện rõ nhất cho 3 dấu hiệu; 2 dấu hiệu còn lại mang bằng giọng đọc)
- Setting: cùng không gian nhà
- Continuity In: ← S069 (cùng ví dụ, khác lớp thời gian) | Continuity Out: → S071
- Production Fills: không gian, trang phục
- Forbidden Additions: không đặc tả bệnh lý cụ thể (không tên bệnh)
- Estimated Duration: 31.02s (00:26:32.677 → 00:27:03.692)

**S071**
- Covered Beat IDs: BEAT_088, BEAT_089 | Covered Obligation IDs: OBL_088, OBL_089 (NO_DEDICATED_VISUAL, DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: một bữa cơm không lạnh nhạt (1 trong 3 ví dụ "tỉnh lại")
- Visual Subject: một gia đình (generic) | One Visible Action: dùng bữa cơm ấm áp (2 ví dụ còn lại — cuộc gọi cuối tuần, nghe chuyện cũ kiên nhẫn — mang bằng giọng đọc)
- Setting: unspecified
- Continuity In: — | Continuity Out: —
- Production Fills: không gian bếp, món ăn
- Forbidden Additions: không dựng hình ảnh "cuộc đua"/đồng hồ đếm ngược cho OBL_088
- Estimated Duration: 49.85s (00:27:03.692 → 00:27:53.539)

**S072**
- Covered Beat IDs: BEAT_090, BEAT_091 | Covered Obligation IDs: OBL_090, OBL_091 (NO_DEDICATED_VISUAL, DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: gọi điện với thái độ chăm chú lắng nghe
- Visual Subject: một người (ở xa, generic) | One Visible Action: gọi điện, chăm chú lắng nghe (2 tương tác còn lại — gửi tiền kèm hỏi han, đưa cha đi khám — mang bằng giọng đọc)
- Setting: unspecified
- Continuity In: — | Continuity Out: —
- Production Fills: không gian, trang phục
- Forbidden Additions: không đặc tả quốc gia/địa điểm cụ thể cho "ở nước ngoài"
- Estimated Duration: 46.62s (00:27:53.539 → 00:28:40.154)

**S073**
- Covered Beat IDs: BEAT_092, BEAT_093 | Covered Obligation IDs: OBL_092, OBL_093 (DEDICATED_SHOT, NO_DEDICATED_VISUAL)
- Shot Function: CONTRAST
- Required Source Evidence: thần thái cô đơn/thiếu kết nối của cha mẹ dù được chu cấp đầy đủ vật chất
- Visual Subject: cha mẹ (generic, mới) | One Visible Action: ngồi cạnh những món đồ đầy đủ (thuốc, quà) nhưng thần thái trống trải
- Setting: unspecified
- Continuity In: — | Continuity Out: —
- Production Fills: không gian, đạo cụ vật chất (thuốc, quà)
- Forbidden Additions: None thêm.
- Estimated Duration: 41.08s (00:28:40.154 → 00:29:21.231)

**S074**
- Covered Beat IDs: BEAT_094 | Covered Obligation IDs: OBL_094 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: 1 trong 4 hoạt động chăm sóc (chọn đại diện: thay thuốc buổi tối)
- Visual Subject: người chăm sóc, mẹ (bệnh) | One Visible Action: thay thuốc cho mẹ
- Setting: tại nhà (Production Fill; 3 hoạt động còn lại — đi làm/nấu ăn/thức đêm — mang bằng giọng đọc theo trình tự)
- Continuity In: — | Continuity Out: → S075 (cùng nhân vật, chuyển không gian)
- Production Fills: không gian, trang phục, đạo cụ y tế tối thiểu
- Forbidden Additions: không đặc tả bệnh cụ thể của mẹ; không đặt tên nhân vật
- Estimated Duration: 15.14s (00:29:21.231 → 00:29:36.369)

**S075**
- Covered Beat IDs: BEAT_094 | Covered Obligation IDs: OBL_094 (DEDICATED_SHOT)
- Shot Function: REVEAL
- Required Source Evidence: khóc trong nhà tắm, nước chảy thật nhỏ (chi tiết cụ thể narration nêu); ý nghĩ thoáng qua (chỉ ngụ ý qua biểu cảm)
- Visual Subject: cùng người chăm sóc (character continuity cục bộ với S074) | One Visible Action: khóc lặng lẽ, vặn vòi nước thật nhỏ
- Setting: nhà tắm (Source Fact — địa điểm cụ thể narration nêu)
- Continuity In: ← S074 (cùng nhân vật, location continuity cục bộ: từ không gian chăm sóc chung sang nhà tắm riêng) | Continuity Out: —
- Production Fills: nội thất nhà tắm
- Forbidden Additions: không hiển thị lời khen "con hiếu quá" bằng một nhân vật khác xuất hiện đồng thời trong khung hình — đây là nhận xét từ một thời điểm/góc nhìn khác theo narration
- Estimated Duration: 22.71s (00:29:36.369 → 00:29:59.077)

**S076**
- Covered Beat IDs: BEAT_095, BEAT_096 | Covered Obligation IDs: OBL_095, OBL_096 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ khung S075 | One Visible Action: (tĩnh, khoảnh khắc lấy lại bình tĩnh)
- Setting: cùng S075
- Continuity In: ← S075 | Continuity Out: → S077
- Production Fills: —
- Forbidden Additions: —
- Estimated Duration: 37.38s (00:29:59.077 → 00:30:36.462)


---

## ACT XI

**S077**
- Covered Beat IDs: BEAT_097, BEAT_098 | Covered Obligation IDs: OBL_097, OBL_098 (NO_DEDICATED_VISUAL)
- Shot Function: TRANSITION
- Required Source Evidence: —
- Visual Subject: — | One Visible Action: —
- Setting: —
- Continuity In: ← S076 | Continuity Out: → S078
- Production Fills: —
- Forbidden Additions: —
- Estimated Duration: 36.00s (00:30:36.462 → 00:31:12.462)

**S078**
- Covered Beat IDs: BEAT_099 | Covered Obligation IDs: OBL_099 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: phản ứng căng cứng cơ thể khi nghe chuông điện thoại cha mẹ
- Visual Subject: một người (generic, mới) | One Visible Action: căng cứng/né tránh khi điện thoại reo
- Setting: unspecified
- Continuity In: — | Continuity Out: —
- Production Fills: không gian, trang phục
- Forbidden Additions: không đặc tả hình thức nhục mạ/kiểm soát cụ thể; không hình ảnh hoá câu thoại "hãy về đi, cha mẹ mà" bằng một nhân vật đang nói câu này
- Estimated Duration: 36.46s (00:31:12.462 → 00:31:48.923)

**S079**
- Covered Beat IDs: BEAT_100, BEAT_101 | Covered Obligation IDs: OBL_100, OBL_101 (NO_DEDICATED_VISUAL, DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: một khoảng cách vật lý giữa hai người chung chung; tư thế cầu nguyện thầm lặng
- Visual Subject: hai người (generic) | One Visible Action: giữ khoảng cách, một người trong tư thế lặng lẽ (cầu nguyện thầm)
- Setting: unspecified
- Continuity In: — | Continuity Out: —
- Production Fills: không gian, trang phục
- Forbidden Additions: không đặc tả nhân vật cụ thể hay lý do xung đột cụ thể
- Estimated Duration: 43.85s (00:31:48.923 → 00:32:32.769)

**S080**
- Covered Beat IDs: BEAT_102, BEAT_103 | Covered Obligation IDs: OBL_102, OBL_103 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ khung S079 | One Visible Action: (tĩnh)
- Setting: cùng S079
- Continuity In: ← S079 | Continuity Out: → S081
- Production Fills: —
- Forbidden Additions: —
- Estimated Duration: 27.69s (00:32:32.769 → 00:33:00.462)

**S081**
- Covered Beat IDs: BEAT_104, BEAT_105 | Covered Obligation IDs: OBL_104, OBL_105 (NO_DEDICATED_VISUAL, DEDICATED_SHOT)
- Shot Function: CONTRAST
- Required Source Evidence: cử chỉ cha xin lỗi con; cử chỉ mẹ lắng nghe con
- Visual Subject: cha, mẹ, con (generic, mới) | One Visible Action: cha cúi đầu xin lỗi con (đại diện; cử chỉ mẹ lắng nghe mang bằng giọng đọc hoặc một shot rất ngắn nối tiếp nếu nhịp cho phép — ở đây giữ 1 hành động chính theo đúng quy tắc)
- Setting: unspecified
- Continuity In: — | Continuity Out: —
- Production Fills: không gian, trang phục
- Forbidden Additions: None thêm.
- Estimated Duration: 48.00s (00:33:00.462 → 00:33:48.462)

**S082**
- Covered Beat IDs: BEAT_106 | Covered Obligation IDs: OBL_106 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ khung S081 | One Visible Action: (tĩnh, im lặng kéo dài)
- Setting: cùng S081
- Continuity In: ← S081 | Continuity Out: → S083
- Production Fills: —
- Forbidden Additions: không đổi/diễn giải lại 2 câu thoại nguyên văn nếu được trích dẫn
- Estimated Duration: 18.46s (00:33:48.462 → 00:34:06.923)


---

## ACT XII

**S083**
- Covered Beat IDs: BEAT_107 | Covered Obligation IDs: OBL_107 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: khoảnh khắc kiềm chế cơn giận (tư thế/biểu cảm dừng lại)
- Visual Subject: cha hoặc mẹ (generic) | One Visible Action: tay dừng giữa chừng trước một cử chỉ giận dữ, hít thở, buông xuống
- Setting: unspecified
- Continuity In: — | Continuity Out: —
- Production Fills: không gian, trang phục
- Forbidden Additions: None thêm.
- Estimated Duration: 34.15s (00:34:06.923 → 00:34:41.077)

**S084**
- Covered Beat IDs: BEAT_108, BEAT_109 | Covered Obligation IDs: OBL_108, OBL_109 (DEDICATED_SHOT, NO_DEDICATED_VISUAL)
- Shot Function: CONTRAST
- Required Source Evidence: hình ảnh ẩn dụ "căn nhà" ở trạng thái bất hoà (KHÔNG phải cảnh giới siêu hình)
- Visual Subject: một căn nhà, các thành viên gia đình generic | One Visible Action: mỗi người ngồi một góc, không ai nhìn ai (căng thẳng lặng lẽ)
- Setting: một căn nhà (Production Fill: nội thất cụ thể)
- Continuity In: — (liên kết chủ đề, không phải continuity chính thức, với S085 kế tiếp) | Continuity Out: → S085
- Production Fills: nội thất, trang phục
- Forbidden Additions: **không thể hiện "địa ngục" bằng biểu tượng tôn giáo/siêu nhiên (lửa, quỷ, hình phạt...)** — ràng buộc minh thị kế thừa từ 04A/04B
- Estimated Duration: 36.92s (00:34:41.077 → 00:35:18.000)

**S085**
- Covered Beat IDs: BEAT_110 | Covered Obligation IDs: OBL_110 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: hình ảnh 1-2/5: căn nhà không ai chịu nghe ai; bàn ăn mỗi người cầm một nỗi giận
- Visual Subject: một gia đình tại bàn ăn (generic) | One Visible Action: im lặng căng thẳng tại bàn ăn (gộp 2 hình ảnh đầu vì cùng bối cảnh bàn ăn, không nhồi thêm hành động khác)
- Setting: bàn ăn trong một căn nhà
- Continuity In: ← S084 (liên kết chủ đề "địa ngục hiện đại") | Continuity Out: → S086
- Production Fills: không gian, món ăn, trang phục
- Forbidden Additions: không biểu tượng tôn giáo/siêu nhiên
- Estimated Duration: 19.85s (00:35:18.000 → 00:35:37.846)

**S086**
- Covered Beat IDs: BEAT_110 | Covered Obligation IDs: OBL_110 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: hình ảnh 3/5: căn phòng có mẹ già nằm đó nhưng con tranh phần thiệt hơn
- Visual Subject: mẹ già (nằm), các con (generic) | One Visible Action: hai người con tranh cãi ở góc phòng, mẹ già nằm yên
- Setting: một căn phòng
- Continuity In: ← S085 | Continuity Out: → S087
- Production Fills: nội thất phòng
- Forbidden Additions: không biểu tượng tôn giáo/siêu nhiên
- Estimated Duration: 7.14s (00:35:37.846 → 00:35:44.991)

**S087**
- Covered Beat IDs: BEAT_110 | Covered Obligation IDs: OBL_110 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: hình ảnh 4-5/5: đứa trẻ học tình thương có điều kiện; người lớn không biết ôm con
- Visual Subject: một người lớn, một đứa trẻ (generic) | One Visible Action: người lớn đứng cứng đờ trước đứa trẻ đang chờ một cái ôm, không tiến lại gần (gộp 2 hình ảnh vì cùng biểu đạt một khoảnh khắc)
- Setting: unspecified
- Continuity In: ← S086 | Continuity Out: → S088
- Production Fills: không gian, trang phục
- Forbidden Additions: không biểu tượng tôn giáo/siêu nhiên
- Estimated Duration: 12.70s (00:35:44.991 → 00:35:57.692)

**S088**
- Covered Beat IDs: BEAT_111 | Covered Obligation IDs: OBL_111 (NO_DEDICATED_VISUAL)
- Shot Function: TRANSITION
- Required Source Evidence: —
- Visual Subject: — | One Visible Action: —
- Setting: —
- Continuity In: ← S087 | Continuity Out: → S089
- Production Fills: —
- Forbidden Additions: không biểu tượng tôn giáo/siêu nhiên cho "địa ngục"/"cõi lành"
- Estimated Duration: 12.46s (00:35:57.692 → 00:36:10.154)

**S089**
- Covered Beat IDs: BEAT_112 | Covered Obligation IDs: OBL_112 (DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: khoảnh khắc kiềm chế/dừng lại trước một hành vi tiêu cực
- Visual Subject: một người (generic, mới) | One Visible Action: tay dừng giữa chừng trước một cử chỉ (không hiển thị hành vi tiêu cực đang xảy ra, chỉ hiển thị khoảnh khắc TRƯỚC nó)
- Setting: unspecified
- Continuity In: — | Continuity Out: —
- Production Fills: không gian, trang phục
- Forbidden Additions: không thêm hành vi nào ngoài 5 hành vi đã liệt kê; không hiển thị hành vi tiêu cực dương tính (không cảnh đang tát, đang so sánh...)
- Estimated Duration: 25.38s (00:36:10.154 → 00:36:35.539)

**S090**
- Covered Beat IDs: BEAT_113 | Covered Obligation IDs: OBL_113 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ khung S089 | One Visible Action: (tĩnh)
- Setting: cùng S089
- Continuity In: ← S089 | Continuity Out: → S091
- Production Fills: —
- Forbidden Additions: không dựng hình ảnh "dòng truyền thừa" bằng biểu tượng phả hệ/cây gia phả
- Estimated Duration: 12.46s (00:36:35.539 → 00:36:48.000)


---

## ACT XIII

**S091**
- Covered Beat IDs: BEAT_114, BEAT_115, BEAT_116 | Covered Obligation IDs: OBL_114, OBL_115, OBL_116 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: một không gian trung tính (Production Fill) | One Visible Action: (tĩnh, không nhân vật cụ thể)
- Setting: unspecified
- Continuity In: — | Continuity Out: → S092
- Production Fills: không gian trung tính (không cửa, không ghế, không điện thoại — tránh mọi motif đã dùng, để không tạo cộng hưởng ngoài ý muốn)
- Forbidden Additions: không dùng lại bất kỳ motif nào đã thiết lập (ghế/cửa/điện thoại) chỉ để lấp khoảng trống hình ảnh cho 3 câu phát biểu này
- Estimated Duration: 17.08s (00:36:48.000 → 00:37:05.077)

**S092**
- Covered Beat IDs: BEAT_117 | Covered Obligation IDs: OBL_117 (DEDICATED_SHOT)
- Shot Function: RESOLUTION
- Required Source Evidence: cử chỉ chăm sóc ấm áp hơn (nhánh 1: cha mẹ còn sống)
- Visual Subject: một người và cha/mẹ còn sống (generic) | One Visible Action: một cử chỉ chăm sóc ấm áp, hiện diện thật hơn
- Setting: unspecified
- Continuity In: ← S091 | Continuity Out: → S093
- Production Fills: không gian, trang phục
- Forbidden Additions: None thêm ngoài phạm vi 3 nhánh.
- Estimated Duration: 15.66s (00:37:05.077 → 00:37:20.737)

**S093**
- Covered Beat IDs: BEAT_117 | Covered Obligation IDs: OBL_117 (DEDICATED_SHOT)
- Shot Function: RESOLUTION
- Required Source Evidence: tư thế giữ khoảng cách an toàn nhưng không thù hận (nhánh 3: gia đình từng gây đau — chọn nhánh này làm đại diện thứ hai vì có evidence rõ nhất; nhánh 2 "biến nỗi nhớ thành đời sống tử tế" là trạng thái nội tâm dài hạn, khó hình ảnh hoá bằng một khoảnh khắc, mang bằng giọng đọc)
- Visual Subject: một người (generic) | One Visible Action: đứng ở khoảng cách an toàn, thần thái bình thản (không thù hận)
- Setting: unspecified
- Continuity In: ← S092 | Continuity Out: → S094
- Production Fills: không gian, trang phục
- Forbidden Additions: None thêm.
- Estimated Duration: 24.49s (00:37:20.737 → 00:37:45.231)

**S094**
- Covered Beat IDs: BEAT_118, BEAT_119, BEAT_120 | Covered Obligation IDs: OBL_118, OBL_119, OBL_120 (NO_DEDICATED_VISUAL, DEDICATED_SHOT)
- Shot Function: DEVELOP
- Required Source Evidence: hình ảnh ẩn dụ "hạt giống"
- Visual Subject: một hạt giống (Symbolic — narration tự đặt tên) | One Visible Action: (tĩnh) một hạt giống đơn lẻ, không dựng cảnh trồng trọt đầy đủ
- Setting: unspecified
- Continuity In: — | Continuity Out: → S095
- Production Fills: không gian đặt hạt giống (mặt bàn/lòng bàn tay — Production Fill)
- Forbidden Additions: không mở rộng ẩn dụ thành cảnh trồng trọt đầy đủ (đất, tay người trồng, cây nảy mầm) — 04B chỉ xác nhận từ "hạt giống"
- Estimated Duration: 19.38s (00:37:45.231 → 00:38:04.616)

**S095**
- Covered Beat IDs: BEAT_121 | Covered Obligation IDs: OBL_121 (DEDICATED_SHOT)
- Shot Function: RESOLUTION
- Required Source Evidence: ngồi xuống trước chiếc ghế; thắp một ngọn đèn
- Visual Subject: cùng chiếc ghế (T1), một người (không xác định là ai trong các nhân vật generic trước đó — đây là hình ảnh khép lại mang tính phổ quát, đại diện cho khán giả) | One Visible Action: ngồi xuống trước chiếc ghế, thắp một ngọn đèn
- Setting: cùng không gian nhà, thread T1
- Continuity In: ← S067 (T1, callback tiếp theo — lần thứ sáu) | Continuity Out: → S096
- Production Fills: kiểu dáng đèn (đây là lần dùng "đèn" thứ ba, ĐỘC LẬP theo sửa đổi 04B — không nối continuity với S028/S092-liên-quan-117)
- Forbidden Additions: không thêm nhang/bàn thờ nếu không được 04A/04B xác nhận ở beat này
- Estimated Duration: 13.59s (00:38:04.616 → 00:38:18.203)

**S096**
- Covered Beat IDs: BEAT_121 | Covered Obligation IDs: OBL_121 (DEDICATED_SHOT)
- Shot Function: RESOLUTION
- Required Source Evidence: chắp tay; nói trong lòng (câu nguyên văn — không hiển thị bằng chữ)
- Visual Subject: cùng người ở S095 | One Visible Action: chắp tay
- Setting: cùng S095, thread T1
- Continuity In: ← S095 (T1) | Continuity Out: → S097
- Production Fills: —
- Forbidden Additions: không đổi nội dung câu nói nguyên văn nếu trích dẫn qua giọng đọc; không hiển thị chữ trên màn hình
- Estimated Duration: 15.95s (00:38:18.203 → 00:38:34.154)

**S097**
- Covered Beat IDs: BEAT_122, BEAT_123 | Covered Obligation IDs: OBL_122, OBL_123 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ khung S096 (T1) | One Visible Action: (tĩnh, lặng yên sau cử chỉ chắp tay)
- Setting: cùng S096, thread T1
- Continuity In: ← S096 (T1) | Continuity Out: → S098
- Production Fills: —
- Forbidden Additions: —
- Estimated Duration: 18.92s (00:38:34.154 → 00:38:53.077)


---

## ACT XIV

**S098**
- Covered Beat IDs: BEAT_124 | Covered Obligation IDs: OBL_124 (NO_DEDICATED_VISUAL)
- Shot Function: TRANSITION
- Required Source Evidence: —
- Visual Subject: — | One Visible Action: —
- Setting: —
- Continuity In: ← S097 | Continuity Out: → S099
- Production Fills: —
- Forbidden Additions: **không mở rộng/diễn giải trước nội dung tập sau bằng hình ảnh cụ thể** — nội dung này thuộc tập tiếp theo, không phải EP004
- Estimated Duration: 30.46s (00:38:53.077 → 00:39:23.539)

**S099**
- Covered Beat IDs: BEAT_125 | Covered Obligation IDs: OBL_125 (SHARED_WITH_NEIGHBOR)
- Shot Function: HOLD
- Required Source Evidence: một trong 4 khả năng ngang hàng (gương mặt/chiếc ghế/bàn tay/câu chưa kịp nói) — không ưu tiên khả năng nào
- Visual Subject: cùng chiếc ghế (T1 — chọn "chiếc ghế" trong 4 khả năng vì đây là motif đã có continuity đầy đủ, giảm thiểu Production Fill mới cần thiết; **đây là lựa chọn dàn dựng (Production Fill ở cấp "chọn khả năng nào trong 4 khả năng ngang hàng"), không phải khẳng định của narration rằng ghế là hình ảnh chính thức duy nhất**) | One Visible Action: (tĩnh) hình ảnh ghế mờ dần
- Setting: cùng không gian nhà, thread T1
- Continuity In: ← S096 (T1, lần callback cuối) | Continuity Out: → S100
- Production Fills: mức độ mờ dần
- Forbidden Additions: không tuyên bố đây là hình ảnh "chính thức" duy nhất của 4 khả năng — ràng buộc kế thừa từ 04A/04B
- Estimated Duration: 19.85s (00:39:23.539 → 00:39:43.385)

**S100**
- Covered Beat IDs: BEAT_126, BEAT_127, BEAT_128 | Covered Obligation IDs: OBL_126, OBL_127, OBL_128 (NO_DEDICATED_VISUAL)
- Shot Function: HOLD
- Required Source Evidence: —
- Visual Subject: giữ khung S099, mờ dần hoàn toàn (Production Fill: tốc độ mờ) | One Visible Action: (tĩnh)
- Setting: cùng S099
- Continuity In: ← S099 (T1) | Continuity Out: —
- Production Fills: hiệu ứng mờ dần cuối phim
- Forbidden Additions: không phát minh hình ảnh mới cho 3 lời nhắc khép lại — tái sử dụng đúng evidence đã có (chiếc ghế), theo đúng khuyến nghị đã ghi tại OBL_128 trong 04B
- Estimated Duration: 26.77s (00:39:43.385 → 00:40:10.154)


---

## Bảng Obligation Disposition (đầy đủ 128/128, đã cập nhật Shot ID sau Phase C.1 — đối soát bằng script)

| OBL | Disposition | Shot(s) |
|---|---|---|
| 001 | DEDICATED_SHOT | S001 |
| 002 | DEDICATED_SHOT | S002, S003 |
| 003 | NO_DEDICATED_VISUAL | S004 |
| 004 | DEDICATED_SHOT | S004 |
| 005 | DEDICATED_SHOT | S005 |
| 006 | CONTINUATION_HOLD | S006 |
| 007 | NO_DEDICATED_VISUAL | S007 |
| 008 | NO_DEDICATED_VISUAL | S008 |
| 009 | NO_DEDICATED_VISUAL | S008 |
| 010 | DEDICATED_SHOT | S009 |
| 011 | NO_DEDICATED_VISUAL | S010 |
| 012 | NO_DEDICATED_VISUAL | S010 |
| 013 | NO_DEDICATED_VISUAL | S010 |
| 014 | NO_DEDICATED_VISUAL | S011 |
| 015 | DEDICATED_SHOT | S011 |
| 016 | NO_DEDICATED_VISUAL | S012 |
| 017 | DEDICATED_SHOT | S013 |
| 018 | NO_DEDICATED_VISUAL | S014 |
| 019 | NO_DEDICATED_VISUAL | S014 |
| 020 | NO_DEDICATED_VISUAL | S015 |
| 021 | NO_DEDICATED_VISUAL | S015 |
| 022 | SHARED_WITH_NEIGHBOR | S016 |
| 023 | NO_DEDICATED_VISUAL | S017 |
| 024 | NO_DEDICATED_VISUAL | S017 |
| 025 | NO_DEDICATED_VISUAL | S018 |
| 026 | DEDICATED_SHOT | S019 |
| 027 | NO_DEDICATED_VISUAL | S020 |
| 028 | NO_DEDICATED_VISUAL | S020 |
| 029 | DEDICATED_SHOT | S021 |
| 030 | DEDICATED_SHOT | S022 |
| 031 | NO_DEDICATED_VISUAL | S022 |
| 032 | DEDICATED_SHOT | S023 |
| 033 | NO_DEDICATED_VISUAL | S024 |
| 034 | DEDICATED_SHOT | S025 |
| 035 | NO_DEDICATED_VISUAL | S025 |
| 036 | DEDICATED_SHOT | S026 |
| 037 | NO_DEDICATED_VISUAL | S027 |
| 038 | NO_DEDICATED_VISUAL | S027 |
| 039 | DEDICATED_SHOT | S028 |
| 040 | DEDICATED_SHOT | S029, S030, S031, S032 |
| 041 | NO_DEDICATED_VISUAL | S033 |
| 042 | DEDICATED_SHOT | S033 |
| 043 | NO_DEDICATED_VISUAL | S034 |
| 044 | NO_DEDICATED_VISUAL | S034 |
| 045 | DEDICATED_SHOT | S035, S036, S037 |
| 046 | NO_DEDICATED_VISUAL | S038 |
| 047 | DEDICATED_SHOT | S038 |
| 048 | NO_DEDICATED_VISUAL | S038 |
| 049 | DEDICATED_SHOT | S039 |
| 050 | NO_DEDICATED_VISUAL | S039 |
| 051 | NO_DEDICATED_VISUAL | S040 |
| 052 | NO_DEDICATED_VISUAL | S040 |
| 053 | NO_DEDICATED_VISUAL | S041 |
| 054 | NO_DEDICATED_VISUAL | S041 |
| 055 | NO_DEDICATED_VISUAL | S041 |
| 056 | DEDICATED_SHOT | S042 |
| 057 | NO_DEDICATED_VISUAL | S042 |
| 058 | DEDICATED_SHOT | S043 |
| 059 | DEDICATED_SHOT | S044 |
| 060 | NO_DEDICATED_VISUAL | S045 |
| 061 | NO_DEDICATED_VISUAL | S045 |
| 062 | DEDICATED_SHOT | S046 |
| 063 | NO_DEDICATED_VISUAL | S047 |
| 064 | DEDICATED_SHOT | S048 |
| 065 | DEDICATED_SHOT | S049, S050, S051 |
| 066 | DEDICATED_SHOT | S052 |
| 067 | NO_DEDICATED_VISUAL | S053 |
| 068 | NO_DEDICATED_VISUAL | S053 |
| 069 | NO_DEDICATED_VISUAL | S054 |
| 070 | DEDICATED_SHOT | S054 |
| 071 | NO_DEDICATED_VISUAL | S055 |
| 072 | NO_DEDICATED_VISUAL | S055 |
| 073 | DEDICATED_SHOT | S056, S057 |
| 074 | NO_DEDICATED_VISUAL | S058 |
| 075 | NO_DEDICATED_VISUAL | S058 |
| 076 | DEDICATED_SHOT | S059 |
| 077 | NO_DEDICATED_VISUAL | S060 |
| 078 | NO_DEDICATED_VISUAL | S060 |
| 079 | NO_DEDICATED_VISUAL | S061 |
| 080 | DEDICATED_SHOT | S062 |
| 081 | DEDICATED_SHOT | S063 |
| 082 | DEDICATED_SHOT | S064 |
| 083 | DEDICATED_SHOT | S065 |
| 084 | DEDICATED_SHOT | S066 |
| 085 | DEDICATED_SHOT | S067 |
| 086 | NO_DEDICATED_VISUAL | S068 |
| 087 | DEDICATED_SHOT | S069, S070 |
| 088 | NO_DEDICATED_VISUAL | S071 |
| 089 | DEDICATED_SHOT | S071 |
| 090 | NO_DEDICATED_VISUAL | S072 |
| 091 | DEDICATED_SHOT | S072 |
| 092 | DEDICATED_SHOT | S073 |
| 093 | NO_DEDICATED_VISUAL | S073 |
| 094 | DEDICATED_SHOT | S074, S075 |
| 095 | NO_DEDICATED_VISUAL | S076 |
| 096 | NO_DEDICATED_VISUAL | S076 |
| 097 | NO_DEDICATED_VISUAL | S077 |
| 098 | NO_DEDICATED_VISUAL | S077 |
| 099 | DEDICATED_SHOT | S078 |
| 100 | NO_DEDICATED_VISUAL | S079 |
| 101 | DEDICATED_SHOT | S079 |
| 102 | NO_DEDICATED_VISUAL | S080 |
| 103 | NO_DEDICATED_VISUAL | S080 |
| 104 | NO_DEDICATED_VISUAL | S081 |
| 105 | DEDICATED_SHOT | S081 |
| 106 | NO_DEDICATED_VISUAL | S082 |
| 107 | DEDICATED_SHOT | S083 |
| 108 | DEDICATED_SHOT | S084 |
| 109 | NO_DEDICATED_VISUAL | S084 |
| 110 | DEDICATED_SHOT | S085, S086, S087 |
| 111 | NO_DEDICATED_VISUAL | S088 |
| 112 | DEDICATED_SHOT | S089 |
| 113 | NO_DEDICATED_VISUAL | S090 |
| 114 | NO_DEDICATED_VISUAL | S091 |
| 115 | NO_DEDICATED_VISUAL | S091 |
| 116 | NO_DEDICATED_VISUAL | S091 |
| 117 | DEDICATED_SHOT | S092, S093 |
| 118 | NO_DEDICATED_VISUAL | S094 |
| 119 | NO_DEDICATED_VISUAL | S094 |
| 120 | DEDICATED_SHOT | S094 |
| 121 | DEDICATED_SHOT | S095, S096 |
| 122 | NO_DEDICATED_VISUAL | S097 |
| 123 | NO_DEDICATED_VISUAL | S097 |
| 124 | NO_DEDICATED_VISUAL | S098 |
| 125 | SHARED_WITH_NEIGHBOR | S099 |
| 126 | NO_DEDICATED_VISUAL | S100 |
| 127 | NO_DEDICATED_VISUAL | S100 |
| 128 | NO_DEDICATED_VISUAL | S100 |

## Validation cuối (Phase C.1)

| Chỉ số | Giá trị | Cách tính |
|---|---:|---|
| final shot count | **100** | đếm Shot ID phân biệt S001–S100 |
| shots added | **16** | S005-S008(4, từ S005 cũ), S012-S017(6, từ S009 cũ), S026-S027(2, từ S018 cũ), S052-S053(2, từ S044 cũ), S059-S060(2, từ S050 cũ) |
| shots merged | **1** | S034(cũ) sáp nhập vào S033(cũ) → S042 (mới) |
| shots renumbered | **79** | shot giữ nguyên nội dung nhưng đổi Shot ID do các shot đứng trước bị tách/gộp |
| total obligations | 128 | không đổi (04B không bị sửa) |
| dedicated-shot obligations | 50 | không đổi |
| shared obligations | 2 | không đổi (OBL_022, OBL_125) |
| continuation-hold obligations | 1 | không đổi (OBL_006) |
| no-dedicated-visual obligations | 75 | không đổi |
| orphan obligations | **0** | 128/128 xuất hiện đúng 1 lần trong Bảng Obligation Disposition, mỗi obligation có ≥1 Shot ID hosting — xác nhận bằng script |
| unsupported continuity links | **0** | mọi Continuity In/Out đã được remap sang ID mới và xác nhận trỏ tới Shot ID tồn tại (100/100 hợp lệ) — xác nhận bằng script |
| timing gaps | **0** | mỗi shot bắt đầu đúng nơi shot trước kết thúc (xác nhận bằng script trên toàn bộ 100 shot) |
| timing overlaps | **0** | — |
| multi-action shots | **0** | rà soát lại toàn bộ trường "One Visible Action" của 100 shot, không phát hiện vi phạm mới phát sinh từ việc tách shot |
| total duration | **2410.154s** (00:40:10.154) | không đổi — tách/gộp shot chỉ vẽ lại ranh giới, không thêm/bớt nội dung narration |
| long holds remaining (≥60s) | **0** | S005/S009/S018 cũ đã được tách hết — không còn shot nào ≥60s |
| short shots remaining (<3.0s) | **1** | S063 (KEEP_WITH_JUSTIFICATION, xem Changelog mục 2) |

### PASS/FAIL

```
S005/S009/S018 đã được xử lý                  → PASS (tách thành 4+6+2 = 12 shot mới)
S034/S053 có resolution rõ                     → PASS (MERGE_WITH_NEIGHBOR / KEEP_WITH_JUSTIFICATION)
orphan obligations: 0                          → PASS
orphan underlay mappings: 0                    → PASS
timing gaps: 0                                 → PASS
timing overlaps: 0                             → PASS
multi-action shots: 0                          → PASS
DOMAIN_REVIEW_REQUIRED remaining: 0            → PASS (26/26 → APPROVED_WITH_CONSTRAINTS, xem 04D)
unsupported additions: 0                       → PASS
total duration: 2410.154s                      → PASS
```

**KẾT QUẢ: PASS_READY_FOR_PROMPT_COMPOSITION** — toàn bộ điều kiện đạt.
