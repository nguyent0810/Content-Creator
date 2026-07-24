---
schema_version: 1.0
packet_id: KP_CL_002
domain_id: CL
canonical_owner: DOMAINS/CRIMINAL_LAW
canonical_topic: Án Đã Xử / Phá Án — Sáu vụ án nền tảng cho Pillar 2 (Năm Cam, Lê Văn Luyện, Cát Tường, O.J. Simpson, Vụ thảm sát Bình Phước, Casey Anthony)
vietnamese_display_name: Án Đã Xử (Phá Án)
english_working_title: Solved True Crime — Foundational Case Studies
object_type: Knowledge Packet
status: draft-pending-human-review
version: 0.2
language: Tiếng Việt (chính), chú thích tiếng Anh cho thuật ngữ luật Hoa Kỳ ở các vụ O.J. Simpson và Casey Anthony
risk_level: critical
risk_reasons:
  - Presumption-of-innocence / net-impression test (`DOMAIN_GUIDE.md` §4) — đặc biệt nghiêm trọng ở vụ O.J. Simpson (trắng án hình sự vs. trách nhiệm dân sự) và vụ Casey Anthony (trắng án hình sự trước niềm tin công chúng gần như đồng thuận ngược lại)
  - Victim dignity & minor-victim non-naming (`DOMAIN_GUIDE.md` §6) — bắt buộc ở vụ Lê Văn Luyện, vụ thảm sát Bình Phước (hai nạn nhân vị thành niên + một em bé sống sót), và vụ Casey Anthony (nạn nhân là bé gái 2 tuổi, tên không được nêu dù đã trở thành danh xưng gắn liền với vụ án trên toàn cầu)
  - Organized-crime non-glorification / no operational detail (`DOMAIN_GUIDE.md` §8) — vụ Năm Cam
  - Single-sourced/chưa xác minh đầy đủ chi tiết phụ (mức án phụ Đào Quang Khánh, ngày phúc thẩm Lê Văn Luyện, tình trạng hiện tại của Trần Đình Thoại, số liệu khảo sát dư luận vụ Casey Anthony) — cần gắn nhãn độ tin cậy đúng, không nâng thành sự thật đã xác lập
  - Jurisdiction precision (`DOMAIN_GUIDE.md` §2) — vụ O.J. Simpson và vụ Casey Anthony diễn ra dưới luật Hoa Kỳ/common law, không được ngầm suy ra tương đương tố tụng Việt Nam
  - Unproven allegation against a living person (`DOMAIN_GUIDE.md` §4/§5) — cáo buộc xâm hại tình dục của bên bào chữa nhắm vào George Anthony (cha của Casey Anthony) trong vụ Casey Anthony, bị chính ông phủ nhận, chưa từng được chứng minh
required_qa:
  - Domain QA (Hình Sự) — `DOMAIN_QA/DOMAIN_QA_POLICY.md`
  - Research QA
  - Safety QA (net-impression test, victim-privacy, anti-glamorization)
  - Legal-accuracy QA (đặc biệt Điều 74 BLHS 1999 và phân biệt hệ thống luật Việt Nam/Hoa Kỳ)
  - Brand QA
dependencies:
  - DOMAINS/CRIMINAL_LAW/DOMAIN_GUIDE.md
  - DOMAINS/CRIMINAL_LAW/SOURCES/RESEARCH_DRAFT_AN_DA_XU.md
  - DOMAINS/CRIMINAL_LAW/SOURCES/RESEARCH_DRAFT_AN_DA_XU_BATCH2.md
  - DOMAINS/CRIMINAL_LAW/GLOSSARY/DOMAIN_GLOSSARY.md
source_lineage: Tổng hợp `SOURCES/RESEARCH_DRAFT_AN_DA_XU.md` (research date 2026-07-23, bốn vụ án gốc) và `SOURCES/RESEARCH_DRAFT_AN_DA_XU_BATCH2.md` (research date 2026-07-24, hai vụ án bổ sung: Vụ thảm sát Bình Phước, Casey Anthony). Không có nguồn bổ sung nào được đưa vào ngoài hai research draft này; mọi nhãn độ tin cậy trong packet giữ nguyên đúng như research draft, không được nâng cấp.
confidence_level: mixed — xem nhãn độ tin cậy riêng ở từng vụ án bên dưới; không có vụ nào trong sáu vụ có nội dung mâu thuẫn nghiêm trọng về sự kiện cốt lõi, nhưng một số chi tiết phụ vẫn ở mức single-sourced/cần xác minh thêm (xem "Ghi chú tổng hợp cho biên tập viên")
QA_status: draft creative-knowledge asset — chưa qua Domain QA / Research QA / Safety QA chính thức; KHÔNG dùng trực tiếp làm kịch bản sản xuất trước khi human review
---

# KP_CL_002 — Án Đã Xử (Gói Tri Thức Nền Tảng — Pillar 2)

## Packet Control

| Field | Value |
|---|---|
| Packet ID | KP_CL_002 |
| Domain ID | CL (Hình Sự) |
| Canonical Topic | Án Đã Xử / Phá Án — 6 vụ án nền tảng: Năm Cam, Lê Văn Luyện, Cát Tường, O.J. Simpson, Vụ thảm sát Bình Phước, Casey Anthony |
| Object Type | Knowledge Packet |
| Status | draft-pending-human-review |
| Version | 0.2 |
| Risk Level | Critical |
| Dùng cho | Pillar 2 (Án Đã Xử/Phá Án) season episodes; vụ Năm Cam có giá trị dùng kép cho Pillar 5 (Tổ Chức Tội Phạm, tương lai `KP_CL_005`); vụ Lê Văn Luyện có giá trị dùng kép cho Pillar 1 (Luật Hình Sự, tuổi chịu trách nhiệm hình sự) |
| Required QA | Domain QA (Hình Sự), Research QA, Safety QA, Legal-accuracy QA, Brand QA |
| Dependencies | `DOMAIN_GUIDE.md`, `SOURCES/RESEARCH_DRAFT_AN_DA_XU.md`, `SOURCES/RESEARCH_DRAFT_AN_DA_XU_BATCH2.md`, `GLOSSARY/DOMAIN_GLOSSARY.md` |

**Lưu ý trạng thái quan trọng:** Đây là Knowledge Packet nền tảng của Pillar 2 trong domain Hình Sự, tổng hợp ban đầu từ một research draft duy nhất (`RESEARCH_DRAFT_AN_DA_XU.md`, research date 2026-07-23, trạng thái gốc "Draft for Knowledge Packet ingestion") và mở rộng (version 0.2) bằng một batch nghiên cứu bổ sung (`RESEARCH_DRAFT_AN_DA_XU_BATCH2.md`, research date 2026-07-24) thêm hai vụ án: Vụ thảm sát Bình Phước và Casey Anthony. Packet này **không thay thế** yêu cầu Domain QA chính thức — nó là bước tổng hợp trung gian bắt buộc trước khi nội dung có thể chuyển sang sản xuất kịch bản, đúng tinh thần đã áp dụng cho `KP_FS_001` và `KP_BUD_001`. Mọi nhãn độ tin cậy và cờ khoảng-trống-nguồn (gap-flag) trong cả hai research draft được **giữ nguyên, không nâng cấp** khi đưa vào packet này.

---

# Identity

## Phạm vi packet

Sáu vụ án hình sự đã có bản án/phán quyết cuối cùng (bản án/phán quyết có hiệu lực pháp luật, không còn kháng cáo/kháng nghị đang treo tại thời điểm nghiên cứu tương ứng), dùng làm nền tảng cho Pillar 2 (Án Đã Xử/Phá Án):

1. **Vụ án Năm Cam (Trương Văn Cam) và đồng phạm** — Việt Nam, 2001-2004.
2. **Vụ án Lê Văn Luyện** — thảm sát tiệm vàng Ngọc Bích, Bắc Giang, Việt Nam, 2011.
3. **Vụ án thẩm mỹ viện Cát Tường** — Hà Nội, Việt Nam, 2013-2015.
4. **Vụ án O.J. Simpson** — Hoa Kỳ (bang California), phiên hình sự 1995 và phiên dân sự 1996-1997.
5. **Vụ thảm sát Bình Phước (Nguyễn Hải Dương và đồng phạm)** — Việt Nam, 2015-2018 (từ ngày xảy ra án đến ngày thi hành án cuối cùng).
6. **Vụ án Casey Anthony** — Hoa Kỳ (bang Florida), 2008-2013 (từ khi phát hiện mất tích đến phán quyết phúc thẩm cuối cùng).

Bốn vụ đầu (1-3, 5) xảy ra dưới hệ thống pháp luật Việt Nam; hai vụ (4, 6) xảy ra dưới hệ thống pháp luật Hoa Kỳ (common law, có bồi thẩm đoàn) — mọi nội dung kịch bản hóa từ vụ O.J. Simpson hoặc vụ Casey Anthony phải nêu rõ jurisdiction này trước khi phát biểu bất kỳ khái niệm thủ tục nào, đúng `DOMAIN_GUIDE.md` §2.

## Ghi chú áp dụng toàn văn kiện (§6 — không nêu tên nạn nhân vị thành niên)

Ba vụ án trong packet này có nạn nhân vị thành niên, và quy tắc "không bao giờ nêu tên nạn nhân vị thành niên" (`DOMAIN_GUIDE.md` §6 — không có ngoại lệ, áp dụng bất kể chi tiết đã từng xuất hiện công khai trên báo chí hay mức độ nổi tiếng toàn cầu của tên) được áp dụng thống nhất cho cả ba:

