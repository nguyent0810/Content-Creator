# VIDEO CREATION REFACTOR BLUEPRINT
Tiếp nối `VIDEO_CREATION_ARCHITECTURE_AUDIT.md`. Không audit lại từ đầu — nhiệm vụ ở đây là (1) verify lại các Critical Root Cause bằng bằng chứng cứng hơn, hạ/nâng confidence khi cần, và tự sửa nếu audit trước sai; (2) thiết kế kiến trúc thay thế. Read-only. Không sửa code, không regenerate prompt, không tạo prototype.

Toàn bộ số liệu re-verify trong tài liệu này được tính lại độc lập bằng script Node.js chạy trên chính `_INTERNAL/04_VIDEO_PROMPT_TIMELINE.json` và grep trực tiếp trên `OUTPUT/04_VIDEO_CREATE_PROMPTS.txt` / `OUTPUT/03_AUDIO_SCRIPT_TTS.txt` — không lấy lại số liệu đã viết sẵn trong audit trước mà không kiểm chứng.

---

## 1. Verify toàn bộ Critical Root Cause

### C1 — QA là tự-chứng-nhận (self-attestation), không phải phép đo độc lập

**Root Cause**
Không có tác nhân/thủ tục nào tách biệt khỏi quá trình sinh nội dung để tính các chỉ số chất lượng ngữ nghĩa; các chỉ số này do chính lượt sinh nội dung tự ghi vào JSON/manifest ngay sau khi viết xong.

↓

**Evidence (re-verified, mạnh hơn audit trước)**
- `qa_status`: 402/402 record = `"PASS"` tuyệt đối, không một giá trị nào khác (đếm lại bằng script, không suy diễn).
- `visual_narration_alignment`: 402/402 = `"PASS"` tuyệt đối (đếm lại bằng bộ đếm trực tiếp trên toàn bộ mảng — audit trước dùng regex lookahead qua Grep, vốn có rủi ro engine không hỗ trợ lookahead và cho "No matches" giả; lần này xác nhận lại bằng phép đếm trực tiếp trong Node, kết quả giống nhau nên **kết luận cũ đứng vững, nay có bằng chứng chắc hơn**).
- **Phát hiện mới, mạnh hơn:** `required_narration_details` và `details_covered` **byte-identical ở 402/402 record, không một sai lệch nào**. Đây là bằng chứng trực tiếp rằng chỉ số `video_prompt_concrete_detail_coverage_percentage: 100` không được "đo" — nó **luôn luôn đúng 100% theo cấu trúc dữ liệu**, vì trường "covered" đơn thuần là bản sao của trường "required" chứ không phải kết quả đối chiếu độc lập với nội dung `video_prompt` thực tế. Đây là dạng tautology rõ ràng nhất tìm được trong toàn bộ hệ thống.
- **Phát hiện mới:** `CORE_OS/VISUAL_ENGINE.md` — văn bản duy nhất quy định pipeline này — **không hề chứa các cụm "semantic beat", "visual obligation", "global_template_id", "template_reuse_justified", "continuity_keys", "scene_sequence_id"** (grep toàn văn 193 dòng: 0 kết quả). Toàn bộ khái niệm cốt lõi mà `manifest.json` công bố là pipeline chính thức (`"video_prompt_visual_pipeline": "SEMANTIC_BEAT_FIRST -> VISUAL_BEAT_DECOMPOSITION -> DISTINCT_VISUAL_OBLIGATION_PER_CLIP -> VIDEO_PROMPT"`) **không có định nghĩa bằng văn bản ở bất kỳ đâu trong repo**. Nghĩa là không chỉ QA tự chấm — mà **cả luật để QA chấm theo cũng do chính lượt sinh nội dung tự phát minh ra trong lúc chạy**, không lưu lại thành một spec ổn định để lần chạy sau (hay một người review) đối chiếu.
- 5 vòng QA addendum trong `06_QA_REPORT.md`/`REVIEW_SUMMARY.md` (Video Prompt QA → Targeted → Safe Rollback → No Random Continuity → Remove Meta Template) mỗi vòng tự nhận `0` lỗi nhưng vòng sau vẫn viết lại 371–402/402 prompt (đã re-count nguyên văn bảng số liệu, khớp với audit trước).

↓

**Code Path**
Không tồn tại. Không có module/hàm/script nào trong repo tính các trường `qa_status`, `visual_narration_alignment`, `*_count`. `TOOLS/package_audit.py` — script thật duy nhất — chỉ đọc `manifest.json` cấp gói (`schema_version`, `package_status`, hash file) và **không mở/đọc `04_VIDEO_PROMPT_TIMELINE.json` hay bất kỳ trường `video_prompt_*` nào** (đã đọc lại 80 dòng đầu của script, không có logic liên quan). "Code path" thực chất là: **chỉ thị ngôn ngữ tự nhiên trong `CORE_OS/VISUAL_ENGINE.md` §"Prompt QA" (dòng 177–193)**, được một LLM diễn giải và tự thực thi trong cùng một phiên với việc sinh nội dung.

↓

**Data Path**
`_INTERNAL/04_VIDEO_PROMPT_TIMELINE.json` → field `prompts[i].qa_status`, `prompts[i].visual_narration_alignment`, `prompts[i].required_narration_details`/`details_covered` → tổng hợp thành `_INTERNAL/manifest.json` field `video_prompt_qa_status`, `video_prompt_visual_narration_mismatch_count`, `video_prompt_concrete_detail_coverage_percentage` → phản ánh vào `_INTERNAL/06_QA_REPORT.md` và `_INTERNAL/REVIEW_SUMMARY.md` dưới dạng bảng "PASS".

↓

**Runtime Effect**
Gói EP004 đạt `content_status: READY_FOR_TTS_HANDOFF`, `video_prompt_qa_status: PASS`, `video_prompt_batch_gate_status: PASS` — tất cả cổng lifecycle được thông qua — trong khi tài liệu này (và audit trước) chứng minh được nhiều lỗi thực tế cụ thể (mục 1.C3, mục 5) mà các cổng đó lẽ ra phải chặn lại.

↓

**Confidence: High** (nâng từ mức suy luận của audit trước lên High nhờ bằng chứng tautology `required_narration_details === details_covered` và bằng chứng "pipeline vocabulary không tồn tại trong spec" — cả hai đều là phép đếm/grep trực tiếp, không suy diễn).

---

### C2 — Cơ chế "chống trùng" (`global_template_id`) đo chuỗi ký tự, không đo nội dung thị giác

**Root Cause**
`global_template_id` được dùng làm khoá chống trùng duy nhất, nhưng giá trị của nó biến thiên theo văn bản đã sinh (hoặc một tổ hợp luôn-duy-nhất khác), nên không bao giờ bắt được lặp về mặt khái niệm/thị giác.

↓

**Evidence (re-verified, có bằng chứng phản chứng trực tiếp — mạnh hơn audit trước)**
Audit trước suy luận `global_template_id = hash(text)` từ việc 402/402 giá trị duy nhất. Lần này, để **chứng minh chứ không suy luận**, đã tìm các nhóm prompt có `main_subject` + `main_action` **giống hệt nhau tuyệt đối** (nếu `global_template_id` là hash của riêng hai trường này, các prompt trong cùng nhóm phải có cùng id) — và đối chiếu id thực tế:

| Cặp subject+action lặp lại | Số lần | Ví dụ prompt | `global_template_id` |
|---|---:|---|---|
| `"the familiar empty wooden chair" + "stands"` | **15** | P1, P22, P41, P93, P115, P197, P218, P233, P242, P326, P351, P381, P390, P393, P400 | **15 giá trị khác nhau tuyệt đối** |
| `"a blank note card" + "lies"` | **15** | P24, P43, P95, P151, P160, P199, P220, P235, P244, P295, P302, P328, P383, P392, P402 | **15 giá trị khác nhau tuyệt đối** |
| `"dust and late-afternoon light" + "drift"` | **16** | P23, P42, P94... | **16 giá trị khác nhau tuyệt đối** |

Tổng cộng **18 nhóm** subject+action trùng lặp tuyệt đối (93 prompt liên quan), **không một nhóm nào** có `global_template_id` trùng nhau trong nhóm. Điều này chứng minh trực tiếp (không còn là suy luận): `global_template_id` **không phải hàm của (subject, action)** — nó phải phụ thuộc vào một thành phần luôn-đổi (nhiều khả năng là toàn văn `video_prompt`, vì độ dài `video_prompt` của các prompt cùng nhóm cũng luôn khác nhau, ví dụ nhóm "empty wooden chair/stands" có `video_prompt_len` trải từ 657 đến 870 ký tự — không có hai bản ghi nào giống hệt nhau).

