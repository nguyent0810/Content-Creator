# 11 Knowledge Model

## Document Role

This document defines the permanent Knowledge Ontology of the Buddhist AI Studio. It describes how knowledge exists in the studio, how knowledge objects are identified, how they relate to one another, how they move through lifecycle states, how they preserve truth and lineage, and how they can be retrieved by future AI systems, databases, knowledge graphs, RAG systems, MCP servers, and publishing platforms.

This document is not an Engine. It does not research, write, design, produce, publish, optimize, review, or approve. It defines the semantic structure that all engines depend on. The Research Engine creates and verifies knowledge artifacts. The Content Engine turns approved knowledge into educational content. The Visual Engine represents knowledge visually. The Production Engine moves artifacts through workflow. The Growth Engine connects knowledge to audience pathways. The QA Engine evaluates integrity. The Master Agent orchestrates the system. The Knowledge Model defines the objects, relationships, metadata, lifecycle, graph structure, and retrieval logic that make those systems coherent.

The Knowledge Model must remain platform-independent. It must be understandable as Markdown documentation, implementable as relational tables, expressible as a property graph, indexable in a vector database, retrievable by RAG systems, usable by AI agents, and portable into future data systems not yet invented.

## Canonical Knowledge Rule

The permanent knowledge rule is:

**No public artifact may be treated as trustworthy unless its knowledge lineage can be traced from source to interpretation to artifact to approval to archive.**

If lineage is missing, the object may exist as a draft, idea, or raw note, but it cannot function as approved studio knowledge.

# PART 1 - Knowledge Philosophy

## Why Knowledge Exists

Knowledge exists to protect truth, preserve Buddhist integrity, support coherent education, and make the studio's work reusable across decades. A Buddhist media studio cannot operate on inspiration alone. It must know what it is saying, where the claim came from, what tradition it belongs to, what confidence it carries, how it has been interpreted, and where it has been used.

The studio's knowledge is not a pile of text. It is an interconnected system of scriptures, commentaries, terms, teachings, persons, places, stories, practices, virtues, research sources, citations, Knowledge Packets, series bibles, character bibles, visual assets, production records, publishing assets, QA decisions, archive records, and versions. Each object must have identity. Each relationship must be explicit. Each claim must be traceable.

Knowledge exists before content because content is a public expression of knowledge. If the knowledge is unclear, the content will drift. If the source lineage is missing, the writing may hallucinate. If the term standards are weak, translations may conflict. If the relationships are implicit, future agents will duplicate, contradict, or misroute work. The Knowledge Model prevents these failures by making the structure visible.

## Why Knowledge Precedes Content

Knowledge precedes content because Buddhist teachings require context. A script, short, article, podcast, course module, description, thumbnail, or community post may appear simple, but it may rest on doctrinal assumptions, historical claims, translation choices, tradition boundaries, symbolic meanings, and safety considerations. These must be known before public expression.

The Content Engine must never be asked to invent missing knowledge. The Visual Engine must never be asked to depict sacred or historical material without references. The Growth Engine must never be allowed to package a teaching without knowing what promise the knowledge can support. The QA Engine cannot evaluate truth if the source structure is absent. The Master Agent cannot route work responsibly if it does not know what objects exist and how they relate.

Knowledge-first production also protects viewers. Viewers may arrive in grief, confusion, devotion, curiosity, or vulnerability. They deserve teachings that are grounded, humble, and carefully framed. Knowledge must be stable before it becomes voice.

## Truth Over Generation

AI systems are powerful generators. They can produce plausible text, images, metadata, and structure quickly. Plausibility is not truth. The Knowledge Model exists to separate generated expression from verified knowledge.

Truth over generation means that every claim must have a status. A claim may be sourced, interpreted, uncertain, disputed, traditional, legendary, symbolic, modern reflection, rejected, or deprecated. Generated content cannot upgrade a claim's status. Only research, review, and governance can.

The Knowledge Model must therefore represent uncertainty as a first-class object property. It must not force false certainty for convenience. A knowledge graph that stores unsupported claims as equivalent to verified claims becomes dangerous. A retrieval system that serves uncertain material without warning can mislead future agents. A vector database that returns semantically similar but unapproved text can create hallucination. Truth over generation requires metadata, lifecycle, and QA state.

## Knowledge Stewardship

The studio acts as steward of Buddhist knowledge, not owner. It inherits teachings, traditions, translations, stories, symbols, and practices that belong to living communities and long histories. Stewardship requires humility, source discipline, cultural respect, and preservation.

Knowledge stewardship means the studio must not flatten Buddhist traditions into generic spirituality. It must distinguish scripture from commentary, commentary from scholarship, scholarship from editorial reflection, editorial reflection from audience response, and audience response from doctrine. It must also distinguish historical evidence from legend, devotional narrative, symbolism, and modern application.

Stewardship is also technical. Objects must be named, versioned, stored, linked, and archived. Sources must be preserved. Citations must point to claims. Visual assets must know what they depict. Character bibles must know who they represent and with what constraints. Archive records must show why an artifact was approved, revised, deprecated, or replaced.

## Long-Term Preservation

The Knowledge Model is designed for twenty or more years. Over that time, AI models will change, search systems will change, platforms will change, and the studio's library will grow. Without a stable knowledge ontology, future teams will inherit confusion.

Long-term preservation requires stable IDs, durable metadata, explicit relationships, version history, deprecation rules, archive records, and exportable formats. A knowledge object must not depend on one tool's interface. It should be portable into Markdown, JSON, CSV, relational databases, graph databases, vector stores, file systems, CMS platforms, and future memory systems.

Preservation also requires semantic clarity. It is not enough to save files. The system must know what a file is. Is it a scripture source, translation, commentary, draft Knowledge Packet, approved Knowledge Packet, visual reference, generated image, QA record, published episode, or deprecated asset? Files without object identity become unusable over time.

## Knowledge as Ethical Infrastructure

Knowledge structure is ethical infrastructure. If the studio cannot trace a claim, it may accidentally misrepresent the Dharma. If it cannot identify risk, it may harm vulnerable viewers. If it cannot track tradition, it may present one interpretation as universal. If it cannot distinguish approved from draft knowledge, it may publish unreviewed material.

The Knowledge Model protects truth by design. It makes safe behavior easier than unsafe behavior. It gives AI agents the context needed to avoid invention. It gives human reviewers the evidence needed to judge. It gives future systems the structure needed to retrieve responsibly.

Knowledge is not merely what the studio knows. It is how the studio remains accountable.

# PART 2 - Knowledge Ontology

## Ontology Overview

The ontology defines the canonical object classes of the Buddhist AI Studio. Each object class represents a type of knowledge or artifact that may exist in the system. Objects are not arbitrary files. They are typed entities with metadata, relationships, lifecycle status, and governance requirements.

Every object must have a unique ID, object type, name or label, language where applicable, status, version where applicable, created date, modified date, owner, source or lineage, confidence where applicable, risk where applicable, and relationships to other objects.

Objects may be conceptual, textual, visual, production-related, publishing-related, archival, or administrative. Some objects represent Buddhist knowledge. Some represent media outputs. Some represent evidence. Some represent memory and governance. The ontology must allow them to connect without collapsing their differences.

## Scripture

A Scripture is a canonical or tradition-recognized text used as a source of Buddhist teaching. It may include sutras, suttas, vinaya texts, abhidharma materials, Mahayana sutras, Pure Land scriptures, Zen texts, Vietnamese Buddhist texts, liturgical texts, or other recognized sources depending on tradition context.

Required metadata includes title, alternate titles, language, tradition, canon or collection, translator where applicable, edition, source status, citation format, rights status where relevant, and confidence level. A Scripture must never be represented as a single undifferentiated object when chapter, section, verse, passage, or story-level relationships are needed.

Scripture objects are high-authority sources but must be tradition-scoped. The ontology must not imply that every scripture is accepted identically across all Buddhist traditions.

## Chapter

A Chapter is a structural subdivision of a Scripture or major text. It may also represent phẩm, chapter, section, fascicle, book, or division depending on the text. Chapter objects allow citation, retrieval, and interpretation at a more precise level than the whole Scripture.

Required metadata includes parent Scripture, chapter number or label, title, language, translation source, sequence, citation identifier, and status. A Chapter may contain Verse, Story, Teaching, Concept, Person, Location, Event, and Practice references.

Chapter objects support precise retrieval and prevent vague scriptural references.

## Verse

A Verse is a smaller citable unit within a Chapter or Scripture. It may represent verse, passage, line, paragraph, gatha, prose segment, or numbered section depending on source structure. Not all scriptures have stable verse divisions; the ontology must allow uncertain or edition-specific units.

Required metadata includes parent Scripture, parent Chapter if applicable, unit identifier, translation, original language where available, source edition, citation, and confidence. A Verse may be quoted, paraphrased, interpreted, or referenced.

Verse objects require strict citation integrity. Public quotation must link to an approved Verse or equivalent source unit.

## Story

A Story is a narrative unit that may appear in scripture, commentary, history, legend, biography, or modern reflection. It may involve characters, events, locations, teachings, virtues, conflicts, or symbolic scenes.

Required metadata includes source, story type, tradition context, historical status, symbolic status, associated persons, associated concepts, associated teachings, and risk flags. Story type must distinguish canonical narrative, commentary narrative, historical account, legend, devotional story, parable, modern analogy, and editorial narrative.

Stories are powerful and therefore high-risk for category confusion. The ontology must prevent legendary stories from being retrieved as historical fact unless explicitly marked.

## Concept

A Concept is an abstract Buddhist or editorial idea such as karma, compassion, impermanence, mindfulness, emptiness, merit, rebirth, filial piety, Bodhisattva path, Pure Land, suffering, wisdom, generosity, ethical conduct, healing, grief, or non-attachment.

Required metadata includes preferred label, alternate labels, language variants, tradition scope, definition, related terms, source anchors, allowed explanation levels, common misconceptions, risk flags, and approved framing. Concepts may connect to Scriptures, Chapters, Verses, Stories, Teachings, Practices, Virtues, Questions, Knowledge Packets, and media artifacts.

Concepts are central graph nodes. They allow the library to become navigable by meaning rather than only by file name.

## Term

A Term is a language-specific expression for a Concept, Person, Scripture, Practice, or other object. Terms include Vietnamese, English, Sanskrit, Pali, Chinese, and future language labels. A Term may be preferred, alternate, deprecated, transliterated, translated, explanatory, or forbidden.

Required metadata includes term text, language, script, diacritics, pronunciation where useful, related concept, tradition, usage status, context notes, translation notes, and forbidden-use notes if applicable.

Terms protect consistency. The ontology must allow one Concept to have multiple Terms without treating all Terms as identical in usage.

## Person

A Person is a human or human-like figure represented in Buddhist history, scripture, legend, commentary, or studio content. It may include the historical Buddha before enlightenment, disciples, kings, householders, monastics, parents, teachers, translators, scholars, or modern figures.

Required metadata includes name, alternate names, type, tradition context, historical status, source references, roles, associated events, associated teachings, and representation rules. A Person may connect to Character Bible when visual or narrative representation is needed.

The Person object must distinguish historical figure, scriptural figure, legendary figure, symbolic figure, and modern person.

## Bodhisattva

A Bodhisattva is a specialized Person or sacred figure object representing a being associated with the Bodhisattva path or devotion. Examples may include Avalokiteshvara, Ksitigarbha, Manjushri, Samantabhadra, Maitreya, and tradition-specific figures.

Required metadata includes names across languages, tradition context, associated virtues, vows, scriptures, iconography, devotional practices, symbolic meanings, representation constraints, and risk flags. A Bodhisattva object may connect to Character Bible, Visual Assets, Practices, Concepts, and Scriptures.

Bodhisattva objects require high dignity controls because they often involve sacred imagery and devotional meaning.

## Buddha

A Buddha is a specialized sacred figure object representing Shakyamuni Buddha, Amitabha Buddha, Medicine Buddha, or other Buddhas recognized in relevant traditions. The ontology must distinguish historical Buddha, cosmic or devotional Buddha, and symbolic representation where appropriate.

Required metadata includes names, titles, tradition context, scriptures, associated practices, iconographic rules, historical status where applicable, doctrinal role, and representation constraints. Buddha objects connect to Teachings, Scriptures, Character Bibles, Visual Assets, Practices, Locations, Events, and Concepts.

Buddha objects require the highest visual and doctrinal dignity controls.

## Historical Figure

A Historical Figure is a Person whose existence or role is treated through historical evidence. This may include Buddhist masters, translators, rulers, scholars, monastics, or cultural figures. A Historical Figure object must include evidence type, confidence, dates where known, locations, associated works, and source references.

Historical Figure objects must distinguish scholarly evidence from tradition. A figure may be historically attested while some stories about them remain legendary.

The ontology must allow partial confidence rather than forcing binary true or false.

## Location

