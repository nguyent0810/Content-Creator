# QA Report — KP_CL_003_Vu_An_Chua_Loi_Giai.md, Batch 2 Addition (Phần 4 "Boy in the Box" & Phần 5 "Tamam Shud")

**Reviewer:** Independent QA pass (fresh review, not the authoring context).
**Domain:** CRIMINAL_LAW (Hình Sự) — risk_level: critical.
**Files read in full:** `DOMAIN_GUIDE.md`, `SOURCES/RESEARCH_DRAFT_VU_AN_CHUA_LOI_GIAI_BATCH2.md`, `KNOWLEDGE_PACKETS/KP_CL_003_Vu_An_Chua_Loi_Giai.md` (entire file, all 307 lines — Phần 1-3 skimmed for unintended edits, Phần 4-5 read closely), `DOMAIN_QA/DOMAIN_QA_POLICY.md`, `GLOSSARY/DOMAIN_GLOSSARY.md`, `SOURCES/SOURCE_REGISTRY.md`, prior `_QA_REPORT_KP_CL_003.md`.

**Verdict: CONDITIONAL PASS.** No blocking issue found inside `KP_CL_003_Vu_An_Chua_Loi_Giai.md` itself — the batch-2 addition (Phần 4-5) is compliant. One blocking-adjacent issue *was* found in a related file (`SOURCE_REGISTRY.md`) and fixed. One advisory (non-blocking) gap noted. The open §6 historical-minor-carve-out policy question is correctly surfaced, not resolved — confirmed working as designed.

---

## (a) Task items — verified

### 1. Boy in the Box (Phần 4)

- **Name search:** grepped the entire `KP_CL_003_Vu_An_Chua_Loi_Giai.md` file (all 307 lines) for `Zarelli`, `Joseph Augustus`, `Joseph Zarelli` (case-insensitive). **Zero matches.** The victim is described only as "một bé trai khoảng 4 tuổi" / "đứa trẻ được đặt tên tạm là 'America's Unknown Child'" throughout, including in the 8/12/2022 identification announcement paragraph, the 2024 headstone-replacement note, and every cross-reference. PASS.
- **"Identifying the victim did NOT solve the murder":** stated explicitly and repeatedly — heading "Tình trạng vụ án" analog in Primary concepts (line 188: "danh tính nạn nhân đã xác định, nhưng danh tính kẻ đã sát hại đứa trẻ VẪN CHƯA ĐƯỢC XÁC ĐỊNH — hồ sơ giết người vẫn đang mở"), Knowledge function intro (line 179), Narrative detail closing line (line 193, quoting Capt. Jason Smith), Script-ready material hook ("65 năm để trả lời một nửa câu hỏi," line 197), and Production cautions (line 211, explicit ban on "vụ án đã được giải" framing, explicit Pillar-3-not-Pillar-2 placement rationale). PASS.
- **Open policy question surfaced, not resolved:** Production cautions contains a dedicated, clearly-labeled block (line 210: "VẤN ĐỀ CHÍNH SÁCH ĐANG BỎ NGỎ (flagged, chưa được giải quyết — KHÔNG được tự ý quyết định bởi bất kỳ agent hay QA đơn lẻ nào)") that lays out the §6 historical-minor-carve-out question, both sides of the argument, ties it explicitly to the Zodiac precedent and to `_QA_REPORT_KP_CL_003.md` item (d), and states the default (no naming) is only a recommendation pending a domain-owner decision — not a silent resolution either way. Same framing repeated in the batch-2 editors' summary note (line 287) and the Packet Control "Review cadence" row (line 306). This QA pass also does not resolve it — consistent with the required posture. PASS.

### 2. Tamam Shud (Phần 5)

