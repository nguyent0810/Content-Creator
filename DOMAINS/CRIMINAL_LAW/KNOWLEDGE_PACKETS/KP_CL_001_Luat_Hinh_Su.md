---
schema_version: 1.0
packet_id: KP_CL_001
domain_id: CL
asset_id: KP_CL_001
canonical_owner: DOMAINS/CRIMINAL_LAW
canonical_topic: Luật Hình Sự Việt Nam — Nền tảng cấu trúc, tố tụng, hình phạt, quyền của người bị buộc tội, và 13 nhóm tội danh phổ biến
vietnamese_display_name: Luật Hình Sự (Pillar 1 — Criminal Law Explainer)
english_working_title: Vietnamese Criminal Law — Foundational Explainer Knowledge
object_type: Knowledge Packet
status: draft-pending-human-review
version: 0.1
language: Tiếng Việt (chính), thuật ngữ Hán-Việt/điều luật giữ nguyên gốc
primary_legal_framework: Bộ luật Hình sự 2015 (số 100/2015/QH13, sửa đổi bổ sung 2017 — Luật số 12/2017/QH14) và Bộ luật Tố tụng Hình sự 2015 (số 101/2015/QH13), pháp luật nước Cộng hòa Xã hội Chủ nghĩa Việt Nam
risk_level: critical
risk_reasons:
  - Ranh giới suy đoán vô tội / legal-status precision — nguy cơ cao nhất toàn kênh nếu ngôn ngữ pháp lý bị dùng sai khi packet này sau này được tham chiếu cho nội dung có vụ án thật (Pillar 2-5)
  - No-legal-advice boundary — nguy cơ biến khung hình phạt tổng quát thành lời khuyên cho tình huống cụ thể của người xem
  - Độ tin cậy không đồng đều giữa khung pháp lý tổng thể (cao) và các khung hình phạt trung gian của từng tội danh cụ thể (trung bình, một số single-sourced)
  - Nguy cơ nhập nhằng khái niệm pháp lý ngoại lai (ví dụ "quyền im lặng" kiểu Miranda) vào hệ thống pháp luật Việt Nam
  - Ranh giới nạn nhân — các tội xâm phạm tình dục/tính mạng cần kỷ luật ẩn danh ngay ở tầng kiến thức nền, trước khi có nội dung vụ án thật nào tham chiếu ngược lại packet này
required_qa:
  - Domain QA (Hình Sự) — DOMAIN_QA/DOMAIN_QA_POLICY.md
  - Research QA (đối chiếu trực tiếp văn bản luật tại vbpl.vn/thuvienphapluat.vn cho các mục còn gắn cờ "cần xác minh thêm")
  - Safety QA (No Legal Advice Boundary, §7; Presumption of Innocence, §4)
  - Legal QA (nếu có luật sư/cố vấn pháp lý cộng tác trước khi phát hành)
  - Brand QA
dependencies:
  - DOMAINS/CRIMINAL_LAW/DOMAIN_GUIDE.md
  - DOMAINS/CRIMINAL_LAW/SOURCES/RESEARCH_DRAFT_LUAT_HINH_SU.md
  - DOMAINS/CRIMINAL_LAW/GLOSSARY/DOMAIN_GLOSSARY.md
  - DOMAINS/CRIMINAL_LAW/SOURCES/SOURCE_REGISTRY.md
  - CORE_OS/SHORTS_ENGINE.md (Myth-Bust mode, dùng cho cấu trúc Phần 6)
source_lineage: Tổng hợp từ 1 research draft nền tảng (RESEARCH_DRAFT_LUAT_HINH_SU.md, research date 2026-07-23). Độ tin cậy cao cho khung pháp lý tổng thể (cấu trúc BLHS, phân loại Điều 9, hệ thống hình phạt, quy trình tố tụng tổng quát, nguyên tắc suy đoán vô tội) — xác minh chéo ≥2-3 nguồn độc lập tùy mục (theo đúng số nguồn research draft tự ghi nhận cho từng mục cụ thể, không làm tròn lên thành một con số duy nhất). Độ tin cậy trung bình đến cao, không đồng đều theo từng mục, cho khung hình phạt chi tiết của 13 tội danh cụ thể — nhiều khung trung gian (khoản 3-5 của các điều luật dài) chỉ single-sourced trong lượt nghiên cứu này. **Chưa đối chiếu trực tiếp văn bản toàn văn tại vbpl.vn** — xem "Khoảng trống nguồn" bên dưới trước khi khóa bất kỳ số liệu cụ thể nào cho kịch bản.
confidence_level: mixed — xem nhãn độ tin cậy riêng ở từng mục trong Core Knowledge Map, đặc biệt Phần 5 (13 nhóm tội danh)
terminology: Xem GLOSSARY/DOMAIN_GLOSSARY.md (trạng thái active foundation) — packet này dùng đúng thuật ngữ đã chuẩn hóa ở đó (bị tình nghi, bị can, bị cáo, bản án có hiệu lực pháp luật, kháng cáo, kháng nghị, giám đốc thẩm, tái thẩm...) và không đề xuất thuật ngữ mới nào chưa có trong glossary
claims: Xem Core Knowledge Map — mỗi tuyên bố cụ thể được gắn nhãn độ tin cậy tại nguồn; không tuyên bố nào được nâng cấp thành "chắc chắn" nếu research draft gốc đã gắn cờ "cần xác minh thêm/gap"
cautions: Xem Risk-Specific Editorial Rules — đặc biệt Rule 1 (Legal-Status Precision), Rule 4 (No Legal Advice), Rule 6 (Foreign Legal Concept Import Ban)
QA_status: draft — chưa qua Domain QA / Research QA / Safety QA chính thức; KHÔNG dùng trực tiếp làm kịch bản sản xuất trước khi human review
review_cadence: Hàng năm, và bất kỳ khi nào có sửa đổi luật mới (đặc biệt điểm gap về hiệu lực 01/07/2025 liên quan Điều 251 — xem Khoảng trống nguồn), phát hiện nguồn mới, hoặc tiền lệ QA mới liên quan §4/§7/§8
---

# KP_CL_001 — Luật Hình Sự (Gói Tri Thức Nền Tảng cho Pillar 1)

## Packet Control

| Field | Value |
|---|---|
| Asset ID | KP_CL_001 |
| Domain | CL (Hình Sự — Luật Hình Sự, Án Có Thật & Tội Phạm Học) |
| Canonical Topic | Luật Hình Sự Việt Nam — cấu trúc BLHS 2015, tố tụng, hình phạt, quyền của người bị buộc tội, 13 nhóm tội danh phổ biến, 6 mythbust |
| Object Type | Knowledge Packet |
| Status | draft-pending-human-review |
| Version | 0.1 |
| Risk Level | **Critical** (một bậc trên `high` của FS/Tử Vi — domain rủi ro cao nhất kênh) |
| Dùng cho | Pillar 1 (Luật Hình Sự — Criminal Law Explainer) — mọi tập mùa sản xuất thuộc pillar này; các Pillar 2-5 tham chiếu ngược lại packet này khi cần mô tả quy trình/thuật ngữ tố tụng của một vụ án thật |
| Phụ thuộc | `DOMAIN_GUIDE.md` + `SOURCES/RESEARCH_DRAFT_LUAT_HINH_SU.md` (nguồn nghiên cứu duy nhất hiện có), `GLOSSARY/DOMAIN_GLOSSARY.md`, `SOURCE_REGISTRY.md` |
| Required QA | Domain QA (Hình Sự), Research QA, Safety QA, Legal QA, Brand QA — tất cả hiện chưa chạy chính thức trên packet này |
| Trạng thái | **Draft creative-knowledge asset — chưa qua QA chính thức.** Không dùng trực tiếp làm kịch bản công chiếu. |

**Lưu ý trạng thái quan trọng:** Đây là Knowledge Packet đầu tiên và duy nhất của domain Hình Sự tính đến thời điểm biên soạn, tổng hợp từ đúng 1 research draft nền tảng (`RESEARCH_DRAFT_LUAT_HINH_SU.md`, research date 2026-07-23). Bản thân research draft đó tự xác nhận: khung pháp lý tổng thể đạt độ tin cậy cao, nhưng nhiều khung hình phạt chi tiết của từng tội danh cụ thể (Phần 3 của research draft, tái hiện ở Phần 5 packet này) **chưa được đối chiếu trực tiếp với văn bản luật toàn văn** — mọi khoảng trống đó được giữ nguyên, không bị lấp bằng suy đoán, trong toàn bộ packet này. `DOMAIN_QA/DOMAIN_QA_POLICY.md` của domain này đã ở trạng thái `active`, nhưng packet này **chưa được chạy qua** checklist đó — packet là bước tổng hợp trung gian bắt buộc trước khi Pillar 1 có thể chuyển sang sản xuất kịch bản thật, đúng tinh thần `DOMAIN_MANIFEST.md`: Knowledge Packets phải qua "nghiên cứu và đối chiếu chéo" trước khi mở khóa production.

---

# Identity

## Canonical Name

Luật Hình Sự (Bộ luật Hình sự 2015, sửa đổi bổ sung 2017) và Bộ luật Tố tụng Hình sự 2015 — hệ thống pháp luật hình sự nước Cộng hòa Xã hội Chủ nghĩa Việt Nam.

## Alternative Names / Related References

- BLHS 2015 (Bộ luật Hình sự số 100/2015/QH13)
- Luật số 12/2017/QH14 (luật sửa đổi, bổ sung BLHS 2015)
- BLTTHS 2015 (Bộ luật Tố tụng Hình sự số 101/2015/QH13)
- "Criminal Code" / "Criminal Procedure Code" (tên gọi tiếng Anh phổ biến khi so sánh liên hệ thống — chỉ dùng khi đã nêu rõ đây là hệ thống civil-law Việt Nam, không suy diễn tương đương common-law)

## Related Terms

Bị tình nghi, bị can, bị cáo, bị hại, người bị buộc tội, khởi tố, truy tố, cáo trạng, kết luận điều tra, xét xử sơ thẩm, xét xử phúc thẩm, bản án có hiệu lực pháp luật, kháng cáo, kháng nghị, giám đốc thẩm, tái thẩm, Cơ quan Điều tra (CQĐT), Viện Kiểm sát Nhân dân (VKSND), Tòa án Nhân dân (TAND), án treo, tù có thời hạn, tù chung thân, tử hình, tình tiết tăng nặng/giảm nhẹ, phòng vệ chính đáng, nguyên tắc suy đoán vô tội.

## Keywords

Bộ luật Hình sự, Bộ luật Tố tụng Hình sự, Điều 9, phân loại tội phạm, tuổi chịu trách nhiệm hình sự, hệ thống hình phạt, án treo, tù chung thân, tử hình, phòng vệ chính đáng, quy trình tố tụng, khởi tố, truy tố, xét xử, kháng cáo, giám đốc thẩm, tái thẩm, suy đoán vô tội, quyền bào chữa, giết người, cố ý gây thương tích, hiếp dâm, cướp tài sản, bắt cóc, trộm cắp, lừa đảo, lạm dụng tín nhiệm, ma túy, rửa tiền, tham ô, nhận hối lộ, vi phạm giao thông đường bộ.

