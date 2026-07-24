# Independent QA Report — KP_BUD_002 (Bát Nhã Tâm Kinh)

**Reviewer role:** Independent QA reviewer, did not author the packet or its research draft.
**Scope:** `KP_BUD_002_Bat_Nha_Tam_Kinh.md` checked against `RESEARCH_DRAFT_BAT_NHA_TAM_KINH.md` and `BUDDHIST_GUIDE.md`.
**Verdict: PASS, with one blocking issue found and fixed during this review.**

---

## Checklist

| # | Check | Result |
|---|---|---|
| 1 | Chinese-vs-Sanskrit origin debate presented as genuinely unresolved, no sentence secretly picks a winner | **PASS** |
| 2 | Xuanzang "sick monk" story consistently labeled legendary, never stated as verified history | **PASS** |
| 3 | No sutra quotation anywhere exceeds ~15 words | **PASS** |
| 4 | Śūnyatā/nihilism myth-bust section doesn't oversimplify into a new misconception | **PASS** |
| 5 | Historical/textual claims (translation dates, patriarch names, dynasty periods) trace to the research draft and are not upgraded beyond stated confidence | **FAIL → FIXED** (see Issue 1) |

---

## Detailed findings

### Check 1 — Chinese/Sanskrit origin debate

Read every mention of the Nattier/Attwood hypothesis and the Fukui/Harada/Ishii Kōsei/Vũ Thế Ngọc rebuttal across the Executive Summary, Core Content Map §2 (Primary concepts, Narrative detail, Script-ready material, Production cautions), and Editorial Notes §2. Both sides are consistently given:

- comparable descriptive weight (each side gets its named proponents, its supporting method/evidence, and an explicit "this is a serious hypothesis, not proof" qualifier)
- identical closing language ("chưa ngã ngũ," "KHÔNG được trình bày ... như sự thật đã chứng minh," repeated near-verbatim four times across the packet)
- the same Human Escalation flag (`BUDDHIST_GUIDE.md` §42) attached to both, not just one

No sentence anywhere resolves the debate or implies one hypothesis is favored. This matches the research draft's own explicit instruction (research draft §3.2, "Kết luận biên tập bắt buộc").

### Check 2 — Xuanzang legend

Checked every occurrence (Identity is silent on it; Core Content Map §2 Primary concepts, Narrative detail, Script-ready material, Production cautions; Editorial Notes §3). Every instance uses "LEGENDARY," "truyền thuyết," or the required phrasing "theo truyền thuyết được lưu truyền trong tiểu sử Huyền Trang..." Production cautions explicitly forbid promoting it to historical fact, and the packet preserves the research draft's own caveat that modern scholars (Jeffrey Kotyk) question its timeline against the Nattier hypothesis. No instance treats it as verified.

### Check 3 — Quotation length

Searched the entire file for every quoted string (straight and curly quotes). All quoted material is either:
- a short doctrinal phrase used as a labeled term, not a sutra excerpt ("Sắc bất dị Không, Không bất dị Sắc" — 6 words; "Không tức thị Sắc" — 4 words)
- editorial/production language in quotes (metaphor names, dialogue-beat sketches, caution-list phrases)
- the mantra transliteration (6 short phrases, already given as a standard formula in the research draft itself, not sutra prose)

Nothing approaches, let alone exceeds, 15 words of continuous sutra text. Production cautions in §1 and §5 independently repeat the 15-word rule twice, and Editorial Note 4 restates it a third time.

### Check 4 — Śūnyatā/nihilism myth-bust

