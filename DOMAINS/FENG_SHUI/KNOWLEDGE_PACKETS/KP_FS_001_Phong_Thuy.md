---
schema_version: 1.0
packet_id: KP_FS_001
domain_id: FS
asset_id: KP_FS_001
canonical_owner: DOMAINS/FENG_SHUI
canonical_topic: Phong Thủy — Nền tảng lý thuyết và Ứng dụng nhà ở
vietnamese_display_name: Phong Thủy (Phong Thủy Học)
chinese_canonical_title: 風水
english_working_title: Feng Shui — Foundational Theory & Home Application
object_type: Knowledge Packet
status: draft-pending-human-review
version: 0.1
language: Tiếng Việt (chính), chú thích Hán/Anh cho thuật ngữ gốc
primary_tradition_context: Phong Thủy Trung Hoa cổ điển (Loan Đầu / Hình Thế phái; Lý Khí / Compass phái gồm Bát Trạch và Huyền Không Phi Tinh), tiếp biến vào văn hóa nhà ở Việt Nam đương đại
secondary_context: Nền Âm Dương – Ngũ Hành – Bát Quái dùng chung với nhánh Tử Vi Đẩu Số trong cùng domain FS (xem DOMAIN_GUIDE.md §1); không đi sâu Tử Vi trong packet này
risk_level: high
risk_reasons:
  - Anti-Fear-Sales — vật phẩm phong thủy, bàn thờ gia tiên, bối cảnh lừa đảo tâm linh thực tế tại Việt Nam
  - Ranh giới cá nhân hóa — nguy cơ biến giải thích lý thuyết thành "luận giải hộ" hướng nhà/mệnh cho khán giả cụ thể
  - Ranh giới tài chính — nguy cơ cam kết vật phẩm/hướng nhà đảm bảo tài lộc
  - Mâu thuẫn liên trường phái — Bát Trạch và Huyền Không Phi Tinh có thể cho khuyến nghị trái ngược trên cùng một nhà
  - Quy gán lịch sử truyền thuyết (Phục Hy, Văn Vương, Quách Phác, Dương Quân Tùng) dễ bị trình bày nhầm thành sử liệu xác thực
required_qa:
  - Domain QA (Phong Thủy) — DOMAIN_QA/DOMAIN_QA_POLICY.md (hiện: planned, cần hoàn thiện trước khi packet này chuyển trạng thái active)
  - Research QA
  - Safety QA (Anti-Fear-Sales Standard)
  - Historical QA
  - Brand QA
dependencies:
  - DOMAINS/FENG_SHUI/DOMAIN_GUIDE.md
  - DOMAINS/FENG_SHUI/DOMAIN_MANIFEST.md
  - DOMAINS/FENG_SHUI/SOURCES/RESEARCH_DRAFT_AM_DUONG_NGU_HANH.md
  - DOMAINS/FENG_SHUI/SOURCES/RESEARCH_DRAFT_BAT_QUAI_TRUONG_PHAI.md
  - DOMAINS/FENG_SHUI/SOURCES/RESEARCH_DRAFT_UNG_DUNG_NHA_O.md
  - DOMAIN_SPECIFICATION/KNOWLEDGE_PACKET_SCHEMA.md
source_lineage: Tổng hợp 3 research draft (2026-07-17). Tier 1 (đồng thuận cổ điển) cho hai chu kỳ Tương Sinh/Tương Khắc Ngũ Hành và bảng Bát Quái Hậu Thiên. Tier 3 (thực hành phổ biến đương đại, đối chiếu ≥2-3 nguồn độc lập/mục) cho phần lớn nội dung ứng dụng nhà ở và các chi tiết trường phái Tử Vi liên quan. Chưa có nguồn academic/dân tộc học tier 4 nào được truy cập — xem "Khoảng trống nguồn" trong Canonical Sources.
confidence_level: mixed — xem nhãn độ tin cậy riêng ở từng khái niệm trong Core Concepts Map và Applied Section
terminology: Xem GLOSSARY/DOMAIN_GLOSSARY.md — hiện đang ở trạng thái "planned/TODO_RESEARCH_REQUIRED"; packet này đề xuất các thuật ngữ lõi cần được nạp vào glossary chính thức (xem mục Terminology bên dưới) trước khi dùng làm nguồn cho kịch bản sản xuất
claims: Xem Core Concepts Map và Applied Section — mỗi tuyên bố cụ thể được gắn nhãn trường phái và mức độ tin cậy tại nguồn
cautions: Xem Risk-Specific Editorial Rules — đặc biệt Rule 1 (không trộn trường phái), Rule 6 (Anti-Fear-Sales)
QA_status: draft — chưa qua Domain QA / Research QA / Safety QA chính thức; KHÔNG dùng trực tiếp làm kịch bản sản xuất trước khi human review
compatibility_aliases: [Feng Shui, Phong Thuy, KP_PHONG_THUY_001, Phong Thuy Nen Tang]
review_cadence: Hàng năm, và bất kỳ khi nào phát hiện nguồn mới, mâu thuẫn liên trường phái mới, hoặc tiền lệ QA mới liên quan Anti-Fear-Sales hoặc ranh giới cá nhân hóa
---

# KP_FS_001 — Phong Thủy (Gói Tri Thức Nền Tảng)

## Packet Control

| Field | Value |
|---|---|
| Packet ID | KP_FS_001 |
| Domain ID | FS |
| Canonical Topic | Phong Thủy — Nền tảng lý thuyết và Ứng dụng nhà ở |
| Vietnamese Display Name | Phong Thủy (Phong Thủy Học) |
| Chinese Canonical Title | 風水 |
| English Working Title | Feng Shui — Foundational Theory & Home Application |
| Object Type | Knowledge Packet |
| Status | draft-pending-human-review |
| Version | 0.1 |
| Language | Tiếng Việt (chính), có chú thích Hán/Anh cho thuật ngữ gốc |
| Primary Tradition Context | Phong Thủy Trung Hoa cổ điển — Loan Đầu (Hình Thế phái) và Lý Khí (Compass phái, gồm Bát Trạch và Huyền Không Phi Tinh) — tiếp biến vào văn hóa nhà ở Việt Nam đương đại |
| Secondary Context | Nền Âm Dương – Ngũ Hành – Bát Quái dùng chung với nhánh Tử Vi Đẩu Số trong cùng domain FS |
| Risk Level | High |
| Risk Reasons | Anti-Fear-Sales (vật phẩm, bàn thờ), ranh giới cá nhân hóa, ranh giới tài chính, mâu thuẫn liên trường phái, quy gán lịch sử truyền thuyết |
| Required QA | Domain QA (Phong Thủy — hiện `planned`), Research QA, Safety QA, Historical QA, Brand QA |
| Dependencies | `DOMAIN_GUIDE.md`, `DOMAIN_MANIFEST.md`, 3 research draft trong `SOURCES/`, `KNOWLEDGE_PACKET_SCHEMA.md` |
| Review Cadence | Hàng năm, và bất kỳ khi có nguồn mới hoặc tiền lệ QA mới |

**Lưu ý trạng thái quan trọng:** Đây là Knowledge Packet đầu tiên của domain Phong Thủy, được biên soạn từ 3 research draft (trạng thái gốc: "draft research input, chưa qua Domain QA"). `DOMAIN_QA/DOMAIN_QA_POLICY.md` và `GLOSSARY/DOMAIN_GLOSSARY.md` của domain này hiện vẫn ở trạng thái `planned`. Packet này **không thay thế** yêu cầu Domain QA chính thức — nó là bước tổng hợp trung gian bắt buộc trước khi domain có thể chuyển từ `in_progress` sang `active` cho mục đích sản xuất kịch bản, đúng tinh thần `DOMAIN_MANIFEST.md`: "Content generation (episode scripts) remains blocked until foundational Knowledge Packets pass the same research-and-cross-check discipline used for KP_BUD_001."

---

# Identity

## Canonical Name

Phong Thủy (風水).

## Alternative Names

- Phong Thủy học
- Kham Dư (堪輿) — thuật ngữ cổ hơn, gần nghĩa hơn với "địa lý học huyền học", từng được dùng song song hoặc thay cho "Phong Thủy" trong văn bản cổ.
- Địa lý (cách gọi dân gian Việt Nam, đặc biệt khi nói về chọn đất/hướng mộ — dễ gây lẫn với "địa lý" theo nghĩa khoa học địa lý hiện đại, cần phân biệt rõ khi kịch bản hóa).
- Feng Shui (tiếng Anh, phiên âm Quan Thoại phổ biến toàn cầu).
- Chinese Geomancy (thuật ngữ học thuật phương Tây cũ hơn, ít dùng trong nội dung phổ thông đương đại).

## Chinese

- 風水 (Phong Thủy)
- 堪輿 (Kham Dư)
- 巒頭 (Loan Đầu — Form School)
- 理氣 (Lý Khí — Compass School)
- 八宅 (Bát Trạch — Eight Mansions)
- 玄空飛星 (Huyền Không Phi Tinh — Flying Star)
- 八卦 (Bát Quái — Eight Trigrams)
- 陰陽 (Âm Dương)
- 五行 (Ngũ Hành)

## Ý nghĩa tên gọi

"Phong Thủy" nghĩa đen là "gió" (phong) và "nước" (thủy). Cách ghép hai chữ này thường được các nguồn thực hành dẫn về ý một câu trong Táng Thư (葬書, "Book of Burial", tương truyền gắn với Quách Phác thời Tấn — xem cảnh báo độ tin cậy ở Historical Background), đại ý: khí gặp gió thì tán, gặp nước thì dừng lại. Đây là nguyên lý gốc của nhánh Loan Đầu — chọn nơi có địa hình giữ được khí lại (tránh gió lộng, có nước bao quanh/chảy qua) — và tên gọi "Phong Thủy" về bản chất là một cách gọi tắt cho toàn bộ hệ thống dựa trên nguyên lý sơ khai này, dù thực hành đương đại đã mở rộng rất xa khỏi ý nghĩa chọn đất thuần túy ban đầu (bao gồm cả nhánh Lý Khí dựa la bàn/thời gian mà nghĩa đen "gió-nước" không còn mô tả trực tiếp).

## Related Terms

Âm Dương, Ngũ Hành, Bát Quái (Tiên Thiên/Hậu Thiên), Khí, Long mạch, Minh đường, Tứ Tượng (Thanh Long, Bạch Hổ, Chu Tước, Huyền Vũ), Loan Đầu, Lý Khí, Bát Trạch, Kua number/Quái Mệnh, Đông Tứ Mệnh/Tây Tứ Mệnh, Huyền Không Phi Tinh, Vận (chu kỳ 20 năm), 24 Sơn Hướng, Dương Trạch, Âm Trạch, Tọa Hung Hướng Cát, thước Lỗ Ban.

## Keywords

Phong thủy, Âm dương, Ngũ hành, Bát quái, Tiên Thiên Bát Quái, Hậu Thiên Bát Quái, Loan Đầu, Hình Thế phái, Lý Khí, Compass School, Bát Trạch, Eight Mansions, Kua number, Huyền Không Phi Tinh, Flying Star, hướng nhà, hướng bếp, hướng giường, bàn thờ gia tiên, vật phẩm phong thủy, gương bát quái, tỳ hưu, thiềm thừ/cóc ba chân, mệnh Kim Mộc Thủy Hỏa Thổ, Đông Tứ Mệnh, Tây Tứ Mệnh, tương sinh, tương khắc, Anti-Fear-Sales.

---

# Historical Background

## Origins

**Âm Dương.** Về ngôn ngữ, "âm" nguyên nghĩa là mặt khuất/bóng râm của sườn đồi, "dương" là mặt hướng nắng — một cặp hình ảnh cụ thể trước khi trở thành phạm trù triết học trừu tượng. Việc dùng Âm Dương như một cặp lực đối lập-bổ sung mang tính triết học được ghi nhận sớm nhất khoảng thế kỷ 4 TCN, gắn với học giả Trâu Diễn (Zou Yan, 305–240 TCN) và phái Âm Dương gia, dù khái niệm có thể đã manh nha sớm hơn trong tư duy dân gian và trong Kinh Dịch (thời Tây Chu, khoảng 1046–256 TCN). Việc gán phát minh Bát Quái/Kinh Dịch cho Phục Hy là quy gán truyền thuyết dân gian, **không phải sự kiện lịch sử đã kiểm chứng** — cần xử lý tương tự cách `DOMAIN_GUIDE.md` §2 yêu cầu xử lý quy gán Trần Đoàn cho Tử Vi. Biểu tượng Thái Cực Đồ (vòng tròn Âm-Dương xoáy vào nhau) xuất hiện **muộn hơn nhiều** so với khái niệm triết học — dạng phổ biến ngày nay được liên hệ chủ yếu với thời Tống (960–1279) và nhà triết học Đạo giáo Chu Đôn Di, nhưng nguồn gốc chính xác của biểu tượng đồ họa vẫn còn tranh luận học thuật — độ tin cậy trung bình.