---

# Scope & Jurisdiction (recap có chủ đích từ `DOMAIN_GUIDE.md` §2)

Toàn bộ packet này nói về pháp luật hình sự của **nước Cộng hòa Xã hội Chủ nghĩa Việt Nam**, cụ thể là BLHS 2015 (sửa đổi 2017) và BLTTHS 2015 — không phải luật hình sự của bất kỳ quốc gia nào khác. Đây là hệ thống **civil-law** (luật thành văn, không có tiền lệ án ràng buộc theo nghĩa common-law) — packet này chủ động không mượn khái niệm ngoại lai (ví dụ "pleading the fifth," "grand jury," "Miranda rights") để mô tả hệ thống Việt Nam; nơi có khái niệm tương đồng thật sự (ví dụ nguyên tắc suy đoán vô tội), packet nêu rõ điểm tương đồng và khác biệt thay vì đồng nhất hai hệ thống (xem Mythbust 6.4). Mọi nội dung phái sinh từ packet này cho Pillar 2-5 (án có thật ở nước khác) phải tự nêu rõ jurisdiction riêng của vụ án đó — packet này không tự động áp dụng cho case ngoài Việt Nam.

---

# Canonical Sources

## Nguồn nghiên cứu đầu vào (Primary Research Input)

| Source | Mô tả | Tier / Độ tin cậy | Hướng dẫn sử dụng |
|---|---|---|---|
| `SOURCES/RESEARCH_DRAFT_LUAT_HINH_SU.md` | Toàn bộ nền tảng: cấu trúc BLHS, phân loại tội phạm, hệ thống hình phạt, quy trình tố tụng, quyền người bị buộc tội, 13 tội danh phổ biến, 6 hiểu lầm mythbust | Tier 1 cho khung pháp lý tổng thể (cấu trúc luật, Điều 9, quy trình tố tụng, nguyên tắc suy đoán vô tội — xác minh ≥3 nguồn độc lập; riêng hệ thống hình phạt/Điều 65/39/40 ở mục 1.5 research draft tự ghi nhận ≥2 nguồn độc lập mỗi điểm, không phải ≥3 — giữ đúng mức này); Tier 3-tương-đương (bình luận/diễn giải pháp luật, chưa đọc trực tiếp văn bản gốc vbpl.vn) cho phần lớn khung hình phạt chi tiết từng tội danh | Nguồn duy nhất và trực tiếp cho toàn bộ packet này; mọi nhãn độ tin cậy trong packet kế thừa nguyên trạng từ research draft, không nâng cấp |

## Source Priority Hierarchy (tái hiện từ `DOMAIN_GUIDE.md` §3)

| Tier | Loại nguồn | Áp dụng trong packet này |
|---|---|---|
| 1 | Văn bản luật gốc (vbpl.vn) | **Chưa được truy cập trực tiếp** trong research draft nền — đây là khoảng trống lớn nhất của toàn packet, xem bên dưới |
| 2 | Trang chính quyền/tư pháp phổ biến pháp luật chính thức (công an tỉnh, VKSNDTC, Tạp chí TAND, Ban Nội chính TW, Bộ Tư pháp) | Nguồn chính cho phần lớn khung pháp lý tổng thể — độ tin cậy cao khi ≥2-3 nguồn khớp nhau |
| 3-4 | Trang luật thương mại (thuvienphapluat.vn, luatminhkhue.vn, luatvietnam.vn, lsvn.vn...) | Dùng cross-check, không dùng làm nguồn duy nhất — đúng như research draft đã áp dụng |
| 5 | Wikipedia tiếng Việt | Chỉ dùng định hướng/cross-check tổng quan (ví dụ số chương/điều BLHS) |

## Khoảng trống nguồn (Known Gaps — kế thừa nguyên trạng từ research draft, KHÔNG được lấp bằng suy đoán)

Mỗi mục dưới đây giữ nguyên mức độ tin cậy và cách diễn đạt "cần xác minh thêm" của tài liệu nghiên cứu gốc — không mục nào được nâng cấp thành sự thật chắc chắn trong packet này:

1. **Chưa đối chiếu trực tiếp văn bản toàn văn BLHS/BLTTHS tại vbpl.vn** cho bất kỳ điều luật nào — toàn bộ packet dựa trên đối chiếu ≥2-3 nguồn thứ cấp độc lập, không phải đọc trực tiếp Tier 1.
2. **Danh sách đầy đủ, chính xác từng số điều liệt kê trong Điều 12 khoản 2** (tội danh mà người 14-16 tuổi phải chịu trách nhiệm hình sự) — chỉ xác nhận qua một lượt tìm kiếm tổng hợp, cần đối chiếu lại trước khi khẳng định "tội X áp dụng/không áp dụng cho người 14-16 tuổi."
3. **Thời hạn 20 ngày cho xác minh nguồn tin ban đầu** (trước khi khởi tố) — chỉ một nguồn xác nhận, chưa đối chiếu chéo độc lập lần hai; thời hạn tố tụng thực tế còn có nhiều mức tùy vụ việc thông thường/phức tạp/đặc biệt phức tạp.
4. **Số điều chính xác cho quyền không tự buộc tội** (dẫn là Điều 60/61 BLTTHS) — tổng hợp từ một nguồn duy nhất, cần xác minh lại số khoản/điều chính xác.
5. **Thời hạn kháng cáo (15 ngày)/kháng nghị (15-30 ngày)** — số liệu phổ biến, nhất quán giữa các nguồn được tra cứu, nhưng toàn bộ khối thông tin đến từ một cụm kết quả tìm kiếm chưa đối chiếu với việc đọc trực tiếp Điều 333/337.
6. **Điều 141 — chi tiết khung "05-10 năm cho bị hại 16-18 tuổi"** mà một nguồn nêu: có thứ tự không khớp logic tăng dần thông thường của khung hình phạt luật hình sự Việt Nam (khung sau thường nặng hơn khung trước) — nhiều khả năng là lỗi tổng hợp của nguồn. **Không dùng chi tiết này cho đến khi xác minh lại trực tiếp văn bản luật.**
7. **Điều 251 (ma túy) — mốc hiệu lực 01/07/2025**: chưa xác minh được đây là một đợt sửa đổi luật thật (ngoài phạm vi "sửa đổi 2017" mà packet giả định) hay chỉ là ngày hiệu lực của một văn bản hướng dẫn thi hành riêng. **Gap cần đóng bắt buộc trước khi khóa nội dung bất kỳ tập nào về chủ đề ma túy sản xuất/phát hành sau mốc này.**
8. **Các khung hình phạt trung gian (khoản 3-5) của Điều 168 (cướp tài sản), Điều 134 (cố ý gây thương tích, đặc biệt mức tỷ lệ thương tật 61%+), Điều 169 (bắt cóc nhằm chiếm đoạt tài sản), Điều 175 (lạm dụng tín nhiệm, khung 3-4)** — độ tin cậy thấp/trung bình, chưa xác minh đủ số liệu từng khoản; chỉ khung thấp nhất và/hoặc khung cao nhất của mỗi điều này đạt độ tin cậy cao.
9. **Cơ chế chuyển tử hình thành tù chung thân theo quyết định Chủ tịch nước** — chưa được nghiên cứu sâu, cần một lượt nghiên cứu riêng.
10. **Một mâu thuẫn số học nhỏ** giữa các nguồn tổng hợp về số điều của riêng Phần thứ hai BLHS — nhiều khả năng là lỗi tính toán của trang tổng hợp thứ cấp, không phải mâu thuẫn thật về ranh giới điều luật (mọi nguồn đều thống nhất Phần 1 kết thúc ở Điều 122, Phần 2 bắt đầu Điều 123). Không dùng con số tổng số điều của riêng Phần 2 làm dữ kiện cứng.

**Khuyến nghị hành động bắt buộc trước khi khóa bất kỳ kịch bản nào trích dẫn số điều/khung hình phạt cụ thể:** tải và đối chiếu trực tiếp văn bản hợp nhất tại vbpl.vn hoặc thuvienphapluat.vn (bản toàn văn còn hiệu lực), kiểm tra Nghị quyết hướng dẫn của Hội đồng Thẩm phán TANDTC liên quan (đặc biệt Điều 65 về án treo, đã ghi nhận có Nghị quyết hướng dẫn riêng).

---

# Core Knowledge Map

Sáu khối kiến thức dưới đây bao phủ toàn bộ nền tảng Pillar 1. Mỗi khối theo cấu trúc 5 phần: Knowledge function / Primary concepts / Narrative detail / Script-ready material / Production cautions — mô phỏng đúng định dạng đã dùng ở `KP_FS_001`.

## 1. Cấu trúc Bộ luật Hình sự 2015 và phân loại tội phạm theo mức độ nghiêm trọng (Điều 9)

### Knowledge function

Đây là "bảng chữ cái chung" của toàn bộ Pillar 1 — mọi tập giải thích một tội danh cụ thể (Phần 5) đều cần định vị tội đó vào 1 trong 4 mức độ nghiêm trọng của Điều 9 trước khi nói đến khung hình phạt, và mọi tập về tố tụng/hình phạt (Phần 2-3) đều giả định khán giả đã hiểu khung phân loại này. Đây cũng là điểm khởi đầu an toàn nhất để mở một chuỗi nội dung Pillar 1 vì đây là dữ kiện cứng, độ tin cậy cao, không có tranh cãi liên nguồn.

### Primary concepts

- BLHS 2015 gồm 3 phần, 26 chương, 426 điều: Phần 1 — Những quy định chung (Điều 1-122); Phần 2 — Các tội phạm (Điều 123-425); Phần 3 — Điều khoản thi hành (Điều 426).
- Điều 9 phân loại tội phạm thành 4 loại theo **mức cao nhất của khung hình phạt luật quy định** (không phải mức tòa thực tế tuyên):
  | Loại tội phạm | Mức cao nhất của khung hình phạt |
  |---|---|
  | Ít nghiêm trọng | Phạt tiền, cải tạo không giam giữ, hoặc tù đến 03 năm |
  | Nghiêm trọng | Tù trên 03 năm đến 07 năm |
  | Rất nghiêm trọng | Tù trên 07 năm đến 15 năm |
  | Đặc biệt nghiêm trọng | Tù trên 15 năm đến 20 năm, tù chung thân, hoặc tử hình |
- Tuổi chịu trách nhiệm hình sự (Điều 12): từ đủ 16 tuổi — chịu trách nhiệm về mọi tội phạm; từ đủ 14 đến dưới 16 tuổi — chỉ chịu trách nhiệm về tội rất nghiêm trọng/đặc biệt nghiêm trọng, giới hạn trong danh sách điều luật cụ thể (danh sách đầy đủ: **gap, xem Khoảng trống nguồn mục 2**).
- Tình tiết giảm nhẹ (Điều 51) và tăng nặng (Điều 52) — hai danh sách riêng biệt Tòa án cân nhắc khi quyết định hình phạt trong phạm vi khung; danh sách Điều 52 là **danh sách đóng, không được suy diễn thêm**. Quy tắc quan trọng: một tình tiết đã là yếu tố định tội/định khung của chính điều luật đó thì không được tính thêm một lần nữa theo Điều 52.