- **Vụ Lê Văn Luyện:** hai nạn nhân là trẻ vị thành niên (một cháu bé khoảng 18 tháng tuổi tử vong, một cháu bé khoảng 8 tuổi bị thương) — packet **chủ động không nêu tên**, chỉ mô tả bằng vai trò/quan hệ gia đình/độ tuổi (ví dụ: "ba nạn nhân trong gia đình chủ tiệm vàng," "cháu bé út khoảng 18 tháng tuổi," "cháu bé khoảng 8 tuổi bị thương").
- **Vụ thảm sát Bình Phước:** hai nạn nhân tử vong là trẻ vị thành niên (con trai út khoảng 15 tuổi, một cháu trai họ hàng khoảng 14 tuổi) cộng thêm một em bé khoảng 18 tháng tuổi sống sót — packet **chủ động không nêu tên** cả ba, dù tên đã xuất hiện công khai rộng rãi trên báo chí Việt Nam năm 2015; chỉ mô tả bằng quan hệ gia đình/độ tuổi ước tính.
- **Vụ Casey Anthony:** nạn nhân là con gái hai tuổi của Casey Anthony — dù tên cháu bé đã trở thành một phần gắn liền với cách vụ án được biết đến trên truyền thông quốc tế, packet **không nêu tên cháu ở bất kỳ đâu**, chỉ gọi là "con gái của Casey Anthony"/"cháu bé"/"nạn nhân nhỏ tuổi." Đúng như research draft batch 2 nhấn mạnh: mức độ nổi tiếng toàn cầu của tên một nạn nhân vị thành niên **không phải là căn cứ để miễn trừ** quy tắc §6.

Không có thông tin địa chỉ/liên hệ hiện tại của bất kỳ gia đình nạn nhân nào (Việt Nam hay Hoa Kỳ) được đưa vào tài liệu này.

## Ghi chú áp dụng toàn văn kiện (§4 — net-impression test)

Mọi phần "Script-ready material" bên dưới được viết để giữ nguyên hook/kịch tính của từng vụ án; mọi phần "Production cautions" là nơi ranh giới `DOMAIN_GUIDE.md` được thực thi cụ thể. Theo đúng tinh thần §14 (Transform First), không có vụ nào trong sáu vụ cần bị từ chối hay làm nhạt bớt — chỉ cần đúng khung ngôn ngữ pháp lý và đúng cấu trúc trần thuật.

---

# Canonical Sources

| Source | Mô tả | Tier / Độ tin cậy | Hướng dẫn sử dụng |
|---|---|---|---|
| `SOURCES/RESEARCH_DRAFT_AN_DA_XU.md` | Nghiên cứu gốc cho 4 vụ án đầu (Năm Cam, Lê Văn Luyện, Cát Tường, O.J. Simpson), dựa trên báo chí điều tra trong nước (VnExpress, CAND, Tuổi Trẻ, VietNamNet, Dân Trí, VTV...) và nguồn tiếng Anh uy tín (Britannica, History.com, CNN, NBC News, ESPN, FindLaw...) | Tier 1-2 cho hầu hết sự kiện thủ tục cốt lõi (bản án, ngày tháng, mức án); một số chi tiết phụ chỉ Tier 2-3/single-sourced (xem từng vụ) | Nguồn bắt buộc cho 4 vụ án đầu; không được bổ sung chi tiết nào ngoài research draft này mà chưa qua vòng nghiên cứu bổ sung riêng |
| `SOURCES/RESEARCH_DRAFT_AN_DA_XU_BATCH2.md` | Nghiên cứu bổ sung (research date 2026-07-24) cho 2 vụ án mới (Vụ thảm sát Bình Phước, Casey Anthony), dựa trên báo chí trong nước (VnExpress, Tuổi Trẻ, Thanh Niên, VietNamNet, CAND, PLO, Công Lý, Người Lao Động) và nguồn tiếng Anh uy tín (ABC News, NPR, CBS News, NBC News, CNN, Police1, Oxygen, Crime Museum, Fox News) | Tier 1-2 cho sự kiện thủ tục cốt lõi của cả hai vụ; một số chi tiết phụ chỉ Tier 2-3/single-sourced (xem từng vụ) | Nguồn bắt buộc cho 2 vụ án bổ sung; không được bổ sung chi tiết nào ngoài research draft này mà chưa qua vòng nghiên cứu bổ sung riêng |

Không có khoảng trống nguồn ở cấp "sự kiện cốt lõi" (bản án/phán quyết, mức án, ngày thi hành) cho cả 6 vụ — nhưng có các khoảng trống ở cấp chi tiết phụ, liệt kê trong "Ghi chú tổng hợp cho biên tập viên" ở cuối packet và trong "Production cautions" của từng vụ liên quan.

---

# Case Knowledge Map

Mỗi vụ án dưới đây theo đúng cấu trúc 5 phần dùng ở `KP_FS_001`: Knowledge function / Primary concepts / Narrative detail / Script-ready material / Production cautions.

## Vụ án Năm Cam (Trương Văn Cam và đồng phạm) — 2001-2004

### Knowledge function

Đây là vụ án nền tảng để giới thiệu khán giả với khái niệm "án điểm" (landmark case) trong lịch sử tố tụng hình sự Việt Nam, và là ví dụ rõ nhất trong domain này về việc tội phạm có tổ chức mở rộng được nhờ "bảo trợ chính trị/tư pháp" — cán bộ nhà nước tiếp tay/bao che. **Lưu ý cấu trúc quan trọng:** phần "cấu trúc tổ chức" của Năm Cam trong mục này chỉ được viết đủ sâu để phần tường thuật vụ án (Pillar 2) mạch lạc, dễ hiểu — **không lặp lại toàn bộ chiều sâu phân tích tổ chức** (mô hình 4 tầng: kinh tế/bảo kê/bạo lực/bảo trợ chính trị) đã có trong research draft gốc. Phần phân tích tổ chức tội phạm đầy đủ, chuyên sâu hơn được **dành riêng và tham chiếu tới gói tri thức tương lai `KP_CL_005` (Tổ Chức Tội Phạm)** — khi biên kịch cần khai thác sâu mô hình vận hành/cấu trúc băng nhóm, phải dùng `KP_CL_005` làm nguồn chính, không tự mở rộng chi tiết ở đây.

### Primary concepts

- Trương Văn Cam (Năm Cam, sinh 1947) — trùm giang hồ Sài Gòn - TP.HCM, hoạt động cờ bạc/bảo kê/cưỡng đoạt tài sản khoảng 8 năm (từ 1987), có mạng lưới bảo trợ trong bộ máy nhà nước.
- Quy mô vụ án: **155 bị can, 24 tội danh** — vụ án hình sự quy mô lớn nhất lịch sử tố tụng Việt Nam tính đến thời điểm xét xử; 21 cán bộ, công chức nhà nước bị xử lý vì tiếp tay/bao che.
- Ba cán bộ cấp cao bị nêu danh trong kết luận điều tra công khai vì tiếp tay/bao che (không phải vì cùng vai trò với Năm Cam): Phạm Sỹ Chiến (nguyên Phó Viện trưởng VKSND Tối cao), Bùi Quốc Huy (nguyên Giám đốc Công an TP.HCM/Thứ trưởng Bộ Công an), Trần Mai Hạnh (nguyên Tổng Giám đốc Đài Tiếng nói Việt Nam).
- Chuyên án Z5.01 (từ tháng 5/2001, do Thiếu tướng Nguyễn Việt Thành chỉ huy) → khởi tố 12/2001 → kết thúc điều tra 10/2002.
- Sơ thẩm (25/2–5/6/2003): 6 án tử hình (gồm Năm Cam), 4 án chung thân, cán bộ tha hóa nhận 4-12 năm tù. Phúc thẩm (15/9–30/10/2003): y án tử hình Năm Cam và các đồng phạm chính. Tổng cộng 140 ngày xét xử (sơ thẩm + phúc thẩm).
- Thi hành án: 3/6/2004, tại trường bắn Thủ Đức — Năm Cam và 4 tử tù đồng phạm (Phạm Văn Minh, Nguyễn Hữu Thịnh, Châu Phát Lai Em, Nguyễn Việt Hưng).
- **Trạng thái pháp lý:** bản án có hiệu lực từ 30/10/2003 (phúc thẩm là cấp cuối theo hệ hai cấp Việt Nam), đã thi hành xong 3/6/2004 — đủ điều kiện Format 1 (`DOMAIN_GUIDE.md` §4a): có thể nêu tên và mô tả sự kiện là sự thật đã xác lập.

### Narrative detail

Năm Cam được giới thiệu vào giới giang hồ qua Huỳnh Tỳ, từng là đàn em của Đại Cathay trước 1975, sau đó xây dựng mạng lưới sòng bạc/đá gà/khách sạn-nhà hàng lớn nhất Sài Gòn - TP.HCM. Từng bị bắt đưa đi tập trung cải tạo năm 1995 nhưng được "giải cứu" nhờ hối lộ quan chức — chính sự kiện này sau đó là một phần nội dung bị điều tra lại trong chuyên án 2001-2003. Điểm khiến vụ án trở thành án điểm không chỉ là quy mô (155 bị can/24 tội danh) mà còn là việc lần đầu tiên phanh phui công khai, ở quy mô lớn, tình trạng cán bộ cấp cao ngành công an, kiểm sát, báo chí tiếp tay/bao che cho một mạng lưới tội phạm tồn tại và mở rộng gần 15 năm. Phiên tòa sơ thẩm và phúc thẩm gộp lại kéo dài 140 ngày — được nhiều nguồn báo chí trong nước mô tả là phiên tòa hình sự dài nhất, nhiều bị cáo/tội danh/mức án nhất trong lịch sử tố tụng Việt Nam. Theo tường thuật báo chí, Năm Cam đã thừa nhận tội trước khi bị hành hình và để lại thư xin lỗi gia đình.

### Script-ready material

- Khung tự sự "từ đàn em giang hồ tới ông trùm có bảo trợ chính trị" — nêu bật câu chuyện con người (Năm Cam) song song với câu chuyện thể chế (cán bộ tha hóa), đúng lớp legal/narrative/societal-reflective của `DOMAIN_GUIDE.md` §10.
- Chi tiết chuyên án Z5.01 và việc "giải cứu" năm 1995 rồi bị lật lại năm 2001 — tạo nhịp điều tra kịch tính mà không cần hư cấu thêm.
- 140 ngày xét xử, 155 bị can, 24 tội danh — các con số cụ thể, có thể dùng làm điểm nhấn mở đầu tập.
- Vai trò 3 cán bộ tha hóa (Phạm Sỹ Chiến, Bùi Quốc Huy, Trần Mai Hạnh) — góc nhìn "bảo kê từ trong bộ máy nhà nước," phù hợp lớp societal-reflective (§10) khi phân tích vì sao mạng lưới tồn tại lâu.
- Khi tập phim cần đi sâu hơn vào cách tổ chức của Năm Cam vận hành (các tầng kinh tế/bảo kê/bạo lực), **chuyển hướng khán giả/biên kịch sang `KP_CL_005`** thay vì tự khai triển thêm ở đây.

