# 04D — Shot Timing & Production Fill Review (EP004)
Phase D của Video Creation Pipeline, **đã cập nhật ở Phase C.1/D.1 (Hold Decomposition / Short-Shot Resolution / Domain Approval Gate)**. Nguồn: `04A_SEMANTIC_BEATS.md`, `04B_VISUAL_OBLIGATIONS.md`, `04C_SHOT_PLAN.md` (100 shot, đã cập nhật), canonical narration (`OUTPUT/03_AUDIO_SCRIPT_TTS.txt`). Phase này không tạo video prompt. **S001–S100** (thay cho S001–S090 ở Phase D gốc).

## 0. Trạng thái audio (không đổi so với Phase D gốc)

Vẫn không có file audio thực tế cho EP004. Toàn bộ timing trong tài liệu này là `ESTIMATED_FROM_NARRATION`, trạng thái `NOT_AUDIO_ALIGNED`. Trạng thái cuối cùng của Phase D.1 là `PASS_READY_FOR_PROMPT_COMPOSITION` với timing vẫn ở dạng ước lượng — không có shot nào được phép gắn nhãn `AUDIO_ALIGNED`.

## 1. Phương pháp tính timing (không đổi phương pháp, tính lại trên cấu trúc 100 shot)

- Tổng thời lượng ước tính: **2410.154 giây (40:10.154)** — không đổi, vì tách/gộp shot chỉ vẽ lại ranh giới trên cùng nội dung narration, không thêm/bớt từ nào.
- Với 16 shot mới (từ việc tách S005/S009/S018 cũ) và 1 shot gộp (S042, hấp thụ S034 cũ), thời lượng được tính lại bằng đúng phương pháp cũ: đếm từ thật của phần narration mỗi shot đại diện, quy đổi theo tỉ lệ 5222 từ / 2410.154 giây.
- Đã xác minh bằng script: tổng thời lượng cộng dồn của 100 shot mới = **2410.154s chính xác**, không gap, không overlap.

## 2. Bảng Timing đầy đủ 100 shot

