# 04D — Shot Timing & Production Fill Review (EP004)
Phase D của Video Creation Pipeline. Nguồn: `04A_SEMANTIC_BEATS.md`, `04B_VISUAL_OBLIGATIONS.md`, `04C_SHOT_PLAN.md`, canonical narration (`OUTPUT/03_AUDIO_SCRIPT_TTS.txt`), và toàn bộ audio/timing metadata hiện có (`_INTERNAL/manifest.json`, `_INTERNAL/04_VIDEO_PROMPT_TIMELINE.json` — bản cũ, chỉ dùng như tham chiếu cơ sở ước lượng, không dùng lại kiến trúc/QA của bản đó). Phase này **không tạo video prompt**. S001–S090 được giữ nguyên từ 04C.

## 0. Trạng thái audio (đã xác minh trước khi làm bất cứ điều gì)

Đã kiểm tra toàn bộ repo: **không có file audio thực tế** (mp3/wav) cho EP004 ở bất kỳ đâu. `manifest.json` xác nhận `"voice_render": "OUT_OF_SCOPE"`. `_ARCHIVE/UNUSED_PRODUCTION_ASSETS/03_SUBTITLE_SEGMENTS.json` có `"timing_status": "AWAITING_AUDIO_ALIGNMENT"` với mọi `start_ms`/`end_ms` = `null`. Metadata timing duy nhất đang tồn tại trong dự án là ước lượng theo số từ: `5222` từ, `130` từ/phút, tổng `2410.154` giây — do chính `_INTERNAL/04_VIDEO_PROMPT_TIMELINE.json` (bản cũ) và `manifest.json` ghi nhận, và `06_QA_REPORT.md` (bản cũ) tự cảnh báo con số này "must not be presented as actual audio timing".

**Kết luận bắt buộc:** Toàn bộ timing trong tài liệu này là `ESTIMATED_FROM_NARRATION`, trạng thái `NOT_AUDIO_ALIGNED`. Không có shot nào được phép gắn nhãn `AUDIO_ALIGNED` hay `SEGMENT_METADATA` (vì không tồn tại segment metadata nào độc lập với chính ước lượng 130 wpm này). Trạng thái cuối cùng của Phase D là `PASS_ESTIMATED_TIMING`, không phải `PASS`/`AUDIO_ALIGNED`.

## 1. Phương pháp tính timing

- Tổng thời lượng ước tính: **2410.154 giây (40:10.154)**, kế thừa nguyên trạng số liệu đã có trong `manifest.json` (5222 từ ÷ 130 từ/phút) — không tự bịa một tổng số khác.
- Với mỗi trong 128 beat, đếm số từ thật của đúng dòng narration tương ứng (`OUTPUT/03_AUDIO_SCRIPT_TTS.txt`), xác nhận tổng cộng đúng 5222 từ.
- Với mỗi shot, cộng số từ của các beat mà nó bao phủ (theo `Covered Beat IDs` ở 04C) → quy đổi thời lượng theo tỉ lệ từ/giây toàn cục (5222 từ / 2410.154 giây).
- **10 beat bị một obligation trải rộng ra nhiều shot** (BEAT_002, 040, 045, 065, 073, 087, 094, 110, 117, 121) không thể chia đều máy móc — đã đối chiếu lại đúng cấu trúc mệnh đề thật của từng câu narration (ví dụ BEAT_040 có 4 mệnh đề riêng biệt cho 4 cảnh chia tay) để chia tỉ trọng từ theo đúng phần nội dung mỗi shot đại diện, thay vì chia đều vô căn cứ. Các shot thuộc nhóm này được gắn `Timing Confidence: Low` vì có thêm một lớp ước lượng thủ công (tỉ trọng mệnh đề) chồng lên ước lượng 130 wpm gốc.
- Timestamp được cộng dồn tuần tự S001→S090, không gap, không overlap theo thiết kế (mỗi shot bắt đầu đúng nơi shot trước kết thúc).
- Đã xác minh: tổng thời lượng cộng dồn = **2410.154s**, khớp chính xác với tổng ước lượng gốc — không có từ nào bị đếm hai lần hoặc bỏ sót (xác minh bằng script, tổng số từ phân bổ = 5222/5222).

## 2. Bảng Timing đầy đủ 90 shot

