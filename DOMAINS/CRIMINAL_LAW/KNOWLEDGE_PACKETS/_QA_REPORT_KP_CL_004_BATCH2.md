# QA Report — KP_CL_004 Batch 2 (Dennis Rader/BTK, Aileen Wuornos)

Status: **Independent QA pass complete, 2026-07-24.** Reviewer did not author the batch 2 additions being reviewed (BTK and Wuornos profiles, added to `KP_CL_004_Chan_Dung_Sat_Nhan.md` version 0.3). This report documents the review of both new sections against `DOMAIN_GUIDE.md`, `DOMAIN_QA/DOMAIN_QA_POLICY.md`, and independent fact-checking (WebSearch), given this file's history of six prior minor-victim-naming violations across two earlier QA passes.

**Verdict: PASS with one blocking fix applied (Missouri cold-case claim, stale/inaccurate) and two minor advisory fixes applied (age-precision hedges). No minor-victim-naming violation found in either new section.**

---

## 1. Checklist Results (`DOMAIN_QA_POLICY.md`)

| Check ID | Result | Notes |
|---|---|---|
| CL-QA-001 (legal-status precision) | PASS | Rader's 10 convictions correctly stated as final/chung thẩm. Oklahoma (Kinney/Pawhuska) case correctly uses "nghi phạm hàng đầu... chưa bị truy tố." Wuornos's 6 convictions correctly stated as final; Siems correctly distinguished as "thừa nhận, không truy tố" rather than a 7th conviction. |
| CL-QA-002 (net-impression test) | PASS after fix | Floppy-disk hook and "cái tôi tự phá hủy" framing avoid implying investigative genius. **Before fix:** pairing the hedged-but-live Oklahoma theory with a second, unqualified "also named as suspect in Missouri" claim risked a net impression that Rader remains under live suspicion in two open matters, when one had in fact been publicly closed with a different perpetrator — see §2 below. Fixed. |
| CL-QA-003 (source-backed identification) | PASS | Oklahoma suspicion traces to Osage County Sheriff's Office public statements (tier 2-3, correctly labeled). |
| CL-QA-004 (theory completeness) | PASS after fix | The Missouri claim's removal is itself a theory-completeness fix — an update that supersedes the original claim was available and had been missed. |
| CL-QA-005 (victim privacy — minor-naming sub-check) | **PASS, independently re-verified** | See §3 below for the full victim-by-victim verification log. No minor victim named in either new section. |
| CL-QA-006 (no legal advice) | PASS | N/A, no legal-advice content in either section. |
| CL-QA-007 (non-glorification) | PASS | BTK: framed as forensic-science/ego-self-destruction, not "criminal genius." Wuornos: dual-rejection rule (reject both tabloid "monster" framing and romanticized "avenger" framing) is explicit, not merely implied — see §4 below. |
| CL-QA-008 (anti-sensationalism) | PASS | No gore, no countdown framing. Wuornos's abuse/sex-work history is framed as social context, not titillation. *Monster* (2003) is explicitly flagged as a non-source, part of the sensationalization the packet critiques. |
| CL-QA-009 (layered interpretation) | PASS | Both profiles carry legal/narrative/societal-reflective layers (digital forensics for Rader; sex-worker legal-protection gap + childhood institutional failure for Wuornos). |
| CL-QA-010 (jurisdiction clarity) | PASS | Kansas (guilty plea, no full jury trial) explicitly distinguished from Florida (full jury trial) and from the other four profiles' jurisdictions. |
| CL-QA-011 (terminology consistency) | PASS after minor fix | Shirley Vian's age had a small precision issue (see §5). |
| CL-QA-012 (forbidden claims) | PASS | No item from §12's list found. |

---

## 2. BLOCKING issue found and fixed: stale Missouri cold-case claim (Rader)

**What was wrong:** The batch 2 research draft (`RESEARCH_DRAFT_CHAN_DUNG_SAT_NHAN_BATCH2.md`, research date stated as 2026-07-24) and the resulting KP section both stated that Rader was "also named as a suspect" in the 1990 murder of a woman in McDonald County, Missouri, presented as an open, unresolved theory alongside the Oklahoma (Kinney/Pawhuska) suspicion.

