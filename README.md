# Kinh Địa Tạng — Content OS

Hệ thống sản xuất nội dung cho kênh YouTube giáo dục Phật giáo tiếng Việt "Giải Mã Kinh Địa Tạng". Đây không phải một phần mềm chạy bằng 1 lệnh — đây là một bộ tài liệu "hiến pháp" (brand, giọng văn, ranh giới giáo lý, quy trình QA) kết hợp vài công cụ Python nhỏ, được vận hành bằng cách chạy trong [Claude Code](https://claude.com/claude-code) và làm theo đúng quy trình đã thiết lập bên dưới.

Nếu bạn mới vào dự án, đọc phần **"Sản xuất 1 tập mới"** bên dưới trước — đó là cách nhanh nhất để có output dùng được.

## Dự án này tạo ra cái gì

Với mỗi tập phim (episode), hệ thống tạo ra 2 file text sẵn sàng đưa vào công cụ TTS (Text-to-Speech) bất kỳ:

```
DOMAINS/BUDDHISM/PRODUCTION_PACKAGES/KINH_DIA_TANG/EP0XX/
  Long/   → 1 file .txt — kịch bản Long-form hoàn chỉnh (~9500-11500 từ, ~35-45 phút @ tốc độ TTS mặc định)
  Short/  → 1 file .txt — 30 kịch bản Shorts, ngăn cách bằng `*** 1`, `*** 2`, ... `*** 30`
```

Không có gì khác cần làm để dùng 2 file này — copy nội dung dán thẳng vào TTS.

## Bản đồ thư mục

| Thư mục | Nội dung |
|---|---|
| `CORE_OS/` | "Hiến pháp" chung của kênh — brand, giọng văn, quy tắc production/QA/growth. Đọc `BRAND_BIBLE.md` và `SHORTS_ENGINE.md` trước khi viết bất kỳ nội dung nào. |
| `DOMAINS/BUDDHISM/` | Toàn bộ kiến thức Phật giáo: knowledge packet (`KNOWLEDGE_PACKETS/KP_BUD_001_...md`), character bible (`CHARACTER_BIBLES/`, 11 nhân vật), nguồn (`SOURCES/`), và **`CONTINUITY_REGISTRY.md`** — file bắt buộc đọc trước mỗi tập mới (thuật ngữ chuẩn, lỗi đã phát hiện, câu chuyện/ẩn dụ đã dùng ở tập nào). |
| `DOMAINS/BUDDHISM/SERIES_BIBLES/SEASON_01_PRODUCTION_PLAN.md` | Danh sách 15 tập Season 1 — nguồn sự thật duy nhất cho việc tập số N nói về chủ đề gì. |
| `DOMAINS/BUDDHISM/PRODUCTION_PACKAGES/KINH_DIA_TANG/` | Output từng tập (xem cấu trúc `EP0XX/Long`, `Short`, `_PRODUCTION` ở dưới). |
| `TOOLS/` | 2 script Python: `package_audit.py` (kiểm tra chất lượng 1 gói) và `build_short_package.py` (đóng gói hàng loạt Shorts). |
| `REGISTRIES/` | Đăng ký ID/asset toàn hệ thống, không cần đụng vào trừ khi tạo asset mới (knowledge packet, character bible...). |

### Bên trong 1 tập (`EP0XX/`)

```
EP0XX/
  Long/                    ← file .txt cuối cùng, sẵn dùng
  Short/                   ← file .txt cuối cùng, sẵn dùng
  _PRODUCTION/             ← hồ sơ sản xuất đầy đủ, chỉ cần khi muốn kiểm tra lại nguồn gốc
    Long/_INTERNAL/
      01_RESEARCH_BRIEF.md       nghiên cứu chủ đề + ranh giới rủi ro
      02_EPISODE_PLANNER.md      outline theo beat
      03_AUDIO_SCRIPT_MASTER.md  kịch bản gốc (có markers NARRATION_START/END)
      06_QA_REPORT.md            báo cáo QA độc lập
      manifest.json              metadata máy đọc được
      PACKAGE_AUDIT_REPORT.md    kết quả chạy package_audit.py
    Short/EP0XX_SHORT_01../30/   30 gói tương tự, mỗi Short 1 gói riêng
```

## Sản xuất 1 tập mới

Đây là quy trình đã kiểm chứng qua nhiều tập (EP001, EP005, EP006). Mở Claude Code trong thư mục này, rồi yêu cầu theo trình tự — Claude Code sẽ tự orchestrate qua các subagent:

1. **"Sản xuất tập N"** — Claude Code sẽ: đọc `SEASON_01_PRODUCTION_PLAN.md` để lấy đúng chủ đề, đọc `CONTINUITY_REGISTRY.md` để tránh lặp/lỗi đã biết, rồi chạy tuần tự: research brief → episode planner → kịch bản Long-form → QA độc lập → tách TTS + dựng `manifest.json` → chạy `package_audit.py`.
2. **"Làm 30 Short cho tập N"** — mining 30 góc khai thác khác nhau từ bản Long (theo `CORE_OS/SHORTS_ENGINE.md`), viết song song, QA batch chống trùng lặp, đóng gói.
3. Sau khi cả 2 bước xong, Claude Code gộp output vào `Long/` và `Short/` thành 1 file mỗi loại.

Toàn bộ quy trình có QA độc lập ở mỗi bước — không tự động publish, luôn có báo cáo để bạn duyệt trước khi dùng.

### Chạy công cụ trực tiếp (không qua Claude Code)

```bash
# Kiểm tra 1 gói (Long hoặc 1 Short) có đạt chuẩn schema/QA không
python TOOLS/package_audit.py "DOMAINS/BUDDHISM/PRODUCTION_PACKAGES/KINH_DIA_TANG/EP006/_PRODUCTION/Long"

# Đóng gói hàng loạt: tách TTS + dựng manifest.json + README cho toàn bộ Short trong 1 thư mục
python TOOLS/build_short_package.py "<thư_mục_cha_chứa_các_EP0XX_SHORT_NN>" "<package_id_của_bản_Long>" "EP0XX_SHORT_*"
```

Yêu cầu: Python 3 (không cần cài thêm thư viện ngoài chuẩn).

## Upload lên Google Drive (rclone)

Quy ước thư mục trên Drive: `TTS-Input/Phật giáo/Long/` và `TTS-Input/Phật giáo/Short/`, tên file theo format `<số tập>_<tên tập>.txt` (Long) và `<số tập>_<tên tập>_Short.txt` (Short).

```bash
rclone copy "EP0XX/Long" "gdrive:TTS-Input/Phật giáo/Long" --progress
rclone copy "EP0XX/Short" "gdrive:TTS-Input/Phật giáo/Short" --progress
```

Cần cấu hình remote `gdrive` một lần bằng `rclone config` (đăng nhập Google qua trình duyệt — bước này không thể tự động hóa thay bạn).

## Đọc thêm trước khi viết nội dung mới

- `CORE_OS/BRAND_BIBLE.md` — giọng văn, giá trị thương hiệu, điều cấm kỵ.
- `CORE_OS/SHORTS_ENGINE.md` — công thức viết Shorts thu hút (6 mode, hook 4 giai đoạn, quy tắc chống trùng lặp).
- `DOMAINS/BUDDHISM/CONTINUITY_REGISTRY.md` — **bắt buộc đọc trước mỗi tập** để không lặp lỗi/motif đã dùng.
- `DOMAINS/BUDDHISM/SERIES_BIBLES/SEASON_01_PRODUCTION_PLAN.md` — chủ đề chính thức từng tập.

## Trạng thái Season 1

| Tập | Chủ đề | Trạng thái |
|---|---|---|
| 1 | Địa Tạng Vương là ai? | ✅ Long + 30 Short |
| 2 | Vì sao gọi là "Địa Tạng"? | Chưa làm |
| 3 | Đại nguyện "địa ngục chưa không" | Chưa làm |
| 4 | Cung trời Đao Lợi và lòng hiếu của Đức Phật | ✅ Long (gói cũ, chưa có Short) |
| 5 | Nghiệp duyên chúng sinh | ✅ Long + 30 Short |
| 6 | Địa ngục trong kinh: thật hay biểu tượng? | ✅ Long + 30 Short |
| 7-15 | Xem chi tiết trong `SEASON_01_PRODUCTION_PLAN.md` | Chưa làm |

## Giới hạn hiện tại (nói thẳng, không giấu)

- Nội dung nguồn là tổng hợp từ nhiều nguồn công khai thứ cấp (không phải 1 bản dịch kinh thống nhất duy nhất) — xem cảnh báo độ tin cậy trong từng file nghiên cứu ở `DOMAINS/BUDDHISM/SOURCES/RESEARCH_DRAFT_*.md`.
- Chưa có bước sinh prompt hình ảnh/video hay render giọng đọc — output dừng ở text sẵn sàng cho TTS, đúng phạm vi đã thiết kế (`external_processes` trong mỗi `manifest.json` luôn ghi `OUT_OF_SCOPE` cho voice/video render/publish).
- Domain khác ngoài Phật giáo (`DOMAINS/FENG_SHUI`, `DOMAINS/CRIMINAL_LAW`) mới có khung thư mục, chưa có nội dung.