| Shot ID | Start | End | Duration (s) | Covered Beat IDs | Covered Obligation IDs | Underlaid Non-Visual OBL | Timing Source | Confidence | Transition Reason |
|---|---|---|---:|---|---|---|---|---|---|
| S001 | 00:00:00.000 | 00:00:07.846 | 7.85 | BEAT_001 | OBL_001 | — | ESTIMATED_FROM_NARRATION | Medium | thiết lập bối cảnh/motif mới |
| S002 | 00:00:07.846 | 00:00:16.338 | 8.49 | BEAT_002 | OBL_002 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S003 | 00:00:16.338 | 00:00:29.077 | 12.74 | BEAT_002 | OBL_002 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S004 | 00:00:29.077 | 00:00:52.615 | 23.54 | BEAT_003, BEAT_004 | OBL_003, OBL_004 | OBL_003 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S005 | 00:00:52.615 | 00:02:09.231 | 76.62 | BEAT_005, BEAT_006, BEAT_007, BEAT_008, BEAT_009 | OBL_005, OBL_006, OBL_007, OBL_008, OBL_009 | OBL_006, OBL_007, OBL_008, OBL_009 | ESTIMATED_FROM_NARRATION | Medium | bộc lộ thông tin mới trong cùng bối cảnh |
| S006 | 00:02:09.231 | 00:02:41.077 | 31.85 | BEAT_010 | OBL_010 | — | ESTIMATED_FROM_NARRATION | Medium | thiết lập bối cảnh/motif mới |
| S007 | 00:02:41.077 | 00:03:19.846 | 38.77 | BEAT_011, BEAT_012, BEAT_013 | OBL_011, OBL_012, OBL_013 | OBL_011, OBL_012, OBL_013 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S008 | 00:03:19.846 | 00:03:58.154 | 38.31 | BEAT_014, BEAT_015 | OBL_014, OBL_015 | OBL_014 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S009 | 00:03:58.154 | 00:06:40.615 | 162.46 | BEAT_016–BEAT_024 | OBL_016–OBL_024 | OBL_016, OBL_018, OBL_019, OBL_020, OBL_021, OBL_023, OBL_024 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo — **xem mục 3, HOLD_REVISION_REQUIRED** |
| S010 | 00:06:40.615 | 00:07:12.462 | 31.85 | BEAT_025 | OBL_025 | OBL_025 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S011 | 00:07:12.462 | 00:07:46.154 | 33.69 | BEAT_026 | OBL_026 | — | ESTIMATED_FROM_NARRATION | Medium | đối lập với ý ngay trước |
| S012 | 00:07:46.154 | 00:08:02.308 | 16.15 | BEAT_027, BEAT_028 | OBL_027, OBL_028 | OBL_027, OBL_028 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S013 | 00:08:02.308 | 00:08:29.538 | 27.23 | BEAT_029 | OBL_029 | — | ESTIMATED_FROM_NARRATION | Medium | đối lập với ý ngay trước |
| S014 | 00:08:29.538 | 00:08:58.615 | 29.08 | BEAT_030, BEAT_031 | OBL_030, OBL_031 | OBL_031 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S015 | 00:08:58.615 | 00:09:35.538 | 36.92 | BEAT_032 | OBL_032 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S016 | 00:09:35.538 | 00:10:01.846 | 26.31 | BEAT_033 | OBL_033 | OBL_033 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S017 | 00:10:01.846 | 00:10:40.615 | 38.77 | BEAT_034, BEAT_035 | OBL_034, OBL_035 | OBL_035 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S018 | 00:10:40.615 | 00:11:51.231 | 70.62 | BEAT_036, BEAT_037, BEAT_038 | OBL_036, OBL_037, OBL_038 | OBL_037, OBL_038 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo — **xem mục 3, HOLD_REVISION_REQUIRED** |
| S019 | 00:11:51.231 | 00:12:13.846 | 22.62 | BEAT_039 | OBL_039 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S020 | 00:12:13.846 | 00:12:27.254 | 13.41 | BEAT_040 | OBL_040 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S021 | 00:12:27.254 | 00:12:34.149 | 6.90 | BEAT_040 | OBL_040 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S022 | 00:12:34.149 | 00:12:42.960 | 8.81 | BEAT_040 | OBL_040 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S023 | 00:12:42.960 | 00:12:52.154 | 9.19 | BEAT_040 | OBL_040 | — | ESTIMATED_FROM_NARRATION | Low | giữ nguyên hình ảnh, narration tiếp tục |
| S024 | 00:12:52.154 | 00:13:19.385 | 27.23 | BEAT_041, BEAT_042 | OBL_041, OBL_042 | OBL_041 | ESTIMATED_FROM_NARRATION | Medium | bộc lộ thông tin mới trong cùng bối cảnh |
| S025 | 00:13:19.385 | 00:13:49.846 | 30.46 | BEAT_043, BEAT_044 | OBL_043, OBL_044 | OBL_043, OBL_044 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S026 | 00:13:49.846 | 00:13:54.000 | 4.15 | BEAT_045 | OBL_045 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S027 | 00:13:54.000 | 00:14:00.231 | 6.23 | BEAT_045 | OBL_045 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S028 | 00:14:00.231 | 00:14:24.462 | 24.23 | BEAT_045 | OBL_045 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S029 | 00:14:24.462 | 00:15:09.692 | 45.23 | BEAT_046, BEAT_047, BEAT_048 | OBL_046, OBL_047, OBL_048 | OBL_046, OBL_048 | ESTIMATED_FROM_NARRATION | Medium | quay lại motif đã thiết lập, chức năng mới |
| S030 | 00:15:09.692 | 00:15:58.615 | 48.92 | BEAT_049, BEAT_050 | OBL_049, OBL_050 | OBL_050 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S031 | 00:15:58.615 | 00:16:40.154 | 41.54 | BEAT_051, BEAT_052 | OBL_051, OBL_052 | OBL_051, OBL_052 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S032 | 00:16:40.154 | 00:17:11.077 | 30.92 | BEAT_053, BEAT_054, BEAT_055 | OBL_053, OBL_054, OBL_055 | OBL_053, OBL_054, OBL_055 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S033 | 00:17:11.077 | 00:17:45.231 | 34.15 | BEAT_056 | OBL_056 | — | ESTIMATED_FROM_NARRATION | Medium | thiết lập bối cảnh/motif mới |
| S034 | 00:17:45.231 | 00:17:48.000 | 2.77 | BEAT_057 | OBL_057 | OBL_057 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh — **dưới ngưỡng đọc tối thiểu, xem mục 3** |
| S035 | 00:17:48.000 | 00:17:51.231 | 3.23 | BEAT_058 | OBL_058 | — | ESTIMATED_FROM_NARRATION | Medium | bộc lộ thông tin mới trong cùng bối cảnh |
| S036 | 00:17:51.231 | 00:18:18.462 | 27.23 | BEAT_059 | OBL_059 | — | ESTIMATED_FROM_NARRATION | Medium | khép lại continuity thread/luận điểm |
| S037 | 00:18:18.462 | 00:18:37.385 | 18.92 | BEAT_060, BEAT_061 | OBL_060, OBL_061 | OBL_060, OBL_061 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S038 | 00:18:37.385 | 00:19:10.154 | 32.77 | BEAT_062 | OBL_062 | — | ESTIMATED_FROM_NARRATION | Medium | đối lập với ý ngay trước |
| S039 | 00:19:10.154 | 00:19:23.539 | 13.38 | BEAT_063 | OBL_063 | OBL_063 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S040 | 00:19:23.539 | 00:19:54.000 | 30.46 | BEAT_064 | OBL_064 | — | ESTIMATED_FROM_NARRATION | Medium | thiết lập bối cảnh/motif mới |
| S041 | 00:19:54.000 | 00:20:01.846 | 7.85 | BEAT_065 | OBL_065 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S042 | 00:20:01.846 | 00:20:09.462 | 7.62 | BEAT_065 | OBL_065 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S043 | 00:20:09.462 | 00:20:17.077 | 7.62 | BEAT_065 | OBL_065 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S044 | 00:20:17.077 | 00:21:16.154 | 59.08 | BEAT_066, BEAT_067, BEAT_068 | OBL_066, OBL_067, OBL_068 | OBL_067, OBL_068 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo — gần ngưỡng review |
| S045 | 00:21:16.154 | 00:21:47.077 | 30.92 | BEAT_069, BEAT_070 | OBL_069, OBL_070 | OBL_069 | ESTIMATED_FROM_NARRATION | Medium | thiết lập bối cảnh/motif mới |
| S046 | 00:21:47.077 | 00:22:28.154 | 41.08 | BEAT_071, BEAT_072 | OBL_071, OBL_072 | OBL_071, OBL_072 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S047 | 00:22:28.154 | 00:22:40.874 | 12.72 | BEAT_073 | OBL_073 | — | ESTIMATED_FROM_NARRATION | Low | đối lập với ý ngay trước |
| S048 | 00:22:40.874 | 00:23:17.077 | 36.20 | BEAT_073 | OBL_073 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S049 | 00:23:17.077 | 00:23:48.000 | 30.92 | BEAT_074, BEAT_075 | OBL_074, OBL_075 | OBL_074, OBL_075 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S050 | 00:23:48.000 | 00:24:45.692 | 57.69 | BEAT_076, BEAT_077, BEAT_078 | OBL_076, OBL_077, OBL_078 | OBL_077, OBL_078 | ESTIMATED_FROM_NARRATION | Medium | quay lại motif đã thiết lập — gần ngưỡng review |
| S051 | 00:24:45.692 | 00:25:16.154 | 30.46 | BEAT_079 | OBL_079 | OBL_079 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S052 | 00:25:16.154 | 00:25:21.231 | 5.08 | BEAT_080 | OBL_080 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S053 | 00:25:21.231 | 00:25:24.000 | 2.77 | BEAT_081 | OBL_081 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo — **dưới ngưỡng đọc tối thiểu, xem mục 3** |
| S054 | 00:25:24.000 | 00:25:29.077 | 5.08 | BEAT_082 | OBL_082 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S055 | 00:25:29.077 | 00:25:33.231 | 4.15 | BEAT_083 | OBL_083 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S056 | 00:25:33.231 | 00:25:45.692 | 12.46 | BEAT_084 | OBL_084 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S057 | 00:25:45.692 | 00:25:59.539 | 13.85 | BEAT_085 | OBL_085 | — | ESTIMATED_FROM_NARRATION | Medium | quay lại motif đã thiết lập, chức năng mới |
| S058 | 00:25:59.539 | 00:26:12.000 | 12.46 | BEAT_086 | OBL_086 | OBL_086 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S059 | 00:26:12.000 | 00:26:32.677 | 20.68 | BEAT_087 | OBL_087 | — | ESTIMATED_FROM_NARRATION | Low | thiết lập bối cảnh/motif mới |
| S060 | 00:26:32.677 | 00:27:03.692 | 31.02 | BEAT_087 | OBL_087 | — | ESTIMATED_FROM_NARRATION | Low | bộc lộ thông tin mới trong cùng bối cảnh |
| S061 | 00:27:03.692 | 00:27:53.539 | 49.85 | BEAT_088, BEAT_089 | OBL_088, OBL_089 | OBL_088 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S062 | 00:27:53.539 | 00:28:40.154 | 46.62 | BEAT_090, BEAT_091 | OBL_090, OBL_091 | OBL_090 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S063 | 00:28:40.154 | 00:29:21.231 | 41.08 | BEAT_092, BEAT_093 | OBL_092, OBL_093 | OBL_093 | ESTIMATED_FROM_NARRATION | Medium | đối lập với ý ngay trước |
| S064 | 00:29:21.231 | 00:29:36.369 | 15.14 | BEAT_094 | OBL_094 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S065 | 00:29:36.369 | 00:29:59.077 | 22.71 | BEAT_094 | OBL_094 | — | ESTIMATED_FROM_NARRATION | Low | bộc lộ thông tin mới trong cùng bối cảnh |
| S066 | 00:29:59.077 | 00:30:36.462 | 37.38 | BEAT_095, BEAT_096 | OBL_095, OBL_096 | OBL_095, OBL_096 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S067 | 00:30:36.462 | 00:31:12.462 | 36.00 | BEAT_097, BEAT_098 | OBL_097, OBL_098 | OBL_097, OBL_098 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S068 | 00:31:12.462 | 00:31:48.923 | 36.46 | BEAT_099 | OBL_099 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S069 | 00:31:48.923 | 00:32:32.769 | 43.85 | BEAT_100, BEAT_101 | OBL_100, OBL_101 | OBL_100 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S070 | 00:32:32.769 | 00:33:00.462 | 27.69 | BEAT_102, BEAT_103 | OBL_102, OBL_103 | OBL_102, OBL_103 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S071 | 00:33:00.462 | 00:33:48.462 | 48.00 | BEAT_104, BEAT_105 | OBL_104, OBL_105 | OBL_104 | ESTIMATED_FROM_NARRATION | Medium | đối lập với ý ngay trước |
| S072 | 00:33:48.462 | 00:34:06.923 | 18.46 | BEAT_106 | OBL_106 | OBL_106 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S073 | 00:34:06.923 | 00:34:41.077 | 34.15 | BEAT_107 | OBL_107 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S074 | 00:34:41.077 | 00:35:18.000 | 36.92 | BEAT_108, BEAT_109 | OBL_108, OBL_109 | OBL_109 | ESTIMATED_FROM_NARRATION | Medium | đối lập với ý ngay trước |
| S075 | 00:35:18.000 | 00:35:37.846 | 19.85 | BEAT_110 | OBL_110 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S076 | 00:35:37.846 | 00:35:44.991 | 7.14 | BEAT_110 | OBL_110 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S077 | 00:35:44.991 | 00:35:57.692 | 12.70 | BEAT_110 | OBL_110 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S078 | 00:35:57.692 | 00:36:10.154 | 12.46 | BEAT_111 | OBL_111 | OBL_111 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S079 | 00:36:10.154 | 00:36:35.539 | 25.38 | BEAT_112 | OBL_112 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S080 | 00:36:35.539 | 00:36:48.000 | 12.46 | BEAT_113 | OBL_113 | OBL_113 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S081 | 00:36:48.000 | 00:37:05.077 | 17.08 | BEAT_114, BEAT_115, BEAT_116 | OBL_114, OBL_115, OBL_116 | OBL_114, OBL_115, OBL_116 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S082 | 00:37:05.077 | 00:37:20.737 | 15.66 | BEAT_117 | OBL_117 | — | ESTIMATED_FROM_NARRATION | Low | khép lại continuity thread/luận điểm |
| S083 | 00:37:20.737 | 00:37:45.231 | 24.49 | BEAT_117 | OBL_117 | — | ESTIMATED_FROM_NARRATION | Low | khép lại continuity thread/luận điểm |
| S084 | 00:37:45.231 | 00:38:04.616 | 19.38 | BEAT_118, BEAT_119, BEAT_120 | OBL_118, OBL_119, OBL_120 | OBL_118, OBL_119 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S085 | 00:38:04.616 | 00:38:18.203 | 13.59 | BEAT_121 | OBL_121 | — | ESTIMATED_FROM_NARRATION | Low | khép lại continuity thread/luận điểm |
| S086 | 00:38:18.203 | 00:38:34.154 | 15.95 | BEAT_121 | OBL_121 | — | ESTIMATED_FROM_NARRATION | Low | khép lại continuity thread/luận điểm |
| S087 | 00:38:34.154 | 00:38:53.077 | 18.92 | BEAT_122, BEAT_123 | OBL_122, OBL_123 | OBL_122, OBL_123 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S088 | 00:38:53.077 | 00:39:23.539 | 30.46 | BEAT_124 | OBL_124 | OBL_124 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S089 | 00:39:23.539 | 00:39:43.385 | 19.85 | BEAT_125 | OBL_125 | — | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S090 | 00:39:43.385 | 00:40:10.154 | 26.77 | BEAT_126, BEAT_127, BEAT_128 | OBL_126, OBL_127, OBL_128 | OBL_126, OBL_127, OBL_128 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |

