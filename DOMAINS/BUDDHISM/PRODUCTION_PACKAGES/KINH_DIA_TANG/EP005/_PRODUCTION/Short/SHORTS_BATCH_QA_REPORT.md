---
schema_version: 1.0
asset_id: AST_EP005_SHORTS_BATCH_QA_REPORT
asset_type: qa_report
episode_id: EP_BUD_KDT_005
package_id: PKG_BUD_KDT_EP005
domain_id: BUD
series_id: SB_BUD_001
version: 0.1.0
language: vi
canonical: false
reviewed_assets: 30
qa_reviewer: independent-agent-pass
created_at: 2026-07-16
---

# Shorts Batch QA Report — EP005 "Nghiệp Duyên Chúng Sinh" (30 Shorts)

## Phạm vi review

Đọc toàn bộ `CORE_OS/SHORTS_ENGINE.md`, `EP005/_INTERNAL/03_AUDIO_SCRIPT_MASTER.md` (Long-form gốc), `EP005/_INTERNAL/01_RESEARCH_BRIEF.md` (Risk Flags), `EP005/_INTERNAL/SHORTS_BATCH_PLAN.md`, và cả 30 file `EP005_SHORT_01`…`EP005_SHORT_30/_INTERNAL/03_AUDIO_SCRIPT_MASTER.md`. Review độc lập, không tin tưởng mặc định các ghi chú "đã tự kiểm" của agent viết gốc.

## Kết luận tổng quan

Batch đạt chất lượng cao về mặt an toàn nội dung (Risk Flags) — không phát hiện vi phạm nghiêm trọng nào (không có Short lãng mạn hóa duyên nợ thành lý do ở lại quan hệ độc hại, không có Short tuyên bố tính được cụ thể ai nợ ai từ kiếp nào, không có định mệnh luận, không đổ lỗi nạn nhân). Tuy nhiên rà soát độc lập phát hiện **3 lỗi thực chất** mà quy trình tự-QA của các agent viết gốc (và cả `SHORTS_BATCH_PLAN.md`) đã bỏ sót — cả 3 đã được sửa trực tiếp trong session này.

## Lỗi đã phát hiện và đã sửa (3)

### 1. Short #11 × Short #20 — trùng core claim gần như nguyên văn (nghiêm trọng — đúng điểm nghi ngờ được chỉ định)
Cả hai đều khai thác dòng 94 Long-form. Bản nháp gốc của #11 (Modern Application) dùng gần nguyên văn câu "Điều chắc chắn hơn cả, không phải là vì sao một người ở lại hay rời đi. Mà là cách bạn đối xử..." làm câu lõi — trong khi đây chính là câu mà #20 (Quote/Reflection) trích gần nguyên văn làm hook/core của chính nó. Hai Short chia sẻ đúng một core claim bằng gần như cùng một câu chữ, vi phạm "Batch-level de-duplication" của `SHORTS_ENGINE.md`. Dù hook mở đầu (hình ảnh) của hai Short khác nhau (kịch bản cụ thể "mối quan hệ đã kết thúc, chưa buông được" ở #11 vs. câu trích triết lý trực tiếp ở #20), phần thân/kết luận trùng lặp là vấn đề thật.
**Sửa:** Viết lại phần thân của #11 để neo vào dòng 138 (khác với dòng 94 mà #20 sở hữu), giữ nguyên hook, mode, và nguồn/ranh giới đã duyệt. `word_count` cập nhật 110 → 121.

### 2. Short #14 × Short #18 — trùng claim/câu chữ (nghiêm trọng — chưa từng được `SHORTS_BATCH_PLAN.md` tự phát hiện)
Cả hai khai thác dòng 92 Long-form (không thể tính ra ai nợ ai từ kiếp nào). Bản nháp gốc của #14 (Compare/Contrast) và #18 (Myth-Bust) dùng gần như cùng cụm từ làm câu trả lời chính: "không có công thức nào để tính ra...", "biết có mạng lưới — vậy là đủ, đoán thêm... thành một cách phán xét." Hai Short khác mode nhưng trả lời cùng một câu hỏi bằng gần như cùng câu chữ — mục "Kiểm tra chống trùng lặp" của `SHORTS_BATCH_PLAN.md` không hề đối chiếu cặp này dù cả hai cùng trích dòng 92.
**Sửa:** Viết lại #14 để khai thác một nhánh khác trong cùng dòng 92 — tương phản giữa hai HƯỚNG suy đoán có hại (đoán để trách người khác vs. đoán để tự trách bản thân), giữ #18 nguyên vẹn (nó là Myth-Bust chuẩn nhất cho Risk Flag "Things Not To Claim" #1). Góc mới của #14 còn bám sát hơn nguyên tắc "không đổ lỗi nạn nhân — kể cả tự đổ lỗi." `word_count` cập nhật 107 → 116.

