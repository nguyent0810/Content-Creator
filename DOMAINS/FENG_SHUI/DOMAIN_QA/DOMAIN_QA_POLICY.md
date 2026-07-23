# Domain QA Policy: Tử Vi & Phong Thủy

Status: active foundation (upgraded from `planned` 2026-07-17). This is the domain-specific QA gate that supplements `CORE_OS/QA_ENGINE.md` for any script, Short, or SEO asset produced under domain `FS`. Every check below traces directly to a numbered section in `DOMAIN_GUIDE.md` — read that file first; this is the checklist derived from it, not an independent set of rules.

## Mandatory Pre-Publication Checks

| Check ID | Category | What it verifies | Source rule |
|---|---|---|---|
| FS-QA-001 | Source attribution | Every specific factual claim names its source/school, or is explicitly flagged as cross-school consensus. No claim is presented as universally agreed when schools disagree (e.g., Bát Trạch vs. Huyền Không Phi Tinh can disagree on the same house). | `DOMAIN_GUIDE.md` §2-3 |
| FS-QA-002 | No individualized reading of a living private person | No line calculates, implies, or narrates a reading "for you," the viewer, or any specific/implied real living private person. Two formats are explicitly exempt from this check, not violations of it: (a) zodiac-year cohort content addressed to a birth-year group, not an individual; (b) retrospective case studies of documented, deceased, or public historical figures. Both exempt formats must still independently pass FS-QA-003 through FS-QA-007. | §4, §4a |
| FS-QA-003 | No certainty language | No line states a future outcome as certain fact ("bạn sẽ..."). All predictive language uses traditional-belief framing ("theo Tử Vi truyền thống, ... thường được xem là..."). | §5 |
| FS-QA-004 | Financial boundary (claim-type lock, not a topic ban) | No specific investment, trading, business, or purchase/loan advice tied to a chart or layout reading. No object/direction/ritual claimed as a guaranteed wealth mechanism. Cultural, symbolic, and psychological wealth content remains fully open — see §14's transform pattern before treating a draft as blocked. | §6, §14 |
| FS-QA-005 | Health boundary (claim-type lock, not a topic ban) | No diagnosis, no specific health-event prediction, no claim that a practice cures, prevents, or replaces medical treatment. Living-space quality, rest, habit, and traditional-belief content remains fully open — see §14's transform pattern before treating a draft as blocked. | §7, §14 |
| FS-QA-006 | Lifespan/serious-event boundary (claim-type lock, highest severity, not a topic ban) | No specific death, health-crisis, or major-misfortune timing for any living real or implied person. No structure inviting a viewer to self-apply a mortality-adjacent reading. Historical pattern, symbolism, life-cycle themes, and §4a Format 2 case studies of documented deceased/public figures remain fully open — see §14's transform pattern before treating a draft as blocked. | §8, §4a, §14 |
| FS-QA-007 | Anti-fear-sales | No manufactured urgency, threat, or dread framing tied to an action, purchase, subscription, or share. | §9 |
| FS-QA-008 | Layered interpretation intact | Cultural/historical, traditional-belief, and modern-reflective layers are all present where relevant — none erased by presenting the content as "just symbolism" or "just literal fact." | §10 |
| FS-QA-009 | Terminology consistency | All terms match `GLOSSARY/DOMAIN_GLOSSARY.md`; no invented terminology. | §11 |
| FS-QA-010 | Forbidden claims | No line matches any item in §12's never-use list (scientific-proof claims, authoritative personal reading, financial/medical/legal/safety advice via reading-frame, mortality timing, fear/urgency framing, mockery or unquestionable-fact framing). | §12 |

## Severity

- **Blocking (must be transformed, per §14, before any publication):** FS-QA-002, FS-QA-004, FS-QA-005, FS-QA-006, FS-QA-007, FS-QA-010 — these map to hard, non-negotiable claim-type locks in `DOMAIN_GUIDE.md`. "Blocking" describes the *claim*, not the script or the topic — see the Process section below for what a reviewer does when one is found.
- **Advisory (should fix, does not block if isolated and minor):** FS-QA-001, FS-QA-003, FS-QA-008, FS-QA-009.

## Process

QA for this domain follows the same independent-reviewer discipline already proven in the Buddhism domain (`BUD`): the agent/reviewer checking a script must not be the same context that wrote it, must read the full script (not skim), and must check against `DOMAIN_GUIDE.md` directly rather than relying on memory of its rules.

**Finding a blocking issue is the start of the QA agent's work, not the end of it.** Per `DOMAIN_GUIDE.md` §14 ("Transform First, Refuse Only When Impossible"), a QA reviewer for this domain acts as an editor who repairs risk, not a gatekeeper who only flags it:

1. Name the exact invalid claim (not the whole beat, Short, or script).
2. Apply §14's per-boundary transform pattern (financial → cultural/psychological framing; health → space/habit framing; lifespan → historical/symbolic/case-study framing) and rewrite that line directly in the script file.
3. If a specific expression must be dropped rather than transformed in place, the QA report must offer at least three alternative directions for it — one mass-appeal, one storytelling, one deep-analysis (per §14) — so the writer/next agent has real options, not just a deletion.
4. Only escalate to "cannot be produced as-is" if no compliant transform exists after genuinely attempting one; state precisely which claim type blocked it, and note what adjacent territory remains open.
5. Continue to a complete, deliverable QA report — do not stop mid-review to relitigate whether §6/§7/§8 apply; they do, and the job is to transform around them.

A QA report that only lists violations without attempting the transform, or that leaves a script watered down into vague/generic language rather than genuinely transformed, has not completed this domain's QA process. Findings (including every transform applied) are written to that package's `06_QA_REPORT.md`, following the same format used across `PRODUCTION_PACKAGES/`.

## Related Documents

- `DOMAIN_GUIDE.md` — the full rules this checklist is derived from.
- `GLOSSARY/DOMAIN_GLOSSARY.md` — terminology reference.
- `SOURCES/SOURCE_REGISTRY.md` — source tracking.
- `KNOWLEDGE_PACKETS/` — foundational knowledge this domain's content must trace back to.