A Location is a geographic or conceptual place connected to Buddhist history, scripture, practice, production, or visual representation. It may include real places such as Bodh Gaya, Varanasi, Rajgir, Nalanda, Vietnamese temples, or symbolic places such as Pure Land or hell realms.

Required metadata includes name, type, coordinates where applicable, tradition context, historical status, symbolic status, associated events, persons, scriptures, practices, visual rules, and risk flags.

Location objects must distinguish geographic, historical, legendary, cosmological, symbolic, and production locations.

## Temple

A Temple is a specialized Location representing a Buddhist religious site, monastery, pagoda, shrine, or temple complex. Required metadata includes name, tradition, country, region, historical period, associated figures, practices, architecture notes, image rights where applicable, and cultural sensitivity notes.

Temple objects may connect to Visual Assets, Events, Practices, Persons, and community context. When real temples are represented, cultural respect and accuracy are required.

Temple objects must not be used as generic atmosphere without context when specificity matters.

## Event

An Event is an occurrence in scripture, history, legend, production, publishing, QA, or community life. Buddhist knowledge Events may include the Buddha's birth, enlightenment, first sermon, parinirvana, councils, translations, teachings, pilgrimages, rituals, or narrative events. Production Events may include publication, revision, QA approval, correction, or deprecation.

Required metadata includes event type, date or period, confidence, source, associated persons, locations, scriptures, concepts, and status. Events must distinguish historical event, scriptural event, legendary event, symbolic event, and production event.

Event objects support timelines and lineage.

## Teaching

A Teaching is a coherent unit of Buddhist instruction. It may be a doctrinal principle, ethical teaching, meditation instruction, devotional teaching, scriptural exposition, or modern reflection grounded in approved sources.

Required metadata includes source anchors, concepts, tradition scope, explanation level, audience maturity, risk, approved framing, common misconceptions, and related practices. A Teaching may derive from Scripture, Commentary, Research Source, or Knowledge Packet.

Teaching objects are the bridge between source knowledge and educational content.

## Practice

A Practice is a Buddhist or Buddhist-informed action such as meditation, chanting, recitation, mindfulness, generosity, dedication of merit, ethical precept observance, bowing, repentance, filial care, or compassion practice.

Required metadata includes tradition context, source support, purpose, required cautions, contraindications or boundaries, audience level, ritual status, devotional status, and safety notes. Practices may connect to Teachings, Virtues, Concepts, Persons, Scriptures, and media artifacts.

Practice objects require boundaries. The ontology must not allow practices to be retrieved as guaranteed solutions.

## Virtue

A Virtue is a wholesome quality cultivated or represented in Buddhist teaching. Examples include compassion, wisdom, patience, generosity, humility, filial piety, gratitude, diligence, truthfulness, equanimity, and loving-kindness.

Required metadata includes definition, associated concepts, practices, stories, figures, scriptures, and audience application. Virtues may connect to series themes, community reflections, and educational pathways.

Virtues are not generic inspirational labels. They must remain grounded in Buddhist context.

## Question

A Question is a viewer, editorial, research, or teaching inquiry. It may represent search intent, community confusion, doctrinal problem, production need, or learning objective.

Required metadata includes question text, language, intent type, audience stage, emotional state, risk, related concepts, source of question, frequency, and status. Questions may connect to Answers, Knowledge Packets, Episodes, Articles, Playlists, and Community Intelligence.

Question objects allow the studio to serve real learning needs without becoming audience-driven doctrine.

## Answer

An Answer is an approved response to a Question. It may be brief, extended, doctrinal, reflective, practical, or source-oriented. Answers must have source lineage and approval status when public-facing.

Required metadata includes parent Question, source support, confidence, tradition scope, safety notes, audience level, related Knowledge Packet, and usage status. An Answer may be used in community moderation, articles, scripts, or FAQs only within approved scope.

Answers must not exist as free-floating assertions.

## Research Source

A Research Source is any source used for evidence, context, interpretation, history, translation, or production knowledge. It may include scripture, commentary, scholarly book, journal article, reputable institutional page, translation, dictionary, interview, public-domain text, or internal source.

Required metadata includes title, author or institution, date, edition, publisher, URL or location, source type, tradition, reliability rating, rights status, language, citation format, and notes. Research Sources connect to References, Citations, Claims, Knowledge Packets, and QA records.

Research Source objects must support source hierarchy and reliability evaluation.

## Knowledge Packet

A Knowledge Packet is a structured, source-supported knowledge artifact used to guide production. It contains approved claims, uncertainties, citations, terminology, tradition scope, risk notes, and approved framing for a topic. This document defines the object type but does not create any specific packet.

Required metadata includes topic, object ID, version, status, owner, source list, confidence, risk class, related concepts, related scriptures, related questions, QA status, dependencies, and lifecycle. A Knowledge Packet may support Episodes, Shorts, Articles, Podcasts, Courses, Playlists, and Community responses.

Knowledge Packets are one of the primary interfaces between research and content.

## Series Bible

A Series Bible is the governing knowledge object for an ongoing or planned series. It defines series purpose, audience, learning pathway, tone, structure, naming rules, visual identity, concept map, dependencies, risk notes, and continuity rules.

Required metadata includes series ID, title, pillar, status, version, owner, audience maturity, related Knowledge Packets, related Concepts, related Episodes, visual rules, QA status, and lifecycle.

Series Bibles prevent series drift over time.

## Character Bible

A Character Bible is the governing object for visual and narrative representation of a recurring person, sacred figure, symbolic figure, or character type. It defines appearance, role, dignity constraints, emotional range, iconographic requirements, forbidden depictions, and visual references.

Required metadata includes character ID, represented Person or sacred figure, status, version, tradition context, visual references, usage scope, related Visual Assets, QA status, and risk class.

Character Bibles are required for recurring sacred or historically sensitive figures.

## Visual Asset

A Visual Asset is any image, reference, artwork, generated visual, graphic, thumbnail, style board, character reference, icon, color system, typography sample, or scene asset used in production. It may be draft, approved, public, deprecated, or archived.

Required metadata includes asset ID, type, format, source, generation method, rights status, associated objects, visual style, language if text appears, status, version, QA status, accessibility notes, and usage restrictions.

Visual Assets must connect to the objects they represent. A Buddha image must link to the Buddha object and relevant Character Bible. A temple image must link to Temple or Location.

## Production Asset

A Production Asset is any internal or final production file used to create a publishable artifact. It may include audio, edit files, captions, transcripts, project files, scene lists, production notes, or assembled packages. This document defines the object type but does not create production assets.

Required metadata includes asset ID, format, owner, source artifacts, version, status, dependencies, related Episode or media object, QA status where applicable, and archive location.

Production Assets preserve workflow lineage.

## Episode

An Episode is a long-form or primary media unit produced by the studio. It may belong to a Series and derive from one or more Knowledge Packets. Episode objects represent the published or production-level unit, not the script alone.

Required metadata includes episode ID, title field, series, content pillar, audience level, language, status, version, source packets, related concepts, related persons, related visuals, publishing package, QA approval, and archive record.

Episode objects connect knowledge to public learning.

## Short

A Short is a short-form media object derived from approved knowledge or an approved parent asset. It functions as entry point, bridge, reflection, clarification, or series connector.

Required metadata includes short ID, source packet or parent Episode, purpose, related concept, pathway target, risk class, script or text status if applicable, visual status, QA status, and publishing status.

Short objects must not be detached from learning pathways.

## Podcast

A Podcast is an audio-first media object. It may be adapted from an Episode, created from approved content, or structured as an independent audio asset. It must remain connected to source knowledge and audio-specific metadata.

Required metadata includes podcast ID, source packet or parent asset, episode number where applicable, transcript status, audio file, description, platform metadata, QA status, and archive record.

Podcast objects support listening pathways and accessibility.

## Article

An Article is a written public or internal educational object. It may explain a concept, support a video, host references, provide transcript context, or serve as a library node.

Required metadata includes article ID, source packets, related concepts, language, audience level, citation status, update status, QA status, and related media.

Articles must not be treated as unstructured blog posts. They are knowledge surfaces.

## Quote

A Quote is a short textual unit used for reference, reflection, visual display, or citation. It may be direct scripture quotation, translated passage, attributed quote, paraphrase, or original editorial reflection.

Required metadata includes quote text, quote type, source, attribution, language, translation status, citation, confidence, usage rights, and QA status. A Quote must never be used publicly without provenance.

Quote objects are high-risk because decontextualization is easy.

## Reference

A Reference is a link between an object and a Research Source. It records that a source was used for a particular object, topic, or claim. References may be broad or claim-specific.

Required metadata includes source ID, target object ID, reference purpose, page or passage where applicable, date accessed, confidence, and notes.

References support evidence but are not always precise enough for public citation.

## Citation

A Citation is a precise claim-supporting reference. It links a claim, quote, verse, teaching, or public statement to a source location. Citations must be specific enough for verification.

Required metadata includes cited object, source, passage, page, URL, edition, translation, access date where applicable, citation format, and confidence.

Citations are required for high-risk public claims.

## Glossary

A Glossary is a structured set of Terms and definitions. It may be global, series-specific, language-specific, or topic-specific. Glossaries connect Terms to Concepts, usage rules, translations, and deprecated forms.

Required metadata includes glossary ID, scope, language, version, owner, term list, status, QA status, and update date.

Glossaries support terminology consistency across agents and languages.

## Media Asset

A Media Asset is a public-facing or production-facing media object such as video, audio, image, caption file, transcript, PDF, web page, or interactive element. Media Asset is a broad class that may include Episode, Short, Podcast, Visual Asset, or Production Asset subtypes.

Required metadata includes media ID, format, duration or dimensions where applicable, language, rights, source, status, version, accessibility fields, QA status, and archive location.

Media Assets must be linked to knowledge and production lineage.

## Archive Record

An Archive Record preserves the final state, history, and lineage of an object or package. It includes storage location, version history, approvals, sources, outputs, publishing data, corrections, deprecation status, and maintenance triggers.

Required metadata includes archive ID, archived object ID, archive date, owner, storage path, version, checksum or integrity marker where feasible, QA record, and retrieval notes.

Archive Records make the system durable.

## Version

A Version is a specific state of an object at a point in time. Versions apply to documents, Knowledge Packets, Series Bibles, Character Bibles, assets, episodes, publishing packages, QA decisions, and archive records.

Required metadata includes version ID, object ID, version number, change summary, previous version, owner, date, reason, QA status, and supersession status.

Version objects allow the system to preserve change without confusion.

# PART 3 - Relationships

## Relationship Philosophy

Every meaningful relationship must be explicit. The studio must not rely on humans or AI agents to infer connections from file names, folder locations, or vague similarity. Relationships define how knowledge travels from source to public artifact and how future systems retrieve context responsibly.

Relationships may be hierarchical, evidentiary, interpretive, derivative, representational, operational, temporal, or governance-related. A Scripture contains a Chapter. A Chapter contains a Verse. A Verse supports a Teaching. A Teaching explains a Concept. A Concept is used by a Knowledge Packet. A Knowledge Packet supports an Episode. An Episode derives a Short. A Short points to a Playlist. A Playlist belongs to a Series.

Relationships must include direction, type, confidence, status, and where appropriate, scope or evidence.

## Core Relationship Types

Canonical relationship types include contains, part_of, cites, cited_by, supports, supported_by, interprets, interpreted_by, explains, explained_by, represents, represented_by, derives_from, derived_by, depends_on, required_by, related_to, contrasts_with, expands, summarizes, adapts, translates, localizes, uses_term, has_term, has_version, supersedes, deprecated_by, approved_by, rejected_by, archived_as, published_as, appears_in, features, depicts, references, answers, asks, belongs_to, sequences_before, sequences_after, and recommends.

The relationship list may expand, but new relationships must not duplicate existing meanings. Relationship names should be stable, lowercase where implemented, and machine-readable.

Every relationship must be clear enough for graph traversal.

## Scripture to Chapter

Relationship: Scripture contains Chapter. Chapter part_of Scripture.

This relationship defines structural hierarchy. It allows retrieval by text, chapter, section, or phẩm. The Chapter must inherit tradition context and source edition from Scripture while retaining its own citation identifier.

This relationship is required for scripture-based content and citation systems.

## Chapter to Verse

Relationship: Chapter contains Verse. Verse part_of Chapter.

This relationship enables precise quotation and passage-level retrieval. If the source lacks stable verse divisions, the relationship may connect Chapter to Passage or textual unit using the Verse class as flexible citable unit.

Verse relationships must preserve edition or translation context.

## Verse to Concept

Relationship: Verse supports Concept, mentions Concept, or illustrates Concept.

The type must be chosen carefully. A Verse that directly teaches karma supports the Concept. A Verse that includes a term may mention it. A narrative passage may illustrate a virtue without formally defining it.

This relationship must not overstate doctrine. QA may require evidence for support-level edges.

## Story to Teaching