### 3. Short #27 — hook có đại từ treo, vi phạm self-sufficiency (trung bình)
Hook gốc: "vì sao lại là người đó?" — đại từ "người đó" không có tiền ngữ trong chính Short này (trong Long-form nó tham chiếu ngược 4 vignette đã kể ở dòng 40–46, nhưng #27 đứng độc lập, không dựng lại các vignette đó). Đây đúng loại lỗi mẫu mà `SHORTS_ENGINE.md` nêu làm ví dụ lịch sử (Short EP001 về "lời nguyện" không nêu ai là người phát nguyện).
**Sửa:** Viết lại thành "vì sao chính một người cụ thể — không phải một ai khác — lại bước vào đời mình..." — giới thiệu chủ thể ngay trong câu, giữ tính khái quát (không thu hẹp về một loại quan hệ), giữ nguyên nguồn, mode, và loop-close đã duyệt. `word_count` cập nhật 78 → 79.

## Các mục đã kiểm tra và KHÔNG phát hiện lỗi

- **A. Trùng lặp toàn batch:** đã đọc lại 30/30 hook + nội dung cốt lõi liên tiếp. Ngoài 2 cặp đã sửa ở trên, không phát hiện cặp trùng nào khác đáng kể. Các trường hợp dùng chung một dòng nguồn nhưng khai thác các mệnh đề khác nhau (VD: #10/#25 cùng dòng 88; #21/#23 cùng dòng 76; #03/#25 cùng dòng 80) đều có hình ảnh mở đầu và kết luận khác biệt rõ — chấp nhận được.
- **D. Risk Flags nghiêm trọng nhất:** không Short nào lãng mạn hóa "duyên nợ" thành lý do ở lại quan hệ độc hại (ngược lại, #05/#09/#22/#24 chủ động bác bỏ điều này); không Short nào tuyên bố tính được cụ thể ai nợ ai từ kiếp nào (#14/#18 sau khi sửa đều là lời cảnh báo chống lại việc đó, không phải ví dụ); không phát hiện định mệnh luận.
- **E. Beat 6 risk-control (#05, #09, #22, #24):** cả 4 Short giữ nguyên câu neo "nghiệp duyên không bao giờ là lý do để ở lại một nơi gây hại cho bạn" theo đúng 4 góc khác nhau (an toàn-hành động / từ bi≠chịu đựng / lạm dụng ngôn ngữ dân gian / quyền hạn-thời lượng của duyên); không Short nào làm mềm hóa tinh thần này. Short #13 (vignette liên quan) và #30 (kiên nhẫn với người thân tự hại bản thân, KHÔNG phải người gây hại cho người xem) đều tự phân biệt rõ ranh giới với Beat 6, không lấn sang khuyên "chịu đựng."
- **C. Trung thực nguồn:** không phát hiện chi tiết/sự kiện bịa ngoài Long-form trong 30 Short.
- **F. Loop-close:** cả 30 Short đều có câu kết echo/trả lời hook; không phát hiện manufactured curiosity gap.
- **B. Hook self-sufficiency:** 29/30 Short đạt ngay từ bản gốc; #27 đã sửa (mục 3 ở trên).

## Vấn đề cần con người xem lại (không tự sửa)

- Không có vấn đề chặn xuất bản nào còn tồn đọng theo đánh giá của reviewer này. Tuy nhiên khuyến nghị: một người QA cuối (không phải AI) nên nghe thử bản đọc của #11, #14, #27 sau khi sửa để xác nhận nhịp đọc và cảm xúc vẫn tự nhiên, vì phần thân đã được viết lại khác bản duyệt gốc trong `SHORTS_BATCH_PLAN.md`.
- `SHORTS_BATCH_PLAN.md` mục "Kiểm tra chống trùng lặp" nên được cập nhật/bổ sung quy trình đối chiếu theo dòng-nguồn-dùng-chung (không chỉ theo hook image) cho các batch Shorts tương lai, vì đây là nguyên nhân khiến 2/3 lỗi trên lọt qua vòng tự-QA ban đầu.