### Narrative detail

BLHS 2015 tổ chức luật hình sự Việt Nam thành ba khối lớn: quy định chung áp dụng cho mọi tội phạm (định nghĩa tội phạm, tuổi chịu trách nhiệm, các giai đoạn phạm tội, đồng phạm, hệ thống hình phạt...), danh mục từng tội danh cụ thể theo nhóm khách thể bị xâm phạm (tính mạng/sức khỏe, sở hữu, ma túy, chức vụ/tham nhũng, an toàn công cộng...), và một điều khoản thi hành ngắn gọn. Điều 9 là bản lề nối hai phần đầu: nó không tự nó định nghĩa một tội cụ thể nào, mà cung cấp một thước đo chung — nhìn vào khung hình phạt cao nhất mà điều luật quy định cho một tội, ta biết ngay tội đó thuộc mức nào trong 4 mức. Thước đo này chi phối nhiều hệ quả pháp lý khác đi kèm (ai phải có luật sư bào chữa bắt buộc, ai đủ tuổi chịu trách nhiệm hình sự, thời hiệu truy cứu...) — nó là một khớp nối cấu trúc, không phải một chi tiết rời rạc.

### Script-ready material

- Hình ảnh "thước đo 4 bậc" (ít nghiêm trọng → nghiêm trọng → rất nghiêm trọng → đặc biệt nghiêm trọng) — dễ trực quan hóa bằng đồ họa dạng thang đo.
- Câu hỏi mở tập: "Cùng là 'phạm tội', nhưng luật phân biệt một người trộm chiếc điện thoại với một vụ giết người như thế nào? Câu trả lời nằm ở khung hình phạt cao nhất luật quy định — không phải ở cảm giác nghiêm trọng của bạn."
- Cấu trúc 3 phần BLHS làm khung sườn tự nhiên cho một tập "tổng quan luật hình sự Việt Nam trong X phút."

### Production cautions

- **Domain Guide §7 (No Legal Advice):** Điều 9 và khung phân loại là kiến thức giáo dục về cách luật *phân loại* tội phạm nói chung — không được dùng để kết luận thay khán giả "hành vi của bạn/người quen thuộc mức nào" trong một tình huống cụ thể.
- Không dùng con số tổng số điều của riêng Phần 2 (425−123+1) làm dữ kiện cứng phát ngôn chắc nịch — một nguồn tổng hợp cho ra số không khớp phép trừ đơn giản, nhiều khả năng là lỗi thứ cấp; nếu cần nêu, dùng "khoảng 300 điều luật cụ thể" hoặc kiểm tra lại trực tiếp trước khi nêu số chính xác.
- Danh sách điều luật cụ thể ở Điều 12 khoản 2 (14-16 tuổi): **chưa đầy đủ/chưa xác minh** — không liệt kê như danh sách đóng, chắc chắn trong kịch bản trước khi đối chiếu lại văn bản hiện hành.
- Danh sách ví dụ tình tiết tăng nặng/giảm nhẹ (Điều 51/52) trong packet này là ví dụ đại diện, không phải liệt kê đầy đủ — không trình bày như danh sách toàn văn.

## 2. Quy trình tố tụng hình sự (từ tin báo tố giác đến thi hành án)

### Knowledge function

Đây là "cốt truyện tố tụng" nền — bất kỳ tập nào (Pillar 1 lẫn Pillar 2-5 khi cần mô tả một vụ án thật) muốn nói "vụ án đang ở giai đoạn nào" đều cần khung 8 bước này để định vị chính xác, đặc biệt để phân biệt "bản án sơ thẩm" với "bản án có hiệu lực pháp luật" — ranh giới ngôn ngữ pháp lý quan trọng nhất của toàn domain (`DOMAIN_GUIDE.md` §4).

### Primary concepts

- 8 giai đoạn tổng quát: (1) nguồn tin về tội phạm (tố giác, tin báo, kiến nghị khởi tố, tự thú) → (2) xác minh & khởi tố (Điều 143; thời hạn phổ biến ghi nhận **20 ngày** — single-sourced, cần xác minh thêm) → (3) điều tra (CQĐT thu thập chứng cứ, ra kết luận điều tra) → (4) truy tố (VKSND ra cáo trạng hoặc trả hồ sơ/đình chỉ) → (5) xét xử sơ thẩm (TAND, ra bản án sơ thẩm — **chưa có hiệu lực pháp luật ngay**) → (6) kháng cáo/kháng nghị & xét xử phúc thẩm (nếu có; nếu không ai kháng cáo/kháng nghị đúng hạn, bản án sơ thẩm trở thành bản án có hiệu lực pháp luật) → (7) thi hành án (sau khi bản án có hiệu lực) → (8) thủ tục xét lại đặc biệt: giám đốc thẩm/tái thẩm (áp dụng ngay cả với bản án **đã** có hiệu lực, không phải một "cấp xét xử" thứ ba thông thường).
- Ba cơ quan tiến hành tố tụng chính: CQĐT (tiếp nhận, xác minh, khởi tố, điều tra), VKSND (thực hành quyền công tố + kiểm sát hoạt động tư pháp xuyên suốt), TAND (cơ quan duy nhất có quyền xét xử, mô hình hai cấp xét xử sơ thẩm/phúc thẩm).
- Thời hạn kháng cáo (bị cáo/đương sự): 15 ngày kể từ ngày tuyên án (hoặc từ ngày nhận/niêm yết bản án nếu vắng mặt). Thời hạn kháng nghị (VKS): 15 ngày (cùng cấp) hoặc 30 ngày (cấp trên trực tiếp) đối với bản án; 07/15 ngày đối với quyết định. *Độ tin cậy trung bình-cao — single cluster nguồn, chưa đối chiếu trực tiếp Điều 333/337.*

### Narrative detail

Một vụ án hình sự Việt Nam không "bắt đầu" ở phiên tòa — nó bắt đầu từ một nguồn tin: một lời tố giác, một tin báo, hoặc chính cơ quan có thẩm quyền phát hiện. CQĐT có một khoảng thời gian luật định để xác minh xem có dấu hiệu tội phạm hay không trước khi được phép ra quyết định khởi tố — khởi tố không phải là kết luận có tội, mà là mở ra một cuộc điều tra chính thức. Nếu điều tra đủ căn cứ, hồ sơ chuyển sang VKSND để quyết định truy tố bằng cáo trạng — đây là thời điểm một "bị can" (người bị khởi tố) trở thành "bị cáo" (người sẽ ra tòa). Bản án sơ thẩm của TAND là lần tuyên án đầu tiên, nhưng luật cho một khoảng thời gian (15 ngày) để các bên kháng cáo hoặc VKS kháng nghị — nếu không ai làm vậy đúng hạn, bản án sơ thẩm "chín" thành bản án có hiệu lực pháp luật; nếu có, vụ án được xét xử lại ở cấp phúc thẩm. Ngay cả sau khi đã có hiệu lực, một bản án vẫn có thể bị mở lại qua hai thủ tục đặc biệt — giám đốc thẩm (khi phát hiện vi phạm tố tụng nghiêm trọng) hoặc tái thẩm (khi có tình tiết mới) — nhưng đây là ngoại lệ hiếm, không phải quy trình thường xuyên. Ba cơ quan CQĐT/VKSND/TAND không thay thế nhau: VKSND đặc biệt có vai trò kép — vừa buộc tội (công tố) vừa giám sát tính hợp pháp của chính quá trình tố tụng, xuyên suốt từ đầu đến cuối, không chỉ ở giai đoạn truy tố.

### Script-ready material

- Sơ đồ dòng chảy 8 bước (timeline ngang) — cấu trúc tự nhiên cho một tập "một vụ án đi qua bao nhiêu cửa trước khi có bản án cuối cùng?"
- Điểm "twist" giáo dục mạnh: nhiều khán giả tưởng bản án sơ thẩm là chung cuộc — tập có thể dùng chính hiểu lầm này làm hook mở đầu (xem Mythbust 6.6, liên kết trực tiếp).
- Phép ẩn dụ vai trò 3 cơ quan: CQĐT "đi tìm sự thật", VKSND "đại diện Nhà nước buộc tội, đồng thời giám sát cả sân chơi", TAND "trọng tài duy nhất có quyền phán quyết".

### Production cautions

- **Domain Guide §4 (ranh giới cốt lõi):** một người mới có bản án sơ thẩm kết tội, chưa hết hạn kháng cáo, hoặc đang trong giai đoạn điều tra/truy tố, **phải luôn được gọi bằng đúng thuật ngữ giai đoạn** (bị tình nghi/bị can/bị cáo) — không gọi "tội phạm," "kẻ giết người," hay bất kỳ danh từ khẳng định tội nào, kể cả khi tập chỉ đang giải thích quy trình chung, không nói về vụ án thật nào. Giữ kỷ luật ngôn ngữ này ngay ở tầng kiến thức nền để không lây lan lỗi sang Pillar 2-5 sau này.
- Con số 20 ngày (xác minh nguồn tin) và 15/30 ngày (kháng cáo/kháng nghị): single-sourced/chưa đối chiếu chéo độc lập — nêu kèm ngôn ngữ "theo quy định phổ biến được ghi nhận" thay vì khẳng định tuyệt đối, và không dùng làm căn cứ tính "còn bao nhiêu ngày" cho một vụ án cụ thể của khán giả (§7).
- Giám đốc thẩm/tái thẩm: không trình bày như "cấp xét xử thứ ba" mà ai cũng có thể yêu cầu tùy ý — đây là thủ tục đặc biệt, hiếm, có điều kiện pháp lý cụ thể.
- Domain Guide §7: mọi mô tả quy trình phải giữ khung "đây là luật quy định chung như thế nào" — không kết luận thay khán giả "trường hợp của bạn/người quen đang ở giai đoạn nào, nên làm gì tiếp theo."

## 3. Hệ thống hình phạt (án treo, tù có thời hạn, tù chung thân, tử hình) và miễn/giảm

### Knowledge function

Đây là khối kiến thức có mật độ hiểu lầm công chúng cao nhất trong toàn bộ Pillar 1 (đặc biệt án treo, xem Mythbust 6.2) — cần trình bày chính xác về bản chất pháp lý của từng loại trước khi bất kỳ tập nào dùng các từ này để mô tả một bản án thật.

### Primary concepts