Independent verification (WebSearch, this QA pass) found that this Missouri case — the 1990 murder of Shawna Beth Garber, 22 — was **publicly announced as solved by the McDonald County Sheriff's Office on 2024-03-21**, naming a different, since-deceased suspect (Talfie/Talfey Reeves, d. 2021). This resolution predates the batch 2 research draft's stated research date by more than two years. The research draft's claim that this is a live, unresolved theory connecting Rader to a Missouri murder is therefore factually stale and, left uncorrected, creates exactly the net-impression risk `DOMAIN_GUIDE.md` §4 is designed to prevent: implying continued suspicion of a named, identifiable person in a matter that has, in fact, been publicly resolved with someone else.

**Why this is blocking:** Even though Rader is a finally-convicted, deceased-adjacent (still living but non-appealable) perpetrator for the 10 Kansas murders, this specific Missouri claim was an *unresolved-suspicion* claim under §4a Format 2 — and Format 2 requires presenting "one theory among the theories the sourced record actually contains," not a claim the current record has already superseded. Continuing to associate Rader's name with a since-solved case (without noting the resolution) fails CL-QA-002 (net-impression) and the theory-completeness discipline of CL-QA-004.

**Fix applied (transform, not deletion of the whole beat):** Per `DOMAIN_GUIDE.md` §14, the Oklahoma/Kinney theory (still genuinely open and hedged) was preserved unchanged. The Missouri claim was removed from the active claim set and replaced with an explicit correction note explaining *why* it was removed (the case was solved with a different, named suspect on 2024-03-21), in three places:
1. Profile #5 "Primary concepts" (BTK section, Oklahoma bullet).
2. "Ghi chú tổng hợp cho biên tập viên," item 1.
3. "Nguồn & độ tin cậy" for the Rader profile.
4. Packet Control table (Trạng thái + Version bumped to 0.4 with changelog entry).

This keeps the hook (forensic/cold-case material generally, and the still-open Oklahoma theory specifically) while removing the one claim that had gone stale. **Recommendation for editors:** apply the same correction to `SOURCES/RESEARCH_DRAFT_CHAN_DUNG_SAT_NHAN_BATCH2.md` itself, since it is the upstream source and will otherwise re-introduce this claim if the KP is regenerated from it.

---

## 3. Victim-by-victim independent age verification (CL-QA-005 sub-check)

Per the mandatory sub-check added 2026-07-23 (do not trust that public naming implies adulthood), every named or age-cited victim in both new sections was independently checked against external sources this session, not just cross-referenced against the research draft's own citations.

**BTK / Dennis Rader section:**
- **Otero children (the specific focus of this task):** independently confirmed via WebSearch that the two Otero children killed 1974-01-15 were **Joseph Otero II, age 9** (son) and **Josephine "Josie" Otero, age 11** (daughter) — both minors. **Confirmed neither name appears anywhere in the BTK section of the KP file** (checked via full-text grep for "Otero," "Josephine," "Joseph Jr/II," "Joey," "Josie" across the file — the only "Joseph"-adjacent name in the file is the unrelated adult Sutcliffe victim "Josephine Whittaker," 19). Both Otero children are described only by age and family role, consistent with §6's no-exception minor rule.
- **Oklahoma/Osage County case victim:** independently confirmed her real identity is **Cynthia Dawn Kinney, 16** (missing 1976, Pawhuska) — a minor. Confirmed she is not named anywhere in the KP; described only as "một thiếu nữ 16 tuổi." Correctly anonymized and correctly hedged as unproven/theory-only, consistent with §4a Format 2 + §6's double-risk framing the research draft itself flagged.
- **Adult named victims (spot-verified):** Joseph Otero (38), Julie Otero (33), Kathryn Bright (21), Nancy Fox (25), Marine Hedge (53), Vicki Wegerle (28), Dolores Davis (62-63, already hedged in packet) — all independently confirmed adult. **Shirley Vian**: packet stated 26; independent check found sources split 24/26, and date-of-birth arithmetic (b. 1951-11-22, d. 1977-03) yields ~25 — corrected to a hedged "khoảng 25 tuổi" (minor, non-blocking factual-precision fix; she is unambiguously an adult under any of the cited ages, so this was not a §6 risk, only an accuracy nicety).