**Tổng thời lượng cộng dồn: 2410.154 giây (00:40:10.154)** — khớp chính xác với ước lượng 130 wpm hiện có của dự án, đã xác minh không gap/không overlap.

## 3. Mapping Non-Visual & Duration Review

### 3.1 Non-Visual underlay coverage

Cả 76 obligation cần underlay (75 `NO_DEDICATED_VISUAL` + 1 `CONTINUATION_HOLD`, theo đúng số liệu đã validate ở 04C) đều có `underlaid_on_shot` tường minh trong cột "Underlaid Non-Visual OBL" ở bảng trên — không có obligation mồ côi. Đã kiểm tra từng shot-host theo 3 tiêu chí bắt buộc:

- **Cùng semantic context:** đạt 76/76 — mọi obligation underlay đều nằm trong shot có `Covered Beat IDs` bao gồm chính beat của obligation đó (không có trường hợp mượn shot của một beat khác).
- **Không tạo nghĩa ngược narration:** đạt — đã rà lại từng shot host, không có trường hợp hình ảnh mâu thuẫn với ý nghĩa beat đang phát (ví dụ S046 giữ hình ảnh tụng kinh trung tính trong lúc narration cảnh báo "không biến nghi lễ thành cái máy" — hình ảnh không khẳng định điều bị phê phán).
- **Không kéo dài chỉ vì thiếu scene / không dùng scene fallback không liên quan:** đạt cho 73/76; **3 trường hợp cần review** vì shot host quá dài — xem mục 3.2 (S005, S009, S018 đều là shot-host của nhiều obligation Non-Visual liền kề).

### 3.2 Duration Review

**Ngưỡng sử dụng (giải thích rõ vì chưa có audio thật):**
- *Ngưỡng đọc tối thiểu:* 3.0 giây. Đây không phải ngưỡng máy móc theo chuẩn edit phim thông thường (vốn có thể chấp nhận 1.5-2s cho một khung hình đơn giản) — được chọn cao hơn một chút vì các shot ở đây thường có một hành động/cử chỉ con người cần đủ thời gian đọc được (không chỉ một bố cục tĩnh), và vì đây là nội dung suy ngẫm chậm rãi, không phải montage nhanh.
- *Ngưỡng hold quá dài (bắt buộc `HOLD_REVISION_REQUIRED`):* ≥ 60 giây (1 phút) cho một hình ảnh về cơ bản không đổi. Chọn mốc này vì đây là giới hạn phổ biến trong dựng phim tài liệu/chiêm nghiệm mà một bố cục tĩnh không đổi bắt đầu có nguy cơ khiến người xem mất tập trung — ngay cả với phong cách chậm, tĩnh tại đã xác lập cho toàn bộ episode (global visual profile: "meditative, no chaotic movement"). Áp dụng thêm điều kiện: chỉ bắt buộc revision khi hold ≥ 60s **và** bao phủ ≥ 3 beat/obligation có nội dung khác biệt rõ rệt (không phải một ý được kéo dài).
- *Vùng cần xem lại nhưng chưa bắt buộc sửa (40-60 giây):* giữ nguyên nhưng ghi chú cho người dựng phim cân nhắc thêm chuyển động rất nhẹ (Production Fill, không phải shot mới) nếu thấy cần khi có audio thật.