**Bằng chứng bổ sung, dạng dễ kiểm chứng nhất tìm được trong toàn bộ audit:** cụm "chỉ đạo camera" (`Use a ... movement only.`) trong `OUTPUT/04_VIDEO_CREATE_PROMPTS.txt` chỉ có **10 biến thể duy nhất cho 402 prompt**, trong đó riêng 4 biến thể: `"slow documentary push-in"` (125), `"locked-off observational frame"` (125), `"gentle lateral track"` (112), `"quiet close-up"` (26) — cộng lại **388/402 = 96.5%** tổng số prompt dùng nguyên văn một trong 4 câu này. Đây là lặp **chuỗi ký tự tuyệt đối, đếm được bằng `grep -c`**, không cần suy luận ngữ nghĩa — và **không có chỉ số nào trong `manifest.json` đo lường điều này** (không có `video_prompt_camera_phrase_repetition_count` hay tương đương). Ba trong bốn cụm phổ biến nhất còn **không nằm trong danh sách "Camera Language" được duyệt** của `CORE_OS/VISUAL_ENGINE.md` (dòng 122–135: chỉ liệt kê "slow dolly in/out, gentle lateral tracking, controlled crane movement, static contemplative composition, slow orbit, subtle handheld documentary movement, aerial drift") — "slow documentary push-in", "locked-off observational frame", "quiet close-up" là thuật ngữ tự phát sinh, trôi khỏi spec gốc.

↓

**Code Path**
Không tồn tại. Không có hàm hash nào trong repo. Giá trị hex 16 ký tự (`42fcbd07230d200b`...) được LLM tự ghi vào JSON, có hình thức giống output của một hàm hash thật nhưng không thể xác minh nó được tính bằng thuật toán nào vì không có code — đây bản thân nó là một rủi ro bổ sung: dữ liệu "trông như" được tính toán máy móc nhưng thực chất là văn bản tự do do LLM viết ra.

↓

**Data Path**
`prompts[i].global_template_id`, `prompts[i].template_reuse_justified` (402/402 = `false`, không một lần nào được set `true`) → `manifest.json.video_prompt_global_repeated_template_count: 0`, `video_prompt_unjustified_template_reuse_count: 0`.

↓

**Runtime Effect**
93/402 prompt (23%) có main_subject+main_action trùng lặp tuyệt đối, và ~68.7% prompt dùng 1 trong 3 cụm camera không nằm trong spec — nhưng cả hai loại lặp này đều được báo cáo là `0` trong mọi chỉ số chống-trùng hiện có.

↓

**Confidence: High** (nâng từ Medium/suy luận ở audit trước lên High — có bằng chứng phản chứng trực tiếp bằng cách đối chiếu 18 nhóm trùng lặp thực tế với id thực tế của chúng, cộng thêm bằng chứng camera-phrase độc lập, dễ kiểm chứng lại bằng một lệnh `grep` đơn giản).

---

### C3 — Không có ràng buộc "vật thể thị giác phải bắt nguồn từ narration" (hallucination không bị chặn)

**Root Cause**
`main_subject`/vật thể phụ trong `video_prompt` không bị ràng buộc phải suy ra được từ `obligation_source_phrases` hay `required_narration_details` của chính clip đó — nên một vật thể hoàn toàn không có trong narration có thể được chèn vào mà vẫn nhận `visual_narration_alignment: PASS`.

↓

**Evidence (re-verified, có điều chỉnh so với audit trước)**
- Grep toàn văn `03_AUDIO_SCRIPT_TTS.txt` (255 dòng, 5222 từ) cho các biến thể "note/thư/giấy/mảnh giấy/nhắn tin/tin nhắn/viết": **chỉ có đúng 1 kết quả**, dòng 129: *"...cách ta nhắn tin, cách ta nghe điện thoại..."* — nói về hành vi nhắn tin hiện đại, **không mô tả một vật thể "mảnh giấy trống"** nào.
- Trong JSON, 45 record có `main_subject` chứa "blank note card"/"note card". Kiểm tra lại **từng record trong số 45** (không chỉ mẫu 5 như audit trước) bằng cách đối chiếu `obligation_source_phrases` + `required_narration_details` của chính record đó với các từ khoá liên quan đến "note/thư/lời chưa nói": **44/45 (97.8%) hoàn toàn không có căn cứ**; **1/45** có liên hệ gián tiếp chấp nhận được (P12, `required_narration_details: ["words not yet said", "empty chair"]` — ý niệm "lời chưa kịp nói" có thể biện minh phần nào cho một vật biểu tượng, dù bản thân "note card" vẫn là một bước diễn giải xa).
  → **Đây là một điều chỉnh so với audit trước**: audit trước ngụ ý toàn bộ 45 lần dùng đều vô căn cứ như nhau; số liệu re-verify cho thấy tỉ lệ chính xác là **44/45 (97.8%) vô căn cứ, 1/45 có thể biện minh yếu**. Kết luận tổng thể của audit trước (đạo cụ này về cơ bản là hallucination lặp lại) **vẫn đúng**, chỉ cần làm chính xác hơn tỉ lệ.
- `visual_narration_alignment` của cả 45/45 record này đều là `"PASS"` — xác nhận: trường tự-chứng-nhận này không có khả năng phát hiện loại lỗi trên.

↓

**Code Path**
Không tồn tại. Không có bước validate nào đối chiếu `main_subject` với `obligation_source_phrases`. `VISUAL_ENGINE.md` không có quy tắc "vật thể trong prompt phải truy vết được về narration" — mục "Narration-To-Visual Mapping" (dòng 56–62) chỉ nói về ranh giới câu/đoạn cho việc chia timeline, không nói về nguồn gốc vật thể.

↓

**Data Path**
`prompts[i].obligation_source_phrases` (luôn không rỗng, đã verify 402/402 có giá trị — nhưng "không rỗng" ≠ "liên quan") → `prompts[i].main_subject` (không bị ràng buộc phải là tập con suy ra được từ trường trên) → `prompts[i].video_prompt` → không có trường tổng hợp nào trong `manifest.json` đo "tỉ lệ vật thể có căn cứ" (trường gần nhất, `video_prompt_obligation_without_source_count: 0`, đo việc "obligation" có nguồn hay không — chứ không đo việc **vật thể cụ thể được chọn để vẽ obligation đó** có nguồn hay không; đây là khác biệt bị bỏ sót giữa lớp trừu tượng và lớp cụ thể, xem mục 4).

↓

**Runtime Effect**
Một đạo cụ không có trong kịch bản (blank note card) xuất hiện lặp lại 45 lần trên 402 clip (11.2% tổng thời lượng phim) mà không một cơ chế nào trong hệ thống hiện tại có khả năng gắn cờ.

↓

**Confidence: High** cho kết luận tổng thể ("hallucination không bị chặn, xảy ra thực tế, lặp lại nhiều lần"). **Medium** cho con số chính xác "44/45" vì việc phân loại "có căn cứ hay không" ở ranh giới (như P12) vẫn có một phần đánh giá chủ quan — không phải phép đếm hoàn toàn máy móc như các con số khác trong tài liệu này.

---

## 2. Information Loss Map

