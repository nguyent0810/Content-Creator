# Core Visual Engine

The Visual Engine manages reusable visual workflow, asset dependency, caption safety, image provenance, video-prompt handoff, and production constraints. Domain-specific iconography, sacred imagery, legal evidence visuals, victim privacy, copyright, clinical imagery, and cultural symbols must be loaded from the domain guide and domain QA.

## Scope Boundary

The Visual Engine may create visual planning data and video-generation prompts as external handoff assets.

The Visual Engine must not:

- render video;
- generate images unless explicitly requested;
- align audio;
- create final subtitles;
- upload;
- publish;
- mark downstream media production as complete.

Video prompts are instructions for an external generation tool. They are not rendered media.

## Video Prompt Output Standard

When a package requests video-generation prompts, the canonical public output is:

`OUTPUT/04_VIDEO_CREATE_PROMPTS.txt`

The optional internal mapping is:

`_INTERNAL/04_VIDEO_PROMPT_TIMELINE.json`

No additional visual brief, prompt report, audit report, status file, subtitle file, metadata publication file, or per-prompt file should be created by default.

## Timeline Handling

Video prompts must cover the full narration timeline in continuous fixed-duration blocks.

Default block duration: `6 seconds`.

Timeline source priority:

1. Use actual audio duration when reliable audio exists.
2. Use QA-approved manifest duration when available.
3. Estimate from TTS word count and declared narration speed. If no speed is declared, use `130` words per minute and mark the timeline as `ESTIMATED`.

Every block must:

- begin at the previous block's end;
- last exactly 6 seconds;
- have no gap;
- have no overlap;
- receive one prompt number;
- map to narration context or a valid closing visual hold.

The final block is rounded up to the next 6-second boundary. If narration ends before the final block ends, use the remaining time for slow visual hold, transition, or contemplative closing without adding false narration.

## Narration-To-Visual Mapping

Mapping must consider sentence boundaries, paragraph boundaries, punctuation pauses, semantic context, and estimated speaking duration.

Do not split purely by word count when doing so would destroy meaning. If a sentence spans multiple blocks, keep those blocks in the same scene sequence and develop the camera or subject action gradually.

The narration context in the public prompt file is for review only. It should be a concise Vietnamese quotation or close summary. It must not rewrite the teaching or add narration.

## Scene Sequences

Adjacent prompts should be grouped into scene sequences when they share the same thought, setting, subject, or emotional movement.

Prompts inside one sequence must maintain:

- character appearance;
- costume;
- environment;
- lighting;
- time of day;
- color palette;
- props;
- architectural style;
- weather;
- visual symbolism.

Each prompt must still stand alone. It may reference continuity by restating important visual features, but must not rely on phrases such as `continue previous scene` or `same as above`.

## Visual Modes

Each prompt record must use exactly one visual mode:

- `CANONICAL_RECONSTRUCTION`
- `TRADITIONAL_REPRESENTATION`
- `SYMBOLIC_VISUALIZATION`
- `MODERN_APPLICATION`
- `ABSTRACT_METAPHOR`
- `TRANSITIONAL_ATMOSPHERE`

Canonical reconstruction is allowed only when sources and planning support the event or setting. Symbolic visualization must not pretend to be historical reconstruction. Modern application must not be presented as scripture.

## Prompt Anatomy

Each video prompt should include, when relevant:

- main subject;
- secondary subjects;
- action;
- environment;
- time and atmosphere;
- camera shot;
- camera movement;
- subject movement;
- lighting;
- composition;
- visual style;
- emotional tone;
- continuity constraints;
- Buddhist representation constraints;
- negative constraints;
- aspect ratio;
- duration.

Each 6-second prompt should contain one primary visual action, one coherent camera idea, and one clear emotional purpose.

Avoid overloaded prompts that request multiple unrelated scenes, rapid montage, fake dialogue, or large shot changes inside a single 6-second block.

## Camera Language

Use one main camera concept per prompt, such as:

- slow dolly in;
- slow dolly out;
- gentle lateral tracking;
- controlled crane movement;
- static contemplative composition;
- slow orbit;
- subtle handheld documentary movement;
- aerial drift.

Camera movement must serve the emotional and doctrinal purpose. Contemplative Buddhist material should not use chaotic motion, rapid flicker, shock cuts, or spectacle-first camera language.

## Buddhist Representation Safety

Sacred figures, Buddhist cosmology, ritual scenes, monastics, and devotional objects must be represented with reverence, restraint, and source humility.

Do not:

- invent dialogue or lip-sync for sacred figures;
- add unsupported motives, emotions, or events;
- use disrespectful angles or horror lighting;
- turn cosmology into scientific proof;
- turn symbolic visualization into canonical fact;
- use filial piety imagery as coercion;
- promise material reward or guaranteed spiritual results.

When character guidance is incomplete, prefer medium-wide, profile, silhouette, symbolic framing, or object-based imagery over invented facial details.

## Negative Constraints

Every prompt should include concise negative constraints appropriate to the scene.

Global defaults:

- no text;
- no subtitles;
- no logo;
- no watermark;
- no UI;
- no malformed anatomy;
- no extra limbs;
- no face distortion;
- no flicker;
- no abrupt costume changes;
- no unstable architecture;
- no modern objects in ancient scenes;
- no disrespectful religious depiction.

## Text-On-Screen Policy

Generated footage should contain no rendered text unless a separate approved visual production task explicitly requests it. Subtitles, captions, logos, UI overlays, watermarks, title cards, and readable private data are forbidden in default video prompts.

## Prompt QA

Video prompt QA must validate:

- prompt numbering is continuous;
- timelines start at zero and advance in exact 6-second blocks;
- there are no gaps or overlaps;
- the final rounded visual duration covers the estimated or actual audio duration;
- all TTS narration is mapped;
- each prompt has timeline, narration context, and video prompt fields;
- prompt text is standalone;
- scene sequences maintain continuity;
- visual modes are valid;
- canonical, traditional, symbolic, modern, and abstract modes are distinguished;
- no fake dialogue or lip-sync is introduced;
- no unsafe Buddhist depiction appears;
- no out-of-scope media render is claimed.
