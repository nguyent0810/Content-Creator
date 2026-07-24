---
schema_version: 1.0
packet_id: KP_CL_005
domain_id: CL
asset_id: KP_CL_005
canonical_owner: DOMAINS/CRIMINAL_LAW
canonical_topic: Tổ Chức Tội Phạm — Lịch sử, Cấu trúc và Sự Sụp Đổ của 7 Tổ Chức Tội Phạm Có Tổ Chức Tiêu Biểu
vietnamese_display_name: Tổ Chức Tội Phạm (Pillar 5 — Hình Sự)
english_working_title: Organized Crime — Foundational Knowledge Packet for Pillar 5
object_type: Knowledge Packet
status: draft-pending-human-review
version: 0.2
language: Tiếng Việt (chính), chú thích Anh/Ý/Nhật/Trung/Tây Ban Nha/Tây Ban Nha-Mỹ Latinh cho thuật ngữ gốc
primary_tradition_context: Bảy tổ chức tội phạm có tổ chức được tư liệu hóa rộng rãi qua nguồn tier 1-3 — Cosa Nostra (Ý), Yakuza (Nhật Bản), Hội Tam Hoàng/Triads (Hong Kong/Trung Quốc), băng nhóm Năm Cam (Việt Nam), Cartel Medellín (Colombia), MS-13/Mara Salvatrucha (El Salvador/Hoa Kỳ), Camorra (Ý)
risk_level: critical
risk_reasons:
  - Non-glorification & no-operational-detail boundary (`DOMAIN_GUIDE.md` §8) — rủi ro cao nhất của toàn domain
  - Ranh giới đặt tên tổ chức không cấp phép đặt tên cá nhân chưa bị kết án (§4a Format 3)
  - Nguy cơ lãng mạn hóa đặc biệt cao ở Pablo Escobar/Cartel Medellín do ảnh hưởng truyền thông đại chúng (Narcos)
  - Truyền thuyết dân gian "phản Thanh phục Minh" dễ bị trình bày nhầm thành sử liệu (Hội Tam Hoàng)
  - Băng Năm Cam liên quan cán bộ nhà nước tha hóa — cần cross-reference đúng với KP_CL_002 để không lặp/mâu thuẫn tường thuật vụ án
  - MS-13 là rủi ro dạng mới, khác bản chất "lãng mạn hóa": nguy cơ chính trị hóa/giật gân theo cả hai chiều của cuộc tranh luận nhập cư Mỹ 2016-2026 — cần tiểu mục "Cảnh báo chính trị hóa/giật gân" riêng, bắt buộc mang theo nguyên vẹn (mục 6)
required_qa:
  - Domain QA (Hình Sự) — DOMAIN_QA/DOMAIN_QA_POLICY.md
  - Research QA
  - Safety QA (§8 Non-Glorification & No-Operational-Detail Boundary)
  - Historical QA
  - Brand QA
dependencies:
  - DOMAINS/CRIMINAL_LAW/DOMAIN_GUIDE.md (đặc biệt §4a Format 3, §8)
  - DOMAINS/CRIMINAL_LAW/SOURCES/RESEARCH_DRAFT_TO_CHUC_TOI_PHAM.md
  - DOMAINS/CRIMINAL_LAW/SOURCES/RESEARCH_DRAFT_TO_CHUC_TOI_PHAM_BATCH2.md (MS-13 & Camorra, research date 2026-07-24)
  - DOMAINS/CRIMINAL_LAW/KNOWLEDGE_PACKETS/KP_CL_002_An_Da_Xu.md (cross-reference cho case Năm Cam — ĐÃ TỒN TẠI kể từ 2026-07-23; số liệu 155 bị can/bị cáo, 24 tội danh, 21 cán bộ nhà nước đã được đối chiếu và khớp, xem "Cập nhật trạng thái" ở Packet Control và `_QA_REPORT_KP_CL_005.md`)
  - DOMAINS/CRIMINAL_LAW/GLOSSARY/DOMAIN_GLOSSARY.md
source_lineage: Tổng hợp 2 research draft — (1) RESEARCH_DRAFT_TO_CHUC_TOI_PHAM.md (research date 2026-07-23, 5 tổ chức gốc); (2) RESEARCH_DRAFT_TO_CHUC_TOI_PHAM_BATCH2.md (research date 2026-07-24, MS-13 & Camorra) — diễn giải lại bằng lời riêng sau khi đối chiếu nhiều nguồn qua WebSearch thực tế. Độ tin cậy hỗn hợp, gắn nhãn riêng theo từng mục — xem "Ghi chú độ tin cậy" cuối mỗi Topic Section.
confidence_level: mixed — xem nhãn độ tin cậy riêng ở từng mục
terminology: Xem GLOSSARY/DOMAIN_GLOSSARY.md — thuật ngữ "Tổ chức tội phạm" và "Hội Tam Hoàng (Triads)" đã có mục riêng; packet này không đặt thêm thuật ngữ mới ngoài glossary hiện có
claims: Xem từng Topic Section — mỗi tuyên bố cụ thể gắn nhãn độ tin cậy tại nguồn
cautions: Xem "Production cautions" trong mỗi Topic Section — đặc biệt §8 (non-glorification/no-operational-detail) và §4a Format 3 (individual-guilt-not-transferred); mục 6 (MS-13) có thêm tiểu mục bắt buộc riêng "Cảnh báo chính trị hóa/giật gân"
QA_status: draft — chưa qua Domain QA / Research QA / Safety QA chính thức cho phần mở rộng (mục 6-7); KHÔNG dùng trực tiếp làm kịch bản sản xuất trước khi human review
compatibility_aliases: [KP_TO_CHUC_TOI_PHAM_001, Organized Crime KP, Pillar 5 KP]
review_cadence: Hàng năm, và bất kỳ khi nào phát hiện nguồn mới, tiền lệ QA mới liên quan §8, hoặc khi KP_CL_002 được viết (cần rà soát lại phần cross-reference Năm Cam)
---

# KP_CL_005 — Tổ Chức Tội Phạm (Gói Tri Thức Nền Tảng, Pillar 5)

## Packet Control

| Field | Value |
|---|---|
| Packet ID | KP_CL_005 |
| Domain ID | CL |
| Canonical Topic | Tổ Chức Tội Phạm — Lịch sử, Cấu trúc và Sự Sụp Đổ của 7 Tổ Chức Tội Phạm Có Tổ Chức Tiêu Biểu |
| Vietnamese Display Name | Tổ Chức Tội Phạm (Pillar 5 — Hình Sự) |
| Object Type | Knowledge Packet |
| Status | draft-pending-human-review |
| Version | 0.2 |
| Language | Tiếng Việt (chính), chú thích gốc nước ngoài cho thuật ngữ |
| Primary Tradition Context | Cosa Nostra (Ý), Yakuza (Nhật Bản), Hội Tam Hoàng/Triads (Hong Kong/Trung Quốc), băng nhóm Năm Cam (Việt Nam), Cartel Medellín (Colombia), MS-13/Mara Salvatrucha (El Salvador/Hoa Kỳ), Camorra (Ý) |
| Risk Level | **Critical** — mức rủi ro cao nhất domain, vì đây là pillar mà §8 (Non-Glorification & No-Operational-Detail) áp dụng trực tiếp và nặng nhất |
| Required QA | Domain QA, Research QA, Safety QA (§8), Historical QA, Brand QA |
| Dependencies | `DOMAIN_GUIDE.md` §4a Format 3 + §8, `RESEARCH_DRAFT_TO_CHUC_TOI_PHAM.md`, `RESEARCH_DRAFT_TO_CHUC_TOI_PHAM_BATCH2.md`, `KP_CL_002_An_Da_Xu.md` (cross-ref, xem cảnh báo dưới) |
| Review Cadence | Hàng năm; ngay khi có nguồn mới hoặc khi KP_CL_002 được viết |

**Cập nhật trạng thái (2026-07-23, sau khi soạn):** `KP_CL_002_An_Da_Xu.md` nay đã được soạn xong. Đã đối chiếu lại: mục 4 (Băng nhóm Năm Cam) dưới đây và KP_CL_002's phần Năm Cam khớp số liệu (155 bị can/bị cáo, 24 tội danh, 21 cán bộ nhà nước xử lý) — không phát hiện mâu thuẫn. Cross-reference giữ nguyên như thiết kế: mục này chỉ tập trung cấu trúc tổ chức + mạng lưới cán bộ tha hóa, `KP_CL_002` giữ narrative vụ án/phiên tòa đầy đủ.

**Cập nhật trạng thái (2026-07-24, mở rộng batch 2 — version 0.1 → 0.2):** Bổ sung hai mục Topic Section mới, **mục 6 (MS-13/Mara Salvatrucha)** và **mục 7 (Camorra, Naples)**, tổng hợp từ `RESEARCH_DRAFT_TO_CHUC_TOI_PHAM_BATCH2.md` (research date 2026-07-24). Roster của packet nay là 7 tổ chức (trước đó 5). Không tổ chức nào trong hai mục mới vi phạm ranh giới §8 (không chi tiết vận hành, không mô tả hình xăm/phù hiệu nhận dạng được). Mục 6 mang theo đầy đủ, nguyên vẹn tiểu mục bắt buộc "Cảnh báo chính trị hóa/giật gân" từ research draft — xem cảnh báo riêng trong mục đó. Hai mục mới **chưa qua Domain QA / Research QA / Safety QA chính thức** — cùng trạng thái draft-pending-human-review như 5 mục gốc.

Đây là Knowledge Packet đầu tiên của Pillar 5 domain Hình Sự, tổng hợp từ `RESEARCH_DRAFT_TO_CHUC_TOI_PHAM.md`. `DOMAIN_QA/DOMAIN_QA_POLICY.md` của domain này cần áp dụng đầy đủ trước khi packet chuyển sang trạng thái `active` cho sản xuất kịch bản, đúng tinh thần đã thiết lập ở `KP_FS_001` và `DOMAIN_MANIFEST.md`.

---

# Nguyên tắc bao trùm (áp dụng cho cả 5 mục dưới đây)

Áp dụng cho cả 7 mục dưới đây (5 mục gốc + mục 6 MS-13 và mục 7 Camorra bổ sung 2026-07-24). Theo `DOMAIN_GUIDE.md` §8, **trọng tâm tường thuật bắt buộc của mọi tổ chức trong packet này là hậu quả/sự sụp đổ** — không phải lối sống, sự giàu có, hay tường thuật kiểu "vươn lên" thiếu vế "sụp đổ" tương xứng. Đây không phải màu sắc tùy chọn: mục "Narrative detail" và "Script-ready material" của mỗi tổ chức **bắt buộc** phải mang theo nhịp hậu quả/giải thể như một phần cấu trúc, không phải một đoạn có thể lược bỏ khi biên tập kịch bản.

Theo `DOMAIN_GUIDE.md` §4a Format 3: mỗi tổ chức dưới đây đủ điều kiện được nêu tên vì designation "tổ chức tội phạm" đến từ nguồn tier-1/tier-2 (phán quyết tư pháp, luật định danh, hoặc báo chí điều tra uy tín) — nhưng **việc nêu tên tổ chức không bao giờ cấp phép nêu tên một cá nhân thành viên chưa bị kết án cuối cùng là có tội về một hành vi cụ thể**. Bất kỳ cá nhân nào được nhắc đến ngoài phạm vi một bản án đã có hiệu lực pháp luật vẫn phải áp dụng đầy đủ ngôn ngữ hedged theo §4 (bị tình nghi/bị can/bị cáo).

Không mục nào trong packet này mô tả chi tiết vận hành có thể dùng như hướng dẫn thực hành (chiêu mộ, rửa tiền, buôn lậu vũ khí/ma túy, trốn tránh pháp luật, hệ thống liên lạc mật mã) — mọi nhắc đến các hoạt động này chỉ ở mức khái quát lịch sử. Không mục nào mô tả hay tái hiện phù hiệu/biểu tượng băng đảng theo cách có thể nhận dạng/sử dụng được — việc nêu tên một biểu tượng (ví dụ "phù hiệu 14K") là được phép, việc mô tả đủ chi tiết để tái tạo hoặc dùng để "nhận diện thành viên ngoài đời" thì không.

---

# Identity

## Canonical Name

Tổ Chức Tội Phạm (Organized Crime) — Pillar 5 của domain Hình Sự.

## Alternative Names

- Tội phạm có tổ chức
- Băng đảng / băng nhóm tội phạm
- Xã hội đen (cách gọi phổ thông tiếng Việt, gần nghĩa với "underworld"/tổ chức tội phạm ngầm)

## Related Terms

Cosa Nostra, Mafia, omertà, pentiti, Yakuza, oyabun/kobun, bōryokudan, Hội Tam Hoàng, Triad, Thiên Địa Hội, cartel, Trương Văn Cam/Năm Cam, tập đoàn tội phạm, bảo kê, MS-13, Mara Salvatrucha, clique/clica, Palabrero, IIRIRA, mano dura, chế độ ngoại lệ, Camorra, clan Casalesi, Roberto Saviano, Gomorra, Phiên tòa Spartacus.

