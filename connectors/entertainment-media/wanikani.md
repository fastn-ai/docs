---
description: "WaniKani API v2 — Japanese kanji learning SRS."
hidden: true
---

# WaniKani

<img src="../../.gitbook/assets/connectors/lg/wanikani.png" alt="WaniKani logo">

WaniKani API v2 — Japanese kanji learning SRS. Read your assignments, subjects (radicals/kanji/vocabulary), reviews, review statistics, level progressions, resets, study materials, spaced repetition systems, voice actors, summary and user profile; start lessons, submit reviews and manage study materials.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [wanikani.com](https://wanikani.com) |
| **Authentication** | API key |
| **Slug** | `wanikani` |

## Use it

Add WaniKani from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.wanikani.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Review | `createReview` | Submits a completed review for an assignment, advancing or demoting its SRS stage and rescheduling the next review. This permanently alters the learner's study schedule and cannot be undone — only call it for a review the user has genuinely just answered. Supply either assignment_id or subject_id, not both. Requires a token with the reviews:create scope. |
| Create Study Material | `createStudyMaterial` | Creates a study material for a subject, attaching a personal meaning note, reading note and up to eight user synonyms. Only one study material may exist per subject. WaniKani has no delete endpoint for study materials, so a created record can only be edited afterwards, never removed. Requires a token with the study_materials:create scope. |
| Get Assignment | `getAssignment` | Returns a single assignment by its id, including the subject it covers, its SRS stage and the timestamps for unlock, lesson start, pass and burn. |
| Get Level Progression | `getLevelProgression` | Returns a single level progression by its id, showing when the user unlocked, started, passed and completed that WaniKani level. |
| Get Reset | `getReset` | Returns a single reset by its id, showing the level the user reset from, the level they reset to and when the reset was confirmed. |
| Get Review | `getReview` | Returns a single completed review by its id, including the assignment and subject reviewed, the incorrect answer counts and the SRS stage transition. |
| Get Review Statistic | `getReviewStatistic` | Returns a single review statistic by its id, with the full correct and incorrect answer tallies, streaks and percentage correct for one subject. |
| Get Spaced Repetition System | `getSpacedRepetitionSystem` | Returns a single spaced repetition system by its id, including every SRS stage with its review interval and the positions at which subjects unlock, pass and burn. |
| Get Study Material | `getStudyMaterial` | Returns a single study material by its id, with the meaning note, reading note and user synonyms the learner saved for that subject. |
| Get Subject | `getSubject` | Returns a single WaniKani subject by its id — a radical, kanji, vocabulary or kana vocabulary item — with its characters, meanings, readings, mnemonics and related subject ids. |

<details>

<summary>See 15 more actions</summary>

* **Get Summary** `getSummary`: Returns the study summary report: the subject ids available for lessons right now, the reviews available in each of the next 24 hourly windows, and the timestamp of the next review.
* **Get User** `getUser`: Returns the profile of the WaniKani user who owns the personal access token, including username, current level, subscription status, preferences and the account start date.
* **Get Voice Actor** `getVoiceActor`: Returns a single voice actor by its id, with the name, gender and description of the person who records WaniKani's vocabulary audio.
* **List Assignments** `listAssignments`: Returns a paginated collection of assignments — the link between the user and a subject, carrying the SRS stage and the next available review time. Supports filtering by level, SRS stage, subject, lifecycle state and update time.
* **List Level Progressions** `listLevelProgressions`: Returns a paginated collection of level progressions, one per WaniKani level the user has unlocked, with the timestamps at which the level was unlocked, started, passed, completed or abandoned.
* **List Resets** `listResets`: Returns a paginated collection of resets, recording every time the user reset their WaniKani progress back to an earlier level, with the original and target levels.
* **List Review Statistics** `listReviewStatistics`: Returns a paginated collection of review statistics, one per subject the user has reviewed, summarising correct and incorrect meaning and reading answers, current and maximum streaks and the overall percentage correct.
* **List Reviews** `listReviews`: Returns a paginated collection of reviews the user has completed, each recording the incorrect meaning and reading counts and the SRS stage the subject moved from and to.
* **List Spaced Repetition Systems** `listSpacedRepetitionSystems`: Returns a paginated collection of the spaced repetition systems WaniKani uses, each listing every SRS stage with its interval, the unlocking stage position and the burning stage position.
* **List Study Materials** `listStudyMaterials`: Returns a paginated collection of the user's study materials — the personal meaning notes, reading notes and user synonyms attached to individual subjects.
* **List Subjects** `listSubjects`: Returns a paginated collection of WaniKani subjects — radicals, kanji, vocabulary and kana vocabulary — with their characters, meanings, readings, mnemonics, component subject ids and level. Filter by type, level, slug or id.
* **List Voice Actors** `listVoiceActors`: Returns a paginated collection of the voice actors who record WaniKani's vocabulary audio, with their name, gender and description.
* **Start Assignment** `startAssignment`: Marks an assignment's lesson as started, moving the subject out of the lesson queue and into the review queue. This permanently changes the learner's study schedule — call it only when the user really means to begin that lesson. Requires a token with the assignments:start scope.
* **Update Study Material** `updateStudyMaterial`: Updates an existing study material by id, replacing the meaning note, reading note and user synonyms. Requires a token with the study_materials:update scope.
* **Update User Preferences** `updateUserPreferences`: Updates the signed-in user's study preferences: lesson batch size and presentation order, review presentation order, SRS indicator display, default voice actor and audio autoplay settings for lessons, reviews and extra study. Requires a token with the user:update scope.

</details>