**Aileen Wuornos section:**
- Independently re-verified the two victims closest to a boundary case, as instructed: **Charles Carskaddon confirmed 40** and **David Spears confirmed 43** — both clearly adult, matching the packet. No indication either was a minor.
- Richard Mallory (51), Troy Burress (50), Charles Humphreys (56), Walter Antonio (60, packet already hedges vs. a 62 variant), Peter Siems (65) — consistent with the research draft and with general source agreement found during this pass; no minor-age red flags on any of the seven.
- **Conclusion: no minor victim in the Wuornos profile.** This matches the research draft's own claim, and this QA pass independently corroborates it rather than merely accepting it.

---

## 4. Wuornos dual-framing-rejection rule — verified explicit, not merely implied

Confirmed present, verbatim in substance, in at least four locations in the KP's Wuornos section:
- Knowledge function: "không rút gọn thành khuôn mẫu 'nữ quái vật' giật gân kiểu tabloid — **và cũng không lật ngược thành khuôn mẫu lãng mạn hóa 'nữ anh hùng trả thù'**... đây là quy tắc dual-rejection bắt buộc."
- Script-ready material: repeats the dual-rejection instruction explicitly.
- Production cautions: "không đóng khung Wuornos như 'quái vật nữ giết đàn ông'... **và cũng không đóng khung bà như 'nữ anh hùng trả thù cho phụ nữ bị hại'**."
- "Ghi chú tổng hợp," item 4: repeats the rule again, applied specifically (and only) to Wuornos among the six profiles.

*Monster* (2003, dir. Patty Jenkins) is named explicitly and multiple times as a **non-source** — a cultural artifact to critique, not a factual reference — consistent with the task's requirement. This satisfies CL-QA-008/§9 and the dual-rejection instruction; no fix needed here.

---

## 5. Self-defense claim — verified honestly complex, not exculpatory

Confirmed the packet does not oversimplify in either direction:
- States plainly that only the Mallory case went to full trial; the other 5 were guilty/no-contest pleas.
- States the Mallory prior conviction (assault with intent to rape, Maryland) was excluded from trial due to defense-counsel failure, sourced to the actual Florida Supreme Court appellate opinion (*Wuornos v. State* — a tier-1 primary source, correctly flagged as such).
- Explicitly instructs: "không tường thuật một cách đơn giản hóa rằng 'tự vệ' là lời bào chữa hoàn toàn giả tạo bị bác bỏ tuyệt đối... nhưng cũng không trình bày như thể tòa án sai hay bản án không có căn cứ" — holding both truths (a real self-defense complexity for Mallory specifically; a final, unweakened conviction on all 6 counts) without excusing the convictions. This is correct and requires no fix.

---

## 6. Floppy-disk capture story — verified factually accurate, non-glorifying

Independently checked against multiple sources (LegalClarity, Refinery29, NBC News, Lawrence Journal-World) this session:
- Purple 1.44MB Memorex floppy disk sent to KSAS-TV: confirmed.
- Deleted, recovered Microsoft Word file, metadata showing last-saved-by "Dennis" and organization "Christ Lutheran Church": confirmed.
- Simple search identifying Rader as church council president: confirmed.
- DNA corroboration via a subpoenaed medical sample linked to Rader's daughter: confirmed.
- Arrest date 2005-02-25: confirmed.
- Minor imprecision: packet says "khoảng 10 ngày" from disk receipt to arrest; independently verified figure is 9 days (disk received ~Feb 16, arrest Feb 25). "Khoảng 10 ngày" is a reasonable rounding, not a factual error — left as-is but flagged in the sources note added during this pass for future precision.
- Framing check: the packet explicitly instructs against a "31 years of criminal genius" framing and instead frames the capture as Rader's own ego (wanting recognition, contacting media again, trusting police's misleading answer about disk traceability) causing his downfall — this satisfies §8 non-glorification. No fix needed.

