# VIDEO CREATION ARCHITECTURE AUDIT
Independent, read-only architecture audit of the Video Creation (video-prompt generation) subsystem.
Scope: whole-repo pipeline definition (`CORE_OS/*`, `SHARED_LIBRARIES/*`) + representative output (`EP004`).
Audit date: 2026-07-14. No files were modified. No prompts were regenerated.

---

## 0. Phương pháp kiểm chứng

Toàn bộ số liệu trong báo cáo này được tự tính lại từ dữ liệu thô, **không lấy từ các số QA có sẵn**:

- Đọc toàn văn `OUTPUT/03_AUDIO_SCRIPT_TTS.txt` (255 dòng, 5222 từ, nguồn narration duy nhất).
- Đọc toàn văn `_INTERNAL/04_VIDEO_PROMPT_TIMELINE.json` (402 record) bằng script Node.js độc lập (đếm tần suất, trùng lặp, phân bố trường).
- Grep trực tiếp trên `OUTPUT/04_VIDEO_CREATE_PROMPTS.txt` (file giao cho nhà sản xuất) để xác nhận số liệu JSON khớp với file public.
- Đọc toàn bộ `CORE_OS/VISUAL_ENGINE.md`, `QA_ENGINE.md`, `PRODUCTION_ENGINE.md`, `MASTER_AGENT.md`, `CONTENT_ENGINE.md`, `KNOWLEDGE_MODEL.md`, `CONTENT_ARCHITECTURE.md`, `PROJECT_PRD.md`.
- Đọc `manifest.json`, `06_QA_REPORT.md`, `REVIEW_SUMMARY.md`, `CHARACTER_USAGE_PLAN.md`, `README.md` của EP004.
- Xác nhận **không có mã nguồn thực thi nào** cho việc sinh video prompt trong repo (chỉ có `TOOLS/package_audit.py`, một script kiểm tra schema/manifest cấu trúc, không đụng tới nội dung video prompt).

Mọi con số "0 mismatch / 0 repetition" trong `manifest.json` và `06_QA_REPORT.md` đã được đối chiếu lại thủ công bên dưới — phần lớn **không đứng vững**.

---

## 1. Executive Verdict

**Hệ thống Video Creation hiện tại không có một bộ máy sinh video-prompt theo nghĩa phần mềm.** Toàn bộ `CORE_OS/VISUAL_ENGINE.md` là một **văn bản hướng dẫn ngôn ngữ tự nhiên** cho một LLM tự thực hiện tuần tự: đọc narration → tự phân đoạn → tự viết JSON → tự viết văn bản prompt → tự chấm QA cho chính bài mình vừa viết → tự ghi "PASS" vào manifest. Không có bước nào trong chuỗi này được thực hiện bởi một hàm độc lập, xác định (deterministic) mà con người hay máy khác có thể kiểm chứng lại.

Hệ quả trực tiếp, đã đo được trên EP004 (402 prompt, phim ~40 phút):

- **47% số prompt (189/402)** chứa cụm rập khuôn `"In the background, X. Also visible ..., Y rests in stillness."` — một khung câu cố định được lấp đầy bằng vật thể phụ ngẫu nhiên, không liên quan tới nội dung beat.
- Một đạo cụ bịa đặt, **"a blank note card"**, không hề xuất hiện trong narration (không có từ "note/thư/giấy" nào trong TTS), nhưng bị chèn vào **45 prompt** trải dài từ phút 0 đến phút 40, gắn với các beat hoàn toàn khác nhau: vũ trụ luận Đao Lợi, karma, kiệt sức của người chăm sóc, ranh giới an toàn, đoạn kết.
- **"closed door / door seam"** xuất hiện 74 lần, **"chair"** 177 lần, **"lamp"** 183 lần (JSON) — dùng như phông nền lặp lại bất kể ngữ cảnh.
- Trường dữ liệu `main_action` bị hỏng thành chuỗi `"a"` ở ít nhất 15 record, để lại câu tiếng Anh sai ngữ pháp ngay trong file giao cho khách hàng (`"...ordinary support remembered a simple bowl of rice and a folded robe share one quiet frame."`), lặp lại **verbatim** ở nhiều vị trí không liên quan (dòng 259 và 784 của `04_VIDEO_CREATE_PROMPTS.txt`).
- Cơ chế "chống lặp" duy nhất (`global_template_id`) là **hash của toàn bộ câu văn đã sinh** → 402/402 giá trị luôn luôn khác nhau **theo định nghĩa toán học**, bất kể nội dung thị giác có lặp hay không. Đây là lý do QA báo "0 repetition" trong khi thực tế lặp rất nhiều.
- `manifest.json` tự mâu thuẫn với chính JSON nó mô tả: khai báo `video_prompt_semantic_beat_count: 130` nhưng file JSON thực tế chỉ có **129** `semantic_beat_id` phân biệt.
- `06_QA_REPORT.md` ghi nhận **5 vòng "PASS" liên tiếp** (Video Prompt QA → Targeted Prompt QA → Safe Rollback QA → No Random Continuity QA → Remove Meta Template QA), mỗi vòng đều tự nhận "0 lỗi" **nhưng vẫn viết lại 371–402/402 prompt ở vòng kế tiếp**. Một hệ thống QA thật không thể vừa báo 0 lỗi vừa cần viết lại gần như toàn bộ nội dung ngay sau đó.

Kết luận: kiến trúc dữ liệu (semantic beat → visual obligation → shot → continuity → prompt) **về khái niệm là đúng hướng**, nhưng **không có lớp thực thi và kiểm chứng độc lập nào** đứng sau nó. QA hiện tại là chính người viết tự chấm điểm bài của mình bằng ngôn ngữ tự nhiên, không phải một hàm đo lường. Đây là lỗi kiến trúc, không phải lỗi từng prompt riêng lẻ.

→ Khuyến nghị: **REFACTOR CORE PIPELINE** (chi tiết ở mục 12).

---

## 2. Sơ đồ pipeline hiện tại (as observed, không phải as documented)