| Bước | Input | Output | Information Preserved | Information Lost | Information Invented | Fallback Triggered | File | Function | Rule |
|---|---|---|---|---|---|---|---|---|---|
| **1. Narration → Semantic Beat** | `03_AUDIO_SCRIPT_TTS.txt`, 255 dòng, 5222 từ, không có timing thật | `semantic_beat_id` (129 phân biệt, verify lại = 129, không phải 130 như `manifest.json`/`REVIEW_SUMMARY.md` công bố), `narration_context`, `source_paragraph_ids` | Trích dẫn gần-nguyên-văn của narration cho mỗi beat (verify: `narration_context` khớp câu gốc ở các mẫu đã đối chiếu) | (a) Timing thật — chỉ có ước lượng 130 wpm, đánh dấu `ESTIMATED` nhưng không có cơ chế bắt buộc retime khi có audio thật; (b) độ chi tiết trong-beat — với beat có 2-5 clip, `narration_context` là **một khối văn bản giống hệt nhau cho mọi clip trong beat** (verify: 129/129 beat có ≥2 clip đều dùng chung 1 `narration_context`, không phân mảnh theo clip) — người đọc JSON không thể biết chỉ từ `narration_context` clip nào-trong-beat đang vẽ phần nào | Không phát hiện việc bịa nội dung ở bước này | Không có rule fallback tường minh nào được ghi lại (không có trường "segmentation_fallback_used" hay tương đương) | Không tồn tại — không có script | Không tồn tại — LLM tự suy luận theo văn xuôi | `VISUAL_ENGINE.md` §"Narration-To-Visual Mapping" (dòng 56–62): "consider sentence boundaries, paragraph boundaries, punctuation pauses, semantic context..." — **không có thuật toán, không có ngưỡng, không tái lập được giữa hai lần chạy** |
| **2. Semantic Beat → Visual Obligation** | 129 beat | 402 `visual_obligation` (329 giá trị phân biệt — mức đa dạng ngữ nghĩa ở lớp trừu tượng là **tốt**, xem mục 4), `obligation_source_phrases`, `required_narration_details`/`details_covered` | Trích dẫn cụ thể hơn per-clip (`obligation_source_phrases` khác nhau giữa các clip cùng beat — verify đúng ở P1 vs P2) | Liên kết nhân-quả/cảm xúc giữa các beat — **không có trường nào lưu quan hệ nhân quả hay dòng cảm xúc xuyên suốt** (chỉ có `visual_progression_role`, 5 giá trị rời rạc, không nối tiếp thành mạch) | `details_covered` **luôn = `required_narration_details`** (402/402 byte-identical, verify bằng script) — "coverage" là copy, không phải kết quả đối chiếu | Không rõ — không có trường đánh dấu | Không tồn tại | Không tồn tại | **Không hề được định nghĩa ở đâu trong `VISUAL_ENGINE.md`** — thuật ngữ "visual obligation" hoàn toàn vắng mặt trong văn bản instruction chính thức (grep xác nhận 0 kết quả) |
| **3. Visual Obligation → Shot Planning (camera/composition)** | `visual_obligation`, `visual_progression_role` | Không có trường JSON riêng cho "shot plan" — quyết định camera/composition nằm **hoàn toàn trong văn xuôi tự do của `video_prompt`** (câu `"Use a ... movement only."`) | `visual_mode` (6 giá trị, khớp đúng danh sách được duyệt trong `VISUAL_ENGINE.md` §83-94 — đây là điểm **tuân thủ tốt**) | Cấu trúc hoá của lựa chọn camera — không thể query/validate/thống kê camera choice mà không parse lại câu tiếng Anh tự do | Chuỗi camera drôi khỏi 8 cụm được duyệt trong `VISUAL_ENGINE.md` (mục 1.C2): "slow documentary push-in", "locked-off observational frame", "quiet close-up" — 3 cụm này **không có trong spec** nhưng chiếm 96.5% tần suất cùng với "gentle lateral track" | Không có cơ chế fallback — khi không chắc chọn gì, hệ thống mặc định lặp lại 1 trong 4 cụm quen thuộc | Không tồn tại | Không tồn tại | `VISUAL_ENGINE.md` §"Camera Language" (dòng 122–135) — có danh sách được duyệt nhưng **không có cơ chế enforce**, và **không có trường JSON để enforce lên** |
| **4. Shot Planning → Scene/Prop Selection** | `visual_obligation`, `continuity_keys` (kế thừa từ scene trước) | `main_subject`, `main_action`, `location`, vật thể phụ nhồi trong khung `"In the background... Also visible..."` | `continuity_keys` cho motif chủ đạo đã duyệt (empty chair ở P1-2, giữ nhất quán trong cùng `scene_sequence_id`) | **Đây là điểm mất thông tin nghiêm trọng nhất trong toàn pipeline**: không có ràng buộc vật thể phụ phải suy ra từ `obligation_source_phrases` của chính clip → 44/45 lần "blank note card" hoàn toàn ngắt kết nối với nguồn (mục 1.C3) | Vật thể phụ bịa đặt: "blank note card" (45 lần), phần lớn "closed door/door seam" (74 lần) không có căn cứ tại vị trí xuất hiện | Khi không có vật thể cụ thể trong narration, hệ thống **fallback về vốn từ vựng quen thuộc đã dùng trước đó** (chair/door/lamp/note/altar) thay vì báo "không đủ căn cứ, dùng ABSTRACT_METAPHOR" | Không tồn tại | Không tồn tại | **Không được định nghĩa ở đâu** — đây là bước "mất tích" hoàn toàn trong tài liệu instruction, chỉ tồn tại như hành vi ngầm định của LLM |
| **5. Prop Selection → Prompt Composition** | `main_subject`, `main_action`, `location`, vật thể phụ | `video_prompt` (câu tiếng Anh hoàn chỉnh) | Khung `Buddhist Representation Safety`/`Negative Constraints` (`VISUAL_ENGINE.md` §137-175) được áp dụng nhất quán (verify: 0 vi phạm rõ ràng phát hiện được trong mẫu đã đọc) | Ngữ pháp: dữ liệu hỏng ở bước ghép trường rò rỉ thẳng ra câu cuối — `main_subject` chứa dấu `"|"` ở **272/402 (67.7%)** record (verify bằng script, cao hơn nhiều so với ước lượng ngầm của audit trước), và `main_action` chứa token rác (`"a"` × 15, `"the"` × 3 — tổng 18/402) | Câu chạy sai ngữ pháp trong chính file public, ví dụ dòng 259/784 `04_VIDEO_CREATE_PROMPTS.txt`, lặp gần-verbatim cách nhau ~13 phút | Không có validate/sanitize nào chặn token rác trước khi ghi ra text cuối | Không tồn tại | Không tồn tại | Không có rule nào trong `VISUAL_ENGINE.md` về việc ghép trường — đây thuần tuý là lỗi tầng thực thi (LLM tự "quên" xoá mảnh vụn khi ghép chuỗi) |
| **6. Prompt Composition → Final Prompt + tự-QA** | `video_prompt` hoàn chỉnh | `qa_status`, `visual_narration_alignment`, `global_template_id`, `template_reuse_justified` — **được ghi vào cùng record, cùng lượt sinh** | Cấu trúc file (Prompt N / Timeline / Narration context / Video prompt) — nhất quán 402/402 (verify: đúng định dạng ở mọi vị trí đã kiểm tra) | Ranh giới kiểm chứng độc lập — hoàn toàn không tồn tại | Toàn bộ 30 trường `video_prompt_*_count` trong `manifest.json` là suy luận/tự khai, không phải phép đo | N/A — không có khái niệm fallback QA (QA luôn PASS) | `06_QA_REPORT.md`, `manifest.json` | Không tồn tại | `VISUAL_ENGINE.md` §"Prompt QA" (dòng 177–193) liệt kê **các tiêu chí cần kiểm** nhưng không nói **ai/cái gì thực hiện việc kiểm**, dẫn tới việc tác nhân sinh nội dung tự đảm nhận luôn vai trò này |

**Tóm tắt 3 câu hỏi trọng tâm của mục này:**
- **Narration biến mất ở đâu?** Không biến mất ở cấp beat (trích dẫn được giữ khá tốt) — biến mất ở cấp **trong-beat** khi một beat có nhiều clip: `narration_context` không phân mảnh, chỉ `obligation_source_phrases` mới phân mảnh, và ngay cả trường phân mảnh này cũng không được dùng làm ràng buộc bắt buộc cho việc chọn vật thể (Bước 4).
- **Semantic bị giảm thành template ở đâu?** Ở Bước 3 (Shot Planning/camera) và Bước 4 (Scene/Prop Selection) — đây là hai bước **hoàn toàn không có định nghĩa văn bản**, nên hành vi mặc định của LLM là quay về một vốn từ vựng hẹp đã dùng trước đó.
- **Visual obligation bị thay bằng scene pool ở đâu?** Chính xác tại ranh giới Bước 4: `visual_obligation`/`required_narration_details` (lớp trừu tượng, verify có 329/402 giá trị phân biệt — đa dạng tốt) bị ánh xạ xuống `main_subject`/vật thể phụ (lớp cụ thể, verify có tới 44/402 record dùng chung "a blank note card", 113/402 dùng "chair" trong main_subject) **mà không có hàm ánh xạ tường minh nào** — đây chính là "khoảng trống" nơi một scene pool ngầm định hình thành.

---

## 3. Failure Propagation Map