**Kết quả đo (tính từ toàn bộ 90 shot, không phải mẫu):**

| Chỉ số | Giá trị |
|---|---|
| shortest shot | 2.77s (S034, S053) |
| longest shot | 162.46s (S009) |
| median duration | 24.94s |
| average duration | 26.78s |
| shots under minimum readable duration (<3.0s) | **2** — S034, S053 |
| shots with excessive hold (≥60s, `HOLD_REVISION_REQUIRED`) | **3** — S009 (162.46s), S005 (76.62s), S018 (70.62s) |
| shots trong vùng cần xem lại (40-60s) | 11 — S029, S030, S031, S044, S046, S050, S061, S062, S063, S069, S071 |
| shots covering ≥3 semantic obligations/beats | 11 — S005(5), S007(3), S009(9), S018(3), S029(3), S032(3), S044(3), S050(3), S081(3), S084(3), S090(3) |

**Đánh giá 2 shot dưới ngưỡng đọc tối thiểu:** S034 (BEAT_057, "vòng lặp vẫn quay" — 6 từ) và S053 (BEAT_081, "Một bữa cơm không cáu gắt" — 6 từ) đều là câu narration cực ngắn có chủ đích (nhịp dồn dập). 2.77s là ngắn nhưng shot chỉ yêu cầu một tư thế tĩnh/gần-tĩnh (không phải một chuyển động phức tạp), nên về nguyên tắc vẫn đọc được — không đề xuất sửa Shot Plan, chỉ khuyến nghị khi có audio thật, nếu nhịp đọc thực tế khiến khung hình dưới 2s, cân nhắc kéo dài production pacing (Production Fill: giữ khung thêm một nhịp im lặng ngắn) chứ không cần shot mới.

**Đánh giá S009 (trường hợp được nêu đích danh trong yêu cầu):** 162.46s, phủ 9 beat (BEAT_016-024) — đoạn lý giải giáo lý dày đặc nhất episode (phân biệt chấp trước/biết ơn/báo ân/từ bi, ý nghĩa giác ngộ...), toàn bộ giữ nguyên MỘT khung hình Đao Lợi tĩnh. Đây là hold dài nhất và bao phủ nhiều ý khác biệt nhất trong toàn bộ shot plan → **`HOLD_REVISION_REQUIRED`**, xem đề xuất ở mục 6.

**Đánh giá S005 và S018:** S005 (76.62s, 5 beat: BEAT_005-009) giữ hold trên chiếc ghế qua cả một đoạn chuyển ý (từ khoảnh khắc ghế trống → 5 câu chưa nói → tóm tắt series → chuyển ý → nghịch lý địa ngục/cõi trời) — 5 nội dung khác biệt trên một khung tĩnh 76s. S018 (70.62s, 3 beat: BEAT_036-038) giữ hold trên cảnh giữ khoảng cách qua 3 luận đề (giữ ranh giới không mất biết ơn; 4 phân biệt biết ơn/tôn trọng/chăm sóc/tha thứ) — nội dung khá đồng nhất về chủ đề (ranh giới) nhưng thời lượng vẫn vượt ngưỡng. Cả hai → **`HOLD_REVISION_REQUIRED`**, xem đề xuất ở mục 6.

**Multi-action shots:** đã rà soát lại toàn bộ 90 "One Visible Action" — **0 shot còn vi phạm** (2 vi phạm phát hiện ở bản nháp Phase C — S041, S042 — đã được tự sửa trực tiếp trong `04C_SHOT_PLAN.md` trước khi Phase C được báo cáo PASS; xác nhận lại lần nữa ở Phase D, không phát hiện vi phạm mới).

## 4. Production Fill Review