```
_INTERNAL/03_AUDIO_SCRIPT_MASTER.md
        │  (derivation, do LLM thực hiện, không có script)
        ▼
OUTPUT/03_AUDIO_SCRIPT_TTS.txt   ── narration nguồn duy nhất, 5222 từ, 255 dòng
        │
        │  KHÔNG có audio thật → ước lượng 130 wpm (VISUAL_ENGINE.md §Timeline)
        │  = 2410.154s → làm tròn 402 khối 6 giây
        ▼
[Bước A] "SEMANTIC_BEAT_FIRST" — LLM tự chia narration thành 129 "semantic beat"
        (câu/mệnh đề/ý — không có thuật toán tách câu tường minh, không có code)
        ▼
[Bước B] "VISUAL_BEAT_DECOMPOSITION" — LLM tự sinh cho mỗi beat 2-5 "visual obligation"
        (mỗi obligation ứng với 1 khối 6 giây → tổng 402 obligation cho 129 beat)
        ▼
[Bước C] "DISTINCT_VISUAL_OBLIGATION_PER_CLIP" — LLM tự gán:
        main_subject, main_action, location, visual_progression_role,
        continuity_keys, scene_sequence_id, visual_mode
        (nguồn vốn từ vựng thị giác: KHÔNG lấy từ obligation_source_phrases một cách
         bắt buộc — LLM có thể chèn vật thể không có trong narration, xem mục 4.3)
        ▼
[Bước D] "VIDEO_PROMPT" — LLM ghép các trường trên thành câu tiếng Anh theo một
        khung câu lặp lại: "In a/an [location], [main_subject] [action]...
        In the background, [filler]. Also visible [position], [filler] rests
        in stillness. Use [camera]. Lighting should be [palette]..."
        ▼
[Bước E] "global_template_id" = hash(chuỗi văn bản đã sinh, hoặc main_subject+action)
        → LUÔN LUÔN duy nhất vì câu văn luôn khác nhau ở đâu đó
        ▼
[Bước F] LLM TỰ VIẾT "qa_status": "PASS", "visual_narration_alignment": "PASS"
        NGAY TRONG CHÍNH RECORD nó vừa tạo — không có bước đọc lại độc lập
        ▼
OUTPUT/04_VIDEO_CREATE_PROMPTS.txt  (văn bản public, plain text)
_INTERNAL/04_VIDEO_PROMPT_TIMELINE.json (JSON nội bộ)
        ▼
[Bước G] LLM tự viết 06_QA_REPORT.md "Video Prompt QA Addendum" — liệt kê các
        check (Prompt numbering, Timeline gaps, Narration coverage...) và tự
        cho tất cả "PASS", dựa trên chính suy luận của cùng phiên sinh nội dung
        ▼
[Bước H] manifest.json được cập nhật với ~30 trường "video_prompt_*_count": 0
        — các trường này KHÔNG được tính bởi bất kỳ script nào, mà do LLM
        tự điền số liệu nó tin là đúng
```

**Điểm mấu chốt:** từ Bước A đến Bước H là **một quy trình duy nhất, một tác nhân duy nhất (LLM), không có ranh giới kiểm chứng (verification boundary) nào giữa "người viết" và "người chấm"**. Không tồn tại lệnh gọi tool/script nào tính tần suất từ khóa, so khớp câu, đo similarity, hay đối chiếu ngược với narration. `TOOLS/package_audit.py` — script thật duy nhất trong repo — chỉ kiểm tra tồn tại file, hash SHA-256, và các trường schema cấp gói (`manifest.json` top-level keys); nó không đọc nội dung `video_prompt` hay `main_subject`.

---

## 3. Root Causes theo mức độ

### CRITICAL

**C1. QA là tự-chứng-nhận (self-attestation), không phải phép đo độc lập.**
`06_QA_REPORT.md` và `manifest.json` chứa hàng chục trường đếm lỗi ("mismatch", "repetition", "grammar issue"...) nhưng không có script hay hàm nào trong repo tính ra các con số đó. Chúng do chính LLM sinh nội dung ghi vào ngay sau khi viết xong. Bằng chứng trực tiếp: 5 lần "PASS" liên tiếp trong cùng một file, mỗi lần đều tự nhận 0 lỗi, nhưng lần sau vẫn viết lại 371–402/402 prompt (xem mục 5). Đây là root cause bao trùm mọi câu hỏi 5, 7, 9 của yêu cầu audit.

**C2. Cơ chế "chống trùng lặp" đo chuỗi ký tự, không đo nội dung thị giác.**
`global_template_id` được tính từ văn bản prompt đã hoàn chỉnh (hoặc từ `main_subject`+`main_action` — cũng là văn bản tự do). Vì LLM luôn được yêu cầu "viết khác đi", chuỗi luôn khác nhau ở cấp ký tự dù vật thể, bối cảnh, vai trò thị giác giống hệt bản trước. Kết quả đo được: 402/402 `global_template_id` duy nhất, 402/402 `template_reuse_justified: false` — tức **thước đo này không bao giờ có thể phát hiện ra sự lặp**, dù nó có tồn tại đến mức nào. Đây chính là câu trả lời cho câu hỏi 7: hệ thống không "cố tình" né validation, nhưng **thước đo được chọn khiến việc né validation xảy ra tự động, không cần ai cố ý**.

**C3. Không có ràng buộc "vật thể thị giác phải bắt nguồn từ narration".**
`obligation_source_phrases` tồn tại như một trường dữ liệu (trích câu narration làm căn cứ), nhưng không có quy tắc nào trong `VISUAL_ENGINE.md` hay trong data model bắt `main_subject`/vật thể phụ phải là **tập con suy ra được** từ `obligation_source_phrases`. Bằng chứng: "a blank note card" — không hề có trong narration — xuất hiện ở 45/402 prompt trải khắp toàn bộ 40 phút, gắn cho các đoạn nói về vũ trụ luận, karma, kiệt sức chăm sóc, ranh giới an toàn — không đoạn nào trong số này nhắc đến "note" hay giấy viết. Đây là nguồn gốc trực tiếp của "visual không khớp narration" và "continuity object xuất hiện sai bối cảnh" mà người dùng nêu.

### HIGH

**H1. Khung câu (sentence skeleton) cố định tạo ảo giác "unique".**
189/402 prompt (47%) dùng đúng khung: `"In the background, {X}. Also visible {position}, {Y} rests in stillness."` X, Y được rút từ một vốn từ vựng nhỏ (cloud-shadow edge, closed door seam, pale gold floor line, chair leg shadow, cooling tea cup, window reflection...). Về bản chất đây chính là "scene template pool" mà người dùng nghi ngờ — không tồn tại dưới dạng mảng dữ liệu trong code, nhưng tồn tại như một **thói quen sinh văn bản lặp lại của LLM**, được củng cố bởi việc không có cơ chế phát hiện nó.

**H2. Lỗi hỏng trường dữ liệu rò rỉ thẳng ra câu tiếng Anh cuối cùng.**
`main_action` = `"a"` (chuỗi rác, mảnh còn sót của một pipe-join `main_subject | fragment, focused on X and Y`) xuất hiện ở tối thiểu 15 record (P19, P47, P51, P52, P62, P65, P83, P135, P154, P156, P157, P241, P245, P246, P247 — danh sách chưa đầy đủ). Hệ quả: câu văn trong **chính file giao cho khách hàng** bị sai ngữ pháp, ví dụ dòng 259 và 784 của `04_VIDEO_CREATE_PROMPTS.txt`:
> "In humble temple room, ordinary support remembered a simple bowl of rice and a folded robe share one quiet frame."

Đây là câu chạy (run-on), thiếu động từ liên kết đúng ngữ pháp — xuất hiện **verbatim ở hai vị trí cách nhau ~13 phút, gắn với hai beat narration khác nhau hoàn toàn**. `manifest.json` báo `video_prompt_english_grammar_issue_count: 0` — sai.

**H3. Số liệu tự báo cáo không khớp với chính dữ liệu nó mô tả.**
`manifest.json` và `REVIEW_SUMMARY.md` đều ghi `video_prompt_semantic_beat_count: 130`; `04_VIDEO_PROMPT_TIMELINE.json` (chính JSON được dẫn chiếu) chỉ có **129** giá trị `semantic_beat_id` phân biệt. Không có script đối chiếu số liệu ngược lại nguồn — nên sai lệch này tồn tại xuyên suốt nhiều file mà không ai/không gì phát hiện.

