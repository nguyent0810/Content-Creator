# QA Report — KP_CL_002_An_Da_Xu.md (Batch 2 additions: Vụ thảm sát Bình Phước, Casey Anthony)

**Reviewer:** Independent QA pass (fresh review, did not author the research draft or the packet additions)
**Date:** 2026-07-24
**Domain:** CRIMINAL_LAW (Hình Sự) — `risk_level: critical`
**Documents read in full before review:** `DOMAIN_GUIDE.md`, `DOMAIN_QA/DOMAIN_QA_POLICY.md`, `SOURCES/RESEARCH_DRAFT_AN_DA_XU_BATCH2.md`, `SOURCES/RESEARCH_DRAFT_AN_DA_XU.md` (original, for diffing the four pre-existing cases), `KNOWLEDGE_PACKETS/KP_CL_002_An_Da_Xu.md` (full current version, v0.2, all six cases), and the prior `_QA_REPORT_KP_CL_002.md` (2026-07-23 pass on the original four-case version, for continuity).

## Verdict: PASS — no blocking issues found

Reviewed with the requested adversarial posture, given this domain's documented history of 8 minor-victim-naming violations across the first content batch. Every claim in the two new sections was traced back to `RESEARCH_DRAFT_AN_DA_XU_BATCH2.md`; every sentence referencing a minor or the surviving infant was read individually, not skimmed; a full-text search of the entire packet file was run for "Caylee" and for any name-shaped string near the Bình Phước minors' descriptions. No fix was required or applied to the packet file.

---

## (a) CL-QA checklist — systematic pass on both new sections

| Check | Result | Evidence |
|---|---|---|
| CL-QA-001 (legal-status precision) | PASS | Bình Phước: all three defendants (Dương, Tiến, Thoại) correctly stated as finally convicted (`bản án đã có hiệu lực pháp luật, không còn kháng cáo/kháng nghị đang treo`), matching the research draft's explicit final-status conclusion. No hedged/accused language misapplied to any of the three (Format 1 correctly used). Casey Anthony: correctly stated as criminally acquitted on the murder counts and separately convicted on the lesser false-statement counts — never blended into a single "guilty" status. |
| CL-QA-002 (net-impression test) | PASS | Bình Phước: "Production cautions" and "Knowledge function" both explicitly instruct never to collapse the three defendants into "các hung thủ"/"bọn chúng," and the actual Primary Concepts/Narrative/Script-ready prose consistently names each defendant individually with his own role and sentence — verified line-by-line, not just the caution paragraph (see item 1 below). Casey Anthony: every statement of the public belief in her guilt is explicitly framed as public opinion, not legal conclusion; the acquittal is repeatedly stated as the only established legal fact (see item 2 below). |
| CL-QA-003 (Format 2/3) | N/A | Both new cases are Format 1 (finally adjudicated); no unsolved-case suspect-naming content. |
| CL-QA-004 (theory completeness) | N/A | Not an unsolved case. |
| CL-QA-005 (victim privacy/dignity + mandatory age-verification sub-check) | PASS | See items 1 and 2 below. Every named victim in both new sections was individually age-checked: Lê Văn Mỹ (48), his wife (42), Lê Thị Ánh Linh (22), the cousin/student victim (confirmed 18 via a dedicated article, adult) are all adults and named consistent with public record. The two minor deceased victims (~15, ~14) and the surviving infant (~18 months, now a living adult) are never named anywhere. Caylee Anthony is never named anywhere in the packet (full-text search returned zero matches for "Caylee"). |
| CL-QA-006 (no legal advice) | PASS | Both sections are descriptive/historical/comparative-law; no line instructs a viewer on their own legal situation. |
| CL-QA-007 (organized-crime non-glorification) | N/A | Neither case is organized-crime content. |
| CL-QA-008 (anti-sensationalism) | PASS | No manufactured-shock titles or countdown-of-horror framing. Forensic/procedural detail (e.g., duct tape found on the skull in the Casey Anthony case) is stated factually once, without sensory embellishment of the child's suffering — see advisory note in (d). |
| CL-QA-009 (layered interpretation intact) | PASS | Bình Phước carries legal (verdict/appeal detail), narrative (80-hour manhunt, "one crime scene, three fates"), and societal-reflective (differentiated culpability) layers. Casey Anthony carries legal (double jeopardy, burden of proof), narrative (the chloroform-search reversal at trial), and societal-reflective (public belief vs. legal standard) layers, plus the explicit O.J. Simpson cross-reference layer. |
| CL-QA-010 (jurisdiction clarity) | PASS | Casey Anthony's Primary Concepts opens with an explicit Florida/common-law/jury statement before any procedural claim, and "double jeopardy" is repeatedly flagged as a US legal concept, not equated with Vietnamese tố tụng. Bình Phước is covered by the packet-level statement (line ~71) that cases 1–3 and 5 occur under Vietnamese law. |
| CL-QA-011 (terminology consistency) | PASS | bị cáo, bản án có hiệu lực pháp luật, sơ thẩm/phúc thẩm, kháng cáo — used consistently with the glossary and with the four pre-existing cases' usage. |
| CL-QA-012 (forbidden claims, §12) | PASS | No living not-finally-convicted person is called a guilt-asserting noun; no minor victim named; no legal advice; no operational crime detail; no manufactured shock. |