**Ngũ Hành.** Hình thành như hệ thống mạch lạc vào khoảng thời Chiến Quốc (475–221 TCN), được các học giả phái Hoàng Lão hệ thống hóa, có mặt trong các văn bản nền tảng như Hoàng Đế Nội Kinh. Năm hành không phải 5 "chất liệu" vật lý tĩnh mà là 5 nguyên mẫu/giai đoạn của sự chuyển hóa. Hai chu kỳ Tương Sinh và Tương Khắc là phần **chắc chắn nhất** trong toàn bộ nền tảng lý thuyết này — xác minh chéo qua ≥3 nguồn độc lập (tiếng Việt phổ thông + Wikipedia + học thuật TCM tiếng Anh), không phát hiện mâu thuẫn, xếp Tier 1 theo `DOMAIN_GUIDE.md` §3.

**Bát Quái.** Tám tổ hợp 3 hào (Càn, Khôn, Chấn, Tốn, Khảm, Ly, Cấn, Đoài) trong vũ trụ quan Kinh Dịch/Đạo giáo. Có **hai cách sắp xếp khác nhau, không được lẫn**: Tiên Thiên Bát Quái (tương truyền Phục Hy sáng lập, thiên về triết học/trạng thái nguyên thủy) và Hậu Thiên Bát Quái (tương truyền Văn Vương nhà Chu sắp xếp lại, thiên về ứng dụng thực tiễn). **Hậu Thiên Bát Quái mới là hệ phương vị dùng trong thực hành Phong Thủy nhà ở** (la bàn, Bát Trạch, Huyền Không) — đây là điểm hay bị lẫn nhất khi biên tập. Cả hai quy gán tác giả (Phục Hy, Văn Vương) đều là truyền thuyết, không phải sử liệu xác thực.

**Loan Đầu (Hình Thế phái).** Trường phái Phong Thủy cổ nhất trong hai nhánh lớn (Loan Đầu và Lý Khí). Nguyên lý cốt lõi — khí theo gió mà tán, gặp nước thì dừng — thường được dẫn (paraphrase) từ Táng Thư, tương truyền gắn với Quách Phác thời Tấn; độ tin cậy trung bình cho việc câu này được lưu truyền rộng trong giới thực hành, thấp hơn cho việc xác thực văn bản gốc chưa qua chỉnh sửa qua các đời. Loan Đầu được cho là hệ thống hóa mạnh vào thời Đường qua nhân vật Dương Quân Tùng (Yang Yun-Sung) — mức tin cậy trung bình, thuộc về truyền thuyết nghề nghiệp phổ biến trong giới Phong Thủy hơn là mốc sử học được kiểm chứng độc lập.

**Lý Khí (Compass School).** Nhánh dùng la bàn/phương vị/thời gian, gồm hai sub-lineage độc lập được nghiên cứu trong packet này: **Bát Trạch** (theo một nguồn thực hành tiếng Việt, có gốc gắn với dòng Tam Hợp) và **Huyền Không Phi Tinh** (gốc dòng Tam Nguyên). Đây là **hai lineage khác gốc lý luận**, không phải hai bước của cùng một hệ thống — điểm này được nhấn mạnh xuyên suốt packet (xem Historical Debates và Risk-Specific Editorial Rules Rule 1).

## Historical Development

Phong Thủy không có một văn bản kinh điển duy nhất như Kinh Địa Tạng có cho domain Phật giáo — đây là một truyền thống sống với nhiều trường phái/lineage cạnh tranh (`DOMAIN_GUIDE.md` §2). Khi tiếp biến vào văn hóa Việt Nam, kiến trúc nhà truyền thống (nhà quay lưng vào núi/gò, nhìn ra ao/sông) là một minh chứng văn hóa gần gũi cho nguyên lý Loan Đầu — thuộc lớp "cultural/historical" theo `DOMAIN_GUIDE.md` §10, không cần khẳng định tính hiệu quả.

Một biến đổi văn hóa đáng chú ý trong thực hành đương đại tại Việt Nam: đô thị hóa khiến phần lớn người mua nhà/đất không còn chọn được hướng đất (quỹ đất có sẵn), nên trọng tâm ứng dụng đã dịch chuyển từ "chọn hướng nhà" (đặc quyền của người xưa có đất) sang "hóa giải hướng nhà không hợp mệnh" bằng cách điều chỉnh hướng cửa/bếp/giường/bàn làm việc bên trong một căn nhà có hướng tổng thể cố định. Đây là một lát cắt "truyền thống được địa phương hóa/đô thị hóa qua thời gian", phù hợp lớp cultural/historical.

Thực hành bàn thờ gia tiên tại Việt Nam là một mảng riêng, mang tính văn hóa/tâm linh dân gian nhiều hơn là kỹ thuật Bát Trạch thuần túy — hiện chỉ có nguồn tier 3 (thương mại/dân gian phổ biến), **chưa tìm được nguồn dân tộc học/nghiên cứu văn hóa Việt Nam độc lập** — đây là khoảng trống nguồn cần bổ sung trước khi nâng packet lên trạng thái active cho nội dung có độ trang trọng cao.

Song song, thị trường vật phẩm phong thủy thương mại tại Việt Nam đương đại có một mô hình lừa đảo tâm linh được báo chí chính thống ghi nhận rộng rãi (xem Applied Section §8 và Risk-Specific Editorial Rules Rule 6) — đây là bối cảnh thực tế lý giải vì sao Anti-Fear-Sales Standard của `DOMAIN_GUIDE.md` §9 là ranh giới bắt buộc, không phải lựa chọn phong cách.

## Schools

Ba trường phái/lineage được nghiên cứu trong packet này, theo đúng cách chia của `DOMAIN_GUIDE.md` §2:

- **Loan Đầu (Hình Thế phái / Form School)** — đọc hình thế vật lý địa hình (núi, sông, hướng dốc, hình dạng đất) để đánh giá nơi khí tụ/tán, không phụ thuộc la bàn hay thời gian.
- **Bát Trạch (Eight Mansions, nhánh Lý Khí)** — dựa số Quái Mệnh (Kua number) tính từ năm sinh + giới tính gia chủ; tĩnh theo đời người, gắn với người rồi áp cho nhà.
- **Huyền Không Phi Tinh (Flying Star, nhánh Lý Khí)** — dựa Vận xây/nhập trạch (chu kỳ 20 năm) + hướng tọa/hướng nhìn của nhà; động, thay đổi theo Vận và theo năm/tháng, gắn với nhà theo thời gian.

**Cảnh báo cấu trúc quan trọng nhất của toàn bộ packet:** Ba trường phái này là **ba hệ thống lý luận độc lập, không cùng một gốc**. Theo chính nguồn thực hành tiếng Việt khảo sát (phongthuyhuyenkhong.vn): "Bát trạch và Huyền không phi tinh vốn không cùng một gốc, làm sao có thể kết hợp với nhau?" Cùng một căn nhà có thể nhận được khuyến nghị khác nhau, thậm chí trái ngược, từ hai hệ thống Lý Khí này — đây là mâu thuẫn được chính giới thực hành thừa nhận, không phải suy diễn của kênh. Không nội dung nào phát sinh từ packet này được phép trộn hai hệ thành một "công thức đúng duy nhất" hoặc ngầm chọn một hệ làm chuẩn (xem Risk-Specific Editorial Rules Rule 1).

## Traditions

- **Primary tradition context:** Phong Thủy Trung Hoa cổ điển (Loan Đầu, Lý Khí/Bát Trạch, Lý Khí/Huyền Không Phi Tinh), tiếp biến vào văn hóa nhà ở Việt Nam đô thị và nông thôn đương đại.
- **Secondary tradition context:** nền Âm Dương – Ngũ Hành – Bát Quái dùng chung với nhánh Tử Vi Đẩu Số của cùng domain FS (xem `DOMAIN_GUIDE.md` §1); tín ngưỡng thờ cúng tổ tiên Việt Nam (bàn thờ gia tiên) như một lớp văn hóa/tâm linh dân gian song song, không thuần túy kỹ thuật Phong Thủy.

## Important Milestones

- Hình thành cặp phạm trù triết học Âm Dương (~thế kỷ 4 TCN, Trâu Diễn/Âm Dương gia), với gốc rễ có thể sớm hơn trong Kinh Dịch thời Tây Chu.
- Hệ thống hóa Ngũ Hành thành 5 phạm trù mạch lạc (thời Chiến Quốc, phái Hoàng Lão).
- Xác lập hai chu kỳ Tương Sinh/Tương Khắc — nội dung đồng thuận cao nhất, dùng làm nền cứng cho toàn bộ domain.
- Hình thành Bát Quái với hai bảng phương vị Tiên Thiên (Phục Hy, truyền thuyết) và Hậu Thiên (Văn Vương, truyền thuyết).
- Hệ thống hóa Loan Đầu, đặc biệt qua thời Đường (Dương Quân Tùng, truyền thuyết nghề nghiệp).
- Liên hệ biểu tượng Thái Cực Đồ với thời Tống (Chu Đôn Di) — còn tranh luận học thuật về nguồn gốc đồ họa chính xác.
- Phát triển hai lineage Lý Khí độc lập: Bát Trạch (Tam Hợp) và Huyền Không Phi Tinh (Tam Nguyên).
- Tiếp biến vào kiến trúc nhà truyền thống Việt Nam (tựa núi nhìn sông).
- Biến đổi đô thị hóa đương đại: dịch chuyển trọng tâm từ "chọn hướng đất" sang "hóa giải hướng nhà trong nội thất."
- Thương mại hóa vật phẩm phong thủy tại Việt Nam đương đại, kèm mô hình lừa đảo tâm linh được báo chí ghi nhận.

## Historical Debates

1. **Quy gán tác giả Bát Quái (Phục Hy/Văn Vương)** — truyền thuyết dân gian, không phải sử liệu xác thực; cần nêu "tương truyền", không khẳng định như sự kiện lịch sử.
2. **Nguồn gốc đồ họa Thái Cực Đồ** — liên hệ phổ biến với thời Tống/Chu Đôn Di nhưng nguồn gốc chính xác còn tranh luận học thuật; độ tin cậy trung bình, không khẳng định tuyệt đối.
3. **Tính xác thực trích dẫn Táng Thư/Quách Phác** — nguyên lý "khí gặp gió tán, gặp nước dừng" được lưu truyền rộng rãi trong giới thực hành nhưng việc xác thực văn bản gốc chưa qua chỉnh sửa qua các đời có độ tin cậy thấp hơn; chỉ nên diễn giải ý, ghi "tương truyền."
4. **Quan hệ Bát Trạch – Huyền Không Phi Tinh** — đây không phải một cuộc tranh luận học thuật trừu tượng mà là một mâu thuẫn thực hành được chính giới hành nghề xác nhận (xem Schools ở trên). Production rule bắt buộc: gọi tên trường phái mỗi khi phát biểu một quy tắc cụ thể, không bao giờ nói trường phái nào "đúng hơn."
5. **Bảng phương vị Tiên Thiên Bát Quái chi tiết** — có sai khác nhỏ giữa các nguồn tiếng Anh khảo sát (ví dụ vị trí Cấn/Đoài); cần một nguồn Kinh Dịch học thuật xác minh thêm trước khi dùng cho script có độ chi tiết cao. Bảng Hậu Thiên (dùng cho nhà ở) có độ đồng thuận cao hơn nhiều và an toàn hơn làm nội dung chính.

---

# Canonical Sources

## Nguồn nghiên cứu đầu vào (Primary Research Inputs)

| Source | Mô tả | Tier / Độ tin cậy | Hướng dẫn sử dụng |
|---|---|---|---|
| `SOURCES/RESEARCH_DRAFT_AM_DUONG_NGU_HANH.md` | Nền tảng Âm Dương & Ngũ Hành, gồm hai chu kỳ Tương Sinh/Tương Khắc, ứng dụng màu sắc/hướng theo mệnh, liên hệ Tử Vi (Cục) | Tier 1 cho hai chu kỳ Tương Sinh/Tương Khắc (xác minh chéo ≥3 nguồn độc lập); Tier 3 cho ứng dụng màu/hướng theo mệnh và liên hệ Tử Vi | Dùng làm nền cứng (hard reference) cho mọi nội dung Ngũ Hành trong domain; phần ứng dụng Tử Vi cần gắn nhãn trường phái/"theo cách luận truyền thống" |
| `SOURCES/RESEARCH_DRAFT_BAT_QUAI_TRUONG_PHAI.md` | Bát Quái (Tiên Thiên/Hậu Thiên), Loan Đầu, Bát Trạch, Huyền Không Phi Tinh | Tier 1 cho cấu trúc Bát Quái Hậu Thiên; Tier 3 cho chi tiết ứng dụng từng trường phái; chưa qua Domain QA | Nguồn chính cho Core Concepts Map §Bát Quái, §Loan Đầu, §Bát Trạch, §Huyền Không Phi Tinh |
| `SOURCES/RESEARCH_DRAFT_UNG_DUNG_NHA_O.md` | Ứng dụng thực tế: hướng nhà, cửa, phòng khách, phòng ngủ, bàn thờ, bếp, cây phong thủy, vật phẩm, văn phòng, bối cảnh lừa đảo tâm linh | Toàn bộ Tier 3 (thương mại/dân gian phổ biến, đối chiếu ≥3 nguồn/mục), cộng thêm báo chí chính thống (mục lừa đảo) và 1 nguồn phản biện văn hóa VnExpress (gương bát quái) | Nguồn chính cho toàn bộ Applied Section; đọc kèm "Standing flag" của chính research draft này về thiên kiến thương mại của nguồn |