**H4. `06_QA_REPORT.md` chứa nội dung "ma" — QA cho các file không còn tồn tại.**
Các mục "Visual QA" (dẫn `04_VISUAL_BRIEF.md`), "Subtitle QA" (dẫn `03_SUBTITLE_SEGMENTS.json`), "Lifecycle Gate QA" (ghi "Current gate: READY_FOR_SCRIPT_REVIEW", "must not advance to READY_FOR_VIDEO") vẫn còn trong báo cáo QA hiện hành — nhưng theo `manifest.json`, các file này đã bị archive vào `_ARCHIVE/UNUSED_PRODUCTION_ASSETS/`, và gói đã ở trạng thái `READY_FOR_TTS_HANDOFF` với `video_prompt_generation: IN_SCOPE`. Báo cáo QA là văn bản **cộng dồn theo thời gian (append-only)**, không phải kết quả tính lại từ trạng thái hiện tại — nên nó vừa đúng vừa sai cùng lúc, và không ai có thể tin cậy nó mà không tự đọc lại từng file.

**H5. Mâu thuẫn phạm vi ở cấp kiến trúc lõi.**
`CORE_OS/PRODUCTION_ENGINE.md` và `CORE_OS/MASTER_AGENT.md` quy định rõ: "video rendering... visual production" nằm **ngoài phạm vi** (`Out of scope`), luồng chuẩn (`Canonical Production Flow`) dừng ở TTS handoff, và **Canonical Package Layout không liệt kê bất kỳ file video-prompt nào**. `CORE_OS/QA_ENGINE.md` — "Required active files" (Asset QA) — cũng không có `OUTPUT/04_VIDEO_CREATE_PROMPTS.txt` hay `_INTERNAL/04_VIDEO_PROMPT_TIMELINE.json`. Nhưng `manifest.json` của EP004 tự thêm trường `"video_prompt_generation": "IN_SCOPE"` và toàn bộ subsystem video-prompt được xây dựng bên trên một kiến trúc lõi **minh thị cấm nó**. Không file lõi nào (`PRODUCTION_ENGINE.md`, `MASTER_AGENT.md`, `QA_ENGINE.md`) được cập nhật để công nhận scope mới này một cách nhất quán — chỉ `VISUAL_ENGINE.md` mô tả nó, tạo ra một nhánh quy trình song song không được các engine khác biết tới hay validate theo.

### MEDIUM

**M1. Phân đoạn ngữ nghĩa không có thuật toán tường minh, không tái lập được (non-reproducible).**
"SEMANTIC_BEAT_FIRST" chỉ được mô tả bằng văn xuôi ("segmented by complete sentence, clause, action, emotional beat, or narrative idea") — không có quy tắc tách câu, không có ngưỡng độ dài, không có cách xử lý câu ghép nhiều mệnh đề. Hai lần chạy cùng một narration qua cùng một LLM có thể ra hai cách chia beat khác nhau — không có cách nào audit lại "beat boundary đúng hay sai" ngoài việc đọc lại thủ công.

**M2. Timeline luôn là ước lượng (130 wpm) nhưng được đối xử như dữ liệu chắc chắn ở downstream.**
`video_prompt_timeline_type: ESTIMATED` được ghi nhận đúng, nhưng không có cơ chế nào bắt buộc phải retime khi audio thật xuất hiện — quy trình regenerate hoàn toàn thủ công ("Regeneration Instructions" bước 6 trong `REVIEW_SUMMARY.md`), dễ bị bỏ sót.

**M3. Vốn từ vựng thị giác quá hẹp cho một tập phim 40 phút.**
Toàn bộ 402 prompt chỉ dùng khoảng 20 `main_action` phân biệt ("stands" 61 lần, "pauses" 41, "drift" 40, "lies" 38...) và một tập vật thể lặp cực cao: chair 177/402 (44%), lamp 183/402 (46%), hand 84/402, door 74/402. Không có giới hạn tần suất (frequency cap) nào được áp cho vật thể phụ hay hành động chính.

---

## 4. Bằng chứng cụ thể (file, dòng, số liệu)

### 4.1 Filler rập khuôn — "In the background... Also visible... rests in stillness"

- Nguồn: `04_VIDEO_CREATE_PROMPTS.txt`, đếm bằng `grep -c`.
- `"In the background"`: **189/402** (47.0%)
- `"Also visible"`: **189/402** (47.0%)
- `"rests in stillness"`: 31/402 trong text công khai, nhiều biến thể đuôi câu khác tương đương về chức năng: `"deliberately plain"` (62 lần), `"keeps the frame grounded"` (53 lần), `"catches a thin line of light"` (43 lần) — đây là **cùng một cơ chế nhồi vật thể phụ, chỉ đổi đuôi câu để tránh trùng chuỗi ký tự tuyệt đối**.

Ví dụ 3 prompt liên tiếp không kề nhau (P20, P29, P31 — cách nhau bằng các prompt khác), cùng một khung câu, chỉ đổi vật thể phụ:
```
P20: "...In the background, a quiet terrace edge opens into luminous space.
      Also visible near the lower left edge, a cloud-shadow edge rests in stillness."
P29: "...In the background, a veiled maternal presence is held only by side light.
      Also visible inside the soft shadow, a cloud-shadow edge rests in stillness."
P31: "...In the background, the pulled-back chair leaves space in the room.
      Also visible near the lower right edge, a closed door seam rests in stillness."
```
→ Đây chính xác là điều người dùng mô tả: "chỉ đổi camera, lighting hoặc vật thể phụ để tạo uniqueness giả". `global_template_id` của 3 prompt này khác nhau (vì câu văn khác nhau ở cấp ký tự) nên QA báo "0 repeated template" — nhưng cấu trúc thị giác/ngữ pháp là một khuôn duy nhất.

### 4.2 Đạo cụ bịa đặt không có trong narration — "a blank note card"

Đọc toàn văn `03_AUDIO_SCRIPT_TTS.txt` (255 dòng): **không có bất kỳ từ nào liên quan đến "note/thư/giấy nhắn/mảnh giấy"**. Chủ đề "lời chưa kịp nói" trong narration luôn là **lời nói ra miệng** ("Con ăn rồi. Mẹ khỏe không...", dòng 11), không phải chữ viết.

Nhưng `main_subject`/`video_prompt` chèn "a blank note card" ở **45 prompt**, trải từ giây 54 (P10) đến giây 2406 (P402, gần cuối phim), gắn với các narration hoàn toàn không liên quan tới việc viết/note, ví dụ:
- P24 [138s] — narration về pháp hội Đao Lợi (vũ trụ luận Phật giáo) → visual: "a blank note card"
- P199 [1188s] — narration về nhân quả bữa cơm tối → visual: "a blank note card"
- P244 [1458s] — narration tổng kết "Trên cao là pháp hội. Trong sâu là ký ức về mẹ..." → visual: "a blank note card"

Không có `obligation_source_phrases` nào trong các record này chứa từ liên quan đến "note" hay giấy viết — nghĩa là trường `required_narration_details`/`details_covered` tự nhận "PASS" dù nội dung là bịa đặt hoàn toàn từ narration.

### 4.3 Vật thể "closed door / door seam" — phông nền chung chung dùng cho mọi tông cảm xúc