- 7 hình phạt chính theo Điều 32 (mỗi người chỉ chịu 1 hình phạt chính/tội, nhẹ→nặng): cảnh cáo, phạt tiền, cải tạo không giam giữ, trục xuất (khi là hình phạt chính), tù có thời hạn, tù chung thân, tử hình. Hình phạt bổ sung (có thể áp dụng kèm): cấm đảm nhiệm chức vụ/hành nghề, cấm cư trú, quản chế, tước quyền công dân, tịch thu tài sản, phạt tiền/trục xuất (khi không phải hình phạt chính).
- **Án treo (Điều 65):** **không phải một loại hình phạt riêng** trong 7 hình phạt chính — về bản chất là **biện pháp miễn chấp hành hình phạt tù có điều kiện**, áp dụng khi mức án tù tuyên ≤ 03 năm, có ≥2 tình tiết giảm nhẹ (≥1 thuộc khoản 1 Điều 51), không có tình tiết tăng nặng, và Tòa xét thấy không cần buộc chấp hành tù. Thời gian thử thách: 01-05 năm. Người hưởng án treo **vẫn là người đã bị kết án tù, vẫn có án tích**.
- **Tù chung thân (Điều 39):** tù không thời hạn, cho tội đặc biệt nghiêm trọng chưa đến mức tử hình; không áp dụng cho người dưới 18 tuổi tại thời điểm phạm tội. Có thể được xét giảm xuống 30 năm (lần đầu) nếu cải tạo tốt, nhưng **thời gian thực tế phải chấp hành tối thiểu vẫn là 20 năm** dù được giảm nhiều lần.
- **Tử hình (Điều 40):** chỉ áp dụng cho tội đặc biệt nghiêm trọng thuộc nhóm an ninh quốc gia, tính mạng con người, ma túy, tham nhũng và một số tội khác luật quy định cụ thể. **Không áp dụng với:** người dưới 18 tuổi khi phạm tội; phụ nữ có thai/đang nuôi con dưới 36 tháng tuổi (khi phạm tội hoặc khi xét xử); người đủ 75 tuổi trở lên (khi phạm tội hoặc khi xét xử). Cơ chế chuyển tử hình thành chung thân qua quyết định Chủ tịch nước: **chưa xác minh sâu, gap còn tồn đọng.**
- **Phòng vệ chính đáng (Điều 22):** không phải hình phạt, mà là trường hợp loại trừ trách nhiệm hình sự — hành vi chống trả cần thiết trước một hành vi xâm phạm thì không phải tội phạm; nếu "vượt quá giới hạn cần thiết" thì vẫn có thể chịu trách nhiệm hình sự (thường nhẹ hơn), theo đánh giá từng vụ việc của tòa án, không có công thức cố định.

### Narrative detail

Hệ thống hình phạt Việt Nam xếp theo một thang từ nhẹ đến nặng, và mỗi người chỉ nhận đúng một hình phạt chính cho một tội — không cộng dồn nhiều loại hình phạt chính cùng lúc, dù có thể kèm thêm các hình phạt bổ sung. Điểm dễ gây hiểu lầm nhất trong toàn hệ thống là án treo: nó không nằm trong danh sách 7 hình phạt chính vì bản chất của nó không phải là "phạt" theo nghĩa một mức án riêng, mà là một cơ chế khoan hồng có điều kiện áp lên một bản án tù đã tuyên — tòa vẫn tuyên người đó có tội và có một mức án tù cụ thể, chỉ là cho phép họ không phải vào trại giam ngay, với điều kiện giữ hạnh kiểm tốt trong thời gian thử thách. Ở đầu kia của thang hình phạt, tù chung thân và tử hình đều có những giới hạn về đối tượng áp dụng mà luật đặt ra vì lý do nhân đạo (tuổi, tình trạng thai sản) — đây là những ranh giới cứng, không phải quyết định tùy nghi của từng vụ. Riêng phòng vệ chính đáng đứng ở một vị trí khác hẳn trong hệ thống: nó không phải là một mức hình phạt nhẹ hơn, mà là sự loại trừ hoàn toàn trách nhiệm hình sự — nhưng ranh giới "cần thiết" và "vượt quá cần thiết" của nó luôn phụ thuộc đánh giá cụ thể từng vụ việc, không phải một công thức số học người xem có thể tự áp dụng.

### Script-ready material

- Thang bậc hình ảnh "cảnh cáo → phạt tiền → cải tạo không giam giữ → trục xuất → tù có thời hạn → tù chung thân → tử hình" — đồ họa dạng bậc thang, dùng xuyên suốt các tập về hình phạt.
- Hook mở đầu mạnh cho tập về án treo: "Một người 'được hưởng án treo' có phải là người vô tội không? Câu trả lời có thể khiến bạn bất ngờ." (nối trực tiếp Mythbust 6.2)
- Đối lập rõ ràng "tù chung thân = không thời hạn, nhưng vẫn có sàn tối thiểu 20 năm thực tế" — điểm số liệu cụ thể, dễ nhớ, tạo giá trị thông tin cao cho khán giả.
- Ranh giới nhân đạo của tử hình (tuổi, thai sản) — chất liệu cho một đoạn giải thích "luật hình sự Việt Nam có những giới hạn nhân đạo nào?"

### Production cautions

- **Domain Guide §10 (Layered Framework):** khi nêu án tử hình/án treo như một hình phạt đã tuyên trong một vụ việc, chỉ trình bày sự kiện đã tuyên, không bình luận về công lý/bất công của mức án đó ở lớp legal/procedural — phê phán hệ thống (nếu có) chỉ thuộc lớp societal-reflective, phải gắn nhãn rõ.
- **Domain Guide §7:** không dùng khung hình phạt để dự đoán "nếu bạn/người quen làm X thì sẽ bị án treo hay đi tù thật" — đây là quyết định của tòa án dựa trên toàn bộ tình tiết vụ việc cụ thể, không phải công thức người xem tự áp dụng được.
- Phòng vệ chính đáng: **không** trình bày ranh giới "vượt quá giới hạn" như một quy tắc rõ ràng, áp dụng máy móc — đây chính là nội dung Mythbust 6.1, phải giữ nguyên tính không-công-thức của nó.
- Cơ chế chuyển tử hình → chung thân qua Chủ tịch nước: chưa xác minh sâu — không mô tả chi tiết quy trình này như thể đã nắm rõ; chỉ nêu "một số trường hợp tử hình có thể được chuyển thành tù chung thân theo quyết định của Chủ tịch nước" và dừng ở đó cho đến khi có nghiên cứu bổ sung.
- Mọi mô tả án treo/tù chung thân/tử hình liên quan một vụ án thật (Pillar 2-5) phải tuân thủ đồng thời `DOMAIN_GUIDE.md` §4 — không gọi người có án treo/tù là "đã thoát tội" hay dùng ngôn ngữ ngụ ý gì khác ngoài sự kiện pháp lý đã tuyên.

## 4. Quyền của bị can/bị cáo và nguyên tắc suy đoán vô tội

### Knowledge function

Đây là khối kiến thức nối trực tiếp với ranh giới an toàn quan trọng nhất của toàn domain (`DOMAIN_GUIDE.md` §4) — nếu khán giả hiểu đúng nguyên tắc suy đoán vô tội và quyền bào chữa, họ sẽ tự nhiên hiểu vì sao kênh luôn dùng "bị can/bị cáo" thay vì "tội phạm" cho người chưa bị kết án cuối cùng. Đây cũng là điểm dễ bị nhầm với khái niệm pháp lý Mỹ nhất (xem Mythbust 6.4).

### Primary concepts

- "Người bị buộc tội" (Điều 4 BLTTHS) là khái niệm bao trùm: người bị bắt, người bị tạm giữ, bị can, bị cáo.
- **Nguyên tắc suy đoán vô tội (Điều 13 BLTTHS):** "Người bị buộc tội được coi là không có tội cho đến khi được chứng minh theo trình tự, thủ tục do Bộ luật này quy định và có bản án kết tội của Tòa án đã có hiệu lực pháp luật." Khi không đủ và không thể làm sáng tỏ căn cứ buộc tội đúng trình tự luật định, cơ quan có thẩm quyền phải kết luận người bị buộc tội **không có tội**.
- **Quyền bào chữa (Điều 16):** tự bào chữa, nhờ luật sư, hoặc nhờ người khác bào chữa; mở rộng diện **bắt buộc phải có người bào chữa** (kể cả khi không tự mời) cho các trường hợp khung hình phạt cao nhất là 20 năm/chung thân/tử hình, và một số trường hợp khác (người chưa thành niên, người có nhược điểm thể chất/tâm thần).
- **Quyền gặp riêng người bào chữa (Điều 73):** bất kỳ giai đoạn tố tụng nào, không giới hạn số lần/thời gian, được gặp riêng không có người tiến hành tố tụng hiện diện.
- **Quyền trình bày lời khai/không bị ép buộc nhận tội** (dẫn Điều 60, 61 BLTTHS — **số điều cần xác minh lại, single-sourced**): quyền được biết lý do bị buộc tội, được giải thích quyền/nghĩa vụ, đưa ra chứng cứ/yêu cầu, đề nghị thay đổi người tiến hành tố tụng, nói lời sau cùng trước khi nghị án.
- **Không có khái niệm "Miranda rights" hay "quyền im lặng" đúng tên gọi common-law trong luật Việt Nam** — điểm tương đồng gần nhất có căn cứ pháp lý thật là tổ hợp: nguyên tắc suy đoán vô tội (Điều 13) + quyền trình bày lời khai như một quyền, không phải nghĩa vụ (Điều 60/61) + nguyên tắc trách nhiệm chứng minh tội phạm thuộc cơ quan tiến hành tố tụng.

### Narrative detail

Luật tố tụng hình sự Việt Nam gom nhiều vị trí pháp lý khác nhau (người bị bắt, bị tạm giữ, bị can, bị cáo) dưới một khái niệm chung — "người bị buộc tội" — để áp một bộ quyền nền tảng chung cho tất cả, bất kể họ đang ở giai đoạn nào của vụ án. Trung tâm của bộ quyền đó là nguyên tắc suy đoán vô tội, lần đầu được ghi nhận minh thị ở cấp độ này trong pháp luật tố tụng hình sự Việt Nam: gánh nặng chứng minh luôn thuộc về cơ quan tiến hành tố tụng, không phải người bị buộc tội phải chứng minh mình vô tội. Đi kèm nguyên tắc đó là một chuỗi quyền cụ thể: quyền có luật sư (và với những tội có khung hình phạt cao nhất đặc biệt nghiêm trọng, luật còn bắt buộc phải có người bào chữa dù đương sự không tự mời), quyền được gặp riêng luật sư ở bất kỳ giai đoạn nào, và quyền trình bày lời khai như một lựa chọn chứ không phải nghĩa vụ tự buộc tội mình. Một điểm biên tập quan trọng: hệ thống này không có một điều khoản mang tên "quyền im lặng" hay một nghi thức đọc cảnh báo kiểu Miranda khi bắt giữ như ở Mỹ/Anh — nó là một hệ thống civil-law khác về cấu trúc, và điểm tương đồng gần nhất là sự kết hợp của nguyên tắc suy đoán vô tội với quyền không bị ép cung, không phải một bản dịch trực tiếp của khái niệm Mỹ.

### Script-ready material