### Production cautions

- **`DOMAIN_GUIDE.md` §8 (Organized Crime Non-Glorification & No-Operational-Detail):** không trình bày Năm Cam hay mạng lưới của ông ta theo hướng "cool"/hấp dẫn/đáng ngưỡng mộ; trọng tâm tự sự luôn là hậu quả (tử hình, sụp đổ mạng lưới), không phải lối sống/quyền lực. Không cung cấp chi tiết vận hành cụ thể có thể dùng như hướng dẫn (kỹ thuật rửa tiền, cách hối lộ/mua chuộc cụ thể, cách tổ chức cưỡng đoạt) — các chi tiết "cấu trúc tổ chức" sâu hơn được cố ý giữ lại cho `KP_CL_005`, nơi có khung QA riêng cho rủi ro này.
- **`DOMAIN_GUIDE.md` §4/Format 1:** ba cán bộ tha hóa đã có kết luận xử lý kỷ luật/hình sự công khai nên có thể nêu tên, nhưng phải trần thuật đúng vai trò của họ (nhận hối lộ/bao che), không quy gán nhầm hành vi giết người/bạo lực của Năm Cam sang họ.
- **Độ tin cậy cần lưu ý:** chi tiết vai trò cụ thể của từng cán bộ tha hóa dựa trên loạt bài trích "nguyên văn kết luận điều tra" của một nguồn báo chí (VnExpress), tier 2 uy tín nhưng chưa đối chiếu trực tiếp với văn bản bản án gốc — nên diễn đạt là "theo kết luận điều tra được báo chí công bố," không khẳng định tuyệt đối như trích dẫn nguyên văn bản án.
- **Không lặp lại chiều sâu tổ chức:** nhắc lại rõ trong bất kỳ bản dựng kịch bản nào rằng phần "cấu trúc tổ chức" ở đây chỉ phục vụ mạch truyện, phần phân tích sâu (mô hình 4 tầng, cơ chế bảo kê/cưỡng đoạt) thuộc phạm vi `KP_CL_005` và phải tuân theo khung QA riêng của gói đó khi được viết.

---

## Vụ án Lê Văn Luyện — thảm sát tiệm vàng Ngọc Bích, Bắc Giang (2011)

### Knowledge function

Đây là vụ án có **giá trị giáo dục pháp luật cao nhất** trong bốn vụ nền tảng của Pillar 2, nhờ minh họa cụ thể, có thật về cách **Điều 74 Bộ luật Hình sự 1999** (trần 18 năm tù cho người 16-18 tuổi phạm tội trong khung hình phạt tử hình/chung thân) vận hành trong một vụ án cực kỳ nghiêm trọng. Knowledge function kép: (1) tường thuật vụ án cho Pillar 2; (2) case study độc lập cho Pillar 1 (Luật Hình Sự) về tuổi chịu trách nhiệm hình sự khi được khai triển riêng. Đây cũng là vụ án duy nhất trong bốn vụ có nạn nhân vị thành niên, nên là ví dụ bắt buộc phải áp dụng đúng `DOMAIN_GUIDE.md` §6.

### Primary concepts

- Đêm 24/8/2011, tại tiệm vàng Ngọc Bích (huyện Lục Nam, Bắc Giang): Lê Văn Luyện (sinh 18/10/1993, còn khoảng 54 ngày nữa mới đủ 18 tuổi tại thời điểm gây án) đột nhập, sát hại chủ tiệm vàng, vợ của chủ tiệm, và con gái út của họ (khoảng 18 tháng tuổi); một người con gái khác của gia đình (khoảng 8 tuổi) bị chém trọng thương nhưng sống sót. Động cơ theo hồ sơ vụ án: cướp tài sản (vàng) để giải quyết khó khăn tài chính cá nhân.
- **Không nêu tên hai nạn nhân trẻ vị thành niên** — chỉ mô tả bằng vai trò/quan hệ gia đình/độ tuổi, đúng §6 (xem "Ghi chú áp dụng toàn văn kiện" ở đầu packet).
- Bị bắt khoảng 16h30 ngày 31/8/2011, gần biên giới tỉnh Lạng Sơn.
- Sơ thẩm (TAND tỉnh Bắc Giang): tổng hợp hình phạt **18 năm tù giam** — mức tối đa pháp luật cho phép với người chưa đủ 18 tuổi trong khung hình phạt có mức cao nhất là tử hình/chung thân. Phúc thẩm: y án 18 năm tù, kết luận không có căn cứ xác định đồng phạm khác.
- **Điều 74 BLHS 1999:** người từ đủ 16 đến dưới 18 tuổi phạm tội trong khung hình phạt tử hình/chung thân → mức án cao nhất áp dụng không quá 18 năm tù; luật quy định rõ không áp dụng tử hình/chung thân cho người chưa thành niên phạm tội — nguyên tắc nhân đạo/ưu tiên khả năng cải tạo, được giữ nguyên tinh thần trong BLHS 2015 hiện hành.
- **Trạng thái pháp lý:** bản án phúc thẩm đã có hiệu lực pháp luật (không ghi nhận kháng nghị giám đốc thẩm/tái thẩm nào trong nghiên cứu) — đủ điều kiện Format 1 đối với Lê Văn Luyện; không áp dụng cho hai nạn nhân vị thành niên.

### Narrative detail

Vì Luyện chưa đủ 18 tuổi tại thời điểm gây án (dù chỉ thiếu 54 ngày), tòa án buộc phải áp dụng trần 18 năm tù dù hành vi phạm tội — giết ba người trong một gia đình (trong đó có một cháu bé), cướp tài sản, gây thương tích nghiêm trọng cho một cháu bé khác — nếu là người đã thành niên hoàn toàn có thể bị xét xử ở khung hình phạt tử hình. Vụ án tạo ra tranh luận công khai kéo dài về ranh giới tuổi chịu trách nhiệm hình sự và mức án tối đa cho người chưa thành niên: một số ý kiến (kể cả từ giới làm luật) ủng hộ xem xét lại ranh giới/mức trần án phạt trong các trường hợp tội ác đặc biệt nghiêm trọng; nhiều ý kiến khác phản đối, cho rằng nguyên tắc nhân đạo và khả năng cải tạo của người chưa thành niên cần được giữ vững bất kể mức độ nghiêm trọng của hành vi. Đây là ví dụ điển hình để giải thích khoảng cách giữa cảm xúc công chúng (đòi hỏi hình phạt nghiêm khắc hơn) và nguyên tắc pháp luật cứng (trần tuổi/mức án cho vị thành niên) — cần trình bày cả hai phía tranh luận, không thiên vị, đúng lớp societal-reflective ở `DOMAIN_GUIDE.md` §10.

### Script-ready material

- **Hook giáo dục pháp luật chính (ưu tiên hàng đầu, không chỉ là chi tiết phụ):** câu hỏi "Vì sao kẻ sát hại ba người trong một gia đình chỉ phải nhận 18 năm tù?" — dẫn thẳng vào giải thích Điều 74 BLHS 1999 như một bài học về nguyên tắc pháp luật cứng (trần tuổi vị thành niên) đối lập với phản ứng cảm xúc công chúng. Đây là một hook giáo dục pháp luật thật sự, không phải chỉ là một chi tiết gây sốc để tạo kịch tính — bản thân sự chênh lệch giữa mức độ nghiêm trọng của hành vi và mức án tối đa theo luật chính là nội dung giáo dục cốt lõi của tập phim.
- Trình bày song song hai phía tranh luận xã hội (đòi xem xét lại mức trần vs. bảo vệ nguyên tắc nhân đạo/cải tạo cho người chưa thành niên) — cấu trúc "hai luồng ý kiến" giúp khán giả tự suy ngẫm thay vì kênh áp đặt kết luận.
- Chi tiết "còn 54 ngày nữa mới đủ 18 tuổi" — điểm nhấn cụ thể, giàu kịch tính nhưng hoàn toàn dựa trên sự kiện đã xác nhận, không cần thêm thắt.
- Có thể dùng làm cầu nối trực tiếp sang Pillar 1 (Luật Hình Sự) khi cần một case study độc lập giải thích cơ chế trần tuổi vị thành niên trong luật hình sự Việt Nam.

### Production cautions

- **`DOMAIN_GUIDE.md` §6 (không có ngoại lệ):** tuyệt đối không nêu tên hai nạn nhân trẻ vị thành niên, không mô tả chi tiết nhận dạng nào ngoài vai trò/quan hệ gia đình/độ tuổi — áp dụng bất kể tên các cháu đã từng xuất hiện công khai trên báo chí năm 2011. Không dựng lại/tường thuật chi tiết cảm giác đau đớn hoặc hình ảnh graphic về khoảnh khắc các nạn nhân bị sát hại/bị thương — sự kiện và hậu quả pháp lý mang trọng lượng tự sự, không phải chi tiết đau thương được dựng lại.
- **`DOMAIN_GUIDE.md` §10 (không erase lớp nào):** phần tranh luận xã hội về mức án phải trình bày cả hai phía, không được chỉ chọn một phía để tạo cảm giác "đúng/sai" rõ ràng — tránh biến lớp societal-reflective thành lời phán xét thay cho hệ thống pháp luật.
- **Độ tin cậy cần lưu ý:** ngày cụ thể của phiên phúc thẩm ("30/3") chỉ được xác nhận qua tóm tắt tổng hợp, chưa đối chiếu trực tiếp văn bản bản án phúc thẩm gốc — cần xác minh thêm nếu kịch bản dùng làm mốc thời gian chính xác, không khẳng định chắc nịch.
- Nội dung Điều 74 BLHS 1999 (trần 18 năm, không áp dụng tử hình/chung thân cho người chưa thành niên) có độ tin cậy cao, xác nhận qua nhiều nguồn pháp lý chuyên ngành độc lập — an toàn để trình bày chắc chắn như nền pháp lý cứng của tập phim.