## Keywords

Tổ chức tội phạm, mafia, Cosa Nostra, Sicilia, Maxi Trial, Falcone, Borsellino, Yakuza, oyabun, kobun, Bōtaihō, Hội Tam Hoàng, Triads, Thiên Địa Hội, 14K, Organized and Serious Crimes Ordinance, Năm Cam, Trương Văn Cam, tập đoàn tội phạm, Cartel Medellín, Pablo Escobar, Search Bloc, Narcos, phản khung lãng mạn hóa, MS-13, Mara Salvatrucha, Pico-Union Los Angeles, IIRIRA 1996, clique, Palabrero, RICO, mano dura, Nayib Bukele, CECOT, chế độ ngoại lệ, cảnh báo chính trị hóa/giật gân, Camorra, Naples, clan Casalesi, Roberto Saviano, Gomorra, Phiên tòa Spartacus.

---

# Historical Background (tổng quan liên tổ chức)

Bảy tổ chức trong packet này hình thành trong những bối cảnh lịch sử-xã hội rất khác nhau — nhà nước Ý mới thống nhất còn yếu ở Sicilia thế kỷ 19; các nhóm bên lề xã hội thời Mạc phủ Tokugawa; hội tương trợ dân gian Phúc Kiến thế kỷ 18; khoảng trống quản lý đô thị TP.HCM thời kỳ đổi mới; nền kinh tế buôn lậu lâu đời của Colombia; nội chiến El Salvador và một làn sóng tị nạn tại Mỹ, sau đó bị chính sách trục xuất "xuất khẩu" ngược về Trung Mỹ; hệ thống nhà tù Naples cuối thế kỷ 18 — nhưng có một mẫu số chung mà `DOMAIN_GUIDE.md` §8 yêu cầu làm khung phân tích xuyên suốt: **mỗi tổ chức lấp một khoảng trống quyền lực/quản lý nhà nước (hoặc, với MS-13, một khoảng trống bảo vệ cộng đồng nhập cư) tại một thời điểm cụ thể, và mỗi tổ chức đều có một quá trình bị nhà nước/nội bộ dẹp bỏ hoặc suy yếu được ghi chép tốt — kể cả khi, như với Camorra, quá trình đó mới thành công ở cấp từng clan cụ thể chứ chưa dẹp bỏ toàn bộ mạng lưới**. Đây là lăng kính phân tích-lịch sử-xã hội bắt buộc, không phải một chuỗi "7 câu chuyện phiêu lưu tội phạm".

Mọi jurisdiction phải được nêu rõ khi dựng kịch bản (`DOMAIN_GUIDE.md` §2): Ý (dân luật, hệ tòa 2-3 cấp + Tòa Phá án — áp dụng cho cả Cosa Nostra và Camorra), Nhật Bản, Hong Kong (thông luật thời thuộc địa Anh, nay là Đặc khu Hành chính Trung Quốc), Việt Nam (dân luật, 2 cấp xét xử sơ thẩm/phúc thẩm), Colombia/Mỹ (hệ phối hợp song phương, DEA hỗ trợ), El Salvador (dân luật; riêng giai đoạn "chế độ ngoại lệ" từ 2022 tạm ngưng một số quyền hiến định — cần nêu rõ đây là tình trạng pháp lý đặc biệt, không phải thủ tục tố tụng thông thường) và Mỹ liên bang (các vụ án RICO nhắm vào MS-13). Không được ngầm hiểu khái niệm tố tụng của nước này áp dụng cho nước khác.

---

# Canonical Sources

| Source | Mô tả | Tier / Độ tin cậy | Hướng dẫn sử dụng |
|---|---|---|---|
| `SOURCES/RESEARCH_DRAFT_TO_CHUC_TOI_PHAM.md` | Nghiên cứu nền cho cả 5 tổ chức: nguồn gốc, cấu trúc, hậu quả/giải thể, cảnh báo lãng mạn hóa (Escobar) | Hỗn hợp — Tier 1-2 cho số liệu tố tụng/luật định/sự kiện đã kiểm chứng chéo; Tier 3 cho truyền thuyết dân gian/chi tiết tường thuật báo chí điều tra dài kỳ | Nguồn chính duy nhất cho packet này; mọi claim giữ nguyên nhãn độ tin cậy gốc, không được làm phẳng |
| `KP_CL_002_An_Da_Xu.md` (đã tồn tại kể từ 2026-07-23) | Chứa tường thuật case/phiên tòa "Trương Văn Cam và đồng phạm" đầy đủ (Pillar 2) | Tier 1-2 cho số liệu tố tụng cốt lõi, kế thừa từ `RESEARCH_DRAFT_AN_DA_XU.md` | Mục 4 dưới đây chỉ tập trung cấu trúc tổ chức + mạng lưới cán bộ tha hóa, cross-reference KP_CL_002 cho narrative vụ án/phiên tòa; đã đối chiếu số liệu 155 bị can/bị cáo, 24 tội danh, 21 cán bộ nhà nước — khớp, không mâu thuẫn (xem "Cập nhật trạng thái" ở Packet Control) |
| `SOURCES/RESEARCH_DRAFT_TO_CHUC_TOI_PHAM_BATCH2.md` (research date 2026-07-24) | Nghiên cứu nền cho MS-13 và Camorra: nguồn gốc, cơ chế trục xuất/xuyên quốc gia hóa, cấu trúc, mano dura, cảnh báo chính trị hóa (MS-13); nguồn gốc, cấu trúc compare/contrast với Cosa Nostra, Saviano/Gomorra, Phiên tòa Spartacus (Camorra) | Hỗn hợp — Tier 1 cho số liệu tố tụng/luật định/sự kiện chính phủ (CRS, DOJ, Federal Register, DIA); Tier 2-3 cho báo chí điều tra, học thuật, fact-checking (InSight Crime, PolitiFact, ACAMS, University of Bath) | Nguồn chính cho mục 6 (MS-13) và mục 7 (Camorra); mọi claim giữ nguyên nhãn độ tin cậy gốc, không được làm phẳng — đặc biệt tiểu mục "Cảnh báo chính trị hóa/giật gân" của MS-13 phải mang theo nguyên vẹn |

## Source Priority Hierarchy (tái hiện từ `DOMAIN_GUIDE.md` §3)

| Tier | Loại nguồn | Ví dụ trong packet này |
|---|---|---|
| 1 | Phán quyết tư pháp, luật định, thống kê cơ quan nhà nước chính thức | Bản án Maxi Trial (Tòa Phá án Ý), luật Bōtaihō, OSCO Hong Kong, bản án Trương Văn Cam, số liệu Cơ quan Cảnh sát Quốc gia Nhật Bản |
| 2 | Báo chí điều tra uy tín, tên tuổi | SCMP, TIME, CAND, Tuổi Trẻ, InSight Crime |
| 3 | Học thuật criminology/lịch sử-xã hội, sách/tài liệu có trích dẫn | Nghiên cứu kinh tế Alesina/Dalmazzo/De Blasio, nghiên cứu Qin Baoqi về Thiên Địa Hội, Cambridge Urban History |
| 4-5 | Nguồn phổ thông (Wikipedia-tier) — chỉ dùng cross-check, không phải nguồn độc quyền | Wikipedia EN/VN cho mốc thời gian, chỉ dùng khi đã đối chiếu ≥1 nguồn tier 1-3 |

## Khoảng trống nguồn (Known Gaps)

- ~~KP_CL_002 chưa tồn tại~~ — **đã giải quyết 2026-07-23:** `KP_CL_002_An_Da_Xu.md` nay đã được soạn xong; mục Năm Cam dưới đây đã được rà soát và đối chiếu số liệu, khớp hoàn toàn (155 bị can/bị cáo, 24 tội danh, 21 cán bộ nhà nước) — xem "Cập nhật trạng thái" ở Packet Control.
- Vai trò/mức độ liên hệ chính thức của "Los Pepes" với Cartel Cali/lực lượng an ninh nhà nước Colombia trong quá trình truy bắt Escobar — độ tin cậy trung bình-cao nhưng còn nhiều góc nhìn gây tranh cãi, chưa hoàn toàn xác nhận chính thức ở mọi chi tiết.
- Số liệu quy mô hoạt động Cartel Medellín (80% cocaine vào Mỹ, ~15 tấn/ngày, ~100 triệu USD/ngày) là ước tính của cơ quan thực thi pháp luật thời kỳ đó, không phải số liệu kiểm toán độc lập — cần trình bày kèm "ước tính".
- Truyền thuyết "phản Thanh phục Minh" của Thiên Địa Hội — độ tin cậy thấp/mang tính dân gian, xem cảnh báo riêng trong mục Hội Tam Hoàng.
- Số liệu trục xuất cụ thể liên quan MS-13 (20.000 người 2000-2004 vs. gần 130.000 người 2001-2010) đến từ hai ước tính khác nguồn/phạm vi thời gian — cần nêu cả hai kèm nguồn, không chọn một số duy nhất (xem mục 6).
- Số liệu người chết trong trại giam El Salvador dưới "chế độ ngoại lệ" dao động 261-517 người tùy nguồn/thời điểm thống kê — chưa có con số chốt được mọi tổ chức nhân quyền đồng thuận (xem mục 6).
- Mức độ tranh luận học thuật về "hierarchical in form but fragmented in practice" của MS-13 — một số nghiên cứu 2025 cho rằng mạng lưới có thể liên kết chặt hơn nhận định phổ biến trước đây; chưa có đồng thuận học thuật cuối cùng (xem mục 6).
- Mốc thời gian cụ thể của việc Saviano sống dưới bảo vệ vũ trang (một số nguồn nêu "tám năm", nhiều nguồn khác xác nhận việc bảo vệ vẫn tiếp diễn tới gần hiện tại) — nguồn không đồng nhất về một con số năm chính xác (xem mục 7).

---

# Topic Sections

Mỗi mục dưới đây theo cấu trúc 5 phần: **Knowledge function / Primary concepts / Narrative detail / Script-ready material / Production cautions** (mô phỏng định dạng đã dùng ở `KP_FS_001`).

## 1. Cosa Nostra / Mafia Sicilia (Ý)

### Knowledge function

Cosa Nostra là ví dụ kinh điển nhất để dạy khán giả một nguyên lý xuyên suốt cả pillar: tổ chức tội phạm có tổ chức thường lấp một khoảng trống quyền lực nhà nước cụ thể, và có thể bị chính hệ thống tư pháp — dù chậm và trả giá đắt — lột trần và giam giữ. Đây là mục mở đầu tự nhiên cho chuỗi Pillar 5 vì có tư liệu tư pháp chính thức (Maxi Trial) đầy đủ và rõ ràng nhất trong 5 tổ chức.

### Primary concepts

- Hình thành thế kỷ 19 gắn với sự sụp đổ chế độ phong kiến Sicilia và nhà nước Ý thống nhất còn yếu (ước tính chưa tới 350 cảnh sát toàn đảo ở một thời điểm) — độ tin cậy cao.
- "Gabellotto" — người thuê đất kiêm tổ chức vệ binh tư nhân — là hạt nhân tổ chức tiền thân của các "gia đình" mafia.
- Cấu trúc: "gia đình" (cosche/famiglie) theo địa bàn, "Ủy ban" (Commissione) điều phối liên gia đình, phân cấp nội bộ capo/sottocapo/consigliere/soldati/associates.
- "Omertà" — quy tắc im lặng tuyệt đối — cơ chế duy trì kỷ luật và cản trở điều tra trong nhiều thập niên.
- "Pentiti" (người hợp tác với công lý, ví dụ Tommaso Buscetta, Salvatore Contorno) — nhân tố phá vỡ omertà, cung cấp "học thuyết Buscetta" cho công tố.

### Narrative detail

**Phần trọng tâm bắt buộc (§8), không phải màu sắc phụ.** Cơ chế omertà và cấu trúc bí mật của Cosa Nostra cuối cùng bị phá vỡ bởi chính nỗ lực điều tra/tư pháp của nhà nước Ý — tiêu biểu nhất là **"Phiên tòa Lớn" (Maxi Trial) tại Palermo**, khai mạc 10/2/1986, xét xử 475 thành viên mafia (120 vụ giết người, buôn ma túy, tống tiền, và tội danh mới "thành viên tổ chức tội phạm kiểu mafia"). Hai thẩm phán điều tra **Giovanni Falcone** và **Paolo Borsellino**, thuộc nhóm "Antimafia Pool", dẫn đầu nỗ lực này dựa trên lời khai đột phá của các pentiti. Kết quả: 338 bị cáo bị kết án, tổng 2.665 năm tù cộng 19 án chung thân; Tòa Phá án Ý giữ nguyên bản án 30/1/1992. **Cái giá phải trả** — và là phần không thể lược khi kể câu chuyện này: cả hai công tố viên chủ chốt bị Cosa Nostra ám sát trả thù ngay sau đó — Falcone bị đánh bom tại Capaci 23/5/1992 (cùng vợ và 3 vệ sĩ), Borsellino bị đánh bom xe 19/7/1992, chỉ 57 ngày sau. Hai vụ ám sát này gây chấn động toàn nước Ý, dẫn tới làn sóng luật chống mafia mới và huy động lực lượng lớn hơn — về lâu dài làm suy yếu thêm khả năng hoạt động công khai của Cosa Nostra. Khung đúng cho kịch bản: nhà nước pháp quyền — dù chậm và trả giá bằng sinh mạng — cuối cùng dùng chính hệ thống tư pháp để lột trần và giam giữ một tổ chức từng bị xem là "không thể đụng tới"; không phải câu chuyện "mafia bất khả chiến bại."