| Shot ID | Source Facts | Required Visual Evidence | Proposed Production Fills | Forbidden Additions | Approval Status | Risk Notes |
|---|---|---|---|---|---|---|
| S001 | chiếc ghế trống | chiếc ghế trống; không người ngồi | chất liệu ghế, không gian phòng, thời điểm trong ngày | không người ngồi/vừa rời ghế; không đạo cụ phụ trợ chưa xác nhận | APPROVED | — |
| S002 | mẹ (generic) ngồi ở ghế cạnh bàn ăn; nhặt rau | ghế cạnh bàn ăn; mẹ nhặt rau | trang phục, loại rau, ánh sáng | không đặc tả danh tính/ngoại hình mẹ; không thêm nhân vật | APPROVED | — |
| S003 | cha (generic) ngồi ở ghế gần cửa sổ; uống trà | ghế gần cửa sổ; cha uống trà | trang phục, loại tách trà, ánh sáng cửa sổ | không đặc tả danh tính/ngoại hình cha | APPROVED | — |
| S004 | một người con (generic); hoàn tất giao dịch chuyển khoản | hành vi chuyển khoản đại diện nghĩa vụ vật chất | không gian, trang phục, giao diện (không chữ) | không số tiền cụ thể; không cảnh gọi điện/về thăm (không xảy ra) | APPROVED | — |
| S005 | cùng chiếc ghế | ghế chuyển sang trạng thái trống hẳn | mức độ bụi, ánh sáng chiều muộn | không cảnh nguyên nhân mất mát; không hiển thị chữ cho 5 câu chưa nói | APPROVED_WITH_CONSTRAINTS | Duration 76.62s vượt ngưỡng — xem mục 6 |
| S006 | Đức Phật (medium-wide/silhouette); thuyết pháp | Đức Phật thuyết pháp tại Đao Lợi, liên hệ thân mẫu | kiến trúc/không gian Đao Lợi (Production Fill hoàn toàn); sự hiện diện tối thiểu của pháp hội | không lời thoại; không cận cảnh khuôn mặt thiêng liêng; không tuyên bố tái hiện lịch sử chính xác | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S007 | giữ khung Đao Lợi từ S006 | (không evidence riêng) | không có mới | không tự trả lời 3 câu hỏi tu từ | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S008 | một người (generic); ngồi yên lặng | dấu hiệu gián tiếp cho lý do "đi chậm" | không gian, trang phục | không thiên vị một trong 5 nhóm đã liệt kê | APPROVED | — |
| S009 | Đức Phật (T2); cử chỉ hướng về thân mẫu | thần thái điềm tĩnh hướng về thân mẫu (kế thừa S006) | không có mới | không minh hoạ "chấp trước"; không minh hoạ 4 định nghĩa OBL_021 | DOMAIN_REVIEW_REQUIRED | Duration 162.46s — xem mục 6 |
| S010 | (bắc cầu, không evidence riêng) | — | — | — | APPROVED | — |
| S011 | người con (generic, KHÔNG liên kết S004) | chuyển khoản + cuộc gọi ngắn | không gian, trang phục | không hiển thị nội dung KHÔNG xảy ra (đau lưng mẹ, chiều mưa cha) | APPROVED | — |
| S012 | giữ khung S011 | — | — | — | APPROVED | — |
| S013 | một buổi giỗ đông người; hai anh em | bàn thờ sáng đèn, mâm cỗ đầy; anh em không nhìn mặt | quy mô mâm cỗ, số khách, trang phục | không số người cụ thể; không nội dung xung đột cụ thể | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S014 | một người (generic) trước bàn thờ/di ảnh | hành vi tưởng niệm mang tính phô diễn | không gian tưởng niệm, trang phục | không dựng "sân khấu" nghĩa đen | APPROVED | — |
| S015 | người chăm sóc, mẹ già; đút cháo | 4 hành động chăm sóc; dấu hiệu mệt mỏi | không gian, trang phục, đạo cụ | không đặc tả bệnh cụ thể | APPROVED | — |
| S016 | cùng người chăm sóc S015 | — | — | — | APPROVED | — |
| S017 | một người (generic mới); căng thẳng khi nghe "cha mẹ" | dấu hiệu căng thẳng/né tránh | không gian, trang phục | không gán câu "cha mẹ mà, bỏ qua đi" cho nhân vật cha/mẹ trong khung | APPROVED | — |
| S018 | hai người (generic); giữ khoảng cách bình tĩnh | hành vi giữ khoảng cách/đặt ranh giới | không gian, trang phục | không đặc tả xung đột cụ thể | APPROVED_WITH_CONSTRAINTS | Duration 70.62s vượt ngưỡng — xem mục 6 |
| S019 | ngọn đèn nhỏ trong không gian tối dịu | ẩn dụ đèn (khẳng định) đối lập roi (phủ định) | kiểu dáng đèn, không gian | không dựng cảnh đánh roi nghĩa đen | APPROVED | — |
| S020 | người con, cha (giường bệnh); nắm tay, khóc | con nắm tay cha khóc | nội thất phòng bệnh, trang phục | không đặt tên nhân vật; không đặc tả bệnh lý | APPROVED | — |
| S021 | mẹ (giường bệnh), con; hỏi | mẹ thở yếu hỏi con ăn gì | nội thất phòng bệnh | không hiển thị câu hỏi bằng chữ | APPROVED | — |
| S022 | cha lớn tuổi (giường bệnh); nói | cha nghiêm khắc nói lời xin lỗi | nội thất phòng bệnh | không hiển thị lời xin lỗi bằng chữ | APPROVED | — |
| S023 | hành lang khoa hồi sức | sự vắng mặt của người không kịp đến | nội thất hành lang | **không dùng "ghế trống" ở đây** — tránh cộng hưởng ngoài ý với T1 | APPROVED_WITH_CONSTRAINTS | Xem mục 4 ghi chú S023 |
| S024 | cùng chiếc ghế (T1) | ghế với dấu hiệu hao mòn | mức độ hao mòn | không hiển thị riêng 6 lý do bận | APPROVED | — |
| S025 | quay lại khung Đao Lợi (T2) | — | — | không thêm hành động/biểu cảm mới cho Đức Phật | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S026 | mẹ và cha (generic, KHÔNG liên kết S002/S003) | mẹ, cha — nguồn nâng đỡ gần nhất | trang phục, không gian | không đặc tả danh tính | APPROVED | — |
| S027 | người trồng lúa (đại diện); làm việc trên ruộng | nhóm lao động/tri thức | không gian ruộng, trang phục | không thêm nghề ngoài 9 nhóm đã liệt kê | APPROVED | — |
| S028 | người quét đường (đại diện); quét đường | nhóm cộng đồng rộng | không gian đường phố, trang phục | không thêm nhóm ngoài 9 nhóm | APPROVED | — |
| S029 | cùng chiếc ghế | ghế làm điểm neo "mở rộng lòng biết ơn" | — | không đám đông "mọi chúng sinh"; không hình tướng Địa Tạng (cấm) | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S030 | một người (generic); thần thái trắc ẩn | thần thái trắc ẩn hướng về gia đình | không gian, trang phục | không đám đông; không chi tiết "đại nguyện" thêm | APPROVED | — |
| S031 | giữ khung S030 | — | — | không dựng cảnh cụ thể cho hành vi bị phê phán | APPROVED | — |
| S032 | giữ khung S030 (kéo dài) | — | — | — | APPROVED | — |
| S033 | người cha, con; la con, cúi mặt | cha la con; đứa trẻ cúi mặt; biểu cảm nhận ra | không gian, trang phục | không đặt tên; không bạo lực thể chất; không 2 lớp thời gian cùng khung | APPROVED | — |
| S034 | cùng người cha (T3) | — | — | không biểu tượng "vòng lặp" | APPROVED | Duration 2.77s — dưới ngưỡng, xem mục 3 |
| S035 | cùng người cha (T3); dừng lại | khoảnh khắc dừng lại | — | không mô tả nguyên nhân cụ thể | APPROVED | — |
| S036 | người cha, con (T3); quỳ, nói | quỳ xuống, nói (câu nguyên văn) | — | không đổi câu thoại; không phản ứng của con | APPROVED | — |
| S037 | giữ khung S036 (T3) | — | — | — | APPROVED | — |
| S038 | một người (generic, KHÔNG phải người cha T3) | ẩn dụ bàn thờ/nén hương (phủ định vị trí) | không gian, trang phục, bàn thờ hậu cảnh | **không mặc định cùng người cha S033-036** | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S039 | giữ khung S038 | — | — | không hiện Đức Phật kể chuyện S033-038 | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S040 | một gia đình bữa cơm (generic, mới); nói, lắng nghe | khoảnh khắc bữa cơm — nhân quả khởi đầu | không gian bếp, món ăn, trang phục | không tách rời chuỗi nhân quả; không "20 năm sau" bằng nhân vật cụ thể | APPROVED | — |
| S041 | một người (generic); gõ tin nhắn | nhắn tin | không gian, trang phục | không hiển thị nội dung tin nhắn | APPROVED_WITH_CONSTRAINTS | Duration bao gồm "nghe điện thoại" qua giọng đọc |
| S042 | một người (generic); đặt ranh giới | đặt ranh giới | không gian, trang phục | — | APPROVED_WITH_CONSTRAINTS | Duration bao gồm "chăm sóc người già" qua giọng đọc |
| S043 | người lớn, trẻ; cúi xuống, xin lỗi | nuôi dạy con; xin lỗi | không gian, trang phục | không thêm hành vi ngoài 6 đã liệt kê | APPROVED | — |
| S044 | một người, người già khác; chăm sóc | ân hận → chăm sóc người già khác | không gian, trang phục | — | APPROVED | Duration 59.08s — gần ngưỡng review |
| S045 | một người (generic); tụng kinh | tụng kinh (đại diện 4 thực hành) | không gian, trang phục, đạo cụ tối thiểu | không mô tả "chùa" cụ thể | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S046 | giữ khung S045 | — | — | không minh hoạ hành vi bị phê phán | APPROVED | Duration 41.08s |
| S047 | một người (đơn sơ); thắp một nén hương | người nghèo thắp nén hương | không gian, trang phục đơn sơ | không bàn thờ lớn | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S048 | một người (generic, mới), mẹ còn sống; dọn cơm | chăm mẹ còn sống; người kiềm chế (ví dụ 3) | không gian bếp, món ăn | không thêm ví dụ thứ 4 | APPROVED_WITH_CONSTRAINTS | 2 nhân vật khác nhau trong cùng nhóm ví dụ |
| S049 | giữ khung S048 | — | — | — | APPROVED | — |
| S050 | cùng khung Đao Lợi (T2) | pháp hội tại Đao Lợi | — | không cảnh riêng "đại nguyện Địa Tạng"; không tự vẽ địa ngục | DOMAIN_REVIEW_REQUIRED | Duration 57.69s — xem mục 5 |
| S051 | (bắc cầu) | — | — | không mô tả hình tướng Địa Tạng | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S052 | một người; gọi điện thư thái | thực hành nhỏ 1/6 | không gian | không đặc tả người gọi/nhận | APPROVED | — |
| S053 | một gia đình; dùng bữa điềm tĩnh | thực hành nhỏ 2/6 | món ăn, không gian | — | APPROVED | Duration 2.77s — dưới ngưỡng, xem mục 3 |
| S054 | một người; xin lỗi chủ động | thực hành nhỏ 3/6 | không gian | — | APPROVED | — |
| S055 | một người; nói bình tĩnh | thực hành nhỏ 4/6 | không gian | — | APPROVED | — |
| S056 | một người; bước vào không gian hỗ trợ | thực hành nhỏ 5/6 | không gian (không xác định loại hình) | không xác định hình thức trị liệu cụ thể | APPROVED | — |
| S057 | cùng chiếc ghế (T1) + một người; nhìn ghế | thực hành nhỏ 6/6, callback T1 | không gian (kế thừa T1) | — | APPROVED | — |
| S058 | (bắc cầu) | — | — | — | APPROVED | — |
| S059 | mẹ, cha (generic, mới); cha sửa bóng đèn | hồi tưởng "luôn ở đó" | không gian, trang phục, dụng cụ | không đặc tả bệnh lý | APPROVED | — |
| S060 | cùng mẹ/cha, lớn tuổi hơn; tay run | 3 dấu hiệu suy yếu | không gian, trang phục | không tên bệnh cụ thể | APPROVED | — |
| S061 | một gia đình; dùng bữa ấm áp | 1 ví dụ "tỉnh lại" | không gian bếp, món ăn | không hình ảnh "cuộc đua"/đồng hồ | APPROVED | Duration 49.85s |
| S062 | một người (ở xa); gọi điện lắng nghe | gọi điện chăm chú | không gian, trang phục | không quốc gia cụ thể cho "nước ngoài" | APPROVED_WITH_CONSTRAINTS | Không gán quốc gia |
| S063 | cha mẹ (generic, mới); ngồi cạnh đồ đầy đủ | cô đơn dù đủ vật chất | không gian, đạo cụ | — | APPROVED | Duration 41.08s |
| S064 | người chăm sóc, mẹ bệnh; thay thuốc | 1/4 hoạt động chăm sóc | không gian, đạo cụ y tế | không đặc tả bệnh, không tên | APPROVED | — |
| S065 | cùng người chăm sóc S064; khóc trong nhà tắm | khóc lặng lẽ, nước chảy nhỏ | nội thất nhà tắm | không hiện lời khen "hiếu quá" cùng khung với cảnh khóc | APPROVED | — |
| S066 | giữ khung S065 | — | — | — | APPROVED | — |
| S067 | (bắc cầu) | — | — | — | APPROVED | — |
| S068 | một người (generic, mới); căng cứng khi chuông reo | phản ứng khi nghe chuông điện thoại | không gian, trang phục | không hình ảnh hoá câu "hãy về đi, cha mẹ mà" bằng nhân vật đang nói | APPROVED_WITH_CONSTRAINTS | Không dựng câu thoại phổ biến như lời của nhân vật |
| S069 | hai người; giữ khoảng cách, cầu nguyện thầm | khoảng cách vật lý; tư thế cầu nguyện | không gian, trang phục | không đặc tả xung đột cụ thể | APPROVED | — |
| S070 | giữ khung S069 | — | — | — | APPROVED | — |
| S071 | cha, mẹ, con (generic, mới); cha xin lỗi | cử chỉ cha xin lỗi con | không gian, trang phục | — | APPROVED | Duration 48.00s |
| S072 | giữ khung S071 | — | — | không đổi câu thoại nếu trích dẫn | APPROVED | — |
| S073 | cha hoặc mẹ (generic); kiềm chế cơn giận | khoảnh khắc dừng tay trước giận dữ | không gian, trang phục | — | APPROVED | — |
| S074 | một căn nhà, gia đình generic; mỗi người một góc | ẩn dụ "căn nhà" bất hoà | nội thất, trang phục | **không biểu tượng tôn giáo/siêu nhiên cho "địa ngục"** | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S075 | gia đình tại bàn ăn; im lặng căng thẳng | ảnh 1-2/5 địa ngục hiện đại | không gian, món ăn | không siêu nhiên | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S076 | mẹ già, các con; con tranh cãi | ảnh 3/5 | nội thất phòng | không siêu nhiên | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S077 | người lớn, trẻ; không ôm | ảnh 4-5/5 | không gian, trang phục | không siêu nhiên | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S078 | (bắc cầu) | — | — | không siêu nhiên cho "địa ngục"/"cõi lành" | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S079 | một người (generic mới); kiềm chế | dừng lại trước hành vi tiêu cực | không gian, trang phục | không hiển thị hành vi tiêu cực dương tính | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S080 | giữ khung S079 | — | — | không biểu tượng phả hệ | APPROVED | — |
| S081 | không gian trung tính | — | không gian trung tính (không mượn motif đã dùng) | không dùng ghế/cửa/điện thoại chỉ để lấp chỗ trống | APPROVED | — |
| S082 | một người, cha/mẹ còn sống; chăm sóc ấm áp | nhánh 1/3 (OBL_117) | không gian, trang phục | — | APPROVED_WITH_CONSTRAINTS | 1/3 nhánh, không phải nhánh duy nhất |
| S083 | một người; giữ khoảng cách an toàn | nhánh 3/3 (OBL_117) | không gian, trang phục | — | APPROVED_WITH_CONSTRAINTS | Nhánh 2 không có hình ảnh riêng |
| S084 | một hạt giống (Symbolic) | ẩn dụ "hạt giống" | không gian đặt hạt giống | không mở rộng thành cảnh trồng trọt đầy đủ | APPROVED | — |
| S085 | cùng chiếc ghế (T1), một người phổ quát; ngồi, thắp đèn | ngồi trước ghế; thắp đèn | kiểu dáng đèn (độc lập, không nối T2/S019) | không thêm nhang/bàn thờ chưa xác nhận | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S086 | cùng người S085; chắp tay | chắp tay; nói trong lòng | — | không đổi câu nói; không chữ trên màn hình | DOMAIN_REVIEW_REQUIRED | Xem mục 5 |
| S087 | giữ khung S086 (T1) | — | — | — | APPROVED | — |
| S088 | (bắc cầu) | — | — | không mở rộng nội dung tập sau | APPROVED | — |
| S089 | cùng chiếc ghế (T1, 1 trong 4 khả năng) | 1 trong 4 khả năng ngang hàng | mức độ mờ dần | không tuyên bố là hình ảnh chính thức duy nhất | APPROVED_WITH_CONSTRAINTS | Lựa chọn dàn dựng, không phải khẳng định narration |
| S090 | giữ khung S089, mờ dần | — | hiệu ứng mờ dần cuối phim | không phát minh hình ảnh mới cho lời nhắc kết | APPROVED | — |