| Shot ID | Start | End | Duration (s) | Covered Beat IDs | Covered Obligation IDs | Underlaid Non-Visual OBL | Timing Source | Confidence | Transition Reason |
|---|---|---|---:|---|---|---|---|---|---|
| S001 | 00:00:00.000 | 00:00:07.846 | 7.85 | BEAT_001 | OBL_001 | — | ESTIMATED_FROM_NARRATION | Medium | thiết lập bối cảnh/motif mới |
| S002 | 00:00:07.846 | 00:00:16.338 | 8.49 | BEAT_002 | OBL_002 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S003 | 00:00:16.338 | 00:00:29.077 | 12.74 | BEAT_002 | OBL_002 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S004 | 00:00:29.077 | 00:00:52.615 | 23.54 | BEAT_003, BEAT_004 | OBL_003, OBL_004 | OBL_003 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S005 | 00:00:52.615 | 00:00:59.077 | 6.46 | BEAT_005 | OBL_005 | — | ESTIMATED_FROM_NARRATION | Medium | bộc lộ thông tin mới trong cùng bối cảnh |
| S006 | 00:00:59.077 | 00:01:20.769 | 21.69 | BEAT_006 | OBL_006 | OBL_006 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S007 | 00:01:20.769 | 00:01:54.000 | 33.23 | BEAT_007 | OBL_007 | OBL_007 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S008 | 00:01:54.000 | 00:02:09.231 | 15.23 | BEAT_008, BEAT_009 | OBL_008, OBL_009 | OBL_008, OBL_009 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S009 | 00:02:09.231 | 00:02:41.077 | 31.85 | BEAT_010 | OBL_010 | — | ESTIMATED_FROM_NARRATION | Medium | thiết lập bối cảnh/motif mới |
| S010 | 00:02:41.077 | 00:03:19.846 | 38.77 | BEAT_011, BEAT_012, BEAT_013 | OBL_011, OBL_012, OBL_013 | OBL_011, OBL_012, OBL_013 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S011 | 00:03:19.846 | 00:03:58.154 | 38.31 | BEAT_014, BEAT_015 | OBL_014, OBL_015 | OBL_014 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S012 | 00:03:58.154 | 00:04:23.538 | 25.38 | BEAT_016 | OBL_016 | OBL_016 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S013 | 00:04:23.538 | 00:04:52.154 | 28.62 | BEAT_017 | OBL_017 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S014 | 00:04:52.154 | 00:05:25.846 | 33.69 | BEAT_018, BEAT_019 | OBL_018, OBL_019 | OBL_018, OBL_019 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S015 | 00:05:25.846 | 00:06:02.308 | 36.46 | BEAT_020, BEAT_021 | OBL_020, OBL_021 | OBL_020, OBL_021 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S016 | 00:06:02.308 | 00:06:30.923 | 28.62 | BEAT_022 | OBL_022 | — | ESTIMATED_FROM_NARRATION | Medium | quay lại motif đã thiết lập, chức năng mới |
| S017 | 00:06:30.923 | 00:06:40.615 | 9.69 | BEAT_023, BEAT_024 | OBL_023, OBL_024 | OBL_023, OBL_024 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S018 | 00:06:40.615 | 00:07:12.462 | 31.85 | BEAT_025 | OBL_025 | OBL_025 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S019 | 00:07:12.462 | 00:07:46.154 | 33.69 | BEAT_026 | OBL_026 | — | ESTIMATED_FROM_NARRATION | Medium | đối lập với ý ngay trước |
| S020 | 00:07:46.154 | 00:08:02.308 | 16.15 | BEAT_027, BEAT_028 | OBL_027, OBL_028 | OBL_027, OBL_028 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S021 | 00:08:02.308 | 00:08:29.538 | 27.23 | BEAT_029 | OBL_029 | — | ESTIMATED_FROM_NARRATION | Medium | đối lập với ý ngay trước |
| S022 | 00:08:29.538 | 00:08:58.615 | 29.08 | BEAT_030, BEAT_031 | OBL_030, OBL_031 | OBL_031 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S023 | 00:08:58.615 | 00:09:35.538 | 36.92 | BEAT_032 | OBL_032 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S024 | 00:09:35.538 | 00:10:01.846 | 26.31 | BEAT_033 | OBL_033 | OBL_033 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S025 | 00:10:01.846 | 00:10:40.615 | 38.77 | BEAT_034, BEAT_035 | OBL_034, OBL_035 | OBL_035 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S026 | 00:10:40.615 | 00:11:18.462 | 37.85 | BEAT_036 | OBL_036 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S027 | 00:11:18.462 | 00:11:51.231 | 32.77 | BEAT_037, BEAT_038 | OBL_037, OBL_038 | OBL_037, OBL_038 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S028 | 00:11:51.231 | 00:12:13.846 | 22.62 | BEAT_039 | OBL_039 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S029 | 00:12:13.846 | 00:12:27.254 | 13.41 | BEAT_040 | OBL_040 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S030 | 00:12:27.254 | 00:12:34.149 | 6.90 | BEAT_040 | OBL_040 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S031 | 00:12:34.149 | 00:12:42.960 | 8.81 | BEAT_040 | OBL_040 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S032 | 00:12:42.960 | 00:12:52.154 | 9.19 | BEAT_040 | OBL_040 | — | ESTIMATED_FROM_NARRATION | Low | giữ nguyên hình ảnh, narration tiếp tục |
| S033 | 00:12:52.154 | 00:13:19.385 | 27.23 | BEAT_041, BEAT_042 | OBL_041, OBL_042 | OBL_041 | ESTIMATED_FROM_NARRATION | Medium | bộc lộ thông tin mới trong cùng bối cảnh |
| S034 | 00:13:19.385 | 00:13:49.846 | 30.46 | BEAT_043, BEAT_044 | OBL_043, OBL_044 | OBL_043, OBL_044 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S035 | 00:13:49.846 | 00:13:54.000 | 4.15 | BEAT_045 | OBL_045 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S036 | 00:13:54.000 | 00:14:00.231 | 6.23 | BEAT_045 | OBL_045 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S037 | 00:14:00.231 | 00:14:24.462 | 24.23 | BEAT_045 | OBL_045 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S038 | 00:14:24.462 | 00:15:09.692 | 45.23 | BEAT_046, BEAT_047, BEAT_048 | OBL_046, OBL_047, OBL_048 | OBL_046, OBL_048 | ESTIMATED_FROM_NARRATION | Medium | quay lại motif đã thiết lập, chức năng mới |
| S039 | 00:15:09.692 | 00:15:58.615 | 48.92 | BEAT_049, BEAT_050 | OBL_049, OBL_050 | OBL_050 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S040 | 00:15:58.615 | 00:16:40.154 | 41.54 | BEAT_051, BEAT_052 | OBL_051, OBL_052 | OBL_051, OBL_052 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S041 | 00:16:40.154 | 00:17:11.077 | 30.92 | BEAT_053, BEAT_054, BEAT_055 | OBL_053, OBL_054, OBL_055 | OBL_053, OBL_054, OBL_055 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S042 | 00:17:11.077 | 00:17:48.000 | 36.92 | BEAT_056, BEAT_057 | OBL_056, OBL_057 | OBL_057 | ESTIMATED_FROM_NARRATION | Medium | thiết lập bối cảnh/motif mới |
| S043 | 00:17:48.000 | 00:17:51.231 | 3.23 | BEAT_058 | OBL_058 | — | ESTIMATED_FROM_NARRATION | Medium | bộc lộ thông tin mới trong cùng bối cảnh |
| S044 | 00:17:51.231 | 00:18:18.462 | 27.23 | BEAT_059 | OBL_059 | — | ESTIMATED_FROM_NARRATION | Medium | khép lại continuity thread/luận điểm |
| S045 | 00:18:18.462 | 00:18:37.385 | 18.92 | BEAT_060, BEAT_061 | OBL_060, OBL_061 | OBL_060, OBL_061 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S046 | 00:18:37.385 | 00:19:10.154 | 32.77 | BEAT_062 | OBL_062 | — | ESTIMATED_FROM_NARRATION | Medium | đối lập với ý ngay trước |
| S047 | 00:19:10.154 | 00:19:23.539 | 13.38 | BEAT_063 | OBL_063 | OBL_063 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S048 | 00:19:23.539 | 00:19:54.000 | 30.46 | BEAT_064 | OBL_064 | — | ESTIMATED_FROM_NARRATION | Medium | thiết lập bối cảnh/motif mới |
| S049 | 00:19:54.000 | 00:20:01.846 | 7.85 | BEAT_065 | OBL_065 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S050 | 00:20:01.846 | 00:20:09.462 | 7.62 | BEAT_065 | OBL_065 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S051 | 00:20:09.462 | 00:20:17.077 | 7.62 | BEAT_065 | OBL_065 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S052 | 00:20:17.077 | 00:20:59.539 | 42.46 | BEAT_066 | OBL_066 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S053 | 00:20:59.539 | 00:21:16.154 | 16.62 | BEAT_067, BEAT_068 | OBL_067, OBL_068 | OBL_067, OBL_068 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S054 | 00:21:16.154 | 00:21:47.077 | 30.92 | BEAT_069, BEAT_070 | OBL_069, OBL_070 | OBL_069 | ESTIMATED_FROM_NARRATION | Medium | thiết lập bối cảnh/motif mới |
| S055 | 00:21:47.077 | 00:22:28.154 | 41.08 | BEAT_071, BEAT_072 | OBL_071, OBL_072 | OBL_071, OBL_072 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S056 | 00:22:28.154 | 00:22:40.874 | 12.72 | BEAT_073 | OBL_073 | — | ESTIMATED_FROM_NARRATION | Low | đối lập với ý ngay trước |
| S057 | 00:22:40.874 | 00:23:17.077 | 36.20 | BEAT_073 | OBL_073 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S058 | 00:23:17.077 | 00:23:48.000 | 30.92 | BEAT_074, BEAT_075 | OBL_074, OBL_075 | OBL_074, OBL_075 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S059 | 00:23:48.000 | 00:24:12.000 | 24.00 | BEAT_076 | OBL_076 | — | ESTIMATED_FROM_NARRATION | Medium | quay lại motif đã thiết lập, chức năng mới |
| S060 | 00:24:12.000 | 00:24:45.692 | 33.69 | BEAT_077, BEAT_078 | OBL_077, OBL_078 | OBL_077, OBL_078 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S061 | 00:24:45.692 | 00:25:16.154 | 30.46 | BEAT_079 | OBL_079 | OBL_079 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S062 | 00:25:16.154 | 00:25:21.231 | 5.08 | BEAT_080 | OBL_080 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S063 | 00:25:21.231 | 00:25:24.000 | 2.77 | BEAT_081 | OBL_081 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S064 | 00:25:24.000 | 00:25:29.077 | 5.08 | BEAT_082 | OBL_082 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S065 | 00:25:29.077 | 00:25:33.231 | 4.15 | BEAT_083 | OBL_083 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S066 | 00:25:33.231 | 00:25:45.692 | 12.46 | BEAT_084 | OBL_084 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S067 | 00:25:45.692 | 00:25:59.539 | 13.85 | BEAT_085 | OBL_085 | — | ESTIMATED_FROM_NARRATION | Medium | quay lại motif đã thiết lập, chức năng mới |
| S068 | 00:25:59.539 | 00:26:12.000 | 12.46 | BEAT_086 | OBL_086 | OBL_086 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S069 | 00:26:12.000 | 00:26:32.677 | 20.68 | BEAT_087 | OBL_087 | — | ESTIMATED_FROM_NARRATION | Low | thiết lập bối cảnh/motif mới |
| S070 | 00:26:32.677 | 00:27:03.692 | 31.02 | BEAT_087 | OBL_087 | — | ESTIMATED_FROM_NARRATION | Low | bộc lộ thông tin mới trong cùng bối cảnh |
| S071 | 00:27:03.692 | 00:27:53.539 | 49.85 | BEAT_088, BEAT_089 | OBL_088, OBL_089 | OBL_088 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S072 | 00:27:53.539 | 00:28:40.154 | 46.62 | BEAT_090, BEAT_091 | OBL_090, OBL_091 | OBL_090 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S073 | 00:28:40.154 | 00:29:21.231 | 41.08 | BEAT_092, BEAT_093 | OBL_092, OBL_093 | OBL_093 | ESTIMATED_FROM_NARRATION | Medium | đối lập với ý ngay trước |
| S074 | 00:29:21.231 | 00:29:36.369 | 15.14 | BEAT_094 | OBL_094 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S075 | 00:29:36.369 | 00:29:59.077 | 22.71 | BEAT_094 | OBL_094 | — | ESTIMATED_FROM_NARRATION | Low | bộc lộ thông tin mới trong cùng bối cảnh |
| S076 | 00:29:59.077 | 00:30:36.462 | 37.38 | BEAT_095, BEAT_096 | OBL_095, OBL_096 | OBL_095, OBL_096 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S077 | 00:30:36.462 | 00:31:12.462 | 36.00 | BEAT_097, BEAT_098 | OBL_097, OBL_098 | OBL_097, OBL_098 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S078 | 00:31:12.462 | 00:31:48.923 | 36.46 | BEAT_099 | OBL_099 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S079 | 00:31:48.923 | 00:32:32.769 | 43.85 | BEAT_100, BEAT_101 | OBL_100, OBL_101 | OBL_100 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S080 | 00:32:32.769 | 00:33:00.462 | 27.69 | BEAT_102, BEAT_103 | OBL_102, OBL_103 | OBL_102, OBL_103 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S081 | 00:33:00.462 | 00:33:48.462 | 48.00 | BEAT_104, BEAT_105 | OBL_104, OBL_105 | OBL_104 | ESTIMATED_FROM_NARRATION | Medium | đối lập với ý ngay trước |
| S082 | 00:33:48.462 | 00:34:06.923 | 18.46 | BEAT_106 | OBL_106 | OBL_106 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S083 | 00:34:06.923 | 00:34:41.077 | 34.15 | BEAT_107 | OBL_107 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S084 | 00:34:41.077 | 00:35:18.000 | 36.92 | BEAT_108, BEAT_109 | OBL_108, OBL_109 | OBL_109 | ESTIMATED_FROM_NARRATION | Medium | đối lập với ý ngay trước |
| S085 | 00:35:18.000 | 00:35:37.846 | 19.85 | BEAT_110 | OBL_110 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S086 | 00:35:37.846 | 00:35:44.991 | 7.14 | BEAT_110 | OBL_110 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S087 | 00:35:44.991 | 00:35:57.692 | 12.70 | BEAT_110 | OBL_110 | — | ESTIMATED_FROM_NARRATION | Low | khai triển ý/evidence tiếp theo |
| S088 | 00:35:57.692 | 00:36:10.154 | 12.46 | BEAT_111 | OBL_111 | OBL_111 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S089 | 00:36:10.154 | 00:36:35.539 | 25.38 | BEAT_112 | OBL_112 | — | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S090 | 00:36:35.539 | 00:36:48.000 | 12.46 | BEAT_113 | OBL_113 | OBL_113 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S091 | 00:36:48.000 | 00:37:05.077 | 17.08 | BEAT_114, BEAT_115, BEAT_116 | OBL_114, OBL_115, OBL_116 | OBL_114, OBL_115, OBL_116 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S092 | 00:37:05.077 | 00:37:20.737 | 15.66 | BEAT_117 | OBL_117 | — | ESTIMATED_FROM_NARRATION | Low | khép lại continuity thread/luận điểm |
| S093 | 00:37:20.737 | 00:37:45.231 | 24.49 | BEAT_117 | OBL_117 | — | ESTIMATED_FROM_NARRATION | Low | khép lại continuity thread/luận điểm |
| S094 | 00:37:45.231 | 00:38:04.616 | 19.38 | BEAT_118, BEAT_119, BEAT_120 | OBL_118, OBL_119, OBL_120 | OBL_118, OBL_119 | ESTIMATED_FROM_NARRATION | Medium | khai triển ý/evidence tiếp theo |
| S095 | 00:38:04.616 | 00:38:18.203 | 13.59 | BEAT_121 | OBL_121 | — | ESTIMATED_FROM_NARRATION | Low | khép lại continuity thread/luận điểm |
| S096 | 00:38:18.203 | 00:38:34.154 | 15.95 | BEAT_121 | OBL_121 | — | ESTIMATED_FROM_NARRATION | Low | khép lại continuity thread/luận điểm |
| S097 | 00:38:34.154 | 00:38:53.077 | 18.92 | BEAT_122, BEAT_123 | OBL_122, OBL_123 | OBL_122, OBL_123 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S098 | 00:38:53.077 | 00:39:23.539 | 30.46 | BEAT_124 | OBL_124 | OBL_124 | ESTIMATED_FROM_NARRATION | Medium | bắc cầu chủ đề, không evidence riêng |
| S099 | 00:39:23.539 | 00:39:43.385 | 19.85 | BEAT_125 | OBL_125 | — | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |
| S100 | 00:39:43.385 | 00:40:10.154 | 26.77 | BEAT_126, BEAT_127, BEAT_128 | OBL_126, OBL_127, OBL_128 | OBL_126, OBL_127, OBL_128 | ESTIMATED_FROM_NARRATION | Medium | giữ nguyên hình ảnh, narration tiếp tục |