### 3.1 Scene repetition (camera-phrase & prop-phrase level)
```
Where created:      Bước 3-4 (Shot Planning/Prop Selection) — không có shot plan cấp beat,
                     không có frequency cap cho vật thể phụ/camera phrase
        ↓
Where amplified:     Bước 5 (Prompt Composition) — mỗi clip độc lập chọn lại filler từ cùng
                     vốn từ vựng, không có bộ nhớ toàn cục (episode memory) nào được tham chiếu
        ↓
Where hidden:        Bước 6 (tự-QA) — global_template_id hash toàn văn nên 402/402 "unique";
                     QA chạy theo batch 25-30 (`rewrite_batch: "P17_402_BATCH_1..16"`,
                     verify đúng cấu trúc batch) nên không có lượt nào nhìn toàn cục 402
                     prompt cùng lúc để thấy P24 và P402 dùng chung "blank note card"
        ↓
Where should have
been detected:       Một lượt QA toàn cục, đếm tần suất theo chuẩn hoá-đồng-nghĩa
                     (không phải theo chuỗi ký tự), chạy SAU khi toàn bộ 402 prompt đã có
        ↓
Why not detected:    (1) đơn vị đo là chuỗi ký tự (mục 1.C2); (2) đơn vị QA là batch nhỏ,
                     không phải toàn tập; (3) không có ngưỡng tần suất (cap) được định nghĩa
                     ở bất kỳ đâu trong VISUAL_ENGINE.md
```

### 3.2 Semantic mismatch (visual không khớp narration)
```
Where created:      Bước 4 — vật thể phụ được chọn không bắt buộc suy ra từ
                     obligation_source_phrases của chính clip
        ↓
Where amplified:     Không amplify theo nghĩa lan rộng lỗi — nhưng LẶP LẠI cùng kiểu
                     mismatch nhiều lần vì cùng một "prop quen thuộc" được tái dùng
                     (44/45 lần "blank note card" đều là mismatch độc lập, không phải
                     một lỗi lan truyền từ lỗi trước)
        ↓
Where hidden:        Bước 6 — visual_narration_alignment được LLM tự gán "PASS" ngay khi
                     viết record, không có bước đối chiếu ngược lại narration gốc
        ↓
Where should have
been detected:       Một bước "entity traceability check": trích thực thể cụ thể (danh từ)
                     từ video_prompt, so với danh từ có trong obligation_source_phrases/
                     narration_context, gắn cờ nếu không tìm thấy liên hệ
        ↓
Why not detected:    Trường `visual_narration_alignment` tồn tại NHƯNG được gán giá trị bởi
                     cùng tác nhân vừa chọn vật thể — không có input độc lập (narration gốc
                     dưới dạng có thể so khớp máy móc) được đưa vào bước gán giá trị này
```

### 3.3 Continuity leak (vật thể sai bối cảnh)
```
Where created:      Không xảy ra ở cấp scene_sequence_id (verify: 129/129 sequence liên
                     tục, continuity_to_prompt 0 broken link) — KHÔNG có continuity leak
                     theo đúng nghĩa "vật thể của scene A rò sang scene B liền kề"
        ↓
Where amplified:     Xảy ra ở cấp KHÁC: vật thể phụ (không phải continuity_keys chính thức)
                     bị tái sử dụng CÁCH QUÃNG xa (P12 và P402, cách nhau 390 prompt/~65
                     phút) — đây là "cross-scene leak" của vốn từ vựng chung, không phải
                     lỗi continuity_keys kỹ thuật
        ↓
Where hidden:        continuity_keys (trường chính thức) hoạt động đúng nên mọi check
                     "continuity" hiện có đều PASS hợp lệ — nhưng các check này không bao
                     phủ vật thể phụ nằm ngoài continuity_keys
        ↓
Where should have
been detected:       Cần một khái niệm RIÊNG cho "vật thể phụ toàn cục" (không phải
                     continuity_keys trong-scene) với sổ tần suất xuyên suốt 402 prompt
        ↓
Why not detected:    Nhầm lẫn phạm vi: hệ thống hiện tại chỉ định nghĩa continuity ở cấp
                     TRONG một scene_sequence, không có khái niệm continuity/tần suất ở
                     cấp TOÀN EPISODE cho vật thể phụ không chính thức
```
*Lưu ý tự sửa: audit trước dùng cụm "continuity object xuất hiện sai bối cảnh" — sau khi verify lại, đây **không phải lỗi continuity_keys kỹ thuật** (cơ chế đó hoạt động đúng) mà là lỗi ở một khái niệm khác, chưa được đặt tên: tần suất vật thể phụ toàn cục. Cần phân biệt rõ hai khái niệm này khi thiết kế lại (mục 6, 8).*

### 3.4 Filler ("In the background...", "Also visible...")
```
Where created:      Bước 5 — khung câu cố định được LLM dùng làm cách "lấp đầy" phần còn
                     lại của 6 giây sau khi đã mô tả main_subject/main_action
        ↓
Where amplified:     Lặp lại ở 189/402 (47%) vì đây là cách "an toàn" để thêm chi tiết mà
                     không cần suy nghĩ lại cấu trúc câu — không bị chặn vì không tính vào
                     bất kỳ metric nào
        ↓
Where hidden:        global_template_id khác nhau vì phần điền vào khung khác nhau ở cấp
                     từ vựng, dù cấu trúc câu giống hệt
        ↓
Where should have
been detected:       Kiểm tra n-gram cấu trúc câu (sentence skeleton), không phải n-gram
                     từ vựng — đây là loại kiểm tra hoàn toàn không tồn tại trong hệ thống
                     hiện tại (không có metric nào tên gần với "skeleton"/"sentence
                     structure repetition")
        ↓
Why not detected:    Không có ai/cái gì định nghĩa "filler" là một loại lỗi cần đo trong
                     VISUAL_ENGINE.md hay trong schema — nó chỉ được người dùng (audit
                     requester) nêu ra như một quan sát định tính, hệ thống chưa từng có
                     khái niệm đo lường tương ứng
```

### 3.5 Fake uniqueness (đổi camera/màu/vật thể phụ để né trùng)
```
Where created:      Hệ quả trực tiếp của C2 (mục 1) — vì thước đo trùng lặp là chuỗi ký
                     tự, "đổi một từ" luôn đủ điều kiện để được tính là "unique"
        ↓
Where amplified:     5 vòng rewrite (Batch 1→16, Targeted, Safe Rollback, No Random
                     Continuity, Remove Meta Template) — mỗi vòng đều là cơ hội để đổi
                     wording mà không bắt buộc đổi nội dung thị giác thực sự
        ↓
Where hidden:        Đúng ở bước tự-QA (C1) — không có bước nào hỏi "nội dung có thực sự
                     khác không" tách biệt khỏi "chuỗi ký tự có khác không"
        ↓
Where should have
been detected:       Semantic/visual fingerprint (Scene Concept + Subject + Action +
                     Setting + Narrative Function — mục 8), không phải text hash
        ↓
Why not detected:    Thước đo duy nhất tồn tại (global_template_id) về bản chất TOÁN HỌC
                     không thể phát hiện loại lỗi này — không phải do thực thi kém, mà do
                     lựa chọn thước đo sai từ đầu
```

### 3.6 QA false PASS (bao trùm)
```
Where created:      Thiết kế: QA và generation cùng một tác nhân, cùng một lượt suy luận
        ↓
Where amplified:     Mỗi lần "revision" (5 vòng) tái tạo lại đúng vấn đề: tự viết, tự chấm,
                     tự PASS — không có vòng nào phá vỡ chu trình này
        ↓
Where hidden:        Ở chính manifest.json/06_QA_REPORT.md — nơi lẽ ra phải là "bằng chứng
                     khách quan cuối cùng" lại là nơi tổng hợp mọi tự-chứng-nhận thành số
        ↓
Where should have
been detected:       Ở cấp KIẾN TRÚC — cần một ranh giới tổ chức (organizational boundary)
                     bắt buộc QA phải nhận input độc lập và không được truy cập lại
                     "lý do" mà generator đã dùng để tự thuyết phục mình là đúng
        ↓
Why not detected:    Đây không phải lỗi thực thi từng bước — đây là lỗi THIẾT KẾ QUY TRÌNH
                     ở cấp cao nhất (CORE_OS/VISUAL_ENGINE.md không bao giờ yêu cầu tách
                     tác nhân QA khỏi tác nhân generation)
```

---

## 4. Responsibility Matrix