## Source Priority Hierarchy (tái hiện từ `DOMAIN_GUIDE.md` §3)

| Tier | Loại nguồn | Ví dụ trong packet này |
|---|---|---|
| 1 | Quy tắc cấu trúc cổ điển được hầu hết trường phái đồng thuận | Cấu trúc 12 cung (thuộc Tử Vi, không dùng ở đây), chu kỳ Tương Sinh/Tương Khắc Ngũ Hành, 8 quẻ Bát Quái |
| 2 | Quy tắc theo trường phái/lineage cụ thể, gắn nhãn rõ | Kua number/nhóm hướng của Bát Trạch; Vận/Phi Tinh của Huyền Không |
| 3 | Thực hành phổ biến đương đại tiếng Việt (sách, trang thực hành), đối chiếu ≥2-3 nguồn độc lập | Phần lớn Applied Section (hướng nhà, cửa, phòng, bàn thờ, bếp, cây, vật phẩm) |
| 4 | Học thuật/lịch sử về nguồn gốc và lịch sử xã hội | Dùng cho lớp lịch sử-khung (Historical Background) — hiện **chưa có nguồn tier 4 nào được truy cập** trong 3 research draft gốc, xem Khoảng trống nguồn bên dưới |

## Khoảng trống nguồn (Known Gaps)

- Không có nguồn academic/dân tộc học độc lập nào được truy cập trong cả 3 research draft — toàn bộ nội dung ứng dụng nhà ở dựa trên tier 3. Đây là mức trần độ tin cậy hiện có cho lãnh thổ nội dung này (không có văn bản kinh điển duy nhất, theo `DOMAIN_GUIDE.md` §2).
- Bàn thờ gia tiên (Applied Section §5): chưa có nguồn dân tộc học Việt Nam độc lập — chỉ dựa nguồn thương mại/dân gian phổ biến; khuyến nghị bổ sung trước khi dùng cho nội dung có độ trang trọng/độ nhạy cảm cao.
- Bảng phương vị Tiên Thiên Bát Quái chi tiết: cần một nguồn Kinh Dịch học thuật xác minh thêm (xem Historical Debates mục 5).
- Quy đổi âm lịch/dương lịch trong công thức tính Kua number (Bát Trạch): một số nguồn nhấn mạnh cần quy đổi sang năm âm lịch (đặc biệt người sinh gần Tết/lập xuân), một số nguồn phổ thông bỏ qua chi tiết này — cần nguồn Tử Vi/lịch pháp xác minh thêm, không khẳng định chắc trong script chi tiết.
- Cơ chế số của Ngũ Hành Cục trong Tử Vi (2-3-4-5-6): nguồn gốc chính xác chưa có lời giải thích thống nhất, dứt khoát — đánh dấu độ tin cậy thấp/còn tranh luận.
- Hướng bàn thờ có bắt buộc trùng hướng nhà hay không: single-sourced/chưa đủ cross-check — không đưa vào kịch bản như quy tắc chắc chắn.
- Danh sách cây phong thủy cụ thể theo mệnh Hỏa: nguồn không hoàn toàn nhất quán — trình bày nguyên lý chọn màu/hành là chính, danh sách cây là ví dụ minh họa, không phải danh sách "chuẩn."

## Ghi chú thiên kiến nguồn (áp dụng cho toàn bộ Applied Section)

`RESEARCH_DRAFT_UNG_DUNG_NHA_O.md` tự gắn cờ ngay từ đầu: đa số nguồn tiếng Việt sẵn có về ứng dụng nhà ở là nguồn thương mại (cửa hàng nội thất, cửa hàng vật phẩm phong thủy, công ty thiết kế nội thất). Động cơ kinh doanh của các nguồn này khiến ngôn ngữ phóng đại và hù dọa nhẹ là **giọng điệu mặc định của chất liệu nguồn**, không phải ngoại lệ. Toàn bộ nội dung trong packet này đã được paraphrase để loại bỏ ngôn ngữ cam kết ("chắc chắn giàu," "hút tiền vào như nước," "rước tài lộc tức thì"), nhưng các mục "Production cautions" trong Applied Section đánh dấu nơi mà **bản thân tuyên bố gốc**, chứ không chỉ cách diễn đạt, có nguy cơ vượt ranh giới `DOMAIN_GUIDE.md` §6 (tài chính) hoặc §9 (Anti-Fear-Sales).

---

# Core Concepts Map

Bảy khái niệm nền tảng dưới đây là "bảng chữ cái chung" của toàn bộ domain Phong Thủy (và một phần nền cho Tử Vi). Mỗi mục theo cấu trúc: Knowledge function / Primary concepts / Narrative detail / Script-ready material / Production cautions — mô phỏng đúng định dạng Chapter-Level Knowledge Map đã dùng ở `KP_BUD_001`.

## Âm Dương

### Knowledge function

Âm Dương là nguyên lý cân bằng-bổ sung nền tảng nhất, dùng để giải thích mọi cặp đối lập trong Phong Thủy (sáng/tối, động/tĩnh, Dương Trạch/Âm Trạch) mà không quy giản thành thiện/ác. Đây là điểm khởi đầu tự nhiên cho bất kỳ chuỗi nội dung nào về Phong Thủy hoặc Tử Vi.

### Primary concepts

- Nguồn gốc ngôn ngữ: mặt tối/mặt sáng sườn đồi.
- Triết lý Âm Dương gia (Trâu Diễn, ~thế kỷ 4 TCN) và Kinh Dịch (Tây Chu).
- Quy gán truyền thuyết Phục Hy — không phải sử liệu.
- Bản chất bổ sung-phụ thuộc lẫn nhau, không đối kháng triệt tiêu ("trong Âm có mầm Dương, trong Dương có mầm Âm").
- Thái Cực Đồ — biểu tượng đồ họa xuất hiện muộn hơn khái niệm triết học (liên hệ thời Tống/Chu Đôn Di, độ tin cậy trung bình).
- Ứng dụng Phong Thủy: cân bằng Dương khí/Âm khí trong Dương Trạch (nhà ở) — ánh sáng, màu sắc, công năng phòng.
- Ứng dụng Tử Vi (liên hệ, không đi sâu ở packet này): phân loại sao Nam Đẩu/Bắc Đẩu, khái niệm "Âm Dương thuận lý/nghịch lý" — độ tin cậy trung bình, mang tính trường phái.

### Narrative detail

Âm Dương ra đời như một cặp hình ảnh cụ thể (sườn núi có mặt sáng mặt tối) trước khi trở thành phạm trù triết học trừu tượng khoảng thế kỷ 4 TCN. Kinh Dịch hệ thống hóa nó qua hào âm/hào dương và mệnh đề "vạn vật đều ôm một Thái Cực — Thái Cực sinh Lưỡng Nghi." Về bản chất, Dương mang đặc tính chủ động/mở rộng/sáng/nóng/cứng; Âm mang đặc tính thụ động/thu liễm/tối/lạnh/mềm — nhưng không có cực nào tồn tại thuần túy độc lập; mỗi cực luôn mang mầm của cực kia và có thể chuyển hóa khi đạt cực điểm ("vật cực tất phản"). Ứng dụng vào Phong Thủy nhà ở: một không gian sống tốt cần Dương khí nhỉnh hơn Âm khí nhưng không lấn át — nhà ở (Dương Trạch) cần đủ ánh sáng, sự sống động, luồng khí lưu thông nhưng vẫn cần yếu tố Âm để tạo sự yên tĩnh nghỉ ngơi, khác với mộ phần (Âm Trạch).

### Script-ready material

- Thái Cực Đồ — biểu tượng hình ảnh trực quan nhất cho mọi đoạn nói về Âm Dương.
- Hình ảnh sườn núi sáng/tối (gốc nghĩa chữ) — mộc mạc, dễ hình dung, tránh trừu tượng hóa quá sớm.
- Cặp hình ảnh ánh sáng/bóng tối, lửa/nước — ẩn dụ cho tính bổ sung chứ không đối kháng.
- Vòng xoáy chuyển hóa (một cực lên đỉnh sinh mầm cực kia) — minh họa "vật cực tất phản", tránh vẽ Âm Dương như hai phe cố định.

### Production cautions

- **Tránh tuyệt đối:** minh họa Âm Dương như "tốt vs xấu" hay "thiện vs ác" — đây là hiểu sai phổ biến, đi ngược tinh thần phi nhị nguyên đạo đức của khái niệm gốc.
- Quy gán Phục Hy phải nêu rõ "tương truyền", không trình bày như sự kiện lịch sử đã kiểm chứng (đúng tinh thần xử lý Trần Đoàn/Tử Vi ở `DOMAIN_GUIDE.md` §2).
- Thái Cực Đồ: độ tin cậy trung bình cho nguồn gốc đồ họa chính xác — không khẳng định tuyệt đối mốc thời gian.
- Phần liên hệ Tử Vi (Âm Dương thuận/nghịch lý, Nam Đẩu/Bắc Đẩu) phải gắn nhãn "theo một số cách luận truyền thống," không trình bày như quy tắc duy nhất (`DOMAIN_GUIDE.md` §3, §5).

## Ngũ Hành

### Knowledge function

Ngũ Hành là công cụ phân loại-chuyển hóa dùng xuyên suốt mọi ứng dụng Phong Thủy (màu sắc, vật liệu, hướng nhà theo mệnh) và là nền tảng bắt buộc phải chính xác trước khi xây bất kỳ nội dung ứng dụng nào — sai một hành trong chu kỳ Tương Sinh/Tương Khắc sẽ làm sai toàn bộ logic tư vấn màu sắc/hướng nhà ở tầng ứng dụng.

### Primary concepts

- Năm hành: Mộc, Hỏa, Thổ, Kim, Thủy — là 5 giai đoạn/tính chất chuyển hóa, không phải 5 "vật chất" tĩnh.
- Chu kỳ Tương Sinh: Mộc sinh Hỏa → Hỏa sinh Thổ → Thổ sinh Kim → Kim sinh Thủy → Thủy sinh Mộc (Tier 1, xác minh ≥3 nguồn độc lập, không mâu thuẫn).
- Chu kỳ Tương Khắc: Mộc khắc Thổ → Thổ khắc Thủy → Thủy khắc Hỏa → Hỏa khắc Kim → Kim khắc Mộc (Tier 1, cùng mức xác minh).
- Ứng dụng chọn màu/hướng theo mệnh gia chủ (Kim/Mộc/Thủy/Hỏa/Thổ) — Tier 3, thực hành phổ biến đương đại.
- Ứng dụng Tử Vi qua khái niệm "Cục" (Ngũ Hành Cục) — nguồn gốc số 2-3-4-5-6 gắn với mỗi Cục chưa có lời giải thích thống nhất, độ tin cậy thấp.

### Narrative detail

Ngũ Hành hình thành như hệ thống mạch lạc vào thời Chiến Quốc, hệ thống hóa bởi phái Hoàng Lão, xuất hiện trong Hoàng Đế Nội Kinh. Mỗi hành mang một đặc tính biểu trưng: Mộc (sinh trưởng, mùa Xuân, Đông, xanh lá), Hỏa (nhiệt, năng lượng đi lên, mùa Hè, Nam, đỏ), Thổ (nuôi dưỡng, ổn định, trung tâm, vàng), Kim (thu liễm, sắc bén, mùa Thu, Tây, trắng), Thủy (lưu chuyển, tàng trữ, mùa Đông, Bắc, đen/xanh dương đậm). Hai chu kỳ Tương Sinh (mỗi hành nuôi dưỡng hành kế tiếp) và Tương Khắc (mỗi hành chế ngự một hành khác) tạo thành cấu trúc vận hành cốt lõi, được diễn giải qua các ẩn dụ tự nhiên cụ thể (cây khô nuôi lửa, tro tàn hóa đất, đất sinh khoáng, kim loại nóng chảy/ngưng tụ hơi nước, nước tưới cây — cho Tương Sinh; rễ cây hút cạn đất, đất chặn dòng nước, nước dập lửa, lửa nung chảy kim loại, kim loại rèn dao chặt cây — cho Tương Khắc). Trong Phong Thủy, nguyên tắc chọn màu/vật liệu/hướng theo mệnh gia chủ dựa trực tiếp trên hai chu kỳ này: chọn màu của hành "sinh" ra mệnh mình hoặc màu bản mệnh, tránh màu của hành "khắc" mệnh mình.

### Script-ready material

- Vòng tròn Ngũ Hành với 5 mũi tên ngoài (Tương Sinh) và ngôi sao 5 cánh bên trong (Tương Khắc) — sơ đồ nền kinh điển cho mọi đoạn giải thích.
- Chuỗi ẩn dụ tự nhiên Tương Sinh và Tương Khắc (liệt kê ở Narrative detail) — sẵn sàng dùng làm narration.
- Bảng màu/phương hướng gắn mỗi hành — hữu ích cho thiết kế đồ họa nhất quán xuyên suốt các tập có Ngũ Hành.