- Trích gần nguyên văn Điều 13 BLTTHS ("Người bị buộc tội được coi là không có tội cho đến khi...") — một câu quote mạnh, dễ dùng làm điểm nhấn (voice-over) cho bất kỳ tập nào về quyền của bị can/bị cáo.
- Đối lập giáo dục: "Việt Nam không có 'đọc quyền Miranda' như phim Mỹ — nhưng có một nguyên tắc còn nền tảng hơn: gánh nặng chứng minh luôn thuộc về nhà nước, không phải bạn."
- Chuỗi 4 vị trí pháp lý (bị bắt → bị tạm giữ → bị can → bị cáo) minh họa bằng một dòng thời gian đơn giản, giúp khán giả tự định vị chính xác thuật ngữ mỗi khi nghe tin tức thời sự.

### Production cautions

- **Domain Guide §2:** tuyệt đối không nói hoặc viết "Việt Nam có quyền im lặng giống Mỹ" hay dùng nguyên xi "Miranda rights" cho hệ thống Việt Nam — đây chính là lỗi khái niệm ngoại lai bị cấm minh thị; xem Mythbust 6.4 để có công thức trình bày đúng.
- Số điều chính xác cho quyền không tự buộc tội (Điều 60/61): single-sourced, cần xác minh lại trước khi trích dẫn số điều cụ thể trong kịch bản có tính khẳng định.
- **Domain Guide §4/§7:** giải thích nguyên tắc suy đoán vô tội là nội dung giáo dục về *cách luật vận hành nói chung* — không dùng để bình luận/kết luận thay về mức độ vô tội/có tội của một bị can/bị cáo cụ thể trong một vụ án thật khi packet này được Pillar 2-5 tham chiếu ngược lại sau này.

## 5. Tổng quan 13 nhóm tội danh phổ biến được nghiên cứu

### Knowledge function

Đây là nội dung có sức hút công chúng cao nhất của Pillar 1 — "tội X bị xử lý thế nào theo luật" là câu hỏi tự nhiên khán giả tìm kiếm. Đồng thời đây là khối rủi ro cao nhất về No-Legal-Advice Boundary (`DOMAIN_GUIDE.md` §7): mọi con số dưới đây phải được trình bày như khung hình phạt **chung, điển hình theo luật**, không phải một dự đoán hay tư vấn cho bất kỳ tình huống cụ thể nào.

**Cảnh báo bắt buộc đọc trước khi dùng bảng dưới đây (kế thừa nguyên văn tinh thần từ research draft):** mọi khung hình phạt liệt kê là khung mà tòa *có thể* tuyên trong phạm vi luật quy định, tùy tình tiết cụ thể của từng vụ — **không phải** mức án chắc chắn, không phải dự đoán cho vụ việc nào, và không phải tư vấn "hành vi của bạn/người bạn quen sẽ bị xử lý ra sao." Số tiền/tỷ lệ thương tật/khối lượng ma túy là ngưỡng phân biệt các khoản trong cùng điều luật, không phải "giá của tội ác."

### Primary concepts — Bảng 13 tội danh (yếu tố cấu thành + khung hình phạt điển hình/tổng quát + độ tin cậy)

| # | Tội danh (Điều) | Yếu tố cấu thành cốt lõi | Khung hình phạt điển hình/tổng quát | Độ tin cậy |
|---|---|---|---|---|
| 1 | Giết người (Đ.123) | Cố ý tước đoạt tính mạng người khác trái pháp luật | Không có tình tiết định khung tăng nặng: tù **07-15 năm**. Có tình tiết tăng nặng (giết nhiều người, giết người dưới 16 tuổi, thuê giết người...): tù **12-20 năm, chung thân, hoặc tử hình** | Cao cho 2 khung chính; **thấp** cho chi tiết khoản "chuẩn bị/chưa đạt" — chưa xác minh |
| 2 | Cố ý gây thương tích (Đ.134) | Cố ý gây tổn hại sức khỏe người khác, phân khung theo % tổn thương cơ thể | Khung thấp nhất: cải tạo không giam giữ đến 03 năm hoặc tù 06 tháng-03 năm (tỷ lệ 11-30%, hoặc dưới 11% kèm tình tiết đặc biệt); tăng dần theo tỷ lệ % — khung 31%+ đã lên tù 02-06 năm | **Trung bình** — khung thấp nhất xác nhận; khung tỷ lệ cao hơn (61%+, gây chết người) **chưa xác minh đủ số liệu** |
| 3 | Hiếp dâm (Đ.141) / Hiếp dâm người dưới 16 tuổi (Đ.142) | Đ.141: dùng vũ lực/đe dọa/lợi dụng tình trạng không thể tự vệ để giao cấu trái ý muốn, bị hại ≥16 tuổi. Đ.142: bị hại dưới 16 tuổi — với bị hại dưới 13 tuổi, không cần chứng minh "trái ý muốn" | Đ.141 cơ bản: tù **02-07 năm**; tăng nặng: tù **07-15 năm**. Đ.142 cơ bản đã ở mức tù **07-15 năm**, tăng nặng cao hơn | Cao cho định nghĩa & khung cơ bản cả hai điều. **Cảnh báo gap quan trọng:** một chi tiết "khung 05-10 năm cho bị hại 16-18 tuổi" ở Đ.141 có thứ tự không khớp logic tăng dần thông thường — **độ tin cậy thấp, không dùng cho đến khi xác minh lại trực tiếp** |
| 4 | Cướp tài sản (Đ.168) | Dùng vũ lực/đe dọa dùng vũ lực ngay tức khắc hoặc thủ đoạn khác làm nạn nhân không thể chống cự để chiếm đoạt tài sản | Cơ bản: tù **03-10 năm**; tăng nặng (tổ chức, chuyên nghiệp, vũ khí, gây thương tích): tù **07-15 năm**; luật có 5 khung tăng dần, khung cao nhất có thể đến chung thân | Cao cho khung 1-2; **thấp/chưa xác minh** cho khung 3-5 |
| 5 | Bắt cóc nhằm chiếm đoạt tài sản (Đ.169) | Bắt giữ người khác làm con tin nhằm chiếm đoạt tài sản | Cơ bản: tù **02-07 năm**; khung cao nhất: **15-20 năm hoặc chung thân** | **Trung bình** — khung đầu/cuối xác nhận, khung giữa single-sourced |
| 6 | Trộm cắp tài sản (Đ.173) | Lén lút chiếm đoạt tài sản người khác | Cơ bản: cải tạo không giam giữ đến 03 năm hoặc tù 06 tháng-03 năm; khung 2: tù **02-07 năm** (giá trị lớn hơn/có tổ chức/thủ đoạn nguy hiểm...); mức tối đa lý thuyết của điều luật: **20 năm** | Cao cho khung 1-2 và mức tối đa lý thuyết; chưa xác minh ranh giới khung 3 |
| 7 | Lừa đảo chiếm đoạt tài sản (Đ.174) | Dùng thủ đoạn gian dối *ngay từ đầu* để chiếm đoạt tài sản; ngưỡng truy cứu từ **02 triệu đồng** trở lên (hoặc thấp hơn kèm tình tiết đặc biệt) | 4 khung: (1) cải tạo không giam giữ đến 03 năm/tù 06 tháng-03 năm; (2) tù 02-07 năm; (3) tù 07-15 năm; (4) tù 12-20 năm hoặc chung thân | **Cao** — cấu trúc 4 khung và ngưỡng 2 triệu khớp nhiều nguồn độc lập |
| 8 | Lạm dụng tín nhiệm chiếm đoạt tài sản (Đ.175) | Có tài sản hợp pháp ban đầu (vay/mượn/thuê) rồi dùng gian dối/bỏ trốn để chiếm đoạt, hoặc dùng tài sản vào mục đích bất hợp pháp dẫn đến mất khả năng trả | 4 khung: (1) cải tạo không giam giữ đến 03 năm/tù 06 tháng-03 năm; (2) tù 02-07 năm; (3) tù 05-12 năm; (4) tù 12-20 năm | Cao cho khung 1-2; **trung bình** cho khung 3-4 (một nguồn tổng hợp) |
| 9 | Mua bán trái phép chất ma túy (Đ.251) | Mua bán trái phép chất ma túy, khung tăng theo khối lượng | Khung thấp nhất: tù **03-07 năm**; khung cao nhất: **chung thân hoặc tử hình** (khối lượng đặc biệt lớn, ví dụ nhựa thuốc phiện/cần sa/cao côca ≥30kg, hoặc heroine/cocaine ở khối lượng lớn tương ứng) | Cao cho khung đầu/cuối; **trung bình** cho khung trung gian. **Gap quan trọng:** mốc hiệu lực 01/07/2025 — bản chất chưa xác minh, xem Khoảng trống nguồn mục 7 |
| 10 | Rửa tiền (Đ.324) | Che giấu/hợp pháp hóa tiền, tài sản có nguồn gốc từ tội phạm | 3 khung: (1) tù 01-05 năm; (2) tù 05-10 năm; (3) tù 10-15 năm; riêng "chuẩn bị phạm tội": tù 06 tháng-03 năm | **Cao** — khớp nhiều nguồn gồm VKSNDTC |
| 11 | Tham ô tài sản (Đ.353) | Người có chức vụ/quyền hạn lợi dụng chức vụ chiếm đoạt tài sản mình quản lý | 4 khung: (1) tù 02-07 năm; (2) tù 07-15 năm; (3) tù 15-20 năm (ví dụ chiếm đoạt 500tr-dưới 1 tỷ, hoặc gây thiệt hại 3-dưới 5 tỷ); (4) tù 20 năm, chung thân, hoặc **tử hình** | **Cao** — khớp nhiều nguồn kể cả ngưỡng giá trị cụ thể ở khung 3 |
| 12 | Nhận hối lộ (Đ.354) | Trực tiếp/qua trung gian nhận (hoặc sẽ nhận) tiền/tài sản/lợi ích để làm/không làm việc theo yêu cầu người đưa hối lộ | Cấu trúc 4 khung tương tự tham ô: (1) 02-07 năm; (2) 07-15 năm; (3) 15-20 năm; (4) 20 năm, chung thân, hoặc **tử hình** | **Cao** — khớp nhiều nguồn |
| 13 | Vi phạm quy định tham gia giao thông đường bộ (Đ.260) | Vi phạm quy định an toàn giao thông đường bộ gây thiệt hại (chết người, thương tích, tài sản) — phần lớn là **lỗi vô ý**, không phải cố ý | Cơ bản: phạt tiền 30-100 triệu, cải tạo không giam giữ đến 03 năm, hoặc tù **01-05 năm**; 4 khung, khung cao nhất đến **15 năm** | Cao cho khung cơ bản và mức tối đa lý thuyết; **trung bình** cho ranh giới khung giữa |

### Narrative detail