---

## Vụ án thẩm mỹ viện Cát Tường (2013-2015)

### Knowledge function

Vụ án minh họa cho khán giả một loại tội phạm khác hẳn hai vụ trên: sai phạm y tế/hành nghề trái phép dẫn đến chết người, cộng thêm hành vi phi tang xác — kết hợp lớp legal/procedural (tội danh, mức án) với lớp narrative giàu kịch tính (9 tháng tìm kiếm thi thể). Đây cũng là vụ án duy nhất trong bốn vụ có nạn nhân trưởng thành được phép nêu tên theo hồ sơ công khai (không thuộc diện phải ẩn danh theo §6).

### Primary concepts

- Ngày 19/10/2013: chị Lê Thị Thanh Huyền (tên nạn nhân đã công khai rộng rãi, không phải người vị thành niên, thuộc phạm vi được phép nêu theo §6) đến Thẩm mỹ viện Cát Tường (Hà Nội) hút mỡ bụng/nâng ngực. Bác sĩ **Nguyễn Mạnh Tường** (chủ cơ sở, không có giấy phép phẫu thuật thẩm mỹ ở quy mô đó) trực tiếp thực hiện; nạn nhân co giật sau gây tê, cấp cứu không thành công, tử vong cùng ngày. Nguyễn Mạnh Tường cùng bảo vệ **Đào Quang Khánh** đưa thi thể lên xe và ném xuống sông Hồng (khu vực cầu Thanh Trì) để phi tang.
- Quá trình tìm kiếm kéo dài **9 tháng 1 ngày**, gồm cả các nỗ lực không hiệu quả (thợ lặn, "ngoại cảm," thiết bị dò tín hiệu điện từ); thi thể được tìm thấy tại bến đò Văn Đức, xác nhận qua giám định ADN.
- Sơ thẩm (5/12/2014, TAND TP. Hà Nội): Nguyễn Mạnh Tường bị tuyên tổng hợp **19 năm tù** (14 năm tội vi phạm quy định khám chữa bệnh + 5 năm tội xâm phạm thi thể), cấm hành nghề y 5 năm sau khi mãn hạn tù, bồi thường gần 600 triệu đồng. Đào Quang Khánh bị tuyên tổng hợp **33 tháng tù** (chia theo hai tội danh — xem lưu ý độ tin cậy bên dưới).
- Phúc thẩm (9/2015): bác kháng cáo, giữ nguyên 19 năm tù đối với Nguyễn Mạnh Tường.
- **Trạng thái pháp lý:** bản án phúc thẩm (9/2015) đã có hiệu lực pháp luật, không ghi nhận kháng nghị giám đốc thẩm/tái thẩm — đủ điều kiện Format 1 đối với cả Nguyễn Mạnh Tường và Đào Quang Khánh.

### Narrative detail

Vụ án gây chấn động dư luận không chỉ vì cái chết của nạn nhân mà vì hành vi phi tang xác kéo dài quá trình tìm kiếm tới hơn 9 tháng — một hành trình có thật, được truyền thông theo sát: tìm kiếm ban đầu dọc sông Hồng với thợ lặn, sự tham gia của những người tự nhận có khả năng "ngoại cảm" (không mang lại kết quả), rồi gia đình nạn nhân nhờ đến thiết bị dò tín hiệu điện từ của Liên hiệp Hội Khoa học và Kỹ thuật tại các địa điểm nghi vấn — cũng không tìm thấy dấu vết. Cuối cùng, sau 9 tháng 1 ngày, thi thể được phát hiện tại bến đò Văn Đức và được xác nhận qua giám định ADN đối chiếu huyết thống với gia đình nạn nhân. Phiên sơ thẩm ban đầu dự kiến 14/4/2014 nhưng bị hoãn do thiếu tài liệu hồ sơ, sau đó mở lại và kết thúc ngày 5/12/2014 với mức án 19 năm tù cho Nguyễn Mạnh Tường.

### Script-ready material

- Hành trình tìm kiếm thi thể kéo dài 9 tháng — mạch tự sự giàu kịch tính, có thật, không cần hư cấu thêm; có thể dùng làm trục chính của tập phim (đầu tập: mất tích/nghi vấn → giữa tập: hành trình tìm kiếm bế tắc → cuối tập: giám định ADN xác nhận, phiên tòa, mức án).
- Chi tiết cấm hành nghề y 5 năm sau khi mãn hạn tù — điểm nhấn tốt cho lớp "hậu quả/hệ thống," cho thấy chế tài không chỉ dừng ở án tù.
- Có thể dùng làm ví dụ cho lớp legal/procedural khi giải thích cách một tội danh y tế (vi phạm quy định khám chữa bệnh) và một tội danh riêng (xâm phạm thi thể) được xét xử tổng hợp hình phạt.

### Production cautions

- **Cần xác minh thêm trước khi công bố là sự kiện đã xác lập (gap-flag rõ ràng từ research draft):** phân chia cụ thể mức án của Đào Quang Khánh giữa hai tội danh (một số nguồn ghi 24 tháng + 9 tháng, tổng 33 tháng, nhưng cách chia tội danh cụ thể sai khác nhỏ giữa các bài báo) và thông tin về việc ra tù trước hạn (khoảng 2017) — cả hai chi tiết này chỉ được xác nhận qua 1-2 nguồn báo chí (single-sourced/lower-confidence theo `DOMAIN_GUIDE.md` §3). **Trước khi một kịch bản phát biểu con số/ngày tháng chính xác này như sự thật đã xác lập, cần đối chiếu thêm với bản án gốc hoặc nguồn tier 1-2 bổ sung** — nếu chưa xác minh được, chỉ nên dùng ngôn ngữ "theo báo chí" hoặc nêu tổng mức án (33 tháng) mà không đi sâu vào cách chia cụ thể.
- Nạn nhân (chị Lê Thị Thanh Huyền) là người trưởng thành, tên đã công khai rộng rãi trên hồ sơ/báo chí — được phép nêu tên theo §6, nhưng vẫn cần giữ giọng điệu tôn trọng, không dựng lại chi tiết đau đớn/graphic của quá trình tử vong hay quá trình phi tang vượt quá mức cần thiết cho hiểu biết sự thật (`DOMAIN_GUIDE.md` §6, §9).
- Không dùng các chi tiết về "ngoại cảm"/tìm kiếm tâm linh trong quá trình tìm xác theo hướng khẳng định hiệu quả hay cổ súy — chỉ nêu như một sự kiện đã xảy ra trong hành trình tìm kiếm (không mang lại kết quả), tránh vô tình quảng bá cho hoạt động ngoại cảm.

---

## Vụ án O.J. Simpson (Hoa Kỳ) — hình sự (1995) và dân sự (1997)

### Knowledge function

Đây là vụ án so sánh luật tốt nhất trong bốn vụ nền tảng — dùng để minh họa cho khán giả Việt Nam sự khác biệt giữa hệ thống thông luật (common law, Hoa Kỳ, có bồi thẩm đoàn) và hệ thống luật thành văn (civil law, Việt Nam), cũng như sự khác biệt giữa mức độ chứng minh hình sự ("beyond a reasonable doubt") và mức độ chứng minh dân sự ("preponderance of the evidence"). Đồng thời — và đây là điểm quan trọng nhất về mặt biên tập — đây là **ví dụ rõ ràng nhất trong toàn bộ domain này về rủi ro của "net-impression test"** (`DOMAIN_GUIDE.md` §4): vụ án có hai phán quyết khác tầng (trắng án hình sự + chịu trách nhiệm dân sự) rất dễ bị một kịch bản vô tình gộp lại thành một kết luận "có tội" duy nhất nếu không cẩn thận về cấu trúc và ngôn từ. Packet này dùng vụ O.J. Simpson làm **ví dụ giảng dạy (teaching example) bắt buộc tham khảo** cho bất kỳ biên kịch nào trong domain, không chỉ riêng cho vụ này.

### Primary concepts

- **Bối cảnh:** xảy ra dưới hệ thống pháp luật Hoa Kỳ, bang California — có bồi thẩm đoàn (jury trial), khái niệm không tồn tại trong tố tụng hình sự Việt Nam (Việt Nam dùng hội đồng xét xử gồm thẩm phán và hội thẩm nhân dân). Phải nêu rõ jurisdiction này trước khi phát biểu bất kỳ khái niệm thủ tục nào (`DOMAIN_GUIDE.md` §2).
- **Phiên hình sự (bắt đầu 24/1/1995, Thẩm phán Lance Ito; công tố Marcia Clark/Christopher Darden; bào chữa "Dream Team" do Johnnie Cochran dẫn đầu):** Simpson bị truy tố tội giết vợ cũ Nicole Brown Simpson và Ronald Goldman. Ngày 3/10/1995, bồi thẩm đoàn tuyên **trắng án (not guilty)** đối với cả hai tội danh, sau khi nghị án chưa đầy 4 giờ. Khoảnh khắc nổi tiếng: thử găng tay không vừa ("if it doesn't fit, you must acquit").
- **Phiên dân sự (1996-1997):** gia đình hai nạn nhân khởi kiện đòi bồi thường "wrongful death." Bồi thẩm đoàn dân sự (khác bồi thẩm đoàn hình sự, áp dụng mức chứng minh thấp hơn) nhất trí kết luận Simpson phải chịu **trách nhiệm dân sự**, tuyên bồi thường **33,5 triệu USD**; phán quyết được tòa phúc thẩm California giữ nguyên.
- **Câu trích tòa phúc thẩm dân sự** ("bồi thẩm đoàn dân sự trên thực tế đã kết luận Simpson đã thực hiện hai vụ giết người có chủ đích, tàn bạo") — chỉ xuất hiện qua một nguồn tổng hợp (FindLaw), độ tin cậy trung bình; đây là nhận định **trong khuôn khổ phán quyết dân sự**, không phải một bản án hình sự.
- Simpson qua đời 10/4/2024 tại Las Vegas, do ung thư — xác nhận qua nhiều nguồn lớn độc lập (CNN, NBC News, ESPN), độ tin cậy cao.
- **Trạng thái pháp lý kép, không được đơn giản hóa:** về mặt hình sự, Simpson **chưa từng bị kết án** giết người (trắng án, và theo nguyên tắc double jeopardy của luật Mỹ không thể bị xử lại cùng tội danh) — dù đã qua đời, không có bản án kết tội hình sự nào tồn tại để áp dụng ngoại lệ "người đã mất có bản án kết tội cuối cùng" của `DOMAIN_GUIDE.md` §4 (ngoại lệ đó chỉ áp dụng khi có bản án *kết tội*, không áp dụng cho trường hợp trắng án). Về mặt dân sự, ông bị tuyên chịu trách nhiệm bồi thường.