### Production cautions

- Giữ tinh thần "5 giai đoạn/tính chất chuyển hóa" — tránh gắn Ngũ Hành cứng nhắc như "5 loại vật chất hóa học."
- Hai chu kỳ Tương Sinh/Tương Khắc là dữ liệu an toàn để làm nền cứng — có thể trình bày chắc chắn.
- Ứng dụng màu sắc/hướng nhà theo mệnh: độ tin cậy trung bình (Tier 3) — không đóng khung như cam kết bảo đảm tài lộc/may mắn ("dùng màu này chắc chắn giàu"), đúng Anti-Fear-Sales Standard §9.
- Cơ chế số Ngũ Hành Cục trong Tử Vi: độ tin cậy thấp/còn tranh luận — không khẳng định một cách lý giải duy nhất là "đúng."

## Bát Quái

### Knowledge function

Bát Quái là "bảng chữ cái" biểu tượng chung mà hầu hết các trường phái Phong Thủy — kể cả Bát Trạch và Huyền Không vốn khác nhau về phương pháp — đều dùng làm ngôn ngữ nền tảng. Nội dung mở đầu tự nhiên trước khi đi vào từng trường phái cụ thể.

### Primary concepts

- Tám quẻ: Càn (☰), Khôn (☷), Chấn (☳), Tốn (☴), Khảm (☵), Ly (☲), Cấn (☶), Đoài (☱) — mỗi quẻ gồm 3 hào Âm/Dương.
- Hai bảng sắp xếp: Tiên Thiên Bát Quái (tương truyền Phục Hy) và Hậu Thiên Bát Quái (tương truyền Văn Vương) — mục đích khác nhau, không phải một đúng một sai.
- Bảng Hậu Thiên (ngũ hành + phương vị + vai trò gia đình từng quẻ) là hệ dùng cho thực hành nhà ở (Bát Trạch, Huyền Không, la bàn phổ thông) — Tier 1, độ tin cậy cao.
- Bảng Tiên Thiên dùng nhiều trong triết học Kinh Dịch, Mai Hoa Dịch Số, một số ứng dụng Âm Trạch — độ tin cậy trung bình cho vị trí chi tiết (sai khác nhỏ giữa nguồn).

### Narrative detail

Bát Quái là tám tổ hợp ký hiệu 3 hào biểu trưng cho các hiện tượng/lực cơ bản của tự nhiên. Bảng Hậu Thiên — hệ dùng cho nhà ở — gán mỗi quẻ với một ngũ hành, một phương vị, và một vai trò trong gia đình: Càn (Kim, Tây Bắc, Cha), Khôn (Thổ, Tây Nam, Mẹ), Chấn (Mộc, Đông, Trưởng nam), Tốn (Mộc, Đông Nam, Trưởng nữ), Khảm (Thủy, Bắc, Trung nam), Ly (Hỏa, Nam, Trung nữ), Cấn (Thổ, Đông Bắc, Thiếu nam), Đoài (Kim, Tây, Thiếu nữ). Bảng Tiên Thiên khác về vị trí (ví dụ Càn ở Nam thay vì Tây Bắc, Khôn ở Bắc thay vì Tây Nam, Ly ở Đông thay vì Nam, Khảm ở Tây thay vì Bắc) và mang tính chất triết lý/đối xứng cao hơn là thực hành phương vị nhà ở. Việc phân biệt rạch ròi hai bảng này là một điểm giáo dục có giá trị, vì nhiều nguồn tiếng Việt phổ thông nhầm lẫn hai bảng phương vị.

### Script-ready material

- Hình ảnh gia đình (cha/mẹ/trưởng nam/thiếu nữ...) làm ẩn dụ dễ nhớ cho 8 quẻ Hậu Thiên.
- "Twist" giáo dục: giải thích vì sao có 2 Bát Quái mà không lẫn — nội dung ít kênh Việt làm rõ, giúp khán giả tránh sai lầm phổ biến.

### Production cautions

- **Không** trình bày Tiên Thiên và Hậu Thiên như chỉ có một bảng "đúng" — phải nói rõ đây là hai hệ sắp xếp có mục đích khác nhau.
- **Không** khẳng định ngũ hành/phương vị Bát Quái là "khoa học đã chứng minh" (`DOMAIN_GUIDE.md` §12).
- Bảng phương vị Tiên Thiên chi tiết: gắn nhãn medium-confidence, không dùng làm câu khẳng định chắc nịch.
- Quy gán Phục Hy/Văn Vương: luôn nêu "tương truyền", không phải sử liệu xác thực.

## Khí (Qi/Chi — Traditional Environmental Flow, Not Physics Energy)

### Knowledge function

"Khí" là thuật ngữ kết nối mà mọi trường phái trong domain này đều mặc định dùng nhưng chưa từng được định nghĩa riêng — packet này đã dùng từ "khí" rải rác hơn 30 lần xuyên suốt Core Concepts Map và Applied Section (Âm Dương: "cân bằng Dương khí/Âm khí"; Loan Đầu: "khí theo gió mà tán, gặp nước thì dừng," "long mạch," "minh đường tụ khí"; Bát Trạch: "khí" người ở hài hòa với hướng nhà; Applied Section: "miệng khí" của cửa chính, nguyên tắc "không thông phong," "hút vượng khí") mà không có một mục hợp nhất giải thích khái niệm gốc. Mục này hợp nhất các mảnh rải rác đó thành một định nghĩa thống nhất, không thêm quy tắc mới, không mâu thuẫn với bất kỳ chỗ nào đã dùng "khí" trước đó trong packet. Đây cũng là ranh giới khoa học quan trọng nhất của toàn bộ packet — tương ứng đúng "Hiểu Lầm Trung Tâm" mà `SB_FS_001` gán cho Episode 4: nhầm ẩn dụ môi trường-cảm nhận truyền thống với một khái niệm năng lượng vật lý đã được khoa học đo lường.

### Primary concepts

- Nghĩa gốc rộng hơn phong thủy: "khí" (氣) trong tư tưởng Trung Hoa cổ là phạm trù triết học chỉ "hơi thở," "sinh lực," hoặc nguyên lý vận hành-chuyển hóa của vạn vật — xuất hiện trong y học cổ truyền, dưỡng sinh, triết học Đạo giáo trước khi được vay mượn riêng vào lý luận chọn đất của Phong Thủy; không phải một khái niệm phát minh riêng cho phong thủy.
- Nguyên lý gốc của Loan Đầu (đã nêu ở mục Loan Đầu, độ tin cậy trung bình cho lưu truyền, tương truyền dẫn từ Táng Thư): "khí gặp gió thì tán, gặp nước thì dừng" — khí được mô tả như một luồng vô hình đi theo địa hình, gió mạnh làm khí phát tán/không tụ được, nước và địa hình bao bọc (minh đường, tựa sơn hướng thủy) giữ khí lại.
- Sinh khí (khí tốt — tương ứng cảm nhận thoáng đãng, hài hòa, nuôi dưỡng) đối lập Tà khí/Sát khí (khí xấu — tương ứng cảm nhận bí bách, dồn nén, góc cạnh sắc nhọn) — cặp phân loại phổ biến trong hầu hết nguồn thực hành khảo sát, luôn ở mức mô tả-cảm nhận, không kèm định nghĩa vật lý.
- Vai trò khác nhau theo từng trường phái — không được trộn thành một cơ chế duy nhất (Rule 1):
  - **Loan Đầu:** khí tụ/tán theo địa hình vật lý — tĩnh về nguyên tắc, đọc bằng địa thế thực tế (núi, nước, hướng dốc).
  - **Bát Trạch:** khí là sự tương hợp giữa hướng nhà/cửa và quái mệnh gia chủ — tĩnh theo đời người, gắn với người rồi áp cho nhà (đã nêu ở mục Bát Trạch).
  - **Huyền Không Phi Tinh:** khí biến đổi theo Vận và Phi Tinh — động, gắn với nhà và thời gian, "khí vượng" của một cung có thể đổi qua các Vận khác nhau (đã nêu ở mục Huyền Không).
- Đại diện hiện đại gần nhất với ý tưởng "khí lưu thông" trong ứng dụng nhà ở: thông gió tự nhiên và ánh sáng — đây là một phép loại suy ở lớp modern-reflective (`DOMAIN_GUIDE.md` §10), không phải bằng chứng khoa học xác nhận khái niệm khí cổ điển (xem Production cautions).

### Narrative detail

Về ngôn ngữ, "khí" trong tư tưởng Trung Hoa cổ rộng hơn nhiều so với phong thủy đơn thuần — nó là một phạm trù triết học phổ quát trước khi được vay mượn vào lý luận chọn đất. Trong khuôn khổ Loan Đầu, nhánh cổ nhất và trực quan nhất, khí được mô tả bằng chính ẩn dụ tạo nên tên gọi "Phong Thủy": gặp gió mạnh thì "tán" (phát tán, không tụ được), gặp nước thì "dừng" (tụ lại) — nên địa thế lý tưởng là nơi có chỗ dựa chắn gió phía sau (Huyền Vũ) và nước/không gian mở phía trước (Chu Tước, minh đường) để giữ khí lại, đúng nguyên lý "tựa sơn hướng thủy" đã nêu ở mục Loan Đầu. Sang hai nhánh Lý Khí, khí không còn được mô tả trực tiếp bằng hình ảnh gió/nước cụ thể nữa mà trở thành một biến trừu tượng hơn: Bát Trạch gắn khí với sự tương hợp giữa hướng và mệnh chủ (tĩnh, không đổi theo thời gian); Huyền Không Phi Tinh gắn khí với Vận và Phi Tinh (động, biến đổi theo chu kỳ 20 năm và theo năm/tháng) — đúng đối lập "tĩnh/động" đã dựng ở mục so sánh hai trường phái. Điểm mấu chốt xuyên suốt cả ba cách dùng: "khí" luôn là một khái niệm mô tả-ẩn dụ về môi trường và cảm nhận không gian (thoáng/bí, mở/đóng, có chỗ dựa/trống trải) mà truyền thống dùng để giải thích trải nghiệm sống trong một không gian, được xác nhận nhất quán qua đối chiếu nhiều nguồn thực hành phong thủy độc lập cả tiếng Việt (ví dụ nguồn dân gian phổ thông về "sinh khí/tà khí," về nguyên lý "khí gặp gió tán, gặp nước dừng") lẫn tiếng Anh (mô tả khí như "vital life force"/"transformative energy flow" gắn với địa hình và hướng la bàn). Điều này khác về bản chất với khái niệm "năng lượng" (energy) trong vật lý hiện đại — một đại lượng đo được bằng đơn vị cụ thể (joule) và tuân theo các định luật vật lý đã kiểm chứng qua thực nghiệm độc lập, lặp lại được. Đối chiếu thêm nguồn học thuật/phê phán phong thủy cho thấy khí chưa từng được đo lường hay xác nhận tồn tại qua bất kỳ thí nghiệm khoa học độc lập nào — đây là cơ sở cho khẳng định "chưa được khoa học chứng minh" mà `DOMAIN_GUIDE.md` §12 yêu cầu. Một khảo sát nguồn phổ thông tiếng Việt về kiến trúc còn cho thấy chính nguồn phổ thông cũng dễ nhòe ranh giới này — một số bài viết lý giải nguyên tắc thông gió dân gian bằng cơ chế vật lý thực (đối lưu không khí, chênh lệch áp suất) rồi ngầm coi đó là "giải thích khoa học cho khí," trong khi thực chất đây chỉ là hai hiện tượng khác nhau được đặt cạnh nhau vì cùng liên quan đến luồng không khí — càng là lý do cần tách bạch rõ khi kịch bản hóa Episode 4.

### Script-ready material

- Ẩn dụ luồng không khí trong nhà: phòng có hai cửa đối diện mở toang tạo gió lùa mạnh (khí "tán") vs. phòng kín bưng không cửa sổ (khí "tù đọng," không lưu thông) vs. phòng có cửa sổ một bên với luồng gió vừa phải, ánh sáng dịu (khí "tụ," "sinh khí") — cầu nối trực quan, dễ hình dung sang lớp modern-reflective (thông gió/ánh sáng) mà không cần khẳng định khoa học.
- Hình ảnh núi chắn gió sau lưng, mặt hồ tĩnh lặng phía trước (đã dùng ở mục Loan Đầu) — dùng lại đúng hình ảnh gốc thay vì phát minh phép ẩn dụ mới, giữ nhất quán xuyên suốt series.
- Đối lập song song "khí tĩnh gắn với người" (Bát Trạch) và "khí động gắn với thời gian/căn nhà" (Huyền Không) — tái dùng khung "hai cách nhìn khác nhau" đã có ở mục Huyền Không, giúp Episode 4 gieo hạt cho Episode 15-16.
- Câu hỏi mở đầu tập gợi ý: "Khí" là năng lượng huyền bí hay chỉ là cách người xưa mô tả một không gian dễ chịu để sống? — đúng Core Question đã định trong `SB_FS_001` Ep004.

### Production cautions