- **Carl Webb naming:** correctly treated as an adult (born 1905, died 1948, age ~43) and named factually per the DNA identification, with an explicit note in Production cautions that this does *not* trip the minor-victim rule (line 266: "không vướng quy tắc minor-victim của §6 (ông là người trưởng thành tại thời điểm tử vong)"). PASS.
- **Cold War espionage theory labeling:** checked every occurrence ("Các giả thuyết" entry line 241, Production cautions line 265, packet-wide overarching-principle note lines 8-9, batch-2 editors' summary line 288). Every instance explicitly labels it "giả thuyết văn hóa đại chúng, không phải kết luận có bằng chứng" and states no official intelligence documentation from any country confirms it. Never asserted as fact anywhere. PASS.
- **Cause-of-death-still-debated-post-ID:** present as a dedicated subsection ("Tình trạng vụ án," lines 250-254), repeated in Knowledge function (line 226), Narrative detail closing (line 248), and Production cautions (line 267). Consistently hedged — no single cause (poisoning/suicide/natural) stated as fact. PASS.
- **Coroner-confirmation-pending flag carried into confidence notes:** confirmed carried through. Research draft's flag ("Cảnh sát Nam Úc / giám định viên pháp y bang (Coroner) VẪN CHƯA đưa ra xác nhận chính thức, công khai đầy đủ") appears in the KP's Primary concepts (line 235), Production cautions (line 266, with an explicit instruction to re-check status before publication), and the Nguồn tham khảo confidence footnote (line 273, "độ tin cậy TRUNG BÌNH về việc đây đã là một 'xác nhận tư pháp chính thức, khép lại hồ sơ'"). PASS.

### 3. Full CL-QA checklist (`DOMAIN_QA_POLICY.md`), applied to Phần 4-5

| Check | Result |
|---|---|
| CL-QA-001 (legal-status precision) | N/A — no living, not-finally-convicted named persons in either section (Boy in the Box has no named suspect at all; Carl Webb is deceased, not a criminal suspect). PASS. |
| CL-QA-002 (net-impression test) | Hooks explicitly reject "solved" framing for both cases (see 1/2 above); no sensational titling. PASS. |
| CL-QA-003 (source-backed identification) | Every named individual (Carl Webb, Dorothy Robertson, Derek Abbott, Colleen Fitzpatrick, Alfred Boxall, Jessica Thomson, William Fleisher, Danielle Outlaw, Jason Smith) traces directly to `RESEARCH_DRAFT_VU_AN_CHUA_LOI_GIAI_BATCH2.md`. No invented name, quote, or detail found on line-by-line comparison. PASS. |
| **CL-QA-004 (theory completeness)** | Boy in the Box: source record contains **zero** named suspect theories as of the research date — the KP correctly lists none and explicitly documents this as a deliberate, source-faithful exception (line 205) rather than an omission, consistent with §5's ban on inventing a theory. Tamam Shud: KP lists all 4 theories present in the research draft (Cold War espionage, Jessica Thomson identity theory — correctly marked superseded by the 2022 DNA result, suicide, Alfred Boxall) with no theory dropped or omitted to favor another. Meets the packet's own stated ≥3-theory minimum. PASS. |
| CL-QA-005 (victim privacy) | Boy in the Box victim redacted throughout (see item 1). Age-at-event independently checked (~4 years — minor) rather than trusting public-record naming, per the mandatory sub-check added 2026-07-23. **Related finding in `SOURCE_REGISTRY.md` — see (b) below.** |
| CL-QA-006 (no legal advice) | N/A — no viewer-directed advice in either section. PASS. |
| CL-QA-007 (organized crime) | N/A — not applicable to either case. PASS. |
| CL-QA-008 (anti-sensationalism) | Injury/discovery details (blunt-force trauma, malnutrition, bruising) are stated factually for case comprehension, not dramatized; Production cautions for Boy in the Box explicitly bans sensationalized scene reconstruction (line 214). No manufactured-shock titling. PASS. |
| CL-QA-009 (layered interpretation) | Both sections carry legal/procedural (jurisdiction, investigating agency, exhumation authorization), narrative (investigation timeline), and societal-reflective (PPD's resulting forensic-genealogy program; the "amateur claim vs. official confirmation" media-literacy lesson) layers. PASS. |
| CL-QA-010 (jurisdiction clarity) | Both sections name jurisdiction and legal system before any procedural claim (Philadelphia/Pennsylvania/US common law; Adelaide/South Australia/Australian common law). PASS. |
| CL-QA-011 (terminology consistency) | **Advisory gap found, not blocking — see (c) below.** Several terms introduced by this batch (giám định gen phả hệ pháp y / forensic investigative genetic genealogy, GEDmatch, coroner, khai quật in the forensic-exhumation sense) are used extensively in the KP but are not yet in `GLOSSARY/DOMAIN_GLOSSARY.md`, contrary to §11's "add new terms to the glossary before using them" workflow. |
| CL-QA-012 (forbidden claims) | Checked against §12's list — no premature-guilt statement (no suspect named for Boy in the Box at all; Webb is not accused of a crime), no legal advice, no operational crime detail, no minor identified, no leading theory presented as settled, no manufactured shock, no glamorization. PASS. |

### Unintended edits to Phần 1-3 (Ripper, Zodiac, Cooper)

Read in full and compared against the prior `_QA_REPORT_KP_CL_003.md`'s documented "before/after" fix for the Zodiac minor-victim redaction. The current file text matches that report's "After" text exactly (line 81 of the KP). No other differences, additions, or removals detected in Phần 1-3 relative to what the prior QA pass describes. PASS — no unintended edits.

---

## (b) Blocking-adjacent issue found and fixed (outside the KP file, but directly on-point)

**Location:** `DOMAINS/CRIMINAL_LAW/SOURCES/SOURCE_REGISTRY.md`, batch-2 research-draft entry (row for `RESEARCH_DRAFT_VU_AN_CHUA_LOI_GIAI_BATCH2.md`).

**Issue:** the registry's own descriptive "Notes" column wrote the minor victim's identified name in plain text ("Boy in the Box: victim identified Dec 2022 (Joseph Augustus Zarelli)..."). This is inconsistent with this exact same file's established practice elsewhere for other minor victims — the Casey Anthony entry and the Lê Văn Luyện/Bình Phước entries both describe the naming situation ("named only once... flagged as requiring full anonymization," "deliberately not named... despite press coverage naming them") **without repeating the name itself**. Since `DOMAIN_GUIDE.md` §6 is exception-free and this domain's own QA policy added a mandatory age-verification sub-check specifically because minor-victim names had leaked through before (`DOMAIN_QA_POLICY.md` CL-QA-005), leaving the name written out in an internal tracking document creates exactly the copy-forward risk that rule exists to prevent (a future writer skimming the registry could lift the name into a script without re-deriving the policy question).

**Before:**
> Boy in the Box: victim identified Dec 2022 (Joseph Augustus Zarelli) but the killer remains unknown — case correctly stays in Pillar 3. **Explicit open policy question flagged (not resolved by the research):** whether §6's exception-free minor-victim rule should have a historical-case carve-out analogous to §4a's for perpetrators, since the victim's name is now major public record.

**After:**
> Boy in the Box: a minor (~4 years old at death) victim identified by name Dec 2022 via forensic genetic genealogy, but the killer remains unknown — case correctly stays in Pillar 3. Per §6's exception-free minor-victim rule, the identified name is deliberately not repeated in this registry entry, matching this file's own existing practice for other minor victims above (Casey Anthony, Lê Văn Luyện, Bình Phước). **Explicit open policy question flagged (not resolved by the research):** whether §6's exception-free minor-victim rule should have a historical-case carve-out analogous to §4a's for perpetrators, since the victim's name is now major public record.

Confirmed via domain-wide grep that after this fix, the only remaining occurrence of "Zarelli" anywhere under `DOMAINS/CRIMINAL_LAW/` is inside `SOURCES/RESEARCH_DRAFT_VU_AN_CHUA_LOI_GIAI_BATCH2.md` itself — where it appears only inside cited source article titles/URLs (unavoidable when citing real published journalism) and inside that draft's own explicit, clearly-labeled policy-question note. This matches the domain's established convention that raw, pre-QA research drafts may retain a name for source-traceability while every downstream QA'd asset (Knowledge Packet, Source Registry prose) must not.

---

## (c) Advisory (non-blocking) finding — not fixed, flagged for follow-up

**CL-QA-011 terminology gap:** `GLOSSARY/DOMAIN_GLOSSARY.md` does not yet define the forensic-genetic-genealogy vocabulary this batch introduces (giám định gen phả hệ pháp y, GEDmatch, SNP, coroner/giám định viên pháp y bang, khai quật in the forensic-exhumation sense). `DOMAIN_GUIDE.md` §11 asks for new terms to be added to the glossary before use. This is advisory-tier per `DOMAIN_QA_POLICY.md`'s severity table (does not block publication on its own) and was left untouched rather than edited unilaterally, since populating a glossary section is an editorial-scope decision better made deliberately rather than as a QA side-effect — flagging it here for the next glossary-maintenance pass.

---

## (d) Requires human judgment (confirmed still open, not resolved by this pass)

Same item already on record in `_QA_REPORT_KP_CL_003.md` (d), now also carried by Phần 4's Production cautions and the batch-2 editors' note: **whether `DOMAIN_GUIDE.md` §6 should gain a narrow, explicitly-scoped historical-minor carve-out** (mirroring §4a Format 1's allowance for historical/deceased perpetrators) for a case like Boy in the Box, where the minor victim's identity is now international, officially-announced, headstone-inscribed public record, and where the investigative journey to that identity — not the name itself — is the episode's narrative center. This QA pass deliberately did not resolve it, consistent with the domain's requirement that this be a channel-owner/domain-policy decision, not a QA reviewer's unilateral call. No further action taken beyond confirming the question is surfaced correctly and not silently pre-decided in either direction.