Relationship: Story illustrates Teaching, contains Teaching, or is_interpreted_as Teaching.

The system must distinguish whether the teaching is explicit in the story or derived through interpretation. A parable may illustrate generosity. A legend may symbolize devotion. A historical account may contextualize a practice.

Story-to-Teaching relationships require story type and historical status.

## Concept to Term

Relationship: Concept has_term Term. Term labels Concept.

This relationship supports multilingual and terminology-aware retrieval. A Concept may have many Terms across languages and traditions. A Term may be preferred, alternate, deprecated, forbidden, or context-specific.

The system must not assume all terms are interchangeable in every context.

## Person to Character Bible

Relationship: Person represented_by Character Bible. Character Bible represents Person.

This relationship exists when a person or sacred figure needs recurring narrative or visual representation. It attaches dignity constraints, visual continuity, and usage rules to the person.

For Buddha and Bodhisattva objects, Character Bible relationships require elevated QA.

## Bodhisattva to Virtue

Relationship: Bodhisattva embodies Virtue or associated_with Virtue.

This relationship supports thematic retrieval and visual-symbolic consistency. For example, a Bodhisattva may be associated with compassion, wisdom, vow, protection, or filial care depending on tradition and source.

The relationship must be source-supported and tradition-aware.

## Buddha to Teaching

Relationship: Buddha teaches Teaching, associated_with Teaching, or represented_in Teaching.

The system must distinguish teachings attributed to Shakyamuni Buddha in scripture from devotional association with Amitabha, Medicine Buddha, or other Buddhas. A Buddha object may connect to Practices, Scriptures, Visual Assets, and Concepts.

Attribution requires citation discipline.

## Location to Event

Relationship: Location hosts Event, associated_with Event, or symbolizes Event.

This relationship supports historical timelines, pilgrimage context, visual planning, and documentary structure. A real location may host a historical event. A symbolic location may represent a teaching. A cosmological location may appear in scripture or devotional context.

The relationship must preserve historical and symbolic status.

## Teaching to Practice

Relationship: Teaching informs Practice. Practice applies Teaching.

This relationship helps the studio connect doctrine to lived application while preserving boundaries. A teaching on compassion may inform a compassion practice. A teaching on mindfulness may inform meditation. A teaching on merit may inform dedication practice.

Practice relationships require safety and tradition context.

## Question to Answer

Relationship: Question answered_by Answer. Answer answers Question.

The Answer must link to sources or approved Knowledge Packets. If the Answer is incomplete, uncertain, or tradition-specific, that status must be explicit.

Question-Answer relationships support community intelligence and future FAQ systems.

## Research Source to Citation

Relationship: Research Source cited_by Citation. Citation cites Research Source.

This relationship provides precise evidence. Citation objects may connect to Verse, Quote, Teaching, Knowledge Packet, Article, Episode, or QA finding.

Citations must include enough detail for verification.

## Knowledge Packet to Episode

Relationship: Knowledge Packet supports Episode. Episode derives_knowledge_from Knowledge Packet.

This relationship proves that public content is grounded in approved knowledge. An Episode may depend on multiple Knowledge Packets. A Knowledge Packet may support many Episodes and derivative formats.

If a Knowledge Packet is deprecated, dependent Episodes must be reviewed.

## Episode to Short

Relationship: Episode source_for Short. Short derives_from Episode.

This relationship supports short-form context and prevents decontextualization. A Short may also derive directly from a Knowledge Packet if no parent Episode exists.

Shorts must retain a pathway relationship to deeper content.

## Short to Playlist

Relationship: Short points_to Playlist, belongs_to Playlist, or bridges_to Playlist.

The relationship type should indicate function. A Short may belong to a shorts playlist, point to a long-form learning path, or bridge viewers into a series.

Short-to-playlist relationships must serve learning, not only retention.

## Playlist to Series

Relationship: Playlist organizes Series, belongs_to Series, or supports Series.

Playlists may represent learning pathways inside a Series or cross-series pathways. The relationship should identify sequence role, prerequisite status, and audience level.

Playlists are not content buckets. Their relationships must express learning function.

## Character to Visual Asset

Relationship: Character Bible governs Visual Asset. Visual Asset depicts Character Bible subject.

This relationship ensures visual continuity. Visual Assets must not depict sacred or recurring figures without reference to the governing Character Bible when one exists.

Visual Assets derived from a Character Bible inherit dignity and usage rules.

## Visual Asset to Episode

Relationship: Visual Asset used_in Episode. Episode uses Visual Asset.

This relationship tracks where visuals appear. If a Visual Asset is deprecated or corrected, dependent Episodes can be identified.

The relationship should include usage type: thumbnail, scene, background, reference, lower-third, illustration, or motion element.

## Episode to Thumbnail

Relationship: Episode has_thumbnail Visual Asset. Visual Asset thumbnail_for Episode.

Thumbnail relationships require Growth QA and Visual QA status. A thumbnail is a Visual Asset with discovery function and public promise.

If the thumbnail changes after QA approval, re-review may be required.

## Version Relationships

Relationship: Object has_version Version. Version version_of Object. Version supersedes Version. Version superseded_by Version.

Version relationships preserve change history. They must be applied to all critical objects, including Knowledge Packets, Series Bibles, Character Bibles, Visual Assets, Episodes, Articles, Publishing Packages, QA records, and governing documents where applicable.

Version relationships prevent wrong-version reuse.

## Archive Relationships

Relationship: Object archived_as Archive Record. Archive Record preserves Object.

Archive relationships connect active knowledge to long-term preservation. Every approved public artifact should have an Archive Record. Deprecated and rejected artifacts may also require archive records when their history matters.

Archive relationships make the system auditable.

# PART 4 - Metadata Standards

## Metadata Philosophy

Metadata is the control layer that makes knowledge retrievable, auditable, governable, and reusable. Without metadata, objects become ambiguous. A file may contain useful text, but the system cannot know whether it is draft, approved, deprecated, public, private, high-risk, source-supported, or safe to reuse. Metadata turns content into managed knowledge.

Every object must carry the minimum metadata required for its type. High-risk objects require richer metadata. Public objects require publication and QA metadata. Source objects require citation and reliability metadata. Visual objects require representation, rights, and accessibility metadata. Versioned objects require change history.

Metadata must be both human-readable and machine-readable. Field names should be stable, explicit, and platform-independent.

## Unique ID

Every object must have a Unique ID. The ID must be stable, machine-readable, and not dependent on file path alone. File paths can change. Titles can change. IDs preserve identity.

The canonical ID format should include object type prefix, normalized slug or semantic label, and numeric or date-based suffix where needed. Examples of pattern categories include scripture IDs, concept IDs, term IDs, person IDs, knowledge packet IDs, series IDs, episode IDs, visual asset IDs, citation IDs, archive IDs, and version IDs. This document defines the requirement, not a complete ID registry.

IDs must never be reused for different objects. If an object is deprecated, its ID remains reserved.

## Version

Version metadata records the specific state of an object. Version should include version number, previous version, change summary, change reason, changed by, date modified, QA status, and supersession status.

Versioning must be applied when meaning, structure, approval status, source support, visual representation, publication context, or metadata changes. Minor formatting may not require major version increment, but it should still be traceable for critical assets.

Version metadata protects against wrong-version publication and stale retrieval.

## Language

Language metadata identifies the language of the object and any related translation status. It should include language code, script where relevant, dialect or regional note when necessary, source language, target language, translation status, translator or agent, and localization notes.

Language is critical for Buddhist terminology. A concept may have different expression in Vietnamese, English, Sanskrit, Pali, Chinese, or other languages. The system must not treat translations as identical without review.

Language metadata supports multilingual retrieval, subtitles, localization, and cross-platform publishing.

## Tradition

Tradition metadata identifies the Buddhist tradition, school, lineage, textual context, or interpretive frame associated with an object. Values may include broad categories such as Mahayana, Theravada, Vajrayana, Pure Land, Zen, Vietnamese Buddhism, East Asian Mahayana, or specific lineage context where appropriate.

Tradition metadata must allow multiple values and scoped values. A concept may be broadly Buddhist but have tradition-specific interpretations. A scripture may belong to one tradition's canon. A practice may be common across traditions but performed differently.

Tradition metadata prevents false universality.

## Source

Source metadata identifies where an object comes from. For a Research Source, it identifies bibliographic origin. For a Knowledge Packet, it identifies supporting sources. For a Visual Asset, it identifies generation method, reference, creator, and rights. For an Episode, it identifies source packets and approved content artifacts.

Source metadata must distinguish primary source, secondary source, internal artifact, AI-generated artifact, human-authored artifact, translated artifact, and adapted artifact.

Source metadata is the foundation of lineage.

## Citation

Citation metadata provides precise evidence for claims, quotations, passages, and source-dependent interpretations. It should include source ID, passage or page, edition, translator, URL or archive location where relevant, access date, citation format, and confidence.

Citation metadata must be claim-specific for high-risk claims. A general source list is not enough when a public statement attributes words to a scripture or makes a historical claim.

Citations support QA and future verification.

## Confidence

Confidence metadata expresses how strongly the studio can rely on an object or claim. Confidence should be evidence-based and may include values such as high, medium, low, disputed, uncertain, or unverified. Numeric scores may be added in implementations, but qualitative labels must remain understandable.

Confidence must not be inflated by repetition or fluency. A claim repeated across many weak sources may still have low confidence. A claim supported by strong canonical or scholarly evidence may have high confidence.

Confidence metadata must travel downstream. A low-confidence source should not become high-confidence content without review.

## Risk

Risk metadata identifies potential harm, sensitivity, or governance complexity. Risk classes include low, medium, high, and critical. Risk reasons should be recorded, such as doctrinal complexity, death, grief, suicide, karma blame, hell realms, rebirth, medical boundary, mental health boundary, children, sacred imagery, historical uncertainty, cultural sensitivity, or platform risk.

Risk metadata determines review intensity and retrieval warnings. A high-risk object should not be served to a generation agent without constraints.

Risk metadata may increase when objects are adapted to public formats.

## Owner

Owner metadata identifies the responsible role, agent, team, or person for an object. Ownership includes maintenance responsibility, not personal possession.

Owner values may include Research Engine, Content Engine, Visual Engine, Production Engine, Growth Engine, QA Engine, Master Agent, human editor, Buddhist reviewer, archive owner, or specific role. Ownership may change across lifecycle states.

Unowned knowledge becomes unmanaged knowledge.

## Created

Created metadata records when the object first entered the system. It should include date, creator, source event, and initial status.

Created metadata supports lifecycle tracking, freshness review, and archive integrity. It also helps distinguish old knowledge from newly added or revised knowledge.

Creation date is not approval date. These must remain separate.

## Modified

Modified metadata records the last meaningful change. It should include date, modifier, change type, version change, and whether QA re-review is required.

Modified metadata is especially important for public and approved objects. If an object changes after approval, the system must know whether approval remains valid.

Modified metadata supports maintenance and freshness.

## Status

Status metadata identifies where the object sits in its lifecycle. Canonical statuses include requested, researching, draft, in review, approved, published, deprecated, archived, rejected, superseded, and on hold.

Status must be controlled. An object cannot declare itself approved without QA where QA is required. Published status requires publication metadata. Deprecated status requires reason and replacement where applicable.

Status determines allowed reuse.

## Dependencies

Dependencies metadata lists objects required for the current object to be valid. A script may depend on a Knowledge Packet. A visual asset may depend on a Character Bible. A playlist may depend on Episodes. A translation may depend on the source language version. A publishing package may depend on QA approval.

Dependencies must be version-specific where meaning matters. Depending on "the karma packet" is weaker than depending on a specific approved version.

Dependency metadata supports impact analysis.

## Lineage

Lineage metadata records the chain from source to artifact. It should identify source objects, research objects, interpretation objects, content objects, visual objects, QA records, publishing records, and archive records.

Lineage may be represented as relationships in a graph, metadata references, or both. The key requirement is that future systems can trace public output back to its knowledge foundation.

Lineage is mandatory for public assets.

## Lifecycle

Lifecycle metadata identifies the object's current lifecycle stage, allowed transitions, review requirements, maintenance triggers, and deprecation conditions.

Lifecycle metadata is more than status. Status says where the object is now. Lifecycle describes how it may move and what must happen next.

Lifecycle metadata supports workflow automation and governance.

## Metadata Completeness Levels

The ontology should support metadata completeness levels. Level 1 includes ID, type, title, status, and owner. Level 2 adds version, language, created, modified, dependencies, and source. Level 3 adds confidence, risk, citations, lineage, QA status, and lifecycle. Level 4 adds full graph relationships, rights, accessibility, freshness, deprecation, and archive links.

Draft internal objects may begin at lower completeness. Public or approved objects require higher completeness. High-risk objects require the highest relevant completeness.

Completeness level should be visible so future agents know whether an object is safe to use.

