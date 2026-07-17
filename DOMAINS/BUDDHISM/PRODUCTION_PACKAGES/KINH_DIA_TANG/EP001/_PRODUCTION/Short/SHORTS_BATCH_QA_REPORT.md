---
schema_version: 1.0
asset_id: AST_EP001_SHORTS_BATCH_QA_REPORT
asset_type: qa_report
episode_id: EP_BUD_KDT_001
package_id: PKG_BUD_KDT_EP001
domain_id: BUD
series_id: SB_BUD_001
version: 0.1.0
language: vi
reviewed_at: 2026-07-16
reviewer: independent QA pass (post-production, 6-agent batch)
---

# Shorts Batch QA Report — EP001 (30 Shorts)

## Vai trò tài liệu

Đây là báo cáo QA độc lập cho toàn bộ batch 30 YouTube Shorts mining từ `EP001/_INTERNAL/03_AUDIO_SCRIPT_MASTER.md`, được 6 agent khác nhau viết song song. Reviewer đã đọc trực tiếp và đầy đủ: `CORE_OS/SHORTS_ENGINE.md` (mục "Shorts-Specific QA Checklist" và "What Not To Do"), `EP001/_INTERNAL/03_AUDIO_SCRIPT_MASTER.md` (nguồn Long-form duy nhất), `EP001/_INTERNAL/01_RESEARCH_BRIEF.md` (Risk Flags / Things Not To Claim), `EP001/_INTERNAL/SHORTS_BATCH_PLAN.md` (kế hoạch mining đã duyệt), và cả 30 file `EP001_SHORT_01`…`EP001_SHORT_30/_INTERNAL/03_AUDIO_SCRIPT_MASTER.md`. Không có giả định nào được tin tưởng mặc định — mọi claim tự-QA trong Editorial Notes của từng Short đã được đối chiếu ngược lại với văn bản gốc.

## Bảng 30 Shorts

Ký hiệu: A = trùng lặp batch-level, B = hook self-sufficiency, C = trung thực nguồn, D = Risk Flags, E = loop-close, F = curiosity gap. ✅ = đạt, ⚠️ = lỗi nhẹ tìm thấy, ❌ = lỗi tìm thấy và đã sửa.