---

## 7. Items needing human judgment / follow-up (not blocking, flagged for editorial awareness)

1. **Upstream source correction recommended:** `SOURCES/RESEARCH_DRAFT_CHAN_DUNG_SAT_NHAN_BATCH2.md` still contains the stale Missouri/Garber claim (uncorrected, since research drafts are treated as source-of-record inputs rather than edited by this QA pass). If this KP is ever regenerated from that research draft, the stale claim will reappear unless the draft itself is annotated or corrected. Recommend a follow-up edit to the research draft or, at minimum, a standing note in the packet's dependency section pointing to this report.
2. **Oklahoma/Kinney case still needs a production-time status re-check**, as the packet already itself flags (§4a Format 2, cold case in flux) — this QA pass did not find a resolution as of the search date, but by the time any script is produced from this packet, the case's status should be re-verified again, since cold cases connected to Rader appear to be actively moving (as evidenced by the Missouri case's own 2024 resolution, which the original research missed).
3. **Shirley Vian's age hedge** is a cosmetic accuracy fix, not a risk fix — flagging only so future edits don't silently revert it to an unhedged "26 tuổi."

---

## 8. Summary

- No minor-victim-naming violation found in either new section (BTK/Otero+Kinney, Wuornos) — the file's prior six-violation history was not repeated.
- One blocking-adjacent factual/net-impression issue found and fixed: a stale "Rader also suspected in a Missouri 1990 murder" claim, superseded by a 2024-03-21 public resolution naming a different suspect. Fixed directly in `KP_CL_004_Chan_Dung_Sat_Nhan.md` (profile #5, editor's synthesis notes, sources note, and Packet Control/version log), preserving the still-valid Oklahoma/Kinney theory unchanged.
- Two minor, non-blocking accuracy hedges applied (Shirley Vian's age; floppy-disk-to-arrest timeline note).
- Wuornos dual-framing-rejection rule and self-defense complexity are both explicitly, not just implicitly, present and required no fix.
- Victim ages independently re-verified this session: Joseph Otero II (9) and Josephine Otero (11) — confirmed minors, confirmed unnamed in the KP; Cynthia Dawn Kinney (16) — confirmed minor, confirmed unnamed; Joseph Otero (38), Julie Otero (33), Kathryn Bright (21), Shirley Vian (~25), Nancy Fox (25), Marine Hedge (53), Vicki Wegerle (28), Dolores Davis (62-63) — confirmed adults; Charles Carskaddon (40) and David Spears (43) — confirmed adults (the two Wuornos victims closest to a boundary case, per task instruction); Richard Mallory (51), Troy Burress (50), Charles Humphreys (56), Walter Antonio (60/62), Peter Siems (65) — confirmed adults, no minor-age red flags.

---

## Report Control

| Field | Value |
|---|---|
| Asset ID | _QA_REPORT_KP_CL_004_BATCH2 |
| Reviews | `KNOWLEDGE_PACKETS/KP_CL_004_Chan_Dung_Sat_Nhan.md` (batch 2 additions: profiles #5 Dennis Rader/BTK, #6 Aileen Wuornos) |
| Reviewer | Independent QA pass (did not author the reviewed content) |
| Review date | 2026-07-24 |
| Verdict | PASS with one blocking fix applied (stale Missouri claim, Rader) and two minor advisory fixes (age-precision hedges) |
| Fixes applied in | `KP_CL_004_Chan_Dung_Sat_Nhan.md`, bumped to Version 0.4 |
| Outstanding follow-up | Correct/annotate `SOURCES/RESEARCH_DRAFT_CHAN_DUNG_SAT_NHAN_BATCH2.md` upstream; re-verify Oklahoma/Kinney case status again before any production use |