# PART 5 - Knowledge Lifecycle

## Lifecycle Overview

Knowledge moves through states. The canonical lifecycle is Requested, Researching, Draft, QA, Approved, Published, Deprecated, and Archived. Some objects may skip Published if they are internal, and some may be Rejected, Superseded, or On Hold. The lifecycle defines what actions are allowed and what trust level the object carries.

Lifecycle states are critical for AI retrieval. A RAG system must not retrieve draft knowledge as if approved. A graph traversal must not route deprecated terminology as current. A content agent must not use a rejected quote. The lifecycle must be visible to every engine.

Lifecycle state must be version-specific. Version 1 may be deprecated while Version 2 is approved.

## Requested

Requested means the object has been proposed or identified as needed. It does not yet contain verified knowledge. A requested object may be a topic, missing concept, needed Knowledge Packet, proposed Series Bible, requested Character Bible, or archive repair.

Required metadata includes requester, reason, intended use, related objects, risk pre-screen, and priority. Requested objects may be routed to Researching, Draft, Rejected, or Deferred.

Requested state is not approval to generate content.

## Researching

Researching means the object is under evidence gathering or verification. This state applies to sources, concepts, knowledge packets, historical claims, terminology, and high-risk relationships.

Required metadata includes research owner, source plan, source hierarchy, open questions, risk class, and expected output. Researching objects may contain raw notes, but raw notes must not be served as approved knowledge.

Researching state ends when a draft evidence artifact is ready for review or when the research is stopped.

## Draft

Draft means the object has structured content or metadata but has not been approved. Draft objects may be useful internally but must be clearly marked. A draft Knowledge Packet, draft Series Bible, draft Character Bible, draft glossary entry, or draft visual reference cannot govern public work until approved.

Required metadata includes version, owner, source references where applicable, unresolved issues, risk, and review needs.

Draft state must not be hidden from retrieval systems. It should be excluded from public-generation retrieval unless the task explicitly requests draft review.

## QA

QA means the object is under quality review. Review may include research QA, Buddhist QA, visual QA, production QA, growth QA, safety QA, accessibility QA, or brand QA depending on object type.

Required metadata includes submitted version, review domains, reviewers, findings, scores, decision, required actions, and status. QA may return Approved, Conditional Approval, Major Revision Required, Rejected, Emergency Hold, or Escalated.

QA state protects the boundary between draft and trusted knowledge.

## Approved

Approved means the object has passed required review for a defined scope. Approval must identify version, scope, reviewer, date, confidence, risk, and usage limits.

Approved objects may be retrieved for production according to their scope. A Knowledge Packet approved for internal planning may not be approved for public quotation. A Visual Asset approved as reference may not be approved as thumbnail. A Series Bible approved as draft architecture may not govern published series.

Approval is not universal unless explicitly stated.

## Published

Published means the object or its derivative is publicly available. Published status applies to Episodes, Shorts, Podcasts, Articles, Quotes, Playlists, Website pages, Community posts, and public reference materials.

Required metadata includes platform, URL or location, publication date, public version, QA approval reference, publishing package, archive record, and monitoring plan.

Published objects remain subject to correction, maintenance, deprecation, and archive updates.

## Deprecated

Deprecated means the object should no longer be used for new work without review. Deprecation may occur because the object is outdated, superseded, inaccurate, unsafe, visually inconsistent, inaccessible, or no longer aligned with governing standards.

Required metadata includes deprecation reason, date, authority, replacement object where applicable, affected dependencies, and reuse restrictions.

Deprecated objects must remain retrievable for audit but excluded from default generation.

## Archived

Archived means the object is preserved with its metadata, lineage, versions, approvals, and storage location. Archive may apply to approved, published, deprecated, rejected, or superseded objects.

Required metadata includes archive record, storage path, integrity marker where feasible, related versions, QA records, publication data, and retrieval notes.

Archived status does not necessarily mean current. It means preserved.

## Rejected

Rejected means the object, claim, relationship, visual, quote, or artifact failed review and should not be used. Rejection must include reason, evidence, reviewer, date, and future-use instructions.

Rejected objects are important knowledge. They prevent future agents from repeating known failures.

Rejected objects should be excluded from generation retrieval except when the task is QA, audit, or avoidance.

## Superseded

Superseded means a newer object version or replacement object should be used. Superseded objects may remain accurate historically but no longer represent the current standard.

Required metadata includes replacement ID, supersession reason, date, and migration notes.

Supersession supports evolution without erasing history.

## On Hold

On Hold means the object cannot progress due to unresolved issue. Reasons may include missing source, doctrinal conflict, safety concern, rights uncertainty, human review need, or version conflict.

Required metadata includes hold reason, owner, required action, date placed on hold, and escalation path.

On Hold objects must not be treated as approved or abandoned.

# PART 6 - Knowledge Integrity

## Integrity Philosophy

Knowledge integrity means that the studio's knowledge remains truthful, traceable, current, scoped, and recoverable. Integrity is not a single check. It is the combined result of source discipline, metadata, relationships, versioning, QA, archive, conflict resolution, and maintenance.

The Knowledge Model must make integrity visible. An agent retrieving an object should know whether it is approved, uncertain, high-risk, deprecated, source-supported, public, internal, or draft. Hidden integrity status creates hallucination risk.

Integrity applies to all object types. A term can lose integrity if translated carelessly. A visual asset can lose integrity if detached from representation rules. A quote can lose integrity if attribution is uncertain. An episode can lose integrity if its source packet is deprecated.

## Truth Preservation

Truth preservation requires that claims remain connected to evidence and that uncertainty remains visible. The studio must preserve what is known, how it is known, what is interpreted, and what is not known.

Truth preservation prohibits silent transformation of cautious research into confident content. If a Knowledge Packet says a historical claim is uncertain, downstream scripts and articles must not present it as fact. If a story is legendary, visual and narrative objects must not classify it as historical without review.

Truth preservation also requires correction. When evidence changes or errors are found, the system must update affected objects and preserve correction history.

## Lineage

Lineage is the chain of dependency and derivation. It answers: where did this knowledge come from, how was it interpreted, where was it used, who approved it, and where is it archived?

Lineage must be represented through relationships and metadata. Source objects support citations. Citations support Knowledge Packets. Knowledge Packets support Episodes. Episodes derive Shorts. Visual Assets depict Persons or Concepts. QA records approve artifacts. Archive Records preserve them.

Lineage enables impact analysis. If a source is found unreliable, the studio can identify dependent objects.

## Auditability

Auditability means that a future reviewer can reconstruct the basis of an object. Auditability requires source records, citations, version history, QA findings, owner records, decision logs, and archive locations.

Auditable knowledge can be defended or corrected. Unauditable knowledge becomes a liability. Public-facing high-risk objects must have strong auditability.

Auditability must be maintained even when tools change. Exportable metadata and stable IDs are required.

## Versioning

Versioning protects change. Every material change should create or update a Version object. Material changes include changes to claims, citations, interpretation, terminology, risk, status, visual representation, public packaging, or QA decision.

Versioning must distinguish current, superseded, deprecated, and rejected versions. The system should allow retrieval of historical versions for audit while preventing accidental reuse.

Versioning is especially important for long-running series and multilingual assets.

## Conflict Resolution

Knowledge conflicts occur when sources disagree, traditions interpret differently, translations vary, historical evidence is uncertain, or prior studio artifacts contradict new findings. The ontology must represent conflict rather than hiding it.

Conflict metadata should identify conflicting objects, conflict type, evidence, affected claims, severity, and resolution status. Resolution options include tradition scoping, multiple interpretations, confidence downgrade, claim removal, further research, QA escalation, or deprecation.

Conflicts are not failures. Concealed conflicts are failures.

## Deprecation

Deprecation protects the system from outdated or unsafe knowledge. Deprecated objects remain in the archive but are excluded from default retrieval. The system must identify why deprecation occurred and what replaces the object.

Deprecation may apply to Terms, Visual Assets, Quotes, Knowledge Packets, Series Bibles, Episodes, Articles, Templates, Sources, and relationships. Relationship deprecation is important when a previously assumed connection is later judged inaccurate.

Deprecation must propagate to dependent objects through impact analysis.

## Freshness

Freshness indicates whether an object remains current enough for its use. Freshness depends on object type. Core Buddhist concepts may remain stable, but translations, scholarship, links, captions, visual standards, platform metadata, and safety guidance may change.

Freshness metadata should include last reviewed date, review cadence, triggers, and freshness status. High-risk or high-traffic objects require more frequent review.

Freshness prevents approved objects from becoming stale.

## Integrity Gates

Integrity Gates are required checks before object promotion. Requested to Researching requires scope. Researching to Draft requires source structure. Draft to QA requires metadata completeness. QA to Approved requires review decision. Approved to Published requires publishing package. Published to Archived requires archive record. Deprecated requires reason and dependency review.

Integrity Gates should be machine-checkable where possible and human-reviewable where necessary.

The Master Agent must not promote objects without required gates.

# PART 7 - Knowledge Graph

## Graph Architecture

The Knowledge Graph is the semantic representation of the ontology. It stores objects as nodes and relationships as edges. Nodes carry metadata. Edges carry relationship type, direction, confidence, status, source, and scope. The graph allows traversal across scriptures, concepts, terms, sources, media artifacts, visual assets, QA decisions, and archive records.

The graph must support both human knowledge navigation and machine retrieval. A human editor may explore all assets related to filial piety. An AI agent may retrieve approved sources for karma. A QA reviewer may trace a quote to its citation. A growth strategist may identify all beginner pathways linked to mindfulness. A maintenance process may find all assets dependent on a deprecated Knowledge Packet.

The graph should be implementable in Neo4j or any property graph system, but not dependent on one platform.

## Nodes

Nodes are instances of ontology object classes. Each node must have unique ID, label, type, status, version where applicable, language, tradition where applicable, owner, confidence where applicable, risk where applicable, and timestamps.

Nodes may have multiple labels in graph implementations. For example, Ksitigarbha may be labeled Person and Bodhisattva. Shakyamuni may be labeled Person, Historical Figure, and Buddha depending on representation needs. A public video may be labeled Media Asset and Episode.

Multiple labels must not erase subtype rules. Sacred figure rules still apply.

## Edges

Edges are typed relationships between nodes. Every edge must have direction and meaning. Some edges are structural, such as contains. Some are evidentiary, such as cites. Some are derivative, such as derives_from. Some are governance-related, such as approved_by. Some are semantic, such as related_to or contrasts_with.

Edges should include metadata: confidence, source, status, created date, owner, and notes. High-risk edges may require QA. For example, an edge claiming that a Verse supports a Concept may require source review.

Edges can also be deprecated. A wrong relationship must be retired without deleting history.

## Traversal

Traversal is the process of moving through the graph. The graph should support common traversal patterns:

Scripture to Chapter to Verse to Concept to Knowledge Packet to Episode.

Concept to Term to Glossary to Article to Playlist.

Bodhisattva to Virtue to Practice to Episode to Community Question.

Character Bible to Visual Asset to Episode to Thumbnail.

Research Source to Citation to Knowledge Packet to Published Asset.

Deprecated Source to affected Knowledge Packets to affected Episodes.

Traversal must respect status and risk filters. Default retrieval should prefer approved current objects and exclude draft, rejected, deprecated, or high-risk unscoped material unless specifically requested.

## Discovery

Graph discovery helps users and agents find meaningful relationships. Discovery may identify unexplored concepts, missing prerequisites, related teachings, repeated viewer questions, weakly sourced areas, or unused approved assets.

Discovery must not automatically create content ideas when the task forbids content ideation. It may identify structural gaps, dependencies, or maintenance needs. Any production planning must route through the appropriate engines.

Discovery is a knowledge function, not a license to generate.

## Semantic Search

Semantic search retrieves objects by meaning rather than exact words. It is useful for viewer questions, concept retrieval, and cross-language discovery. However, semantic similarity can be dangerous if it ignores status, source, tradition, or confidence.

The Knowledge Graph must work with semantic search by providing filters and grounding. A vector search result should be checked against graph metadata before use. Approved objects should rank above drafts. Current objects should rank above deprecated objects. Tradition-specific results should match the task context.

Semantic search should retrieve candidates; the graph determines trust.

## Future Neo4j Compatibility

For Neo4j or similar property graph implementation, ontology object classes should map to node labels. Relationship types should map to uppercase or consistent edge labels. Metadata should map to node and edge properties. IDs should be indexed. Status, type, language, tradition, confidence, risk, and version should be queryable.

Example conceptual mappings:

Scripture node contains Chapter node.

Chapter node contains Verse node.

Verse node supports Concept node.

Concept node has_term Term node.

KnowledgePacket node supports Episode node.

VisualAsset node depicts Person node.

Episode node approved_by QARecord node.

Episode node archived_as ArchiveRecord node.

The implementation must preserve relationship direction and metadata.

## Graph Governance