- **Cấm tuyệt đối (ranh giới an toàn quan trọng nhất của mục này):** không khẳng định hoặc ngụ ý Khí là một dạng năng lượng vật lý đã được khoa học chứng minh; không nói khí "tương đương," "chính là," hay "được giải thích bởi" điện từ trường, nhiệt động lực học, hay bất kỳ đại lượng vật lý đo được nào. **Không dùng cụm "đo được khí," "khoa học đã đo được khí," hay "thiết bị phát hiện khí" như một tuyên bố khoa học xác thực** — đúng `DOMAIN_GUIDE.md` §12 ("Never present Phong Thủy... as scientifically proven"). Đây chính là Hiểu Lầm Trung Tâm mà Episode 4 được thiết kế để tháo gỡ theo `SB_FS_001`.
- Khi liên hệ "khí lưu thông" với thông gió/ánh sáng nhà ở hiện đại (lớp modern-reflective, §10), chỉ được trình bày đây là "phép loại suy dễ hình dung nhất" hoặc "điểm gần gũi nhất với trực giác không gian sống hiện đại" — **không** nói ngược lại rằng khoa học thông gió/đối lưu không khí "chứng minh" khí có thật, và **không** nói khí "chính là" luồng không khí vật lý. Đây là hai khái niệm khác nhau được đặt cạnh nhau để dễ hiểu, không phải một phép quy đổi hay một sự đồng nhất.
- Không tự sáng chế cơ chế vận hành của khí (ví dụ không nói khí "di chuyển qua trường điện từ của Trái Đất" hoặc dùng ngôn ngữ giả-khoa học nghe có vẻ chính xác) — không nguồn nào khảo sát cho packet này (Việt lẫn Anh) đưa ra cơ chế vật lý đã kiểm chứng; mọi mô tả "cơ chế" trong nguồn phổ thông là ẩn dụ, không phải giải thích khoa học đã xác nhận.
- Không trộn cách hiểu khí của Loan Đầu (tĩnh, theo địa hình), Bát Trạch (tĩnh, theo mệnh chủ) và Huyền Không (động, theo Vận) thành một cơ chế duy nhất — luôn gọi tên trường phái khi nói "khí" trong một ngữ cảnh cụ thể (Rule 1).
- Sinh khí/Tà khí: trình bày như cách phân loại truyền thống về cảm nhận không gian (thoáng-hài hòa vs. bí bách-sắc nhọn), không suy diễn thành cơ chế gây bệnh/tai họa cụ thể có thể kiểm chứng y khoa (Rule 5, ranh giới §7).
- Nhãn độ tin cậy: cách truyền thống mô tả khí (ẩn dụ gió/nước, sinh khí/tà khí, vai trò khác nhau theo trường phái) đối chiếu nhất quán qua ≥3 nguồn độc lập (thực hành phổ thông tiếng Việt, thực hành phổ thông tiếng Anh, nguồn học thuật/phê phán phong thủy) — mức tin cậy trung bình-cao cho phần "cách truyền thống mô tả khí." Bất kỳ tuyên bố nào rằng khí là hiện tượng vật lý đã được khoa học xác nhận có mức tin cậy: **không có nguồn nào xác nhận** — phải bị loại khỏi kịch bản, không chỉ gắn nhãn thấp.

## Loan Đầu (Hình Thế phái)

### Knowledge function

Loan Đầu là trường phái đọc hình thế vật lý địa hình — nền tảng lịch sử của toàn bộ Phong Thủy trước khi Lý Khí (la bàn/thời gian) phát triển. Đây là chủ đề dễ hình ảnh hóa nhất trong bốn nhánh trường phái, phù hợp mở đầu một chuỗi nội dung về "đọc không gian sống."

### Primary concepts

- Nguyên lý gốc: khí theo gió mà tán, gặp nước thì dừng (tương truyền dẫn từ Táng Thư/Quách Phác — độ tin cậy trung bình cho lưu truyền, thấp hơn cho xác thực văn bản gốc).
- Long mạch — mạch núi/địa hình ví như rồng, nơi khí lưu chuyển.
- Minh đường — khoảng không gian mở, thoáng phía trước nhà/mộ, nơi khí được cho là tụ lại.
- Tứ Tượng (Tứ Linh): Huyền Vũ (Thủy, sau lưng/Bắc, chỗ dựa), Chu Tước (Hỏa, trước mặt/Nam, không gian mở), Thanh Long (Mộc, trái/Đông, nên cao/vững hơn), Bạch Hổ (Kim, phải/Tây, nên thấp/êm hơn).
- Dương Quân Tùng (Đường dynasty) — tương truyền người hệ thống hóa mạnh Loan Đầu, độ tin cậy trung bình (truyền thuyết nghề nghiệp).

### Narrative detail

Loan Đầu là trường phái cổ nhất, đọc núi, sông, hướng dốc, hình dạng đất để đánh giá nơi khí tụ lại hay tán đi, trước khi tính đến hướng la bàn hay thời gian. Địa thế lý tưởng là nơi được "bao bọc": có chỗ dựa phía sau (Huyền Vũ), không gian mở phía trước thường có nước/minh đường tụ khí (Chu Tước), và hai bên có thế cân bằng nhưng không đối xứng tuyệt đối (Thanh Long bên trái nên vững hơn Bạch Hổ bên phải một chút). Bốn vị trí hộ vệ này (Tứ Tượng/Tứ Linh) là khung hình ảnh kinh điển nhất của Loan Đầu, và về sau được mượn lại trong nhiều ứng dụng nhà ở khác (ví dụ nguyên lý "tựa sơn hướng thủy" cho sofa, giường, bàn làm việc — xem Applied Section).

### Script-ready material

- Animation địa hình: núi sau lưng, nước phía trước, "tay ngai" hai bên — dễ hình ảnh hóa nhất trong 4 chủ đề trường phái.
- Liên hệ kiến trúc nhà truyền thống Việt Nam (tựa núi/gò, nhìn ra ao/sông) — lớp cultural/historical, không cần khẳng định hiệu quả.
- Tứ Tượng nhân cách hóa (rồng xanh, hổ trắng, phượng đỏ, rùa-rắn đen) — hình ảnh mạnh sẵn có cho video.

### Production cautions

- Loan Đầu đọc hình thế thực tế — **không** biến thành khẳng định phong thủy "đảm bảo" tài lộc/sức khỏe khi làm theo (`DOMAIN_GUIDE.md` §6-7, §9).
- Không gán trích dẫn Táng Thư là nguyên văn chính xác nếu chưa đối chiếu bản dịch gốc — chỉ diễn giải ý, ghi rõ "tương truyền."
- Tứ Tượng không nên bị đơn giản hóa thành quy tắc cứng ("phải trồng cây bên phải, để trống bên trái") — giữ tinh thần "nguyên lý nền tảng, ứng dụng cần địa hình cụ thể."

## Bát Trạch (Eight Mansions)

### Knowledge function

Bát Trạch là nhánh Lý Khí phổ biến nhất trong ứng dụng nhà ở đại chúng — công thức tính Kua number có thể minh họa bằng ví dụ hư cấu, phù hợp nội dung "công thức có thể học được" nhưng đòi hỏi kỷ luật biên tập nghiêm ngặt nhất về ranh giới cá nhân hóa (`DOMAIN_GUIDE.md` §4).

### Primary concepts

- Số Quái Mệnh (Kua number) tính từ năm sinh + giới tính gia chủ.
- Phân nhóm Đông Tứ Mệnh (Kua 1, 3, 4, 9 — quẻ Khảm, Chấn, Tốn, Ly; hướng tốt Bắc, Đông, Đông Nam, Nam) và Tây Tứ Mệnh (Kua 2, 6, 7, 8 — quẻ Khôn, Càn, Đoài, Cấn; hướng tốt Tây Nam, Tây Bắc, Tây, Đông Bắc).
- Công thức tính Kua: tổng 2 số cuối năm sinh rút gọn thành 1 chữ số (x); trước 2000: Nam = 10−x, Nữ = 5+x; từ 2000: Nam = 9−x, Nữ = 6+x; kết quả 0 → 9; kết quả 5 → Nam 2/Nữ 8.
- Gốc lineage: theo nguồn thực hành tiếng Việt khảo sát, Bát Trạch gắn với dòng Tam Hợp (khác dòng Tam Nguyên của Huyền Không).

### Narrative detail

Bát Trạch chia người và nhà thành hai nhóm — Đông Tứ Mệnh/Trạch và Tây Tứ Mệnh/Trạch — mỗi nhóm có 4 hướng tốt và 4 hướng xấu, dựa trên việc quẻ Bát Quái của hướng đó cùng nhóm hay khác nhóm với quẻ mệnh gia chủ. Công thức tính Kua number phần lớn khớp giữa các nguồn khảo sát, nhưng có hai điểm cần lưu ý: (1) một số nguồn nhấn mạnh cần quy đổi năm sinh sang âm lịch, đặc biệt với người sinh gần Tết/lập xuân — điểm này cần một nguồn Tử Vi/lịch pháp xác minh thêm; (2) mốc "năm 2000" trong công thức liên quan đến hệ số điều chỉnh la bàn 24 sơn hướng đổi sau khi bước sang Vận 8 (2004) trong hệ Huyền Không — các nguồn phổ thông diễn giải mốc này còn khác nhau đôi chút, nên trình bày như quy ước phổ biến, không đi sâu lý giải thiên văn trong nội dung phổ thông.

### Script-ready material

- Ví dụ hư cấu/lịch sử minh họa cách tính Kua number — **không** mời khán giả tự tính rồi channel "phán" hộ.
- Sơ đồ trực quan "người Đông Tứ Mệnh hợp hướng nào, người Tây Tứ Mệnh hợp hướng nào" — dùng khung câu "theo Bát Trạch truyền thống, người mang mệnh quái X thường được xem là hợp hướng Y."

### Production cautions

- **Đây là hệ thống ước tính dựa trên năm sinh — không phải phép tính "định mệnh" chắc chắn.** Không dùng ngôn ngữ "bạn sẽ..." (`DOMAIN_GUIDE.md` §5).
- **Không trộn Bát Trạch với Huyền Không Phi Tinh thành một "công thức đúng duy nhất."** Luôn nêu rõ đây là hai trường phái riêng, mỗi trường phái có logic riêng — không nói trường phái nào "đúng hơn" hay tự sáng chế cách hòa giải hai hệ.
- Kua number không được biến thành "chỉ số định mệnh cá nhân" gắn với tài chính/sức khỏe (`DOMAIN_GUIDE.md` §6-7).
- Quy đổi âm lịch: gắn nhãn "cần xác minh thêm", không khẳng định chắc trong script chi tiết.

## Huyền Không Phi Tinh (Flying Star)

### Knowledge function

Huyền Không Phi Tinh là nhánh Lý Khí phức tạp nhất, phù hợp làm nội dung "giải thích khái niệm" (why/what) hơn là "how-to" chi tiết — rủi ro đơn giản hóa sai cao nhất trong toàn bộ Core Concepts Map, cần xử lý cẩn trọng khi rút gọn cho định dạng video ngắn.

### Primary concepts

- Vận — chu kỳ 20 năm, 9 Vận trong một "Tam Nguyên" ~180 năm; Vận 8 (2004–2023), Vận 9 (2024–2043) theo nguồn khảo sát.
- Hướng tọa/hướng nhìn (tọa sơn - hướng) của nhà tại thời điểm xây/nhập trạch.
- Phi Tinh — 9 sao (Nhất Bạch đến Cửu Tử) "bay" vào 9 cung nhà theo lưới Lạc Thư.
- Ba lớp sao mỗi cung: sao vận (nguyên đán), sao hướng (tài lộc/quan hệ), sao tọa (sức khỏe/nhân đinh).
- Sao bay theo năm/tháng (lưu niên/lưu nguyệt) — khiến mức tốt/xấu từng cung biến đổi theo thời gian.
- 24 Sơn Hướng — la bàn chi tiết hơn 8 hướng Bát Trạch (chỉ cần nêu khái niệm, không đi sâu).
- Gốc lineage: dòng Tam Nguyên (khác Tam Hợp của Bát Trạch).

### Narrative detail

Khác với Bát Trạch (tĩnh theo mệnh chủ), Huyền Không Phi Tinh là hệ động — mỗi căn nhà có một Vận cố định tại thời điểm xây/nhập trạch, và từ Vận cùng hướng tọa/hướng nhà, hệ thống "cho các sao bay" vào 9 cung tạo thành một "lá số" riêng cho từng căn nhà, biến đổi thêm theo sao lưu niên/lưu nguyệt. Đây là điểm khác biệt cấu trúc lớn nhất so với Bát Trạch: Huyền Không gắn với nhà và thời gian, Bát Trạch gắn với người và không đổi theo thời gian. Đối lập này ("tĩnh, gắn với người" vs "động, gắn với thời gian và căn nhà") là chất liệu kịch bản tốt để dựng thành "hai cách nhìn khác nhau về cùng một câu hỏi" thay vì chọn phe.

### Script-ready material