Nhìn xuyên suốt 13 tội danh này, một vài mạch chung nổi lên rất rõ, hữu ích để dựng kịch bản theo cụm thay vì rời rạc từng tội. Nhóm tội xâm phạm sở hữu (trộm cắp, cướp, bắt cóc chiếm đoạt tài sản, lừa đảo, lạm dụng tín nhiệm) đều dùng cấu trúc khung tăng dần theo giá trị/thủ đoạn, và hai tội dễ gây nhầm lẫn nhất trong cụm này — lừa đảo (Đ.174) và lạm dụng tín nhiệm (Đ.175) — chỉ khác nhau ở một điểm mấu chốt: gian dối xuất hiện *trước* khi có tài sản (lừa đảo) hay *sau* khi đã có tài sản hợp pháp (lạm dụng tín nhiệm) — ranh giới này, và ranh giới xa hơn với một khoản nợ dân sự thuần túy không có ý định chiếm đoạt, là chất liệu mythbust mạnh (6.3). Nhóm tội chức vụ/tham nhũng (tham ô, nhận hối lộ) có cấu trúc 4 khung gần như đối xứng nhau, cả hai đều có thể lên đến tử hình ở khung cao nhất — phản ánh mức độ nghiêm khắc luật dành cho hành vi lợi dụng quyền lực công. Nhóm tội xâm phạm tính mạng/sức khỏe/tình dục (giết người, cố ý gây thương tích, hiếp dâm) đứng riêng vì đụng trực tiếp vào Domain Guide §6 — mọi nội dung liên quan phải giữ kỷ luật ẩn danh nạn nhân ngay từ tầng kiến thức nền này. Cuối cùng, tội vi phạm giao thông đường bộ (Đ.260) khác về bản chất so với 12 tội còn lại: phần lớn là lỗi vô ý (vô tình gây tai nạn), không phải hành vi cố ý như các tội khác — một điểm quan trọng để tránh việc kịch bản vô tình gọi người vi phạm giao thông gây tai nạn là "tội phạm" theo nghĩa cố ý thông thường của các tội khác trong danh sách.

### Script-ready material

- Mỗi tội danh là ứng viên cho một tập/short riêng theo mô-típ "Điều [số] nói gì?" — bảng trên có thể chuyển trực tiếp thành 13 outline riêng biệt.
- Cặp Đ.174/Đ.175 là chất liệu cho một tập "so sánh song song" mạnh — cấu trúc kịch bản kiểu "hai tội nhìn giống nhau nhưng luật phân biệt ở đâu?"
- Cặp Đ.353/Đ.354 (tham ô/nhận hối lộ) là chất liệu cho một tập về nhóm tội chức vụ, có thể nối với chủ đề rửa tiền (Đ.324) thành một chuỗi 3 tập liên quan đến tội phạm kinh tế/chức vụ.
- Đ.260 (giao thông) xứng đáng một tập riêng làm rõ ranh giới lỗi vô ý vs cố ý — chủ đề gần gũi đời sống, mức độ liên quan khán giả cao.

### Production cautions

- **Domain Guide §7 (nhắc lại bắt buộc cho toàn bộ mục 5):** mọi khung hình phạt trong bảng trên là khung **chung, điển hình/tổng quát theo luật** — tuyệt đối không trình bày như dự đoán hay tư vấn cho bất kỳ tình huống, hành vi, hay người xem cụ thể nào ("nếu bạn làm X thì sẽ bị Y năm tù" là câu bị cấm tuyệt đối, kể cả khi số liệu đúng theo luật).
- Mọi khung được gắn nhãn **trung bình/thấp/chưa xác minh** trong bảng trên (đặc biệt Đ.134 khung 61%+, Đ.168 khung 3-5, Đ.169 khung giữa, Đ.175 khung 3-4, chi tiết Đ.141 "05-10 năm cho 16-18 tuổi", và mốc hiệu lực Đ.251 01/07/2025) **không được nâng cấp thành khẳng định chắc nịch** trong bất kỳ kịch bản nào cho đến khi có một lượt nghiên cứu bổ sung đối chiếu trực tiếp văn bản luật.
- **Domain Guide §6:** mọi nội dung về Đ.141/Đ.142 (hiếp dâm) phải tuân thủ chặt chẽ ẩn danh nạn nhân — không mô tả chi tiết hành vi ngoài mức cần thiết để hiểu cấu thành tội phạm, và áp dụng kỷ luật ẩn danh mức tối đa cho nạn nhân dưới 16 tuổi ngay cả ở tầng giải thích luật chung (chưa gắn với vụ án thật nào).
- Đ.260 (giao thông): phải nêu rõ đây chủ yếu là lỗi vô ý — tránh ngôn ngữ đóng khung người vi phạm giao thông như "tội phạm" theo nghĩa cố ý của 12 tội còn lại; đồng thời lưu ý ranh giới với các tội giao thông liên quan khác (đua xe, gây rối trật tự công cộng) là mảng phức tạp riêng, ngoài phạm vi packet này.
- Khi bất kỳ tội danh nào trong 13 tội trên sau này được Pillar 2-5 dùng để mô tả một vụ án thật, ngôn ngữ khung hình phạt "điển hình/tổng quát" ở đây phải được thay bằng mức án **cụ thể đã tuyên trong bản án đó** (trích từ hồ sơ vụ án thật, tier 1), không trộn hai loại thông tin (khung luật chung vs. mức án cụ thể của một vụ) vào cùng một câu mà không phân biệt rõ.

## 6. Sáu hiểu lầm phổ biến (Myth-Bust units)

Sáu mục dưới đây là chất liệu trực tiếp cho mode **Myth-Bust** của `CORE_OS/SHORTS_ENGINE.md`, theo đúng công thức: *"Nhiều người nghĩ [hiểu lầm phổ biến]. Nhưng thực ra [sự thật]."* Mỗi mục là một unit độc lập, có thể tách thành một Short riêng, và giữ đúng tinh thần educational/explainer của Pillar 1 — không đưa lời khuyên hành động cho tình huống cụ thể của người xem (`DOMAIN_GUIDE.md` §7).

### 6.1 "Tự vệ là được đánh lại thoải mái, muốn làm gì cũng được vì mình đúng"

#### Knowledge function

Đây là hiểu lầm có nguy cơ thực tế cao nhất trong 6 mục — khán giả tin sai điều này có thể tự đặt mình vào rủi ro pháp lý thật. Là mythbust tự nhiên nối với khối kiến thức 3 (Phòng vệ chính đáng).

#### Primary concepts

- Điều 22: phòng vệ chính đáng không phải tội phạm, nhưng đòi hỏi hành vi chống trả phải "cần thiết", tương xứng tính chất/mức độ nguy hiểm của hành vi xâm phạm.
- "Vượt quá giới hạn phòng vệ chính đáng" — chống trả rõ ràng quá mức cần thiết — vẫn có thể bị truy cứu trách nhiệm hình sự (dù thường nhẹ hơn người tấn công ban đầu).
- Ranh giới "cần thiết" là đánh giá theo từng vụ việc của cơ quan tố tụng/tòa án, không có công thức số học cố định.

#### Narrative detail

Công thức "Nhiều người nghĩ... Nhưng thực ra...": Nhiều người nghĩ hễ mình là bên bị tấn công trước thì được quyền chống trả không giới hạn, làm gì cũng "vô tội vì tự vệ". Nhưng thực ra luật đòi hỏi hành vi chống trả phải cần thiết và tương xứng với mức độ nguy hiểm của hành vi xâm phạm — nếu chống trả rõ ràng vượt quá mức cần thiết, chính người phòng vệ cũng có thể phải chịu trách nhiệm hình sự, dù ở mức nhẹ hơn. Ranh giới "cần thiết" không phải một con số hay một quy tắc máy móc — nó là một đánh giá từng vụ việc cụ thể của cơ quan có thẩm quyền.

#### Script-ready material

- Mở đầu: "Bạn có nghĩ rằng nếu người khác tấn công mình trước, mình được quyền làm gì cũng vô tội? Luật không nói vậy."
- Đóng: nhấn mạnh đây là nguyên tắc chung, không phải hướng dẫn hành động cho tình huống cụ thể nào.

#### Production cautions

- **Domain Guide §7:** đây là điểm rủi ro nhất trong 6 mythbust — tuyệt đối không biến giải thích này thành "quy tắc" khán giả có thể tự áp dụng để quyết định mức độ chống trả trong một tình huống thật của họ. Chỉ trình bày nguyên tắc chung, không đưa "công thức" hành động.

### 6.2 "Án treo nghĩa là được tha bổng / trắng án / không sao cả"

#### Knowledge function

Hiểu lầm phổ biến và rủi ro cao nếu channel mô tả sai — liên quan trực tiếp thuật ngữ glossary "án treo", và có nguy cơ khiến khán giả nghĩ người có án treo trong một vụ án thật "đã thoát tội".

#### Primary concepts

- Người hưởng án treo **đã bị tòa tuyên án tù** — vẫn có án tích, vẫn là người đã bị kết án.
- Án treo là biện pháp miễn chấp hành hình phạt tù có điều kiện, kèm thời gian thử thách 01-05 năm.
- Vi phạm trong thời gian thử thách (phạm tội mới, vi phạm nghĩa vụ) có thể bị buộc chấp hành hình phạt tù đã tuyên.

#### Narrative detail

Nhiều người nghĩ "được hưởng án treo" nghĩa là tòa tha bổng, không có tội, hoặc "không sao cả". Nhưng thực ra người được hưởng án treo đã bị tòa tuyên một mức án tù cụ thể — họ vẫn có án tích, vẫn là người đã bị kết án hình sự. Án treo chỉ là một cơ chế khoan hồng có điều kiện: tòa cho phép người đó không phải vào trại giam ngay, với một thời gian thử thách 01 đến 05 năm; nếu trong thời gian đó họ phạm tội mới hoặc vi phạm nghĩa vụ đặt ra, họ có thể phải chấp hành đúng mức án tù đã tuyên.

#### Script-ready material

- Câu hook: "Người 'được hưởng án treo' có phải người vô tội không? Không — họ đã bị kết án, chỉ là chưa phải vào tù ngay."
- Dùng liên kết trực tiếp tới khối 3 (Hệ thống hình phạt) khi cần chiều sâu.

#### Production cautions

- **Domain Guide §11 (Terminology Standards):** dùng đúng định nghĩa glossary "Án treo (suspended sentence)" — không diễn giải như "tha bổng."
- **Domain Guide §10:** khi mô tả một vụ án thật có án treo (Pillar 2-5), chỉ nêu sự kiện pháp lý đã tuyên, không suy diễn/bình luận "người này coi như thoát tội" — giữ đúng sắc thái factual của lớp legal/procedural.

### 6.3 Nhầm lẫn giữa tranh chấp dân sự (nợ, hợp đồng) và tội phạm hình sự (lừa đảo/lạm dụng tín nhiệm)

#### Knowledge function

Đây là ranh giới hay bị hiểu sai nhất trong đời sống thực tế Việt Nam ("vay tiền không trả có phải đi tù không?") — giá trị giáo dục cao, đồng thời rủi ro No-Legal-Advice cao nếu không cẩn thận.

#### Primary concepts

- Ranh giới nằm ở **ý định chiếm đoạt và thủ đoạn gian dối**, không phải ở việc "có trả được nợ hay không".
- Không trả được nợ vì lý do khách quan (làm ăn thua lỗ, mất khả năng thanh toán), không có gian dối/bỏ trốn: thường là quan hệ **dân sự** (khởi kiện đòi nợ), không phải hình sự.
- Gian dối ngay từ đầu (Đ.174) hoặc gian dối/bỏ trốn sau khi đã có tài sản hợp pháp (Đ.175): mới cấu thành tội hình sự.
- Một hành vi có thể vừa phát sinh trách nhiệm hình sự vừa phát sinh trách nhiệm dân sự song song (ví dụ tai nạn giao thông Đ.260: vừa xử lý hình sự vừa phải bồi thường dân sự) — không phải "chọn một trong hai".

