# EP004 QA Plan

## QA Readiness

`qa_plan_status: READY_FOR_PLANNING_REVIEW`

Scriptwriting gate remains closed until blocking research gaps are resolved.

## QA Records

| QA ID | QA name | Category | Reason required | Inputs | Checks | Blocking or advisory | Failure condition | Required evidence | Reviewer type | Execution stage | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| QA-001 | Asset resolution QA | Core QA | Ensure new architecture only | EP004_ASSET_RESOLUTION.md | required assets exist; no root fallback | blocking | missing canonical asset or legacy fallback | asset table | systems/editorial | pre-draft | READY |
| QA-002 | Source presence QA | Core QA | Verify source files exist | SOURCE_REGISTRY; source files | source paths resolve; metadata gaps labeled | blocking | source absent or metadata fabricated | file paths | researcher | pre-draft | READY |
| QA-003 | Claim-to-source QA | Core QA | Prevent hallucination | Source-Claim Matrix | every critical claim sourced or gapped | blocking | critical claim unsupported | claim matrix | researcher | pre-draft | READY |
| QA-004 | Internal consistency QA | Core QA | Align manifest, plan, claims | all EP004 docs | IDs and statuses match | blocking | conflicting status or ID | cross-doc check | producer | pre-draft | READY |
| QA-005 | Terminology consistency QA | Core QA | Standardize Buddhist terms | Terminology Map; glossary | no forbidden simplifications | blocking | nghiệp as punishment; phước as material guarantee | term map | Buddhist editor | draft/review | READY |
| QA-006 | Lineage QA | Core QA | Avoid pan-Buddhist overclaim | KP; Guide | label Mahayana/Vietnamese context | blocking | universal claim without attribution | source notes | Buddhist editor | draft | READY |
| QA-007 | Unsupported generalization QA | Core QA | Prevent broad claims | claim matrix | no “Buddhism says” without scope | blocking | overgeneralization | wording review | editor | draft | READY |
| QA-008 | Structure QA | Core QA | Confirm outline is not script | Episode Plan | no narration/hook/scene screenplay | blocking | script-like passages | plan review | producer | pre-draft | READY |
| QA-009 | Doctrinal QA | Buddhism Domain QA | Protect Buddhist accuracy | Guide; KP; matrix | doctrine vs interpretation separated | blocking | creative framing treated as doctrine | annotated claims | Buddhist reviewer | pre-draft/draft | READY |
| QA-010 | School/tradition attribution QA | Buddhism Domain QA | Avoid tradition drift | KP; brief | Mahayana and Vietnamese reception labeled | blocking | sectarian/universal overclaim | attribution notes | Buddhist reviewer | draft | READY |
| QA-011 | Canonical-versus-commentarial QA | Buddhism Domain QA | Separate layers | matrix | canonical, commentary, modern reflection labeled | blocking | commentary presented as sutra | claim types | Buddhist editor | pre-draft | READY |
| QA-012 | Superstition QA | Buddhism Domain QA | Prevent magical claims | Guide; KP rules | no fear, guarantee, transaction language | blocking | miracle bait or ritual guarantee | wording review | safety/editorial | draft | READY |
| QA-013 | False-promise QA | Buddhism Domain QA | Avoid guaranteed merit/rescue | KP Merit Rule; Guide | no certainty claims about benefits | blocking | guaranteed rescue/reward | claim matrix | safety reviewer | draft | READY |
| QA-014 | Grief and emotional-safety QA | Buddhism Domain QA | Protect vulnerable viewers | Guide; QA policy | no blame for deceased/parents | blocking | guilt or crisis-triggering content | safety review | safety reviewer | draft | READY |
| QA-015 | Respectful representation QA | Buddhism Domain QA | Protect sacred figures | CB; visual plan | respectful Buddha, Maya, Địa Tạng representation | blocking | invented disrespectful depiction | character plan | Buddhist/editorial | visual/draft | READY |
| QA-016 | Cung Trời Đao Lợi context QA | Episode-specific QA | Central setting | brief; matrix | cosmology framed properly | blocking | science/history confusion | source/cosmology notes | Buddhist reviewer | pre-draft | READY |
| QA-017 | Buddha-mother relationship claim QA | Episode-specific QA | Critical episode claim | C003/C004/C014 | exact source citation before quote | blocking | invented motive or quote | verified citation | researcher/Buddhist reviewer | pre-draft | READY |
| QA-018 | Filial-piety interpretation QA | Episode-specific QA | Sensitive family ethics | Guide; claims C005-C006 | no coercion, no absolute obedience | blocking | guilt-based hiếu | wording checklist | Buddhist/safety reviewer | draft | READY |
| QA-019 | Character-role QA | Episode-specific QA | Missing character bibles | Character Plan | no invented interiority | blocking | unsupported characterization | character asset notes | producer/editor | draft | READY |
| QA-020 | Cosmology framing QA | Episode-specific QA | Prevent realism confusion | Visual plan; Guide | label symbolic/cosmological layer | blocking | literal documentary claim | visual notes | visual/research reviewer | visual | READY |
| QA-021 | Historical-claim QA | Episode-specific QA | Prevent false history | Research Brief | no secular historical claim unless sourced | blocking | heavenly assembly as modern historical fact | source citation | researcher | draft | READY |
| QA-022 | Creative-adaptation boundary QA | Episode-specific QA | Keep framing safe | CK; episode plan | creative layer labeled | blocking | creative detail used as evidence | section layer table | producer | draft | READY |
| QA-023 | Guilt-based filial-piety QA | Risk-specific QA | Protect audience | Guide; claims | no shame tactics | blocking | “bad child” messaging | wording review | safety reviewer | draft | READY |
| QA-024 | Absolute-obedience implication QA | Risk-specific QA | Prevent abuse enabling | Guide | no obedience absolutism | blocking | suggests obeying harmful parents | safety review | safety reviewer | draft | READY |
| QA-025 | Material-reward promise QA | Risk-specific QA | Prevent transactional doctrine | KP; Guide | no material guarantees | blocking | promises money/fortune | claim scan | safety/editor | draft | READY |
| QA-026 | Health or fortune promise QA | Risk-specific QA | Avoid medical/fortune claims | Guide | no healing/fortune guarantees | blocking | health/fortune promise | safety review | safety reviewer | draft | READY |
| QA-027 | Scientific-fact confusion QA | Risk-specific QA | Cosmology safety | Visual plan; Guide | no science claims | blocking | cosmology as empirical fact | claim scan | researcher | draft | READY |
| QA-028 | Sectarian overclaim QA | Risk-specific QA | Tradition humility | KP; Guide | label Mahayana/Vietnamese context | blocking | “all Buddhism teaches exactly” | source notes | Buddhist reviewer | draft | READY |
| QA-029 | Copyright and citation QA | Risk-specific QA | Publication safety | Source registry; source files | metadata complete before public script | blocking | public quote without clearance | bibliographic record | human researcher | pre-production | PENDING_HUMAN_REVIEW |

## QA Gate

| Gate condition | Current status |
|---|---|
| Asset Resolution: PASS | PASS |
| Critical Claims: APPROVED_FOR_PLANNING or APPROVED_WITH_ATTRIBUTION | NOT_MET |
| Research Gaps: no blocking gaps | NOT_MET |
| Doctrinal QA Plan: READY | READY |
| Source Attribution Plan: READY | HUMAN_REVIEW_REQUIRED |
| Episode Structure: APPROVED | PLANNING_READY |
| Human Review completed for blocking items | NOT_MET |

`scriptwriting_gate: CLOSED`