---

## (b) Issues found / (c) fixes applied

**None. No blocking or non-blocking textual violation was found requiring a fix to the packet file.**

Detail on the three specifically-assigned focus areas:

### 1. Bình Phước — three defendants never collapsed; no minor named

- Read every paragraph across Knowledge function, Primary concepts, Narrative detail, Script-ready material, and Production cautions (5 subsections) for the Bình Phước case. In every single instance, Nguyễn Hải Dương, Vũ Văn Tiến, and Trần Đình Thoại are referred to by name with their individually differentiated roles (chủ mưu/trực tiếp thực hiện; đồng phạm trực tiếp có mặt tại hiện trường; rút lui/không có mặt). The only appearances of the string "hung thủ" in this section are (a) inside the explicit prohibition against using it as a collective label, and (b) one instance ("một trong hai hung thủ đã không ra tay với em") that correctly refers only to the two defendants who were physically present at the scene (Dương, Tiến) — consistent with the research draft's own framing that Thoại had already withdrawn and was not present. This is an accurate use, not a collapsing violation.
- Full-text search for "Caylee" returned no matches (irrelevant to this case but confirms no cross-contamination). Read every sentence describing the two deceased minors and the surviving infant: all three are described only as "con trai út của ông Mỹ (khoảng 15 tuổi)," "một cháu trai họ hàng (khoảng 14 tuổi...)," and "một em bé khoảng 18 tháng tuổi" — role/age only, no first name, surname, initial, school, or other identifying detail, anywhere in the file (Primary concepts, Narrative detail, Script-ready material, Production cautions, and both editor's-summary sections at the top and bottom of the packet).
- Legal-status language verified: the packet states "cả ba bị cáo đều có bản án đã có hiệu lực pháp luật, không còn kháng cáo/kháng nghị đang treo" — this matches the research draft's conclusion exactly (Dương: final via non-appeal; Tiến and Thoại: final via the 18/7/2016 appellate ruling). Format 1 eligibility is explicitly and correctly stated for all three individually.

**No violation found. No fix needed.**

### 2. Casey Anthony — no victim name; sexual-abuse allegation properly hedged; O.J. Simpson cross-reference present and accurate

- Full-text search of the entire packet file for "Caylee" returned **zero matches**. Every reference to the victim uses "con gái của Casey Anthony," "cháu bé," or "nạn nhân nhỏ tuổi," including in the Script-ready material's explicit thumbnail/title guidance ("dùng 'Casey Anthony'... không dùng tên cháu bé"). Note: the *research draft* (a separate, non-production, internally-flagged document) deliberately names the victim exactly once for source-identification purposes with an explicit editorial flag that the name must never carry forward — the packet correctly honored that flag and did not carry the name forward anywhere.
- The sexual-abuse allegation against George Anthony (a living person) is hedged identically in all three places it appears (Primary concepts, Narrative detail, Production cautions): always framed as "một tuyên bố chưa được chứng minh của bên bào chữa, bị chính người bị cáo buộc phủ nhận, không có bằng chứng/nhân chứng xác nhận," never stated as settled fact in either direction. This matches `DOMAIN_GUIDE.md` §4/§5 exactly.
- The O.J. Simpson cross-reference is present in the Knowledge function ("đây là vụ án đối lập trực tiếp — và là bài học đồng hành bắt buộc tham chiếu — với vụ O.J. Simpson"), correctly stated as the inverse lesson (Simpson: divided public opinion; Casey Anthony: near-unanimous public belief in guilt despite acquittal), and reinforced again in Script-ready material and the editor's closing notes (item 7). The comparison is factually accurate to both sections' own content and does not conflate the two cases' distinct legal postures (Simpson: acquittal + separate civil liability; Anthony: acquittal + no civil companion verdict).

**No violation found. No fix needed.**

### 3. Existing four cases (Năm Cam, Lê Văn Luyện, Cát Tường, O.J. Simpson) — checked for silent alteration

Diffed every fact, date, sentence figure, and legal-status claim in the current v0.2 packet against the original `RESEARCH_DRAFT_AN_DA_XU.md` and the prior (2026-07-23) clean QA pass. No alteration found: all dates (25/2–5/6/2003, 15/9–30/10/2003, 3/6/2004; 24/8/2011, 18 năm tù; 19/10/2013, 5/12/2014, 19 năm tù/33 tháng; 24/1/1995, 3/10/1995, 33,5 triệu USD, 10/4/2024) and all legal-status conclusions match the original draft and the previously-passed packet content verbatim in substance. The Lê Văn Luyện and Cát Tường minor/adult-victim naming discipline is unchanged from the prior clean pass.

---

## (d) Anything unfixable / requiring human judgment (not blocking)

1. **Forensic detail in the Casey Anthony section** ("hộp sọ được tìm thấy có băng dính quanh vùng mũi/miệng/hàm") is factual and load-bearing for the prosecution's asphyxiation theory, stated once without sensory embellishment of the child's suffering — it passes §6/§9 as written, but a human editor adapting this into a script should keep it exactly this clinical rather than expanding it into a dramatized moment-by-moment reconstruction.
2. **The 18-year-old cousin/student victim in Bình Phước** is treated as an adult (nameable under §6) based on one dedicated article directly confirming age 18, despite a birth-year discrepancy noted in the confidence notes (1997 vs. "18 tuổi"). The packet does not actually name her (no name was available in the source research either), so this is moot for the naming rule, but if a future script wants to state her age as a specific fact, the birth-year discrepancy should be resolved against a primary source first — flagging per the research draft's own confidence label, not a new finding.
3. **The phrase "một trong hai hung thủ"** (referring to Dương/Tiến only, excluding Thoại) is accurate as used, but is a phrase future scriptwriters could carelessly widen to "the killers" in a way that would drag Thoại back into the undifferentiated group the packet works hard to keep him out of. Recommend any downstream script preserve the "two, not three" scope explicitly if this detail is used.
4. This QA pass reviewed the Knowledge Packet only, not a produced script. Per the packet's own status field, full Domain QA / Research QA / Safety QA / Legal-accuracy QA / Brand QA is still required before any script derived from this packet is published — this report satisfies the Domain QA (Hình Sự) pass for the Batch 2 additions specifically.

---

## Explicit confirmation (per task requirement)

- **"Caylee" / any name for Casey Anthony's daughter:** does not appear anywhere in `KP_CL_002_An_Da_Xu.md`. Confirmed via full-text search (zero matches) and full manual read of the Casey Anthony section.
- **Bình Phước's two minor victims (~15, ~14) and the surviving infant (~18 months, now a living adult):** none of the three is named anywhere in the file. Only family role and estimated age are used, consistently, in every subsection.
- **Bình Phước's three defendants:** never collapsed into an undifferentiated "the killers" in any paragraph; each is named individually with his own role and sentence throughout.
