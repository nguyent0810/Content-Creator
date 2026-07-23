# QA Report — KP_CL_003_Vu_An_Chua_Loi_Giai.md

**Reviewer:** Independent QA pass (fresh review, not the authoring context).
**Domain:** CRIMINAL_LAW (Hình Sự) — risk_level: critical.
**Files read in full:** `DOMAIN_GUIDE.md`, `DOMAIN_QA/DOMAIN_QA_POLICY.md`, `KNOWLEDGE_PACKETS/KP_CL_003_Vu_An_Chua_Loi_Giai.md`, `SOURCES/RESEARCH_DRAFT_VU_AN_CHUA_LOI_GIAI.md`.
**Verdict: CONDITIONAL PASS.** One blocking issue found and fixed directly in the file (CL-QA-005, minor-victim naming). No other blocking issues found across the five specifically-requested checks or the full 12-point checklist. One item is flagged for domain-owner/human policy judgment rather than unilaterally resolved further (see part d).

---

## (a) Checklist items that passed

Verified against every suspect mention in all three cases (Jack the Ripper: 7 named suspects; Zodiac: 5; D.B. Cooper: 6 — 18 total) and cross-checked each claim against `RESEARCH_DRAFT_VU_AN_CHUA_LOI_GIAI.md` line by line.