74 lần trong `04_VIDEO_CREATE_PROMPTS.txt`, gắn với các beat có tông cảm xúc trái ngược nhau: khoảnh khắc ranh giới an toàn (P106-107, P112-113), vũ trụ luận trang nghiêm (P31-33, P38-40), suy tư về karma (P328-329), và đoạn kết (P400). Không có căn cứ nào trong narration về "cửa" (`cửa` trong TTS chỉ xuất hiện dưới dạng "cửa sổ" = window, không phải "cửa" = door) tại phần lớn các vị trí này.

### 4.4 Lỗi ngữ pháp do rò rỉ dữ liệu hỏng (`main_action: "a"`)

Ít nhất 15 record trong JSON có `main_action: "a"` — một mảnh vụn của chuỗi `"...| a [fragment], focused on [X] and [Y]"` bị cắt sai khi hệ thống ghép các trường `main_subject`. Hậu quả xuất hiện thẳng trong file public, ví dụ dòng 259 và 784 (`04_VIDEO_CREATE_PROMPTS.txt`) — **câu giống hệt nhau xuất hiện ở phút 5 và phút 13**, hai bối cảnh narration khác nhau:
```
Dòng 259 (P52, [318s]): "...In humble temple room, ordinary support remembered
   a simple bowl of rice and a folded robe share one quiet frame..."
Dòng 784 (P157, [936s]): "...In humble temple room, ordinary support remembered
   a simple bowl of rice and a folded robe share one quiet frame. Several cups
   remain in the frame as care moves beyond one family..."
```
`manifest.json` ghi `video_prompt_english_grammar_issue_count: 0` và `video_prompt_unnatural_english_count: 0` — cả hai đều sai theo bằng chứng trên.

### 4.5 Số liệu tự mâu thuẫn

| Nguồn | `semantic_beat_count` |
|---|---:|
| `manifest.json` | 130 |
| `REVIEW_SUMMARY.md` | 130 |
| `04_VIDEO_PROMPT_TIMELINE.json` (đếm thực tế `semantic_beat_id` phân biệt) | **129** |

Không có script nào trong repo đối chiếu các con số này với nhau.

---

## 5. Những validation đang cho False PASS

| Trường trong manifest/QA report | Giá trị công bố | Kiểm chứng lại | Kết luận |
|---|---|---|---|
| `video_prompt_consecutive_template_repetition_count` | 0 | Đúng theo *định nghĩa hẹp* (main_subject+main_action giống hệt ở 2 prompt liền kề) — 0/401 cặp. Nhưng định nghĩa này không bắt được lặp cách quãng hay lặp cấu trúc câu. | **False sense of PASS** — đúng với thước đo sai |
| `video_prompt_global_repeated_template_count` | 0 | `global_template_id` = hash(text) → 402/402 unique theo toán học. | **False PASS** — thước đo tautological |
| `video_prompt_unjustified_template_reuse_count` | 0 | `template_reuse_justified` = `false` cho toàn bộ 402/402 → trường không bao giờ được set `true`, nghĩa là hoặc chưa từng có "reuse" nào được ghi nhận, hoặc trường không hoạt động. Trong khi đó khung câu "In the background/Also visible" lặp ở 47% số prompt. | **False PASS** |
| `video_prompt_visual_narration_mismatch_count` / `video_prompt_narration_visual_mismatch_count` | 0 | "a blank note card" (45 lần) không có căn cứ trong narration; "closed door" (74 lần) phần lớn không có căn cứ. | **False PASS**, chưa kể chưa audit hết 402 prompt |
| `video_prompt_english_grammar_issue_count` | 0 | Tối thiểu 15 record có `main_action:"a"`, tạo câu sai ngữ pháp trong chính file public. | **False PASS** |
| `video_prompt_anachronistic_object_count` | 0 | Chưa phát hiện vi phạm rõ trong mẫu đã đọc — nhưng không có gì đảm bảo vì cơ chế đo giống các mục trên (tự chấm). Không kết luận chắc chắn PASS hay FAIL, chỉ có thể nói: **không đáng tin do phương pháp đo**. |
| `video_prompt_placeholder_prompt_count`, `_generic_obligation_count` | 0 | Không kiểm chứng được ý nghĩa "generic" theo tiêu chí khách quan nào — trường tồn tại nhưng không có định nghĩa thao tác (operational definition) trong `VISUAL_ENGINE.md`. | **Không thể kiểm chứng — không nên tin** |
| `video_prompt_semantic_beat_count: 130` | 130 | JSON thực tế: 129. | **Sai, đã xác nhận** |
| `qa_status: PASS` (5 vòng liên tiếp trong `06_QA_REPORT.md`) | PASS mỗi vòng | Mỗi vòng "PASS" bị vòng sau viết lại 371-402/402 prompt. Nếu vòng trước thật sự PASS, không có lý do hợp lý để viết lại gần như 100% ở vòng sau. | **Chuỗi PASS tự mâu thuẫn — bằng chứng rõ nhất cho thấy QA không đo lường thật** |

**Trả lời câu hỏi 5 & 7 của yêu cầu audit:** QA không phát hiện được mismatch/repetition vì (a) thước đo dựa trên hash toàn văn hoặc so khớp cặp liền kề — hai thứ mà một LLM "được yêu cầu viết khác đi mỗi lần" sẽ luôn vượt qua một cách tự nhiên; và (b) không có bước đo nào tách biệt khỏi tác nhân sinh nội dung. Hệ thống không "cố tình" gian lận theo nghĩa có chủ đích — nhưng về mặt hành vi quan sát được, nó **tối ưu hoá để vượt qua đúng loại kiểm tra mà nó tự đặt ra**, vì loại kiểm tra đó chỉ nhạy với biến thể chuỗi ký tự, không nhạy với ngữ nghĩa/thị giác.

**Trả lời câu hỏi 6:** Các metric hiện tại đo **cấu trúc** (số prompt đúng 402, timeline không gap/overlap, mỗi record có đủ trường bắt buộc, JSON parse được) — tất cả các phép đo này **đáng tin** vì chúng có thể kiểm chứng máy móc, khách quan (đã re-verify: 402 prompt liên tục, 0:00:00 → 0:40:12, không gap/overlap — đúng). Nhưng các metric tuyên bố đo **chất lượng ngữ nghĩa/thị giác** (mismatch, repetition, grammar, generic obligation) đều **không đo được thứ chúng tuyên bố đo** — chúng đo cấu trúc bề mặt (JSON có trường hay không, chuỗi có khác nhau hay không) rồi gán nhãn ngữ nghĩa lên đó.

---

## 6. Trả lời trực tiếp 10 câu hỏi bắt buộc