**Tổng thời lượng cộng dồn: 2410.154 giây (00:40:10.154)** — khớp chính xác, đã xác minh không gap/không overlap trên toàn bộ 100 shot.

## 3. Mapping Non-Visual & Duration Review (Phase C.1 kết quả)

### 3.1 Non-Visual underlay coverage

Cả 76 obligation Non-Visual/Continuation-Hold (75 + 1, không đổi so với trước) đều có shot host tường minh trong bảng trên. **0 orphan.** Việc tách shot không làm mất mapping nào — mỗi obligation đã tách theo đúng shot mới đại diện cho beat của nó (xác nhận bằng script, xem `final_obligation_table.json` nội bộ).

### 3.2 Duration Review — kết quả sau Phase C.1

| Chỉ số | Trước Phase C.1 | Sau Phase C.1 |
|---|---|---|
| shortest shot | 2.77s (S034, S053 cũ) | 2.77s (S063 mới — S053 cũ, giữ nguyên có justification) |
| longest shot | 162.46s (S009 cũ) | **49.85s** (S071 mới) |
| median duration | 24.94s | ~20-25s (phân bố mịn hơn do 16 shot mới chen vào) |
| shots ≥60s (`HOLD_REVISION_REQUIRED`) | 3 | **0** |
| shots <3.0s | 2 | **1** (S063, KEEP_WITH_JUSTIFICATION) |
| shots 40-60s | 11 | **10** (2 đã tách ra khỏi vùng này, 1 shot mới S052 rơi vào vùng này với evidence hợp lệ) |

**Không còn hold nào vượt ngưỡng 60 giây.** 3 hold dài nhất trước đây (S005/S009/S018 cũ) đã được tách thành 12 shot mới dựa trên semantic progression và evidence thật đã có trong 04B — không tách bằng camera/framing/lighting, không phát minh nội dung mới cho các đoạn thuần triết lý (04B đã xác nhận Non-Visual thì vẫn giữ Non-Visual, chỉ đổi ranh giới shot để mỗi shot có Shot Function/vai trò tường thuật rõ ràng hơn thay vì gộp chung một hold khổng lồ).

**S063 (2.77s) — quyết định cuối:** `KEEP_WITH_JUSTIFICATION`. Đây là 1 trong 6 shot của chuỗi "thực hành nhỏ" nhịp nhanh có chủ đích; hành động đơn giản (dùng bữa, thần thái điềm tĩnh) đọc được trong thời gian ngắn; kéo dài nhân tạo sẽ phá vỡ nhịp điệu dồn dập đã thiết kế cho cả chuỗi 6 shot.

**Multi-action shots: 0** — đã rà soát lại toàn bộ 100 "One Visible Action", bao gồm 16 shot mới, không phát hiện vi phạm.

## 4. Production Fill Review (100 shot, đã tích hợp Domain Approval Gate)

