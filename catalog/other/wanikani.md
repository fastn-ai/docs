---
description: "WaniKani is an app for learning Japanese kanji. Read assignments, subjects, reviews and level progress, and create reviews and study materials."
hidden: true
---

# WaniKani

<img src="../../.gitbook/assets/connectors/lg/wanikani.png" alt="WaniKani logo">

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [wanikani.com](https://wanikani.com) |
| **Authentication** | API key |
| **Slug** | `wanikani` |

## Setup

Your customers enter their API key for WaniKani when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect WaniKani from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **WaniKani**.
2. Select **Connect** on the WaniKani card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use WaniKani's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Review</td><td><code>createReview</code></td><td>Submits a completed review for an assignment, advancing or demoting its SRS stage and rescheduling the next review. This permanently alters the learner's study schedule and cannot be undone — only call it for a review the user has genuinely just answered. Supply either assignment_id or subject_id, not both. Requires a token with the reviews:create scope.</td></tr><tr><td>Create Study Material</td><td><code>createStudyMaterial</code></td><td>Creates a study material for a subject, attaching a personal meaning note, reading note and up to eight user synonyms. Only one study material may exist per subject. WaniKani has no delete endpoint for study materials, so a created record can only be edited afterwards, never removed. Requires a token with the study_materials:create scope.</td></tr><tr><td>Get Assignment</td><td><code>getAssignment</code></td><td>Returns a single assignment by its id, including the subject it covers, its SRS stage and the timestamps for unlock, lesson start, pass and burn.</td></tr><tr><td>Get Level Progression</td><td><code>getLevelProgression</code></td><td>Returns a single level progression by its id, showing when the user unlocked, started, passed and completed that WaniKani level.</td></tr><tr><td>Get Reset</td><td><code>getReset</code></td><td>Returns a single reset by its id, showing the level the user reset from, the level they reset to and when the reset was confirmed.</td></tr><tr><td>Get Review</td><td><code>getReview</code></td><td>Returns a single completed review by its id, including the assignment and subject reviewed, the incorrect answer counts and the SRS stage transition.</td></tr><tr><td>Get Review Statistic</td><td><code>getReviewStatistic</code></td><td>Returns a single review statistic by its id, with the full correct and incorrect answer tallies, streaks and percentage correct for one subject.</td></tr><tr><td>Get Spaced Repetition System</td><td><code>getSpacedRepetitionSystem</code></td><td>Returns a single spaced repetition system by its id, including every SRS stage with its review interval and the positions at which subjects unlock, pass and burn.</td></tr><tr><td>Get Study Material</td><td><code>getStudyMaterial</code></td><td>Returns a single study material by its id, with the meaning note, reading note and user synonyms the learner saved for that subject.</td></tr><tr><td>Get Subject</td><td><code>getSubject</code></td><td>Returns a single WaniKani subject by its id — a radical, kanji, vocabulary or kana vocabulary item — with its characters, meanings, readings, mnemonics and related subject ids.</td></tr></tbody></table>

<details>

<summary>View 15 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Summary</td><td><code>getSummary</code></td><td>Returns the study summary report: the subject ids available for lessons right now, the reviews available in each of the next 24 hourly windows, and the timestamp of the next review.</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Returns the profile of the WaniKani user who owns the personal access token, including username, current level, subscription status, preferences and the account start date.</td></tr><tr><td>Get Voice Actor</td><td><code>getVoiceActor</code></td><td>Returns a single voice actor by its id, with the name, gender and description of the person who records WaniKani's vocabulary audio.</td></tr><tr><td>List Assignments</td><td><code>listAssignments</code></td><td>Returns a paginated collection of assignments — the link between the user and a subject, carrying the SRS stage and the next available review time. Supports filtering by level, SRS stage, subject, lifecycle state and update time.</td></tr><tr><td>List Level Progressions</td><td><code>listLevelProgressions</code></td><td>Returns a paginated collection of level progressions, one per WaniKani level the user has unlocked, with the timestamps at which the level was unlocked, started, passed, completed or abandoned.</td></tr><tr><td>List Resets</td><td><code>listResets</code></td><td>Returns a paginated collection of resets, recording every time the user reset their WaniKani progress back to an earlier level, with the original and target levels.</td></tr><tr><td>List Review Statistics</td><td><code>listReviewStatistics</code></td><td>Returns a paginated collection of review statistics, one per subject the user has reviewed, summarising correct and incorrect meaning and reading answers, current and maximum streaks and the overall percentage correct.</td></tr><tr><td>List Reviews</td><td><code>listReviews</code></td><td>Returns a paginated collection of reviews the user has completed, each recording the incorrect meaning and reading counts and the SRS stage the subject moved from and to.</td></tr><tr><td>List Spaced Repetition Systems</td><td><code>listSpacedRepetitionSystems</code></td><td>Returns a paginated collection of the spaced repetition systems WaniKani uses, each listing every SRS stage with its interval, the unlocking stage position and the burning stage position.</td></tr><tr><td>List Study Materials</td><td><code>listStudyMaterials</code></td><td>Returns a paginated collection of the user's study materials — the personal meaning notes, reading notes and user synonyms attached to individual subjects.</td></tr><tr><td>List Subjects</td><td><code>listSubjects</code></td><td>Returns a paginated collection of WaniKani subjects — radicals, kanji, vocabulary and kana vocabulary — with their characters, meanings, readings, mnemonics, component subject ids and level. Filter by type, level, slug or id.</td></tr><tr><td>List Voice Actors</td><td><code>listVoiceActors</code></td><td>Returns a paginated collection of the voice actors who record WaniKani's vocabulary audio, with their name, gender and description.</td></tr><tr><td>Start Assignment</td><td><code>startAssignment</code></td><td>Marks an assignment's lesson as started, moving the subject out of the lesson queue and into the review queue. This permanently changes the learner's study schedule — call it only when the user really means to begin that lesson. Requires a token with the assignments:start scope.</td></tr><tr><td>Update Study Material</td><td><code>updateStudyMaterial</code></td><td>Updates an existing study material by id, replacing the meaning note, reading note and user synonyms. Requires a token with the study_materials:update scope.</td></tr><tr><td>Update User Preferences</td><td><code>updateUserPreferences</code></td><td>Updates the signed-in user's study preferences: lesson batch size and presentation order, review presentation order, SRS indicator display, default voice actor and audio autoplay settings for lessons, reviews and extra study. Requires a token with the user:update scope.</td></tr></tbody></table>

</details>