- Đối lập trực quan Bát Trạch (tĩnh) vs Huyền Không (động) — đoạn "hai cách nhìn khác nhau."
- Khái niệm "Vận" (chu kỳ 20 năm) — chất liệu về quan niệm thời gian tuần hoàn trong văn hóa Á Đông, có thể liên hệ can chi/vòng đời mà không cần tính toán.

### Production cautions

- **Tuyệt đối tránh** đưa ra "bảng tra nhanh" khiến khán giả tự tính rồi áp cho nhà mình — vi phạm ranh giới cá nhân hóa (`DOMAIN_GUIDE.md` §4).
- Mốc chuyển Vận (2004, 2024) nên nêu như quy ước tính toán truyền thống, không phải sự kiện thiên văn được khoa học hiện đại xác nhận.
- **Không** dùng khung "sao xấu bay vào cung X năm nay nên phải mua vật phẩm Y ngay" — mẫu hình quảng cáo sợ hãi bị cấm rõ ràng ở §9.
- Không ngầm hiểu Bát Trạch và Huyền Không là "hai bước của cùng một quy trình" — luôn gọi tên trường phái khi đưa ra quy tắc cụ thể (`DOMAIN_GUIDE.md` §2, §13 mục 1).

## Bảng tóm tắt 4 chủ đề (Bát Quái, Loan Đầu, Bát Trạch, Huyền Không)

| Chủ đề | Biến số chính | Tĩnh/động theo thời gian? | Gắn với người hay nhà? |
|---|---|---|---|
| Bát Quái | Cấu trúc biểu tượng nền (Tiên Thiên/Hậu Thiên) | Tĩnh (hệ quy chiếu) | Cả hai — nền tảng chung |
| Loan Đầu | Hình thế địa hình | Tĩnh về nguyên tắc | Nhà/đất |
| Bát Trạch | Năm sinh + giới tính gia chủ → Kua number | Tĩnh theo đời người | Người (rồi áp cho nhà) |
| Huyền Không Phi Tinh | Vận xây/nhập trạch + hướng nhà + thời gian | Động — theo Vận và năm/tháng | Nhà (theo thời gian) |

---

# Applied Section — Ứng dụng Phong Thủy vào Nhà ở

**Khung lý thuyết nền cho toàn bộ mục này:** phần lớn nội dung dưới đây dựa trên khung Bát Trạch (Đông Tứ Mệnh/Tây Tứ Mệnh, 8 hướng tốt-xấu theo cung phi — xem Core Concepts Map §Bát Trạch). Đây là quy tắc trường phái Bát Trạch (Lý Khí) — Huyền Không Phi Tinh tính hướng tốt/xấu theo Vận và có thể cho kết quả khác. Mọi nội dung sản xuất từ mục này phải nói rõ "theo trường phái Bát Trạch" thay vì trình bày như quy tắc duy nhất đúng (`DOMAIN_GUIDE.md` §2, §10). Nguyên lý Loan Đầu (minh đường, tựa sơn hướng thủy) cũng được dùng lồng ghép ở một số mục và cần được gọi tên riêng khi xuất hiện.

**Cảnh báo tiêu chuẩn cho toàn mục:** phần lớn nguồn cho mục này là nguồn thương mại (cửa hàng nội thất, cửa hàng vật phẩm phong thủy) — xem "Ghi chú thiên kiến nguồn" ở Canonical Sources. Mọi "Production cautions" dưới đây nhắc lại rõ ràng ranh giới `DOMAIN_GUIDE.md` §6 (tài chính) và §9 (Anti-Fear-Sales) theo đúng yêu cầu nhiệm vụ.

## 1. Hướng nhà theo Cung Mệnh

**Nguyên lý truyền thống:** sau khi xác định cung phi (Đông Tứ Mệnh hay Tây Tứ Mệnh — xem Bát Trạch), gia chủ được khuyến nghị ưu tiên nhà/cửa chính nằm trong nhóm hướng tương ứng để "khí" người ở và công trình hài hòa.

**Chi tiết ứng dụng:** thực tế đô thị Việt Nam hiện nay, đa số người mua nhà/đất không chọn được hướng vì quỹ đất có sẵn — ứng dụng phổ biến nhất không phải "chọn hướng nhà" mà là "hóa giải hướng nhà không hợp mệnh" bằng cách điều chỉnh hướng cửa/bếp/giường/bàn làm việc lệch so với hướng tổng thể căn nhà. Khi vợ chồng khác cung mệnh, nguồn thương mại thường khuyên ưu tiên mệnh của trụ cột tài chính/chủ hộ đứng tên nhà — đây là quy ước thực hành phổ biến, **không phải quy tắc cổ điển thống nhất**, cần gắn nhãn "theo thực hành phổ biến hiện nay."

**Production cautions (Anti-Fear-Sales §9 và ranh giới tài chính §6):**
- **Cấm tuyệt đối:** nói "hướng nhà hợp mệnh sẽ đảm bảo giàu có/thành công" — đây chính là ví dụ mẫu bị cấm ở `DOMAIN_GUIDE.md` §6. Không lặp lại giọng điệu "phất lên như diều gặp gió," "rước tài lộc" từng thấy ở nguồn thương mại.
- Không mời khán giả gửi năm sinh để được "tính hướng nhà cho bạn" — vi phạm ranh giới cá nhân hóa §4.
- Tránh khung "nhà sai hướng = tai họa sắp đến" — mẫu câu sợ hãi bị cấm ở §9.

## 2. Cửa chính và Minh Đường

**Nguyên lý truyền thống:** cửa chính là "miệng khí" của nhà. Minh đường (nguyên lý Loan Đầu) là khoảng không gian mở, thoáng phía trước cửa chính — thoáng đãng được xem là điều kiện tốt để khí tụ lại trước khi vào nhà.

**Chi tiết ứng dụng:** nguyên tắc "không thông phong" (cửa chính không thẳng hàng cửa sau/cửa sổ lớn đối diện) — cách hóa giải truyền thống: bình phong, tủ/vách ngăn nhẹ, rèm, chuông gió, chậu cây cao giữa lối đi. Kích thước cửa theo thước Lỗ Ban (hệ đo dân gian, không phải Bát Trạch) và màu cửa tương sinh với mệnh gia chủ là hai lớp quy tắc riêng biệt, thường bị nguồn thương mại gộp chung với hướng cửa — cần phân biệt rõ khi kịch bản hóa. Khái niệm "minh đường" nguyên gốc nói về sân nhà làng quê/dinh thự, khi áp vào nhà ống đô thị Việt Nam đã biến đổi thành các quy tắc thu nhỏ (bậc thềm, khoảng lùi nhỏ, chậu cây trước cửa) — một minh chứng "địa phương hóa/đô thị hóa" qua thời gian (lớp cultural/historical, `DOMAIN_GUIDE.md` §10).

**Production cautions:**
- Cẩn trọng với danh sách kiểu "12 lỗi phong thủy cửa chính" clickbait — nguồn thương mại thường liệt kê nhiều "đại kỵ" để tạo cảm giác nhà nào cũng "phạm lỗi," rồi bán giải pháp/vật phẩm. Chỉ giữ nguyên tắc có đồng thuận liên nguồn (thông phong, minh đường bị chắn), không liệt kê tràn lan gây lo âu — vi phạm §9 nếu không kiểm soát.

## 3. Phòng khách

**Nguyên lý truyền thống:** phòng khách thường đặt gần cửa chính, được xem là "vượng vị" — nơi đón khí đầu tiên, không gian sinh hoạt chung.

**Chi tiết ứng dụng:** sofa/ghế chính nên tựa lưng vào tường vững chắc ("tọa sơn" — mượn nguyên lý Loan Đầu về chỗ dựa) thay vì tựa lưng ra cửa sổ/khoảng trống; tránh đặt sofa đối diện thẳng cửa ra vào hoặc dưới xà ngang/quạt trần; bố cục chữ L/U tạo thế "quy tụ" mang tính biểu tượng đoàn tụ gia đình hơn là quy tắc kỹ thuật chặt chẽ.

**Production cautions:**
- Không khẳng định "kê sofa đúng chỗ sẽ hút vượng khí, sung túc" như tiêu đề một số nguồn thương mại — trình bày đúng hơn: đây là bố cục được tin là tạo cảm giác an toàn/ổn định theo quan niệm truyền thống, **không phải cơ chế đảm bảo tài chính** (§6).

## 4. Phòng ngủ

**Nguyên lý truyền thống:** giường ngủ là nơi cơ thể ở trạng thái yếu/mở nhất trong ngày, nên đặc biệt chú trọng cảm giác được che chở, không bị "đe dọa" thị giác.

**Chi tiết ứng dụng (đồng thuận liên nguồn):** không đặt giường thẳng hàng đối diện cửa phòng; không đặt dưới xà ngang; không để đầu giường sát tường chung với nhà vệ sinh; tránh góc nhọn chĩa thẳng vào giường; nên có khoảng trống hai bên giường; hướng đầu giường lý tưởng theo cung mệnh (logic Bát Trạch giống hướng nhà/hướng bếp). Nhiều quy tắc nhóm này trùng khớp với lý do tâm lý học môi trường hiện đại (cảm giác an toàn khi ngủ, giảm giật mình) — chất liệu tốt cho lớp "modern-reflective" (§10 domain guide): giải thích song song logic truyền thống và trực giác không gian sống hiện đại, không cần khẳng định cơ chế "khí" là có thật khoa học, cũng không phủ nhận hoàn toàn.

**Production cautions (ranh giới sức khỏe §7):**
- Một số nguồn gắn trực tiếp bố cục phòng ngủ với "sức khỏe" ("gây đau đầu, buồn nôn") như thể cơ chế y học — chỉ được nói "theo quan niệm truyền thống, cách bố trí này được tin là ảnh hưởng tới giấc ngủ/tinh thần," **không được khẳng định như cơ chế y khoa đã kiểm chứng.**

## 5. Bàn thờ gia tiên — trọng tâm văn hóa Việt Nam

**Nguyên lý truyền thống:** bàn thờ gia tiên trong nhà Việt là trung tâm thực hành tín ngưỡng thờ cúng tổ tiên — mang tính văn hóa/tâm linh dân gian nhiều hơn kỹ thuật Bát Trạch thuần túy, cần kịch bản hóa với sự trang trọng cao hơn các mục nội thất khác.

**Chi tiết ứng dụng:** vị trí trang trọng nhất trong nhà (phòng khách ở nhà ống đô thị, hoặc phòng riêng ở nhà rộng); kiêng kỵ đồng thuận liên nguồn — không đặt gần/đối diện nhà vệ sinh, phòng tắm, bếp; không đặt dưới xà ngang; không đối diện trực tiếp cửa chính/cửa bếp/cửa nhà vệ sinh. Bố trí ba bát hương phổ biến (thế "Tam Sơn"): Thần linh ở giữa/cao nhất, gia tiên bên phải, Bà Cô/Ông Mãnh bên trái — tượng trưng Phúc-Lộc-Thọ; đây là quy ước dân gian phổ biến, các gia đình/vùng miền có thể khác nhau về số lượng và cách sắp. **Hướng bàn thờ có bắt buộc trùng hướng nhà hay không: single-sourced/chưa đủ cross-check** — không đưa vào kịch bản như quy tắc chắc chắn cho tới khi có thêm nguồn xác nhận.

**Production cautions (rủi ro cao nhất về giọng điệu hù dọa trong toàn bộ Applied Section, §9):**
- Nhiều nguồn dùng chữ "đại kỵ," "phạm phải sẽ hại phúc lộc/sức khỏe cả nhà." `DOMAIN_GUIDE.md` §9 cấm tuyệt đối khung "nếu không làm X thì vận xui ập đến." Khi kịch bản hóa, chuyển "phạm đại kỵ sẽ gặp họa" thành "theo quan niệm dân gian, đây được xem là điều nên tránh vì lý do [ý nghĩa văn hóa/sự tôn kính]" — giữ lý do văn hóa, bỏ ngôn ngữ đe dọa hậu quả.
- Không suy diễn "đặt sai bàn thờ = tổ tiên trừng phạt" dù nguồn có ngụ ý gần đó — vượt quá khung "giải thích truyền thống" sang khung gieo sợ hãi tâm linh cụ thể.
- Nguồn hiện tại toàn bộ tier 3 (thương mại/dân gian) — khuyến nghị bổ sung nguồn dân tộc học trước khi dùng cho nội dung có độ nhạy cảm/trang trọng cao (xem Khoảng trống nguồn).

## 6. Bếp

**Nguyên lý truyền thống:** bếp thuộc hành Hỏa, gắn với "cái ăn" của gia đình, được xem trọng ngang bàn thờ và cửa chính (bộ ba "Môn - Táo - Chủ").

**Chi tiết ứng dụng (đồng thuận liên nguồn):** không đặt bếp đối diện thẳng cửa chính/cửa nhà vệ sinh, không quay lưng nghịch hướng nhà; không đặt bếp sát/đối diện giường ngủ; không đặt dưới xà ngang; tủ lạnh (Kim) đặt sát bếp (Hỏa) được diễn giải là xung khí theo Ngũ Hành — cần nói rõ đây là suy diễn từ nguyên lý tổng quát, không phải quy tắc trong văn bản cổ điển thống nhất. **Nguyên lý "Tọa Hung — Hướng Cát"** (riêng của Bát Trạch ứng dụng cho bếp, khác logic "tọa cát" ở phòng ngủ/phòng khách): vị trí đặt bếp nên nằm ở cung xấu của gia chủ, hướng miệng bếp/lưng người nấu nên quay về cung tốt — logic dân gian: dùng lửa hóa giải cái xấu tại vị trí đó, trong khi hướng nấu đón khí tốt.