Graph changes require governance. Adding a node may be low-risk. Adding a high-confidence doctrinal edge may be high-risk. Deprecating a source may affect many assets. The Master Agent must route graph changes through appropriate review.

The graph must maintain change logs. It should be possible to know when an edge was created, who created it, what evidence supports it, and whether QA approved it.

A knowledge graph without governance becomes a hallucination graph.

# PART 8 - Retrieval Strategy

## Retrieval Philosophy

Retrieval is how future AI systems, human collaborators, and production workflows access knowledge. Retrieval must be precise enough to protect truth and flexible enough to support discovery. The studio must not retrieve knowledge as undifferentiated text. It must retrieve objects with metadata, relationships, status, confidence, risk, and lineage.

The default retrieval rule is: **retrieve the safest current approved object that matches the task context, then retrieve supporting lineage and constraints.** Retrieval should not begin with the most semantically similar text if that text is draft, deprecated, high-risk, or unsupported.

Retrieval must be task-aware. A Research Agent needs sources and citations. A Content Agent needs approved Knowledge Packets, audience level, and terminology. A Visual Agent needs Character Bibles, Visual Assets, and dignity constraints. A QA Agent needs full lineage and version history. A Growth Agent needs audience pathways and trust constraints. The Master Agent must decide retrieval scope.

## Keyword Retrieval

Keyword retrieval finds exact terms, titles, IDs, names, citations, and known phrases. It is essential for scriptures, terms, file names, source titles, quotes, and stable identifiers. Keyword retrieval is precise but brittle because viewers and agents may use different language for the same concept.

Keyword retrieval should search preferred terms, alternate terms, deprecated terms, transliterations, Vietnamese terms, English terms, Sanskrit or Pali terms, scripture titles, person names, and IDs. Results must include object status and usage notes.

Keyword retrieval is especially important for quote verification. A direct quote should be matched exactly or with controlled translation context.

## Semantic Retrieval

Semantic retrieval finds meaning-based matches. It helps when a user asks a natural-language question or when an agent needs related concepts. Semantic retrieval can connect "how to stop blaming myself for suffering" to karma, compassion, non-blame, grief, and ethical responsibility.

Semantic retrieval must be constrained by metadata. It should not retrieve unapproved reflections as doctrine or tradition-specific interpretations as universal. It should return candidate objects with confidence and status.

Semantic retrieval is powerful for discovery but must be grounded by graph and QA metadata.

## Hybrid Retrieval

Hybrid retrieval combines keyword and semantic search. This should be the default for most AI workflows. Keyword search provides precision. Semantic search provides recall. Graph filters provide trust and context.

A hybrid retrieval pipeline may search IDs and titles first, retrieve exact term matches, retrieve semantically related concepts, filter by status and language, expand through graph relationships, attach citations, and return ranked context packages.

Hybrid retrieval should include negative filters for rejected, deprecated, draft, or restricted objects unless the task explicitly requests audit or review.

## Context-Aware Retrieval

Context-aware retrieval uses the task context to select appropriate objects. Context includes audience maturity, language, tradition, format, risk, series, requested output, forbidden output, and production state.

For beginner content, retrieval should include definitions, safe explanations, common misconceptions, and foundational pathways. For advanced scripture study, retrieval should include primary sources, commentary, translation notes, and scholarly context. For grief content, retrieval should include safety boundaries and compassionate language rules.

Context-aware retrieval prevents the right object from being used in the wrong way.

## Series-Aware Retrieval

Series-aware retrieval selects knowledge based on Series Bible, series continuity, episode sequence, naming rules, visual identity, and prior decisions. A series may have approved interpretations, recurring terms, visual standards, and audience assumptions.

When retrieving for a series, the system should load the Series Bible, related Knowledge Packets, prior episodes, series glossary, character bibles, visual references, and QA precedents. It should also retrieve unresolved series risks.

Series-aware retrieval prevents drift across multi-year production.

## Character-Aware Retrieval

Character-aware retrieval selects Character Bibles, Person objects, sacred figure metadata, visual references, iconographic notes, dignity rules, and usage history. It is required whenever a recurring figure or sacred person appears in narrative or visual work.

For Buddha and Bodhisattva objects, retrieval must include sacred imagery constraints, tradition context, associated virtues, source references, and forbidden depictions.

Character-aware retrieval prevents visual and narrative inconsistency.

## Tradition-Aware Retrieval

Tradition-aware retrieval filters and scopes knowledge according to Buddhist tradition. If a task concerns Pure Land, retrieval should prioritize Pure Land-relevant scriptures, practices, terms, and interpretations. If a task is general Buddhist education, retrieval should avoid tradition-specific claims unless clearly framed.

Tradition-aware retrieval must support multiple traditions without forcing false equivalence. It should return tradition labels and interpretation differences.

Tradition awareness is essential for doctrinal humility.

## Risk-Aware Retrieval

Risk-aware retrieval attaches safety and QA constraints to high-risk objects. If a query touches suicide, grief, death, abuse, illness, karma blame, hell realms, miracles, children, or medical/mental health boundaries, retrieval must include safety rules and escalation requirements.

Risk-aware retrieval should prefer approved safe framing and exclude sensational or unreviewed material. It should return warnings when retrieved objects require human review or QA.

Risk-aware retrieval protects vulnerable viewers.

## Retrieval Output Package

A retrieval output package should include selected objects, object IDs, status, version, confidence, risk, language, tradition, citations, relationship path, usage limits, and missing-context warnings.

The package should distinguish required context from optional context. It should identify if any object is draft, deprecated, superseded, or restricted.

Retrieval output should be machine-readable enough for agents and human-readable enough for reviewers.

## Retrieval Failure

Retrieval failure occurs when the system cannot find approved knowledge sufficient for the task. The Master Agent must treat retrieval failure as a decision point. It may route to Research Engine, ask for clarification, reduce scope, use a lower-confidence object with explicit limits for internal work, or stop.

Retrieval failure must never be solved by invention.

Failed retrieval should be logged as a possible knowledge gap.

# PART 9 - Future AI Compatibility

## Compatibility Philosophy

The Knowledge Model must support future AI systems without depending on current implementation details. AI systems may use RAG, vector databases, knowledge graphs, long-term memory, MCP servers, enterprise CMS platforms, agentic workflows, or future retrieval systems. The ontology should remain stable across all of them.

Future AI compatibility requires structured objects, explicit metadata, stable IDs, relationship semantics, lifecycle status, versioning, and exportable records. AI systems should not consume raw documents without knowing object type and trust status.

The goal is not only to help AI retrieve more. It is to help AI retrieve responsibly.

## RAG Compatibility

Retrieval-Augmented Generation systems require chunks. The Knowledge Model must define how chunks relate to objects. A chunk from a Scripture, Knowledge Packet, QA record, or Article must carry object ID, source, status, version, language, tradition, confidence, risk, and citation metadata.

RAG systems must not chunk away context. A passage about karma should include risk notes and approved framing. A legendary story should include historical status. A quote should include attribution confidence.

RAG output should include citations and object IDs so generated content can be audited.

## Vector Database Compatibility

Vector databases store embeddings for semantic retrieval. The Knowledge Model must ensure that every embedded item includes metadata filters. Embeddings should be created for approved objects, draft objects only when needed for review, and deprecated objects only with clear exclusion flags.

Vector metadata should include object type, ID, status, version, language, tradition, risk, confidence, owner, and related concept IDs. This allows retrieval systems to filter before generation.

Vector similarity should never be treated as approval.

## Knowledge Graph Compatibility

Knowledge graph compatibility requires stable node classes, relationship types, and metadata properties. The ontology should map cleanly to graph databases such as Neo4j, RDF-like triples where appropriate, and future graph systems.

Graph systems should support relationship traversal, dependency impact analysis, concept discovery, source lineage, and QA audit. They should also support edge status and confidence.

Graph compatibility allows the studio to reason over relationships, not just retrieve text.

## LLM Memory Compatibility

LLM memory systems may store persistent facts, preferences, prior decisions, and context. The Knowledge Model must prevent ungoverned memory from becoming authority. Only approved and scoped knowledge should enter durable agent memory as binding context.

Memory entries must include source, status, version, and expiration or freshness review where appropriate. Temporary conversation memory must not become canonical knowledge without promotion.

LLM memory must remain subordinate to the Knowledge Model and QA.

## MCP Compatibility

Model Context Protocol servers or future tool servers may expose knowledge resources to agents. The Knowledge Model must support MCP resources such as object lookup, graph traversal, citation retrieval, glossary lookup, version history, QA status, and archive retrieval.

MCP resources should return structured metadata with content. They should not expose raw text without status and usage constraints. Access rules may restrict draft, high-risk, or sensitive objects.

MCP compatibility allows specialized tools to serve governed knowledge.

## Agentic Systems Compatibility

Agentic systems require clear contracts. The Knowledge Model gives agents object types, relationships, lifecycle states, and retrieval rules. Agents must know what they may read, what they may use, what they may modify, and what requires QA.

Agentic systems should use Knowledge Model metadata to plan tasks. A Content Agent should detect that a Knowledge Packet is missing. A Visual Agent should detect that a Character Bible is required. A QA Agent should detect missing citations. A Growth Agent should detect pathway relationships.

Agentic autonomy must be constrained by ontology and governance.

## Enterprise CMS Compatibility

An enterprise CMS may store articles, videos, metadata, assets, workflows, and publishing packages. The Knowledge Model should map object classes to CMS content types and relationships to reference fields.

CMS compatibility requires stable IDs, content type schemas, versioning, publication status, localization support, access control, and archive integration. The CMS should not become the ontology; it should implement part of it.

If CMS limitations prevent full graph expression, external relationship records must preserve ontology integrity.

## Future Search Systems

Future search systems may combine keyword, semantic, graph, behavior, personalization, and AI summarization. The Knowledge Model must ensure that search systems can distinguish approved knowledge from drafts, tradition-specific from general, high-confidence from uncertain, and current from deprecated.

Search systems should return context, not only answers. They should show source, confidence, and related pathways.

Future search must support humility.

## Interoperability Standards

The Knowledge Model should be exportable into JSON, JSON-LD, CSV, Markdown frontmatter, relational tables, graph database import files, and vector metadata. Interoperability protects the studio from tool lock-in.

Core fields must be stable across exports: ID, type, label, status, version, language, tradition, source, confidence, risk, owner, created, modified, dependencies, lineage, lifecycle.

Interoperability is long-term preservation.

# PART 10 - Knowledge Constitution

## Constitutional Role

The Knowledge Constitution defines the immutable principles governing all knowledge objects, relationships, retrieval systems, and future implementations. It is the ethical and structural foundation of the ontology.

The Constitution does not replace the Project PRD, Brand Bible, Buddhist Guide, QA Engine, or Master Agent. It expresses how their standards become knowledge architecture. When implementation convenience conflicts with this Constitution, the Constitution controls.

The studio's knowledge must remain worthy of the teachings it carries.

## Truth

Truth is the first principle. Every knowledge object must distinguish verified fact, sourced teaching, interpretation, tradition, legend, symbolism, modern reflection, uncertainty, and rejection. The system must not treat all text as equal.

Truth requires source lineage. It requires citation. It requires confidence metadata. It requires correction when wrong. It requires refusing to generate unsupported claims.

The Knowledge Model exists to make truth operational.

## Compassion

Compassion shapes knowledge design. Objects that touch suffering, grief, death, karma, family conflict, trauma, illness, suicide, rebirth, hell realms, and devotional hope must carry risk metadata and safe framing.

Compassion means the system should not retrieve harmful language by default. It should not serve fear-based claims as engagement material. It should not allow vulnerable viewers to become targets of ungoverned content.

Compassion is a retrieval constraint and a metadata requirement.

## Traceability

Traceability means every public artifact can be followed back to its sources, interpretations, versions, approvals, and archive records. Traceability is required for trust, correction, reuse, and future AI governance.

Traceability must survive platform changes and tool migrations. Stable IDs, metadata exports, graph relationships, and archive records are required.

Untraceable knowledge is not approved knowledge.

## Stewardship

Stewardship means Buddhist knowledge is handled with humility and respect. The studio must preserve tradition context, avoid false universality, distinguish sacred from editorial, and represent living traditions with care.

Stewardship applies to textual, visual, audio, community, and production knowledge. It also applies to deprecated and rejected objects, because future agents must learn what not to repeat.

The studio is a caretaker of knowledge, not an owner of the Dharma.

## Transparency

Transparency means the system should reveal status, confidence, uncertainty, source, and scope. AI agents and human collaborators should not have to guess whether an object is approved or draft, current or deprecated, general or tradition-specific.

Transparency also applies to public correction. When meaningful errors affect public assets, the knowledge system must record corrections and support honest communication.

Transparency supports humility.

## Future-Proofing

Future-proofing means the ontology must remain useful across twenty or more years of changing technology. The model must not depend on one file system, one AI model, one database, one platform, or one production workflow.