Read Core Content Map §3 (Primary concepts, Narrative detail, Script-ready material) and §5 (myth-busting). The section:
- states Śūnyatā as "mô tả cách mọi vật hiện hữu (tương thuộc), không phủ nhận rằng chúng hiện hữu ở cấp độ quy ước" — correctly avoids collapsing into "everything is illusion" or "nothing matters ethically"
- explicitly retains the Trung Đạo (Middle Way) framing between thường kiến and đoạn kiến rather than replacing one extreme with another
- flags Trung Quán vs Duy Thức as requiring escalation rather than flattening them
- the wave/ocean and mirror metaphors are tied back to the technical definition each time they appear, per Production cautions ("luôn nối lại với định nghĩa gốc")

No sentence found that substitutes a new oversimplification (e.g., "everything is just interconnected energy," "emptiness means it's all relative/subjective") for the corrected misconception.

### Check 5 — Traceability of historical/textual claims (Issue found)

Cross-checked every date, patriarch name, and textual identifier in the packet against the research draft. All check out **except one**:

## Issue 1 (BLOCKING — fixed)

**Location:** Identity → Chinese (original line 95) and Canonical Sources → Source Priority Hierarchy table (original line 143).

**Problem:** The packet stated Kumārajīva's earlier Chinese translation of the Heart Sutra carries the Taishō Tripiṭaka catalog number **T250**. The research draft (§3.3) only states Kumārajīva produced a translation "khoảng 402–412 CN" — it never gives a Taishō number for it. Only Xuanzang's translation's Taishō number (T251) is sourced in the research draft (research draft §1). Presenting "T250" as fact is an unsupported addition beyond the source's stated confidence, and violates `BUDDHIST_GUIDE.md` §30 ("Never invent textual locations, chapter numbers, translators, or dates") and §40 ("Never cite what was not consulted").

**Before:**
```
- Bản dịch Huyền Trang: Đại Tạng Kinh Taishō ký hiệu T251 (649 CN)
- Bản dịch trước đó của Cưu Ma La Thập: Taishō T250 (khoảng 402–412 CN)
```
```
| 1 | Canonical — bản dịch Hán được công nhận rộng rãi | Bản Huyền Trang T251 (649 CN), bản Cưu Ma La Thập T250 |
```

**After (fixed in this review):**
```
- Bản dịch Huyền Trang: Đại Tạng Kinh Taishō ký hiệu T251 (649 CN)
- Bản dịch trước đó của Cưu Ma La Thập (khoảng 402–412 CN) — research draft nguồn không xác nhận ký hiệu Taishō cụ thể cho bản dịch này; không dùng số hiệu catalog chưa được đối chiếu độc lập cho tới khi có nguồn xác minh, theo `BUDDHIST_GUIDE.md` §30 ("Never invent textual locations, chapter numbers, translators, or dates")
```
```
| 1 | Canonical — bản dịch Hán được công nhận rộng rãi | Bản Huyền Trang T251 (649 CN), bản Cưu Ma La Thập (khoảng 402–412 CN, ký hiệu Taishō cụ thể chưa được xác minh trong research draft nguồn) |
```

All other traceable claims checked clean: Huyền Trang's dates (602–664), the 649 CN translation year and Chùa Từ Ân setting, the three steles (661/669/672 CN) and Đường Thái Tông decree, Edward Conze's ~350 CE estimate and ~90% textual-overlap figure, the Nattier/Attwood/Fukui/Harada/Ishii Kōsei/Vũ Thế Ngọc names and positions, and the Nāgārjuna "systematization" attribution (correctly flagged as traditional, not historical) all trace cleanly to the research draft without upgrade.

---

## Anything needing human judgment

Nothing new surfaced by this QA pass. The packet already correctly flags, and this review concurs, that the following remain open Human Escalation candidates per `BUDDHIST_GUIDE.md` §42 if a future script goes beyond high-level summary:

1. Detailed scholarly treatment of the Nattier/Attwood vs. Fukui/Harada/Ishii Kōsei/Vũ Thế Ngọc debate (syntactic comparison specifics, manuscript dating).
2. Detailed Trung Quán vs. Duy Thức comparison of Śūnyatā interpretation.

No other blocking or judgment-call items were found.