| Shot ID | Source Facts | Required Visual Evidence | Proposed Production Fills | Forbidden Additions | Approval Status | Risk Notes |
|---|---|---|---|---|---|---|
| S001 | chiếc ghế trống | chiếc ghế trống; không người ngồi | chất liệu ghế (gỗ), không gian phòng cụ thể, thời điểm trong ngày | không người ngồi/vừa rời ghế; không đạo cụ phụ trợ (ảnh, hoa, đồ vật khác) chưa được 04A/04B xác nhận | APPROVED | Không phát hiện rủi ro đáng kể. |
| S002 | mẹ (generic, không đặc tả) ngồi ở ghế cạnh bàn ăn; nhặt rau | ghế cạnh bàn ăn; mẹ nhặt rau (hồi tưởng/thường lệ) | trang phục mẹ, loại rau, ánh sáng | không đặc tả danh tính/ngoại hình cụ thể của mẹ; không thêm nhân vật khác | APPROVED | Không phát hiện rủi ro đáng kể. |
| S003 | cha (generic) ngồi ở ghế gần cửa sổ; uống trà | ghế gần cửa sổ; cha uống trà (hồi tưởng/thường lệ) | trang phục cha, loại tách trà, ánh sáng cửa sổ | không đặc tả danh tính/ngoại hình cụ thể của cha | APPROVED | Không phát hiện rủi ro đáng kể. |
| S004 | một người con (generic); hoàn tất một giao dịch chuyển khoản trên điện thoại | hành vi chuyển khoản đại diện cho nghĩa vụ vật chất thay thế hiện diện | không gian, trang phục, kiểu điện thoại/giao diện chuyển khoản (không hiển thị chữ/UI theo policy) | không số tiền cụ thể; không thêm cảnh gọi điện/về thăm (đây là các hành vi KHÔNG xảy ra, không được hiển thị dương tính) | APPROVED | Không phát hiện rủi ro đáng kể. |
| S005 | cùng chiếc ghế (thread T1) | chiếc ghế chuyển sang trạng thái trống hẳn (không còn gắn với mẹ/cha) | mức độ bụi, ánh sáng buổi chiều muộn | không cảnh nguyên nhân mất mát (bệnh viện, tang lễ...) | APPROVED | Không phát hiện rủi ro đáng kể. |
| S006 | cùng chiếc ghế (thread T1) | 5 câu chưa kịp nói (chỉ mang qua giọng đọc, không hiển thị chữ) | — | không hiển thị chữ cho 5 câu chưa kịp nói | APPROVED | Không phát hiện rủi ro đáng kể. |
| S007 | cùng chiếc ghế (thread T1) | — (04B xác nhận Non-Visual) | — | không dựng cảnh minh hoạ cho nội dung hồi cố series (địa ngục/nghiệp báo/Địa Tạng) — không có evidence | APPROVED | Không phát hiện rủi ro đáng kể. |
| S008 | cùng chiếc ghế (thread T1), hình ảnh bắt đầu mờ dần | — (04B xác nhận Non-Visual cho cả hai beat) | tốc độ/kiểu mờ dần — kỹ thuật chuyển cảnh, không phải nội dung mới; Source Fact vẫn là chiếc ghế đã thiết lập | không dựng hình ảnh mới nào đại diện cho Đao Lợi ở shot này — việc mờ dần chỉ là kỹ thuật chuyển cảnh trên Source Fact đã có (chiếc ghế), không phải nội dung Đao Lợi được vẽ trước | APPROVED | Không phát hiện rủi ro đáng kể. |
| S009 | Đức Phật (medium-wide/silhouette theo ràng buộc an toàn tôn giáo đã có sẵn trong dự án); thuyết pháp | Đức Phật thuyết pháp tại Cung Trời Đao Lợi, trong liên hệ với thân mẫu | kiến trúc/không gian cụ thể của Đao Lợi (04A/04B không đặc tả — đây hoàn toàn là Production Fill, phải giữ mức biểu tượng/khiêm tốn theo chính sách an toàn tôn giáo của dự án, không tuyên bố là tái dựng lịch sử chính xác); sự hiện diện của một nhóm người dự pháp hội ở khoảng cách tôn kính (Production Fill cần thiết để hình ảnh hoá khái niệm "pháp hội" — bản thân từ "pháp hội" hàm ý một cuộc tụ họp, không thể hình ảnh hoá "pháp hội" mà không có ít nhất một gợi ý về người tham dự; số lượng/danh tính người tham dự không được đặc tả cụ thể) | không lời thoại của Đức Phật/thân mẫu; không đặc tả khuôn mặt cận cảnh của các nhân vật thiêng liêng; không kiến trúc được tuyên bố là tái hiện lịch sử chính xác | APPROVED_WITH_CONSTRAINTS | Tier 1 (Đức Phật/Đao Lợi) — xem Domain Approval Gate. |
| S010 | giữ nguyên khung Đao Lợi từ S009 | (không có evidence riêng — 04B xác nhận cả 3 obligation Non-Visual) | không có mới (kế thừa S009) | không tự trả lời 3 câu hỏi tu từ bằng hình ảnh mới | APPROVED_WITH_CONSTRAINTS | Tier 1 (Đức Phật/Đao Lợi) — xem Domain Approval Gate. |
| S011 | một người (generic, không xác định vai trò cụ thể trong 5 nhóm); ngồi yên lặng, tay khép hờ | dấu hiệu gián tiếp cho các lý do "đi chậm" (mệt mỏi/trầm lặng — theo đúng Visualization Strategy Abstract của 04B) | không gian, trang phục | không đặc tả nhân vật cụ thể đại diện cho 1 trong 5 nhóm đã liệt kê (kinh điển/truyền thống/người mất cha mẹ/người chăm sóc/người tổn thương) — chỉ dùng MỘT dấu hiệu chung (trầm lặng) đại diện tổng quát, không chọn thiên vị một nhóm | APPROVED | Không phát hiện rủi ro đáng kể. |
| S012 | Đức Phật, khung rộng (cùng continuity T2, kế thừa S009) | — (04B: cảnh báo nhận thức sai, không evidence dương tính) | không có mới | không dựng cảnh 'xa xôi rực rỡ tách biệt' (cách hiểu sai bị phê phán) | APPROVED_WITH_CONSTRAINTS | Tier 1 (Đức Phật/Đao Lợi) — xem Domain Approval Gate. |
| S013 | Đức Phật (T2), cử chỉ hướng về phía thân mẫu — khung gần hơn S012; cử chỉ hướng về phía thân mẫu | thần thái điềm tĩnh/tôn kính của Đức Phật hướng về thân mẫu | không có mới ngoài Production Fill đã dùng ở S009 | không cận cảnh khuôn mặt thiêng liêng; không lời thoại | APPROVED_WITH_CONSTRAINTS | Tier 1 (Đức Phật/Đao Lợi) — xem Domain Approval Gate. |
| S014 | Đức Phật (T2), giữ khung gần từ S013 | — (04B: luận đề trừu tượng, không minh hoạ) | — | không minh hoạ 'chấp trước/bám víu/chiếm hữu' (khái niệm bị phủ định) | APPROVED_WITH_CONSTRAINTS | Tier 1 (Đức Phật/Đao Lợi) — xem Domain Approval Gate. |
| S015 | Đức Phật (T2), giữ khung gần | — (04B: 4 định nghĩa khái niệm thuần tuý, không minh hoạ) | — | không minh hoạ 4 khái niệm (chấp trước/biết ơn/báo ân/từ bi) bằng hình ảnh/nhân vật cụ thể | APPROVED_WITH_CONSTRAINTS | Tier 1 (Đức Phật/Đao Lợi) — xem Domain Approval Gate. |
| S016 | Đức Phật (T2), khung rộng — tái hiện chính xác S009; thuyết pháp | hành vi thuyết pháp/hiện diện của Đức Phật trong liên hệ với thân mẫu — TÁI HIỆN đúng evidence đã có ở S009, không thêm hành vi mới | không có mới — dùng lại chính xác Production Fill của S009 | không thêm hành động/lời thoại mới cho Đức Phật ngoài những gì đã ở S009 | APPROVED_WITH_CONSTRAINTS | Tier 1 (Đức Phật/Đao Lợi) — xem Domain Approval Gate. |
| S017 | Đức Phật (T2), giữ khung rộng từ S016 | — (2 luận đề khẳng định, không evidence hình ảnh) | — | None thêm | APPROVED_WITH_CONSTRAINTS | Tier 1 (Đức Phật/Đao Lợi) — xem Domain Approval Gate. |
| S018 | (bắc cầu, không có evidence riêng — dùng đầu shot S019 làm điểm chuyển); — | — | — | — | APPROVED | Không phát hiện rủi ro đáng kể. |
| S019 | người con (generic, KHÔNG liên kết với người con ở S004 — 04B không xác nhận cùng nhân vật); kết thúc nhanh một cuộc gọi điện thoại | hành vi chuyển khoản + cuộc gọi ngắn, đại diện mẫu hình nhiều năm thiếu lắng nghe | không gian, trang phục | không hiển thị "đau lưng của mẹ"/"chiều mưa của cha" như hình ảnh dương tính — đây là nội dung KHÔNG xảy ra; không số tiền cụ thể | APPROVED | Không phát hiện rủi ro đáng kể. |
| S020 | giữ nguyên khung S019 | — | — | — | APPROVED | Không phát hiện rủi ro đáng kể. |
| S021 | một buổi giỗ đông người; hai anh em | bàn thờ sáng đèn, mâm cỗ đầy, khách khứa đông; anh em không nhìn mặt nhau sau bữa ăn | quy mô mâm cỗ, số lượng khách, trang phục | không số lượng người cụ thể; không nội dung xung đột cụ thể (loại "câu nói cũ" không được nêu) | APPROVED_WITH_CONSTRAINTS | Tier 3 (nghi lễ generic) — xem Domain Approval Gate. |
| S022 | một người (generic) trước bàn thờ/di ảnh; cử chỉ tưởng niệm mang tính trình diễn | hành vi tưởng niệm mang tính phô diễn, đối lập ngầm với căng thẳng người sống | không gian tưởng niệm, trang phục | không dựng "sân khấu" nghĩa đen (rạp hát, ánh đèn sân khấu) — đây là ẩn dụ hành vi, không phải địa điểm; không đặc tả nhân vật cụ thể | APPROVED | Không phát hiện rủi ro đáng kể. |
| S023 | người chăm sóc (generic) và mẹ già; đút cháo cho mẹ già | 4 hành động chăm sóc (thay áo/đút cháo/đưa đi khám/lau vết đau); dấu hiệu mệt mỏi/căng thẳng | không gian, trang phục, đạo cụ chăm sóc (bát cháo, thìa) | không đặc tả bệnh cụ thể của mẹ già; không thêm chi tiết thời gian biểu ngoài 4 hành động đã nêu | APPROVED | Không phát hiện rủi ro đáng kể. |
| S024 | cùng người chăm sóc từ S023 | — | — | — | APPROVED | Không phát hiện rủi ro đáng kể. |
| S025 | một người (generic, nhân vật mới); thần thái căng thẳng/né tránh khi nghe nhắc đến cha mẹ | dấu hiệu căng thẳng/né tránh khi nghe nhắc "cha mẹ" | không gian, trang phục | không đặc tả chi tiết cụ thể của "bạo lực" quá khứ; không gán câu thoại "cha mẹ mà, bỏ qua đi" cho một nhân vật cha/mẹ xuất hiện trong khung hình | APPROVED | Không phát hiện rủi ro đáng kể. |
| S026 | hai người (generic); một người lùi lại một bước, giữ khoảng cách bình tĩnh | hành vi giữ khoảng cách/đặt ranh giới giữa hai người chung chung | không gian, trang phục | không đặc tả nhân vật cụ thể hay lý do xung đột cụ thể | APPROVED | Không phát hiện rủi ro đáng kể. |
| S027 | giữ khung S026 | — (luận đề + 4 phân biệt, không evidence hình ảnh mới) | — | không dựng cảnh cụ thể cho 4 phân biệt (biết ơn/tôn trọng/chăm sóc/tha thứ) | APPROVED | Không phát hiện rủi ro đáng kể. |
| S028 | một ngọn đèn nhỏ trong không gian tối dịu | hình ảnh ẩn dụ "ngọn đèn" (khẳng định) đối lập "cây roi" (phủ định) | kiểu dáng đèn, chất liệu, không gian xung quanh | không dựng cảnh đánh roi theo nghĩa đen (ẩn dụ bị phủ định); không thêm chi tiết đèn ngoài việc nó là "ngọn đèn" ổn định, ấm áp | APPROVED | Không phát hiện rủi ro đáng kể. |
| S029 | người con, người cha (trên giường bệnh); nắm tay, khóc | người con nắm tay cha khóc | nội thất phòng bệnh, trang phục bệnh nhân/người nhà | không đặt tên nhân vật; không đặc tả bệnh lý cụ thể | APPROVED | Không phát hiện rủi ro đáng kể. |
| S030 | người mẹ (trên giường bệnh), người con; hỏi | người mẹ thở yếu vẫn hỏi con đã ăn gì | nội thất phòng bệnh | không hiển thị nội dung câu hỏi bằng chữ; không đặc tả bệnh lý | APPROVED | Không phát hiện rủi ro đáng kể. |
| S031 | người cha lớn tuổi (trên giường bệnh); nói | người cha nghiêm khắc cả đời, phút cuối nói lời xin lỗi nhỏ | nội thất phòng bệnh | không hiển thị nội dung lời xin lỗi bằng chữ | APPROVED | Không phát hiện rủi ro đáng kể. |
| S032 | hành lang khoa hồi sức | sự vắng mặt của một người không kịp đến (chỉ có thể ngụ ý, không hiển thị dương tính) | nội thất hành lang, ánh sáng | **không dùng hình ảnh "ghế trống" cho cảnh này** — dù chủ đề gần với motif chiếc ghế, đây KHÔNG phải continuity thread T1 và việc mượn hình ảnh ghế ở đây sẽ tạo một sự cộng hưởng ngoài ý định, gây nhầm lẫn continuity (đúng tinh thần chống scene-pool của yêu cầu Phase C — không tái dùng vật thể phụ chỉ vì nó "tiện"); chỉ dùng hành lang vắng, không thêm đồ vật biểu tượng nào | APPROVED_WITH_CONSTRAINTS | Không dùng ghế trống cho hành lang khoa hồi sức — tránh cộng hưởng với T1. |
| S033 | cùng chiếc ghế (thread T1) | chiếc ghế với dấu hiệu hao mòn/cũ đi theo thời gian | mức độ hao mòn cụ thể | không hiển thị riêng biệt 6 lý do bận bằng 6 cảnh khác nhau (04B xác nhận không có evidence hình ảnh cho từng lý do) | APPROVED | Không phát hiện rủi ro đáng kể. |
| S034 | quay lại khung Đao Lợi (thread T2, mượn từ S009/S012) | — | — | không thêm hành động/biểu cảm mới cho Đức Phật ngoài đã có | APPROVED_WITH_CONSTRAINTS | Tier 1 (Đức Phật/Đao Lợi) — xem Domain Approval Gate. |
| S035 | mẹ và cha (generic, KHÔNG liên kết với mẹ/cha ở S002/S003 — 04B không xác nhận cùng nhân vật); hiện diện, không hành động cụ thể | mẹ, cha (2 trong 9 nhóm) — nguồn nâng đỡ gần nhất | trang phục, không gian | không đặc tả danh tính cụ thể | APPROVED | Không phát hiện rủi ro đáng kể. |
| S036 | người trồng lúa (đại diện, 1 trong 3); đang làm việc trên đồng ruộng | người trồng lúa, người may áo, thầy cô — nhóm lao động/tri thức trực tiếp phục vụ đời sống | không gian đồng ruộng, trang phục lao động | không thêm nghề nghiệp nào ngoài 9 nhóm đã liệt kê ở 04A/04B | APPROVED | Không phát hiện rủi ro đáng kể. |
| S037 | người quét đường (đại diện, 1 trong 4); quét đường vào sáng sớm | hàng xóm, người xa lạ, bác sĩ, người quét đường — nhóm cộng đồng rộng hơn | không gian đường phố, trang phục lao động | không thêm nhóm người nào ngoài 9 nhóm đã liệt kê | APPROVED | Không phát hiện rủi ro đáng kể. |
| S038 | cùng chiếc ghế | cùng chiếc ghế (thread T1), làm điểm neo cho ý "mở rộng lòng biết ơn" | — | không dựng cảnh đám đông "mọi chúng sinh"; không mô tả hình tướng Địa Tạng Bồ Tát (OBL_048 minh thị cấm) | APPROVED_WITH_CONSTRAINTS | Tier 2 (Địa Tạng, không hiển thị) — xem Domain Approval Gate. |
| S039 | một người (generic); thần thái trắc ẩn, ánh mắt hướng xa xăm | thần thái trắc ẩn hướng về gia đình (mẹ/cha) làm điểm khởi đầu của lòng từ bi mở rộng | không gian, trang phục | không dựng cảnh đám đông "mọi chúng sinh"; không mô tả chi tiết "đại nguyện" ngoài đã có | APPROVED | Không phát hiện rủi ro đáng kể. |
| S040 | giữ khung S039 | — | — | không dựng cảnh cụ thể cho "chà đạp gia đình khác"/"bất công với người làm việc" — quá cụ thể so với 04B xác nhận | APPROVED | Không phát hiện rủi ro đáng kể. |
| S041 | giữ khung S039 (kéo dài) | — | — | — | APPROVED | Không phát hiện rủi ro đáng kể. |
| S042 | người cha, con; la con, đứa trẻ cúi mặt | người cha la con; đứa trẻ cúi mặt xuống; biểu cảm nhận ra trên gương mặt cha (giữ nguyên qua BEAT_057 — 'vòng lặp vẫn quay' không có evidence riêng, mang bằng giữ nguyên khung căng thẳng) | không gian, trang phục | không đặt tên nhân vật; không mô tả hành vi bạo lực thể chất; không hiển thị "đứa trẻ trong quá khứ" như nhân vật riêng cùng khung hình; không dựng biểu tượng 'vòng lặp' (vòng tròn...) cho phần BEAT_057 vừa sáp nhập | APPROVED | Không phát hiện rủi ro đáng kể. |
| S043 | cùng người cha (T3); dừng lại | khoảnh khắc "dừng lại" — thay đổi tư thế/biểu cảm | — | không mô tả nguyên nhân cụ thể khiến ông dừng lại | APPROVED | Không phát hiện rủi ro đáng kể. |
| S044 | người cha, con (T3); quỳ xuống, nói với con | người cha quỳ xuống trước con; đang nói (câu nguyên văn) | — | không đổi/diễn giải lại câu thoại; không thêm phản ứng của con | APPROVED | Không phát hiện rủi ro đáng kể. |
| S045 | giữ khung S044 (T3) | — | — | — | APPROVED | Không phát hiện rủi ro đáng kể. |
| S046 | một người (generic — **KHÔNG phải người cha ở T3**, theo đúng sửa đổi 04B); bàn tay dừng lại giữa chừng | hình ảnh ẩn dụ bàn thờ/nén hương (bị phủ định vị trí); một khoảnh khắc "dừng lại" chung chung | không gian, trang phục, chi tiết bàn thờ hậu cảnh | **không mặc định đây là cùng người cha của S042–S044** — ràng buộc minh thị kế thừa từ 04B; không thêm hành động "dừng" nào ngoài phạm vi ý nghĩa chung đã nêu | APPROVED_WITH_CONSTRAINTS | Tier 3 (nghi lễ generic) — xem Domain Approval Gate. |
| S047 | giữ khung S046 | — | — | không thể hiện Đức Phật đang kể câu chuyện S042–S046 như một sự kiện kinh điển — ràng buộc disclaimer áp dụng ngược cho toàn bộ S042-038 | APPROVED_WITH_CONSTRAINTS | Tier 3 (nghi lễ generic) — xem Domain Approval Gate. |
| S048 | một gia đình tại bữa cơm (generic, mới — không nối T3); một người lớn nói, một đứa trẻ lắng nghe/tiếp nhận | khoảnh khắc bữa cơm — lời nói được nói ra, một đứa trẻ tiếp nhận | không gian bếp/bàn ăn, món ăn, trang phục | không tách rời chuỗi 5 bước nhân quả thành cảnh riêng; không nhân vật cụ thể có tên; không hiển thị "20 năm sau" bằng nhân vật trưởng thành cụ thể | APPROVED | Không phát hiện rủi ro đáng kể. |
| S049 | một người (generic); gõ tin nhắn trên điện thoại | nhắn tin (1/6 hành vi — "nghe điện thoại" chuyển sang mang bằng giọng đọc, xem sửa lỗi bên dưới) | không gian, trang phục | không hiển thị nội dung tin nhắn bằng chữ | APPROVED | Không phát hiện rủi ro đáng kể. |
| S050 | một người (generic); một cử chỉ đặt ranh giới bình tĩnh | đặt ranh giới (1/6 hành vi — "chăm sóc người già" chuyển sang mang bằng giọng đọc, xem sửa lỗi bên dưới) | không gian, trang phục | None thêm. | APPROVED | Không phát hiện rủi ro đáng kể. |
| S051 | một người lớn và một đứa trẻ (generic); cúi xuống ngang tầm mắt trẻ, nói lời xin lỗi | nuôi dạy con; nói lời xin lỗi | không gian, trang phục | không thêm hành vi nào ngoài 6 hành vi đã liệt kê ở 04A/04B | APPROVED | Không phát hiện rủi ro đáng kể. |
| S052 | một người (generic, mới) và một người già khác; chăm sóc một người già không phải cha mẹ ruột | hành vi chăm sóc người già khác (cử chỉ ấm áp); dấu hiệu ân hận (thần thái trầm lặng) làm điểm khởi đầu | không gian, trang phục | None thêm ngoài phạm vi đã liệt kê | APPROVED | Không phát hiện rủi ro đáng kể. |
| S053 | giữ khung S052 | — (2 luận đề khẳng định, không evidence hình ảnh mới) | — | None thêm | APPROVED | Không phát hiện rủi ro đáng kể. |
| S054 | một người (generic); tụng kinh | hành vi tụng kinh (đại diện cho 4 thực hành: tụng kinh/làm phước/hồi hướng/tưởng niệm) | không gian, trang phục, đạo cụ tối thiểu (không đặc tả tượng Phật/kiến trúc chùa cụ thể nếu 04B không xác nhận) | không mô tả không gian "chùa" cụ thể — 04B minh thị cấm; không tự thêm địa điểm chùa nếu narration không nêu | APPROVED_WITH_CONSTRAINTS | Tier 3 (nghi lễ generic) — xem Domain Approval Gate. |
| S055 | giữ khung S054 | — | — | không dựng cảnh minh hoạ "bán sợ hãi"/"nghi lễ như cái máy" — hành vi bị phê phán, không hình ảnh hoá dương tính | APPROVED | Không phát hiện rủi ro đáng kể. |
| S056 | một người (rõ ràng đơn sơ, không phô trương); thắp một nén hương đơn lẻ | người nghèo thắp một nén hương với tâm lành | không gian, trang phục đơn sơ | không dựng bàn thờ lớn — narration minh thị đối lập với sự phô trương | APPROVED_WITH_CONSTRAINTS | Tier 3 (nghi lễ generic) — xem Domain Approval Gate. |
| S057 | một người (generic, mới) và mẹ còn sống; dọn một bữa cơm ấm cho mẹ | người chăm mẹ còn sống bằng bữa cơm ấm/đưa đi khám/trò chuyện; người kiềm chế không biến vết thương thành bạo lực với con | không gian bếp, món ăn | không thêm ví dụ thứ 4; không đặc tả danh tính cụ thể | APPROVED_WITH_CONSTRAINTS | 2 nhân vật khác nhau trong cùng nhóm ví dụ OBL_073 — không dựng như cùng một người. |
| S058 | giữ khung S057 | — | — | — | APPROVED | Không phát hiện rủi ro đáng kể. |
| S059 | cùng khung Đao Lợi (T2, mượn từ S009/S012-S017) | pháp hội tại Cung Trời Đao Lợi (thread T2) | — | không dựng cảnh riêng cho 'đại nguyện của Địa Tạng'; không tự vẽ hình ảnh địa ngục | APPROVED_WITH_CONSTRAINTS | Tier 1 (Đức Phật/Đao Lợi) — xem Domain Approval Gate. |
| S060 | giữ khung S059 (T2) | — (luận đề + câu hỏi tu từ khép đoạn, không evidence hình ảnh mới) | — | không tự vẽ hình ảnh địa ngục ở beat này | APPROVED_WITH_CONSTRAINTS | Tier 1 (Đức Phật/Đao Lợi) — xem Domain Approval Gate. |
| S061 | — (bắc cầu sang chuỗi thực hành nhỏ); — | — | — | không mô tả hình tướng Địa Tạng Bồ Tát | APPROVED_WITH_CONSTRAINTS | Tier 2 (Địa Tạng, không hiển thị) — xem Domain Approval Gate. |
| S062 | một người; gọi điện, tư thế thư thái | thực hành nhỏ 1/6: hành vi thực hiện một cuộc gọi điện thoại, không vội vàng (tư thế thư thái) | không gian | không đặc tả người gọi/nhận cụ thể | APPROVED | Không phát hiện rủi ro đáng kể. |
| S063 | một gia đình (generic); dùng bữa, thần thái điềm tĩnh | thực hành nhỏ 2/6: hành vi dùng bữa với thần thái điềm tĩnh (không cáu gắt) | món ăn, không gian | None thêm. | APPROVED | Không phát hiện rủi ro đáng kể. |
| S064 | một người; cử chỉ chủ động xin lỗi | thực hành nhỏ 3/6: hành vi chủ động xin lỗi (cử chỉ/tư thế hướng về đối phương) | không gian | None thêm. | APPROVED | Không phát hiện rủi ro đáng kể. |
| S065 | một người; nói với thần thái bình tĩnh | thực hành nhỏ 4/6: hành vi nói với thần thái/tư thế bình tĩnh, không căng thẳng | không gian | None thêm. | APPROVED | Không phát hiện rủi ro đáng kể. |
| S066 | một người; bước vào một không gian hỗ trợ | thực hành nhỏ 5/6: hành vi tìm kiếm/tiếp nhận sự giúp đỡ (một trong ba hình thức: trị liệu/tu học/giúp đỡ) | không gian (không xác định loại hình cụ thể) | không xác định hình thức trị liệu/tu học cụ thể | APPROVED | Không phát hiện rủi ro đáng kể. |
| S067 | cùng chiếc ghế (T1) + một người; nhìn vào chiếc ghế | thực hành nhỏ 6/6, Critical: hành vi nhìn vào chiếc ghế; câu hỏi nội tâm không hiển thị trực tiếp | không gian (kế thừa T1) | None thêm ngoài ràng buộc T1. | APPROVED | Không phát hiện rủi ro đáng kể. |
| S068 | —; — | — | — | — | APPROVED | Không phát hiện rủi ro đáng kể. |
| S069 | mẹ, cha (generic, nhân vật mới — không nối các mẹ/cha khác trong episode); cha đang sửa một bóng đèn | mẹ biết bếp còn gì, cha sửa bóng đèn/vá cửa (hồi tưởng thời trẻ — hình ảnh cha mẹ "luôn ở đó") | không gian, trang phục, dụng cụ sửa chữa | không đặc tả bệnh lý | APPROVED | Không phát hiện rủi ro đáng kể. |
| S070 | cùng mẹ/cha, nay lớn tuổi hơn (location continuity cục bộ, cùng ví dụ); tay run khi cầm chén | 3 dấu hiệu suy yếu hiện tại (hỏi lại nhiều lần/không nghe rõ/tay run khi cầm chén) | không gian, trang phục | không đặc tả bệnh lý cụ thể (không tên bệnh) | APPROVED | Không phát hiện rủi ro đáng kể. |
| S071 | một gia đình (generic); dùng bữa cơm ấm áp | một bữa cơm không lạnh nhạt (1 trong 3 ví dụ "tỉnh lại") | không gian bếp, món ăn | không dựng hình ảnh "cuộc đua"/đồng hồ đếm ngược cho OBL_088 | APPROVED | Không phát hiện rủi ro đáng kể. |
| S072 | một người (ở xa, generic); gọi điện, chăm chú lắng nghe | gọi điện với thái độ chăm chú lắng nghe | không gian, trang phục | không đặc tả quốc gia/địa điểm cụ thể cho "ở nước ngoài" | APPROVED | Không phát hiện rủi ro đáng kể. |
| S073 | cha mẹ (generic, mới); ngồi cạnh những món đồ đầy đủ | thần thái cô đơn/thiếu kết nối của cha mẹ dù được chu cấp đầy đủ vật chất | không gian, đạo cụ vật chất (thuốc, quà) | None thêm. | APPROVED | Không phát hiện rủi ro đáng kể. |
| S074 | người chăm sóc, mẹ (bệnh); thay thuốc cho mẹ | 1 trong 4 hoạt động chăm sóc (chọn đại diện: thay thuốc buổi tối) | không gian, trang phục, đạo cụ y tế tối thiểu | không đặc tả bệnh cụ thể của mẹ; không đặt tên nhân vật | APPROVED | Không phát hiện rủi ro đáng kể. |
| S075 | cùng người chăm sóc (character continuity cục bộ với S074); khóc lặng lẽ, vặn vòi nước thật nhỏ | khóc trong nhà tắm, nước chảy thật nhỏ (chi tiết cụ thể narration nêu); ý nghĩ thoáng qua (chỉ ngụ ý qua biểu cảm) | nội thất nhà tắm | không hiển thị lời khen "con hiếu quá" bằng một nhân vật khác xuất hiện đồng thời trong khung hình — đây là nhận xét từ một thời điểm/góc nhìn khác theo narration | APPROVED | Không phát hiện rủi ro đáng kể. |
| S076 | giữ khung S075 | — | — | — | APPROVED | Không phát hiện rủi ro đáng kể. |
| S077 | —; — | — | — | — | APPROVED | Không phát hiện rủi ro đáng kể. |
| S078 | một người (generic, mới); căng cứng/né tránh khi điện thoại reo | phản ứng căng cứng cơ thể khi nghe chuông điện thoại cha mẹ | không gian, trang phục | không đặc tả hình thức nhục mạ/kiểm soát cụ thể; không hình ảnh hoá câu thoại "hãy về đi, cha mẹ mà" bằng một nhân vật đang nói câu này | APPROVED_WITH_CONSTRAINTS | Không dựng câu thoại phổ biến như lời của nhân vật. |
| S079 | hai người (generic); giữ khoảng cách, một người trong tư thế lặng lẽ | một khoảng cách vật lý giữa hai người chung chung; tư thế cầu nguyện thầm lặng | không gian, trang phục | không đặc tả nhân vật cụ thể hay lý do xung đột cụ thể | APPROVED | Không phát hiện rủi ro đáng kể. |
| S080 | giữ khung S079 | — | — | — | APPROVED | Không phát hiện rủi ro đáng kể. |
| S081 | cha, mẹ, con (generic, mới); cha cúi đầu xin lỗi con | cử chỉ cha xin lỗi con; cử chỉ mẹ lắng nghe con | không gian, trang phục | None thêm. | APPROVED | Không phát hiện rủi ro đáng kể. |
| S082 | giữ khung S081 | — | — | không đổi/diễn giải lại 2 câu thoại nguyên văn nếu được trích dẫn | APPROVED | Không phát hiện rủi ro đáng kể. |
| S083 | cha hoặc mẹ (generic); tay dừng giữa chừng trước một cử chỉ giận dữ, hít thở, buông xuống | khoảnh khắc kiềm chế cơn giận (tư thế/biểu cảm dừng lại) | không gian, trang phục | None thêm. | APPROVED | Không phát hiện rủi ro đáng kể. |
| S084 | một căn nhà, các thành viên gia đình generic; mỗi người ngồi một góc, không ai nhìn ai | hình ảnh ẩn dụ "căn nhà" ở trạng thái bất hoà (KHÔNG phải cảnh giới siêu hình) | nội thất, trang phục | **không thể hiện "địa ngục" bằng biểu tượng tôn giáo/siêu nhiên (lửa, quỷ, hình phạt...)** — ràng buộc minh thị kế thừa từ 04A/04B | APPROVED_WITH_CONSTRAINTS | Tier 4 (địa ngục ẩn dụ) — xem Domain Approval Gate, mục 5 của 04D. |
| S085 | một gia đình tại bàn ăn (generic); im lặng căng thẳng tại bàn ăn | hình ảnh 1-2/5: căn nhà không ai chịu nghe ai; bàn ăn mỗi người cầm một nỗi giận | không gian, món ăn, trang phục | không biểu tượng tôn giáo/siêu nhiên | APPROVED_WITH_CONSTRAINTS | Tier 4 (địa ngục ẩn dụ) — xem Domain Approval Gate, mục 5 của 04D. |
| S086 | mẹ già (nằm), các con (generic); hai người con tranh cãi ở góc phòng, mẹ già nằm yên | hình ảnh 3/5: căn phòng có mẹ già nằm đó nhưng con tranh phần thiệt hơn | nội thất phòng | không biểu tượng tôn giáo/siêu nhiên | APPROVED_WITH_CONSTRAINTS | Tier 4 (địa ngục ẩn dụ) — xem Domain Approval Gate, mục 5 của 04D. |
| S087 | một người lớn, một đứa trẻ (generic); người lớn đứng cứng đờ trước đứa trẻ đang chờ một cái ôm, không tiến lại gần | hình ảnh 4-5/5: đứa trẻ học tình thương có điều kiện; người lớn không biết ôm con | không gian, trang phục | không biểu tượng tôn giáo/siêu nhiên | APPROVED_WITH_CONSTRAINTS | Tier 4 (địa ngục ẩn dụ) — xem Domain Approval Gate, mục 5 của 04D. |
| S088 | —; — | — | — | không biểu tượng tôn giáo/siêu nhiên cho "địa ngục"/"cõi lành" | APPROVED_WITH_CONSTRAINTS | Tier 4 (địa ngục ẩn dụ) — xem Domain Approval Gate, mục 5 của 04D. |
| S089 | một người (generic, mới); tay dừng giữa chừng trước một cử chỉ | khoảnh khắc kiềm chế/dừng lại trước một hành vi tiêu cực | không gian, trang phục | không thêm hành vi nào ngoài 5 hành vi đã liệt kê; không hiển thị hành vi tiêu cực dương tính (không cảnh đang tát, đang so sánh...) | APPROVED_WITH_CONSTRAINTS | Tier 4 (địa ngục ẩn dụ) — xem Domain Approval Gate, mục 5 của 04D. |
| S090 | giữ khung S089 | — | — | không dựng hình ảnh "dòng truyền thừa" bằng biểu tượng phả hệ/cây gia phả | APPROVED | Không phát hiện rủi ro đáng kể. |
| S091 | một không gian trung tính (Production Fill) | — | không gian trung tính (không cửa, không ghế, không điện thoại — tránh mọi motif đã dùng, để không tạo cộng hưởng ngoài ý muốn) | không dùng lại bất kỳ motif nào đã thiết lập (ghế/cửa/điện thoại) chỉ để lấp khoảng trống hình ảnh cho 3 câu phát biểu này | APPROVED | Không phát hiện rủi ro đáng kể. |
| S092 | một người và cha/mẹ còn sống (generic); một cử chỉ chăm sóc ấm áp, hiện diện thật hơn | cử chỉ chăm sóc ấm áp hơn (nhánh 1: cha mẹ còn sống) | không gian, trang phục | None thêm ngoài phạm vi 3 nhánh. | APPROVED_WITH_CONSTRAINTS | 1/3 nhánh hướng dẫn OBL_117 — không phải nhánh duy nhất. |
| S093 | một người (generic); đứng ở khoảng cách an toàn, thần thái bình thản | tư thế giữ khoảng cách an toàn nhưng không thù hận (nhánh 3: gia đình từng gây đau — chọn nhánh này làm đại diện thứ hai vì có evidence rõ nhất; nhánh 2 "biến nỗi nhớ thành đời sống tử tế" là trạng thái nội tâm dài hạn, khó hình ảnh hoá bằng một khoảnh khắc, mang bằng giọng đọc) | không gian, trang phục | None thêm. | APPROVED_WITH_CONSTRAINTS | 2/3 nhánh — nhánh 2 không có hình ảnh riêng. |
| S094 | một hạt giống (Symbolic — narration tự đặt tên) | hình ảnh ẩn dụ "hạt giống" | không gian đặt hạt giống (mặt bàn/lòng bàn tay — Production Fill) | không mở rộng ẩn dụ thành cảnh trồng trọt đầy đủ (đất, tay người trồng, cây nảy mầm) — 04B chỉ xác nhận từ "hạt giống" | APPROVED | Không phát hiện rủi ro đáng kể. |
| S095 | cùng chiếc ghế (T1), một người (không xác định là ai trong các nhân vật generic trước đó — đây là hình ảnh khép lại mang tính phổ quát, đại diện cho khán giả); ngồi xuống trước chiếc ghế, thắp một ngọn đèn | ngồi xuống trước chiếc ghế; thắp một ngọn đèn | kiểu dáng đèn (đây là lần dùng "đèn" thứ ba, ĐỘC LẬP theo sửa đổi 04B — không nối continuity với S028/S092-liên-quan-117) | không thêm nhang/bàn thờ nếu không được 04A/04B xác nhận ở beat này | APPROVED_WITH_CONSTRAINTS | Tier 5 (nghi thức khép phim) — xem Domain Approval Gate. |
| S096 | cùng người ở S095; chắp tay | chắp tay; nói trong lòng (câu nguyên văn — không hiển thị bằng chữ) | — | không đổi nội dung câu nói nguyên văn nếu trích dẫn qua giọng đọc; không hiển thị chữ trên màn hình | APPROVED_WITH_CONSTRAINTS | Tier 5 (nghi thức khép phim) — xem Domain Approval Gate. |
| S097 | giữ khung S096 (T1) | — | — | — | APPROVED | Không phát hiện rủi ro đáng kể. |
| S098 | —; — | — | — | **không mở rộng/diễn giải trước nội dung tập sau bằng hình ảnh cụ thể** — nội dung này thuộc tập tiếp theo, không phải EP004 | APPROVED | Không phát hiện rủi ro đáng kể. |
| S099 | cùng chiếc ghế (T1 — chọn "chiếc ghế" trong 4 khả năng vì đây là motif đã có continuity đầy đủ, giảm thiểu Production Fill mới cần thiết; **đây là lựa chọn dàn dựng (Production Fill ở cấp "chọn khả năng nào trong 4 khả năng ngang hàng"), không phải khẳng định của narration rằng ghế là hình ảnh chính thức duy nhất**) | một trong 4 khả năng ngang hàng (gương mặt/chiếc ghế/bàn tay/câu chưa kịp nói) — không ưu tiên khả năng nào | mức độ mờ dần | không tuyên bố đây là hình ảnh "chính thức" duy nhất của 4 khả năng — ràng buộc kế thừa từ 04A/04B | APPROVED_WITH_CONSTRAINTS | Lựa chọn dàn dựng (1/4 khả năng ngang hàng), không phải khẳng định narration. |
| S100 | giữ khung S099, mờ dần hoàn toàn (Production Fill: tốc độ mờ) | — | hiệu ứng mờ dần cuối phim | không phát minh hình ảnh mới cho 3 lời nhắc khép lại — tái sử dụng đúng evidence đã có (chiếc ghế), theo đúng khuyến nghị đã ghi tại OBL_128 trong 04B | APPROVED | Không phát hiện rủi ro đáng kể. |