Future-proofing requires stable concepts, portable metadata, extensible relationships, deprecation rules, versioning, and interoperability. It also requires restraint: not every new tool should redefine the ontology.

The Knowledge Model should evolve by extension, not by abandonment.

## Machine-Readable and Human-Readable

The ontology must serve both machines and humans. Machines need stable IDs, types, properties, statuses, and relationships. Humans need clear language, definitions, examples of relationship logic, and governance principles.

If the system is only human-readable, automation will fail. If it is only machine-readable, editorial judgment and Buddhist humility may be lost.

Both forms are required.

## Platform Independence

Knowledge must not be trapped in YouTube, a CMS, a vector database, a graph database, a document folder, or any single vendor system. These tools may implement the model, but none should define it.

Platform independence requires export, backup, stable IDs, and semantic documentation.

The studio's knowledge must outlive its tools.

## Immutable Knowledge Rules

No public claim without lineage.

No scripture attribution without citation.

No direct quote without provenance.

No doctrinal statement without tradition awareness.

No historical claim without historical status.

No visual depiction without represented object linkage.

No recurring character without representation governance.

No approved object without version.

No deprecated object in default retrieval.

No high-risk object without risk metadata.

No generated artifact treated as knowledge without review.

No knowledge object without owner.

No public asset without archive record.

## Final Knowledge Standard

Before any object becomes part of the studio's trusted knowledge system, the studio must be able to answer:

What is this object?

Where did it come from?

What does it mean?

What sources support it?

What tradition or context does it belong to?

How confident are we?

What risks does it carry?

What does it relate to?

Who owns it?

What version is current?

Who approved it?

Where has it been used?

Where is it archived?

When should it be reviewed?

If these questions cannot be answered, the object is not trusted knowledge. It may be a draft, raw note, candidate, or artifact, but it is not yet part of the approved knowledge foundation of the Buddhist AI Studio.

# PART 11 - Implementation Profiles

## Purpose of Implementation Profiles

Implementation Profiles describe how the ontology can be expressed in different technical systems while preserving the same semantics. The Knowledge Model is platform-independent, but future teams will need practical mappings. These profiles are not workflows and not engines. They are implementation guidance for databases, files, graphs, vector stores, CMS platforms, and AI tool layers.

Every implementation must preserve object identity, metadata, lifecycle, relationships, versioning, and archive linkage. A system that stores content but loses status is incomplete. A system that stores embeddings but loses citations is unsafe. A system that stores files but loses relationships is not a knowledge model.

Implementation may vary. Semantics must not.

## Markdown Profile

Markdown is useful for human-readable governing documents, bibles, packets, review records, and archive notes. Markdown objects should use consistent headings, optional frontmatter, stable IDs, version notes, related object links, and status fields.

Markdown alone is not enough for large-scale graph operations unless supported by indexes or metadata extraction. However, Markdown is durable, readable, portable, and easy to preserve.

The Markdown profile should be used for documents requiring human judgment and editorial review.

## JSON Profile

JSON is useful for machine-readable object records, metadata exports, API responses, RAG chunks, and MCP resources. JSON records should include canonical fields such as id, type, label, status, version, language, tradition, confidence, risk, owner, source_ids, relationship_ids, lifecycle, and timestamps.

JSON should avoid embedding large unstructured text without metadata. Text content should be linked to source fields, chunk IDs, or file references.

JSON supports portability and automation.

## Relational Profile

A relational database can represent object tables, relationship tables, version tables, citation tables, and archive tables. This profile is useful for structured queries, reporting, dashboards, and governance checks.

Core tables may include objects, object_metadata, relationships, sources, citations, versions, qa_records, archive_records, and lifecycle_events. Relationship tables must preserve direction and type.

Relational systems are strong for consistency but may need graph extensions for deep traversal.

## Graph Profile

A graph database expresses ontology naturally through nodes and edges. It is strong for traversal, dependency analysis, recommendation, concept mapping, source lineage, and impact analysis.

Graph implementation should include node labels for object types, edge labels for relationship types, and properties for status, confidence, risk, version, language, and tradition.

Graph systems must include governance controls so unapproved edges do not become trusted knowledge.

## Vector Profile

A vector database stores embeddings for semantic retrieval. The vector profile must attach robust metadata to every embedding. The embedded text should reference object ID, chunk ID, source object, status, version, language, tradition, confidence, risk, and retrieval restrictions.

Embedding generation should prefer approved and current objects. Draft, rejected, and deprecated objects may be embedded only for restricted review or audit use.

Vector retrieval must be filtered and grounded before generation.

## CMS Profile

A CMS may manage published articles, pages, media, transcripts, descriptions, and metadata. CMS content types should map to ontology object types. Relationship fields should connect articles to concepts, sources, episodes, series, and archive records.

CMS implementations often prioritize publishing convenience. The studio must ensure CMS workflows do not bypass QA, versioning, or source lineage.

The CMS should implement the Knowledge Model, not replace it.

## File System Profile

A file system may store source files, Markdown documents, media assets, exports, archives, and working files. File paths should be meaningful but never treated as the only identity system.

Folders may reflect object type, status, series, language, or lifecycle, but stable IDs must still exist inside metadata. Moving a file should not change its object identity.

File systems are practical but require discipline to remain knowledge-aware.

# PART 12 - Object Governance Matrix

## Purpose of Governance Matrix

The Object Governance Matrix defines minimum requirements by object class. Different objects carry different risks. A Term requires terminology control. A Quote requires provenance. A Visual Asset requires representation and rights metadata. A Knowledge Packet requires source lineage and QA. An Episode requires production, publishing, and archive records.

The matrix prevents overprocessing low-risk objects and underprocessing high-risk objects. It also helps future systems validate completeness automatically.

Governance requirements may increase based on risk.

## High-Governance Objects

High-governance objects include Scripture, Verse, Quote, Knowledge Packet, Series Bible, Character Bible, Buddha, Bodhisattva, Practice, Teaching, Episode, Visual Asset depicting sacred subjects, Publishing Package, QA Record, and Archive Record.

These objects require strong metadata, source lineage, versioning, QA status, risk assessment, and ownership. Public use requires approval.

High-governance objects should be excluded from casual editing.

## Medium-Governance Objects

Medium-governance objects include Concept, Term, Story, Person, Historical Figure, Location, Temple, Event, Article, Podcast, Short, Playlist, Glossary, Reference, and Research Source.

These objects require structured metadata and may require QA depending on use. A Concept used internally may be medium governance; a Concept used in public doctrinal teaching becomes high governance. A Story classified as legendary may require high governance if used in a documentary context.

Governance level follows use and risk.

## Low-Governance Objects

Low-governance objects include internal navigation notes, low-risk administrative metadata, non-public draft labels, and temporary retrieval candidates. Even low-governance objects require ID, type, status, and owner if they enter the knowledge system.

Low governance does not mean no governance. It means lightweight governance.

Low-governance objects must not be promoted to public use without review.

## Governance Escalation

Governance escalation occurs when an object's risk increases. A Term becomes high governance if it affects doctrine. A Visual Asset becomes high governance if it depicts the Buddha. A community Question becomes high governance if it involves suicide or abuse. A Story becomes high governance if it is presented as history.

The Knowledge Model must allow dynamic governance levels.

Escalation should be automatic where risk metadata triggers it.

# PART 13 - Dependency and Impact Analysis

## Purpose of Impact Analysis

Impact analysis identifies what is affected when a knowledge object changes. If a source is deprecated, which Knowledge Packets depend on it? If a term is replaced, which scripts, articles, subtitles, and glossary entries use it? If a Character Bible changes, which Visual Assets and Episodes are affected? If a QA decision rejects a phrase, where has that phrase appeared?

Impact analysis is one of the most important benefits of explicit relationships. It turns maintenance from guesswork into traceable work.

The Master Agent and future tools must support impact queries.

## Source Impact

When a Research Source is corrected, deprecated, disputed, or superseded, the system must identify all Citations, References, Knowledge Packets, Teachings, Articles, Episodes, and Quotes that rely on it.

Impact level depends on how central the source is. If the source supports a minor background note, risk may be low. If it supports a central doctrine or quote, risk may be high.

Source impact may trigger Research QA and public correction.

## Term Impact

When a Term changes status, the system must identify Glossaries, Knowledge Packets, Scripts, Articles, Captions, Translations, Visual text, Titles, Descriptions, and Community responses using that term.

Term impact is especially important for Vietnamese terminology, diacritics, Buddhist concepts, and translation consistency.

Deprecated terms must be excluded from future default generation.

## Visual Impact

When a Visual Asset or Character Bible is deprecated, the system must identify all Episodes, Shorts, Thumbnails, Articles, Course materials, and Website pages using or deriving from it.

Visual impact may require replacement, correction, or public update if dignity or accuracy is affected.

Sacred imagery impact should be reviewed with Visual QA.

## Knowledge Packet Impact

When a Knowledge Packet changes, all dependent Episodes, Shorts, Articles, Podcasts, Courses, Playlists, and Answers must be reviewed for impact. The system must identify whether the change affects central claims, minor wording, citations, terminology, safety notes, or tradition scope.

Major Knowledge Packet changes may require re-review of published content.

Knowledge Packet impact analysis protects long-term consistency.

## QA Impact

When QA issues a new precedent, rejected language rule, safety rule, or correction, the system should identify affected existing assets and future templates.

QA impact may create maintenance tasks, training updates, or deprecation records.

QA findings must become knowledge, not disappear after one review.

# PART 14 - Access and Retrieval Permissions

## Purpose of Access Rules

Not every object should be available to every agent for every purpose. Access and retrieval permissions prevent draft, unsafe, deprecated, private, or high-risk knowledge from being used incorrectly.

Permissions should be based on object status, risk, role, task intent, and output type. A QA Agent may retrieve rejected examples for audit. A Content Agent should not retrieve rejected language as usable phrasing. A Research Agent may access raw sources. A public-generation agent should access only approved scoped knowledge.

Access rules protect the system from accidental misuse.

## Public-Ready Retrieval

Public-ready retrieval includes approved, current objects with sufficient metadata and QA status for the intended use. These objects may support public content generation through the proper engines.

Public-ready does not mean unrestricted. A public-ready Knowledge Packet may be approved for one tradition or audience level. A quote may be approved only with citation and context.

Public-ready retrieval must include usage limits.

## Internal Draft Retrieval

Internal draft retrieval is allowed for research, planning, review, and development. Draft objects must be clearly marked. Agents using drafts must not present them as approved knowledge.

Draft retrieval is useful for QA and improvement, but dangerous for public generation.

The retrieval package must include draft warnings.

## Deprecated Retrieval

Deprecated objects may be retrieved for audit, lineage, correction, historical understanding, or avoidance. They must be excluded from default production retrieval.

When deprecated objects are retrieved, the system must also retrieve deprecation reason and replacement object where applicable.

Deprecated knowledge teaches what not to repeat.

## Restricted Retrieval

Restricted objects include sensitive safety records, crisis-related notes, private viewer information, rights-restricted sources, internal reviewer notes, or high-risk unresolved materials. Access should be limited to authorized roles.

Restricted retrieval must minimize unnecessary exposure. Sensitive viewer details should be anonymized where possible.

Protection of people is part of knowledge integrity.

# PART 15 - Maintenance and Preservation

## Purpose of Maintenance

Maintenance keeps the knowledge system accurate, current, accessible, and useful. Without maintenance, even a well-designed ontology decays. Sources break, translations improve, terms evolve, visual standards change, QA precedents accumulate, and published assets age.

The Knowledge Model must define maintenance as a normal lifecycle function, not emergency cleanup.

Maintenance is how the studio honors long-term stewardship.

## Review Cadence

Review cadence should be based on risk, importance, traffic, dependency count, and age. Foundational Knowledge Packets, high-risk Concepts, major Scriptures, commonly used Terms, Character Bibles for sacred figures, and high-traffic Episodes require more frequent review.

Low-risk objects may have longer review intervals. Deprecated objects may require review only when referenced.

Cadence metadata should be attached to objects.

## Freshness Triggers

Freshness triggers include new source evidence, QA finding, viewer confusion, broken citation, platform change, accessibility complaint, visual dignity concern, translation update, terminology change, or dependency deprecation.

Triggers should create maintenance tasks. They should not silently change objects without review.

Freshness triggers allow proactive care.

## Preservation Format

Preservation requires durable formats. Markdown, plain text, JSON, CSV, and open media formats should be preferred for long-term records where feasible. Proprietary formats may be used for production but should have export or archive strategy.

Archive records should include storage path, object ID, version, checksum where feasible, and retrieval instructions.

The future studio should not be trapped by today's tools.

## Backup and Redundancy

The knowledge system should support backup and redundancy. Governing documents, approved knowledge, QA records, archive metadata, and source records should not exist in only one fragile location.