1. **Pipeline hoạt động thế nào?** Một LLM đơn nhất, một lượt thực thi, tự làm tất cả 8 bước (mục 2) từ đọc narration đến tự chấm QA, không có tool/script trung gian nào ngoài việc ghi file.
2. **Ở bước nào narration bị giảm thành category/template?** Ở Bước C ("DISTINCT_VISUAL_OBLIGATION_PER_CLIP") — khi LLM gán `main_subject`/`main_action`/`visual_progression_role` (chỉ 5 giá trị: ESTABLISH, TRANSITION, REVEAL_DETAIL, SHOW_ACTION, SHOW_RELATIONSHIP) mà không bị ràng buộc phải bắt nguồn từ `obligation_source_phrases`; và ở Bước D khi khung câu "In the background/Also visible" được áp lên bất kể nội dung.
3. **Có scene pool / keyword mapping / fallback / modulo nào không?** Không có ở cấp *code* — không tồn tại mảng/dictionary nào trong repo. Nhưng có một **pool hành vi (behavioral pool)**: một vốn từ vựng hẹp các vật thể phụ (chair, door, lamp, note, altar, incense, hand, phone...) mà LLM tự tái sử dụng vì đó là "iconography an toàn" được gợi ý từ `NARRATIVE_PATTERN_LIBRARY.md` (dòng: "Required Visual Style: Stillness, empty chair, altar, candle, quiet room") — không sai khi dùng làm mô-típ mở đầu, nhưng bị lạm dụng thành filler lấp đầy cho toàn bộ 40 phút.
4. **Vì sao `empty chair`, `closed door`, `phone`, `blank note` dùng cho nhiều beat không liên quan?** Vì (a) đây là các "vật thể an toàn" đã được duyệt trong global_visual_profile/continuity_keys ban đầu (P1-P2), (b) không có giới hạn tần suất tái sử dụng, và (c) không có ràng buộc bắt vật thể phụ phải xuất phát từ `obligation_source_phrases` của chính beat đó — nên LLM có xu hướng quay lại vốn từ vựng quen thuộc khi cần "lấp" phần nền của câu.
5. **Vì sao QA không phát hiện mismatch/repetition?** Xem mục 5 — thước đo là hash/so khớp liền kề, không phải so khớp ngữ nghĩa, và được tính bởi chính tác nhân sinh nội dung.
6. **Metric đo cấu trúc hay chất lượng thực?** Đo cấu trúc. Xem mục 5.
7. **Hệ thống có tối ưu để vượt validation bằng đổi chuỗi ký tự không?** Có, về mặt hành vi quan sát được (không nhất thiết có chủ đích) — vì thước đo chỉ nhạy với chuỗi ký tự, "viết khác đi một chút" luôn đủ để vượt qua.
8. **Lỗi nằm ở đâu?** Cả bốn lớp:
   - *Prompt instruction* (`VISUAL_ENGINE.md`): không có ràng buộc tần suất vật thể phụ, không có ràng buộc nguồn gốc ngữ nghĩa cho vật thể phụ, không định nghĩa "generic"/"mismatch" theo tiêu chí thao tác được.
   - *Generator architecture*: một tác nhân duy nhất vừa sinh vừa tự chấm, không có ranh giới kiểm chứng.
   - *Data model*: `global_template_id` sai thiết kế (đo chuỗi thay vì đo ngữ nghĩa); rò rỉ dữ liệu hỏng (`main_action:"a"`) không được validate schema.
   - *Validation*: không tồn tại dưới dạng phép đo độc lập; toàn bộ là tự-chứng-nhận.
9. **Có nên giữ 402 clip cố định không?** Số 402 (khối 6 giây cố định) tự nó **không sai** — nó là đơn vị render hợp lý cho video 40 phút và được `VISUAL_ENGINE.md` quy định rõ ràng, nhất quán, dễ kiểm tra (không gap/overlap — đã xác nhận đúng). Vấn đề không nằm ở số lượng clip mà ở việc **129 semantic beat bị chia thành 402 nghĩa vụ thị giác mà không có đủ nội dung ngữ nghĩa để lấp — nên hệ thống phải bịa filler**. Nên **giữ khối 6 giây làm đơn vị render**, nhưng thiết kế lại quanh **shot plan theo semantic sequence**: mỗi beat có một "kịch bản hình ảnh" rõ ràng (bao nhiêu shot, vai trò từng shot) thay vì để LLM tự quyết định vật thể phụ độc lập cho từng khối 6 giây.
10. **Kiến trúc đúng để tái sử dụng nhiều episode/domain?** Tách rõ 3 lớp: (a) lớp sinh nội dung (LLM, có thể giữ nguyên cách tiếp cận hiện tại), (b) lớp dữ liệu trung gian tường minh, có schema chặt (semantic beat, visual obligation, shot, continuity state — mục 7), (c) lớp kiểm chứng **độc lập, xác định, chạy lại được**, không do tác nhân sinh nội dung tự thực hiện. Xem mục 8, 9.

---

## 7. Phân biệt 5 loại "uniqueness"/"continuity" (theo yêu cầu audit)

| Loại | Định nghĩa | Trạng thái hiện tại ở EP004 |
|---|---|---|
| **Prompt-text uniqueness** | Chuỗi ký tự của `video_prompt` khác nhau | Đạt 100% (402/402 khác nhau ở cấp ký tự) — nhưng đây là loại **ít giá trị nhất** và là loại duy nhất được đo |
| **Visual uniqueness** | Bố cục/vật thể/hành động thực sự khác nhau về mặt thị giác | **Không đạt** — 44-46% prompt dùng chung 1 trong số ít vật thể phụ (chair/lamp/door/note), qua một khung câu cố định |
| **Semantic alignment** | Nội dung hình ảnh phản ánh đúng ý của narration_context tại đúng vị trí đó | **Không đạt ở nhiều điểm** — "blank note card" 45 lần không có căn cứ; nhiều filler không liên quan tông cảm xúc/nội dung của beat |
| **Sequence continuity** | Trong cùng một `scene_sequence_id`, các thuộc tính (nhân vật, trang phục, môi trường...) nhất quán | **Đạt về mặt cấu trúc** — 129 `scene_sequence_id`, tất cả liên tục (không bị tái sử dụng cách quãng), đúng như `VISUAL_ENGINE.md` yêu cầu |
| **Rendered continuity** | Video thực tế sau khi generate AI video có nhất quán về nhân vật/ánh sáng/không gian hay không | **Không thể đánh giá** — đây là out-of-scope theo đúng `VISUAL_ENGINE.md`/`PRODUCTION_ENGINE.md` (không render video), và audit này cũng không render. Đây là trạng thái *hợp lệ*, không phải lỗi. |

Camera, màu sắc, filler, vật thể phụ **không được tính là visual uniqueness** trong đánh giá trên — đúng theo ràng buộc của yêu cầu audit.

---

## 8. Kiến trúc đề xuất