### Script-ready material

- Cấu trúc song song: từ "khoảng trống nhà nước yếu" (gabellotto lấp khoảng trống) đến "nhà nước mạnh trở lại" (Maxi Trial) — khung hai vế rõ ràng, tự nhiên cho một tập phim có mở đầu/kết thúc cân xứng.
- "Học thuyết Buscetta" — điểm ngoặt tình báo/tư pháp, có thể dùng làm nút thắt kịch tính hợp pháp (không cần dựng lại chi tiết vận hành mafia).
- Falcone và Borsellino — hai nhân vật anh hùng công vụ thực, cái chết của họ là hồi kết cảm xúc bắt buộc, cân bằng lại mọi phần "cấu trúc/quyền lực" đã kể trước đó.
- Con số 2.665 năm tù/19 án chung thân — số liệu ấn tượng, an toàn để dùng nguyên văn vì có nguồn tier 1-2.

### Production cautions

- **Thực thi §8 (non-glorification/no-operational-detail):** không mô tả chi tiết vận hành nội bộ gia đình mafia (cách thu tiền bảo kê cụ thể, cách "kết nạp" cụ thể) theo cách có thể học theo; chỉ mô tả cấu trúc phân cấp ở mức khái quát lịch sử-xã hội. Trọng tâm tường thuật luôn là Maxi Trial + cái chết của Falcone/Borsellino — đây là phần bắt buộc, không phải đoạn có thể cắt để "dành thời lượng cho phần trỗi dậy."
- **Thực thi §4a Format 3:** Cosa Nostra đủ điều kiện nêu tên vì designation "tổ chức tội phạm mafia" đến từ chính phán quyết tư pháp Ý (tier 1). Tuy nhiên, việc nêu tên tổ chức không cấp phép gọi bất kỳ thành viên/associate nào ngoài phạm vi 338 bị cáo đã bị kết án cuối cùng trong Maxi Trial là "có tội" — với các cá nhân đó vẫn cần áp dụng §4 (bị tình nghi/bị can/bị cáo) nếu chưa có bản án cuối cùng.
- Nhãn độ tin cậy: nguồn gốc kinh tế-xã hội — cao (xác nhận thống nhất Britannica, HISTORY.com, nghiên cứu kinh tế bình duyệt, tier 2-3). Số liệu Maxi Trial và ngày ám sát — cao (khớp giữa Wikipedia EN và nhiều nguồn báo chí/học thuật độc lập, tier 2).

---

## 2. Yakuza (Nhật Bản)

### Knowledge function

Yakuza là ví dụ duy nhất trong 7 tổ chức từng tồn tại bán công khai, được xã hội "dung thứ" trong phần lớn lịch sử hiện đại — một điểm giáo dục quý giá để dạy khán giả phân biệt "được dung thứ" với "được chấp nhận đạo đức", và để minh họa cách một nhà nước chuyển từ khoan dung sang trấn áp có hệ thống bằng công cụ luật pháp dân sự (không chỉ hình sự).

### Primary concepts

- Gốc gác thời Mạc phủ Tokugawa (thế kỷ 17-18) từ hai nhóm bên lề: "bakuto" (cờ bạc rong) và "tekiya" (bán hàng rong/chợ phiên).
- Tên gọi "yakuza" xuất phát từ một bộ bài xấu vô giá trị (8-9-3, "ya-ku-sa") trong trò bài truyền thống của bakuto.
- Vị thế bán công khai lịch sử: văn phòng, danh thiếp, tạp chí riêng ở nhiều giai đoạn — khác biệt rõ với hầu hết tổ chức tội phạm khác trên thế giới.
- Cấu trúc "cha-con" hình thức (không huyết thống): "oyabun" (thủ lĩnh) và "kobun" (đàn em), tạo kim tự tháp phân tầng.

### Narrative detail

**Phần trọng tâm bắt buộc (§8).** Từ đầu thập niên 1990, Nhật Bản chuyển hướng rõ rệt từ dung thứ sang trấn áp có hệ thống bằng luật pháp: **Luật chống Bōryokudan (Bōtaihō) năm 1992** là đạo luật lớn đầu tiên nhắm trực tiếp vào các tổ chức yakuza được chỉ định; **sửa đổi 2008** quy định trách nhiệm dân sự của thủ lĩnh với hành vi cấp dưới; **các Sắc lệnh Loại trừ Bōryokudan** cấp tỉnh (Saga ban hành đầu tiên năm 2009, phủ toàn bộ 47 tỉnh/thành đến cuối 2011) cấm công dân/doanh nghiệp giao dịch thường xuyên với thành viên tổ chức tội phạm. **Kết quả định lượng — phần bắt buộc phải có mặt trong mọi kịch bản về Yakuza:** số thành viên sụt từ hơn 80.000 người (2009) xuống còn khoảng 17.600-18.800 người (2024-2025, theo Cơ quan Cảnh sát Quốc gia Nhật Bản) — năm suy giảm liên tiếp thứ 20, mức thấp kỷ lục mới. Khung đúng cho kịch bản: "từ một thực thể bán công khai, được xã hội dung thứ, đến một tổ chức bị luật pháp siết chặt từng bước và suy giảm liên tục hơn 20 năm" — không phải "yakuza vẫn hùng mạnh và bí ẩn," một khung dễ trượt sang lãng mạn hóa.

### Script-ready material

- Nghịch lý mở đầu tập hấp dẫn: "một tổ chức tội phạm từng có danh thiếp và văn phòng công khai" — hook tự nhiên, không cần phóng đại.
- Đường cong suy giảm 20 năm liên tiếp (80.000 → dưới 19.000) — dữ liệu định lượng mạnh, dễ trực quan hóa thành biểu đồ, đồng thời tự nó đã là "hồi kết" của câu chuyện mà không cần thêm kịch tính giả tạo.
- Cấu trúc oyabun-kobun — dùng để giải thích khái niệm trung thành/tổ chức, không cần mô tả nghi thức kết nạp cụ thể.

### Production cautions

- **Thực thi §8:** tuyệt đối không mô tả nghi thức kết nạp cụ thể hay bất kỳ chi tiết vận hành tài chính/thu phí bảo kê nào ở mức đủ để làm theo — chỉ mô tả quan hệ oyabun-kobun ở mức khái niệm cấu trúc. Vị thế "bán công khai" lịch sử của yakuza **không được** trình bày theo hướng khiến tổ chức trông "đáng nể" hay "có quy tắc danh dự đáng ngưỡng mộ" — luôn gắn kèm hệ quả pháp lý hiện đại (Bōtaihō, sắc lệnh loại trừ, sụt giảm thành viên) trong cùng đoạn.
- **Thực thi §4a Format 3:** Yakuza/bōryokudan là designation chính thức từ luật Nhật Bản (tier 1) — đủ điều kiện nêu tên tổ chức, nhưng không cấp phép gọi tên bất kỳ cá nhân thành viên cụ thể nào là có tội nếu không có bản án cuối cùng.
- Nhãn độ tin cậy: nguồn gốc lịch sử (bakuto/tekiya) — cao (Britannica, Wikipedia EN, nguồn lịch sử phổ thông, tier 2-5 cross-checked). Số liệu suy giảm thành viên — cao (báo cáo trực tiếp từ Cơ quan Cảnh sát Quốc gia Nhật Bản, tier 1-2).

---

## 3. Hội Tam Hoàng / Triads (Hong Kong / Trung Quốc)

### Knowledge function

Hội Tam Hoàng là ví dụ tốt nhất trong packet để dạy khán giả phân biệt giữa **truyền thuyết dân gian** và **sử liệu đã kiểm chứng**, đồng thời minh họa rằng "một tổ chức tội phạm thống nhất, có chỉ huy trung ương" là hiểu lầm phổ biến cần tháo gỡ — thực tế là mạng lưới phân tán nhiều nhóm độc lập.

### Primary concepts

- Tiền thân được công nhận rộng rãi nhất: **Thiên Địa Hội** (Tiandihui/Hongmen), thành lập tại Phúc Kiến khoảng 1761-1762 — ban đầu là **hội tương trợ** bình dân, không phải tổ chức tội phạm ngay từ đầu (theo phân tích của học giả Qin Baoqi dựa trên văn khố nhà Thanh, nguồn có thẩm quyền, tier 3).
- **Cờ đỏ cảnh báo bắt buộc:** truyền thuyết dân gian gán cho hội này nguồn gốc "phản Thanh phục Minh" mang màu sắc anh hùng — nhưng theo hồ sơ lịch sử xác thực, nguồn gốc thực tế mang tính "tương trợ đời thường" hơn là hội kháng chiến chính trị có tổ chức. **Đây là truyền thuyết dân gian, không phải sự kiện lịch sử đã kiểm chứng hoàn toàn** — phải luôn gắn ngôn ngữ "tương truyền"/"theo truyền thuyết dân gian", không bao giờ trình bày như sử liệu xác thực.
- Chính quyền thuộc địa Anh cấm hội Tam Hoàng tại Hong Kong từ 1845; các hội từng chi phối một phần thị trường lao động bến cảng từ khoảng 1857.
- **Không tồn tại một "Hội Tam Hoàng" thống nhất, có chỉ huy trung ương duy nhất** — mà là nhiều nhóm/phân nhánh tách biệt, phân tán, mỗi nhóm mang tên riêng (ví dụ 14K, Sun Yee On, Wo Shing Wo). "Tổ chức mẹ" (Thiên Địa Hội) chỉ để lại khuôn mẫu chung về cấu trúc/nghi thức, không phải chuỗi chỉ huy thống nhất.

### Narrative detail

**Phần trọng tâm bắt buộc (§8).** Hong Kong ban hành **Pháp lệnh Tội phạm Nghiêm trọng và Có Tổ chức (Organized and Serious Crimes Ordinance — OSCO)** năm 1994/có hiệu lực 1995, sau một báo cáo mật của giới lãnh đạo cảnh sát năm 1994 mô tả hội Tam Hoàng là "mối đe dọa cho xã hội" và cảnh báo luật này là cấp thiết; OSCO cho phép điều tra có mục tiêu vào cấp lãnh đạo cao thay vì chỉ xử lý thành viên cấp thấp. Luật song song **Societies Ordinance** hình sự hóa cả hành vi tự nhận là thành viên hội Tam Hoàng. Cảnh sát Hong Kong duy trì các chiến dịch trấn áp định kỳ qua đơn vị "Organised Crime and Triad Bureau" — ví dụ một chiến dịch bắt 185 người trong 3 ngày, một đợt khác bắt 4.343 nghi phạm. **Xu hướng hiện tại — phần bắt buộc để tránh lãng mạn hóa:** nghiên cứu tại Đại học Thành thị Hong Kong ghi nhận quyền lực công khai của hội Tam Hoàng "kém rõ ràng hơn nhiều" so với trước 1997; cấu trúc chuyển từ phân cấp cứng sang mạng lưới lỏng lẻo, nhiều thủ lĩnh 14K bị bỏ tù, và xu hướng chuyển sang kinh doanh hợp pháp phản ánh sự suy yếu của mô hình bạo lực công khai truyền thống. Khung đúng cho kịch bản: từ hội tương trợ dân gian, qua giai đoạn bị chính quyền thuộc địa cấm và đẩy vào hoạt động ngầm, đến bị luật hình sự hiện đại (OSCO) nhắm mục tiêu trực diện vào cấp lãnh đạo — không phải câu chuyện "hội kín bất khả xâm phạm."

### Script-ready material

- "Twist" giáo dục kép: (1) nguồn gốc thật là hội tương trợ, không phải hội kháng chiến anh hùng như truyền thuyết; (2) không có một "Hội Tam Hoàng" duy nhất mà là mạng lưới phân tán — hai điểm sửa hiểu lầm phổ biến, hấp dẫn tự nhiên mà không cần dựng kịch.
- OSCO 1994/1995 như bước ngoặt pháp lý — dễ kể như "luật thay đổi cách nhà nước săn lùng cấp lãnh đạo, không chỉ cấp dưới".
- Số liệu chiến dịch trấn áp (185 người/3 ngày; 4.343 nghi phạm) — dữ liệu cụ thể, an toàn dùng nguyên văn vì nguồn tier 2 (SCMP, TIME).

