# QA Report — Gap-Closure Edits to KP_FS_001 & KP_FS_002 (2026-07-24)

**Reviewer:** Independent QA pass (no authorship overlap with the edits reviewed)
**Scope:** All edits made in commit `5731b34` ("Expand knowledge base across all three domains" — Feng Shui portion only) that added material sourced from `SOURCES/RESEARCH_DRAFT_GAP_CLOSURE_2026_07.md` into `KP_FS_001_Phong_Thuy.md` and `KP_FS_002_Tu_Vi.md`.
**Context:** This domain had one prior real incident (caught by an earlier independent QA pass) where a research/synthesis agent fabricated source attribution inside `KP_FS_001`'s Khí section. This pass treats every new citation with the same suspicion that incident warrants, and cross-checks each claim directly against the diff (`git show 5731b34 -- <file>`), not just the final file text.

**Verdict: PASS.** No fabricated, stretched, or invented citation found. No caution was loosened. No confidence tier was upgraded beyond what the research draft actually supports.

---

## 1. KP_FS_001 — New citations to Bruun / Paton / Smith

Checked every instance (frontmatter `source_lineage`, Packet Control `Last Updated`, Loan Đầu paragraph, Historical Development, Historical Debates #3, Canonical Sources table row, Source Priority Hierarchy Tier 4, and the new "Nguồn học thuật Tier 4 mới xác định" section — 8 locations total, confirmed via `Grep` for "Bruun|Paton|Smith").

| Claim | Research draft support | Verdict |
|---|---|---|
| 3 sources (Bruun ×2, Paton, Smith) exist, are genuine academic publications (university presses / peer-reviewed journal), confirmed via direct search | Research draft §1: "Confidence: cao rằng các nguồn này tồn tại và là học thuật thật" | Matches — not a stretch |
| Confidence "trung bình" for internal/detailed content of these sources (not deep-read) | Research draft §1: "Confidence trung bình về nội dung chi tiết bên trong... chỉ xác minh được sự tồn tại, phạm vi, và uy tín học thuật" | Matches exactly, correctly carried into the packet's own confidence language |
| Bruun's *Fengshui in China* used only for a general framing claim (living tradition evolving through state-orthodoxy/popular-religion phases, ethnographic fieldwork basis) | Research draft describes book's fieldwork basis and subtitle ("State Orthodoxy and Popular Religion") | General framing claim, not a page-level content claim — appropriately scoped and explicitly caveated in-text ("packet này chưa dùng chúng để xác nhận bất kỳ chi tiết cụ thể nào về quá trình tiếp biến vào Việt Nam") |
| Paton's *Five Classics of Fengshui* flagged as the strongest future candidate to verify the Táng Thư/Quách Phác citation, but confidence on that citation explicitly **held at "trung bình," not upgraded** | Research draft §1 explicitly recommends this exact restraint: "khuyến nghị bước tổng hợp sau này đối chiếu bản dịch của Paton trước khi nâng nhãn tin cậy" | Matches precisely — the packet does NOT upgrade the Táng Thư/Quách Phác confidence, twice reaffirming this restraint (Loan Đầu paragraph and Historical Debates #3) |
| Smith's article used only as a pointer for possible future research into Phong Thủy's transmission into Vietnam — explicitly marked as not yet used for any Vietnam-specific claim | Research draft §1 describes Smith's article scope only (1600–1900 East Asia transnational spread) | Matches, correctly under-claimed |

**No instance found** of the packet claiming these sources were "deeply read," citing page numbers, chapter content, or any specific argument/finding beyond what the research draft itself reported finding (existence, scope, publisher/journal credibility). Every new passage carries its own confidence caveat consistent with the research draft's own two-tier confidence split (high for existence/scope, medium for content).

## 2. KP_FS_002 — an sao, Ho Peng Yoke, Cụ Thiên Lương, Vân Đằng Thái Thứ Lang

Verified by diffing the exact pre-edit and post-edit text (`git show 5731b34 -- KP_FS_002_Tu_Vi.md`), not just reading the current file — this catches silent loosening that a same-file-only read could miss.

**a) An sao caution (highest-priority check per task instructions).** The four pre-existing Production caution bullets under "Cách lập lá số Tử Vi cơ bản" are preserved **verbatim, character-for-character**, in the diff:
- "This is the single highest-risk structural topic in the packet..."
- "Never present the counting procedure as one universally fixed formula..."
- "Do not go deeper into chính tinh/phụ tinh placement technique..."
- "Any illustrative example of chart construction must use a clearly fictional or long-deceased historical/legendary figure..."