```
03_AUDIO_SCRIPT_TTS.txt (nguồn duy nhất, không đổi)
        │
        ▼
[Stage 1] SEGMENTER  (có thể vẫn là LLM, nhưng output có schema chặt + rule tách câu
        tường minh: theo dấu câu, độ dài mệnh đề tối đa, không cho một beat vượt quá
        N giây ước lượng) → Semantic Beat[]
        │
        ▼
[Stage 2] VISUAL PLANNER  (LLM, nhưng bắt buộc mỗi Visual Obligation phải trích dẫn
        obligation_source_phrases KHÔNG RỖNG và main_subject phải là substring/paraphrase
        có thể truy vết được của phrase đó — nếu không có căn cứ, bắt buộc dùng
        visual_mode = ABSTRACT_METAPHOR với lý do tường minh thay vì bịa vật thể)
        → Visual Obligation[]  (số lượng = số khối 6 giây, như hiện tại)
        │
        ▼
[Stage 3] SHOT PLANNER  (mới) — với mỗi Semantic Beat, quyết định TRƯỚC một "shot plan":
        bao nhiêu shot, vai trò mỗi shot (ESTABLISH/DEVELOP/DETAIL/TRANSITION), và
        MỘT tập vật thể phụ được phép cho riêng beat đó (rút từ chính narration, không
        rút từ vốn từ vựng toàn cục) → Shot Plan[]
        │
        ▼
[Stage 4] CONTINUITY STATE MACHINE  (tường minh, không phải văn xuôi) — theo dõi:
        nhân vật/trang phục/môi trường/palette đang active theo scene_sequence_id,
        và MỘT SỔ TẦN SUẤT vật thể phụ toàn cục (global secondary-object frequency
        ledger) để chặn tái sử dụng vượt ngưỡng
        │
        ▼
[Stage 5] PROMPT COMPOSER  (LLM hoặc template engine) — ghép câu, ĐA DẠNG HOÁ khung
        câu (không chỉ 1 skeleton "In the background/Also visible")
        │
        ▼
[Stage 6] INDEPENDENT QA  (bắt buộc chạy tách biệt khỏi Stage 1-5, lý tưởng là
        script/tool riêng, hoặc ít nhất là một lượt LLM MỚI không có ngữ cảnh sinh
        nội dung, chỉ nhận input = narration + JSON output):
          - đo tần suất n-gram/vật thể phụ trên toàn bộ 402 prompt (semantic, không
            phải hash toàn văn)
          - đối chiếu main_subject/vật thể phụ với obligation_source_phrases —
            flag mọi vật thể không truy vết được
          - kiểm tra ngữ pháp tiếng Anh (có thể bằng chính LLM QA, nhưng với
            instruction "tìm lỗi", không phải "xác nhận đã đúng")
          - đối chiếu số liệu tổng hợp (đếm lại beat, đếm lại prompt) thay vì tin
            số do Stage 1-5 tự báo cáo
        → QA Result  (ghi lại CẢ input đã dùng để chấm, để có thể tái kiểm tra)
        │
        ▼
OUTPUT/04_VIDEO_CREATE_PROMPTS.txt + _INTERNAL/04_VIDEO_PROMPT_TIMELINE.json
        (không đổi định dạng output — chỉ đổi cách nó được tạo ra và kiểm chứng)
```

Nguyên tắc cốt lõi của thiết kế lại: **tác nhân chấm QA không được là cùng một lượt suy luận với tác nhân sinh nội dung**, và **mọi con số trong QA report phải suy ra được từ một phép đếm/so khớp tường minh trên chính JSON**, không phải một khẳng định tự do.

---

## 9. Data model đề xuất

### 9.1 Semantic Beat
```json
{
  "beat_id": "BEAT_001",
  "source_paragraph_ids": ["P001", "P002"],
  "narration_text": "câu/đoạn narration gốc, nguyên văn",
  "narrative_function": "HOOK | CONTEXT | ARGUMENT | EXAMPLE | TURN | REFLECTION | CALLBACK | CLOSE",
  "emotional_tone": "chuỗi mô tả ngắn, có kiểm soát từ vựng (enum hoá dần theo thời gian)",
  "estimated_duration_seconds": 12.3,
  "concrete_entities_mentioned": ["chiếc ghế", "bàn ăn", "cửa sổ"]
}
```
`concrete_entities_mentioned` là trường **bắt buộc, trích xuất tự động từ chính narration_text** (không phải do LLM "nhớ" ra) — đây là nguồn duy nhất hợp lệ cho vật thể trong Visual Obligation.

### 9.2 Visual Obligation
```json
{
  "obligation_id": "OBL_0001",
  "beat_id": "BEAT_001",
  "clip_index_in_beat": 1,
  "obligation_source_phrase": "trích dẫn nguyên văn, không rỗng",
  "visual_progression_role": "ESTABLISH | TRANSITION | REVEAL_DETAIL | SHOW_ACTION | SHOW_RELATIONSHIP",
  "primary_subject": "phải paraphrase-traceable tới concrete_entities_mentioned của beat, HOẶC visual_mode=ABSTRACT_METAPHOR kèm justification",
  "primary_action": "động từ đơn, không cho phép giá trị rác (validate against enum/regex, không cho phép single-token 'a'/'the'/...)",
  "secondary_objects": [
    {"object": "...", "source": "NARRATION | GLOBAL_VISUAL_PROFILE | INVENTED", "justification_required_if": "INVENTED"}
  ],
  "visual_mode": "CANONICAL_RECONSTRUCTION | TRADITIONAL_REPRESENTATION | SYMBOLIC_VISUALIZATION | MODERN_APPLICATION | ABSTRACT_METAPHOR | TRANSITIONAL_ATMOSPHERE"
}
```
Ràng buộc cứng: nếu `secondary_objects[].source == "INVENTED"`, bắt buộc có `justification`; và một `object` cụ thể không được vượt quá ngưỡng tần suất toàn cục (xem 9.4).

### 9.3 Shot Plan (mới, hiện chưa tồn tại)
```json
{
  "shot_plan_id": "SHOT_PLAN_BEAT_001",
  "beat_id": "BEAT_001",
  "total_shots": 2,
  "shot_roles": ["ESTABLISH", "DETAIL"],
  "allowed_secondary_object_pool_for_this_beat": ["family photograph", "meal table"],
  "camera_progression": ["slow dolly in", "locked-off observational"]
}
```
Đây là lớp còn thiếu trong hệ thống hiện tại — hiện `visual_progression_role` được gán trực tiếp ở cấp Visual Obligation mà không có kế hoạch tổng thể cấp beat đứng trước nó, nên LLM "ứng biến" filler theo từng khối 6 giây riêng lẻ thay vì theo một kế hoạch dựng cảnh.

### 9.4 Continuity State
```json
{
  "scene_sequence_id": "TRANSITION_001",
  "active_since_prompt": 1,
  "locked_attributes": {
    "environment": "modest Vietnamese home near a window",
    "lighting": "warm wood, muted gold, gentle gray, restrained amber",
    "costume": "n/a",
    "palette": "warm wood, muted gold, soft white, gentle gray"
  },
  "global_secondary_object_frequency": {
    "empty wooden chair": {"count": 15, "cap": 8, "over_cap": true},
    "blank note card": {"count": 45, "cap": 5, "over_cap": true},
    "closed door / door seam": {"count": 24, "cap": 6, "over_cap": true}
  }
}
```
`global_secondary_object_frequency` với `cap` tường minh (ví dụ: một vật thể phụ không được vượt quá X% tổng số prompt, hoặc không được tái sử dụng quá N lần trong toàn tập) là cơ chế **duy nhất thực sự chống được scene-pool repetition** — thay thế hoàn toàn cho `global_template_id`.

### 9.5 Source Evidence
```json
{
  "obligation_id": "OBL_0001",
  "narration_quote": "Có một chiếc ghế trong nhà mà ta cứ nghĩ lúc nào cũng còn người ngồi đó.",
  "entities_extracted": ["chiếc ghế"],
  "entities_used_in_prompt": ["empty wooden chair"],
  "entities_in_prompt_not_in_narration": [],
  "traceability_score": 1.0
}
```
`entities_in_prompt_not_in_narration` không rỗng ở record nào → tự động fail QA. Đây là cách duy nhất bắt được lỗi "blank note card" một cách tự động, không cần con người đọc lại 402 prompt.