### Production cautions

- **Thực thi §8:** phải gắn nhãn "truyền thuyết dân gian"/"tương truyền" mỗi khi nhắc "phản Thanh phục Minh" — không bao giờ trình bày như sự kiện lịch sử xác thực. Không mô tả nghi thức kết nạp, hệ thống ám hiệu, hay bất kỳ phù hiệu/biểu tượng nào theo cách có thể nhận dạng hoặc tái tạo được — chỉ được nêu tên biểu tượng ở mức khái quát lịch sử (ví dụ "hội có hệ thống nghi thức và biểu tượng riêng"), không mô tả hình dạng/nội dung cụ thể.
- **Thực thi §4a Format 3:** các nhóm cụ thể (14K, Sun Yee On, Wo Shing Wo...) đủ điều kiện nêu tên vì designation đến từ luật Hong Kong (tier 1); nhưng nêu tên nhóm không cấp phép gọi bất kỳ cá nhân nào là thành viên có tội nếu chưa có bản án cuối cùng — kể cả khi báo chí đã "nghi ngờ" liên hệ.
- Nhãn độ tin cậy: nguồn gốc Thiên Địa Hội (Qin Baoqi) — cao, được giới sử học công nhận thẩm quyền (tier 3). Cấu trúc phân tán — cao (Wikipedia EN + Cambridge). Số liệu OSCO/chiến dịch — cao (tier 2, SCMP/TIME + văn bản luật). Truyền thuyết "phản Thanh phục Minh" — **thấp/mang tính truyền thuyết dân gian**, phải gắn nhãn rõ mỗi lần dùng.

---

## 4. Băng nhóm Năm Cam (Việt Nam)

**Cross-reference bắt buộc:** mục này tập trung **cấu trúc tổ chức và mạng lưới cấu kết với cán bộ tha hóa** của băng nhóm Năm Cam; tường thuật chi tiết vụ án/phiên tòa "Trương Văn Cam và đồng phạm" (2003-2004) — diễn biến điều tra, các phiên xét xử, phản ứng dư luận — thuộc phạm vi của `KP_CL_002_An_Da_Xu.md` (Pillar 2, Án Đã Xử) và **không được lặp lại đầy đủ ở đây** để tránh trùng lặp nội dung giữa hai Knowledge Packet. Tại thời điểm soạn packet này, KP_CL_002 **chưa tồn tại** trên hệ thống — xem "Khoảng trống phụ thuộc" ở Packet Control; số liệu tố tụng dưới đây được giữ ở mức tối thiểu cần thiết để mục "Góc độ hậu quả/giải thể" không rỗng, và cần đối chiếu lại với KP_CL_002 ngay khi packet đó ra đời.

### Knowledge function

Băng nhóm Năm Cam là ví dụ duy nhất trong 5 tổ chức xảy ra tại Việt Nam và có bản án đã có hiệu lực pháp luật — đủ điều kiện Format 1 (`DOMAIN_GUIDE.md` §4a) để nêu tên/mô tả factual đối với Năm Cam và các đồng phạm đã bị kết án cuối cùng. Vai trò sư phạm đặc biệt của mục này: minh họa cách một tổ chức tội phạm nội địa vươn tới quy mô lớn được **thông qua cấu kết với chính bộ máy nhà nước tha hóa** — khác về bản chất với 4 tổ chức còn lại, vốn chủ yếu đối đầu trực diện với nhà nước.

### Primary concepts

- Trương Văn Cam (biệt danh "Năm Cam", sinh 22/4/1947 tại TP.HCM) — người đứng đầu tổ chức tội phạm có tổ chức lớn nhất TP.HCM tồn tại nhiều năm, hoạt động ngầm từ thập niên 1990 đến khi bị triệt phá 2001-2002.
- Mô hình kinh tế ngầm: đường dây "bảo kê" cho sòng bạc đổi lấy khoản tiền hằng tháng, mở rộng sang bảo kê buôn lậu/vận chuyển hàng cấm; nguồn thu được dùng lập doanh nghiệp tư nhân — vừa che giấu nguồn gốc bất hợp pháp, vừa né tránh sự chú ý điều tra (mô tả ở mức khái quát lịch sử, không đủ chi tiết để làm theo).
- Mạng lưới đàn em trải rộng Nam ra Bắc, quan hệ trực tiếp/gián tiếp với nhiều nhóm tội phạm địa phương; báo chí trong nước mô tả tổ chức này như một "tập đoàn tội phạm" do quy mô và độ phức tạp mạng lưới.
- **Điểm đặc biệt nghiêm trọng, làm nên ý nghĩa lịch sử của vụ án vượt xa một vụ án hình sự thông thường:** tổ chức cấu kết được với một mạng lưới cán bộ thoái hóa, biến chất trong chính bộ máy nhà nước — bao gồm cả những người có trách nhiệm trực tiếp trong công tác phòng chống tội phạm.

### Narrative detail

**Phần trọng tâm bắt buộc (§8) — trình bày tối giản, dẫn chiếu KP_CL_002 cho chi tiết đầy đủ.** Vụ án "Trương Văn Cam và đồng phạm" là một trong những vụ án hình sự quy mô lớn nhất lịch sử tố tụng Việt Nam: 155 bị cáo bị truy tố về 24 tội danh khác nhau, trong đó có 21 người là cán bộ nhà nước/lực lượng chức năng (công an, kiểm sát viên, cán bộ hành chính) và 17 đảng viên — phản ánh đúng mức độ cấu kết giữa tổ chức tội phạm và một bộ phận cán bộ tha hóa. Năm Cam bị tuyên án tử hình (tổng hợp 7 tội danh); bản án phúc thẩm giữ nguyên, thi hành án tháng 6/2004. Một số cán bộ từng giữ chức vụ cao cũng bị xét xử và tuyên án tù vì nhận hối lộ/lợi dụng chức vụ, thể hiện rõ khía cạnh "vừa triệt phá tội phạm có tổ chức, vừa mang ý nghĩa chống tham nhũng trong bộ máy nhà nước." **Diễn biến đầy đủ của quá trình điều tra, hai phiên xét xử sơ thẩm/phúc thẩm, và tường thuật nhân vật/con người liên quan thuộc phạm vi `KP_CL_002_An_Da_Xu.md` — mục này không lặp lại.** Khung đúng cho kịch bản: một mạng lưới tội phạm tưởng như "bất khả xâm phạm" nhờ quan hệ với cán bộ tha hóa, cuối cùng bị phanh phui và xử lý toàn diện — cả kẻ cầm đầu lẫn cán bộ tiếp tay — bằng một chuyên án điều tra quy mô lớn của cơ quan chức năng. Trọng tâm là quá trình phá án và xét xử, không phải chi tiết "cách Năm Cam đã lách luật" theo hướng có thể học theo.

### Script-ready material

- Góc kể "tổ chức tội phạm + tham nhũng nhà nước" — khác biệt hóa mục này so với 4 tổ chức quốc tế còn lại, tự nhiên làm điểm neo bản sắc Việt Nam cho pillar.
- Con số 155 bị cáo/24 tội danh/21 cán bộ nhà nước/17 đảng viên — dữ liệu định lượng mạnh, tự thân đã truyền tải quy mô "dọn dẹp" mà không cần phóng đại.
- Điểm nối kịch bản sang KP_CL_002: mục này nên kết bằng một câu dẫn ("câu chuyện đầy đủ về cách chuyên án phá vỡ mạng lưới này được kể chi tiết ở tập [X]") thay vì cố kể lại toàn bộ.

### Production cautions

- **Thực thi §8:** mô tả mô hình bảo kê/rửa nguồn thu qua doanh nghiệp chỉ ở mức khái quát lịch sử-xã hội (đã nêu ở Primary concepts) — tuyệt đối không đi sâu cơ chế cụ thể ("cách Năm Cam đã lách luật") theo hướng người xem có thể học theo, đúng cảnh báo mà chính research draft đã ghi rõ.
- **Thực thi §4a Format 3 và §4:** Năm Cam và các đồng phạm chính đã có bản án có hiệu lực pháp luật — có thể nêu tên/mô tả factual (Format 1). Nhưng **bất kỳ cá nhân nào khác được nhắc đến ngoài phạm vi bản án đã công bố** (ví dụ nghi vấn liên quan chưa qua xét xử) vẫn phải áp dụng đầy đủ ngôn ngữ hedged của §4 — việc nêu tên tổ chức/vụ án không tự động cấp phép gọi tên thêm cá nhân khác là có tội.
- **Cross-reference bắt buộc:** không sao chép lặp nguyên văn narrative vụ án từ mục này sang kịch bản Pillar 2 hoặc ngược lại — luôn dẫn chiếu KP_CL_002 cho phần case/trial, giữ mục này tập trung vào cấu trúc tổ chức + mạng lưới cán bộ tha hóa. Khi KP_CL_002 được soạn, rà soát lại đoạn Narrative detail ở trên để đảm bảo số liệu khớp và không trùng lặp câu chữ.
- Nhãn độ tin cậy: số liệu tố tụng (155 bị cáo, 24 tội danh, 21 cán bộ, 17 đảng viên, ngày xét xử, mức án, ngày thi hành án) — cao (khớp giữa Wikipedia tiếng Việt và báo chí trong nước uy tín CAND/Tuổi Trẻ, tier 1-2). Mô tả cấu trúc/quy mô mạng lưới đàn em cụ thể — trung bình (chủ yếu báo chí điều tra dài kỳ, tier 2, mang tính tường thuật) — tránh dùng để suy diễn chi tiết vận hành ngoài phạm vi đã tường thuật công khai.

---

## 5. Cartel Medellín dưới thời Pablo Escobar (Colombia)

### Knowledge function

Cartel Medellín/Pablo Escobar là **trường hợp rủi ro lãng mạn hóa cao nhất trong cả 7 tổ chức của packet này**, do ảnh hưởng của các sản phẩm giải trí đại chúng (đặc biệt loạt phim Netflix "Narcos") — MS-13 (mục 6) mang một rủi ro khác về bản chất (chính trị hóa/giật gân, không phải lãng mạn hóa), xem mục đó. Đây là mục đòi hỏi một tầng phòng vệ biên tập bổ sung ngoài khung 5 phần thông thường — xem "Cảnh báo lãng mạn hóa" riêng bên dưới, tách biệt khỏi "Production cautions" chung.

### Primary concepts

- Hình thành đầu thập niên 1970, phát triển từ nền kinh tế buôn lậu lâu đời của Colombia, mở rộng khi cocaine thay thế cần sa/hàng buôn lậu khác thành mặt hàng xuất khẩu bất hợp pháp chủ lực.
- Sáng lập bởi Pablo Escobar cùng anh em nhà Ochoa (Jorge Luis, Juan David, Fabio) và các cộng sự Gonzalo Rodríguez Gacha ("El Mexicano"), Carlos Lehder ("El Loco").
- Quy mô đỉnh cao (ước tính của cơ quan thực thi pháp luật thời kỳ đó, không phải số liệu kiểm toán độc lập — cần trình bày kèm "ước tính"): hơn 80% cocaine buôn lậu vào Mỹ đầu thập niên 1980, ~15 tấn/ngày, lợi nhuận ước ~100 triệu USD/ngày, có giai đoạn ước chiếm ~96% thị phần cocaine nhập vào Mỹ.
- Cấu trúc: không phải một tổ chức phân cấp đơn nhất mà **một mạng lưới các trùm buôn lậu bán độc lập**, hợp tác trong sản xuất/vận chuyển/tài trợ vốn/"thực thi kỷ luật nội bộ" (thuật ngữ khái quát), mỗi trùm giữ quyền kiểm soát độc lập mảng riêng. Duy trì vị thế bằng kết hợp bạo lực cực đoan và tha hóa định chế nhà nước (hối lộ quan chức, thẩm phán, an ninh), loại bỏ đối thủ/người chỉ trích bằng đánh bom/bắt cóc/ám sát (chỉ nêu như sự kiện lịch sử, không mô tả chi tiết kỹ thuật).

### Narrative detail