| # | Mode | A | B | C | D | E | F | Đã sửa? |
|---|---|---|---|---|---|---|---|---|
| 01 | Myth-Bust | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 02 | Symbol Decode | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 03 | Story Beat | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 04 | Compare/Contrast | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 05 | Quote/Reflection | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 06 | Modern Application | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 07 | Myth-Bust | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 08 | Symbol Decode | ✅ | ✅ | ✅ | ✅ | ⚠️ (loop-close hơi lỏng, không bắt buộc sửa) | ✅ | Không |
| 09 | Story Beat | ✅ | ✅ | ✅ | ✅ | ✅ (beat giữa, kết mở sang beat kế — được Engine cho phép cho story tách 3 beat) | ✅ | Không |
| 10 | Compare/Contrast | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 11 | Quote/Reflection | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 12 | Modern Application | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 13 | Myth-Bust | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 14 | Symbol Decode | ✅ | ✅ | ⚠️ ("gian phòng" là chi tiết bối cảnh nhẹ không có nguyên văn trong Long-form, không phải claim giáo lý — chấp nhận được) | ✅ | ✅ | ✅ | Không |
| 15 | Story Beat | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 16 | Compare/Contrast | ❌ Trùng claim + gần trùng cấu trúc câu kết với #22 | ✅ | ✅ | ✅ | ✅ | ✅ | **Có — đã sửa** |
| 17 | Quote/Reflection | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 18 | Modern Application | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 19 | Myth-Bust | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 20 | Symbol Decode | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 21 | Story Beat | ✅ | ✅ | ✅ | ✅ | ✅ (setup-beat, được Engine cho phép) | ✅ | Không |
| 22 | Compare/Contrast | ⚠️ (bị trùng bởi #16, đã xử lý bằng cách sửa #16) | ✅ | ✅ | ✅ | ✅ | ✅ | Không (giữ nguyên, là bản neo lại Risk Flag rõ ràng hơn) |
| 23 | Quote/Reflection | ✅ (đối chiếu #28 — khác trục, không trùng) | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 24 | Modern Application | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 25 | Myth-Bust | ✅ | ✅ | ❌ Dùng cụm Hán-Việt 16 chữ trong ngoặc kép, không có nguyên văn trong Long-form | ❌ Vi phạm kỹ thuật control "not inside hard quotation marks" | ✅ | ✅ | **Có — đã sửa** |
| 26 | Symbol Decode | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 27 | Story Beat | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 28 | Compare/Contrast | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 29 | Symbol Decode | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |
| 30 | Modern Application | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Không |

## Phần riêng: Trùng lặp phát hiện và cách đã sửa

### 1. Short #16 vs Short #22 — trùng claim cốt lõi + gần trùng cấu trúc câu kết (LỖI THẬT, đã sửa)

Cả hai đều là Compare/Contrast, đều nguồn từ vùng dòng 110-140 của Long-form, và cả hai bản gốc đã hội tụ về cùng một từ khóa "phép màu" và cùng một cấu trúc câu kết:

- #16 (gốc): "...Không có phép màu nào trong đó cả. Chỉ có một người chọn ở lại, năm này qua năm khác."
- #22 (gốc): "...Không có phép màu nào chạm vào là hết khổ. Chỉ có một người chọn không rời đi trước, một mình."

Dù hook và góc tiếp cận khác nhau trên giấy (thần chú vs. cứu rỗi tự động), người xem nghe liên tiếp hai Short này trong cùng một batch sẽ thấy chúng truyền đạt gần như cùng một insight bằng gần như cùng một câu — đây chính xác là loại trùng lặp mà `SHORTS_ENGINE.md` mục "Batch-level de-duplication" yêu cầu bắt.

**Cách sửa:** Giữ nguyên góc/mode đã duyệt của #16 trong `SHORTS_BATCH_PLAN.md` (đại nguyện vs. thần chú), chỉ viết lại nửa sau của kịch bản: bỏ hoàn toàn từ "phép màu" và cấu trúc "Không có X. Chỉ có Y.", thay bằng đối lập mới ("một câu thần chú chỉ cần nói đúng, là xong" vs. "một đại nguyện thì phải mang theo, ngày này qua ngày khác, không có điểm dừng") — vẫn đúng nội dung dòng 110 của Long-form, không thêm claim mới. #22 được giữ nguyên vì nó neo trực tiếp và rõ ràng hơn vào Risk Flag "vow guarantees automatic rescue" của Research Brief. word_count của #16 cập nhật từ 110 → 116.

### 2. Short #25 — dùng cụm Hán-Việt "16 chữ" trong ngoặc kép, không có nguyên văn trong Long-form (LỖI THẬT, đã sửa)

Bản gốc #25 mở bằng: `Nhiều người tin câu "Địa ngục vị không, thệ bất thành Phật" là nguyên văn lời kinh.` Hai vấn đề:

1. **Vi phạm Risk Flag kỹ thuật:** `01_RESEARCH_BRIEF.md` quy định rõ câu nguyện này phải được trình bày "not inside hard quotation marks as sutra text." Short #25 đặt đúng cụm đó trong ngoặc kép ở câu đầu tiên — dù ý đồ là để bác bỏ ngay sau đó (đúng cấu trúc Myth-Bust), hình thức trình bày vẫn đi ngược literal control này.
2. **Vi phạm trung thực nguồn:** cụm Hán-Việt cô đọng "Địa ngục vị không, thệ bất thành Phật. Chúng sinh độ tận, phương chứng Bồ Đề" **không xuất hiện nguyên văn** trong `03_AUDIO_SCRIPT_MASTER.md` (Long-form). Long-form cố tình chỉ diễn giải bằng tiếng Việt thường ở dòng 138 ("rằng nếu địa ngục vẫn còn người chịu khổ, thì thề không thành Phật; chừng nào chúng sinh chưa được độ hết, thì chưa nhận lấy quả vị giác ngộ cho riêng mình"), không dùng cụm cô đọng 16 chữ này. Cụm đó chỉ xuất hiện trong `01_RESEARCH_BRIEF.md` và các file nguồn địa phương chưa xác thực — tức Short #25 đã lấy chi tiết từ một tài liệu khác ngoài Long-form, vi phạm nguyên tắc "Fidelity to Long-form" của Shorts Engine.

**Cách sửa:** Bỏ hẳn ngoặc kép và cụm Hán-Việt cô đọng, thay bằng đúng cách diễn giải tiếng Việt mà Long-form dòng 138 đã dùng, không có ngoặc kép. Giữ nguyên góc Myth-Bust, cấu trúc, và loop-close đã duyệt trong `SHORTS_BATCH_PLAN.md`. word_count cập nhật từ 92 → 98.

### Các cặp gần-trùng đã kiểm tra và xác nhận KHÔNG cần sửa

- **Tích trượng #02 vs #07:** khác claim (ý nghĩa tiếng khua vs. bác bỏ hình ảnh vũ khí) — không trùng.
- **Minh châu #08 vs #13:** khác claim (chất lượng ánh sáng vs. bác bỏ bùa tài lộc) — không trùng.
- **Diêm La Vương #01 vs #04 vs #19:** ba claim tách bạch (myth chung / phân biệt vai trò cụ thể / chữ "Vương") — không trùng.
- **Ngưỡng cửa #21 vs #27 vs #29:** #21/#27 là setup-beat/resolution-beat hợp lệ của cùng cao trào (Engine cho phép); #29 là Symbol Decode tách khỏi dòng kể chuyện, kết bằng câu hỏi hướng người xem — không trùng.
- **"Không quay lưng" xuất hiện ở #05, #06, #12, #18, #30:** đây là throughline chủ đề của cả tập, nhưng mỗi Short áp dụng vào một tình huống cụ thể khác nhau (định danh trừu tượng / chăm bệnh / tin nhắn trì hoãn / lời cay nghiệt / người lạ khó khăn) — đúng tinh thần Modern Application của Engine, không phải trùng lặp.
- **#23 vs #28 (cùng vùng nguồn dòng 142-148):** #23 đối lập trên trục thời lượng cam kết (nói một lần vs. giữ nhiều năm), #28 đối lập trên trục giọng điệu (khiêm nhường vs. hùng tráng) — hai trục khác nhau, không trùng.

## Kết luận tổng thể

Batch 30 Shorts nhìn chung tuân thủ tốt `SHORTS_ENGINE.md` và Risk Flags của `01_RESEARCH_BRIEF.md`: không có tên tiền thân chưa xác minh ("Mục Kiền Liên Thanh") ở bất kỳ đâu, không có Short nào biến tích trượng thành vũ khí thật hay minh châu thành bùa tài lộc thật, không có Short nào khẳng định nguyện = cứu rỗi tự động, không có CTA directive, và hook của cả 30 Short đều tự đủ nghĩa (không đại từ treo). Đây là kết quả tốt hơn mong đợi cho một batch viết song song bởi 6 agent.

Tuy nhiên rà soát độc lập phát hiện đúng loại lỗi mà brief đã cảnh báo — trùng lặp lọt lưới giữa các agent không thấy bài của nhau: **Short #16 và #22 hội tụ về cùng một câu kết** dù xuất phát từ hai góc khác nhau trên giấy. Ngoài ra phát hiện thêm một vi phạm Risk Flag/fidelity độc lập ở **Short #25** (trích cụm Hán-Việt 16 chữ trong ngoặc kép, chi tiết không có trong Long-form). Cả hai đã được sửa trực tiếp, giữ nguyên góc/mode đã duyệt trong `SHORTS_BATCH_PLAN.md`, chỉ đổi câu chữ cụ thể.

**Tổng kết:** 30/30 Short đã đọc và đối chiếu độc lập. 2 Short có lỗi thật (#16, #25) — cả hai đã sửa. 2 điểm ghi nhận là lỗi nhẹ không bắt buộc sửa (#08 loop-close hơi lỏng, #14 "gian phòng" là chi tiết bối cảnh không có nguyên văn nhưng không phải claim giáo lý). Không phát hiện vi phạm nghiêm trọng nào về bịa danh xưng, biến biểu tượng thành vật thật, hay claim nguyện = phép màu tự động được khẳng định (mọi trường hợp nêu ra đều để bác bỏ). Khuyến nghị con người xem lại: xác nhận cách diễn đạt mới của #25 (không còn cụm Hán-Việt cô đọng) vẫn đủ "quotable"/nhận diện được với khán giả quen thuộc câu 16 chữ, vì đây là lựa chọn biên tập đánh đổi giữa độ nhận diện và độ an toàn nguồn.