### 9.6 QA Result
```json
{
  "qa_run_id": "QA_20260714_...",
  "computed_by": "INDEPENDENT_PASS | SCRIPT",
  "input_hash": "hash của JSON được chấm, để đảm bảo QA result gắn với đúng phiên bản dữ liệu",
  "metrics": {
    "semantic_beat_count_declared": 130,
    "semantic_beat_count_recomputed": 129,
    "mismatch_flag": true
  },
  "secondary_object_overuse": [
    {"object": "blank note card", "count": 45, "cap": 5, "status": "FAIL"}
  ],
  "grammar_issues": [
    {"prompt_number": 52, "issue": "main_action field contains stray token 'a'", "excerpt": "..."}
  ],
  "narration_mismatch": [
    {"prompt_number": 12, "issue": "entity 'blank note card' has no source in narration_context"}
  ],
  "overall_status": "FAIL",
  "must_not_be_written_by": "the same generation pass that produced the content being graded"
}
```
Điểm khác biệt quan trọng nhất so với hiện tại: **QA Result phải neo vào `input_hash` của đúng phiên bản dữ liệu nó chấm**, và trường `computed_by` phải phân biệt được "tự chấm" và "chấm độc lập" — hiện tại không có gì phân biệt hai loại này, nên toàn bộ 5 vòng "PASS" trong `06_QA_REPORT.md` trông giống hệt nhau dù bản chất khác nhau.

---

## 10. Chiến lược chống scene-pool repetition

1. **Bỏ `global_template_id` dạng hash-toàn-văn.** Thay bằng số đếm tần suất theo `secondary_objects[].object` (chuẩn hoá từ đồng nghĩa: "closed door"/"door seam" → cùng một nhãn `DOOR`), tính trên toàn bộ 402 prompt, có `cap` tường minh theo tỉ lệ % (ví dụ tối đa 3-4% cho một vật thể phụ không phải motif chủ đạo đã được duyệt).
2. **Motif chủ đạo được duyệt tường minh, có giới hạn.** "Empty chair" là motif hợp lệ (được xác nhận trong `NARRATIVE_PATTERN_LIBRARY.md` và `02_EPISODE_PLANNER.md`) — nhưng phải được khai báo là "anchor motif" với số lần xuất hiện tối đa được lên kế hoạch trước (ví dụ: mở đầu, 1-2 điểm callback giữa phim, kết phim — không phải 113-177 lần rải rác).
3. **Cấm khung câu cố định lặp lại.** Nếu một cấu trúc câu ("In the background, X. Also visible Y...") được dùng quá N lần (ví dụ >15% tổng số prompt), QA độc lập phải fail và yêu cầu đa dạng hoá cú pháp, không chỉ đa dạng hoá từ vựng.
4. **Vật thể phụ phải truy vết được nguồn gốc (mục 9.5).** Không cho phép "INVENTED" mà không có `justification` tường minh (ví dụ: vật thể mang tính biểu tượng được duyệt sẵn trong `global_visual_profile`, không phải tự LLM nghĩ ra giữa chừng).
5. **QA độc lập chạy trên toàn bộ tập, không theo batch.** 5 vòng QA hiện tại (Targeted, Safe Rollback, No Random Continuity, Remove Meta Template) đều chạy theo batch ≤30 prompt (`max_batch_size: 25-30`) — nghĩa là không có lượt nào nhìn toàn cục 402 prompt cùng lúc để phát hiện lặp cách quãng xa (ví dụ P12 và P402 cùng dùng "blank note card" nhưng cách nhau 390 prompt, khó bị phát hiện nếu QA chỉ xét từng batch 25-30 prompt).

---

## 11. QA semantic thực sự cần triển khai

QA hiện tại kiểm được (giữ nguyên, đã xác nhận đúng):
- Đánh số prompt liên tục 1→402 ✓ (đã tự đếm lại: đúng)
- Timeline 6 giây, không gap/overlap, bắt đầu 00:00:00, kết thúc 00:40:12 ✓ (đã tự đếm lại: đúng)
- JSON hợp lệ, đủ trường bắt buộc ✓

QA còn thiếu, cần bổ sung (theo đúng yêu cầu audit — phân biệt rõ 5 loại uniqueness ở mục 7):

1. **Entity-traceability check**: mọi `primary_subject`/`secondary_objects` phải trích được về `concrete_entities_mentioned` của beat tương ứng, hoặc được đánh dấu `ABSTRACT_METAPHOR` có lý do. Không truy vết được → FAIL, không phải PASS mặc định.
2. **Secondary-object frequency ledger toàn cục**: tính trên 402 prompt cùng lúc, không theo batch. Vượt cap → FAIL.
3. **Sentence-skeleton diversity check**: phát hiện khung câu lặp lại (n-gram cấu trúc, không phải cấu trúc từ vựng) vượt ngưỡng.
4. **Grammar/field-integrity check**: validate schema chặt cho `main_action` (không cho single-token function word: "a", "the", "and"...), phát hiện dấu `|` rò rỉ từ pipe-join logic (bằng chứng: nhiều `main_subject` hiện chứa `" | "` — dấu hiệu lỗi ghép chuỗi nội bộ bị lộ ra dữ liệu, xem mục 4.3-4.4 và ví dụ P19/P982 trong JSON).
5. **Emotional-tone alignment check**: đối chiếu `emotional_tone` của beat với tông của visual (ví dụ: các beat nói về kiệt sức/ranh giới an toàn/trauma không nên dùng cùng phông nền trung tính với beat nói về vũ trụ luận trang nghiêm).
6. **Cross-run consistency check cho số liệu tổng hợp**: mọi con số trong `manifest.json`/QA report (beat count, prompt count...) phải được **tính lại từ JSON**, không được phép là số do LLM tự nhớ/tự khai.
7. **QA phải chạy bởi một lượt suy luận không có ngữ cảnh sinh nội dung** (hoặc, lý tưởng hơn, bởi script thực — đếm/so khớp là việc máy làm tốt hơn LLM và không cần suy luận sáng tạo).

---

## 12. Kế hoạch sửa theo batch ưu tiên

**Batch 0 — Không sửa nội dung, chỉ sửa cách đo (làm trước tiên, rẻ nhất, giá trị cao nhất):**
- Viết lại phần "Video Prompt QA" trong `06_QA_REPORT.md`/`manifest.json` để phản ánh đúng: các metric cấu trúc (numbering, timeline, schema) tách bạch khỏi các metric ngữ nghĩa (mismatch, repetition, grammar) — và đánh dấu rõ nhóm thứ hai là **"unverified — self-reported"** cho đến khi có cơ chế đo độc lập.
- Tính lại và sửa `semantic_beat_count` (129, không phải 130) trong `manifest.json` và `REVIEW_SUMMARY.md`.

**Batch 1 — Xây lớp đo độc lập tối thiểu (không cần đổi generator):**
- Xây một lượt QA chạy tách biệt, nhận input = toàn bộ `04_VIDEO_PROMPT_TIMELINE.json` + `03_AUDIO_SCRIPT_TTS.txt`, output = entity-traceability report + frequency ledger cho toàn bộ 402 prompt cùng lúc (không theo batch 25-30).
- Áp dụng cho EP004 hiện có để có baseline thật (không phải baseline tự nhận).