**Phần trọng tâm bắt buộc (§8) — phải chiếm trọng lượng tường thuật tương đương hoặc lớn hơn phần "trỗi dậy".** Chính quyền Colombia thành lập **"Search Bloc" (Bloque de Búsqueda)** năm 1989 — đơn vị cảnh sát tinh nhuệ khoảng 600 người, đóng tại trường cảnh sát Carlos Holguín ở Medellín — với nhiệm vụ săn lùng Escobar; tái lập sau khi ông trốn khỏi nhà tù do chính ông "thương lượng" xây dựng và kiểm soát năm 1992. Search Bloc nhận hỗ trợ kỹ thuật/tình báo từ DEA và đặc nhiệm quân đội Mỹ. Escobar bị **tiêu diệt ngày 2/12/1993** tại Medellín, sau khi bị định vị qua một cuộc gọi điện thoại tới gia đình, cố chạy trốn qua mái nhà nhưng bị bắn hạ. Song song còn có nhóm **"Los Pepes"** ("Persegidos por Pablo Escobar") — cựu đồng minh, lực lượng bán vũ trang, một số nạn nhân phẫn nộ, được cho là có liên hệ tài trợ từ Cartel Cali — dùng bạo lực ngoài vòng pháp luật để truy đuổi Escobar và người liên quan; đây là khía cạnh phức tạp, gây tranh cãi (không phải chiến dịch thực thi pháp luật thuần túy), cần trình bày trung thực, không tô hồng bất kỳ bên nào. Ngay sau cái chết của Escobar, cartel Medellín **sụp đổ nhanh chóng**, kết thúc một thời kỳ buôn lậu cocaine và mở đường tạm thời cho Cartel Cali trước khi cũng bị triệt phá các năm sau. Khung đúng cho kịch bản: "cái kết" (Search Bloc, cái chết 1993, sự sụp đổ ngay sau đó của cartel) phải có trọng lượng tường thuật tương đương hoặc lớn hơn phần "sự trỗi dậy" — không có "rise" mà thiếu "fall" tương xứng, đúng tinh thần §8.

### Script-ready material

- Cấu trúc hai vế cân xứng bắt buộc: mọi số liệu về quy mô/lợi nhuận (Primary concepts) phải được đặt cạnh — không tách rời khỏi — số liệu về thiệt hại xã hội (xem Cảnh báo lãng mạn hóa) và kết cục bị săn lùng.
- Search Bloc — nhân vật tập thể phù hợp làm trọng tâm tường thuật hồi kết (thay vì cho Escobar "độc chiếm" toàn bộ mạch truyện).
- Ngày 2/12/1993 và chi tiết bị định vị qua cuộc gọi điện thoại — điểm kết an toàn, có nguồn tier 2 vững, không cần dựng thêm kịch tính.

### Cảnh báo lãng mạn hóa

**Đây là tiểu mục bắt buộc riêng cho tổ chức này** (yêu cầu nhiệm vụ, không phải phần tùy chọn), mang theo phát hiện của research draft gốc để chủ động phản khung (counter-frame) ngay từ đầu quá trình lên kịch bản — không chỉ dựa vào việc tự động "hedge" ở câu chữ:

- Loạt phim **"Narcos" (Netflix)** bị chỉ trích rộng rãi vì khắc họa Escobar theo hướng dễ mến, kiểu "người cha gia đình đáng yêu" — trong khi tại Colombia, nhắc đến Escobar với thái độ tôn kính/ngưỡng mộ bị xem là một điều cấm kỵ lớn (có nguồn ví việc này với việc ca ngợi Osama bin Laden tại Mỹ).
- Bối cảnh thực tế mà "Narcos" và sản phẩm giải trí tương tự thường làm mờ đi: cuộc chiến ma túy/bạo lực liên quan các cartel Colombia (không chỉ Medellín) được ước tính khiến khoảng **260.000 người thiệt mạng và 7 triệu người phải di dời** trong suốt giai đoạn xung đột kéo dài.
- Người Colombia từng sống qua thời kỳ khủng bố của Escobar (đặc biệt Medellín) từng phản ánh việc các sản phẩm giải trí này góp phần gắn định kiến tiêu cực về ma túy/bạo lực lên hình ảnh đất nước họ.
- Ngay cả gia đình Escobar cũng phản ứng trái chiều gây tranh cãi (con trai liệt kê "sai sót thực tế" của phim, em trai từng đe dọa kiện Netflix vì sở hữu trí tuệ) — cho thấy diễn ngôn xung quanh nhân vật này đã bị thương mại hóa/tranh chấp hình ảnh theo nhiều chiều; kênh này nên giữ khoảng cách, không lặp lại kiểu tranh chấp hình ảnh đó.
- **Hướng dẫn phản khung cụ thể cho biên kịch tương lai:**
  1. **Trung tâm hóa góc nhìn nạn nhân/người sống sót Colombia**, không phải "thiên tài"/lối sống của trùm ma túy — mọi đoạn mô tả quy mô tài chính/quyền lực của Escobar phải đi kèm ngay số liệu thiệt hại con người (260.000 người chết, 7 triệu người di dời) trong cùng nhịp kể, không tách xa nhau trong kết cấu tập phim.
  2. Tránh mọi nhịp điệu tường thuật kiểu "từ tay trắng vươn lên làm ông trùm quyền lực" mà không đặt song song, cân xứng ngay từ đầu với quy mô thiệt hại xã hội.
  3. Các vụ bạo lực nhắm vào dân thường (ví dụ vụ đánh bom máy bay Avianca) chỉ nên nêu như sự kiện lịch sử để minh họa hậu quả — không mô tả chi tiết kỹ thuật.
  4. Không dùng khung "gia đình đáng yêu"/"Robin Hood hiện đại" mà Narcos và một số truyền thông đại chúng từng dùng — đây chính xác là khung bị chỉ trích tại Colombia và là ranh giới cần chủ động tránh, không đợi QA phát hiện sau.

### Production cautions

- **Thực thi §8:** trọng tâm tường thuật là Search Bloc + cái chết 1993 + sự sụp đổ ngay sau đó — không phải lối sống/sự giàu có của Escobar. Không mô tả chi tiết kỹ thuật vận chuyển/buôn lậu (đường bay, phương thức giấu hàng, mạng lưới hối lộ cụ thể) theo cách có thể học theo — chỉ nêu ở mức khái quát lịch sử-xã hội như đã làm ở Primary concepts.
- **Thực thi §4a Format 3:** designation "cartel"/tổ chức buôn lậu ma túy có tổ chức đến từ nguồn tier 1-2 (cơ quan thực thi pháp luật, báo chí điều tra uy tín Mỹ/Colombia) — đủ điều kiện nêu tên tổ chức và các trùm chủ chốt đã tử vong/có hồ sơ tư pháp công khai rộng rãi (Escobar, anh em Ochoa...). Vai trò của "Los Pepes" cần trình bày cẩn trọng — độ tin cậy trung bình-cao nhưng còn tranh cãi về liên hệ với Cartel Cali/an ninh nhà nước, không khẳng định dứt khoát.
- Nhãn độ tin cậy: quy mô hoạt động — trung bình-cao (số liệu ước tính, cần gắn "ước tính"). Sự kiện cái chết Escobar (2/12/1993, Search Bloc, hỗ trợ DEA) — cao (Wikipedia EN, Mob Museum, nhiều nguồn báo chí uy tín, tier 2). Vai trò Los Pepes — trung bình-cao nhưng gây tranh cãi, cần nhãn cẩn trọng. Phản ứng chỉ trích "Narcos" — cao (nhiều outlet độc lập: France 24, Hollywood Reporter, Remezcla).

---

## 6. MS-13 (Mara Salvatrucha) — El Salvador / Hoa Kỳ

### Knowledge function

MS-13 là tổ chức duy nhất trong packet này không hình thành từ một khoảng trống quyền lực nhà nước nội tại, mà từ một làn sóng tị nạn chiến tranh tại một quốc gia thứ ba (Mỹ), sau đó bị "xuất khẩu" ngược về quê hương qua một cơ chế chính sách nhập cư cụ thể, có thể kiểm chứng — Đạo luật IIRIRA năm 1996. Bài học sư phạm cốt lõi: một tổ chức tội phạm xuyên quốc gia có thể hình thành từ sự giao thoa giữa chấn thương chiến tranh, thất bại hòa nhập cộng đồng nhập cư, và một quyết định chính sách công cụ thể — không phải một "bản chất" gán sẵn cho bất kỳ nhóm dân cư nào. Đây cũng là tổ chức duy nhất trong packet đòi hỏi một tầng phòng vệ biên tập thứ hai ngoài khung 5 phần và §8: **chống chính trị hóa/giật gân** — đối xứng ngược với "Cảnh báo lãng mạn hóa" của Cartel Medellín (mục 5): ở Escobar, rủi ro là khiến tổ chức trông hấp dẫn; ở MS-13, rủi ro là biến tập phim thành công cụ minh họa cho một luận điểm chính trị đảng phái Mỹ về nhập cư, theo bất kỳ chiều nào của cuộc tranh luận đó.

### Primary concepts