| Thành phần | Đánh giá | Giải thích |
|---|---|---|
| **Segmentation** (Narration → Semantic Beat) | **Needs Improvement** | Kết quả cấu trúc đúng (129 beat, mọi clip map về đúng 1 beat, timeline không gap/overlap — verify đúng) nhưng không có thuật toán tường minh, không tái lập được, và tự mâu thuẫn số liệu (129 thực tế vs 130 công bố). |
| **Semantic Representation** (`visual_obligation`, `required_narration_details`) | **Healthy** (ở lớp trừu tượng) | 329/402 `visual_obligation` phân biệt, `obligation_source_phrases` luôn có giá trị, luôn trích đúng câu nguồn ở các mẫu đã kiểm — đây là lớp làm **tốt nhất** trong toàn hệ thống. Vấn đề nằm ở lớp cụ thể-hoá phía sau nó (Scene Selection), không phải ở chính lớp này. |
| **Visual Obligation → Shot Planning** | **Broken** | Không tồn tại như một bước riêng có dữ liệu (mục 2, Bước 3) — camera/composition chỉ là văn xuôi tự do, không enforce theo `VISUAL_ENGINE.md`, 96.5% dùng lại 4 cụm cố định, 3/4 cụm không nằm trong spec được duyệt. |
| **Scene/Prop Selection** | **Should Replace** | Nguồn gốc trực tiếp của cả hallucination (blank note card) lẫn fake-uniqueness. Không có ràng buộc nguồn gốc, không có frequency cap, không có định nghĩa văn bản. Đây là thành phần cần thiết kế lại từ đầu (không chỉ "cải thiện"), vì hiện tại nó không tồn tại như một bước tường minh — cần TẠO MỚI, không phải sửa. |
| **Continuity (`continuity_keys`, `scene_sequence_id`)** | **Healthy** | Verify lại: 129/129 scene sequence liên tục, 0 broken `continuity_to_prompt` link, 0 non-contiguous scene_sequence_id. Đây là cơ chế hoạt động đúng như thiết kế — nên giữ nguyên. Lưu ý: phạm vi của nó chỉ trong-scene, không bao phủ vật thể phụ toàn cục (mục 3.3) — không phải lỗi của chính nó, mà là khoảng trống nó không được thiết kế để lấp. |
| **Prompt Composer** (ghép câu cuối) | **Broken** | Rò rỉ dữ liệu hỏng ra câu cuối (`main_action` = "a"/"the" ở 18 record, dấu `|` ở 272/402 `main_subject`) — không có bước sanitize/validate trước khi ghi. Khung câu filler cố định (47%) cũng thuộc trách nhiệm của bước này. |
| **QA (video-prompt QA addenda)** | **Should Replace** | Toàn bộ khái niệm hiện tại (tự chấm trong cùng lượt sinh) là sai cấu trúc, không phải sai chi tiết. Không thể "cải thiện" bằng cách thêm câu hỏi mới cho QA hỏi — vì bản thân AI trả lời câu hỏi đó vẫn là tác nhân vừa viết nội dung. Cần thay bằng một tầng độc lập thật sự (mục 9). |
| **Manifest (`video_prompt_*` fields)** | **Needs Improvement** | Cấu trúc field tốt, phong phú, có ý định đúng (đo nhiều khía cạnh) — nhưng toàn bộ giá trị là tự khai. Không cần đổi schema, cần đổi **nguồn** của giá trị (từ "LLM tự điền" sang "tính lại từ JSON bằng phép đếm"). Đã tìm được 1 lỗi số liệu cụ thể (130 vs 129) chứng minh không có bước đối chiếu ngược. |
| **Metrics** (`*_count`, `*_percentage` nói chung) | **Broken** | Phân biệt rõ hai nhóm (đã verify): nhóm cấu trúc (numbering, timeline gap/overlap, JSON valid) — đúng, đáng tin; nhóm ngữ nghĩa (mismatch, repetition, grammar, generic obligation) — toàn bộ không đáng tin vì lý do đã chứng minh ở mục 1 và mục 5. |

---

## 5. Xác minh False Metrics

| Metric (`manifest.json`) | Đang đo cái gì (thực tế) | KHÔNG đo cái gì | Có thể PASS trong khi output sai? | Ví dụ cụ thể (re-verified) |
|---|---|---|---|---|
| `video_prompt_consecutive_template_repetition_count: 0` | So khớp `main_subject`+`main_action` giữa **hai prompt liền kề duy nhất** | Trùng lặp cách quãng (không liền kề); trùng lặp về cấu trúc câu/camera; trùng lặp về vật thể phụ (không nằm trong `main_subject`) | **Có** | 18 nhóm subject+action trùng lặp tuyệt đối (93 prompt) nhưng không liền kề nhau → metric = 0, thực tế lặp 23% số prompt |
| `video_prompt_global_repeated_template_count: 0` | Đếm số `global_template_id` trùng nhau, mà `global_template_id` = hash của văn bản luôn-khác-nhau | Trùng lặp ngữ nghĩa/thị giác dưới bất kỳ hình thức nào | **Có, gần như luôn luôn** | 96.5% prompt (388/402) dùng 1 trong 4 câu camera cố định — metric vẫn = 0 |
| `video_prompt_unjustified_template_reuse_count: 0` | Đếm số lần `template_reuse_justified: true` — nhưng trường này **không bao giờ được set `true`** (402/402 = `false`) | Bất kỳ trường hợp tái sử dụng thực tế nào, vì trường nguồn không hoạt động | **Có** | Không thể phân biệt "chưa từng reuse" với "cơ chế đánh dấu reuse chưa từng chạy" |
| `video_prompt_concrete_detail_coverage_percentage: 100` | So khớp `details_covered` với `required_narration_details` — nhưng hai trường **byte-identical ở 402/402 record theo thiết kế** (verify bằng script) | Việc `video_prompt` (câu tiếng Anh) có thực sự vẽ ra các chi tiết trong `required_narration_details` hay không | **Luôn luôn PASS bất kể nội dung**, đây là tautology, không phải phép đo | Không cần ví dụ lỗi cụ thể — bản thân công thức tính đảm bảo 100% trong mọi trường hợp |
| `video_prompt_visual_narration_mismatch_count: 0` / `narration_visual_mismatch_count: 0` | Tự-đánh-giá `visual_narration_alignment` bởi cùng tác nhân sinh nội dung | Đối chiếu thực thể (entity) trong `video_prompt` với danh từ có trong `narration_context` gốc | **Có** | 44/45 lần "blank note card" không có căn cứ trong narration — cả 45 đều `visual_narration_alignment: PASS` |
| `video_prompt_english_grammar_issue_count: 0` | Tự-đánh-giá, không chạy qua bất kỳ bước kiểm tra ngữ pháp nào | Lỗi rò rỉ dữ liệu (`main_action: "a"`) trong chính câu cuối | **Có** | Dòng 259, 784 `04_VIDEO_CREATE_PROMPTS.txt`: câu chạy sai ngữ pháp, xuất hiện gần-verbatim 2 lần |
| `video_prompt_anachronistic_object_count: 0` | Tự-đánh-giá | Không kiểm chứng được bằng phương pháp trong tài liệu này (chưa đọc đủ 402/402 để khẳng định có/không vi phạm) | **Không kết luận được PASS hay FAIL — chỉ kết luận được: phương pháp đo không đáng tin** | Không có ví dụ vi phạm cụ thể tìm được trong mẫu đã đọc — nhưng đây không phải bằng chứng cho "đúng", chỉ là "chưa tìm thấy phản chứng" |
| `video_prompt_semantic_beat_count: 130` | Con số do LLM tự khai, không đối chiếu lại với chính JSON nó mô tả | Số `semantic_beat_id` phân biệt thực tế trong `04_VIDEO_PROMPT_TIMELINE.json` | **Sai, đã xác nhận trực tiếp** (không phải "có thể sai") | Đếm lại: 129 giá trị `semantic_beat_id` phân biệt, không phải 130 |
| `video_prompt_batch_gate_status: PASS` (5 lần, mỗi vòng revision) | Trạng thái hoàn tất của một vòng rewrite theo batch ≤30 prompt | Việc vòng rewrite tiếp theo có cần thiết hay không — nếu vòng trước thật sự PASS, tại sao vòng sau viết lại 371-402/402? | **Có, và đã xảy ra 5 lần liên tiếp trong cùng 1 episode** | `06_QA_REPORT.md` mục "Video Prompt QA Addendum" → "Remove Meta Template Video Prompt QA Addendum": 5 vòng PASS, mỗi vòng viết lại gần như 100% |

**Nhắc lại ràng buộc của yêu cầu:** camera, lighting, framing, weather, tính từ, cách chọn từ (wording) **không được coi là visual uniqueness** trong toàn bộ đánh giá trên. Bằng chứng camera-phrase (96.5% dùng 4 cụm cố định) được trình bày như **một dạng lặp cần đo**, không phải như bằng chứng của "tính đa dạng" — kể cả khi wording xung quanh nó khác nhau.

---