**Tổng hợp Approval Status:** APPROVED = 59 | APPROVED_WITH_CONSTRAINTS = 11 | DOMAIN_REVIEW_REQUIRED = 20 | REVISION_REQUIRED = 0.

## 5. Religious/Domain Safety Review

### Tier 1 — Đức Phật, thân mẫu, Cung Trời Đao Lợi (thread T2: S006, S007, S009, S025, S050)

| Hạng mục | Nội dung |
|---|---|
| **Source-confirmed** | Đức Phật thuyết pháp tại Cung Trời Đao Lợi, trong liên hệ với thân mẫu (04A BEAT_010, trích trực tiếp từ narration: "pháp hội của Kinh Địa Tạng được đặt tại Cung Trời Đao Lợi... Đức Phật thuyết pháp nơi ấy trong liên hệ với thân mẫu của Ngài"). Đây là khung giáo lý theo truyền thống Phật giáo Đại thừa, được narration tự gọi là "theo truyền thống", không phải khẳng định lịch sử tuyệt đối. |
| **Production interpretation** | Toàn bộ kiến trúc/không gian vật lý của Cung Trời Đao Lợi là Production Fill 100% — 04A/04B không đặc tả bất kỳ chi tiết kiến trúc/hình ảnh nào. Sự hiện diện của một nhóm người dự pháp hội (để hình ảnh hoá khái niệm "pháp hội") cũng là Production Fill cần thiết, không phải Source Fact. |
| **Phải giữ ở mức biểu tượng/khoảng cách** | Gương mặt Đức Phật và thân mẫu: theo đúng chính sách an toàn tôn giáo đã có sẵn của dự án (Character Usage Plan của EP004: "medium-wide/profile/silhouette khi character guidance chưa đầy đủ") — không cận cảnh, không đặc tả chi tiết khuôn mặt. Kiến trúc Đao Lợi: phải giữ tính biểu tượng, không tuyên bố là tái hiện lịch sử/khảo cổ chính xác (đúng `VISUAL_ENGINE.md`: "Symbolic visualization must not pretend to be historical reconstruction"). |
| **Bị cấm tuyệt đối** | Lời thoại/độc thoại nội tâm của Đức Phật hoặc thân mẫu (Character Usage Plan: "No invented dialogue", "No first-person invented speech"); biến cảnh thành "bằng chứng khoa học/lịch sử" cho vũ trụ quan Phật giáo; góc máy/ánh sáng thiếu tôn kính. |