- Hình thành đầu thập niên 1980 tại khu Pico-Union, Los Angeles, bởi người tị nạn/nhập cư El Salvador chạy trốn nội chiến El Salvador (1979/1980-1992, chính phủ vs. FMLN) — ước tính khoảng 900.000 người bị di dời trong cuộc nội chiến này. Nhóm hình thành ban đầu mang tính tự vệ cộng đồng đồng hương trước sự thù địch của các băng nhóm gốc Mexico/Mỹ-Latin, Mỹ gốc Phi đã tồn tại từ trước tại khu vực. **Bối cảnh nguồn gốc này phải luôn xuất hiện trong kịch bản — không phải để biện minh, mà vì đây là bối cảnh lịch sử cần thiết thường bị lược bỏ trong tường thuật giật gân.** Độ tin cậy cao (khớp Britannica, Wikipedia, InSight Crime, CRS).
- Tên gọi: "Mara" (tiếng lóng El Salvador chỉ "băng nhóm") + "Salvatrucha" (ghép "Salva" + tiếng lóng "trucha" nghĩa "cảnh giác/tinh ranh"). Đầu thập niên 1990, liên minh với Mexican Mafia (Sureños) trong hệ thống nhà tù California — từ đó có số "13" gắn với tên gọi.
- **Cơ chế trục xuất 1996 (IIRIRA) → xuyên quốc gia hóa** — chuỗi nhân-quả chính sách công cụ thể, độ tin cậy cao (CRS tier 1, InSight Crime, VoxDev): Đạo luật *Illegal Immigration Reform and Immigrant Responsibility Act* (IIRIRA) 1996 mở rộng đáng kể diện trục xuất người nước ngoài có tiền án hình sự. Ước tính dao động giữa các nguồn — cần nêu cả hai, gắn nguồn, không chọn một số duy nhất: khoảng 20.000 người có tiền án bị trục xuất về Trung Mỹ giai đoạn 2000-2004 theo một ước tính; theo CRS, gần 130.000 công dân nước ngoài bị trục xuất về Trung Mỹ vì lý do hình sự giai đoạn 2001-2010. Nhiều người bị trục xuất về một El Salvador vừa ra khỏi nội chiến, thể chế còn yếu, không có mạng lưới tái hòa nhập, đã tái tạo cấu trúc "clique" học được ở Mỹ ngay tại quê nhà — khung đúng cho kịch bản: một trường hợp giáo dục về hệ quả chính sách nhập cư/hình sự không lường trước, không phải để đổ lỗi đơn giản.
- Cấu trúc: mạng lưới **"clica"/"clique"** phân tán theo địa bàn, mỗi clique tự chủ tài chính/nhân sự ở mức độ cao; trong tù (đặc biệt El Salvador) mỗi clique có "shot-caller"/**"Palabrero"**, hỗ trợ bởi các vị trí khác — nêu ở mức khái quát vai trò tổ chức, không đi sâu cơ chế vận hành nội bộ. Criminology mô tả MS-13 là "hierarchical in form but fragmented in practice" — độ tin cậy cao (CRS, InSight Crime, Orion Policy Institute, học thuật ResearchGate); có tranh luận học thuật nhỏ (2025) về mức độ liên kết mạng lưới thực sự — cần gắn nhãn "đang có tranh luận học thuật về mức độ," không khẳng định tuyệt đối một chiều.
- Ứng phó pháp lý Mỹ: nhiều vụ án liên bang dùng đạo luật RICO nhắm vào cấu trúc lãnh đạo MS-13 theo từng clique/khu vực cụ thể (ví dụ Las Vegas 2024 — ba bị cáo kết án liên quan chuỗi 9 vụ giết người 2017-2018; Massachusetts từ 2016; California) — khác Maxi Trial của Cosa Nostra (mục 1) ở chỗ đây là nhiều vụ án riêng lẻ qua nhiều năm/khu vực tài phán, không phải một đại án duy nhất "đánh sập" toàn mạng lưới. Độ tin cậy cao cho từng vụ án cụ thể (nguồn DOJ, tier 1).

### Narrative detail

**Phần trọng tâm bắt buộc (§8), và đồng thời là phần nhạy cảm chính trị nhất trong packet — jurisdiction phải luôn nêu rõ (El Salvador, dân luật; Mỹ, liên bang) theo `DOMAIN_GUIDE.md` §2. Cảnh báo bắt buộc: đây là chủ đề đang diễn ra (ongoing), không phải lịch sử đã khép lại — mọi con số cần gắn mốc thời gian rõ ràng.** Từ tháng 3/2022, Tổng thống El Salvador Nayib Bukele ban bố "chế độ ngoại lệ" (régimen de excepción/state of exception), tạm ngưng một số quyền hiến định, nới lỏng quy định bắt giữ — gia hạn liên tục hàng chục lần đến 2024-2025; xây dựng CECOT (Terrorism Confinement Center) — nhà tù được truyền thông mô tả có sức chứa tới 40.000 người. **Số liệu an ninh (theo chính phủ El Salvador, cần gắn ngày công bố):** tỷ lệ giết người giảm mạnh, từ 53,1/100.000 dân (2018) xuống mức báo cáo 1,9/100.000 dân (2024) — giảm hơn 98% giai đoạn 2015-2024 theo số liệu cảnh sát El Salvador; khoảng 84.000-118.000 người bị giam giữ vì cáo buộc liên quan tổ chức tội phạm tính đến đầu 2025 (số liệu dao động theo nguồn/thời điểm); Bukele nhận tỷ lệ ủng hộ rất cao trong khảo sát dư luận (một khảo sát CID Gallup ghi nhận khoảng 95%). **Song song, tài liệu hóa tốt bởi Human Rights Watch, Amnesty International, WOLA, Cristosal:** bắt giữ hàng loạt/tùy tiện, nhiều trường hợp bị giam giữ chỉ vì hình xăm, nơi cư trú thu nhập thấp, hoặc "biểu hiện lo lắng" khi bị hỏi — không phải bằng chứng phạm tội cụ thể; báo cáo tra tấn, thiếu ăn, điều kiện giam giữ vô nhân đạo, và số người chết trong trại giam dao động 261-517 người tùy thời điểm/nguồn thống kê, phần lớn — theo một tổ chức giám sát — chưa từng bị kết án bất kỳ tội danh nào. **Khung đúng, bắt buộc cho kịch bản: đây là một cuộc tranh luận thực sự, chưa có hồi kết đồng thuận, giữa hiệu quả an ninh định lượng được và cái giá nhân quyền tài liệu hóa được — không phải một câu chuyện "thành công tuyệt đối" hay "thất bại tuyệt đối" theo một chiều. Cả hai vế của tranh luận đều phải xuất hiện, đúng tinh thần `DOMAIN_GUIDE.md` §5 (trình bày đầy đủ các luồng ý kiến, không chỉ chọn một chiều).**

### Script-ready material

- Cấu trúc "chuỗi nhân-quả chính sách công" (nội chiến → tị nạn → nhóm tự vệ cộng đồng → IIRIRA 1996 → xuyên quốc gia hóa) — mạch kể giáo dục mạnh, trung lập chính trị, không cần dựng thêm kịch tính.
- Đối lập "hierarchical in form but fragmented in practice" — điểm sửa hiểu lầm phổ biến (MS-13 không phải một "đế chế" có chỉ huy trung ương thống nhất, mà một mạng lưới clique tự chủ).
- mano dura/chế độ ngoại lệ như một hồi kết **mở**, không đóng — vừa có số liệu an ninh ấn tượng, vừa có cái giá nhân quyền tài liệu hóa tốt — chất liệu tự nhiên cho kết cấu "tranh luận hai chiều," thay vì một kết luận đơn phương.

### Cảnh báo chính trị hóa/giật gân

**Đây là tiểu mục bắt buộc riêng cho tổ chức này** khi Knowledge Packet hóa nội dung — song song, không thay thế, "Cảnh báo lãng mạn hóa" của Cartel Medellín ở mục 5, nhưng đối xứng ngược: rủi ro ở đây là **chính trị hóa/giật gân**, không phải lãng mạn hóa. MS-13 là tổ chức tội phạm có tổ chức bị chính trị hóa nhiều nhất trong diễn ngôn công chúng Mỹ giai đoạn 2016-2026, theo cả hai hướng: (a) phóng đại quy mô/mối đe dọa để phục vụ luận điểm chính sách nhập cư, và (b) một số tiếng nói khác giảm thiểu quy mô thiệt hại thực tế để phản bác luận điểm (a). Kênh này không đứng về phía nào của cuộc tranh luận chính sách nhập cư Mỹ — chỉ trình bày sự kiện đã kiểm chứng.

- **Fact-check đã xác nhận (PolitiFact, AP Fact Check — tier 2 fact-checking uy tín):** nhiều tuyên bố chính trị giai đoạn 2017-2018 về MS-13 bị các tổ chức fact-check đánh giá là gây hiểu lầm hoặc sai lệch cụ thể — tuyên bố băng nhóm đang "gia tăng mạnh" không khớp số liệu FBI (quy mô tại Mỹ được ước tính ổn định quanh mức ~10.000 thành viên liên tục từ khoảng 2005 đến nay); tuyên bố phần lớn thành viên là người nhập cư bất hợp pháp không khớp (nhiều nguồn, gồm nghiên cứu được PolitiFact trích dẫn, ghi nhận phần lớn thành viên MS-13 tại Mỹ hiện nay là công dân Mỹ sinh ra tại Mỹ, không phải người mới nhập cư); tuyên bố cụ thể về số lượng bị trục xuất "hàng nghìn người" được PolitiFact xếp hạng "Mostly False" vì không có số liệu xác minh được cho riêng thành viên MS-13.
- **Về quy mô thực tế (đối chiếu nhiều nguồn, luôn gắn "ước tính," không chọn một con số tuyệt đối):** ước tính tại Mỹ dao động 8.000-10.000 thành viên (dưới 1% tổng số ~1,4 triệu thành viên băng nhóm tại Mỹ theo một ước tính 2018); ước tính toàn cầu dao động rộng hơn nhiều — từ khoảng 30.000-50.000 đến 50.000-70.000 tùy nguồn/phương pháp đếm.
- **Diễn biến chính trị hóa tiếp theo (2025, đang diễn ra, chưa khép lại):** ngày 20/2/2025, Bộ Ngoại giao Mỹ chính thức định danh MS-13 là "Tổ chức Khủng bố Nước ngoài" (Foreign Terrorist Organization) và "Cá nhân/Tổ chức Khủng bố Toàn cầu được Chỉ định Đặc biệt" (Specially Designated Global Terrorist) — cùng đợt với Tren de Aragua và một số cartel Mexico. Nhiều nhà nghiên cứu tội phạm học và chính sách (được CNN, AULA Blog/American University, Council on Foreign Relations trích dẫn — đây là quan điểm chuyên gia được báo chí/tổ chức nghiên cứu ghi nhận, không phải kết luận của kênh) cho rằng gọi MS-13 là "tổ chức khủng bố" là mô tả không chính xác về mặt học thuật — MS-13 theo các học giả này là "tổ chức tội phạm xuyên quốc gia" (transnational criminal organization), hoạt động vì lợi ích kinh tế/lãnh thổ, không phải mục tiêu chính trị/ý thức hệ như định nghĩa khủng bố học thuật thông thường yêu cầu. Một chuyên gia được CNN trích dẫn còn lưu ý nghịch lý thời điểm: MS-13 tại chính El Salvador — nơi từng là thành trì mạnh nhất — đã bị dẹp bỏ phần lớn bởi chính chiến dịch mano dura của Bukele, khiến việc định danh khủng bố ở thời điểm 2025 bị một số nhà quan sát cho là chọn thời điểm kỳ lạ. **Đây là tranh luận học thuật/chính sách đang mở, chưa có kết luận đồng thuận — phải trình bày như tranh luận đang diễn ra, nhiều phía, không chọn phe.**
- **Hướng dẫn phản khung cụ thể cho biên kịch tương lai (bắt buộc, không phải tùy chọn):**
  1. Luôn phân biệt rõ ba tầng thông tin trong kịch bản: (a) sự kiện/số liệu đã kiểm chứng chéo (quy mô ước tính, cấu trúc clique, các vụ RICO, chính sách mano dura và số liệu an ninh/nhân quyền của nó); (b) tuyên bố chính trị đã bị fact-check xác định là sai/gây hiểu lầm (không lặp lại như sự thật); (c) tranh luận học thuật/chính sách đang mở (ví dụ định danh khủng bố có phù hợp không) — trình bày như tranh luận đang diễn ra, có nhiều phía, không chọn phe.
  2. **Không** dùng khung "làn sóng nhập cư mang theo tội phạm" như một kết luận của kịch bản — đây là khung diễn ngôn chính trị đã bị nhiều fact-checker tier 2 xác định là không khớp dữ liệu nhân khẩu học thực tế của tổ chức (đa số thành viên hiện là công dân Mỹ sinh tại Mỹ).
  3. **Không** dùng khung ngược lại là giảm thiểu/phủ nhận thiệt hại thực tế mà MS-13 gây ra (các vụ giết người, tống tiền, buôn ma túy đã có bản án — đây là sự thật đã kiểm chứng, không phải hư cấu chính trị) — cân bằng đúng mức, không đi từ thái cực giật gân sang thái cực xóa nhòa hậu quả thật.
  4. Trọng tâm tường thuật nên đặt ở: (a) bối cảnh xã hội-lịch sử hình thành (nội chiến, tị nạn, hòa nhập thất bại), (b) cơ chế chính sách trục xuất dẫn tới xuyên quốc gia hóa (bài học chính sách công có giá trị giáo dục cao, trung lập chính trị), (c) hậu quả pháp lý/xã hội đã kiểm chứng (RICO, mano dura và các mặt được-mất của nó) — tránh biến tập phim thành một luận điểm ủng hộ/phản đối bất kỳ đảng phái hay chính sách nhập cư cụ thể nào của Mỹ.
  5. Đúng theo `DOMAIN_GUIDE.md` §4a Format 3 và §4: designation "tổ chức tội phạm" của MS-13 đủ điều kiện nêu tên tổ chức (tier 1: bản án RICO, cơ quan hành pháp Mỹ, DOJ) — nhưng không cấp phép quy kết bất kỳ cá nhân cụ thể nào (kể cả nghi phạm bị bắt tại El Salvador dưới chế độ ngoại lệ, nhiều người trong đó *chưa từng bị kết án* theo chính báo cáo nhân quyền) là có tội nếu chưa có bản án cuối cùng. Đây là điểm giao thoa nhạy cảm giữa §4 và §8 cần cảnh giác đặc biệt khi nói về các đợt bắt giữ hàng loạt ở El Salvador.

### Production cautions

- **Thực thi §8:** không mô tả chi tiết vận hành clique/tuyển mộ/hệ thống liên lạc nội bộ theo cách có thể học theo — chỉ mô tả cấu trúc ở mức khái quát tổ chức học lịch sử-xã hội. **Không mô tả hình dạng/nội dung hình xăm cụ thể**, dù nguồn phổ thông/truyền thông thường nhắc tới hình xăm như đặc điểm nhận dạng phổ biến của MS-13 — packet này chủ động không mô tả, giữ nguyên giới hạn đã đặt ra trong research draft gốc.
- **Thực thi §4a Format 3 + §4:** MS-13 đủ điều kiện nêu tên tổ chức (designation tier 1 từ bản án RICO/DOJ); nhưng cá nhân bị bắt/bị tình nghi tại El Salvador dưới chế độ ngoại lệ — đặc biệt phần lớn chưa qua xét xử theo chính báo cáo nhân quyền — phải giữ nguyên ngôn ngữ hedged (bị tình nghi/bị can), không bao giờ gọi là "tội phạm" nếu chưa có bản án cuối cùng.
- **Bắt buộc mang theo tiểu mục "Cảnh báo chính trị hóa/giật gân" ở trên nguyên vẹn, không rút gọn hay làm mềm đi**, mỗi khi packet này được dùng làm nền cho kịch bản — không phải phần có thể lược bỏ để "gọn nội dung," tương tự cách "Cảnh báo lãng mạn hóa" của Escobar không thể lược bỏ (mục 5).
- Nhãn độ tin cậy: nguồn gốc LA/nội chiến El Salvador — cao (khớp nhiều nguồn tier 2-3 độc lập); cơ chế trục xuất 1996 IIRIRA → xuyên quốc gia hóa — cao (CRS tier 1, InSight Crime, VoxDev); số liệu trục xuất cụ thể (20.000 vs 130.000) — trung bình-cao (hai ước tính khác nguồn/phạm vi thời gian, cần nêu rõ cả hai); cấu trúc clique phân tán — cao (có tranh luận nhỏ về mức độ liên kết mạng lưới thực sự); các vụ RICO cụ thể — cao (nguồn DOJ trực tiếp, tier 1); số liệu mano dura/chế độ ngoại lệ (an ninh) — cao nhưng biến động theo thời điểm (số liệu chính phủ El Salvador); số liệu vi phạm nhân quyền mano dura — cao nhưng dao động giữa các nguồn (HRW/Amnesty/WOLA/Cristosal); fact-check tuyên bố chính trị 2018 — cao (PolitiFact/AP, tier 2); định danh khủng bố 2025 và phản biện học thuật — cao cho sự kiện đã xảy ra (Federal Register, tier 1), tranh luận học thuật vẫn mở; quy mô thành viên toàn cầu — trung bình (ước tính dao động rộng 30.000-70.000 tùy nguồn, luôn gắn "ước tính").

---

## 7. Camorra (Naples, Ý)

### Knowledge function

Camorra là cơ hội compare/contrast mạnh nhất trong packet này, khai thác trực tiếp việc Cosa Nostra đã được kể ở mục 1: cùng được xếp vào nhóm "mafia kiểu Ý," nhưng hai tổ chức hình thành ở hai vùng khác nhau (Naples/Campania vs. Sicilia), trong bối cảnh lịch sử-xã hội khác nhau, và quan trọng nhất — với hai kiến trúc tổ chức đối lập nhau: kim tự tháp tập trung (Cosa Nostra, "Ủy ban"/Commissione) so với mạng lưới ngang phân tán (Camorra, hơn 100 clan độc lập). Đây là điểm giáo dục xuyên suốt của toàn mục, đúng tinh thần "phân tích-lịch sử-xã hội" mà §8 yêu cầu cho cả pillar — không phải một "phần hai" của Cosa Nostra, mà một tổ chức riêng biệt được kể tốt nhất *thông qua* sự đối chiếu đó.

### Primary concepts

- Gốc rễ được ghi nhận từ cuối thế kỷ 18, khiến Camorra **cổ xưa hơn Cosa Nostra** (Cosa Nostra hình thành thế kỷ 19, đã mô tả ở mục 1) — theo đa số nhà sử học, hình thành từ các băng nhóm trong hệ thống nhà tù Naples, ngay trước thời kỳ thống nhất nước Ý (1861). Có giả thuyết bên lề (**độ tin cậy thấp**, mang tính suy đoán lịch sử) về liên hệ xa với Tây Ban Nha thế kỷ 15 — chỉ nêu như một giả thuyết nếu cần, không phải khẳng định chính. Camorra và Cosa Nostra là **hai tổ chức riêng biệt, hình thành ở hai vùng khác nhau của Ý, không phải một tổ chức chia nhánh từ tổ chức kia** — dù cả hai cùng được xếp vào nhóm "mafia kiểu Ý" với 'Ndrangheta (Calabria) trong phân loại học thuật/báo chí hiện đại. Độ tin cậy cao cho niên đại tương đối và bối cảnh nhà tù Naples (Britannica, ACAMS); thấp cho giả thuyết gốc Tây Ban Nha.
- **Cấu trúc — điểm compare/contrast cốt lõi của toàn mục:** Cosa Nostra (mục 1) là kim tự tháp — mỗi "gia đình" (cosca/famiglia) theo địa bàn có phân cấp nội bộ capo/sottocapo/consigliere/soldati/associates, và "Ủy ban" (Commissione) điều phối liên gia đình, có vai trò giải quyết tranh chấp giữa các gia đình (đúng như đã mô tả ở mục 1). Camorra **không có một cơ quan điều phối trung ương duy nhất tương đương** — là mạng lưới hàng trăm "clan" độc lập (nhiều nguồn ước tính hơn 100 nhóm hoạt động ở các thời điểm khác nhau), mỗi clan tự chủ về tài chính, nhân sự, địa bàn, vận hành song song, không có cơ chế phân xử tranh chấp cấp trên. Ví von thường dùng: Cosa Nostra như "kim tự tháp," Camorra như "mạng lưới ngang/hỗn loạn" — phản ánh đúng địa lý đô thị chằng chịt của Naples. **Hệ quả giáo dục trực tiếp:** vì thiếu cơ chế phân xử tập trung, xung đột giữa các clan Camorra về địa bàn/thị phần thường xuyên leo thang thành bạo lực trực diện giữa các clan (không nêu chi tiết kỹ thuật bạo lực) — khác Cosa Nostra, nơi Ủy ban về lý thuyết có vai trò kiềm chế xung đột nội bộ giữa các gia đình. Độ tin cậy cao — một trong những điểm ít gây tranh cãi nhất trong toàn bộ tư liệu về hai tổ chức này.
- Hoạt động kinh tế được tài liệu hóa (nêu ở mức khái quát lịch sử, không mô tả cơ chế vận hành cụ thể): buôn lậu ma túy, hàng giả/hàng nhái, tống tiền ("bảo kê"), cho vay nặng lãi, đổ trộm chất thải độc hại, buôn lậu thuốc lá, cờ bạc phi pháp, tham nhũng chính trị — đặc biệt **rửa tiền qua đầu tư vào ngành kinh doanh hợp pháp** (nhà hàng, xây dựng, bất động sản, vận tải), nhiều nguồn xác nhận đây là đặc điểm nổi bật của Camorra so với các tổ chức tội phạm khác. Độ tin cậy cao (ACAMS, understandingitaly.com, nhiều báo chí độc lập).
- Mức độ "ăn sâu" xã hội: một số clan kiểm soát gần như toàn bộ đời sống kinh tế của một khu phố cụ thể tại Naples qua tống tiền doanh nghiệp nhỏ và cho vay nặng lãi — một số nghiên cứu mô tả điều này như việc mạng lưới clan "hòa trộn tính bất hợp pháp với vẻ ngoài của nghĩa vụ công dân," tức lấp một phần khoảng trống quản lý nhà nước ở một số khu vực. **Cảnh báo biên tập quan trọng:** đặc điểm này **không được trình bày theo hướng lãng mạn hóa** (kiểu "Camorra giúp đỡ người nghèo") — đây là hiện tượng tội phạm học có tài liệu, cùng khung phân tích "tổ chức tội phạm lấp khoảng trống nhà nước" đã dùng cho cả 5 tổ chức gốc của packet này, không phải một đặc điểm đáng ngưỡng mộ. Độ tin cậy trung bình-cao (chủ yếu báo chí điều tra dài kỳ và nghiên cứu xã hội học, tier 2-3, mang tính diễn giải hơn số liệu định lượng cứng).

### Narrative detail

**Phần trọng tâm bắt buộc (§8) — đối xứng trực tiếp với Maxi Trial của Cosa Nostra ở mục 1.** Từ 1/7/1998 đến phán quyết cuối cùng 19/6/2008, **"Phiên tòa Spartacus" (Processo Spartacus)** — một loạt phiên xử kéo dài hơn 10 năm — nhắm trực diện vào clan Casalesi thuộc Camorra. Kết quả: 36 thành viên clan bị truy tố về một loạt tội giết người và tội danh khác; toàn bộ bị cáo bị tuyên có tội; **16 người lãnh án chung thân** (bao gồm các thủ lĩnh clan cấp cao), 14 người khác nhận án từ 2 đến 30 năm tù. Phiên tòa phơi bày quy mô kinh tế của clan Casalesi — độc chiếm thị trường xi măng/xây dựng, đổ trộm chất thải, mở rộng hoạt động (buôn ma túy, vũ khí, chất thải độc hại, mại dâm) ra ngoài biên giới Ý tới Đông Âu — nêu ở mức khái quát lịch sử-tư pháp, không mô tả cơ chế cụ thể. Đây là ví dụ tư pháp tốt, đối xứng với Maxi Trial của Cosa Nostra: cùng khung "nhà nước pháp quyền, dù chậm, cuối cùng dùng chính hệ thống tư pháp để lột trần và giam giữ một mạng lưới tội phạm quy mô lớn."

Song song, và **là điểm neo cảm xúc bắt buộc thứ hai của mục này** — vai trò tương tự Falcone/Borsellino ở mục 1, nhưng với một khác biệt quan trọng cần nêu rõ (nhân vật này còn sống, cái giá vẫn đang tiếp diễn, không phải một cái kết đã khép lại): nhà báo/nhà văn **Roberto Saviano** (sinh 1979, quê Casal di Principe gần Naples — chính là địa bàn hoạt động của clan Casalesi) xuất bản sách **"Gomorra"** năm 2006 (Mondadori) — kết hợp báo chí điều tra và văn chương, dựa trên hồ sơ tòa án thực tế và trải nghiệm cá nhân của tác giả (5 năm nghiên cứu). Sách trở thành best-seller quốc tế; bản chuyển thể điện ảnh cùng tên (đạo diễn Matteo Garrone) đoạt Grand Prix tại Cannes 2008, là đại diện chính thức của Ý tại Oscar năm đó, sau đó có thêm phiên bản phim truyền hình nhiều mùa. **Hậu quả thực tế đối với tác giả — phần bắt buộc phải kể cùng thành công của sách/phim, không tách rời:** sau khi sách gây tiếng vang, Saviano nhận được đe dọa tính mạng nghiêm trọng, được xác nhận qua nguồn tin cảnh sát/điều tra — có thông tin cho rằng thủ lĩnh clan Casalesi từng chỉ đạo việc này. Từ năm 2006, Saviano phải sống dưới sự bảo vệ vũ trang liên tục — mốc thời gian nêu linh hoạt ("từ 2006 đến nhiều năm sau"/"cho tới nay theo nhiều nguồn"), không chốt một con số năm duy nhất vì nguồn không đồng nhất; ông từng phải rời Ý một thời gian để tìm nơi trú ẩn an toàn hơn. Khung đúng cho kịch bản: một nhà báo trả giá cá nhân rất lớn — có thật, không phải hư cấu, một phần vẫn đang tiếp diễn — để phơi bày sự thật về một tổ chức tội phạm, phù hợp làm điểm neo cảm xúc/hồi kết cho tập phim.

**Ghi chú trung thực bắt buộc về hiện trạng:** khác 4/5 tổ chức gốc trong packet này (vốn đã được xử lý dứt điểm hoặc suy giảm rõ rệt), Camorra **không phải một tổ chức đã kết thúc** — nhiều nguồn học thuật/báo chí gần đây (The Conversation, EU Today, University of Bath) mô tả Camorra vẫn đang hoạt động tích cực, kể cả mở rộng hiện diện ra một số nước châu Âu. Khung "sụp đổ" ở mục này phải áp dụng cho **từng clan cụ thể đã bị xét xử** (Casalesi qua Spartacus), không được khái quát hóa thành "Camorra nói chung đã bị dẹp bỏ" — đây là điểm cần trình bày trung thực, không thỏa hiệp với khuôn mẫu "rise-and-fall" gọn gàng chỉ vì nó dễ kể hơn.

### Script-ready material

- Compare/contrast mở đầu tự nhiên, tận dụng trực tiếp mục 1 đã có sẵn trong packet: "Cosa Nostra có một Ủy ban phân xử tranh chấp; Camorra thì không" — hook giáo dục mạnh, không cần dựng thêm kịch tính.
- Saviano/Gomorra — nhân vật thật, hậu quả thật, điểm neo cảm xúc/hồi kết tự nhiên tương tự Falcone/Borsellino ở mục 1, nhưng khác biệt vì Saviano còn sống và vẫn đang trả giá ở hiện tại — cần trình bày với sự tôn trọng tương xứng, không kịch tính hóa quá mức một tình huống đang diễn ra ngoài đời thật.
- Số liệu Spartacus (36 bị cáo, 16 án chung thân, 14 án 2-30 năm, hơn 10 năm tố tụng) — dữ liệu ấn tượng, an toàn dùng nguyên văn vì nguồn tier 1-2 (DIA, Wikipedia, France 24/AFP).
- Ghi chú "vẫn đang hoạt động tích cực" như một kết thúc mở trung thực — tránh cảm giác giả tạo "đã xong," đồng thời tự thân đã đủ hấp dẫn mà không cần thêm kịch tính.

### Production cautions

- **Thực thi §8:** không mô tả chi tiết vận hành cụ thể của tống tiền/cho vay nặng lãi/rửa tiền/đổ trộm chất thải/buôn lậu — chỉ nêu ở mức khái quát lịch sử như đã làm ở Primary concepts. Đặc điểm "ăn sâu xã hội" **không được** trình bày theo hướng lãng mạn hóa kiểu "Camorra giúp đỡ cộng đồng" — luôn gắn kèm khung phân tích "lấp khoảng trống nhà nước" trong cùng đoạn, không phải một đặc điểm đáng ngưỡng mộ, đúng tinh thần đã áp dụng cho cả 5 tổ chức gốc trong packet.
- **Thực thi §4a Format 3 + §4:** designation "tổ chức tội phạm mafia kiểu Ý" cho Camorra/clan Casalesi đến từ phán quyết tư pháp Ý (Spartacus, tier 1) — đủ điều kiện nêu tên tổ chức và 36 bị cáo đã bị kết án cuối cùng trong Spartacus (Format 1). Nhưng nêu tên tổ chức không cấp phép gọi bất kỳ thành viên/associate nào ngoài phạm vi các bị cáo đã kết án cuối cùng là "có tội" — cá nhân khác được nhắc tới (kể cả nghi phạm mới) vẫn cần ngôn ngữ hedged theo §4 nếu chưa có bản án cuối cùng.
- Trọng tâm tường thuật luôn giữ song song Spartacus + Saviano — hai nhịp hậu quả/tiếp diễn không thể lược bỏ để "dành thời lượng cho phần cấu trúc/mạng lưới kinh tế" của tổ chức.
- Nhãn độ tin cậy: niên đại cổ xưa hơn Cosa Nostra/gốc nhà tù Naples — cao (Britannica, ACAMS, nhiều nguồn cross-check); giả thuyết gốc Tây Ban Nha thế kỷ 15 — thấp, chỉ nêu bên lề, cần gắn nhãn; cấu trúc phân tán/clan độc lập vs. Ủy ban Cosa Nostra — cao, điểm ít tranh cãi nhất trong tư liệu về hai tổ chức; hoạt động kinh tế/rửa tiền qua kinh doanh hợp pháp — cao (ACAMS, understandingitaly.com, nhiều báo chí); mức độ "ăn sâu" xã hội Naples — trung bình-cao (diễn giải xã hội học, tier 2-3, cần cẩn trọng tránh lãng mạn hóa); Saviano/Gomorra — sách, phim, đe dọa, bảo vệ vũ trang — cao (khớp nhiều nguồn tier 2-3 độc lập: Wikipedia, Literary Review, BBC, Collider, PBS Frontline; mốc thời gian bảo vệ cụ thể hơi dao động giữa nguồn); Phiên tòa Spartacus — số liệu, kết quả — cao (khớp Wikipedia, France 24, Taipei Times/AFP, DIA tier 1-2); tình trạng Camorra hiện tại (vẫn hoạt động) — trung bình-cao (báo chí gần đây — The Conversation, EU Today — cần gắn mốc thời gian, tránh khái quát hóa "đã kết thúc").

---

# Ghi chú tổng hợp cho biên tập viên

1. **Điểm chung bắt buộc của cả 7 mục:** mỗi tổ chức có một câu chuyện sụp đổ/hậu quả được ghi chép tốt, có thể kể hấp dẫn mà không cần chi tiết vận hành — trọng tâm luôn là "nhà nước/pháp luật/nội bộ tổ chức đã đánh sập nó như thế nào," không phải "tổ chức đã hoạt động trơn tru ra sao." (Ngoại lệ trung thực: Camorra, mục 7 — quá trình đó mới thành công ở cấp từng clan cụ thể, không phải toàn mạng lưới; xem ghi chú số 7 dưới đây.)
2. **Escobar/Cartel Medellín là trường hợp rủi ro cao nhất** về lãng mạn hóa — có tiểu mục "Cảnh báo lãng mạn hóa" riêng, không chỉ dựa vào hedge câu chữ.
3. **Năm Cam là trường hợp duy nhất xảy ra tại Việt Nam** và có bản án đã có hiệu lực pháp luật (Format 1) — nhưng mục này của packet **chủ động không lặp lại** narrative vụ án đã/sẽ có ở KP_CL_002, chỉ tập trung cấu trúc tổ chức + mạng lưới cán bộ tha hóa; **cần rà soát cross-reference khi KP_CL_002 được viết**.
4. **Hội Tam Hoàng** cần gắn nhãn "truyền thuyết dân gian" nhất quán cho câu chuyện "phản Thanh phục Minh" — không bao giờ trình bày như sử liệu xác thực.
5. **Không có nội dung nào trong packet này** vi phạm ranh giới cấm của `DOMAIN_GUIDE.md` §8: không có chi tiết vận hành đủ để làm theo (chiêu mộ/rửa tiền/buôn lậu/né tránh pháp luật/liên lạc mật mã); không có mô tả/tái hiện phù hiệu băng đảng hoặc hình xăm theo cách nhận dạng được — bao gồm cả MS-13 (mục 6), dù nguồn phổ thông thường nhắc tới hình xăm như đặc điểm nhận dạng. Toàn bộ nội dung dừng ở lớp lịch sử-xã hội-cấu trúc phân tích-hậu quả pháp lý.
6. **Jurisdiction phải luôn được nêu rõ** khi dựng kịch bản (`DOMAIN_GUIDE.md` §2) — xem Historical Background.
7. **MS-13 (mục 6) là trường hợp rủi ro cao nhất về chính trị hóa/giật gân** — một dạng rủi ro mới, khác bản chất với lãng mạn hóa (Escobar) hay truyền thuyết-nhầm-thành-sử-liệu (Hội Tam Hoàng). Tiểu mục "Cảnh báo chính trị hóa/giật gân" của mục 6 **phải được mang theo nguyên vẹn, không rút gọn**, mỗi khi packet được dùng làm nền kịch bản — cùng mức bắt buộc như "Cảnh báo lãng mạn hóa" của Escobar.
8. **Camorra (mục 7) là cơ hội compare/contrast chính với Cosa Nostra (mục 1)** — cấu trúc mạng lưới ngang (hơn 100 clan độc lập) đối lập với cấu trúc kim tự tháp/Ủy ban của Cosa Nostra; đồng thời là tổ chức duy nhất trong packet mà khung "sụp đổ" chỉ áp dụng đúng ở cấp từng clan (Casalesi qua Phiên tòa Spartacus), không phải toàn bộ tổ chức — Camorra vẫn được nhiều nguồn mô tả là đang hoạt động tích cực tính đến thời điểm nghiên cứu (2026).

---

# Retrieval Warnings

Khi packet này được truy xuất, hệ thống nên đính kèm các cảnh báo:

- Mọi mục phải giữ tỉ lệ tường thuật "hậu quả/sụp đổ" tương đương hoặc lớn hơn "trỗi dậy" — đây là ranh giới §8, không phải lựa chọn phong cách.
- Không mô tả chi tiết vận hành (chiêu mộ/rửa tiền/buôn lậu/né tránh pháp luật/mật mã) dù nguồn gốc có đề cập — chỉ ở mức khái quát lịch sử.
- Không mô tả/tái hiện phù hiệu, biểu tượng băng đảng theo cách có thể nhận dạng/sử dụng.
- Nêu tên tổ chức không bao giờ cấp phép nêu tên cá nhân chưa bị kết án cuối cùng là có tội (§4a Format 3 + §4).
- Truyền thuyết "phản Thanh phục Minh" (Hội Tam Hoàng) là folklore/disputed, không phải sử liệu.
- Escobar/Cartel Medellín bắt buộc có counter-framing chống lãng mạn hóa, trung tâm hóa góc nhìn nạn nhân Colombia.
- Mục Năm Cam chỉ nói cấu trúc tổ chức + cán bộ tha hóa; narrative vụ án/phiên tòa thuộc `KP_CL_002_An_Da_Xu.md` — packet đó **đã tồn tại** (kể từ 2026-07-23) và cross-reference số liệu đã được xác nhận khớp (155 bị can/bị cáo, 24 tội danh, 21 cán bộ nhà nước).
- Mục MS-13 (mục 6) bắt buộc kèm theo tiểu mục "Cảnh báo chính trị hóa/giật gân" nguyên vẹn — không chọn phe trong tranh luận chính sách nhập cư Mỹ; định danh FTO 2025 và phản biện học thuật là tranh luận đang mở, chưa có kết luận đồng thuận.
- Mục Camorra (mục 7) bắt buộc giữ song song hai nhịp hậu quả: Phiên tòa Spartacus (clan Casalesi) và cái giá cá nhân thực tế của Roberto Saviano; không khái quát hóa "Camorra đã bị dẹp bỏ" — tổ chức vẫn được nhiều nguồn mô tả là đang hoạt động.
- Domain QA Policy chính thức của domain CL cần áp dụng đầy đủ trước khi packet chuyển `active` — bao gồm cả hai mục mở rộng (6-7), hiện **chưa qua QA chính thức**.

---

# Packet Completion Notes

Packet này ban đầu tổng hợp toàn bộ `RESEARCH_DRAFT_TO_CHUC_TOI_PHAM.md` (research date 2026-07-23, 5 tổ chức gốc) thành một Knowledge Packet có cấu trúc thống nhất, giữ nguyên mọi cảnh báo/nhãn độ tin cậy/cờ dị bản đã ghi trong nguồn gốc. **Mở rộng 2026-07-24 (version 0.2):** bổ sung mục 6 (MS-13) và mục 7 (Camorra) từ `RESEARCH_DRAFT_TO_CHUC_TOI_PHAM_BATCH2.md`, cùng chuẩn cấu trúc 5 phần và cùng mức độ giữ nguyên nhãn độ tin cậy/cờ dị bản — không có tuyên bố nào trong cả hai research draft bị lược bỏ hoặc làm phẳng. Đây là draft phù hợp làm nền tri thức nội bộ cho các bước tiếp theo (Creative Knowledge, Series Bible, Character Bible, kịch bản Pillar 5), **không phải nội dung sẵn sàng công chiếu**.

Packet cần trước khi nâng trạng thái `active`: (1) Domain QA Policy chính thức của domain CL áp dụng và ký duyệt, đặc biệt hạng mục §8 Non-Glorification/No-Operational-Detail — **độc lập QA đã thực hiện 2026-07-23 cho 5 mục gốc, xem `_QA_REPORT_KP_CL_005.md`; mục 6-7 (bổ sung 2026-07-24) chưa qua vòng QA này, cần chạy lại/mở rộng QA report trước khi packet toàn bộ chuyển `active`**; (2) ~~`KP_CL_002_An_Da_Xu.md` được soạn và cross-reference ở mục Năm Cam được xác nhận/khớp~~ — **hoàn tất 2026-07-23:** đã soạn xong và số liệu đã đối chiếu khớp (155 bị can/bị cáo, 24 tội danh, 21 cán bộ nhà nước); (3) rà soát bổ sung các "Khoảng trống nguồn" đã liệt kê, đặc biệt vai trò Los Pepes và số liệu ước tính quy mô Cartel Medellín, cũng như các khoảng trống mới của batch 2 (số liệu trục xuất MS-13, số người chết mano dura, mốc thời gian bảo vệ Saviano) — vẫn còn mở, cần human judgment (xem QA report).

# Final Packet Use Boundary

Các agent tương lai phải coi packet này là một tài sản tri thức được quản trị, không phải nội dung sẵn sàng khán giả. Packet có thể dùng để truy xuất khái niệm, cảnh báo, ràng buộc sản xuất, và phụ thuộc QA. Packet **không được** sao chép trực tiếp vào kịch bản công khai mà không qua Content Engine transformation và QA review đầy đủ.

Mọi sản phẩm phái sinh phải giữ được các ranh giới sau:

1. Trọng tâm tường thuật luôn là hậu quả/sụp đổ — không có "rise" thiếu "fall" tương xứng (§8); với Camorra (mục 7), khung này áp dụng ở cấp từng clan cụ thể, không khái quát hóa thành toàn tổ chức đã kết thúc.
2. Không chi tiết vận hành đủ để làm theo, không tái hiện phù hiệu/biểu tượng/hình xăm nhận dạng được (§8).
3. Nêu tên tổ chức không cấp phép nêu tên cá nhân chưa bị kết án cuối cùng là có tội (§4a Format 3, §4).
4. Escobar/Cartel Medellín luôn đi kèm counter-framing chống lãng mạn hóa, trung tâm hóa nạn nhân.
5. Mục Năm Cam không lặp lại narrative vụ án thuộc phạm vi KP_CL_002.
6. MS-13 (mục 6) luôn đi kèm nguyên vẹn tiểu mục "Cảnh báo chính trị hóa/giật gân" — không chọn phe trong tranh luận chính sách nhập cư Mỹ, theo bất kỳ chiều nào.
7. Camorra (mục 7) luôn giữ song song hai nhịp hậu quả bắt buộc — Phiên tòa Spartacus (clan Casalesi) và cái giá cá nhân thực tế của Roberto Saviano — không được lược bỏ một trong hai để rút gọn thời lượng; không khái quát hóa "Camorra đã bị dẹp bỏ" vượt quá phạm vi từng clan cụ thể đã bị xét xử.

Nếu một sản phẩm đầu ra tương lai không thể giữ được bảy ranh giới này, nó phải được sửa lại, nâng cấp xét duyệt, hoặc từ chối trước khi công chiếu.

---

# Frontmatter Header (Asset Registry Reference)

| Field | Value |
|---|---|
| Asset ID | KP_CL_005 |
| Domain | CL (Hình Sự — Criminal Law) |
| Dùng cho | Pillar 5 (Tổ Chức Tội Phạm) season episodes |
| Phụ thuộc | `DOMAIN_GUIDE.md` + `RESEARCH_DRAFT_TO_CHUC_TOI_PHAM.md` + `RESEARCH_DRAFT_TO_CHUC_TOI_PHAM_BATCH2.md` + cross-reference `KP_CL_002_An_Da_Xu.md` (đã tồn tại kể từ 2026-07-23, số liệu Năm Cam đã đối chiếu khớp) |
| Trạng thái | draft creative-knowledge asset — chưa qua QA chính thức (mục 6-7 mới bổ sung 2026-07-24, chưa qua vòng QA nào) |
| Version | 0.2 (2026-07-24 — mở rộng thêm mục 6 MS-13, mục 7 Camorra; roster từ 5 lên 7 tổ chức) |
