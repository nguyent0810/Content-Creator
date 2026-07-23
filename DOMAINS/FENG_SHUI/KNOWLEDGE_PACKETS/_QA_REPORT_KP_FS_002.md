# QA Report — KP_FS_002_Tu_Vi.md (Independent Review)

| Field | Value |
|---|---|
| Reviewed asset | `DOMAINS/FENG_SHUI/KNOWLEDGE_PACKETS/KP_FS_002_Tu_Vi.md` (v1.0, status draft-pending-human-review) |
| Reviewer role | Independent QA (per `DOMAIN_QA_POLICY.md` "Process" — did not author the packet) |
| Reviewed against | `DOMAIN_GUIDE.md` (full, esp. §4, §8), `DOMAIN_QA/DOMAIN_QA_POLICY.md` (FS-QA-001–010), `GLOSSARY/DOMAIN_GLOSSARY.md`, `SOURCES/RESEARCH_DRAFT_AM_DUONG_NGU_HANH.md`, `RESEARCH_DRAFT_THIEN_CAN_DIA_CHI_12_CUNG.md`, `RESEARCH_DRAFT_14_CHINH_TINH_LICH_SU.md`, `SOURCES/SOURCE_REGISTRY.md` |
| Review date | 2026-07-23 |
| Verdict | **PASS** — no blocking issues found. This is the first independent scrutiny this packet has received; it holds up under adversarial reading. |
| Blocking issues found/fixed | 0 found, 0 fixes required |
| Items requiring human judgment | 2 (see section (d)) — neither is a claim-type violation, both are pre-existing "pending human review" gates already flagged by the packet's own status |

---

## (a) Checklist items that passed

**FS-QA-001 (source attribution, §2-3)** — PASS. Every specific factual claim in the packet either (i) is flagged as cross-school/cross-source consensus (the two Ngũ Hành cycles, Thiên Can/Địa Chi tables, 12 Cung names, 14 star names/groupings), or (ii) explicitly names which source(s) it comes from and flags disagreement (5-star Ngũ Hành variance, Cục numbering, Cụ Thiên Lương's name/birth year, Vân Đằng Thái Thứ Lang's monastic-background claim, the Hoàng Bính 1257 story). No claim is silently presented as universal when the underlying research drafts show disagreement.

**FS-QA-002 (no individualized reading, §4/§4a)** — PASS. The packet contains **zero instantiated example charts** — every place a worked example would appear (chart construction, Cung Mệnh calculation, a specific Cung's meaning), the packet explicitly defers to "a future, dedicated packet" or specifies the *rule* an example must follow (fictional/long-deceased figure, explicit on-screen "LÁ SỐ MINH HỌA — NHÂN VẬT HƯ CẤU" label, no birth data resembling a real viewer's own) rather than performing one itself. Checked specifically for "hãy tính lá số của bạn"-style framing — none found; the only second-person ("bạn") usages in the file are inside explicit prohibitions ("Do not use 'bạn sẽ...'", "never invite... 'tính giờ sinh của bạn'").