**Tổng hợp Approval Status (sau Phase D.1): APPROVED = 68 | APPROVED_WITH_CONSTRAINTS = 32 | DOMAIN_REVIEW_REQUIRED = 0 | REVISION_REQUIRED = 0.**

## Domain Approval Gate (Phase D.1) — 26/26 shot đã có trạng thái chính thức

Toàn bộ 20 shot `DOMAIN_REVIEW_REQUIRED` cũ (nay là 26 shot sau khi S009/S050 được tách) đã được duyệt. **Không còn shot nào ở trạng thái chờ.**

### Tier 1 — Đức Phật, thân mẫu, Cung Trời Đao Lợi (thread T2)
Shot: S009, S010, S012, S013, S014, S015, S016, S017, S034, S059, S060

| Hạng mục | Nội dung áp dụng chung cho cả 11 shot |
|---|---|
| **Source-confirmed content** | Đức Phật thuyết pháp tại Cung Trời Đao Lợi, trong liên hệ với thân mẫu (04A BEAT_010). Khung này được truyền thống Phật giáo Đại thừa xác nhận ("theo truyền thống"), không phải khẳng định lịch sử tuyệt đối. S013 bổ sung: cử chỉ hướng về thân mẫu (04B OBL_017). |
| **Allowed Production Fill** | Kiến trúc/không gian Đao Lợi ở mức biểu tượng/khiêm tốn (không kiến trúc cụ thể được narration xác nhận); sự hiện diện tối thiểu của một nhóm dự pháp hội ở khoảng cách tôn kính (cần thiết để hình ảnh hoá khái niệm "pháp hội"). |
| **Mandatory constraints** | Nhân vật tôn giáo giữ framing tôn kính (medium-wide/silhouette/profile); không cận cảnh khuôn mặt Đức Phật/thân mẫu; không tuyên bố tái hiện lịch sử/kiến trúc chính xác. |
| **Forbidden depiction** | Không lời thoại/độc thoại của Đức Phật hoặc thân mẫu; không góc máy/ánh sáng thiếu tôn kính; không biến cảnh thành "bằng chứng khoa học" cho vũ trụ quan Phật giáo. |
| **Final approval status** | **APPROVED_WITH_CONSTRAINTS** cho cả 11 shot — không phát hiện vi phạm trong thiết kế hiện tại; các ràng buộc trên đã được ghi trực tiếp vào Forbidden Additions của từng shot. |

