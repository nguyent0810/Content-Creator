---
schema_version: 1.0
domain_id: CL
domain_name: Hình Sự (Criminal Law & True Crime)
status: active
domain_guide: DOMAIN_GUIDE.md
default_language: vi
source_registry: SOURCES/SOURCE_REGISTRY.md
glossary: GLOSSARY/DOMAIN_GLOSSARY.md
qa_policy: DOMAIN_QA/DOMAIN_QA_POLICY.md
knowledge_packet_prefix: KP_CL
creative_packet_prefix: CK_CL
character_bible_prefix: CB_CL
series_bible_prefix: SB_CL
risk_level: critical
---

# Hình Sự Domain Manifest (Criminal Law & True Crime, merged)

Status: active (updated 2026-07-23). This domain absorbs the separate `TRUE_CRIME` (`TC`) domain skeleton per explicit channel-owner decision — one domain, five content pillars (Luật Hình Sự, Án Đã Xử, Vụ Án Chưa Có Lời Giải, Chân Dung Sát Nhân, Tổ Chức Tội Phạm), the same consolidation pattern used for `FS` (Tử Vi + Phong Thủy). `DOMAINS/TRUE_CRIME/` stays on disk marked `planned`/deprecated for registry-history continuity; do not produce content there. Full foundation: `DOMAIN_GUIDE.md` (critical-risk boundaries: presumption of innocence, victim privacy, no legal advice, organized-crime non-glorification, anti-sensationalism), `SOURCES/SOURCE_REGISTRY.md`, `GLOSSARY/DOMAIN_GLOSSARY.md`, `DOMAIN_QA/DOMAIN_QA_POLICY.md`. Five foundational Knowledge Packets built, one per pillar (`KP_CL_001_Luat_Hinh_Su.md` through `KP_CL_005_To_Chuc_Toi_Pham.md`, each drawing on a dedicated 2026-07-23 web-research pass cross-checked per `DOMAIN_GUIDE.md` §3's source hierarchy) — case roster: Pillar 2 (Năm Cam, Lê Văn Luyện, thẩm mỹ viện Cát Tường, O.J. Simpson), Pillar 3 (Jack the Ripper, Zodiac Killer, D.B. Cooper held for Season 2), Pillar 4 (Ted Bundy, Jeffrey Dahmer, Peter Sutcliffe/Andrei Chikatilo held for Season 2), Pillar 5 (Cosa Nostra, Yakuza/Hội Tam Hoàng/Cartel Medellín held for Season 2, băng Năm Cam). One Creative Knowledge packet (`CK_CL_001_Hinh_Su.md`) and one Series Bible (`SB_CL_001_Hinh_Su.md`, series name "Giải Mã Hình Sự") with a locked 15-episode Season 1 production plan (`SERIES_BIBLES/SEASON_01_PRODUCTION_PLAN.md`) are now also built. All content packets are `status: draft-pending-human-review` — a solid content-ready foundation, not a fully closed-out reference. HUMAN_REVIEW_REQUIRED before publishing any output — this is the highest risk_level domain on the channel, and every asset remains draft-pending-human-review until a human reviewer signs off, per the Activation Gate. **Known fix applied 2026-07-23:** `KP_CL_004` originally named six minor victims across its four profiles (not two as first found) in violation of §6 — found across two independent QA passes, corrected to anonymized age/role descriptions; the corresponding raw research draft carries a caution note for any future re-use. **First production package (2026-07-24):** `PRODUCTION_PACKAGES/HINH_SU/EP001/` (Season 1 Episode 1) validated the full pipeline end-to-end — `TOOLS/package_audit.py` result: PASS, 0 blocking, 0 warnings. This is a pipeline-validation test, not a publish-ready package; human sign-off is still required before real use.