**S009 cần lưu ý thêm:** ngoài vấn đề thời lượng (mục 3), nội dung narration mà S009 làm nền (BEAT_016-024) bao gồm các khái niệm dễ bị hiểu sai nếu hình ảnh "khẳng định" thay vì chỉ "làm nền" — ví dụ OBL_019 (chấp trước bị phủ định) và OBL_021 (4 định nghĩa) đã được 04B cấm minh hoạ cụ thể; giữ nguyên một khung hình trung tính (Đức Phật, thần thái điềm tĩnh) là lựa chọn AN TOÀN về mặt tôn giáo dù có vấn đề về nhịp dựng phim (mục 3). Đây là đánh đổi cần cân nhắc ở mục 6, không phải lỗi an toàn tôn giáo.

### Tier 2 — Địa Tạng Bồ Tát (được nhắc tên, không được hiển thị: S029 tail, S051)

| Hạng mục | Nội dung |
|---|---|
| **Source-confirmed** | Địa Tạng Bồ Tát được nhắc tên tại BEAT_048 và BEAT_079 (narration: "Đó là nơi Địa Tạng Bồ Tát xuất hiện trong mạch cảm xúc của series này"; "Địa Tạng Bồ Tát không nên được nhìn như một vị thần cai quản cõi âm"). |
| **Production interpretation** | Không có — 04A/04B **minh thị cấm mô tả hình tướng Địa Tạng Bồ Tát ở cả hai vị trí này** (Forbidden Hallucination của OBL_048 và OBL_079). |
| **Phải giữ ở mức biểu tượng/khoảng cách** | N/A — không hiển thị. |
| **Bị cấm tuyệt đối** | Bất kỳ hình tướng/y phục/biểu tượng cụ thể nào của Địa Tạng Bồ Tát tại S029, S051. Nếu một phiên bản dựng phim sau này muốn hiển thị Địa Tạng Bồ Tát, phải quay lại `CB_BUD_001` (Character Bible Địa Tạng Bồ Tát đã có trong dự án) và làm một vòng review riêng — ngoài phạm vi Phase D này. |

### Tier 3 — Nghi lễ/kinh điển/bàn thờ/nén hương generic (S013, S038, S039, S045, S047, S085, S086)

| Hạng mục | Nội dung |
|---|---|
| **Source-confirmed** | Giỗ lớn với bàn thờ sáng đèn (BEAT_029, S013); ẩn dụ "nén hương chân thành không nằm trên bàn thờ" (BEAT_062, S038); disclaimer rõ ràng "không phải lời Đức Phật, đây là quán chiếu hiện đại" (BEAT_063, S039); tụng kinh/làm phước/hồi hướng/tưởng niệm là các thực hành có tên (BEAT_070, S045); người nghèo thắp một nén hương đối lập phô trương (BEAT_073, S047); thắp một ngọn đèn + chắp tay ở đoạn kết (BEAT_121, S085/S086). |
| **Production interpretation** | Không gian nghi lễ cụ thể (trong nhà/nơi thờ cúng/không gian tu tập) là Production Fill — 04A/04B không đặc tả. Không được tự thêm địa điểm "chùa" nếu narration không nêu (04B minh thị cấm ở OBL_070/S045). |
| **Phải giữ ở mức biểu tượng/khoảng cách** | Nhân vật thực hiện nghi lễ (tụng kinh, thắp hương) đều là người thường (generic, lay person), không phải tăng ni/sư thầy trừ khi 04A xác nhận — hiện tại không có beat nào xác nhận nhân vật tu sĩ, nên **không được tự thêm hình tượng tăng ni/sư thầy** ở các shot này. |
| **Bị cấm tuyệt đối** | S038/S039: không được mặc định nhân vật "một người" (OBL_062) là cùng người cha ở T3, và không được thể hiện Đức Phật đang kể câu chuyện người cha như một sự kiện kinh điển (disclaimer của chính OBL_063 áp dụng ngược cho toàn bộ S033-038). S045: không mô tả không gian "chùa" cụ thể. S047: không dựng bàn thờ lớn (narration minh thị đối lập với phô trương — dựng bàn thờ lớn ở đây sẽ TRỰC TIẾP mâu thuẫn với ý nghĩa của beat). |

### Tier 4 — "Địa ngục" như ẩn dụ tâm lý (S074, S075, S076, S077, S078, S079 — CRITICAL)

Đây là hạng mục rủi ro cao nhất trong toàn bộ Phase D, vì `VIDEO_CREATION_ARCHITECTURE_AUDIT.md` (audit trước) đã ghi nhận đây là loại lỗi cụ thể cần tránh (biến ẩn dụ tâm lý thành cảnh siêu nhiên).

| Hạng mục | Nội dung |
|---|---|
| **Source-confirmed** | BEAT_108: "địa ngục" = ẩn dụ cho "căn nhà bớt một chút địa ngục" (bất hoà gia đình). BEAT_110: 5 hình ảnh cụ thể được liệt kê rõ — căn nhà không ai nghe ai; bàn ăn mỗi người một nỗi giận; căn phòng mẹ già + con tranh giành; đứa trẻ học tình thương có điều kiện; người lớn không biết ôm con. BEAT_111: "nếu địa ngục bắt đầu từ tâm sân hận, cõi lành bắt đầu từ tâm biết dừng" — đối lập ẩn dụ, không phải mô tả hai cảnh giới vật lý. |
| **Production interpretation** | Không gian "căn nhà"/"bàn ăn"/"căn phòng" là Production Fill — không gian gia đình đời thường, hiện đại hoặc phi thời gian tính, do 04A/04B không đặc tả kiến trúc cụ thể. |
| **Phải giữ ở mức biểu tượng/khoảng cách** | Toàn bộ 5 hình ảnh phải giữ đúng bản chất "khoảnh khắc đời thường bất hoà" — căng thẳng, im lặng, xa cách — không phải hình ảnh gây sợ hãi hay kịch tính hoá. |
| **Bị cấm tuyệt đối** | **Không dùng bất kỳ biểu tượng tôn giáo/siêu nhiên nào cho "địa ngục"**: không lửa, không quỷ, không hình phạt, không cảnh giới âm phủ, không ánh sáng/màu sắc kiểu horror. Đây là ràng buộc đã được 04A/04B ghi nhận minh thị và được nhắc lại nguyên văn trong yêu cầu Phase D ("Không biến 'địa ngục' tâm lý thành cảnh siêu nhiên") — vi phạm ở đây sẽ đồng thời phá vỡ tinh thần giáo lý gốc (Kinh Địa Tạng không nên "bị kẹt trong sợ hãi", đúng BEAT_077/S077-tail-context) và tạo rủi ro tôn giáo nghiêm trọng nhất trong toàn episode. |