Backups must preserve metadata and relationships, not only files.

A backup without ontology structure is incomplete.

# PART 16 - Final Ontology Standard

## Ontology Completion Test

A knowledge object is complete enough for trusted use only when it satisfies identity, type, metadata, relationships, lifecycle, lineage, and governance requirements appropriate to its risk.

For public use, the object must also satisfy QA, archive, and publication requirements where applicable. For AI retrieval, the object must include status and usage constraints. For future graph use, relationships must be explicit. For future RAG use, chunks must carry metadata.

The ontology completion test must be applied before an object becomes trusted context.

## Final Principle

The Buddhist AI Studio is building a library of meaning, not a pile of media. Every video, short, article, visual, quote, source, term, and series must know where it belongs in the larger knowledge system.

Knowledge must precede generation. Lineage must precede confidence. Context must precede interpretation. QA must precede public trust. Archive must follow publication. Maintenance must follow growth.

This Knowledge Model is the semantic foundation that allows the studio to scale without forgetting what it knows, why it knows it, and how carefully it must speak.

# PART 17 - Schema Design Rules

## Purpose of Schema Rules

Schema Design Rules define how future databases, file schemas, graph systems, RAG stores, and CMS implementations should translate this ontology into operational structures. Without schema rules, each implementation may invent its own field names, relationship meanings, and lifecycle interpretations. That would fragment the studio's memory.

The schema must preserve semantics first and optimize implementation second. A database may store fields differently from a graph, and a Markdown file may express metadata differently from JSON, but the meaning must remain stable. A Knowledge Packet must mean the same kind of object everywhere. Approved must mean the same status everywhere. Deprecated must trigger the same caution everywhere.

Schema design must support both strict validation and future extension. The studio will add object types, languages, formats, tools, and relationships over time. The schema should allow extension without breaking existing objects.

## Required Core Schema

Every object schema must include the core fields: id, object_type, label, status, version, language, owner, created_at, modified_at, source_summary, confidence, risk, lifecycle_state, and archive_link where applicable.

Some fields may be null for object types where they do not apply, but the fields should exist in the schema so systems can query consistently. For example, a Location may not need a language in the same way an Article does, but it may still have language-specific labels.

Core fields must be stable across exports. Future systems should not rename them casually because renaming breaks interoperability.

## Type-Specific Schema

Each object type requires additional fields. Scripture requires canon, tradition, edition, translator, and citation pattern. Term requires language, script, preferred status, and linked concept. Visual Asset requires format, dimensions, rights, representation target, and visual QA status. Episode requires series, source packets, publishing status, and public URL. QA Record requires reviewer, decision, score, findings, and required actions.

Type-specific fields must be documented in implementation schemas. If a field is essential for governance, it should be required. If it is helpful but not always available, it may be optional with completeness scoring.

Schema validation should prevent public approval when required type-specific fields are missing.

## Enumerated Values

Certain fields should use controlled vocabularies. Status, lifecycle_state, object_type, risk, confidence, tradition, source_type, relationship_type, approval_status, language, and governance_level should not be free text in machine systems.

Controlled values prevent drift. If one system uses "approved," another uses "final," and another uses "ready," future retrieval becomes ambiguous. Human display labels may vary, but stored values should be stable.

Controlled vocabularies may expand through governance, not casual invention.

## Free Text Fields

Free text fields are still necessary for definitions, notes, reasoning, summaries, reviewer comments, deprecation reasons, and context. Free text must not replace structured fields. A deprecation note is useful, but the object also needs status = deprecated.

Free text should be concise, evidence-aware, and connected to sources where relevant. It should not contain unreviewed doctrinal claims if the object is public or approved.

Free text fields are for explanation, not hidden governance.

## Validation Levels

Schemas should support validation levels. Draft validation checks minimal identity and owner fields. Review validation checks sources, status, risk, confidence, and relationships. Approval validation checks QA status, required metadata, versioning, and archive readiness. Publication validation checks public package fields, accessibility, platform metadata, and archive link.

Validation levels allow objects to mature over time without forcing complete metadata at the first moment. However, public trust requires full relevant validation.

The Master Agent should know which validation level a task requires.

## Schema Evolution

Schema evolution must be versioned. When fields are added, renamed, deprecated, or split, migration notes must be created. Existing objects should be migrated or mapped so future systems do not lose meaning.

Schema changes must not silently alter object status or confidence. If a new risk field reveals that older objects lack risk metadata, those objects should be marked for review rather than assumed safe.

Schema evolution is part of knowledge stewardship.

# PART 18 - Relationship Cardinality and Constraints

## Purpose of Cardinality

Cardinality defines how many objects may participate in a relationship. It prevents impossible or ambiguous structures. A Chapter must belong to one parent Scripture in a specific edition context. A Concept may have many Terms. A Quote must have at least one provenance record before public use. A Visual Asset may depict multiple objects but each depicted object should be explicit.

Cardinality rules make the ontology more machine-readable. They also help future validators detect incomplete objects.

Cardinality should be flexible enough for Buddhist textual complexity while strict enough to protect meaning.

## One-to-One Relationships

One-to-one relationships are rare but useful. A Version belongs to one primary object. An Archive Record may preserve one primary object or package, though packages may contain many components. A Character Bible may represent one primary figure, even if it includes related symbolic motifs.

One-to-one rules should not be overused. Many Buddhist and production objects have multiple relationships. A Teaching may be supported by multiple sources. A Concept may appear in many scriptures. A Person may have many names.

The ontology should use one-to-one only when identity requires it.

## One-to-Many Relationships

One-to-many relationships include Scripture contains Chapters, Chapter contains Verses, Series contains Episodes, Series Bible governs multiple Episodes, Character Bible governs multiple Visual Assets, Knowledge Packet supports multiple assets, and Glossary contains many Terms.

One-to-many relationships support hierarchy and reuse. They also create dependency impact. If a parent object changes, child objects may need review.

Parent status should not automatically determine child status. A Scripture may be approved as source, while a Chapter relationship may still require citation mapping.

## Many-to-Many Relationships

Many-to-many relationships are common. Concepts appear in many Scriptures, and Scriptures support many Concepts. Episodes may derive from many Knowledge Packets, and Knowledge Packets may support many Episodes. Terms may be used across many objects, and objects may use many Terms.

Many-to-many relationships usually require relationship metadata. The edge must explain whether the relationship is central, minor, illustrative, contrastive, prerequisite, or derivative.

Without edge metadata, many-to-many relationships become vague.

## Required Relationships

Some objects require relationships before approval. A Quote requires source or provenance. A Knowledge Packet requires Research Sources and Citations. An Episode requires source Knowledge Packets or approved research lineage. A Visual Asset depicting a sacred figure requires represented object and visual QA relationship. A Published asset requires QA record and Archive Record.

Required relationships should be enforced by validation.

Objects missing required relationships may remain drafts but cannot become trusted.

## Optional Relationships

Optional relationships enrich discovery but are not always required. A Concept may relate to other Concepts. A Story may connect to Virtues. A Location may connect to visual references. A Question may connect to audience maturity. Optional relationships should be added when useful and evidence-supported.

Optional relationships must not become speculative clutter. Each relationship should have a purpose.

Graph quality is better served by fewer meaningful edges than many weak edges.

## Forbidden Relationships

Some relationships must be forbidden or restricted. A draft object must not be marked approved_by QA unless an actual QA record exists. A rejected quote must not supports public Episode. A deprecated term must not preferred_term_for Concept. A modern reflection must not cited_as Scripture. A legendary story must not historical_event unless evidence and framing justify it.

Forbidden relationships should be enforced through validation and QA.

These constraints prevent category errors.

## Relationship Confidence

Relationships may carry confidence distinct from node confidence. A Source may be reliable, but a specific edge between that Source and a Concept may be interpretive. A Story may be canonical, but its relationship to a modern psychological concept may have medium confidence.

Relationship confidence should be recorded for interpretive, historical, symbolic, or cross-tradition edges.

Edge confidence helps retrieval systems avoid overclaiming.

# PART 19 - Claim Modeling

## Purpose of Claim Modeling

Claims are the smallest meaningful assertions that may require evidence. A claim may state that a scripture says something, that a practice belongs to a tradition, that a historical event occurred, that a term means something, or that a visual symbol represents a concept.

The Knowledge Model must support claim-level tracking because public errors often occur at the claim level. A whole Article may be mostly accurate while one sentence contains an unsupported historical claim. A Knowledge Packet may be approved except for one uncertain interpretation. Claim modeling allows precise QA and correction.

Not every sentence needs formal claim modeling. High-risk, public, doctrinal, historical, quotation, scientific, medical, and safety-relevant assertions should be modeled.

## Claim Object

A Claim object is a structured assertion. It should include claim ID, claim text, claim type, subject object, predicate, object or value, source citations, confidence, tradition scope, risk, status, owner, and QA status.

Claim types include scriptural claim, doctrinal claim, historical claim, translation claim, interpretive claim, symbolic claim, practice claim, visual claim, production claim, and editorial claim.

Claim objects can be embedded inside Knowledge Packets or stored separately in a graph or database.

## Scriptural Claim

A Scriptural Claim states that a scripture, chapter, verse, or passage contains, teaches, mentions, or supports something. It requires citation and source edition.

Scriptural Claims must distinguish quotation, paraphrase, summary, and interpretation. A passage may mention a term without teaching the full modern Concept. A story may imply a virtue without explicitly defining it.

Scriptural Claims require careful QA when public.

## Doctrinal Claim

A Doctrinal Claim states something about Buddhist teaching or interpretation. It requires tradition scope, source support, and confidence. It may be general Buddhist, Mahayana-specific, Pure Land-specific, Zen-specific, Theravada-specific, Vietnamese tradition-specific, or modern reflection.

Doctrinal Claims must not be universalized without evidence. If traditions differ, the claim must say so or be scoped.

Doctrinal Claims are high-governance objects.

## Historical Claim

A Historical Claim states that a person, event, date, place, institution, text transmission, or cultural development occurred in history. It requires historical evidence, confidence, and distinction from legend or devotional narrative.

Historical Claims may be high confidence, plausible, disputed, legendary, traditional, symbolic, or unknown. The ontology must represent this status clearly.

Historical Claims should never be strengthened for narrative convenience.

## Translation Claim

A Translation Claim states that a term, passage, title, or phrase is rendered in a particular way. It requires source language, target language, translator or authority, context, and notes.

Translation Claims may have multiple valid alternatives. The Knowledge Model must support alternate translations without treating one as universal unless approved.

Translation Claims are important for multilingual consistency.

## Symbolic Claim

A Symbolic Claim states that an image, story, location, color, object, gesture, or figure symbolizes a concept, virtue, teaching, or practice. It requires tradition context or editorial framing.

Symbolic Claims are often interpretive. They should not be presented as historical or literal unless supported.

Visual Engine and QA depend on symbolic claim clarity.

## Claim Status

Claim status values include proposed, researching, supported, approved, disputed, rejected, deprecated, superseded, and restricted. A claim may be supported by research but not approved for public use. A claim may be approved in one context but restricted in another.

Claim status must be visible to generation systems.

Unsupported claims must not become public assertions.

## Claim Correction

When a claim is corrected, the system must identify every object that used the claim. Corrections may affect Knowledge Packets, Episodes, Articles, Shorts, Captions, Quotes, Visual Assets, and community answers.

Claim correction should create a new version and preserve prior status.

Claim-level correction is more precise than whole-object panic.

# PART 20 - Multilingual and Cross-Cultural Model

## Purpose of Multilingual Modeling

Buddhist knowledge crosses languages and cultures. The studio's likely languages include Vietnamese and English, with possible future Sanskrit, Pali, Chinese, and other languages. The Knowledge Model must support multilingual identity without losing meaning.

A Concept is not identical to one Term. A Term is not identical to one translation. A translated Article is not identical to the source Article. A subtitle is not merely text; it is a timed public teaching surface.

Multilingual modeling prevents translation drift.

## Language-Neutral Concepts

Concept objects should be language-neutral where possible. Karma, nghiệp, and karma in English are Terms linked to a broader Concept. The Concept stores core meaning, tradition scope, source anchors, and risk notes.

Language-neutral does not mean culture-neutral. Concept metadata should allow tradition and culture notes. A concept may be explained differently for Vietnamese Buddhist audiences and English-speaking beginners.

The model should separate concept identity from expression.

## Language-Specific Terms

Terms are language-specific. They carry spelling, script, diacritics, pronunciation, usage status, translation notes, and context. Vietnamese terms must preserve diacritics where appropriate. English terms must avoid misleading generic substitutes.

Term status may vary by language. A Vietnamese term may be preferred in one context while an English translation is explanatory rather than canonical.

Language-specific Terms support consistent localization.

## Translation Relationships

Translation relationships connect source objects to target-language objects. Relationship types include translates, translated_as, localizes, adapted_from, and equivalent_to. These must not be used interchangeably.