**Production cautions:**
- Các nguồn liệt kê "16-20 điều đại kỵ nhà bếp" là ví dụ điển hình liệt kê tràn lan gây lo âu — chỉ giữ điểm có đồng thuận liên nguồn và lý do hợp lý (an toàn, vệ sinh, công năng), không liệt kê hết để tạo cảm giác nguy hiểm rình rập.
- Không nói bếp sai hướng "gây hao tài tán lộc" như khẳng định nhân quả — chỉ trình bày như niềm tin truyền thống (§6, §9).
- Khi giới thiệu "Tọa Hung Hướng Cát," nói rõ đây là quy tắc riêng của Bát Trạch cho bếp, không áp dụng logic giống các không gian khác — tránh gây nhầm lẫn.

## 7. Cây phong thủy theo mệnh

**Nguyên lý truyền thống:** ứng dụng Ngũ Hành tương sinh/tương khắc vào chọn cây theo màu sắc/đặc tính tương ứng mệnh gia chủ.

**Chi tiết ứng dụng:** Mệnh Kim — cây tông trắng/ánh kim hoặc mệnh Thổ (Thổ sinh Kim); Mệnh Mộc — cây xanh lá (bản mệnh) hoặc mệnh Thủy (Thủy sinh Mộc); Mệnh Thủy — cây tông trắng (Kim sinh Thủy) hoặc xanh dương/đen (bản mệnh); Mệnh Hỏa — nguồn không hoàn toàn nhất quán giữa cây tông đỏ/tím và cây Mộc (Mộc sinh Hỏa), cần cross-check thêm; Mệnh Thổ — tránh cây thuần Mộc (Mộc khắc Thổ) và cây thủy sinh thuần túy. Cây kim ngân (5 lá/cành tượng trưng đủ 5 hành) là biểu tượng phổ biến độc lập với mệnh cá nhân. Nhiều loại cây phong thủy phổ biến ở Việt Nam (kim ngân, kim tiền, trầu bà, lưỡi hổ) thực chất là cây cảnh nội thất du nhập/phổ biến hóa gần đây, ý nghĩa phong thủy phần lớn được gắn vào sau khi cây đã phổ biến trong ngành cây cảnh — một góc "sự thật thú vị" cho video.

**Production cautions:**
- Không dùng cụm "trồng cây này sẽ hút tài lộc/tiền vào như nước" — vi phạm §6 trực tiếp. Đổi thành: "theo quan niệm phong thủy, loại cây này được xem là biểu tượng phù hợp với mệnh X."
- Danh sách cây cụ thể theo từng mệnh chỉ là ví dụ minh họa, không phải danh sách "chuẩn" duy nhất — nguyên lý chọn màu/hành mới là nội dung chính.

## 8. Vật phẩm phong thủy phổ biến

### 8.1 Gương bát quái

**Nguyên lý truyền thống:** tấm gương/bảng hình bát giác khắc 8 quẻ quanh Thái Cực, dân gian tin có khả năng phản/hóa giải sát khí (hướng ra ngoài, đối diện vật được cho là mang sát khí).

**Chi tiết ứng dụng:** ba loại — gương lồi (phân tán sát khí), gương lõm (thu hút vượng khí), gương phẳng (cân bằng). Quy tắc phổ biến: không treo trong phòng ngủ/phòng làm việc, không treo đối diện cửa chính nhà mình, không treo quá 2 chiếc.

**Điểm đối chiếu quan trọng — sự bất đồng thực sự giữa các nguồn:** một bài trên VnExpress (tác giả nghiên cứu văn hóa Phạm Đình Hải) đưa ra góc nhìn khác hẳn phần lớn nguồn thương mại: gương bát quái **không phải là "pháp khí" phong thủy chính thống** — nguồn gốc thực sự không rõ ràng, có thể bắt nguồn từ việc đạo sĩ dùng gỗ đào khắc bát quái làm công cụ tu tập chứ không phải bùa hộ mệnh; gương bát quái ngày nay chủ yếu là vật trang trí bằng kính/kim loại, không có khả năng "trấn" hay "hại" hàng xóm như lời đồn dân gian. Đây là ví dụ tốt về bất đồng nguồn thực sự — **cần trình bày cả hai luồng quan điểm** (dân gian phổ biến tin có tác dụng hóa giải vs. góc nhìn nghiên cứu văn hóa hoài nghi) thay vì chọn một bên, đúng tinh thần §10.

**Production cautions:**
- Vật phẩm dễ bị lạm dụng nhất để gây bất hòa hàng xóm trong đời thực (tin đồn "gương bát quái trấn nhà đối diện" từng gây tranh chấp dân sự thật ở Việt Nam) — kịch bản nên chủ động nói rõ đây là quan niệm dân gian gây tranh cãi, không phải sự thật được xác nhận, để tránh cổ vũ hành vi treo gương "trấn" hàng xóm.

### 8.2 Tỳ Hưu

**Nguyên lý truyền thống:** theo truyền thuyết dân gian Trung Hoa (không phải chính sử), Tỳ Hưu là con thứ 9 của Rồng, không có hậu môn (chỉ ăn vào không thải ra) — gắn với hình tượng "giữ của, không để tài lộc thất thoát."

**Chi tiết ứng dụng:** hai loại — Thiên Lộc (một sừng, chiêu tài) và Tịch Tà (hai sừng, trấn trạch/xua tà). Cách đặt phổ biến: đầu/mắt hướng ra cửa chính/cửa sổ, tuyệt đối không quay đầu vào trong nhà (theo quan niệm dân gian).

**Production cautions:**
- Vật phẩm bị thương mại hóa mạnh nhất trong nghiên cứu — nhiều nguồn dùng ngôn ngữ "linh vật giá trị nhất về chiêu tài" gần như quảng cáo trực tiếp sản phẩm đá quý/vàng. `DOMAIN_GUIDE.md` §6 cấm thẳng khung "đặt Tỳ Hưu → chắc chắn giàu." Chỉ trình bày Tỳ Hưu như biểu tượng văn hóa về khát vọng giữ của cải, không phải cơ chế tài chính.

### 8.3 Cóc ba chân (Thiềm Thừ)

**Nguyên lý truyền thống:** gắn với truyền thuyết tiên nhân Lưu Hải thu phục yêu tinh Thiềm Thừ (một dị bản: gãy mất một chân trong lúc thu phục), sau đó cải tà quy chính, theo Lưu Hải nhả tiền giúp người nghèo.

**Chi tiết ứng dụng:** hình tượng cóc ngậm đồng tiền cổ, thường đặt gần bàn thờ Thần Tài - Thổ Địa, bàn làm việc, quầy thu ngân. Quy tắc phổ biến: đặt thấp/sát đất, đầu cóc quay vào trong nhà (ngược với Tỳ Hưu quay ra ngoài).

**Production cautions:**
- Cùng mức rủi ro thương mại hóa như Tỳ Hưu — không khẳng định "đặt cóc sẽ hút tài lộc," chỉ trình bày là biểu tượng văn hóa gắn với khát vọng đủ đầy (§6).

### 8.4 Thác nước mini

**Nguyên lý truyền thống:** nước trong Loan Đầu gắn với dòng chảy tài lộc ("thủy tụ thì tài tụ") — thác nước mini là phiên bản thu nhỏ/nhân tạo của nguyên lý "minh đường có thủy."

**Chi tiết ứng dụng (đồng thuận liên nguồn):** hướng dòng nước nên chảy vào trong nhà/khu sinh hoạt chính, tránh chảy thẳng ra cửa/ra ngoài; vị trí phổ biến phòng khách/gần cầu thang, tránh phòng ngủ/gần bếp/gần nhà vệ sinh/giữa lối cửa; cần duy trì nước chảy liên tục, sạch.

**Production cautions:**
- Một số nguồn dùng tiêu đề dạng cảnh báo ("chỉ một sai lầm khiến tài lộc chảy mất") — mẫu câu tạo lo âu nhẹ để tăng click, cần tránh khi viết tiêu đề/kịch bản theo quy định anti-fear-bait ở `CORE_OS/SEO_ENGINE.md` và §9 domain guide.

## 9. Phong thủy văn phòng / kinh doanh cơ bản

**Nguyên lý truyền thống:** cùng logic "tựa sơn hướng thủy" và hướng theo cung mệnh như nhà ở, thêm lớp quan sát/kiểm soát không gian (thấy được cửa ra vào mà không đối diện trực tiếp).

**Chi tiết ứng dụng:** bàn làm việc lý tưởng — lưng tựa tường/vách chắc chắn, mặt hướng không gian thoáng, quan sát được cửa nhưng không nằm ngay trục cửa. Sự gọn gàng/sạch sẽ được nhiều nguồn xem là nguyên tắc cơ bản và quan trọng nhất — điểm giao thoa rõ giữa phong thủy dân gian và quản lý không gian làm việc hiện đại, không cần yếu tố huyền học để hợp lý.

**Production cautions:**
- Không gợi ý "sắp xếp bàn làm việc theo phong thủy sẽ giúp thăng chức/kinh doanh phát đạt" như một cam kết — thuộc phạm vi tư vấn kinh doanh/tài chính bị cấm ở §6. Có thể nói: "được tin là hỗ trợ sự tập trung và cảm giác chủ động" — khung tâm lý-không gian hợp lý hơn khung tài chính.

## 10. Bối cảnh rủi ro thực tế — Lừa đảo tâm linh/phong thủy tại Việt Nam (đầu vào cho Anti-Fear-Sales, không phải chất liệu kịch bản trực tiếp)

Nhiều báo chính thống Việt Nam (Công an Nhân dân, An ninh Thủ đô, Pháp Luật Việt Nam, Nhân Dân) đưa tin về mô hình lừa đảo tâm linh/phong thủy phổ biến: kịch bản điển hình bắt đầu bằng "phán miễn phí" một vận hạn/vấn đề tâm linh đánh trúng tâm lý lo âu, sau đó dẫn dắt nạn nhân mua vật phẩm phong thủy hoặc làm lễ giải hạn với chi phí từ vài trăm nghìn đến hàng tỷ đồng. Một thống kê được báo chí trích dẫn: khoảng 28.000 trường hợp bị lừa trong một năm với tổng thiệt hại hơn 8 tỷ đồng qua hình thức tâm linh nói chung.

**Vì sao ghi chú này quan trọng cho packet:** đây không phải chất liệu kịch bản trực tiếp, nhưng là bằng chứng thực tế, có nguồn báo chí, cho thấy vì sao Anti-Fear-Sales Standard (`DOMAIN_GUIDE.md` §9) là ranh giới bắt buộc chứ không phải lựa chọn phong cách — kênh cần chủ động phân biệt mình với chính mô hình nội dung thương mại hù dọa đang bị báo chí trong nước cảnh báo. Có thể cân nhắc dùng làm chất liệu cho một video riêng "vì sao kênh không bán vật phẩm phong thủy" hoặc một đoạn disclaimer định kỳ, thay vì lồng vào các video ứng dụng nhà ở.

---

# Terminology

Đề xuất nạp vào `GLOSSARY/DOMAIN_GLOSSARY.md` (hiện `planned`) trước khi dùng làm nguồn sản xuất chính thức: Âm Dương, Ngũ Hành (Kim/Mộc/Thủy/Hỏa/Thổ), Tương Sinh, Tương Khắc, Bát Quái, Tiên Thiên Bát Quái, Hậu Thiên Bát Quái, Khí, Sinh khí, Tà khí/Sát khí, Loan Đầu, Lý Khí, Long mạch, Minh đường, Tứ Tượng/Tứ Linh (Thanh Long, Bạch Hổ, Chu Tước, Huyền Vũ), Bát Trạch, Kua number/Quái Mệnh, Đông Tứ Mệnh, Tây Tứ Mệnh, Huyền Không Phi Tinh, Vận, Phi Tinh, 24 Sơn Hướng, Dương Trạch, Âm Trạch, Tọa Hung Hướng Cát, thước Lỗ Ban, Thiềm Thừ, Tỳ Hưu, Gương bát quái. Không tự sáng chế thuật ngữ mới ngoài danh sách này; nếu kịch bản cần một thuật ngữ chưa có trong glossary, phải bổ sung glossary trước (cùng quy trình đã dùng cho domain Buddhism).

---

# Risk-Specific Editorial Rules

Các quy tắc dưới đây cụ thể hóa `DOMAIN_GUIDE.md` (§2, §4-9, §12-13) cho từng khái niệm trong packet này, theo cùng định dạng "Required language pattern / Forbidden pattern" đã dùng ở `KP_BUD_001`.

## Rule 1 — School-Naming Rule (không trộn trường phái)