**Kết luận Tier 4:** cả 6 shot (S074-S079) đã được 04C thiết kế đúng hướng (ẩn dụ đời thường, có ghi cấm rõ trong Forbidden Additions) — Approval Status đúng đắn là `DOMAIN_REVIEW_REQUIRED` không phải vì shot hiện tại sai, mà vì đây là điểm rủi ro cao nhất cần con người duyệt lại trước khi bất kỳ ai (kể cả Phase E sau này) được phép viết prompt final cho các shot này.

## 6. Đề xuất sửa Shot Plan (chỉ đề xuất — không tự áp dụng vào 04C)

### Đề xuất 1

- **Shot ID:** S009
- **Problem:** Hold 162.46 giây trên một khung hình gần như không đổi (Đức Phật tại Đao Lợi), bao phủ 9 beat có nội dung giáo lý khác biệt rõ rệt (phân biệt chấp trước/biết ơn/báo ân/từ bi; ý nghĩa giác ngộ và ân nghĩa). Đây là hold dài nhất toàn bộ shot plan, vượt xa ngưỡng 60s đã định.
- **Evidence:** Mục 3.2 — 162.46s, 9 `Covered Beat IDs` (BEAT_016-024), so với shot dài thứ nhì (S005, 76.62s) đã gấp hơn 2 lần.
- **Recommended Revision:** Không đề xuất thêm nhân vật/vật thể mới (không có rationale hình ảnh nào được 04A/04B cung cấp cho 9 beat này ngoài khung Đao Lợi). Đề xuất một trong hai hướng, cả hai đều KHÔNG cần Phase D tự thực hiện vì cần quyết định biên tập: (a) chia S009 thành 2-3 shot con cùng bối cảnh Đao Lợi nhưng thay đổi rất nhẹ `Visual Progression`/khung hình (ví dụ: từ trung cảnh Đức Phật sang một góc nhìn khác của cùng pháp hội — vẫn cùng Source Fact, chỉ khác bố cục Production Fill) để chia nhỏ thời lượng hold mà không thêm nội dung mới; hoặc (b) giữ nguyên 1 shot nhưng rút ngắn về mặt biên tập bằng cách chấp nhận một phần narration của đoạn này được "nói nhanh hơn" khi có audio thật (ngoài phạm vi Phase D).
- **Impact on neighboring shots:** Nếu chọn (a), Continuity In/Out của S008→S009→S010 không đổi (vẫn cùng thread T2, cùng vị trí trong chuỗi); chỉ cần đổi `total planned shots` từ 90 lên 91-92 và đánh số lại S010 trở đi — đây là thay đổi cấu trúc thật sự cần một lượt duyệt Phase C mới, không thực hiện trong Phase D.

### Đề xuất 2

- **Shot ID:** S005
- **Problem:** Hold 76.62 giây trên chiếc ghế trống, bao phủ 5 beat có bước ngoặt nội dung rõ (khoảnh khắc trống → 5 câu chưa nói → tóm tắt series → chuyển ý → nghịch lý địa ngục/cõi trời).
- **Evidence:** Mục 3.2 — 76.62s, 5 beat, vượt ngưỡng 60s.
- **Recommended Revision:** Vì đây là motif Critical (T1) và chức năng cảm xúc đã đúng (một khoảnh lặng dài là chủ đích nghệ thuật hợp lý ở đây, khác S009), đề xuất **giữ nguyên 1 shot nhưng ghi nhận rõ đây là chủ đích nghệ thuật** (không giống S009/S018) — chỉ cần production khi dàn dựng cân nhắc một chuyển động cực nhẹ (ánh sáng thay đổi dần, không phải nội dung mới) để giữ khung hình "sống" trong 76s, đây là Production Fill chứ không phải shot mới.
- **Impact on neighboring shots:** Không đổi nếu chọn giữ nguyên; nếu quyết định chia nhỏ ở bước sau, Continuity T1 (→ S006 không đổi vì S006 đã là shot khác bối cảnh) không bị ảnh hưởng.

### Đề xuất 3

- **Shot ID:** S018
- **Problem:** Hold 70.62 giây, 3 beat cùng chủ đề ranh giới nhưng thời lượng dài so với nội dung tương đối đơn giản (một cử chỉ giữ khoảng cách).
- **Evidence:** Mục 3.2 — 70.62s, 3 beat.
- **Recommended Revision:** Tương tự S009, đề xuất chia thành 2 shot cùng nhân vật/bối cảnh nhưng khác góc độ/khoảnh khắc (ví dụ: một shot cho hành động giữ khoảng cách, một shot cho khoảnh khắc "biết ơn trở nên thật hơn" — có thể là một biểu cảm khác trên cùng nhân vật) — cần một lượt duyệt Phase C mới, không thực hiện trong Phase D.
- **Impact on neighboring shots:** Nếu thực hiện, cần đánh số lại từ S019 trở đi tương tự Đề xuất 1.

**Không có đề xuất nào khác** — không phát hiện obligation bị gán sai host shot, không phát hiện Production Fill làm sai nghĩa, không phát hiện religious depiction không an toàn ở thiết kế hiện tại của 04C (chỉ có rủi ro cần *review*, không phải lỗi đã xảy ra).

## 7. Validation cuối

| Chỉ số | Giá trị |
|---|---|
| total shots | 90 |
| timed shots | 90/90 |
| audio-aligned shots | **0** (không có audio thật) |
| estimated shots | 90/90 (ESTIMATED_FROM_NARRATION) |
| total mapped duration | 2410.154s (00:40:10.154) |
| audio duration (thực tế đo được) | N/A — chưa có audio render |
| timing gaps | 0 (xác minh: mỗi shot bắt đầu đúng nơi shot trước kết thúc) |
| timing overlaps | 0 |
| orphan Non-Visual obligations | 0 (76/76 có `underlaid_on_shot` tường minh) |
| excessive holds (`HOLD_REVISION_REQUIRED`) | 3 — S005, S009, S018 |
| multi-action shots | 0 (2 vi phạm phát hiện và sửa trong Phase C trước khi báo cáo) |
| Production Fill items reviewed | 90/90 |
| Production Fill revisions required | 0 (không có Approval Status = REVISION_REQUIRED) |
| domain-review-required shots | 20 |
| unsupported additions | 0 |

### PASS/FAIL

```
90/90 shots có timing disposition             → PASS
128/128 obligations có visual hoặc underlay mapping → PASS
orphan Non-Visual obligations: 0              → PASS
timing gaps: 0                                → PASS
timing overlaps: 0                            → PASS
multi-action shots: 0                         → PASS
unsupported additions: 0                      → PASS
mọi religious shot có approval status         → PASS (20/20 = DOMAIN_REVIEW_REQUIRED, không có shot tôn giáo nào thiếu status)
```

**Vì không có timing audio thật, trạng thái cuối cùng theo đúng yêu cầu là:**

```
PASS_ESTIMATED_TIMING
```

**Không báo cáo `AUDIO_ALIGNED`.** 3 shot bị `HOLD_REVISION_REQUIRED` (S005, S009, S018) không làm thay đổi trạng thái PASS tổng thể — đây là warning cần xử lý ở một vòng duyệt Phase C riêng (mục 6), không phải điều kiện fail của Phase D.