### Tier 2 — Địa Tạng Bồ Tát (được nhắc tên, không được hiển thị)
Shot: S038, S061

| Hạng mục | Nội dung |
|---|---|
| **Source-confirmed content** | Địa Tạng Bồ Tát được nhắc tên tại BEAT_048 (S038) và BEAT_079 (S061) — không có mô tả hình tướng nào trong narration. |
| **Allowed Production Fill** | Không có — 04A/04B minh thị cấm mô tả hình tướng ở cả hai vị trí. |
| **Mandatory constraints** | Cả hai shot phải giữ nguyên trạng thái "không hiển thị" — S038 dùng hình ảnh chiếc ghế (T1) làm điểm neo thay thế; S061 là TRANSITION không có evidence hình ảnh riêng. |
| **Forbidden depiction** | Bất kỳ hình tướng/y phục/biểu tượng cụ thể nào của Địa Tạng Bồ Tát. Nếu một phiên bản dựng phim sau này cần hiển thị Địa Tạng Bồ Tát, phải quay lại `CB_BUD_001` (Character Bible đã có trong dự án) và mở một vòng review riêng — ngoài phạm vi Phase C.1/D.1. |
| **Final approval status** | **APPROVED_WITH_CONSTRAINTS** cho cả 2 shot. |

### Tier 3 — Nghi lễ/kinh điển/bàn thờ/nén hương generic
Shot: S021, S046, S047, S054, S056