### Narrative detail

Vụ án là một trong những phiên tòa được theo dõi nhiều nhất lịch sử truyền hình Mỹ — ước tính khoảng 150 triệu người xem trực tiếp lúc tuyên án hình sự. Vì bản án trắng án đã có hiệu lực và không thể xử lại theo nguyên tắc double jeopardy (khái niệm luật Mỹ, chỉ tương đương một phần với nguyên tắc "không ai bị kết án hai lần vì một tội phạm" nhưng không nên đánh đồng cơ chế chi tiết với luật tố tụng Việt Nam), về mặt hình sự Simpson không phải là người đã bị kết án giết người. Ngược lại, phiên dân sự sau đó — với mức chứng minh thấp hơn ("preponderance of the evidence" thay vì "beyond a reasonable doubt") — kết luận ông phải chịu trách nhiệm dân sự cho cái chết của hai nạn nhân, phán quyết được tòa phúc thẩm giữ nguyên. Khoản bồi thường 33,5 triệu USD phần lớn không được thanh toán trong suốt phần đời còn lại của Simpson; sau khi ông qua đời (10/4/2024, ung thư), gia đình Goldman đã nộp yêu cầu đòi nợ đối với di sản của ông.

### Script-ready material

- Khung "một vụ án, hai phiên tòa, hai tiêu chuẩn chứng minh khác nhau" — hook so sánh luật tự nhiên, đặc biệt hữu ích để giải thích khái niệm common law/civil law và sự khác biệt burden of proof cho khán giả Việt Nam vốn quen với hệ thống luật thành văn.
- Chi tiết "găng tay không vừa" và câu nói "if it doesn't fit, you must acquit" — hình ảnh trực quan, dễ nhớ, có thật, không cần thêm thắt.
- Cấu trúc tập phim gợi ý: mở đầu bằng phiên hình sự và kết quả trắng án → giải thích vì sao trắng án không đồng nghĩa "vô tội tuyệt đối" theo mọi nghĩa pháp lý → chuyển sang phiên dân sự và kết quả chịu trách nhiệm dân sự → chốt lại bằng đúng hai tầng phán quyết, không gộp thành một kết luận duy nhất.
- Cái chết của Simpson (2024) có thể dùng làm điểm neo thời sự/mở đầu tập ("người đàn ông được cả nước Mỹ theo dõi qua TV năm 1995 vừa qua đời năm 2024 — nhưng câu hỏi pháp lý cốt lõi của vụ án chưa bao giờ có một câu trả lời duy nhất").

### Production cautions

- **Đây là ranh giới quan trọng nhất của toàn bộ mục này, và là ví dụ giảng dạy bắt buộc cho `DOMAIN_GUIDE.md` §4 (net-impression test):** kịch bản **tuyệt đối không được trộn lẫn hai tầng phán quyết** (trắng án hình sự + chịu trách nhiệm dân sự) thành một kết luận "có tội" chung, dù mỗi câu riêng lẻ có vẻ hedge đúng. Cụ thể: không được nói hoặc ngụ ý "Simpson đã giết người" hay "Simpson là hung thủ" ở bất kỳ đâu trong kịch bản — kể cả khi trích dẫn nhận định của tòa phúc thẩm dân sự ("trên thực tế đã kết luận Simpson đã thực hiện hai vụ giết người...") — câu trích này **bắt buộc phải luôn đi kèm bối cảnh** rằng đây là nhận định trong khuôn khổ vụ kiện dân sự, theo tiêu chuẩn chứng minh dân sự thấp hơn tiêu chuẩn hình sự, không phải một bản án hình sự kết tội. Việc tách câu trích này khỏi ngữ cảnh dân sự, hoặc dùng tông giọng/cấu trúc kịch bản (ví dụ: dựng phiên dân sự như "màn lật ngược sự thật," hay đặt tên/thumbnail ngụ ý "cuối cùng công lý đã tìm ra hung thủ") để khán giả kết luận Simpson "thực ra có tội," là vi phạm net-impression test dù từng câu chữ có hedge đúng — QA phải đánh giá ấn tượng tổng thể của tập phim, không chỉ tìm-và-thay các cụm hedge.
- Không dùng cái chết của Simpson (2024) như một cái cớ để "bây giờ có thể nói thẳng ông ta có tội" — ngoại lệ của §4 dành cho người đã mất chỉ áp dụng khi đã có **bản án kết tội cuối cùng**; trường hợp này là trắng án, nên chiều áp dụng đúng là giữ nguyên hiện trạng "trắng án hình sự, chịu trách nhiệm dân sự" — không đơn giản hóa theo hướng nào.
- **`DOMAIN_GUIDE.md` §2 (jurisdiction precision):** phải nêu rõ đây là vụ án dưới luật Hoa Kỳ/bang California, có bồi thẩm đoàn — không dùng thuật ngữ tố tụng Việt Nam (hội đồng xét xử, hội thẩm nhân dân) để mô tả, và không ngụ ý thủ tục này áp dụng tương tự ở Việt Nam. Khái niệm "double jeopardy" phải được giới thiệu như một khái niệm luật Mỹ, không đánh đồng cơ chế chi tiết với nguyên tắc tố tụng hình sự Việt Nam dù có điểm tương đồng khái quát.
- **Độ tin cậy cần lưu ý:** câu trích dẫn từ tòa phúc thẩm dân sự chỉ xác nhận qua một nguồn tổng hợp (FindLaw) — nên xác minh thêm qua văn bản phán quyết phúc thẩm gốc nếu kịch bản dự định trích nguyên văn; nếu không xác minh được, vẫn có thể diễn giải ý nhưng nên gắn nhãn "theo một số nguồn tổng hợp" thay vì trích nguyên văn như sự thật tuyệt đối.

---

## Vụ thảm sát Bình Phước — Nguyễn Hải Dương và đồng phạm (2015)

### Knowledge function

Đây là vụ án có giá trị riêng biệt trong packet để minh họa một nguyên tắc dễ bị bỏ qua khi tường thuật một tội ác do nhiều người cùng thực hiện: **đồng phạm không đồng nghĩa đồng mức trách nhiệm.** Ba bị cáo trong cùng một vụ án nhận ba mức án khác nhau rõ rệt (tử hình – tử hình – 16 năm tù) tùy theo vai trò thực tế của từng người, và một kịch bản gộp chung "các hung thủ" thành một khối duy nhất vừa sai sự thật vừa vi phạm net-impression test (`DOMAIN_GUIDE.md` §4) đối với riêng bị cáo có vai trò nhẹ hơn — người đã rút lui trước khi vụ giết người xảy ra. Đây cũng là vụ án thứ hai trong toàn bộ packet (sau Lê Văn Luyện) có nạn nhân vị thành niên, và là vụ đầu tiên có thêm một người sống sót vị thành niên (một em bé) cần được ẩn danh theo cùng nguyên tắc §6.

### Primary concepts

- Sáng **7/7/2015**, tại một căn biệt thự ở xã Minh Hưng, huyện Chơn Thành, tỉnh Bình Phước: sáu người trong gia đình ông Lê Văn Mỹ (giám đốc một công ty chế biến gỗ) bị sát hại. Thủ phạm chính, **Nguyễn Hải Dương**, là bạn trai cũ của con gái lớn nhà ông Mỹ; động cơ theo hồ sơ vụ án là "hận tình" (bị gia đình bạn gái cũ phản đối/chia tay) kết hợp ý định cướp tài sản.
- Sáu nạn nhân tử vong: ông Lê Văn Mỹ (48 tuổi), vợ ông (tên xuất hiện với hai cách viết khác nhau giữa các nguồn — "Lê Thị Ánh Nga"/"Nguyễn Lê Thị Ánh Nga", 42 tuổi, cần xác minh thêm nếu kịch bản cần trích tên đầy đủ chính xác), con gái lớn Lê Thị Ánh Linh (22 tuổi, bạn gái cũ của Dương), một cháu gái họ hàng (nữ sinh vừa thi tốt nghiệp THPT, 18 tuổi — độ tuổi được xác nhận trực tiếp qua một bài báo chuyên đề, nên thuộc phạm vi có thể nêu theo §6 vì đã thành niên; tuy nhiên nghiên cứu gốc không cung cấp tên riêng cho nạn nhân này, nên tài liệu này mô tả bằng vai trò/độ tuổi thay vì suy đoán một cái tên), và **hai nạn nhân vị thành niên** — con trai út của ông Mỹ (khoảng 15 tuổi) và một cháu trai họ hàng (khoảng 14 tuổi, người mở cổng cho hung thủ). Một em bé khoảng 18 tháng tuổi sống sót vì một trong hai hung thủ đã không ra tay với em.
- **Không nêu tên hai nạn nhân vị thành niên và em bé sống sót** — chỉ mô tả bằng quan hệ gia đình/độ tuổi ước tính, đúng §6 (xem "Ghi chú áp dụng toàn văn kiện" ở đầu packet).
- Nguyễn Hải Dương bị bắt **10/7/2015** (trong vòng khoảng 80 giờ kể từ khi phát hiện vụ án, dựa trên dấu vân tay, mẫu máu, dữ liệu điện thoại); đồng phạm **Vũ Văn Tiến** bị bắt cùng ngày tại TP.HCM; nghi can thứ ba, **Trần Đình Thoại**, bị bắt khoảng đầu/giữa tháng 8/2015 (một số nguồn ghi 10/8/2015).
- **Ba vai trò khác biệt rõ rệt — điểm quan trọng nhất cần giữ chính xác, không được gộp chung thành "các hung thủ":**
  - **Nguyễn Hải Dương** — chủ mưu, trực tiếp thực hiện phần lớn/toàn bộ hành vi giết người theo cáo trạng và tường thuật phiên tòa.
  - **Vũ Văn Tiến** — đồng phạm trực tiếp có mặt tại hiện trường, khống chế/giữ nạn nhân trong khi Dương ra tay; bị tuyên cùng mức án tử hình như Dương.
  - **Trần Đình Thoại** — vai trò khác biệt rõ rệt: theo hồ sơ vụ án, từng đồng ý tham gia kế hoạch và có hành vi hỗ trợ vật chất (một số nguồn nêu cụ thể là mua dao cho Dương), nhưng **rút lui, không có mặt/không trực tiếp thực hiện hành vi giết người tại hiện trường** đêm xảy ra án — vì vậy chỉ bị truy tố và xét xử ở mức án thấp hơn nhiều, không phải tử hình.