Translates indicates close language rendering. Localizes indicates cultural adaptation. Adapted_from indicates format or audience transformation. Equivalent_to should be used cautiously because exact equivalence is rare in Buddhist terminology.

Translation relationships should include translator, method, QA status, and confidence.

## Cross-Cultural Notes

Cross-cultural notes explain cultural assumptions, ritual contexts, family structures, devotional practices, and audience sensitivities. They are important for filial piety, ancestor remembrance, temple practices, chanting, bowing, monastic representation, and grief rituals.

Cross-cultural notes must avoid stereotypes and overgeneralization. They should be tied to sources or editorial review where possible.

These notes help the studio be respectful across audiences.

## Localization Risk

Localization risk occurs when adapting content changes meaning. Examples include translating karma into fate, merit into reward points, mindfulness into productivity attention, emptiness into nothingness, or filial piety into unconditional obedience.

The Knowledge Model must flag high-risk localization terms and require QA before public use.

Localization should make teachings accessible without distorting them.

## Multilingual Versioning

Each language version must have its own version history and QA status. Updating the English version does not automatically update the Vietnamese version. Correcting a source claim may require updates across all language versions.

Multilingual versioning should connect versions through translation relationships and dependency links.

This enables impact analysis across languages.

# PART 21 - QA and Knowledge Model Integration

## Purpose of QA Integration

The QA Engine and Knowledge Model must be tightly integrated. QA evaluates objects, relationships, claims, metadata completeness, retrieval safety, and public readiness. The Knowledge Model stores QA decisions as structured objects and relationships.

QA must not exist only as comments in documents. QA findings should become queryable knowledge. Future agents should know what was approved, rejected, revised, deprecated, or escalated.

QA integration turns quality decisions into long-term memory.

## QA Record Object

Although not listed as a core object in the initial object list, QA Record is an essential governance object. A QA Record documents reviewer, review domains, timestamp, evidence, scores, findings, decision, required actions, confidence, and scope.

QA Records connect to reviewed objects through approved_by, rejected_by, requires_revision_by, escalated_by, or held_by relationships.

QA Records must be immutable after finalization, except for metadata corrections. New decisions should create new records.

## QA Findings as Knowledge

QA findings should be structured where possible. A finding may identify issue type, severity, affected object, evidence, standard violated, required action, and resolution.

Findings can feed the Rejected Language Bank, Visual Caution Library, Safety Precedent Library, and Quality Pattern Reports. They can also update risk metadata and deprecation status.

QA findings should not disappear after one artifact is fixed.

## Approval Scope

Approval scope must be encoded. QA approval may apply to a specific object version, format, language, platform, audience, series, or use case. It must not be assumed universal.

For example, a Knowledge Packet may be approved for content planning but not direct public quotation. A Visual Asset may be approved as internal reference but not as thumbnail. A script may be approved in Vietnamese but not in English translation.

Approval scope prevents overuse.

## QA-Driven Retrieval

Retrieval systems should use QA status as a ranking and filtering signal. Approved current objects should be preferred. Rejected and deprecated objects should be excluded unless the task is review, audit, or avoidance. Conditional approval should include conditions.

QA-driven retrieval helps AI agents avoid unsafe context.

The system should not rely on agents to remember QA decisions from prose.

## QA Impact Propagation

When QA changes an object's status, dependent objects may need review. A rejected claim affects Knowledge Packets. A deprecated term affects captions and articles. A visual caution affects future image generation. A safety precedent affects community responses.

The Knowledge Model must support propagation through dependency relationships.

QA impact propagation is essential for a living library.

# PART 22 - Migration and Legacy Strategy

## Purpose of Migration Strategy

The studio will accumulate legacy files, early documents, old scripts, old visuals, unstructured notes, and published assets created before the full ontology is implemented. Migration strategy defines how to bring them into the Knowledge Model without pretending they already meet current standards.

Migration must be careful. Legacy material may be useful, but it may lack metadata, source lineage, QA records, or terminology consistency. The system should classify it honestly.

Migration is a knowledge stewardship task.

## Legacy Object Intake

Legacy intake begins by identifying object type, file location, title, language, status, and rough relationship to existing knowledge. The object should enter with status legacy_unclassified or draft until reviewed.

Legacy objects must not be automatically marked approved because they were previously published or used. Publication history is evidence of exposure, not evidence of quality.

Legacy intake should prioritize high-risk and high-value assets.

## Metadata Backfill

Metadata backfill adds IDs, object types, dates, owners, language, status, source summaries, relationships, and archive records to legacy objects. Backfill should be staged. Minimum identity comes first. Source lineage and QA status come later.

Backfill should not invent missing evidence. If a source is unknown, metadata should say unknown.

Honest incomplete metadata is better than false completeness.

## Relationship Reconstruction

Legacy relationship reconstruction identifies how old assets connect to concepts, sources, series, visuals, and published objects. This may require human review or research.

Relationships should be marked with confidence. A likely relationship should not be treated as verified. If an old episode appears to rely on a source but lacks citation, the relationship may be probable_source until reviewed.

Reconstruction must preserve uncertainty.

## Legacy QA Review

Legacy QA review should prioritize public assets with high traffic, high risk, foundational role, or known viewer confusion. Review may result in approved legacy, needs refresh, needs correction, deprecated, or restricted.

Not every legacy asset must be fully reviewed immediately. The system should use risk-based prioritization.

Legacy review is how the library matures without erasing its past.

## Migration Completion

Migration is complete for an object when it has stable ID, object type, status, core metadata, key relationships, archive record, and appropriate QA or legacy classification.

Migration completion does not necessarily mean the object is approved for new use. It means it is known to the system.

Known legacy is safer than invisible legacy.

# PART 23 - Knowledge Model Operating Checklist

## Purpose of Checklist

The Operating Checklist helps future agents apply the Knowledge Model. It should be used when creating, importing, reviewing, retrieving, adapting, publishing, archiving, or deprecating knowledge objects.

The checklist is not a workflow engine. It is an ontology integrity aid.

Every substantial object should pass the relevant checklist before trusted use.

## Object Creation Checklist

Identify object type.

Assign stable ID.

Record label and alternate labels.

Record language and tradition where applicable.

Assign owner.

Set status.

Attach source or source summary.

Record confidence and risk.

Add required relationships.

Set lifecycle state.

Identify QA requirement.

Create version record.

## Retrieval Checklist

Define task intent.

Filter by approved status where public use is intended.

Filter by language and tradition.

Check risk metadata.

Retrieve source lineage.

Retrieve related terms and concepts.

Retrieve usage limits.

Exclude deprecated and rejected objects unless needed for audit.

Report missing context.

## Publication Checklist

Confirm public asset object exists.

Confirm source lineage.

Confirm approved versions.

Confirm QA scope.

Confirm language status.

Confirm visual representation links where applicable.

Confirm accessibility metadata.

Confirm publishing metadata.

Confirm archive record.

Confirm maintenance trigger.

## Deprecation Checklist

Identify object to deprecate.

Record reason.

Identify authority.

Set deprecation date.

Link replacement object if available.

Run dependency impact analysis.

Update retrieval filters.

Archive deprecation record.

Notify affected workflows.

## Final Operating Mandate

The Knowledge Model must make the right action easier than the wrong action. It should make approved knowledge easy to find, uncertain knowledge easy to recognize, deprecated knowledge hard to misuse, and public claims easy to audit.

Every future AI system should inherit this structure before generating, adapting, reviewing, or publishing Buddhist educational media.

# PART 24 - Machine Use Quality Controls

## Purpose of Machine Use Controls

Machine Use Quality Controls define how AI systems, retrieval tools, graph queries, automation scripts, and future MCP servers should consume the Knowledge Model. The ontology is designed for machines, but machines must not treat every retrieved object as permission to generate. Retrieval is not approval. Similarity is not truth. Availability is not suitability.

Machine use controls are necessary because future systems may retrieve thousands of objects faster than humans can inspect them. Without controls, an agent may mix draft and approved knowledge, merge traditions, reuse deprecated terms, or present uncertain claims as settled. The Knowledge Model must therefore make retrieval safe by default.

The canonical machine rule is: **an AI system may use a knowledge object only within the object's status, scope, confidence, risk, language, tradition, and QA limits.**

## Default Retrieval Filter

The default retrieval filter for public-facing generation must include only current, approved, in-scope objects unless the task explicitly requests review, audit, migration, or correction. Draft, rejected, deprecated, superseded, on-hold, restricted, and low-confidence objects must be excluded by default.

If a task requires internal planning, the filter may include draft or researching objects, but the retrieval package must label them clearly. If a task requires QA review, rejected and deprecated objects may be retrieved as evidence or warnings.

Default filters are the first defense against accidental misuse.

## Context Package Assembly

AI systems should receive context packages, not raw search dumps. A context package should include primary objects, supporting sources, citations, relationship paths, terminology notes, risk notes, usage limits, and missing-context warnings.

The package should identify which objects are required and which are supplementary. It should also identify whether the knowledge is sufficient for the requested task. If sufficient knowledge is not available, the package must say so.

Context package assembly should be controlled by the Master Agent or a dedicated retrieval service following this ontology.

## Generation Preconditions

Before any AI agent generates public-facing material from retrieved knowledge, the system must verify preconditions: approved source context exists, lifecycle status allows use, risk has been classified, language and tradition match the task, forbidden outputs are respected, and QA requirements are known.

If preconditions fail, the agent may produce a plan, question, or internal note if authorized, but not public content. If the active request forbids content, the agent must not generate content even when knowledge exists.

Generation preconditions protect the boundary between knowledge and expression.

## Citation Injection Rules

When AI systems produce research-facing or public factual material, citations must be drawn from Citation objects, not invented from source names. If no Citation object exists for a claim, the system must either omit the claim, mark it for research, or route to the Research Engine.

Citation injection must preserve source edition, translator, passage, page, URL, and confidence where available. It must not cite an entire scripture or book for a precise claim unless that level of citation is appropriate.

Citation systems must prefer precision over appearance.

## Uncertainty Preservation

AI systems must preserve uncertainty metadata. If an object or claim is marked uncertain, disputed, tradition-specific, symbolic, legendary, or low-confidence, generated output must not upgrade it to certainty.

Uncertainty preservation should apply across all formats: scripts, articles, captions, descriptions, visual briefs, community responses, and course materials. A short format may not have room for full nuance; in that case the system should avoid the claim or direct viewers to fuller context.

Uncertainty is not weakness. It is honesty.

## Risk Propagation

Risk metadata must propagate into downstream tasks. If a Knowledge Packet is high-risk because it involves death, karma blame, or hell realms, any Episode, Short, Article, visual plan, title, description, or community prompt derived from it inherits risk unless QA explicitly scopes otherwise.

Risk propagation prevents a sensitive topic from becoming casual during adaptation. A high-risk concept remains high-risk in short form, translation, title packaging, and visual design.

AI systems must not drop risk flags when summarizing.

## Hallucination Resistance

The Knowledge Model supports hallucination resistance by requiring object IDs, citations, status, confidence, and lineage. AI systems must be instructed to use only retrieved approved information for factual claims and to identify gaps rather than inventing.

Hallucination resistance also requires negative knowledge. Rejected quotes, deprecated terms, forbidden relationships, and QA findings should be retrievable for prevention when relevant. An agent should know not only what to say, but what the studio has already rejected.

Negative knowledge is part of safety.

## Machine-Readable Warnings

Objects should support machine-readable warnings. Warning fields may include requires_human_review, high_risk_topic, tradition_specific, citation_required, quote_provenance_required, visual_dignity_required, safety_language_required, deprecated_do_not_use, and draft_not_for_publication.

Warnings should be simple enough for automation to apply and clear enough for humans to understand.

Warning fields reduce reliance on long prose instructions.

## Output Validation Hooks

Future systems should include validation hooks that compare generated output against the Knowledge Model. Validation may check whether quoted text exists, whether terms are approved, whether forbidden language appears, whether public claims have citations, whether visual assets are approved, and whether deprecated objects were used.

Validation hooks do not replace QA. They reduce preventable errors before QA.

The Knowledge Model should be built so validators can query it efficiently.

## Machine Use Audit

AI usage should be auditable. When an AI system uses retrieved objects, the system should record which objects were retrieved, which were used, which were ignored, what output was generated, and which validation checks ran.

Machine use audit supports debugging, QA, and incident response. If an error appears in public output, the studio should know whether the issue came from retrieval, generation, validation, or review.

Auditable machine use is required for enterprise-scale trust.

## Final Machine Control Standard

Every future AI system connected to the Buddhist AI Studio must treat the Knowledge Model as a governed memory system, not a content pile. It must retrieve with filters, preserve metadata, respect lifecycle, propagate risk, cite precisely, maintain uncertainty, and submit public artifacts to QA.

The machine's task is not to sound knowledgeable. Its task is to serve knowledge faithfully.

