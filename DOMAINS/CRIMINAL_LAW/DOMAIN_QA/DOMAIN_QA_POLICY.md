# Domain QA Policy: Hình Sự (Criminal Law & True Crime)

Status: active foundation (upgraded from `planned` 2026-07-22). This is the domain-specific QA gate that supplements `CORE_OS/QA_ENGINE.md` for any script, Short, or SEO asset produced under domain `CL`. Every check below traces directly to a numbered section in `DOMAIN_GUIDE.md` — read that file first; this is the checklist derived from it, not an independent set of rules. This domain's QA carries real legal-risk weight (defamation, contempt of an active case) that the FS and BUD domains' QA does not — treat a QA pass here with correspondingly greater rigor.

## Mandatory Pre-Publication Checks

| Check ID | Category | What it verifies | Source rule |
|---|---|---|---|
| CL-QA-001 | Legal-status precision | Every living, not-finally-convicted person is described with correct hedged language (bị tình nghi/bị can/bị cáo), never a guilt-asserting noun. Finally-convicted persons (bản án có hiệu lực pháp luật) may be named factually; live-appeal status is disclosed if applicable. | `DOMAIN_GUIDE.md` §4 |
| CL-QA-002 | Net-impression test | The piece as a whole — title, thumbnail-text, hook, narrative structure — does not lead an ordinary viewer to conclude guilt is established fact, even where individual sentences are correctly hedged. This is a whole-piece judgment call, not a search-and-replace check. | §4 |
| CL-QA-003 | Source-backed identification (Format 2/3) | Any named suspect/person-of-interest or criminal organization traces to a tier-1-to-3 source that already publicly makes that connection; the content presents it as one theory among the sourced record's theories, not the channel's own conclusion. | §4a, §5 |
| CL-QA-004 | Theory completeness | For unsolved cases, credible competing theories in the sourced record are represented, not omitted to make one theory look stronger. No invented theory, forensic detail, or witness statement. | §5 |
| CL-QA-005 | Victim privacy & dignity (claim-type lock, not a topic ban) | No victim's current address/contact info or private photos; no minor victim identified under any circumstance; adult victims named only within public-record/self-disclosure bounds; no exploitative/graphic dramatization of suffering. Case-narrative and legal-explainer content about victims generally remains fully open — see §14's transform pattern before treating a draft as blocked. **Mandatory sub-check (added 2026-07-23, after a QA pass found 8 separate minor-victim-naming instances across this domain's first content batch, missed by the writing agents that produced them):** for every named victim in any script, Knowledge Packet, or research draft, the reviewer must independently verify the victim's age at the time of the event — do not trust that "the victim is widely named in public sources" implies they were an adult. Well-documented historical minors (e.g., a famous case's youngest victim) are exactly the ones most likely to appear pre-named in source material and get carried through without an age check. This sub-check is required even when the surrounding case is otherwise low-risk (finally-convicted, deceased perpetrator, decades-old case). | §6, §14 |
| CL-QA-006 | No legal advice (claim-type lock, not a topic ban) | No line tells the viewer what to do about their own specific legal situation. General educational explanation of law/procedure remains fully open. | §7, §14 |
| CL-QA-007 | Organized-crime non-glorification (claim-type lock, highest severity, not a topic ban) | No operational recruitment/laundering/evasion detail; no heroic/aspirational framing of a criminal figure or organization; no usable gang/triad insignia. Historical/sociological organized-crime content remains fully open — see §14's transform pattern before treating a draft as blocked. | §8, §14 |
| CL-QA-008 | Anti-sensationalism | No manufactured shock titles, gore, or countdown-of-horror framing; no treating a real victim's death as entertainment shock value. | §9 |
| CL-QA-009 | Layered interpretation intact | Legal/procedural, narrative/case, and societal-reflective layers are all present where relevant — none erased by flattening into "just" a timeline or "just" a dramatic story. | §10 |
| CL-QA-010 | Jurisdiction clarity | Every case names which country's legal system it occurred under before any procedural claim is made; no foreign legal concept (grand jury, Miranda rights, plea bargain) is implied to apply in Vietnam without being flagged as foreign. | §2 |
| CL-QA-011 | Terminology consistency | All terms match `GLOSSARY/DOMAIN_GLOSSARY.md`; no invented terminology. | §11 |
| CL-QA-012 | Forbidden claims | No line matches any item in §12's never-use list. | §12 |

## Severity

- **Blocking (must be transformed, per §14, before any publication):** CL-QA-001, CL-QA-002, CL-QA-003, CL-QA-005, CL-QA-006, CL-QA-007, CL-QA-008, CL-QA-012 — these map to hard, non-negotiable claim-type locks in `DOMAIN_GUIDE.md`. "Blocking" describes the *claim*, not the script or the case, per the Process section below.
- **Advisory (should fix, does not block if isolated and minor):** CL-QA-004, CL-QA-009, CL-QA-010, CL-QA-011.

## Process

QA for this domain follows the same independent-reviewer discipline already proven in the Buddhism (`BUD`) and Feng Shui (`FS`) domains: the agent/reviewer checking a script must not be the same context that wrote it, must read the full script (not skim), and must check against `DOMAIN_GUIDE.md` directly rather than relying on memory of its rules. **Given this domain's real-person legal risk, a QA reviewer here should also independently re-verify at least the case's legal-status claims and its most load-bearing citations against the `SOURCE_REGISTRY.md` entries — not just check that a citation exists, but that the citation actually says what the script claims it says.**

**Finding a blocking issue is the start of the QA agent's work, not the end of it.** Per `DOMAIN_GUIDE.md` §14 ("Transform First, Refuse Only When Impossible"), a QA reviewer for this domain acts as an editor who repairs risk, not a gatekeeper who only flags it:

1. Name the exact invalid claim (not the whole beat, Short, or script).
2. Apply §14's per-boundary transform pattern (premature guilt → investigation/mystery framing; victim privacy → shift weight to investigation/consequence; legal advice → general educational framing; organized-crime glamorization → systemic/investigative-response framing) and rewrite that line directly in the script file.
3. If a specific expression must be dropped rather than transformed in place, the QA report must offer at least three alternative directions for it — one mass-appeal, one storytelling, one deep-analysis (per §14) — so the writer/next agent has real options, not just a deletion.
4. Only escalate to "cannot be produced as-is" if no compliant transform exists after genuinely attempting one; state precisely which claim type blocked it, and note what adjacent territory remains open.
5. Continue to a complete, deliverable QA report — do not stop mid-review to relitigate whether §4/§6/§7/§8 apply; they do, and the job is to transform around them.

A QA report that only lists violations without attempting the transform, or that leaves a script watered down into vague/generic language rather than genuinely transformed, has not completed this domain's QA process. Findings (including every transform applied) are written to that package's `06_QA_REPORT.md`, following the same format used across `PRODUCTION_PACKAGES/`.

## Related Documents

- `DOMAIN_GUIDE.md` — the full rules this checklist is derived from.
- `GLOSSARY/DOMAIN_GLOSSARY.md` — terminology reference.
- `SOURCES/SOURCE_REGISTRY.md` — source tracking.
- `KNOWLEDGE_PACKETS/` — foundational knowledge this domain's content must trace back to (not yet written).