#### Narrative detail

Nhiều người nghĩ "vay tiền không trả = lừa đảo, chắc chắn phải đi tù", hoặc ngược lại nghĩ "chuyện tiền bạc giữa hai bên chỉ là dân sự, công an không bao giờ can thiệp được". Nhưng thực ra ranh giới nằm ở ý định chiếm đoạt và thủ đoạn gian dối, không nằm ở việc có trả được nợ hay không. Nếu một người không trả được nợ vì lý do khách quan — làm ăn thua lỗ, mất khả năng thanh toán — mà không có hành vi gian dối hay bỏ trốn, đây thường là một tranh chấp dân sự, xử lý bằng con đường khởi kiện đòi nợ. Chỉ khi có yếu tố gian dối ngay từ đầu, hoặc gian dối/bỏ trốn sau khi đã có tài sản hợp pháp trong tay, hành vi mới cấu thành tội lừa đảo hoặc lạm dụng tín nhiệm chiếm đoạt tài sản.

#### Script-ready material

- Cấu trúc "hai tình huống song song": tình huống A (thua lỗ khách quan, không gian dối) → dân sự; tình huống B (gian dối/bỏ trốn) → hình sự — dựng thành hai nhân vật hư cấu đối chiếu.
- Nối trực tiếp với bảng tội danh 7-8 (Đ.174/Đ.175) ở khối 5.

#### Production cautions

- **Domain Guide §7:** đây là mythbust có rủi ro tư vấn pháp lý cao nhất trong 6 mục vì cực kỳ dễ bị khán giả hỏi ngược "vậy trường hợp của tôi thì sao?" — kịch bản phải chủ động chặn câu hỏi đó bằng khung "đây là nguyên tắc phân biệt chung, mỗi vụ việc thật cần được đánh giá bởi cơ quan có thẩm quyền/luật sư, kênh không thể kết luận thay cho trường hợp cụ thể của bạn."

### 6.4 Hiểu sai kiểu "quyền im lặng" (Miranda) tồn tại y hệt ở Việt Nam

#### Knowledge function

Đây là mythbust duy nhất trong 6 mục nhằm trực tiếp chặn một lỗi khái niệm pháp lý ngoại lai — đúng trọng tâm `DOMAIN_GUIDE.md` §2.

#### Primary concepts

- Việt Nam **không có** khái niệm "Miranda rights" hay cụm "quyền im lặng" đúng nghĩa common-law — không có nghĩa vụ đọc cảnh báo kiểu Miranda khi bắt giữ.
- Điểm tương đồng gần nhất, có căn cứ pháp lý thật: nguyên tắc suy đoán vô tội (Điều 13 BLTTHS) + quyền trình bày lời khai như một quyền, không phải nghĩa vụ (Điều 60/61, cần xác minh số điều) + nguyên tắc trách nhiệm chứng minh thuộc cơ quan tố tụng.

#### Narrative detail

Nhiều người xem phim Mỹ rồi nghĩ ở Việt Nam công an cũng phải "đọc quyền" cho người bị bắt kiểu Miranda, hoặc nghĩ có một "quyền im lặng" y hệt. Nhưng thực ra pháp luật Việt Nam không có khái niệm mang đúng tên gọi đó — đây là một hệ thống civil-law khác về cấu trúc. Điều gần nhất có căn cứ pháp lý thật ở Việt Nam là sự kết hợp giữa nguyên tắc suy đoán vô tội (gánh nặng chứng minh luôn thuộc về cơ quan tố tụng, không phải người bị buộc tội) và quyền trình bày lời khai như một lựa chọn, không phải nghĩa vụ tự nhận tội.

#### Script-ready material

- Đối lập trực quan: cảnh phim Mỹ đọc Miranda vs. thực tế pháp lý Việt Nam — dùng làm hook "phim ảnh nói gì, luật thật nói gì".
- Nối trực tiếp khối kiến thức 4 (Quyền của bị can/bị cáo).

#### Production cautions

- **Domain Guide §2 (nhắc lại nguyên văn):** không mô tả pháp luật Việt Nam bằng khái niệm pháp lý ngoại lai không tồn tại trong hệ thống — nêu rõ điểm tương đồng/khác biệt thay vì mượn nguyên xi thuật ngữ nước ngoài.

### 6.5 "Xử phúc thẩm là xử lại từ đầu" / lẫn lộn phúc thẩm với giám đốc thẩm-tái thẩm

#### Knowledge function

Mythbust kỹ thuật-tố tụng, cần thiết để khán giả không hiểu sai khi theo dõi tin tức về một vụ án đang kháng cáo hay đang được xét lại đặc biệt.

#### Primary concepts

- Phúc thẩm: xét xử lại vụ án (hoặc phần bị kháng cáo/kháng nghị) khi bản án sơ thẩm **chưa** có hiệu lực pháp luật — dựa trên hồ sơ đã có, có thể bổ sung chứng cứ, không phải "xóa bỏ hoàn toàn" sơ thẩm.
- Giám đốc thẩm/tái thẩm: thủ tục đặc biệt, **không phải một cấp xét xử thường xuyên**, chỉ tiến hành khi có căn cứ pháp luật cụ thể (vi phạm tố tụng nghiêm trọng, hoặc tình tiết mới), áp dụng cho bản án **đã** có hiệu lực pháp luật.

#### Narrative detail

Nhiều người hiểu phúc thẩm là một "phiên xử mới hoàn toàn độc lập", như thể toàn bộ quá trình sơ thẩm bị xóa bỏ. Nhưng thực ra phúc thẩm là xét xử lại vụ án dựa trên hồ sơ đã có (có thể bổ sung thêm chứng cứ), khi bản án sơ thẩm chưa có hiệu lực pháp luật. Một hiểu lầm khác thường đi kèm: coi giám đốc thẩm/tái thẩm là "phiên tòa cấp 3" mà ai cũng có thể yêu cầu bất cứ lúc nào. Nhưng thực ra đây là thủ tục đặc biệt, hiếm, chỉ được tiến hành khi có căn cứ pháp luật cụ thể, và áp dụng cho bản án đã có hiệu lực pháp luật — khác hẳn bản chất phúc thẩm vốn áp dụng cho bản án chưa có hiệu lực.

#### Script-ready material

- Sơ đồ so sánh 2 cột: "Phúc thẩm (bản án chưa hiệu lực)" vs. "Giám đốc thẩm/Tái thẩm (bản án đã hiệu lực, thủ tục đặc biệt hiếm)".
- Nối trực tiếp khối kiến thức 2 (Quy trình tố tụng).

#### Production cautions

- **Domain Guide §11:** giữ đúng định nghĩa "bản án có hiệu lực pháp luật" trong glossary khi đối chiếu hai thủ tục này — không lẫn lộn ranh giới hiệu lực giữa phúc thẩm và giám đốc thẩm/tái thẩm.

### 6.6 "Có bản án sơ thẩm rồi = đã bị kết án chính thức, có thể gọi thẳng là tội phạm/hung thủ"

#### Knowledge function

Đây là mythbust trực tiếp nhất của toàn bộ ranh giới cốt lõi domain (`DOMAIN_GUIDE.md` §4) — bắt buộc phải có mặt trong bất kỳ chuỗi mythbust nào của Pillar 1, vì đây là lỗi có thể gây hậu quả pháp lý thật (defamation) nếu lan sang nội dung Pillar 2-5 sau này.

#### Primary concepts

- Bản án sơ thẩm, **một mình nó, không phải "bản án có hiệu lực pháp luật"** nếu vẫn còn trong thời hạn kháng cáo/kháng nghị (15 ngày kể từ ngày tuyên án) hoặc đang được xét xử phúc thẩm.
- Một người mới chỉ có bản án sơ thẩm kết tội, chưa hết hạn kháng cáo, **vẫn phải được gọi là "bị cáo"**, không phải "tội phạm" hay "kẻ giết người".

#### Narrative detail

Nhiều người nghĩ hễ tòa đã tuyên bản án sơ thẩm kết tội thì coi như xong, có thể gọi thẳng người đó là "tội phạm" hay dùng tên tội để gọi họ. Nhưng thực ra bản án sơ thẩm chỉ trở thành "bản án có hiệu lực pháp luật" sau khi hết thời hạn kháng cáo/kháng nghị (15 ngày kể từ ngày tuyên án) mà không ai kháng cáo/kháng nghị, hoặc sau khi đã xét xử phúc thẩm xong. Trước thời điểm đó, đúng ngôn ngữ pháp lý bắt buộc là gọi người này "bị cáo" — không phải "tội phạm", "hung thủ", hay bất kỳ danh từ khẳng định tội nào khác.

#### Script-ready material

- Câu hook mạnh nhất trong cả 6 mythbust, có thể dùng làm title Short: "Tòa đã tuyên án — vậy đã được gọi là 'tội phạm' chưa? Câu trả lời quyết định cả một nguyên tắc pháp lý."
- Nối trực tiếp khối kiến thức 2 (quy trình tố tụng, đặc biệt bước 5-6) và khối 4 (suy đoán vô tội).

#### Production cautions

- **Domain Guide §4 (nhắc lại nguyên văn, ranh giới quan trọng nhất toàn domain):** một script kỹ thuật hedge đúng từng câu ("bị cáo được cho là...") nhưng tiêu đề/thumbnail/cấu trúc tổng thể ngụ ý tội đã được xác định vẫn **fail "net impression test"** — QA phải đánh giá ấn tượng tổng thể của cả video, không chỉ tìm-thay cụm từ hedge.
- **Domain Guide §11:** dùng đúng thuật ngữ glossary — "bị cáo" cho giai đoạn này, không phải "tội phạm"/"kẻ giết người"; đây là quy tắc không có ngoại lệ cho đến khi có bản án có hiệu lực pháp luật (hoặc, với người đã mất/lịch sử, có kết án cuối cùng được sử liệu tier 1-3 xác nhận).

---

# Risk-Specific Editorial Rules

Các quy tắc dưới đây tái hiện và cụ thể hóa `DOMAIN_GUIDE.md` cho phạm vi Pillar 1, theo mẫu Required/Forbidden language pattern đã dùng ở `KP_FS_001`.

## Rule 1 — Legal-Status Precision Rule (§4, ranh giới quan trọng nhất domain)

Mọi đề cập một người chưa có bản án có hiệu lực pháp luật phải dùng đúng thuật ngữ giai đoạn (bị tình nghi/bị can/bị cáo), kể cả trong nội dung thuần túy giáo dục về luật (không gắn với vụ án thật nào) — giữ kỷ luật ngôn ngữ này ngay từ tầng kiến thức nền để nó tự động đúng khi Pillar 2-5 tham chiếu ngược lại packet.

**Required:** "bị cáo", "bị can", "bị tình nghi" theo đúng giai đoạn tố tụng.
**Forbidden:** "tội phạm", "hung thủ", "kẻ giết người" cho bất kỳ ai chưa có bản án có hiệu lực pháp luật.