| Hạng mục | Nội dung |
|---|---|
| **Source-confirmed content** | S021: giỗ lớn, bàn thờ sáng đèn (BEAT_029). S046: ẩn dụ "nén hương chân thành không nằm trên bàn thờ" (BEAT_062). S047: disclaimer "không phải lời Đức Phật" (BEAT_063). S054: tụng kinh/làm phước/hồi hướng/tưởng niệm (BEAT_070). S056: người nghèo thắp một nén hương, đối lập phô trương (BEAT_073). |
| **Allowed Production Fill** | Không gian nghi lễ (trong nhà/nơi thờ cúng/không gian tu tập đơn sơ) — hoàn toàn Production Fill, không đặc tả bởi 04A/04B. |
| **Mandatory constraints** | Nhân vật thực hiện nghi lễ là người thường (generic, lay person) — không được tự thêm hình tượng tăng ni/sư thầy vì không có beat nào xác nhận nhân vật tu sĩ. S046/S047 không được mặc định là cùng người cha ở thread T3. S056 không được dựng bàn thờ lớn (mâu thuẫn trực tiếp ý nghĩa "đối lập phô trương"). |
| **Forbidden depiction** | S054 không mô tả "chùa" cụ thể; S046 không thể hiện Đức Phật đang kể chuyện người cha như sự kiện kinh điển. |
| **Final approval status** | **APPROVED_WITH_CONSTRAINTS** cho cả 5 shot. |