One new bullet was *inserted* (not substituted) between bullets 3 and 4, explicitly reaffirming the caution is "kept, not loosened," and a new Script-ready material metaphor ("two anchor stars... without walking through the counting/remainder arithmetic") was added, explicitly labeled as additive-only and explicitly not authorizing any worked calculation. **No loosening found.**

**b) Ho Peng Yoke.** Presented strictly as an existence/scope-confirmed Tier 4 candidate ("A full-text search confirmed the book genuinely discusses 'Ziwei doushu' directly... only short excerpts were read, not the full relevant chapter — do not cite specific claims from this book... as settled until a full read is done"). No specific content claim (e.g., about Trần Đoàn, dating, or transmission history) is attributed to the book anywhere in the packet. Matches research draft §1 exactly.

**c) Cụ Thiên Lương.** Before: "real name given variously as Lê Quang Khải or Lê Quang Vinh depending on source — name requires further verification... reportedly born 1910." After: name/dates (Lê Quang Khải, 1910–1985) presented at explicit **"medium-high," not "high"** confidence, with the independence caveat spelled out in full ("the wording... is near-identical across the sites that repeat it... strongly suggesting they all trace back to a single original biographical article... not several genuinely independent research sources converging"). The "Lê Quang Vinh" variant is dropped with the correct justification (not found in this pass, not "proven false"). This matches the research draft's §3 confidence level and caveat precisely — no upgrade beyond what was found.

**d) Vân Đằng Thái Thứ Lang.** Remains explicitly unresolved: "This gap remains genuinely unresolved as of the 2026-07-24 follow-up pass," "No real name, birth year, or death year was found." The only addition is the forum-thread finding ("Cụ VDTTL còn sống hay đã mất?"), reported honestly as an unread thread whose *existence* (not content) is the finding, exactly as the research draft frames it. **No invented resolution.**

## 3. Version/date bump check

Confirmed via diff, not just current-file text:

- `KP_FS_001_Phong_Thuy.md`: `version: 0.1` → `0.2`, `last_updated: 2026-07-24` added (frontmatter and Packet Control table both updated consistently).
- `KP_FS_002_Tu_Vi.md`: `Version: 1.0` → `1.1`, `Last Updated: 2026-07-24 (gap-closure pass...)` added.

Both bumps are real (confirmed against the prior committed version, not just asserted in the new text) and dated correctly to today.

---

## Issues found

None blocking. No fixes were required or made to either file.

## Items for human judgment (not QA failures, carried over from the research draft itself)

- Paton's *Five Classics of Fengshui* remains the natural next step to actually upgrade the Táng Thư/Quách Phác citation — this requires someone to read the translation directly; the packet correctly does not do this itself yet.
- Cụ Thiên Lương's biography is at "medium-high," one step short of DOMAIN_GUIDE.md §3's "2-3 independent sources" bar for "high" — a genuinely independently-sourced biography (e.g., a digitized original "Khoa Học Huyền Bí" issue) would close this the rest of the way. Not required before current use, since the packet already discloses the caveat.
- Vân Đằng Thái Thứ Lang's biography remains a standing open research gap; no action taken here beyond what the research draft supports, per instructions.

## Conclusion

Both packets pass this QA pass with no fabricated, stretched, or prematurely-upgraded citation, and no loosened safety caution. The edits are unusually disciplined about carrying forward the research draft's own confidence ceilings rather than rounding them up — this is the correct behavior given this domain's prior incident.