## Rule 2 — No-Individualized-Advice Rule (§7)

Không dùng khung hình phạt/quy trình tố tụng để kết luận thay khán giả về tình huống cụ thể của họ hoặc người quen của họ.

**Required:** "Đây là khung hình phạt/quy trình chung theo luật — mỗi vụ việc thật cần cơ quan có thẩm quyền hoặc luật sư đánh giá cụ thể."
**Forbidden:** "Nếu bạn/người quen bạn ở trường hợp này thì sẽ bị xử lý ra sao..." dưới dạng kết luận trực tiếp.

## Rule 3 — Confidence-Tiering Disclosure Rule (§3, §5)

Mọi khung hình phạt trung gian/chi tiết được research draft gắn cờ "trung bình/thấp/chưa xác minh" phải giữ nguyên nhãn đó trong kịch bản — không lặng lẽ nâng cấp thành khẳng định chắc nịch.

**Required:** "theo các nguồn phổ biến hiện có, khung này thường được ghi nhận là..." (khi độ tin cậy trung bình/thấp).
**Forbidden:** phát biểu số liệu chưa xác minh như một sự thật tuyệt đối, không gắn nhãn.

## Rule 4 — Foreign Legal Concept Import Ban (§2)

Không mô tả pháp luật Việt Nam bằng khái niệm common-law không tồn tại trong hệ thống (Miranda, grand jury, pleading the fifth...).

**Required:** nêu điểm tương đồng/khác biệt thật (ví dụ nguyên tắc suy đoán vô tội) thay vì mượn thuật ngữ nước ngoài.
**Forbidden:** "Việt Nam có quyền im lặng/Miranda giống Mỹ."

## Rule 5 — Victim Anonymity Rule (§6)

Áp dụng ngay từ tầng giải thích luật chung cho các tội xâm phạm tình dục/tính mạng, không chờ đến khi có nội dung vụ án thật mới bật quy tắc này.

**Required:** mô tả cấu thành tội phạm ở mức khái quát cần thiết để hiểu luật, không thêm chi tiết hành vi/nạn nhân không cần thiết.
**Forbidden:** mô tả chi tiết hành vi xâm phạm tình dục vượt quá mức cần thiết để hiểu cấu thành tội phạm.

## Rule 6 — Net Impression Rule (§4)

QA phải đánh giá ấn tượng tổng thể của toàn bộ video (tiêu đề, thumbnail, cấu trúc), không chỉ từng câu hedge riêng lẻ.

**Required:** tiêu đề/thumbnail trung lập, không ngụ ý kết luận tội trước khi có bản án có hiệu lực.
**Forbidden:** thumbnail/tiêu đề giật gân ngụ ý tội đã xác định trong khi script bên trong hedge đúng từng câu.

## Rule 7 — Anti-Sensationalism Rule (§9)

**Forbidden:** "SỰ THẬT RÙNG RỢN", "KHÔNG AI DÁM KỂ", countdown-of-horror framing cho bất kỳ nội dung giải thích luật/tội danh nào.
**Required:** giọng điệu điềm tĩnh, tôn trọng, tò mò thực chất làm động lực hook, không dựng sợ hãi giả tạo.

## Rule 8 — Gap Non-Fabrication Rule (đặc thù packet này, §3)

Không lấp bất kỳ khoảng trống nào đã liệt kê ở "Khoảng trống nguồn" bằng suy đoán khi viết kịch bản chi tiết.

**Required:** "cần đối chiếu thêm văn bản luật hiện hành trước khi khóa số liệu này."
**Forbidden:** tự bổ sung số liệu/ranh giới khung hình phạt không có trong nguồn đã xác minh.

---

# Domain QA Checklist (áp dụng cho nội dung phát sinh từ packet này)

Tái hiện và cụ thể hóa từ `DOMAIN_GUIDE.md` §13 cho phạm vi Pillar 1:

1. Mọi đề cập một người chưa có bản án có hiệu lực pháp luật có dùng đúng ngôn ngữ giai đoạn hợp pháp không, và cả video (không chỉ từng câu) có vượt qua "net impression test" không (§4)?
2. Có dòng nào đưa khung hình phạt/quy trình như lời khuyên trực tiếp cho tình huống cụ thể của khán giả không (§7)?
3. Mọi số liệu gắn cờ trung bình/thấp/chưa xác minh trong packet có được giữ nguyên nhãn, không bị nâng cấp thành khẳng định chắc nịch không (§3)?
4. Có khái niệm pháp lý ngoại lai (Miranda, quyền im lặng kiểu Mỹ...) bị mượn nguyên xi cho hệ thống Việt Nam không (§2)?
5. Nội dung về tội xâm phạm tình dục/tính mạng có giữ kỷ luật ẩn danh nạn nhân, đặc biệt nạn nhân dưới 16 tuổi, không (§6)?
6. Có dòng nào dùng khung sợ hãi/giật gân (countdown-of-horror, "SỰ THẬT RÙNG RỢN"...) không (§9)?
7. Nội dung có giữ được cả ba lớp legal/procedural, narrative, societal-reflective mà không xóa bỏ lớp nào không (§10)?
8. Thuật ngữ có nhất quán với `GLOSSARY/DOMAIN_GLOSSARY.md` không, và mọi khung hình phạt có nêu rõ đây là "Việt Nam, BLHS 2015 sửa đổi 2017" không (§2)?

---

# Retrieval Warnings

Khi packet này được truy xuất, hệ thống nên đính kèm các cảnh báo:

- Đây là domain rủi ro `critical` — một bậc trên `high` của FS/Tử Vi.
- Mọi khung hình phạt ở Phần 5 là khung chung/điển hình theo luật, không phải mức án cụ thể hay tư vấn cho tình huống nào.
- Nhiều khung hình phạt trung gian (khoản 3-5 của các điều luật dài) chưa được đối chiếu trực tiếp văn bản luật — xem "Khoảng trống nguồn" trước khi dùng làm số liệu cứng.
- Điều 141 có một chi tiết khung hình phạt bị nghi ngờ sai lệch (khung "05-10 năm cho bị hại 16-18 tuổi") — không dùng cho đến khi xác minh lại.
- Điều 251 có một gap chưa đóng về mốc hiệu lực 01/07/2025 — bắt buộc kiểm tra trước khi khóa nội dung tập về ma túy sản xuất/phát hành sau mốc này.
- Một người chưa có bản án có hiệu lực pháp luật luôn phải được gọi bằng đúng thuật ngữ giai đoạn (bị tình nghi/bị can/bị cáo).
- Không có khái niệm "quyền im lặng"/Miranda kiểu Mỹ trong hệ thống pháp luật Việt Nam.
- Domain QA Policy của domain CL đã `active`, nhưng packet này **chưa** được chạy qua checklist đó chính thức.

---

# Editorial Memory Seeds

Các nguyên tắc sau nên được đẩy vào bộ nhớ vận hành sau khi packet qua QA:

- Trước bản án có hiệu lực pháp luật: luôn "bị tình nghi/bị can/bị cáo", không bao giờ "tội phạm/hung thủ".
- Án treo = đã bị kết án + miễn chấp hành tù có điều kiện, không phải "trắng án".
- Khung hình phạt trong Pillar 1 luôn là khung chung/điển hình — không phải tư vấn hay dự đoán cho một tình huống cụ thể.
- Việt Nam không có "quyền im lặng"/Miranda kiểu Mỹ — chỉ có nguyên tắc suy đoán vô tội + quyền không bị ép cung.
- Bản án sơ thẩm ≠ bản án có hiệu lực pháp luật nếu còn trong hạn kháng cáo/kháng nghị hoặc đang phúc thẩm.
- Giám đốc thẩm/tái thẩm là thủ tục đặc biệt hiếm, không phải "cấp xét xử thứ ba".
- Ranh giới lừa đảo/lạm dụng tín nhiệm/tranh chấp dân sự nằm ở ý định chiếm đoạt + gian dối, không ở việc trả được nợ hay không.
- Nhiều số liệu chi tiết ở Phần 5 (khung hình phạt trung gian) chưa xác minh trực tiếp văn bản luật — không lấp gap bằng suy đoán khi viết kịch bản.

---

# Packet Completion Notes

Packet này tổng hợp đầy đủ 1 research draft nền tảng duy nhất hiện có của Pillar 1 (`RESEARCH_DRAFT_LUAT_HINH_SU.md`) thành một Knowledge Packet có cấu trúc thống nhất, giữ nguyên toàn bộ cảnh báo/nhãn độ tin cậy/"gap cần xác minh thêm" đã ghi trong nguồn gốc — không có tuyên bố nào trong research draft bị lược bỏ hoặc bị làm phẳng thành khẳng định chắc chắn hơn mức nguồn cho phép. Đây là draft phù hợp làm nền tri thức nội bộ cho các bước tiếp theo (Creative Knowledge, Series Bible, Character Bible nếu cần cho nhân vật hư cấu minh họa, kịch bản Pillar 1), **không phải nội dung sẵn sàng công chiếu**. Packet cần: (1) Domain QA Policy chính thức của domain CL (hiện `active`) áp dụng và ký duyệt trên chính packet này; (2) đối chiếu trực tiếp văn bản luật gốc tại vbpl.vn/thuvienphapluat.vn cho toàn bộ các mục còn gắn cờ ở "Khoảng trống nguồn"; (3) rà soát Legal QA bởi cố vấn pháp lý trước khi bất kỳ tập nào trích dẫn số điều/khung hình phạt cụ thể được phát hành.

# Final Packet Use Boundary

Các agent tương lai phải coi packet này là một tài sản tri thức được quản trị, không phải nội dung sẵn sàng khán giả. Packet có thể dùng để truy xuất khái niệm, cảnh báo, thuật ngữ, ràng buộc sản xuất, và phụ thuộc QA. Packet **không được** sao chép trực tiếp vào kịch bản công khai mà không qua Content Engine transformation và QA review đầy đủ.

Mọi sản phẩm phái sinh phải giữ được các ranh giới sau:

1. Không ai được gọi là "tội phạm/hung thủ" trước khi có bản án có hiệu lực pháp luật — bất kể ngữ cảnh giáo dục hay ngữ cảnh vụ án thật.
2. Giải thích luật không phải là tư vấn pháp lý cho tình huống cụ thể của người xem.
3. Mọi khung hình phạt là thông tin chung/điển hình, không phải dự đoán hay cam kết cho một vụ việc thật.
4. Không mượn khái niệm pháp lý ngoại lai (Miranda, quyền im lặng kiểu Mỹ...) để mô tả hệ thống pháp luật Việt Nam.
5. Không bao giờ lấp một khoảng trống nguồn đã gắn cờ bằng suy đoán — giữ nguyên trạng thái "chưa xác minh" cho đến khi có nghiên cứu bổ sung đọc trực tiếp văn bản luật.

Nếu một sản phẩm đầu ra tương lai không thể giữ được năm ranh giới này, nó phải được sửa lại, nâng cấp xét duyệt, hoặc từ chối trước khi công chiếu.