**Batch 2 — Sửa data model + instruction (`VISUAL_ENGINE.md`):**
- Thêm ràng buộc bắt buộc `obligation_source_phrase` không rỗng và traceable.
- Thêm `secondary_objects[].source` + cap tần suất tường minh.
- Thay `global_template_id` bằng frequency ledger theo object đã chuẩn hoá.
- Validate schema cho `main_action`/`main_subject` (cấm token rác, cấm dấu `|` rò rỉ).

**Batch 3 — Thêm Shot Plan layer (mục 9.3):**
- Với các episode mới, sinh shot plan cấp beat trước khi sinh visual obligation cấp clip — để filler không còn là quyết định độc lập theo từng khối 6 giây.

**Batch 4 — Áp dụng lại cho EP004 (sau khi có Batch 1-3) và regenerate có kiểm soát:**
- Không nằm trong phạm vi audit này (audit không regenerate) — nhưng nên là bước tiếp theo có chủ đích, không phải một vòng "rewrite 391/402 prompt và tự PASS" khác.

**Batch 5 — Chuẩn hoá cho nhiều domain/episode:**
- Đưa `VISUAL_ENGINE.md` + data model mới vào `SHARED_LIBRARIES/PRODUCTION_TEMPLATES/` để các domain khác (Criminal Law, Feng Shui, True Crime, Psychology, Music) dùng chung lớp kiểm chứng, không lặp lại lỗi tự-chứng-nhận ở từng domain riêng lẻ.

---

## 13. Giữ / viết lại / loại bỏ

**Nên giữ:**
- Khối 6 giây cố định làm đơn vị render (mục 6, câu 9).
- Cấu trúc `OUTPUT/04_VIDEO_CREATE_PROMPTS.txt` dạng plain text (Prompt N / Timeline / Narration context / Video prompt) — đơn giản, đúng mục đích handoff.
- Concept `semantic_beat_id` → nhiều clip/beat — đúng hướng, chỉ cần thực thi chặt hơn.
- `visual_mode` enum (6 giá trị) — rõ ràng, hữu ích, nên giữ nguyên.
- `continuity_keys`/`scene_sequence_id` — cấu trúc đúng, không phát hiện lỗi (129/129 sequence liên tục, không tái sử dụng cách quãng).
- Nguyên tắc "Buddhist Representation Safety" trong `VISUAL_ENGINE.md` — không thuộc phạm vi lỗi được audit này phát hiện.

**Nên viết lại:**
- Cơ chế "chống trùng" (`global_template_id`, `template_reuse_justified`) — viết lại hoàn toàn theo hướng frequency ledger (mục 9.4, 10).
- Toàn bộ quy trình QA cho video prompt trong `06_QA_REPORT.md` — cần tách bạch cấu trúc vs ngữ nghĩa, và cần một `computed_by` minh bạch.
- Đoạn logic ghép `main_subject` (nguồn gốc của dấu `|` và token rác `"a"`) — cần thay bằng một bước validate/sanitize schema tường minh trước khi ghi vào JSON.

**Nên loại bỏ:**
- Các đoạn QA "ma" trong `06_QA_REPORT.md` tham chiếu tới file đã archive (`04_VISUAL_BRIEF.md`, `03_SUBTITLE_SEGMENTS.json`, "Lifecycle Gate QA" nói về `READY_FOR_SCRIPT_REVIEW`) — không còn phản ánh trạng thái gói hiện tại, gây nhiễu cho bất kỳ ai đọc báo cáo.
- Mô hình append-only cho QA report (5 addendum chồng lên nhau, không addendum nào ghi đè/làm rõ addendum trước) — nên thay bằng một QA report được **tính lại từ đầu** mỗi lần, không cộng dồn lịch sử vào cùng một file coi như bằng chứng hiện hành.

---

## 14. Ước lượng rủi ro nếu tiếp tục patch kiến trúc hiện tại

- **Rủi ro cao nhất: false confidence lan rộng sang nhiều episode/domain.** Vì lỗi nằm ở cơ chế đo (không phải ở một vài prompt lỗi cụ thể), mỗi episode mới sinh ra theo kiến trúc hiện tại sẽ tiếp tục tự báo "0 mismatch/0 repetition" bất kể chất lượng thực tế — rủi ro này **tăng theo số lượng episode**, không giảm dần theo thời gian.
- **Chi phí ẩn của "rewrite gần như toàn bộ" lặp lại nhiều lần.** 5 vòng QA trên EP004 đã rewrite 371-402/402 prompt mỗi vòng — nghĩa là chi phí sinh nội dung thực tế cao gấp nhiều lần một lần sinh đúng ngay từ đầu, trong khi vẫn không đảm bảo chất lượng cuối cùng (vì thước đo vẫn sai sau cả 5 vòng).
- **Nếu chỉ patch từng triệu chứng** (ví dụ: thêm rule "không dùng blank note card" thủ công), hệ thống sẽ tìm một vật thể phụ khác để lấp chỗ trống theo đúng cơ chế cũ — vì root cause (không có ràng buộc nguồn gốc + không có cap tần suất + QA tự chứng nhận) vẫn còn nguyên. Đây là lý do khuyến nghị REFACTOR thay vì PATCH.
- **Rủi ro thấp hơn nếu KHÔNG rebuild toàn bộ**: schema JSON hiện tại (`semantic_beat_id`, `visual_obligation`, `continuity_keys`...) là nền tảng hợp lý, không cần bỏ đi. Rebuild toàn bộ sẽ tốn công sức không cần thiết cho phần đã đúng hướng (phân đoạn theo semantic beat, giữ liên tục scene sequence, đơn vị 6 giây).

---

## 15. Kết luận cuối cùng

```
REFACTOR CORE PIPELINE
```

**Không PATCH CURRENT SYSTEM**, vì root cause nằm ở cơ chế đo lường (measurement mechanism), không phải ở nội dung từng prompt — patch từng triệu chứng (một vật thể phụ cụ thể, một câu ngữ pháp cụ thể) sẽ không ngăn được hệ thống tái tạo lại đúng loại lỗi đó ở episode tiếp theo, vì bản chất tautological của `global_template_id` và bản chất tự-chứng-nhận của QA vẫn còn nguyên.

**Không REBUILD VIDEO CREATION MODULE toàn bộ**, vì phần khung dữ liệu (semantic beat → visual obligation → continuity) và phần cấu trúc timeline (6 giây, liên tục, không gap/overlap) đã đúng hướng và đã được xác nhận hoạt động chính xác về mặt cấu trúc — bỏ đi toàn bộ sẽ lãng phí phần đã làm đúng, và rủi ro làm mất luôn các ràng buộc an toàn tôn giáo (Buddhist Representation Safety) hiện đang hoạt động tốt.

**REFACTOR CORE PIPELINE** là lựa chọn đúng vì thay đổi cần thiết tập trung vào đúng ba điểm: (1) thay cơ chế chống-trùng từ hash-toàn-văn sang frequency ledger theo thực thể ngữ nghĩa, (2) bắt buộc truy vết nguồn gốc mọi vật thể thị giác về narration, và (3) tách lớp QA ra khỏi lớp sinh nội dung để nó trở thành một phép đo thật, không phải một lời tự nhận. Cả ba thay đổi này đều thực hiện được **trong khuôn khổ kiến trúc hiện có**, không cần thiết kế lại từ đầu toàn bộ khái niệm pipeline.