1. **Suspect theory-hedging (task item 1).** Every one of the 18 named suspects across all three cases uses correct hedge language ("một giả thuyết cho rằng...", "chưa từng bị truy tố/buộc tội...", "giới nghiên cứu hiện nay phần lớn bác bỏ...", etc.), and every entry that has exculpatory/counter-evidence (Kosminski's uncertain identity, Druitt's factual errors in Macnaghten, Ostrog's alibi, Tumblety's likely custody alibi, Allen's DNA/handwriting/fingerprint exclusions, McCoy's alibi, Rackstraw's FBI exclusion) states that evidence in the same entry, not just the pro-guilt framing. PASS.
2. **No implicit-guilt-through-structure ("dramatic reveal").** Checked the ordering of every "Các giả thuyết" list: Ripper opens with Kosminski (the most publicized claim) and closes with Maybrick (widely called a hoax) — not built toward a climactic name. Zodiac opens with Allen and explicitly labels Poste/Case Breakers "claim gây tranh cãi nhất" up front (skepticism signposted before the claim is even detailed) rather than saving it as a triumphant reveal. Cooper closes on the least-established, most recent theory (Petersen/Ulis), explicitly marked as a private researcher's unconfirmed idea. The document's own Script-ready-material and Production-cautions sections additionally instruct downstream scriptwriters, in all three cases, never to use a "dramatic reveal" structure for any name. PASS.
3. **Kosminski 2014 shawl-DNA claim rebuttal, every occurrence (task item 2).** Grepped every occurrence of "Kosminski," "shawl/khăn choàng," "Edwards," "Louhelainen" in the file. Two bare name-only mentions (Macnaghten Memoranda suspect list, line 26; "Tứ Tượng nghi phạm" framing note, line 38) do not invoke the DNA claim at all, so no rebuttal is owed there. Every place the DNA claim itself is invoked (full suspect entry, its Production-cautions reminder, and the source-confidence footnote) carries the rebuttal (lack of published technical detail, disputed mutation citation, shawl provenance/chain-of-custody doubts, mtDNA's inherent non-specificity) in the same paragraph. PASS — no fix needed.
4. **Case Breakers / Gary Poste 2021 claim rebuttal, every occurrence (task item 2).** Same method for "Poste" and "Case Breakers." Every occurrence that states the claim also states the rebuttal (FBI non-confirmation/case remains open, SFPD same, Riverside PD's on-record denial of any Cheri Jo Bates–Zodiac link, DNA not independently verified) in the same sentence/paragraph, including the brief mentions in Script-ready material (line 92) and the source-confidence footnote (line 117). PASS — no fix needed.
5. **Zodiac's officially-open status flagged with extra caution (task item 3).** §"Production cautions" for Zodiac explicitly states the case is officially open (unlike the other two), and adds a specific instruction set: no proposing a "new" identity outside cited sources, no publishing the channel's own investigative conclusions, no inviting the audience to "self-investigate" or seek personal information about any living person of interest. This directly implements Guide §4a Format 2's "never imply guilt through structural placement" and the general non-interference concern for a technically-open case. PASS.
6. **D.B. Cooper: no fatality assumed anywhere (task item 4).** Checked every paragraph of the Cooper section. The "Primary concepts" section states outright that there is no certainty of death and instructs the script not to assume one; "Narrative detail" explicitly frames the 1980 money find as supporting two mutually-non-exclusive scenarios (died in the jump / survived and later discarded the cash) rather than picking one; "Production cautions" repeats the instruction not to assume death. Individual suspect entries (Christiansen, Rackstraw, Weber) refer to those *suspects'* deaths, never to Cooper's. PASS.
7. **CL-QA-002 net-impression test.** No sensational titles/thumbnail-style language anywhere in the packet (hooks are framed as "over 130 years, no one convicted" / "the only unresolved US hijacking" — sourced superlatives, not manufactured shock). Combined with finding #2 above (no reveal structure), the piece as a whole does not lead a viewer to conclude any one theory is settled. PASS.
8. **CL-QA-003 source-backed identification.** Every suspect name in the KP traces directly to a suspect already named in `RESEARCH_DRAFT_VU_AN_CHUA_LOI_GIAI.md`, itself citing tier 1–3 outlets (Wikipedia, Britannica, National Geographic, Smithsonian, Science/AAAS, The Conversation, Yale University Press blog, CBS News, BBC, FBI, CNN, NBC News, HistoryLink.org, etc.). No name, quote, or piece of forensic detail in the KP was found that isn't already present in the research draft. PASS.
9. **CL-QA-004 theory completeness.** Every case lists well above the 3-theory minimum (7 / 5 / 6) and explicitly carries forward competing/debunking evidence for each, rather than showcasing only the most dramatic name. PASS.
10. **CL-QA-009 layered interpretation, CL-QA-010 jurisdiction clarity, CL-QA-011 terminology, CL-QA-012 forbidden claims.** Each case states its jurisdiction and legal system before any procedural claim (UK/common law for Ripper; California/US federal-vs-state distinction for Zodiac; US federal jurisdiction for Cooper). No Vietnamese-specific procedural terms (bị can/bị cáo) are misapplied to these foreign cases. No forbidden-pattern sensational titling found. PASS (CL-QA-010 could be marginally strengthened — see note under (d) — but this is advisory-tier, not blocking).

---

## (b) Issue found

**CL-QA-005 (Victim privacy & dignity, blocking tier) — minor victims named without redaction.**

`DOMAIN_GUIDE.md` §6: *"Minor victims: never name, never show an identifiable image, and never describe identifying biographical detail — regardless of whether that detail is technically present in a public court record. This exception-free rule applies even when adult-victim naming would otherwise be permitted for the same case."*

The Zodiac section's "Primary concepts" listed the case's five confirmed victims by full name, including the two victims of the first (December 1968) attack, David Faraday and Betty Lou Jensen — both minors at the time of their deaths (historically documented as 17 and 16 respectively). The Guide's minor-victim rule is written as exception-free and explicitly overrides the public-record-naming allowance that applies to adult victims elsewhere in the same section — unlike §4's suspect-naming rule, §6 contains no parallel carve-out for well-documented historical/decades-old cases. Taken at face value, the rule required these two names not to appear in the packet.

This is a genuine, non-trivial finding: every mainstream source on this case (including the FBI's own materials) names these two victims as a matter of routine, and the KP's use here was purely a faithful, undramatized statement of the case's own basic confirmed-victim list — not exploitative detail. But per this domain's stated posture (§14: an unfixable-through-nuance rule still gets transformed, not left as a judgment call by the QA pass alone when the rule's text is unambiguous), the safer compliant action is redaction with a clear rationale note, leaving the policy question of whether a historical-victim carve-out should be added to §6 for the domain owner (see (d) below).

---

## (c) Exact fix applied

**Location:** `KP_CL_003_Vu_An_Chua_Loi_Giai.md`, §2 Zodiac Killer → "Primary concepts."

**Before:**
> 5 nạn nhân được điều tra viên xác nhận liên kết với "Zodiac" qua 4 vụ tấn công (12/1968 tới 10/1969): David Faraday & Betty Lou Jensen (cả hai chết); Michael Mageau & Darlene Ferrin (Ferrin chết, Mageau sống sót); Bryan Hartnell & Cecelia Shepard (Shepard chết, Hartnell sống sót); Paul Stine (chết).

**After:**
> 5 nạn nhân được điều tra viên xác nhận liên kết với "Zodiac" qua 4 vụ tấn công (12/1968 tới 10/1969): vụ tấn công đầu tiên có hai nạn nhân **vị thành niên** (một nam, một nữ; cả hai chết) — danh tính cụ thể của hai nạn nhân này KHÔNG được nêu trong tài liệu này và không được nêu trong bất kỳ script nào kéo từ packet này, theo `DOMAIN_GUIDE.md` §6 (quy tắc bảo vệ nạn nhân vị thành niên, không có ngoại lệ dù đã là hồ sơ công khai/lịch sử); Michael Mageau & Darlene Ferrin (Ferrin chết, Mageau sống sót — cả hai là người trưởng thành tại thời điểm vụ án, tên đã là hồ sơ công khai); Bryan Hartnell & Cecelia Shepard (Shepard chết, Hartnell sống sót — người trưởng thành); Paul Stine (chết — người trưởng thành).

**Second fix — added a standing Production-caution note** (§2 Zodiac Killer → "Production cautions") so future scripts drawn from this packet don't quietly re-insert the redacted names from other public sources:
> Nạn nhân vị thành niên (vụ tấn công 12/1968): hai nạn nhân đầu tiên của Zodiac là vị thành niên tại thời điểm bị sát hại. `DOMAIN_GUIDE.md` §6 cấm nêu danh tính nạn nhân vị thành niên không có ngoại lệ, kể cả khi tên đã là hồ sơ công khai/lịch sử rộng rãi (khác với quy tắc §4 dành cho nghi phạm/thủ phạm lịch sử, vốn có ngoại lệ cho trường hợp đã qua đời/đã kết án). Danh tính của hai nạn nhân này CỐ Ý không xuất hiện trong tài liệu này. Bất kỳ script nào kéo từ packet này không được tự tra cứu và chèn lại tên hai nạn nhân này từ các nguồn công khai khác — quy tắc này áp dụng bất kể mức độ phổ biến của thông tin trên các nguồn đại chúng. Nếu người phụ trách domain muốn xem xét một ngoại lệ cho nạn nhân vị thành niên đã qua đời hơn 55 năm trong hồ sơ đã đóng công khai, đó là quyết định chính sách cấp domain (sửa `DOMAIN_GUIDE.md` §6), không phải quyết định của một QA review đơn lẻ.

No other locations in the file named these two victims (confirmed via full-text search for "Faraday" and "Jensen" — only the one instance existed, now fixed). All other victims in the packet (Ferrin, Mageau, Hartnell, Shepard, Stine — all adults) remain named, consistent with §6's adult-victim allowance, and Ripper/Cooper have no victim-privacy issues (Ripper victims are 19th-century adults; Cooper has no confirmed-dead victim at all).

---

## (d) Unfixable / requires human judgment

**Whether `DOMAIN_GUIDE.md` §6 should carry a historical-victim carve-out, analogous to §4 Format 1's carve-out for historical/deceased perpetrators.**

The redaction applied above is the literally-compliant fix, but it creates a real tension the QA process alone shouldn't resolve unilaterally:

- §5 states procedural facts (which arguably include a decades-old case's basic, court/FBI-documented victim list) "may be stated as settled once confirmed by a tier-1 source."
- §6's minor-victim clause explicitly overrides that allowance with no age-of-case exception, unlike §4 which *does* grant convicted/historical perpetrators a named-factually exception once well-documented.
- In practice, every tier-1 source on this case (FBI's own Zodiac materials, all major press) names these two victims as a routine, undramatized case fact — this is not the kind of gratuitous/identifying detail (current address, family contact, photo, assault specifics) the rule appears aimed at stopping.

Recommendation for the domain owner: decide whether to (1) leave §6 as strictly exception-free (in which case this redaction — and the equivalent redaction in any other CL asset naming a historical minor victim — should be applied domain-wide), or (2) amend §6 to add a narrow, explicitly-scoped carve-out (e.g., "a minor victim deceased 50+ years, already named in the case's own official law-enforcement record and universally reported without objection from surviving family, may be named factually — mirrors §4 Format 1's historical-perpetrator allowance") so this doesn't need to be re-litigated file-by-file. This is a domain-policy decision, not something this single-file QA pass should decide by itself.

No other unfixable items were found — the five items the task specifically asked about (suspect hedging, the two contested-claim rebuttals, Zodiac's open-case caution, and Cooper's no-fatality-assumption) all passed on first read with no fix required.