## 6. Thiết kế pipeline mới

```
Narration
   ↓
Semantic Extraction
   ↓
Semantic Beat
   ↓
Visual Obligation
   ↓
Shot Planner
   ↓
Continuity Manager
   ↓
Scene Planner
   ↓
Prompt Composer
   ↓
Independent QA
   ↓
Final Prompt
```

| Tầng | Input | Output | Ownership | Invariant bắt buộc |
|---|---|---|---|---|
| **Semantic Extraction** | Toàn văn narration (`03_AUDIO_SCRIPT_TTS.txt`) | Danh sách thực thể/hành động/quan hệ nhân quả được trích xuất **tường minh, có thể kiểm tra lại bằng cách so khớp chuỗi con** (không phải chỉ diễn giải tự do) | Tầng này sở hữu "sự thật ngôn ngữ" — mọi tầng sau chỉ được tham chiếu, không được tự ý bổ sung thực thể mới | Mọi thực thể được trích phải là chuỗi con (hoặc paraphrase có thể truy vết 1-1) của chính narration; không suy diễn thực thể không xuất hiện |
| **Semantic Beat** | Output của Semantic Extraction + ranh giới câu/đoạn | Beat có `source_span`, `meaning`, `entities`, `causal_links` (mục 7.1) | Sở hữu "đơn vị ý nghĩa" — là ranh giới không được các tầng sau chia nhỏ hơn về mặt NGỮ NGHĨA (dù có thể chia nhỏ hơn về mặt SỐ CLIP render) | Mỗi beat phải có `source_span` không rỗng, không chồng lấn với beat khác; tổng `source_span` phải phủ 100% narration (đối chiếu tự động được) |
| **Visual Obligation** | 1 Semantic Beat | N nghĩa vụ thị giác (N = số clip 6 giây cần để phủ beat đó) | Sở hữu "cái gì bắt buộc phải thấy" — KHÔNG sở hữu "thấy như thế nào" (đó là việc của Shot Planner) | Mỗi obligation phải trích `source_evidence` không rỗng từ beat cha; `required_subject`/`required_action` phải suy ra được từ `source_evidence` (không phải từ vốn từ vựng toàn cục) |
| **Shot Planner** | 1 Semantic Beat + toàn bộ Visual Obligation của beat đó | Shot Plan cấp BEAT (không phải cấp clip riêng lẻ): số shot, vai trò từng shot, tiến trình camera | Sở hữu "kịch bản dựng cảnh" — quyết định TRƯỚC khi cụ thể hoá từng clip, để tránh việc mỗi clip tự ứng biến filler độc lập | Camera choice phải nằm trong vốn từ vựng đã duyệt (đóng, có thể mở rộng theo quy trình duyệt riêng — không phải tự phát sinh); không có shot nào không gắn với ít nhất 1 obligation |
| **Continuity Manager** | Scene Planner của các beat trước (trạng thái tích luỹ) | Continuity State cập nhật: motif đang active, tần suất vật thể phụ toàn cục | Sở hữu "trí nhớ toàn episode" — là tầng DUY NHẤT được phép biết những gì đã xảy ra ở các prompt trước | Không thành phần nào khác được phép tự ý "nhớ" lại prompt trước — mọi tham chiếu continuity phải đi qua tầng này; mọi vật thể phụ phải kiểm tra tần suất qua tầng này trước khi được chọn |
| **Scene Planner** | Shot Plan (từ Shot Planner) + Continuity State (từ Continuity Manager) | Vật thể cụ thể (`main_subject`, vật thể phụ) cho từng shot, đã qua kiểm tra tần suất và nguồn gốc | Sở hữu "lựa chọn cụ thể hoá" — đây là tầng thay thế cho "Scene/Prop Selection" hiện đang **không tồn tại tường minh** (mục 4) | Mọi vật thể phải hoặc (a) truy vết được về `source_evidence` của obligation, hoặc (b) là motif đã duyệt trong `global_visual_profile`, hoặc (c) gắn nhãn `INVENTED` kèm lý do — không có lựa chọn thứ tư |
| **Prompt Composer** | Scene Planner output + ràng buộc an toàn tôn giáo/negative constraints | Câu `video_prompt` tiếng Anh hoàn chỉnh | Sở hữu "diễn đạt ngôn ngữ cuối" — KHÔNG được tự ý thêm/bớt vật thể (đó là việc của Scene Planner) | Output phải validate được bằng schema (không cho phép token rác trong các trường cấu trúc trước khi ghép câu); đa dạng hoá cấu trúc câu (không dùng quá X% một khung câu) |
| **Independent QA** | TOÀN BỘ 402 prompt cùng lúc (không theo batch) + narration gốc + Continuity State cuối cùng | QA Result (mục 7.5) | Sở hữu "phán quyết khách quan" — **không được chạy trong cùng lượt suy luận đã tạo ra nội dung**, không được truy cập "lý do" nội bộ mà Scene Planner đã dùng để tự thuyết phục, chỉ được truy cập input/output quan sát được | Mọi số liệu trong QA Result phải tính lại được từ dữ liệu thô (không chấp nhận giá trị do tầng trước tự khai); QA phải chạy trên toàn tập, không theo batch nhỏ |

---

## 7. Data Model

### 7.1 Semantic Beat

| Field | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|
| `beat_id` | string | có | duy nhất toàn episode |
| `source_span` | {start_char, end_char} trên chính văn bản narration gốc | **có** | không rỗng, không chồng lấn beat khác, hợp lại phủ 100% narration |
| `meaning` | string (tóm tắt 1 câu) | có | phải là diễn giải, không phải trích dẫn nguyên văn (để phân biệt với `source_span`) |
| `entities` | list of string | **có** | mỗi entity phải là chuỗi con hoặc từ đồng nghĩa trực tiếp của văn bản trong `source_span` |
| `actions` | list of string | có | tương tự `entities`, truy vết được về `source_span` |
| `emotions` | string hoặc enum có kiểm soát | có | không được chỉ tồn tại dưới dạng văn xuôi tự do trong prompt cuối (khác với hiện trạng — hiện tại cảm xúc chỉ nằm trong câu "The emotion should feel...") |
| `causal_links` | list of {`from_beat_id`, `relation`} | không bắt buộc nhưng khuyến nghị mạnh | nếu có, `from_beat_id` phải tồn tại và đứng trước beat hiện tại theo thứ tự narration |
| `evidence` | = `source_span` dưới dạng text đã trích sẵn (denormalized để dễ đọc) | có | phải khớp chuỗi con chính xác với narration gốc tại `source_span` |

### 7.2 Visual Obligation

| Field | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|
| `obligation_id` | string | có | duy nhất |
| `beat_id` | string | có | phải trỏ tới Semantic Beat tồn tại |
| `required_subject` | string | **có** | phải truy vết được về `entities`/`evidence` của beat cha, HOẶC đánh dấu `abstract: true` kèm lý do |
| `required_action` | string | có | không được là single-token function word (chặn lại đúng loại lỗi `main_action: "a"` đã phát hiện) |
| `required_setting` | string | có | phải nhất quán với Continuity State đang active cho `scene_sequence` hiện tại |
| `forbidden_hallucination` | list of string | khuyến nghị | danh sách vật thể KHÔNG được dùng cho obligation này dù chúng phổ biến ở nơi khác (ví dụ: cấm "note card" trừ khi `evidence` thực sự nhắc tới văn bản viết) |
| `source_evidence` | string (trích từ beat) | **có, không rỗng** | phải là chuỗi con của `evidence` cấp beat |

### 7.3 Shot Plan

| Field | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|
| `shot_plan_id` | string | có | 1-1 với `beat_id` |
| `shot_objective` | list of string, 1 phần tử/shot | có | mỗi objective phải map về đúng 1 hoặc nhiều `obligation_id` |
| `cinematic_choice` | list of {camera, framing} | có | camera phải thuộc vốn từ vựng đã duyệt (đóng nhưng mở rộng được qua quy trình duyệt, không tự phát sinh tự do) |
| `required_visual_evidence` | list of `obligation_id` | có | mọi obligation của beat phải xuất hiện trong đúng 1 shot, không thiếu không thừa |
| `continuity_dependency` | list of `continuity_state_key` | có | khai báo tường minh những gì shot này GIẢ ĐỊNH đã tồn tại từ shot/scene trước (để Continuity Manager kiểm tra được) |

### 7.4 Continuity State