- **Sơ thẩm (17/12/2015, TAND tỉnh Bình Phước):** Nguyễn Hải Dương — tử hình (giết người + cướp tài sản); Vũ Văn Tiến — tử hình (giết người + cướp tài sản); Trần Đình Thoại — 16 năm tù (13 năm giết người + 3 năm cướp tài sản). Cả ba buộc bồi thường dân sự khoảng 480 triệu đồng cho gia đình nạn nhân.
- Nguyễn Hải Dương **không kháng cáo**, chấp nhận bản án tử hình (một số nguồn ghi ông nộp đơn xin sớm thi hành án cuối tháng 3/2016, nhưng đơn này không có giá trị pháp lý vì tử tù không có quyền tự quyết định thời điểm thi hành án). Vũ Văn Tiến và Trần Đình Thoại đều kháng cáo xin giảm nhẹ. **Phúc thẩm (18/7/2016, Tòa án Cấp cao tại TP.HCM):** bác toàn bộ kháng cáo, y án tử hình Vũ Văn Tiến và y án 16 năm tù Trần Đình Thoại; bản án của Nguyễn Hải Dương có hiệu lực theo cơ chế không kháng cáo.
- **Thi hành án:** Nguyễn Hải Dương — tiêm thuốc độc, 7 giờ sáng **17/11/2017**, tại một cơ sở ở huyện Phú Giáo, tỉnh Bình Dương. Vũ Văn Tiến — tiêm thuốc độc, khoảng 4 giờ sáng **20/9/2018**, tại Bình Phước. Trần Đình Thoại — đang thụ án 16 năm tù; **không tìm thấy thông tin đã kiểm chứng** về việc giảm án/ra tù sớm tính đến thời điểm nghiên cứu (2026-07-24).
- **Trạng thái pháp lý:** cả ba bị cáo đều có bản án đã có hiệu lực pháp luật, không còn kháng cáo/kháng nghị đang treo (Dương: không kháng cáo, bản án sơ thẩm có hiệu lực; Tiến và Thoại: bản án phúc thẩm 18/7/2016 là chung thẩm); không có nguồn nào cho thấy giám đốc thẩm/tái thẩm được mở lại. Đủ điều kiện Format 1 (`DOMAIN_GUIDE.md` §4a) đối với cả ba người — có thể nêu tên và mô tả là người đã bị kết án, đúng vai trò riêng của từng người. **Không áp dụng cho hai nạn nhân vị thành niên và em bé sống sót — không được nêu tên theo §6.**

### Narrative detail

Vụ án được phát hiện sáng 7/7/2015 khi người làm công phát hiện các thi thể; tốc độ phá án — xác định và bắt giữ chủ mưu trong khoảng 80 giờ dựa trên dấu vân tay, mẫu máu và dữ liệu điện thoại — là một mạch tự sự có thật, giàu kịch tính mà không cần thêm thắt. Nhưng phần quan trọng nhất về mặt biên tập không phải là tốc độ phá án mà là cách ba bị cáo, cùng bị xét xử trong một vụ án, bước ra khỏi phiên tòa với ba số phận khác nhau hoàn toàn: hai người bị tuyên và thi hành án tử hình cách nhau gần một năm, người thứ ba — người đã rút lui trước đêm xảy ra án — nhận 16 năm tù. Sự khác biệt này không phải là một chi tiết phụ có thể lược bỏ để đơn giản hóa câu chuyện; nó chính là bài học pháp luật cốt lõi của vụ án này, tương tự cách Điều 74 BLHS 1999 là bài học cốt lõi của vụ Lê Văn Luyện. Phiên sơ thẩm và phúc thẩm không ghi nhận tranh chấp nào về việc ba bị cáo có tội hay không, hay về kết quả cuối cùng của vụ án; toàn bộ diễn biến tố tụng — từ khởi tố đến hai lần thi hành án tử hình cách nhau gần một năm — đã khép lại về mặt pháp lý.

### Script-ready material

- Khung tự sự "một hiện trường, ba số phận" — mở đầu bằng tốc độ phá án (80 giờ), sau đó tách rõ ba tuyến vai trò và ba kết cục pháp lý khác nhau, thay vì gộp chung thành một cao trào duy nhất.
- Trường hợp Trần Đình Thoại là chất liệu giá trị cho lớp legal/procedural: minh họa cụ thể việc pháp luật phân biệt mức độ trách nhiệm hình sự dựa trên hành vi thực tế (rút lui trước khi tội ác xảy ra), không dựa trên việc "có mặt trong kế hoạch ban đầu."
- Chi tiết em bé khoảng 18 tháng tuổi sống sót vì một trong hai hung thủ không ra tay — có thể nêu như một sự kiện đã xác lập, nhưng không mô tả danh tính, hoàn cảnh sống hiện tại, hay bất kỳ chi tiết nhận dạng nào của em (em vẫn là một người thật đang lớn lên).
- Khoảng cách thời gian giữa hai lần thi hành án tử hình (17/11/2017 và 20/9/2018, cách nhau gần một năm dù cùng tuyên án một ngày) là một chi tiết thủ tục có thật, có thể dùng để giải thích cho khán giả rằng thi hành án tử hình ở Việt Nam không diễn ra đồng thời cho các đồng phạm dù cùng mức án.

### Production cautions

- **Yêu cầu cấu trúc quan trọng nhất:** trong mọi bản dựng kịch bản, ba bị cáo phải được nhắc đến bằng tên và vai trò riêng xuyên suốt — không dùng cụm "các hung thủ"/"bọn chúng" để gộp chung ba người, đặc biệt không được để Trần Đình Thoại bị cuốn vào ấn tượng "đồng phạm giết người trực tiếp" như hai người kia (vi phạm net-impression test, `DOMAIN_GUIDE.md` §4, đối với riêng ông ta).
- **`DOMAIN_GUIDE.md` §6 (không có ngoại lệ):** tuyệt đối không nêu tên hai nạn nhân vị thành niên và em bé sống sót, không mô tả chi tiết nhận dạng nào ngoài vai trò/quan hệ gia đình/độ tuổi ước tính — áp dụng bất kể tên cả ba đã từng xuất hiện công khai trên báo chí năm 2015. Không dựng lại/tường thuật chi tiết graphic về khoảnh khắc các nạn nhân bị sát hại — sự kiện và hậu quả pháp lý mang trọng lượng tự sự, không phải chi tiết đau thương được dựng lại (§9).
- **Độ tin cậy cần lưu ý:** phân chia vai trò cụ thể của Trần Đình Thoại (mua dao, rút lui khỏi hiện trường) ở mức tin cậy trung bình-cao — xác nhận qua tổng hợp nhiều bài báo nhưng chưa đối chiếu trực tiếp với văn bản bản án gốc; nên diễn đạt "theo hồ sơ vụ án được báo chí công bố," không khẳng định như trích dẫn nguyên văn bản án. Tên đầy đủ của người vợ nạn nhân có hai cách viết khác nhau giữa các nguồn — cần xác minh thêm nếu kịch bản cần trích tên chính xác. Độ tuổi của cháu gái họ hàng 18 tuổi có sai lệch nhỏ về năm sinh giữa các nguồn, nhưng độ tuổi 18 (thành niên) được một bài báo chuyên đề xác nhận trực tiếp nên tài liệu này xử lý nạn nhân này là người thành niên.
- **Khoảng trống nguồn:** tình trạng hiện tại của Trần Đình Thoại (đã ra tù/giảm án hay chưa, tính đến 2026) — không tìm thấy nguồn cập nhật trong nghiên cứu này; nếu kịch bản cần nêu tình trạng hiện tại của ông, phải xác minh thêm trước, không suy đoán.

---

## Vụ án Casey Anthony (Hoa Kỳ, bang Florida, 2008-2011)

### Knowledge function

Đây là vụ án đối lập trực tiếp — và là bài học đồng hành bắt buộc tham chiếu — với vụ **O.J. Simpson** đã có ở trên trong packet này. Nếu vụ Simpson minh họa cấu trúc "hai phán quyết khác tầng" (trắng án hình sự + chịu trách nhiệm dân sự) trong bối cảnh dư luận Mỹ khi đó bị chia rẽ, thì vụ Casey Anthony minh họa chiều ngược lại: gần như toàn bộ công luận Mỹ theo dõi vụ án tin chắc bị cáo có tội giết con, nhưng bồi thẩm đoàn hình sự vẫn tuyên **trắng án hoàn toàn** đối với các tội danh giết người — không có một tầng phán quyết dân sự đối trọng nào như vụ Simpson để "cân bằng" kết quả trong mắt công chúng. Cùng với vụ Simpson, đây là cặp bài học so sánh luật giá trị nhất trong packet về khoảng cách giữa niềm tin công chúng và tiêu chuẩn chứng minh pháp lý "beyond a reasonable doubt" (không còn nghi ngờ hợp lý) — và là ví dụ thứ hai trong packet về nguyên tắc double jeopardy của luật Mỹ, áp dụng theo chiều ngược với vụ Simpson: ở đây, double jeopardy bảo vệ một người đã được trắng án khỏi bị xử lại cùng tội danh, bất kể niềm tin của công chúng.