Luôn gọi tên trường phái/lineage cụ thể (Loan Đầu, Bát Trạch, Huyền Không Phi Tinh) mỗi khi phát biểu một quy tắc cụ thể. Không bao giờ trình bày Bát Trạch và Huyền Không Phi Tinh như hai bước bổ sung của một quy trình duy nhất, và không ngầm chọn một hệ làm "chuẩn."

**Required language pattern:** "Theo trường phái Bát Trạch, ... trong khi theo Huyền Không Phi Tinh, ... — đây là hai hệ thống có gốc lý luận khác nhau, có thể cho khuyến nghị khác nhau trên cùng một căn nhà."

**Forbidden pattern:** "Phong thủy nói rằng..." (khi thực chất là quy tắc riêng của một trường phái); "kết hợp Bát Trạch và Huyền Không để có kết quả chính xác nhất."

## Rule 2 — Individualized-Reading Rule (ranh giới cá nhân hóa, §4)

Không tính toán hướng nhà/mệnh/Kua number/Vận cho khán giả cụ thể trên sóng, không mời khán giả gửi năm sinh hoặc sơ đồ nhà để được "xem giúp." Mọi ví dụ minh họa cách tính/cách đọc phải dùng nhân vật hư cấu hoặc lịch sử/truyền thuyết.

**Required language pattern:** "Hãy cùng xem cách tính này qua một ví dụ minh họa — không phải nhà của bạn."

**Forbidden pattern:** "Bình luận năm sinh của bạn để được tính hướng nhà miễn phí."

## Rule 3 — Certainty Rule (§5)

Dùng khung "theo trường phái X, ... thường được xem là" thay vì khẳng định tương lai chắc chắn.

**Required language pattern:** "Theo Bát Trạch truyền thống, hướng này thường được xem là hợp với người mang mệnh quái X."

**Forbidden pattern:** "Bạn sẽ gặp may mắn/khó khăn nếu..."

## Rule 4 — Financial Boundary Rule (§6)

Không cam kết hoặc ngụ ý vật phẩm/hướng/bố cục là cơ chế đảm bảo tài chính.

**Required language pattern:** "Theo quan niệm phong thủy, vật phẩm/bố cục này được xem là biểu tượng của khát vọng tài lộc — không phải cơ chế đảm bảo kết quả tài chính."

**Forbidden pattern:** "Đặt vật này ở đây để chắc chắn giàu / hút tiền vào như nước."

## Rule 5 — Health Boundary Rule (§7)

Không khẳng định bố cục nhà ở là cơ chế y khoa đã kiểm chứng.

**Required language pattern:** "Theo quan niệm truyền thống, cách bố trí này được tin là ảnh hưởng tới giấc ngủ/tinh thần — đây là niềm tin văn hóa, không phải chẩn đoán y khoa."

**Forbidden pattern:** "Bố trí sai sẽ gây đau đầu, buồn nôn, bệnh tật."

## Rule 6 — Anti-Fear-Sales Rule (§9, mức ưu tiên cao nhất domain này)

Cấm mọi khung hù dọa/thúc giục mua vật phẩm hoặc làm lễ giải hạn. Bối cảnh: báo chí Việt Nam đã ghi nhận mô hình lừa đảo tâm linh dùng đúng khung này (xem Applied Section §10) — kênh phải chủ động phân biệt mình với mô hình đó.

**Required language pattern:** giải thích thực hành truyền thống bằng giọng điềm tĩnh, tôn trọng (`CORE_OS/BRAND_BIBLE.md`); đối xử với lo âu của khán giả về vận may bằng sự cảm thông, không khai thác nó.

**Forbidden pattern:** "Nếu không làm điều này, vận xui sẽ ập đến"; "mua ngay kẻo muộn"; "chỉ 3 ngày nữa là hết hạn hóa giải"; bất kỳ tiêu đề/kịch bản nào dựng quanh một deadline hoặc mối đe dọa giả tạo.

## Rule 7 — Vật phẩm-Specific Rule

Riêng cho gương bát quái, Tỳ Hưu, Thiềm Thừ, thác nước mini: trình bày như biểu tượng văn hóa gắn với khát vọng (giữ của, xua tà, tài lộc), không suy diễn thành cơ chế có hiệu quả kiểm chứng được. Khi nguồn có bất đồng thực sự (ví dụ gương bát quái, xem §8.1), trình bày cả hai luồng quan điểm thay vì chọn một bên.

**Required language pattern:** "Đây là một biểu tượng văn hóa lâu đời, gắn với khát vọng [giữ của/xua tà/đủ đầy] — không phải một cơ chế được xác nhận có hiệu quả."

**Forbidden pattern:** "Linh vật giá trị nhất về chiêu tài" (ngôn ngữ quảng cáo trực tiếp).

## Rule 8 — Bàn thờ gia tiên Rule (giọng trang trọng)

Bàn thờ gia tiên đòi hỏi giọng điệu trang trọng hơn các mục nội thất khác — đây là thực hành tín ngưỡng, không chỉ kỹ thuật bố trí. Không dùng ngôn ngữ "đại kỵ" mang tính đe dọa hậu quả.

**Required language pattern:** "Theo quan niệm dân gian, đây được xem là điều nên tránh vì lý do [ý nghĩa văn hóa/sự tôn kính]."

**Forbidden pattern:** "Phạm điều này sẽ hại phúc lộc/sức khỏe cả nhà"; bất kỳ suy diễn nào về "tổ tiên trừng phạt."

## Rule 9 — Historical-Legend Attribution Rule

Mọi quy gán tác giả/nhân vật lịch sử (Phục Hy, Văn Vương, Quách Phác, Dương Quân Tùng, Chu Đôn Di cho Thái Cực Đồ) phải được nêu là "tương truyền," không trình bày như sự kiện lịch sử đã kiểm chứng — cùng chuẩn xử lý Trần Đoàn/Tử Vi ở `DOMAIN_GUIDE.md` §2.

**Required language pattern:** "Tương truyền, [nhân vật] là người sáng lập/hệ thống hóa [khái niệm] — đây là quy gán truyền thống, chưa được xác thực bằng sử liệu độc lập."

**Forbidden pattern:** "[Nhân vật] đã phát minh ra [khái niệm] vào năm [X]" (trình bày như sự kiện lịch sử chắc chắn).

## Rule 10 — Cross-School Contradiction Disclosure Rule

Khi một quy tắc cụ thể có thể mâu thuẫn giữa các trường phái (đặc biệt Bát Trạch vs Huyền Không), phải chủ động nêu khả năng mâu thuẫn thay vì im lặng bỏ qua.

**Required language pattern:** "Lưu ý: một trường phái khác (ví dụ Huyền Không Phi Tinh) có thể đưa ra khuyến nghị khác cho cùng căn nhà này — đây không phải kênh sai, mà là hai hệ thống khác gốc lý luận."

**Forbidden pattern:** im lặng không nhắc đến khả năng có trường phái khác kết luận khác đi.

---

# Domain QA Checklist (áp dụng cho mọi nội dung phát sinh từ packet này)

Tái hiện và mở rộng từ `DOMAIN_GUIDE.md` §13:

1. Mọi tuyên bố cụ thể có gọi tên nguồn/trường phái, hoặc được gắn nhãn đồng thuận liên trường phái không?
2. Có dòng nào chạm ranh giới đọc/luận giải cá nhân hóa cho khán giả cụ thể (§4) không?
3. Có dòng nào ngụ ý chắc chắn về một kết quả tương lai cụ thể (§5) không?
4. Có dòng nào đưa lời khuyên tài chính, y tế, hoặc dự đoán thời điểm rủi ro lớn (§6-8) không?
5. Có dòng nào dùng khung sợ hãi, thúc giục, hoặc đe dọa (§9) không?
6. Nội dung có giữ được cả ba lớp văn hóa/tín ngưỡng truyền thống/phản chiếu hiện đại mà không xóa bỏ lớp nào (§10) không?
7. Thuật ngữ dùng có nhất quán với `DOMAIN_GLOSSARY.md` (sau khi glossary được kích hoạt) không?
8. Có quy gán lịch sử nào bị trình bày như sự kiện xác thực thay vì "tương truyền" không?
9. Có mục vật phẩm/ứng dụng nào thiếu Production caution nhắc §9 Anti-Fear-Sales không?
10. Có nội dung nào trộn Bát Trạch và Huyền Không Phi Tinh thành một công thức duy nhất không?

---

# Retrieval Warnings

Khi packet này được truy xuất, hệ thống nên đính kèm các cảnh báo:

- Nội dung rủi ro cao liên quan tài chính/lo âu (vật phẩm phong thủy, bàn thờ gia tiên).
- Bát Trạch và Huyền Không Phi Tinh là hai hệ khác gốc, không được trộn.
- Mọi quy tắc "hợp mệnh/hợp hướng" phải gắn nhãn trường phái, không trình bày như quy tắc phổ quát.
- Không dùng packet này để tính toán hoặc luận giải cho một khán giả/căn nhà cụ thể.
- Ngôn ngữ cam kết tài chính ("chắc chắn giàu") bị cấm tuyệt đối.
- Bàn thờ gia tiên yêu cầu giọng điệu trang trọng riêng, khác các mục nội thất.
- Quy gán lịch sử (Phục Hy, Văn Vương, Quách Phác, Dương Quân Tùng) là truyền thuyết, cần ngôn ngữ "tương truyền."
- Domain QA Policy và Domain Glossary của domain FS hiện vẫn `planned` — packet này chưa thay thế yêu cầu QA chính thức.

# Editorial Memory Seeds

Các nguyên tắc sau nên được đẩy vào bộ nhớ vận hành sau khi packet qua QA:

- Phong Thủy nội dung bắt đầu từ giải thích truyền thống, không phải từ nỗi sợ.
- Ba trường phái Loan Đầu/Bát Trạch/Huyền Không không bao giờ được trộn thành một công thức.
- Không có "công thức đúng duy nhất" cho hướng nhà — chỉ có "theo trường phái X."
- Vật phẩm phong thủy là biểu tượng văn hóa, không phải cơ chế tài chính đảm bảo.
- Hai chu kỳ Tương Sinh/Tương Khắc Ngũ Hành là nền cứng, an toàn để khẳng định chắc chắn; hầu hết phần còn lại cần gắn nhãn độ tin cậy.
- Bàn thờ gia tiên đòi hỏi giọng trang trọng hơn các mục nội thất khác.
- Không tính toán/luận giải trên sóng cho khán giả cụ thể — mọi ví dụ dùng nhân vật hư cấu/lịch sử.
- Bối cảnh lừa đảo tâm linh thực tế tại Việt Nam là lý do vận hành, không phải lý do phong cách, cho Anti-Fear-Sales Standard.

---

# Packet Completion Notes

Packet này tổng hợp đầy đủ 3 research draft nền tảng của nhánh Phong Thủy (Âm Dương-Ngũ Hành, Bát Quái-trường phái, Ứng dụng nhà ở) thành một Knowledge Packet có cấu trúc thống nhất, giữ nguyên toàn bộ cảnh báo/dị bản/mức độ tin cậy đã ghi trong nguồn gốc — không có tuyên bố nào trong 3 research draft bị lược bỏ hoặc làm phẳng mâu thuẫn liên trường phái khi tổng hợp. Đây là draft phù hợp làm nền tri thức nội bộ cho các bước tiếp theo (Creative Knowledge, Character Bible, Series Bible, kịch bản), **không phải nội dung sẵn sàng công chiếu**. Packet cần: (1) Domain QA Policy chính thức của domain FS (hiện `planned`) áp dụng và ký duyệt; (2) Domain Glossary chính thức (hiện `planned`) được kích hoạt và đối chiếu thuật ngữ; (3) rà soát bổ sung các "Khoảng trống nguồn" đã liệt kê, đặc biệt nguồn dân tộc học cho bàn thờ gia tiên và xác minh Kinh Dịch học thuật cho bảng Tiên Thiên Bát Quái.

# Final Packet Use Boundary

Các agent tương lai phải coi packet này là một tài sản tri thức được quản trị, không phải nội dung sẵn sàng khán giả. Packet có thể dùng để truy xuất khái niệm, cảnh báo, quan hệ liên trường phái, ràng buộc sản xuất, và phụ thuộc QA. Packet **không được** sao chép trực tiếp vào kịch bản công khai mà không qua Content Engine transformation và QA review đầy đủ.

Mọi sản phẩm phái sinh phải giữ được các ranh giới sau:

1. Phong Thủy là một truyền thống sống với nhiều trường phái độc lập, không có một "công thức đúng duy nhất" — luôn gọi tên trường phái.
2. Giải thích một truyền thống không phải là thực hiện một buổi luận giải cá nhân hóa cho khán giả cụ thể.
3. Vật phẩm/hướng/bố cục phong thủy là thực hành văn hóa-tín ngưỡng, không phải cơ chế đảm bảo tài chính hay y khoa.
4. Không bao giờ dùng khung sợ hãi/thúc giục để dẫn dắt hành động, mua sắm, hoặc chia sẻ.

Nếu một sản phẩm đầu ra tương lai không thể giữ được bốn ranh giới này, nó phải được sửa lại, nâng cấp xét duyệt, hoặc từ chối trước khi công chiếu.