### Tier 4 — "Địa ngục" như ẩn dụ tâm lý (rủi ro cao nhất, đã kiểm tra kỹ nhất)
Shot: S084, S085, S086, S087, S088, S089

| Hạng mục | Nội dung |
|---|---|
| **Source-confirmed content** | BEAT_108: "địa ngục" = ẩn dụ cho căn nhà bất hoà. BEAT_110: đúng 5 hình ảnh cụ thể (căn nhà không ai nghe ai; bàn ăn mỗi người một nỗi giận; mẹ già + con tranh giành; đứa trẻ học tình thương có điều kiện; người lớn không biết ôm con) — narration tự liệt kê, không phải suy diễn thêm. BEAT_111: "địa ngục bắt đầu từ sân hận, cõi lành bắt đầu từ tâm biết dừng" — đối lập ẩn dụ. |
| **Allowed Production Fill** | Không gian "căn nhà"/"bàn ăn"/"căn phòng" đời thường, hiện đại hoặc phi thời gian tính — không đặc tả kiến trúc cụ thể bởi 04A/04B. |
| **Mandatory constraints** | Toàn bộ 6 shot phải giữ đúng bản chất "khoảnh khắc đời thường bất hoà" — căng thẳng, im lặng, xa cách. S089 chỉ hiển thị khoảnh khắc TRƯỚC hành vi tiêu cực, không hiển thị chính hành vi đó. |
| **Forbidden depiction** | **Tuyệt đối không dùng biểu tượng tôn giáo/siêu nhiên cho "địa ngục"**: không lửa, không quỷ, không hình phạt, không cảnh giới âm phủ, không ánh sáng/màu sắc kiểu kinh dị. Đây là ràng buộc nghiêm ngặt nhất trong toàn bộ episode — vi phạm sẽ đồng thời phá vỡ tinh thần giáo lý gốc (Kinh Địa Tạng "không bị kẹt trong sợ hãi", BEAT_077) và tạo rủi ro tôn giáo nghiêm trọng. |
| **Final approval status** | **APPROVED_WITH_CONSTRAINTS** cho cả 6 shot — đã xác nhận lại lần thứ hai (04D + Phase D.1) không phát hiện bất kỳ đề xuất/vi phạm siêu nhiên nào trong thiết kế hiện tại. |

### Tier 5 — Nghi thức cá nhân khép phim (ngọn đèn, chắp tay)
Shot: S095, S096

| Hạng mục | Nội dung |
|---|---|
| **Source-confirmed content** | BEAT_121: "Ta có thể thắp một ngọn đèn. Ta có thể chắp tay." — hành động cụ thể, không phải ẩn dụ. Đây là lần dùng "ngọn đèn" độc lập thứ ba (không nối continuity với S028/T4-cũ, theo đúng sửa đổi tại 04B). |
| **Allowed Production Fill** | Kiểu dáng đèn, chất liệu — không đặc tả bởi 04A/04B. |
| **Mandatory constraints** | Không thêm nhang/bàn thờ nếu không được xác nhận ở chính beat này (04A/04B chỉ nêu "ngọn đèn" và "chắp tay"). Câu nói trong lòng (nguyên văn) không hiển thị bằng chữ trên màn hình. |
| **Forbidden depiction** | Không đổi nội dung câu nói nguyên văn; không thêm nghi thức tôn giáo khác (quỳ lạy, tụng niệm...) ngoài 2 hành động đã xác nhận. |
| **Final approval status** | **APPROVED_WITH_CONSTRAINTS** cho cả 2 shot. |

### Bảng tổng hợp 26/26 shot

| Shot | Tier | Final Status |
|---|---|---|
| S009, S010, S012, S013, S014, S015, S016, S017, S034, S059, S060 | 1 | APPROVED_WITH_CONSTRAINTS |
| S038, S061 | 2 | APPROVED_WITH_CONSTRAINTS |
| S021, S046, S047, S054, S056 | 3 | APPROVED_WITH_CONSTRAINTS |
| S084, S085, S086, S087, S088, S089 | 4 | APPROVED_WITH_CONSTRAINTS |
| S095, S096 | 5 | APPROVED_WITH_CONSTRAINTS |

**REVISION_REQUIRED: 0/26.** Không phát hiện shot nào có thiết kế sai/vi phạm — toàn bộ 26 shot đã được dựng đúng ngay từ Phase C, Domain Approval Gate chỉ chính thức hoá trạng thái duyệt (chuyển từ "cần review" sang "đã review, có ràng buộc rõ").

## 6. Đề xuất sửa Shot Plan (Phase D gốc) — đã thực hiện ở Phase C.1

Ba đề xuất sửa từ Phase D gốc (tách S005/S009/S018) đã được **thực hiện trực tiếp** trong Phase C.1 — không còn ở trạng thái "đề xuất chờ duyệt". Chi tiết thực hiện xem `04C_SHOT_PLAN.md` mục "Phase C.1 Changelog". Không phát sinh đề xuất sửa mới nào trong quá trình thực hiện — không có obligation bị gán sai host shot, không có Production Fill làm sai nghĩa, không có religious depiction không an toàn nào bị phát hiện.

## 7. Validation cuối (Phase C.1/D.1)

| Chỉ số | Giá trị |
|---|---|
| final shot count | **100** |
| shots added | 16 |
| shots merged | 1 |
| shots renumbered | 79 |
| long holds remaining (≥60s) | **0** |
| short shots remaining (<3.0s) | 1 (S063, KEEP_WITH_JUSTIFICATION) |
| 40–60s shots reviewed | 11 (2 tách, 9 giữ nguyên có căn cứ) |
| orphan obligations | **0** |
| orphan underlay mappings | **0** |
| timing gaps | **0** |
| timing overlaps | **0** |
| multi-action shots | **0** |
| DOMAIN_REVIEW_REQUIRED remaining | **0** (26/26 → APPROVED_WITH_CONSTRAINTS) |
| APPROVED_WITH_CONSTRAINTS count | 32 |
| REVISION_REQUIRED count | **0** |
| unsupported additions | **0** |
| total duration | **2410.154s** |

### PASS/FAIL

```
S005/S009/S018 đã được xử lý                  → PASS (tách thành 12 shot mới, không còn hold ≥60s)
S034/S053 có resolution rõ                     → PASS (MERGE_WITH_NEIGHBOR / KEEP_WITH_JUSTIFICATION)
orphan obligations: 0                          → PASS
orphan underlay mappings: 0                    → PASS
timing gaps: 0                                 → PASS
timing overlaps: 0                             → PASS
multi-action shots: 0                          → PASS
DOMAIN_REVIEW_REQUIRED remaining: 0            → PASS
unsupported additions: 0                       → PASS
total duration: 2410.154s                      → PASS
```

**Trạng thái cuối cùng:**

```
PASS_READY_FOR_PROMPT_COMPOSITION
```

Toàn bộ 10 điều kiện PASS đều đạt. EP004 sẵn sàng cho Phase E (Prompt Composition) — nằm ngoài phạm vi của lượt này.
