# EP004 Status

manifest.json is the machine-readable source of truth. This file is a human-readable projection from the manifest.

| Field | Value |
|---|---|
| Package ID | PKG_BUD_KDT_EP004 |
| Version | 0.1.0 |
| Package status | READY_FOR_REVIEW |
| Current gate | READY_FOR_SCRIPT_REVIEW |
| Production profile | YOUTUBE_LONG_FORM |

| Stage | Workflow status | QA status | Blocking issues | Required next action |
|---|---|---|---|---|
| Research | READY_FOR_REVIEW | PASS_WITH_ADVISORIES | citation/copyright human review before publish | human review |
| Planner | READY_FOR_REVIEW | PASS | none | human review |
| Script | READY_FOR_REVIEW | PASS_WITH_ADVISORIES | human review before voice approval | review master script |
| TTS | READY_FOR_REVIEW | PASS | none | render voice after approval |
| Voice | NOT_STARTED | NOT_RUN | audio not rendered | render audio |
| Subtitle | IN_PROGRESS | PASS_WITH_ADVISORIES | awaiting audio alignment | align after audio exists |
| Visual | READY_FOR_REVIEW | PASS_WITH_ADVISORIES | Buddha/Maya visual review | visual review |
| Metadata | READY_FOR_REVIEW | PASS_WITH_ADVISORIES | citation/copyright review before publish | human review |
| Package QA | READY_FOR_REVIEW | PASS_WITH_ADVISORIES | no audio/final SRT yet | rerun audit after voice |
| Human Review | IN_PROGRESS | NOT_RUN | human review pending | complete review |
| Video | NOT_STARTED | NOT_APPLICABLE | no audio/video | begin after voice/subtitle |
| Publish | NOT_STARTED | NOT_APPLICABLE | not publish-ready | complete final QA |