### Primary concepts

- **Bối cảnh:** xảy ra dưới hệ thống pháp luật Hoa Kỳ, bang Florida — thông luật (common law), có bồi thẩm đoàn (jury), khái niệm không tồn tại trong tố tụng hình sự Việt Nam. Phải nêu rõ jurisdiction này trước khi phát biểu bất kỳ khái niệm thủ tục nào (`DOMAIN_GUIDE.md` §2).
- Con gái hai tuổi của Casey Anthony (**không nêu tên ở bất kỳ đâu trong mục này, đúng §6 — gọi là "con gái của Casey Anthony"/"cháu bé"/"nạn nhân nhỏ tuổi" xuyên suốt**) được nhìn thấy lần cuối còn sống ngày **16/6/2008**. Bà ngoại cháu bé (Cindy Anthony) trình báo mất tích với cảnh sát ngày **15/7/2008** — khoảng một tháng sau — sau khi phát hiện Casey Anthony không báo cáo và có nhiều lời khai không nhất quán, gồm khai cháu bé bị một người giữ trẻ có tên hư cấu bắt cóc; người giữ trẻ này sau đó được xác định là không tồn tại.
- Ngày **17/7/2008**, một con chó nghiệp vụ phát hiện dấu vết mùi phân hủy tử thi trong cốp xe ô tô của Casey Anthony. Casey Anthony bị bắt ngày **14/10/2008** với các cáo buộc ban đầu: bỏ mặc trẻ em (child neglect), khai báo gian dối, cản trở điều tra. Ngày **11/12/2008**, hài cốt của cháu bé được tìm thấy trong khu vực cây cối gần nhà ông bà ngoại, đã phân hủy nhiều tháng; hộp sọ có băng dính quanh vùng mũi/miệng/hàm.
- Bên công tố cáo buộc Casey Anthony làm cháu bé bất tỉnh bằng chloroform, sau đó dùng băng dính bịt đường thở khiến cháu bé tử vong ngạt thở, rồi vứt xác. Một trong những bằng chứng gây tranh cãi nhất tại phiên tòa: lịch sử tìm kiếm từ khóa "chloroform" trên máy tính gia đình (một chuyên gia phần mềm trình bày 84 lần tìm kiếm) — nhưng mẹ của Casey Anthony, bà Cindy Anthony, sau đó khai trước tòa rằng chính bà mới là người tìm kiếm từ khóa này (liên quan đến việc chó nhà bà ăn phải lá cây có chất diệp lục), không phải Casey Anthony — một chi tiết pháp y/nhân chứng gây tranh cãi lớn về độ tin cậy của bằng chứng buộc tội.
- **Lưu ý §4/§5 bắt buộc:** trong tuyên bố mở đầu phiên tòa, luật sư bào chữa Jose Baez đưa ra giả thuyết cháu bé chết đuối do tai nạn trong hồ bơi của ông bà ngoại, và cáo buộc Casey Anthony từng bị chính cha mình (George Anthony) xâm hại tình dục thời thơ ấu — được mô tả là nguyên nhân dẫn đến "cơ chế đối phó" khiến bà nói dối trong gần ba năm. **George Anthony đã phủ nhận hoàn toàn** cả việc liên quan đến cái chết của cháu bé, việc phi tang thi thể, lẫn cáo buộc xâm hại tình dục; không có nhân chứng nào, kể cả chính George Anthony, xác nhận cáo buộc này, và một bức thư tuyệt mệnh trước đó của ông (viết trong giai đoạn khủng hoảng tâm lý riêng, tháng 1/2009) không hề nhắc đến nội dung này. **Đây là một tuyên bố chưa được chứng minh của bên bào chữa, bị chính người bị cáo buộc phủ nhận, không có bằng chứng/nhân chứng xác nhận — tuyệt đối không được trình bày như một sự thật đã xác lập trong bất kỳ kịch bản nào; nếu nhắc đến, phải giữ nguyên khung "cáo buộc của luật sư bào chữa, bị phủ nhận."**
- Bên công tố ban đầu (tháng 12/2008) thông báo sẽ không truy tố tử hình, nhưng đến tháng 4/2009 đã đảo ngược quyết định, chính thức tìm kiếm án tử hình; quá trình tuyển chọn bồi thẩm đoàn (bắt đầu 9/5/2011) áp dụng tiêu chuẩn "đủ điều kiện xét xử tử hình" (death-qualified jury).
- Phiên tòa diễn ra tại Florida, Thẩm phán Belvin Perry chủ tọa, kéo dài khoảng 6 tuần. Ngày **5/7/2011**, sau khoảng 10 giờ 40 phút nghị án, bồi thẩm đoàn tuyên **trắng án (not guilty)** đối với ba tội danh nghiêm trọng nhất — giết người cấp độ một, ngược đãi trẻ em nghiêm trọng, ngộ sát nghiêm trọng trẻ em — và **có tội (guilty)** đối với bốn tội danh nhẹ hơn: cung cấp thông tin sai sự thật cho cơ quan thực thi pháp luật, liên quan đến các lời khai gian dối về người giữ trẻ hư cấu và các tình tiết khác trong điều tra ban đầu.
- **Tuyên án:** đối với bốn tội danh khai báo gian dối, thẩm phán tuyên phạt tổng cộng 4 năm tù giam (mức tối đa, cộng dồn) và phạt tiền 1.000 USD mỗi tội (tổng 4.000 USD). Do đã bị tạm giam gần ba năm chờ xét xử (tính trừ vào thời gian thụ án) cùng giảm trừ vì cải tạo tốt, Casey Anthony được trả tự do ngày **17/7/2011** — chỉ vài ngày sau khi tuyên án.
- **Phúc thẩm:** Casey Anthony kháng cáo bốn tội danh khai báo gian dối (không kháng cáo phần trắng án vì đó là kết quả có lợi cho bà). Ngày **25/1/2013**, Tòa Phúc thẩm Khu vực 5 của Florida tuyên hủy 2 trong 4 tội danh khai báo gian dối vì vi phạm nguyên tắc double jeopardy — tòa nhận định luật không có ý định trừng phạt riêng biệt cho từng lời khai sai trong cùng một buổi thẩm vấn. Kết quả cuối cùng: còn lại 2 tội danh khai báo gian dối bị kết án (thay vì 4). Không tìm thấy nguồn nào cho thấy phán quyết này sau đó bị kháng nghị lên cấp cao hơn hoặc bị đảo ngược.
- **Trạng thái pháp lý tổng thể:** nhánh giết người — trắng án có hiệu lực, không thể bị xử lại cùng tội danh theo nguyên tắc double jeopardy; nhánh khai báo gian dối — đã thụ án xong, kết quả phúc thẩm 25/1/2013 (còn 2/4 tội danh) là kết quả cuối cùng được tìm thấy trong nghiên cứu này. **Về mặt hình sự, Casey Anthony không phải là người đã bị kết án giết con** — tuyệt đối không được viết kịch bản theo hướng ngầm khẳng định điều ngược lại bằng tông giọng, cấu trúc, tiêu đề, hay thumbnail (net-impression test), dù dư luận Mỹ đương thời và nhiều năm sau đó vẫn có một bộ phận lớn công chúng tin bà có tội (số liệu khảo sát cụ thể chưa được tài liệu này xác minh trực tiếp qua nguồn gốc — xem ghi chú độ tin cậy).

### Narrative detail

Từ góc độ biên tập, giá trị lớn nhất của vụ án này nằm ở khoảng cách giữa hai câu chuyện chạy song song: câu chuyện dư luận (gần như đồng thuận rằng Casey Anthony đã giết con mình, được củng cố bởi gần ba năm nói dối về người giữ trẻ hư cấu, hành vi không báo mất tích trong một tháng, và các chi tiết pháp y gây sốc như dấu vết phân hủy trong cốp xe) và câu chuyện pháp lý (bồi thẩm đoàn kết luận công tố không chứng minh được tội giết người "vượt quá nghi ngờ hợp lý," một phần vì chính bằng chứng "tìm kiếm chloroform" — trụ cột của lập luận buộc tội — bị chính mẹ của bị cáo làm suy yếu ngay tại tòa). Đây không phải là một vụ án nơi có sự mơ hồ về sự kiện cốt lõi (bồi thẩm đoàn tuyên trắng án là một sự kiện không tranh cãi); sự tranh cãi nằm hoàn toàn ở tầng xã hội — liệu kết quả đó có "đúng" hay không — một tranh luận xã hội, không phải một tranh chấp về sự kiện pháp lý đã xảy ra. Giả thuyết chết đuối do tai nạn của bên bào chữa và cáo buộc xâm hại tình dục nhắm vào George Anthony là hai yếu tố then chốt trong chiến lược bào chữa nhằm tạo ra nghi ngờ hợp lý, nhưng cả hai đều chưa từng được chứng minh là sự thật — tòa án không đưa ra kết luận về việc cháu bé chết đuối do tai nạn hay bị giết, chỉ kết luận công tố chưa chứng minh được tội giết người.

### Script-ready material