| Field | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|
| `scene_sequence_id` | string | có | |
| `persistent_objects` | list of {object, first_seen_prompt, frequency_count, cap} | **có** | đây là cơ chế thay thế `global_template_id` — mỗi object phải có `cap` tường minh; vượt cap → tự động flag |
| `persistent_characters` | list of {character, visual_constraints} | có | tham chiếu tới `CHARACTER_USAGE_PLAN.md` đã có sẵn trong repo, không tạo song song |
| `location` | string | có | |
| `timeline_position` | {start_ms, end_ms} | có | |
| `causal_dependency` | list of {depends_on_prompt, reason} | khuyến nghị | dùng để phân biệt "tái sử dụng có chủ đích" (ví dụ: empty chair quay lại ở đoạn kết, có chủ đích callback) với "tái sử dụng ngẫu nhiên" |

### 7.5 QA Result

| Field | Kiểu | Bắt buộc | Ràng buộc |
|---|---|---|---|
| `qa_run_id` | string | có | gắn với `input_hash` của đúng phiên bản dữ liệu được chấm |
| `computed_by` | enum {`INDEPENDENT_PASS`, `SELF_REPORTED`} | **có, bắt buộc phân biệt rõ** | mọi số liệu công bố công khai (README, manifest) chỉ được lấy từ record có `computed_by: INDEPENDENT_PASS` |
| `semantic_score` | số 0-1 theo từng obligation | có | tính từ đối chiếu `required_subject`/`required_action` với `video_prompt` thực tế, KHÔNG được là copy của `required_narration_details` (chặn lại đúng loại tautology đã phát hiện ở mục 1.C1) |
| `visual_obligation_coverage` | % obligation có shot tương ứng | có | tính lại từ `Shot Plan.required_visual_evidence`, không tự khai |
| `continuity_coverage` | % continuity_dependency được thoả mãn | có | |
| `hallucination` | list of {object, prompt_id, reason} | có | liệt kê MỌI vật thể không truy vết được, không chỉ đếm số lượng |
| `repetition` | {theo Scene Concept, không theo hash — mục 8} | có | |
| `grammar` | list of {prompt_id, issue} | có | |
| `evidence` | tham chiếu ngược tới đúng `source_span`/`obligation_source_phrases` đã dùng để tính từng số liệu trên (để có thể tái kiểm tra thủ công) | có | |

---

## 8. Anti-Repetition Strategy

**Không dùng:** hash văn bản, so khớp wording, `template_id` dạng chuỗi ngẫu nhiên.

**Cơ chế đề xuất — Scene Fingerprint đa chiều:**

Mỗi shot được gán một fingerprint gồm 5 trục, mỗi trục là một giá trị đã CHUẨN HOÁ (không phải chuỗi tự do):

```
Scene Concept       — ý niệm hình ảnh cấp cao (ví dụ: "absence-marker", "assembly-scene",
                       "care-gesture") — một tập đóng, được duyệt trước, không tự phát sinh
        +
Subject              — thực thể chính, chuẩn hoá đồng nghĩa (chair/ghế → 1 nhãn duy nhất,
                       bất kể "the familiar empty wooden chair" hay "an empty chair by
                       the window" đều quy về cùng 1 nhãn subject)
        +
Action                — hành động chính, chuẩn hoá tương tự (stands/sits/rests → nhóm theo
                       nhóm ngữ nghĩa "static-presence", không phải chuỗi ký tự)
        +
Setting                — bối cảnh (nhà/temple/altar...), chuẩn hoá
        +
Narrative Function     — vai trò trong mạch kể (ESTABLISH/TRANSITION/REVEAL/CALLBACK...),
                       đã có sẵn dưới dạng `visual_progression_role` — giữ nguyên trường này
```

**Episode Memory** = một sổ tần suất tích luỹ theo (Scene Concept × Subject) trong suốt episode, cập nhật bởi Continuity Manager sau MỖI shot (không phải theo batch). Khi một tổ hợp (Scene Concept, Subject) vượt ngưỡng đã định (ví dụ: không quá X% tổng số shot, hoặc không quá N lần trong một cửa sổ M-phút), Scene Planner **bị chặn** dùng lại tổ hợp đó và bắt buộc phải chọn phương án khác hoặc dùng `visual_mode: ABSTRACT_METAPHOR` với lý do tường minh.

**Vì sao hiệu quả hơn hash:**
1. **Bất biến với wording**: "the familiar empty wooden chair" và "an empty chair by the window" cho cùng 1 fingerprint (Subject=CHAIR) — bắt được đúng 15 lần lặp "empty wooden chair + stands" mà `global_template_id` đã bỏ lọt hoàn toàn (mục 1.C2).
2. **Nhạy với lặp cách quãng**: vì Episode Memory là sổ tích luỹ toàn episode (không phải so khớp liền kề hay theo batch), nó bắt được P12 và P402 dùng chung "blank note card" dù cách nhau 390 prompt.
3. **Phân biệt được lặp-có-chủ-đích với lặp-ngẫu-nhiên**: motif chủ đạo đã duyệt (ví dụ empty chair ở đầu/cuối phim làm callback) được khai báo tường minh qua `causal_dependency` trong Continuity State (mục 7.4) — không bị đếm như lặp lỗi, trong khi "blank note card" xuất hiện không có khai báo callback nào sẽ bị chặn ngay từ lần thứ N+1.
4. **Đo được đúng loại lặp mà camera-phrase evidence (mục 5) cho thấy đang bị bỏ sót hoàn toàn**: một trục fingerprint riêng cho cinematic choice (đối chiếu ngược với Shot Plan §7.3) có thể áp dụng cùng cơ chế cap cho camera, không chỉ cho vật thể.

---

## 9. Independent QA

**Nguyên tắc bắt buộc:** generator không được tự chấm. QA phải là một lượt suy luận/thủ tục KHÁC — không có quyền truy cập "quá trình suy nghĩ" đã tạo ra nội dung, chỉ nhận input quan sát được (narration gốc + JSON output hoàn chỉnh), và mọi output của nó phải gắn `computed_by: INDEPENDENT_PASS` (mục 7.5) để phân biệt với các báo cáo tự khai trước đây.

QA mới tối thiểu phải kiểm 6 hạng mục sau, mỗi hạng mục chạy trên **toàn bộ tập prompt cùng lúc**, không theo batch nhỏ (khắc phục trực tiếp lỗ hổng đã chứng minh ở mục 3.1, 3.6 — batch ≤30 khiến không lượt nào nhìn thấy lặp cách quãng xa):

1. **Semantic alignment** — đối chiếu `required_subject`/`required_action` (Visual Obligation) với nội dung thực tế của `video_prompt` — không copy `required_narration_details` sang `details_covered` như tautology hiện tại.
2. **Hallucination** — với mỗi vật thể xuất hiện trong `video_prompt`, kiểm tra nó có truy vết được về `source_evidence` hay được khai báo tường minh là motif đã duyệt hay không; nếu không → liệt kê, không chỉ đếm số.
3. **Repetition** — dùng Scene Fingerprint (mục 8), không dùng hash; chạy trên toàn episode, không theo batch.
4. **Continuity** — đối chiếu `continuity_dependency` khai báo trong Shot Plan với Continuity State thực tế tại thời điểm đó (bắt được cả continuity kỹ thuật hiện đang tốt, lẫn tần suất vật thể phụ toàn cục hiện đang thiếu — mục 3.3).
5. **Grammar** — validate schema cứng cho các trường cấu trúc trước khi chúng được ghép thành câu (chặn được chính xác loại lỗi `main_action: "a"`/`"the"` và dấu `|` rò rỉ, đã phát hiện ở 18 và 272 record tương ứng) + một lượt đọc lại câu hoàn chỉnh tìm câu chạy/thiếu động từ.
6. **Evidence traceability** — mọi số liệu ở 5 mục trên phải neo được ngược lại về `source_span`/`obligation_source_phrases` cụ thể đã dùng để tính ra nó (đúng yêu cầu `evidence` trong QA Result, mục 7.5) — để một người review có thể tái kiểm tra thủ công bất kỳ con số nào mà không phải tin tưởng mù quáng.

---

## 10. Migration Plan

### Batch 1 — Sửa cách đo, không sửa nội dung
- **Mục tiêu:** Dừng việc công bố số liệu tự-khai như thể là số liệu đã kiểm chứng. Sửa `manifest.json`/`REVIEW_SUMMARY.md`: đổi `video_prompt_semantic_beat_count` từ 130 → 129 (đã xác nhận sai); gắn nhãn `SELF_REPORTED` cho toàn bộ 30 trường `video_prompt_*_count`/`*_percentage` hiện có cho tới khi có Batch 2.
- **Rủi ro:** Thấp — không đụng nội dung, chỉ đụng metadata/label.
- **Expected improvement:** Không cải thiện chất lượng video prompt, nhưng chặn được việc ra quyết định dựa trên số liệu sai (ví dụ: không nên dùng `video_prompt_qa_status: PASS` hiện tại làm căn cứ publish).
- **Backward compatibility:** Hoàn toàn tương thích — không đổi schema, chỉ thêm/sửa giá trị field.