**FS-QA-006 / §8 (Cung Tật Ách, lifespan)** — PASS, and notably stricter than the minimum bar. The packet's "Lifespan & Serious-Event Prediction Rule" section bans the pattern "nhân vật X có Cung Tật Ách xấu nên mất năm Y tuổi Z" **even for admittedly fictional characters**, correctly reasoning that the narrative *shape* teaches self-application regardless of whether the subject is real (this is a correct, non-watered-down reading of §8 — it does not just repeat the Guide, it closes a gap the Guide's literal text leaves open for fictional subjects). Cung Tật Ách is called out at every layer it appears (Identity's Related Terms, the 12-Cung table, the Risk-Specific Editorial Rules section) with consistent "no specific illness/timing" framing.

**Historical attribution consistency (Trần Đoàn / 1581 / Lã Động Tân)** — PASS. Cross-checked every mention against the source draft's three-tier framework:
- Trần Đoàn is consistently called "traditional lore," "popular/traditional attribution," "semi-legendary," never asserted as founder-in-fact. The packet correctly separates the *verifiable* fact (a posthumous Ming-era preface attributes the work to him) from the *unverifiable* claim (that he actually wrote/founded it).
- The 1581 date is consistently used only as "earliest attested written use of the term," correctly framed as postdating Trần Đoàn's traditional lifetime by centuries — never used to imply an earlier confirmed founding date.
- The Lã Động Tân variant is correctly used as evidence of *plurality* of founding legends, not resolved in favor of either figure.
- The Hoàng Bính 1257 transmission-to-Vietnam story is correctly downgraded to "internet-circulated legend/lore... never presented as a confirmed historical event."

**5-star Ngũ Hành cross-school disagreement (§3)** — PASS. Thiên Cơ, Thiên Đồng, Thiên Tướng, Thất Sát, Thiên Lương are flagged identically in the Executive Summary, the 14-Chính-Tinh table's per-row "Variant note" column, and the table-level "Production caution." Matches `DOMAIN_GLOSSARY.md`'s identical five-star list and `SOURCE_REGISTRY.md`'s identical five-star list — no drift between the three documents. Tham Lang's separate dual-element issue is additionally and correctly flagged as a distinct (6th) variance, not folded into or confused with the "5."

**An sao (star placement) low-confidence flag (source registry gap)** — PASS. The "Cách lập lá số Tử Vi cơ bản" section is explicitly subtitled "(concept only — not a how-to)," states plainly that "detailed star-placement mechanics are explicitly out of scope for this packet... were not researched in sufficient depth to state as settled technique here," and its Production Cautions repeat "use conceptual language... rather than 'công thức chính xác là...'" This matches `SOURCE_REGISTRY.md`'s Known Gaps entry verbatim in substance.

**No personal-reading-format drift (§4, "hãy tính lá số của bạn")** — PASS. Searched the full file for second-person address, invitation-to-calculate phrasing, and "comment your result"-style hooks. Every instance found is a *prohibition* being stated, not an instance of the prohibited pattern.

**FS-QA-003 (certainty language, §5)** — PASS. All predictive/traditional-belief statements use "được xem là," "theo Tử Vi truyền thống," "thường," "một số cách luận truyền thống," etc. No "bạn sẽ..." or flat-assertion predictive language found anywhere in the packet's own voice.

**FS-QA-004 (financial boundary, §6)** — PASS. Cung Tài Bạch and Vũ Khúc content stays at the cultural/traditional-meaning level; explicit "never" on investment advice and "guaranteed wealth mechanism" framing.

**FS-QA-005 (health boundary, §7)** — PASS. Cung Tật Ách and Thiên Lương's "y dược/giải nạn" association are both kept at general-trait / cultural-belief level; no diagnosis, cure, or medical-substitution claim anywhere.

**FS-QA-007 (anti-fear-sales, §9)** — PASS. No urgency, threat, or purchase-linked framing anywhere in this structural/historical packet.

**FS-QA-009 (terminology consistency)** — PASS. Cross-checked every controlled term (Tử Vi Đẩu Số, Cung, Chính tinh/Phụ tinh, Mệnh, Thân, Tài Bạch, Tật Ách, Phúc Đức, Thiên Can, Địa Chi) against `DOMAIN_GLOSSARY.md` — consistent definitions, no invented terminology. (One structural note, not a terminology error, logged under (c) below.)

**FS-QA-010 (forbidden claims, §12)** — PASS. Grepped the file for certainty/proof language ("definitely," "guaranteed," "proven," "scientifically valid," etc.) — every match found is part of a prohibition ("do not claim X is proven"), not an instance of the claim itself.

---

## (b) Issues found

**No blocking issues were found.** This packet was already written with unusual discipline around the domain's two highest-risk boundaries (§4 and §8) — including a self-imposed rule (banning mortality-timing examples even for fictional characters) that is stricter than the Domain Guide's literal minimum. No FS-QA-002/004/005/006/007/010 violation was located anywhere in the file after a full, non-skimming read cross-referenced against all three source research drafts and the source registry.

Two **non-blocking (advisory)** observations, logged for completeness per FS-QA-008/001's advisory tier — neither required a §14 transform because neither is a locked-claim-type violation:

1. **FS-QA-008 (layered interpretation, advisory)** — The packet self-scopes as "structural and historical only" and defers the "modern-reflective layer" (§10's third layer) entirely to future scripts. This is a legitimate design choice for a foundational structural packet (it is not making any claim that erases the modern-reflective layer — it simply hasn't reached that layer yet), so it does not fail FS-QA-008 as written. Flagged only so that whichever script/Short is produced *from* this packet is reminded to add the modern-reflective layer itself, since the packet won't supply it.

2. **12-Cung listing direction vs. `DOMAIN_GLOSSARY.md`** — `KP_FS_002`'s 12-Cung table lists the ring starting Mệnh → Huynh Đệ → Phu Thê → Tử Tức → Tài Bạch → Tật Ách → Thiên Di → Nô Bộc → Quan Lộc → Điền Trạch → Phúc Đức → Phụ Mẫu, while `DOMAIN_GLOSSARY.md`'s prose lists Mệnh → Phụ Mẫu → Phúc Đức → Điền Trạch → Quan Lộc → Nô Bộc → Thiên Di → Tật Ách → Tài Bạch → Tử Tức → Phu Thê → Huynh Đệ — the exact reverse. Both are internally correct (the packet itself explains that clockwise/counter-clockwise listings from Cung Mệnh describe the identical ring, "not a school disagreement"), so this is not a factual error. It is only worth a note because a reader who consults the glossary and the packet back-to-back without registering that caveat could momentarily read it as a contradiction. No fix applied to either file; recommend whoever next edits `DOMAIN_GLOSSARY.md`'s Cung entry add a one-line pointer to the packet's ring-direction note.

---

## (c) Exact fixes applied

**None.** No blocking issue was found that required invoking `DOMAIN_GUIDE.md` §14's transform procedure. The packet did not need any claim rewritten, softened, or reframed — it was already compliant on every blocking checklist item (FS-QA-002, 004, 005, 006, 007, 010).

---

## (d) Anything unfixable requiring human judgment

Neither item below is a QA violation; both are pre-existing, already-disclosed research gaps that the packet itself flags as needing a **human**, not an editorial-transform, resolution — restating them here only because the task asked what remains outside this review's authority:

1. **Cụ Thiên Lương's real name and birth year, and Vân Đằng Thái Thứ Lang's monastic-background claim** remain genuinely unverified in the current source base (single-sourced / conflicting across secondary Vietnamese sites). This is not a compliance problem — the packet already hedges correctly — but it cannot be resolved by rewriting the packet; it requires a human researcher to locate a stronger primary/academic source (e.g., an original book preface, a documented interview) before these specific biographical facts could ever be stated as settled. Per the packet's own QA Status table, this is exactly why "Historical QA" is still marked Pending.

2. **The an sao (star-placement) computational detail** is a known, self-disclosed research gap (`SOURCE_REGISTRY.md` Known Gaps: "No single canonical Vietnamese-language reference text has been designated... exact an sao computation... remain lower-confidence until one is chosen"). This is not something a QA pass can fix by editing prose — it requires a human decision on which classical/canonical text to adopt as the project's reference edition before a dedicated star-placement packet can be written. The current packet correctly avoids the gap rather than papering over it, which is the right editorial choice until that human decision is made.

Both gaps were already known and disclosed by the packet's own authors (see its QA Status table: Historical QA and Domain QA both listed "Pending," Human Review listed "Required before... production use"). This review confirms those self-assessments are accurate and does not surface any additional undisclosed gap.

---

## Related Documents

- `DOMAINS/FENG_SHUI/KNOWLEDGE_PACKETS/KP_FS_002_Tu_Vi.md` — packet reviewed (unmodified by this pass).
- `DOMAINS/FENG_SHUI/DOMAIN_GUIDE.md`, `DOMAIN_QA/DOMAIN_QA_POLICY.md`, `GLOSSARY/DOMAIN_GLOSSARY.md`, `SOURCES/SOURCE_REGISTRY.md` — rules and registries this review checked against.
- `DOMAINS/FENG_SHUI/SOURCES/RESEARCH_DRAFT_AM_DUONG_NGU_HANH.md`, `RESEARCH_DRAFT_THIEN_CAN_DIA_CHI_12_CUNG.md`, `RESEARCH_DRAFT_14_CHINH_TINH_LICH_SU.md` — source drafts the packet is built from; cross-checked line-by-line against the packet's claims.