- Khung "bài học đồng hành với vụ O.J. Simpson" — dùng trực tiếp làm cầu nối trong kịch bản: "Nếu vụ Simpson là một vụ án nơi dư luận bị chia rẽ, thì đây là vụ án nơi cả nước Mỹ gần như đồng lòng tin có tội — nhưng luật pháp lại nói khác." Đây là hook so sánh luật tự nhiên, không cần thêm thắt.
- Chi tiết "84 lần tìm kiếm chloroform" và cú lật ngược tại tòa khi mẹ của bị cáo nhận mình mới là người tìm kiếm — một khoảnh khắc kịch tính có thật, minh họa cụ thể cách một bằng chứng tưởng như quyết định có thể sụp đổ trước tòa.
- Cấu trúc tập phim gợi ý: mở đầu bằng sự mất tích và các lời khai gian dối (gần ba năm nói dối) → hành trình điều tra và phát hiện hài cốt → phiên tòa và bằng chứng gây tranh cãi → trắng án 5/7/2011 và phản ứng dư luận → chốt lại bằng khung "double jeopardy nghĩa là gì" và tham chiếu chéo tới vụ O.J. Simpson để khép lại bài học so sánh luật của cả hai vụ án.
- Khi thiết kế tiêu đề/thumbnail: dùng "Casey Anthony" (người trưởng thành, đã bị xét xử công khai) làm danh xưng chính của tập, không dùng tên cháu bé.

### Production cautions

- **`DOMAIN_GUIDE.md` §6 (không có ngoại lệ, kể cả khi tên nạn nhân nổi tiếng toàn cầu):** tuyệt đối không nêu tên cháu bé ở bất kỳ đâu trong kịch bản — kể cả trong tiêu đề, mô tả video, thumbnail, hay khi trích dẫn nguồn. Chỉ dùng "con gái của Casey Anthony," "cháu bé," "nạn nhân nhỏ tuổi." Việc tên cháu đã trở thành một phần không thể tách rời của cách vụ án được biết đến trên truyền thông quốc tế **không phải là căn cứ để miễn trừ** quy tắc này.
- **Đây là ranh giới §4/§5 quan trọng nhất của mục này:** cáo buộc xâm hại tình dục nhắm vào George Anthony (cha của Casey Anthony, một người còn sống) do luật sư bào chữa đưa ra **phải luôn đi kèm khung "cáo buộc chưa chứng minh, bị chính ông phủ nhận, không có nhân chứng xác nhận"** mỗi khi được nhắc đến — không được trần thuật như sự thật đã xác lập theo bất kỳ chiều nào (không khẳng định đúng, cũng không cần thiết phải khẳng định sai — chỉ trình bày đúng như những gì hồ sơ thể hiện: một cáo buộc bị phủ nhận, chưa từng được chứng minh).
- **Net-impression test:** không được để tông giọng, cấu trúc, tiêu đề, hay nhịp kịch bản ngầm khẳng định "Casey Anthony đã giết con mình" — kể cả khi tường thuật lại niềm tin của dư luận Mỹ đương thời, phải luôn giữ rõ ràng đây là niềm tin công chúng, không phải kết luận pháp lý; bản án trắng án là sự kiện pháp lý duy nhất được xác lập.
- **Độ tin cậy cần lưu ý:** ngày bắt đầu chính xác của phiên tòa (một số nguồn tổng hợp ghi 24/5/2011) chưa được xác minh trực tiếp qua hồ sơ tòa án — mức tin cậy trung bình. Số liệu khảo sát dư luận Mỹ tin Casey Anthony có tội sau trắng án được nhiều nguồn nhắc đến định tính nhưng **chưa được xác minh trực tiếp qua nguồn khảo sát gốc** — không trích dẫn con số phần trăm cụ thể trong kịch bản trước khi xác minh thêm. Tình trạng còn sống/đã mất hiện tại của George Anthony **chưa được xác minh trực tiếp** trong nghiên cứu này — cần kiểm tra lại nếu kịch bản cần nêu tình trạng hiện tại của ông.
- **Khoảng trống nguồn:** không tìm thấy thông tin về việc có xảy ra giám đốc thẩm/tái thẩm hay bất kỳ thủ tục pháp lý nào khác sau phán quyết phúc thẩm 25/1/2013 — tạm coi đây là điểm kết thúc tố tụng cuối cùng đã biết, nhưng không khẳng định tuyệt đối không còn diễn biến nào khác.

---

# Ghi chú tổng hợp cho biên tập viên (carry-forward từ research draft)

1. Cả sáu vụ án đều đã có bản án/phán quyết cuối cùng, không còn kháng cáo/kháng nghị đang treo tại thời điểm nghiên cứu tương ứng (2026-07-23 cho bốn vụ đầu; 2026-07-24 cho hai vụ bổ sung) — đủ điều kiện Format 1 (`DOMAIN_GUIDE.md` §4a) để nêu tên người bị kết án, **ngoại trừ** hai trường hợp trắng án hình sự: O.J. Simpson (trắng án hình sự + chịu trách nhiệm dân sự — hai tầng phán quyết khác nhau) và Casey Anthony (trắng án hình sự đối với tội giết người, chỉ kết tội các tội danh khai báo gian dối nhẹ hơn) — cả hai đều phải luôn trình bày đúng trạng thái pháp lý thực tế, không gộp chung thành "có tội" (xem Production cautions của từng mục).
2. Ba vụ trong sáu vụ có nạn nhân vị thành niên cần ẩn danh theo §6 — packet này chủ động ẩn danh cả ba trường hợp và phải giữ nguyên nguyên tắc này ở mọi bản dựng kịch bản phát sinh từ packet, dù tên các nạn nhân đã từng được công khai trên báo chí hoặc đã trở thành danh xưng nổi tiếng toàn cầu: (a) vụ Lê Văn Luyện — hai nạn nhân vị thành niên; (b) vụ thảm sát Bình Phước — hai nạn nhân vị thành niên và một em bé sống sót; (c) vụ Casey Anthony — nạn nhân là một bé gái 2 tuổi, trường hợp khó ẩn danh nhất trong toàn bộ packet vì tên cháu đã trở thành một phần gắn liền với cách vụ án được biết đến quốc tế, nhưng quy tắc §6 vẫn áp dụng không có ngoại lệ.
3. Vụ Năm Cam có giá trị dùng kép cho Pillar 2 và Pillar 5 (tương lai `KP_CL_005`) — phần "cấu trúc tổ chức" trong mục Năm Cam ở trên **cố ý không đi sâu**; khi `KP_CL_005` được viết, đó mới là nơi triển khai đầy đủ mô hình vận hành/cấu trúc tổ chức, dưới khung QA riêng của §8.
4. Vụ Lê Văn Luyện có giá trị giáo dục pháp luật cao nhất (Pillar 1 chồng lấn) nhờ minh họa cụ thể về Điều 74 BLHS 1999 — nên khai thác như một case study độc lập khi xây Knowledge Packet Pillar 1 về tuổi chịu trách nhiệm hình sự.
5. Vụ O.J. Simpson là tài liệu so sánh luật tốt nhất trong sáu vụ nhưng cũng là vụ **dễ vi phạm §4 nhất** nếu biên tập không cẩn thận — rủi ro lớn nhất là kịch bản vô tình ngầm khẳng định "Simpson đã giết người" bằng cách trích câu phúc thẩm dân sự tách khỏi ngữ cảnh, hoặc bằng tông giọng/cấu trúc kịch bản (net-impression test). Không có nguồn nào trong nghiên cứu gốc cho thấy Simpson từng bị kết án hình sự.
6. Vụ thảm sát Bình Phước là ví dụ rõ nhất trong packet về nguyên tắc "đồng phạm không đồng nghĩa đồng mức trách nhiệm" — ba bị cáo (Nguyễn Hải Dương, Vũ Văn Tiến, Trần Đình Thoại) có ba vai trò và ba mức án khác nhau rõ rệt (tử hình – tử hình – 16 năm tù), tuyệt đối không được gộp chung thành "các hung thủ" trong bất kỳ kịch bản nào; đặc biệt vai trò hạn chế hơn của Trần Đình Thoại (rút lui, không trực tiếp giết người) phải luôn được giữ tách biệt để tránh vi phạm §4 net-impression test đối với riêng ông ta.
7. Vụ Casey Anthony là bài học đồng hành, đối lập chiều hướng với vụ O.J. Simpson — thay vì dư luận chia rẽ (Simpson), đây là trường hợp dư luận gần như đồng thuận tin có tội nhưng luật không kết tội; hai vụ nên được tham chiếu chéo lẫn nhau khi khai thác kịch bản. Vụ này còn chứa một cáo buộc xâm hại tình dục nhắm vào một người còn sống (George Anthony) do luật sư bào chữa đưa ra, chưa từng được chứng minh và bị chính người đó phủ nhận — rủi ro §4/§5 lớn nhất của vụ án này, luôn phải đi kèm khung "cáo buộc của bên bào chữa, bị phủ nhận, không có bằng chứng xác nhận."
8. Các điểm "độ tin cậy trung bình/single-sourced" cần xác minh thêm trước khi một kịch bản phát biểu như sự thật đã xác lập: (a) vai trò chi tiết của từng cán bộ tha hóa trong vụ Năm Cam; (b) ngày phúc thẩm chính xác trong vụ Lê Văn Luyện; (c) phân chia mức án cụ thể và ngày ra tù trước hạn của Đào Quang Khánh trong vụ Cát Tường; (d) câu trích dẫn nguyên văn của tòa phúc thẩm dân sự trong vụ Simpson; (e) cách viết tên đầy đủ của người vợ nạn nhân và tình trạng hiện tại của Trần Đình Thoại trong vụ Bình Phước; (f) ngày bắt đầu chính xác của phiên tòa và số liệu khảo sát dư luận cụ thể trong vụ Casey Anthony. Không có vụ nào trong sáu vụ có mâu thuẫn nghiêm trọng giữa các nguồn về sự kiện cốt lõi (bản án/phán quyết, mức án, ngày tháng chính) — các điểm nêu trên đều là chi tiết phụ.

---

## Packet Footer

| Field | Value |
|---|---|
| Asset ID | KP_CL_002 |
| Domain | CL (Hình Sự) |
| Dùng cho | Pillar 2 (Án Đã Xử/Phá Án) season episodes |
| Phụ thuộc | `DOMAIN_GUIDE.md` + `SOURCES/RESEARCH_DRAFT_AN_DA_XU.md` + `SOURCES/RESEARCH_DRAFT_AN_DA_XU_BATCH2.md` |
| Trạng thái | draft creative-knowledge asset — chưa qua QA chính thức |