### Batch 2 — Xây Independent QA tối thiểu (mục 9), áp dụng thử trên EP004 đã có
- **Mục tiêu:** Có được baseline THẬT (không phải baseline tự nhận) cho chính EP004 hiện tại, không regenerate.
- **Rủi ro:** Trung bình — cần định nghĩa "chuẩn hoá đồng nghĩa" cho Scene Fingerprint (mục 8), là công việc cần một vài vòng hiệu chỉnh để không quá lỏng (bỏ lọt) hay quá chặt (báo động giả).
- **Expected improvement:** Có số liệu đáng tin để quyết định EP004 có cần rewrite hay không — hiện tại quyết định này không có căn cứ đáng tin.
- **Backward compatibility:** Không đổi `04_VIDEO_PROMPT_TIMELINE.json`/`04_VIDEO_CREATE_PROMPTS.txt` hiện có — QA mới chỉ ĐỌC, tạo ra report mới song song.

### Batch 3 — Cập nhật `CORE_OS/VISUAL_ENGINE.md` với vốn từ vựng chính thức
- **Mục tiêu:** Viết vào văn bản chính thức các khái niệm hiện chỉ tồn tại ngầm định (semantic beat, visual obligation, scene fingerprint, continuity state, cap tần suất) — để pipeline có MỘT nguồn sự thật ổn định, không phải "bất cứ gì LLM phát minh ra trong lượt chạy đó".
- **Rủi ro:** Trung bình — đây là thay đổi tài liệu instruction cấp lõi, ảnh hưởng tới mọi domain dùng chung `CORE_OS` (không chỉ Buddhism/Kinh Địa Tạng).
- **Expected improvement:** Loại bỏ hoàn toàn root cause "pipeline vocabulary không được định nghĩa ở đâu" (mục 1.C1) — điều kiện tiên quyết để bất kỳ QA nào (kể cả Batch 2) có một spec ổn định để đối chiếu.
- **Backward compatibility:** Cần rà soát `MASTER_AGENT.md`/`PRODUCTION_ENGINE.md` để giải quyết mâu thuẫn scope đã nêu (audit trước, mục H5) — đây là điểm duy nhất trong migration plan có khả năng ảnh hưởng ngược lên các engine khác ngoài `VISUAL_ENGINE.md`.

### Batch 4 — Thêm Shot Planner + Scene Planner như 2 bước tường minh mới (mục 6, 7.3)
- **Mục tiêu:** Lấp khoảng trống lớn nhất đã xác định (mục 2, Bước 3-4; mục 4 "Should Replace") — nơi camera và vật thể phụ hiện đang được quyết định mà không qua bất kỳ dữ liệu có cấu trúc nào.
- **Rủi ro:** Cao nhất trong 4 batch — đây là thay đổi kiến trúc thực sự (thêm 2 tầng dữ liệu mới), cần thử nghiệm trên episode mới trước, không áp ngay cho EP004.
- **Expected improvement:** Giải quyết tận gốc cả 6 loại lỗi trong Failure Propagation Map (mục 3) cho các episode SINH MỚI sau Batch 4 — không hồi tố cho EP004.
- **Backward compatibility:** Định dạng `OUTPUT/04_VIDEO_CREATE_PROMPTS.txt` (Prompt N/Timeline/Narration context/Video prompt) **không đổi** — thay đổi chỉ nằm ở cách `_INTERNAL/04_VIDEO_PROMPT_TIMELINE.json` được tạo ra phía sau, nên không phá vỡ bất kỳ hệ thống downstream nào đang đọc file public.

**Về EP004 cụ thể:** không nằm trong phạm vi audit/blueprint này để quyết định regenerate hay không (ràng buộc: không regenerate prompt). Batch 2 (Independent QA áp dụng thử) là bước hợp lý tiếp theo để có căn cứ ra quyết định đó ở một task riêng.

---

## 11. Quyết định cuối — KEEP / REFACTOR / REPLACE / REMOVE

| Thành phần | Quyết định | Lý do |
|---|---|---|
| Đơn vị render 6 giây, cấu trúc `Prompt N/Timeline/Narration context/Video prompt` | **KEEP** | Đã verify: 402 prompt liên tục, 0 gap/overlap, định dạng nhất quán 100%. Không có lỗi nào được tìm thấy ở tầng này. |
| `visual_mode` (6 giá trị enum) | **KEEP** | Tuân thủ đúng spec đã duyệt (`VISUAL_ENGINE.md` §83-94), phân bố hợp lý, không phát hiện vi phạm. |
| `continuity_keys` / `scene_sequence_id` / `continuity_from_prompt`/`continuity_to_prompt` | **KEEP** | Verify: 129/129 sequence liên tục, 0 broken link. Cơ chế đúng thiết kế — chỉ cần MỞ RỘNG phạm vi (Batch 4), không cần sửa. |
| `semantic_beat_id` + phân đoạn semantic beat | **REFACTOR** | Khái niệm đúng hướng (329/402 `visual_obligation` phân biệt — lớp trừu tượng lành mạnh), nhưng cần thuật toán tường minh, tái lập được, và đối chiếu số liệu tự động (129 vs 130). |
| `obligation_source_phrases` / `required_narration_details` | **REFACTOR** | Giữ khái niệm "trích nguồn", nhưng bỏ cơ chế `details_covered` = copy của `required_narration_details` (tautology) — thay bằng phép đối chiếu thật với `video_prompt` (mục 7.5, 9.1). |
| Camera/shot decision (hiện nằm trong văn xuôi tự do) | **REPLACE** | Không có dữ liệu cấu trúc để sửa — cần thay bằng Shot Planner (mục 6, 7.3) như một tầng mới hoàn toàn. |
| Scene/Prop Selection (vật thể phụ, hiện không tồn tại tường minh) | **REPLACE** | Đây là nguồn gốc trực tiếp của hallucination (blank note card) và phần lớn fake-uniqueness. Không "sửa" được vì hiện tại nó không tồn tại như một bước có dữ liệu — cần TẠO MỚI theo thiết kế ở mục 6, 7.3, 8. |
| `global_template_id` / `template_reuse_justified` | **REMOVE** | Đã chứng minh trực tiếp (mục 1.C2) đây là thước đo sai về bản chất toán học, không thể sửa bằng cách điều chỉnh — phải bỏ hẳn, thay bằng Scene Fingerprint + Episode Memory (mục 8). |
| Cơ chế QA hiện tại (tự chấm trong cùng lượt sinh, theo batch ≤30) | **REPLACE** | Không phải lỗi chi tiết — là lỗi thiết kế quy trình (mục 3.6). Thay bằng Independent QA (mục 9) chạy toàn tập, tách tác nhân. |
| Nội dung "ma" trong `06_QA_REPORT.md` (tham chiếu file đã archive, "Lifecycle Gate QA" lỗi thời) | **REMOVE** | Không phản ánh trạng thái hiện tại của gói, gây nhiễu, không có giá trị giữ lại. |
| Mô hình QA report append-only (5 addendum chồng lên nhau) | **REPLACE** | Thay bằng QA Result (mục 7.5) tính lại từ đầu mỗi lần, gắn `input_hash`, không cộng dồn lịch sử thành bằng chứng hiện hành. |
| `Buddhist Representation Safety` / `Negative Constraints` (`VISUAL_ENGINE.md` §137-175) | **KEEP** | Ngoài phạm vi lỗi đã phát hiện trong cả hai audit; không có bằng chứng vi phạm ở tầng này. |

**Tổng kết:** không có quyết định "rebuild toàn bộ" nào ở cấp thành phần — đúng như kết luận `REFACTOR CORE PIPELINE` của audit trước. Tuy nhiên ở cấp chi tiết, hai thành phần cụ thể (Scene/Prop Selection và cơ chế QA) cần **REPLACE** hoàn toàn chứ không phải REFACTOR, vì cả hai đều không tồn tại dưới dạng có dữ liệu/ranh giới tổ chức tường minh ở hiện trạng — không có gì để "chỉnh sửa", chỉ có thể xây mới bên cạnh phần khung (semantic beat, continuity, timeline) đang hoạt động đúng và nên giữ nguyên.
