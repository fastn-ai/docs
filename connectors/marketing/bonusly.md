---
description: "Bonusly employee recognition and rewards platform."
hidden: true
---

# Bonusly

<img src="../../.gitbook/assets/connectors/lg/bonusly.png" alt="Bonusly logo">

Bonusly employee recognition and rewards platform. Covers the Bonusly REST API v1 (bonuses, users, achievements, redemptions, custom reward redemptions and company settings), the public API (awards, file uploads, profile settings and the analytics data warehouse with its snapshot exports) and SCIM user provisioning. Authenticates with a Bonusly personal access token sent as a Bearer token. Bonusly publishes no webhook or event API, so this connector has no event configuration and no bindable triggers; poll the list endpoints or the analytics datasets instead.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [bonus.ly](https://bonus.ly) |
| **Authentication** | Credentials you enter |
| **Slug** | `bonusly` |

## Use it

Add Bonusly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bonusly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Approve Custom Reward Redemptions | `approveCustomRewardsRedemptions` | Bulk-approves the supplied custom reward redemptions. Returns per-record results — rewards that couldn't be approved (e.g. wrong state) are listed in result.errors rather than failing the whole call. |
| Autocomplete Users | `autocompleteUsers` | Returns up to limit (default 20) users matching search, ordered by the relevance ranking from the Algolia search index. Results are a compact summary, not the full UserDecorator output. |
| Check Analytics Health | `analyticsHealthcheck` | Returns ok if the Analytics surface is reachable. Unauthenticated. |
| Create Award | `createAward` | Creates a new manual award for the user's company. Sets up the award, eligibility conditions, and optional approval process. Requires the awards:administer scope and awards admin permission. |
| Create Bonus | `createBonus` | Creates a bonus. The reason is parsed for amount, recipients, and hashtags (e.g. +10 @alice @bob for shipping #teamwork). Admin tokens can issue bonuses on behalf of another giver via giver_email/giver_id. |
| Create User | `createUser` | Creates a user in the authenticated admin's company. Requires an admin (or company-scoped) access token. Reactivates an existing deactivated user if their email matches. |
| Create User (SCIM 1.1) | `scim1CreateScimUser` | Creates a new user in Bonusly. If a deactivated user with the same userName exists, that user is reactivated and updated. If an active user already exists with the same userName, returns 409. |
| Create User (SCIM 2.0) | `scim2CreateUser` | Creates a new user in the authenticated company. Returns the created user in SCIM form with Location header pointing at /Users/{id}. Returns 409 Conflict with scimType: "uniqueness" if a user with the same userName (email) already exists in the company. The conflict response does not echo the conflicting email back to the IdP. New users automatically receive a Bonusly welcome email. The invitation flow used for self-signup is bypassed for SCIM-provisioned users. |
| Create User Redemption | `createUserRedemption` | Create a User Redemption. |
| Deactivate User | `deleteUser` | Soft-deletes (deactivates) a user. Requires admin auth. |
| Deactivate User (SCIM 1.1) | `scim1UpdateScimUserActivationStatus` | Sets the user's active state. Maps to DELETE / PATCH on the same path. |
| Deactivate User (SCIM 2.0) | `scim2DeleteUser` | Deactivates the user. Bonusly does NOT hard-delete records — the user is preserved (for audit, balance history, and possible rehire) and marked inactive. To restore later, send PATCH or PUT with active: true. Activation policy refusals surface as 422. |
| Delete Award | `deleteAward` | Soft-deletes the award and deactivates its bot user. The award will no longer appear in any list or show responses. Requires the awards:administer scope and awards admin permission. |
| Delete Bonus | `deleteBonus` | Archives a bonus (soft delete). Subject to the BonusArchiving policy — the giver can undo their own bonus within the edit window; admins can undo any bonus within the window. |
| Fulfill Custom Reward Redemptions | `fulfillCustomRewardsRedemptions` | Bulk-fulfills the supplied custom reward redemptions. Same response shape and error contract as /approve. |
| Get Analytics Snapshot | `getAnalyticsSnapshot` | Returns the current status and (when ready) signed file URL for a previously-queued snapshot. Scoped to the requesting API key's company. |
| Get Award | `getAward` | Returns a single award including approval levels and title. Requires the awards:read scope and awards admin permission. |
| Get Bonus | `getBonus` | Returns a single bonus by id, scoped to the authenticated user's company. |
| Get Company | `getCompany` | Returns the authenticated user's company. |
| Get Current User | `getMe` | Returns the authenticated user. Requires a *user* access token — company-scoped tokens return 400. Also surfaces the X-BONUSLY-Country-Code and X-BONUSLY-Authentication-Token response headers. |
| Get Redemption | `getRedemption` | Returns a single redemption by ID, scoped to the authenticated user's company. |
| Get Service Provider Configuration (SCIM 1.1) | `scim1GetServiceProviderConfigs` | Returns the SCIM features supported by the Bonusly server. |
| Get Service Provider Configuration (SCIM 2.0) | `scim2GetServiceProviderConfig` | Returns the SCIM 2.0 service provider configuration document describing which optional protocol features Bonusly supports (PATCH, filtering, bulk, etag, change password, sort). |
| Get User | `getUser` | Returns a single user by id, scoped to the authenticated user's company. |
| Get User (SCIM 1.1) | `scim1GetScimUser` | Fetch a specific user by id. |
| Get User (SCIM 2.0) | `scim2GetUser` | Fetch a single user. |
| Give Award | `giveAward` | Initiates an award give on behalf of the authenticated user. The user must satisfy the award's eligibility conditions. If the award has no approval process, the give is auto-approved and a bonus is created immediately. Otherwise, an approval request is created and approvers are notified. Requires the awards:write scope. |
| List Achievements | `listAchievements` | Returns the 50 most recent achievements earned by users in the authenticated user's company. |
| List Analytics Users | `listAnalyticsUsers` | Page of analytics_users rows for the requesting company. Resolves the user_id references surfaced by every other analytics MV (RecognitionEvents.giver_id / receiver_ids, the MonthlyUser* rollups, etc.) back to the customer's own identity (email, external_unique_id). |
| List Awards | `listAwards` | Returns a paginated list of awards belonging to the user's company. Supports filtering by state. Uses opaque cursor pagination — pass page_size (and optionally state) on the first call; on subsequent calls pass only the returned next_cursor. Results are ordered by ID ascending. Requires the awards:read scope and awards admin permission. |
| List Bonuses | `listBonuses` | Returns a paginated list of bonuses for the authenticated user's company. |
| List Bonuses As Atom Feed | `listBonusesAtom` | Returns the bonuses index as an ATOM RSS feed (append .atom to the normal bonuses index URL). |
| List Check-In Events | `listCheckInEvents` | Page of check_in_events rows. One row per check-in, carrying the per-check-in score and topic sentiment plus the author's manager and custom properties snapshotted at check-in time. meeting_v2_id distinguishes 1:1 meeting check-ins (set) from standalone cadence check-ins (null); meeting_manager marks the manager's side of a 1:1. |
| List Custom Reward Redemptions | `listCustomRewardsRedemptions` | Returns rewards redeemed for items in the company's custom catalog (e.g. branded swag, in-house perks). Admin token required. |
| List Daily User Recognition Statistics | `listDailyUserRecognitionStatistics` | Page of daily_user_recognition_statistics rows. One row per (user, end_of_day) summarising recognition activity (peer, add-on, comment, award, celebration, incentive — given and received) for that user on that day. |
| List Monthly Company Metrics | `listMonthlyCompanyMetrics` | Page of monthly_company_metrics rows. One row per (company, month_end, feature_category, metric_name), with the computed value, the eligible-user denominator, and the cohort gating flag used for cross-customer benchmarking. |
| List Monthly Group Connections | `listMonthlyGroupConnections` | Page of monthly_group_connections rows. One row per (month_end, group_type, from_group, to_group) directed edge — recognition flow between two groups (department, location, manager_team, etc.) within a month, with interaction counts and cumulative quality score. |
| List Monthly Group Recognition Statistics | `listMonthlyGroupRecognitionStatistics` | Page of monthly_group_recognition_statistics rows. One row per (month_end, group_type, group_value) with eligibility-based participation rates, per-category given/received counts and amounts, average quality score, and Gini-style concentration metrics. A reserved group_type="company" / group_value="overall" row carries the company-wide totals. |
| List Monthly User Archetypes | `listMonthlyUserArchetypes` | Page of monthly_user_archetypes rows. One row per (user_id, month_end) carrying org-relative percentile scores (activity, connection breadth, cross-group, within-group, depth, receive ratio, quality received, etc.) and the user's assigned network archetype for the month. |
| List Monthly User Connections | `listMonthlyUserConnections` | Page of monthly_user_connections rows. One row per directed (giver, receiver, month_end) edge — peer, add-on, and comment interactions between two users within a month, with the snapshotted giver and receiver custom properties and the cross-group flags for every property dimension. |
| List Recognition Events | `listRecognitionEvents` | Page of recognition_events rows. One row per recognition (Bonus) with giver / receiver ids, amount, reason, category, taxonomy fields, snapshotted giver and receiver custom properties at recognition time, and — when available — the LLM quality score and any emoji reactions. |
| List Recognition Templates | `listRecognitionTemplates` | Page of recognition_templates rows. A per-company identity lookup table — one row per recognition template — that resolves the template_id references exposed by recognition_events back to a human-readable name. The payload is deliberately minimal. |
| List Redemptions | `listRedemptions` | Returns fulfilled redemptions for the authenticated admin's company, newest first. Non-admin tokens are rejected with 403. |
| List Resource Types (SCIM 1.1) | `scim1ListResourceTypes` | Returns the SCIM resource types supported by Bonusly. |
| List Resource Types (SCIM 2.0) | `scim2ListResourceTypes` | Returns one entry: User. Bonusly does not implement Group. |
| List Schemas (SCIM 1.1) | `scim1ListScimSchemas` | Returns the SCIM schemas supported by Bonusly. |
| List Schemas (SCIM 2.0) | `scim2ListSchemas` | Returns the SCIM schemas Bonusly advertises: core User plus the Bonusly URN extension. IdPs use this to auto-populate the list of target attributes during mapping setup. |
| List User Achievements | `listUserAchievements` | User's Achievements. |
| List User Bonuses | `listUserBonuses` | User's Bonuses. |
| List User Redemptions | `listUserRedemptions` | User's Redemptions. |
| List Users | `listUsers` | Returns a paginated list of users in the authenticated user's company. |
| List Users (SCIM 1.1) | `scim1ListScimUsers` | Returns the company's users in SCIM 1.1 format. Supports pagination via startIndex/count and filtering via filter. |
| List Users (SCIM 2.0) | `scim2ListUsers` | Returns a paginated SCIM ListResponse of users in the authenticated company. Supports the SCIM filter grammar (per RFC 7644 §3.4.2.2) for the attributes listed under "Filterable attributes" below. |
| List Weekly Group Check-In Statistics | `listWeeklyGroupCheckInStatistics` | Page of weekly_group_check_in_statistics rows. One row per (week_end, group_type, group_value) with eligibility-based check-in participation rates, check-in counts, score aggregates (average, high, low), and per-topic sentiment frequencies. A reserved group_type="company" / group_value="overall" row carries the company-wide totals. |
| List Weighted Monthly User Connections | `listMonthlyUserConnectionsWeighted` | Page of monthly_user_connections_weighted rows. One row per undirected (user_id_a, user_id_b, month_end) user-pair edge (canonically ordered) with pre-computed forward, reverse, reciprocity, and combined weights — the input to community detection on the collaboration graph. |
| Patch User (SCIM 2.0) | `scim2PatchUser` | Applies a SCIM PATCH operation set (RFC 7644 §3.5.2) to the user. Supports Add, Replace, and Remove operations against any writable attribute in either schema. Bonusly tolerates a few real-world IdP quirks: - **String boolean active** — Microsoft Entra sends "True" / "False" strings instead of JSON booleans. We accept either (along with 1/0, yes/no, t/f — case-insensitive). - **Leading whitespace in URN paths** — Entra occasionally emits " urn:..." on Add operations. We strip the leading space rather than rejecting the operation. Activation / deactivation policy refusals (last admin, etc.) surface as 422 so the IdP doesn't drift into thinking the toggle stuck. |
| Patch User Activation Status (SCIM 1.1) | `scim1PatchScimUserActivationStatus` | Same handler as DELETE on this path — Okta's SCIM client uses PATCH for activate/deactivate so the route accepts both verbs. Request body, response shape, and error codes match DELETE. |
| Queue Analytics Users Snapshot | `createAnalyticsUsersSnapshot` | Queues a one-shot NDJSON snapshot of the analytics_users dataset for the requesting company. Idempotent per company while a snapshot is in-flight; up to 3 in-flight snapshots per company are allowed. |
| Queue Check-In Events Snapshot | `createCheckInEventsSnapshot` | Queues a one-shot NDJSON snapshot of the check_in_events dataset for the requesting company. |
| Queue Daily User Recognition Statistics Snapshot | `createDailyUserRecognitionStatisticsSnapshot` | Queues a one-shot NDJSON snapshot of the daily_user_recognition_statistics dataset for the requesting company. |
| Queue Monthly Company Metrics Snapshot | `createMonthlyCompanyMetricsSnapshot` | Queues a one-shot NDJSON snapshot of the monthly_company_metrics dataset for the requesting company. |
| Queue Monthly Group Connections Snapshot | `createMonthlyGroupConnectionsSnapshot` | Queues a one-shot NDJSON snapshot of the monthly_group_connections dataset for the requesting company. |
| Queue Monthly Group Recognition Statistics Snapshot | `createMonthlyGroupRecognitionStatisticsSnapshot` | Queues a one-shot NDJSON snapshot of the monthly_group_recognition_statistics dataset for the requesting company. |
| Queue Monthly User Archetypes Snapshot | `createMonthlyUserArchetypesSnapshot` | Queues a one-shot NDJSON snapshot of the monthly_user_archetypes dataset for the requesting company. |
| Queue Monthly User Connections Snapshot | `createMonthlyUserConnectionsSnapshot` | Queues a one-shot NDJSON snapshot of the monthly_user_connections dataset for the requesting company. |
| Queue Recognition Events Snapshot | `createRecognitionEventsSnapshot` | Queues a one-shot NDJSON snapshot of the recognition_events dataset for the requesting company. |
| Queue Recognition Templates Snapshot | `createRecognitionTemplatesSnapshot` | Queues a one-shot NDJSON snapshot of the recognition_templates dataset for the requesting company. |
| Queue Weekly Group Check-In Statistics Snapshot | `createWeeklyGroupCheckInStatisticsSnapshot` | Queues a one-shot NDJSON snapshot of the weekly_group_check_in_statistics dataset for the requesting company. |
| Queue Weighted Monthly User Connections Snapshot | `createMonthlyUserConnectionsWeightedSnapshot` | Queues a one-shot NDJSON snapshot of the monthly_user_connections_weighted dataset for the requesting company. |
| Replace User (SCIM 1.1) | `scim1UpdateScimUser` | Updates an active, existing user in Bonusly. Per-field semantics mirror the create endpoint. If a user already exists with the specified userName, returns 409. |
| Replace User (SCIM 2.0) | `scim2ReplaceUser` | Replaces the user's mutable attributes with the supplied body. Attributes the IdP omits are **not cleared** — Bonusly preserves existing values that the IdP doesn't manage. This matches what most IdPs (including Microsoft Entra) expect from a SCIM 2.0 target and prevents an IdP-side schema gap from wiping Bonusly-only fields. If the payload sets active: false, the user is deactivated after the attribute replacement is persisted. Activation / deactivation that violates a Bonusly policy (last admin, aliased user, integration-managed company) is rejected with 422. |
| Stage File Upload | `createUpload` | Creates a staged upload and returns a pre-signed S3 URL for the client to PUT the file to directly. The file_url can then be used in resource mutations. Requires the uploads:write scope. |
| Update Award | `updateAward` | Partially updates an award. Only provided fields are changed. Can update name, description, conditions, budget, amount, message, visibility, state, and approval process. Requires the awards:administer scope and awards admin permission. |
| Update Bonus | `updateBonus` | Updates the reason of an existing bonus. Subject to the BonusEditing policy — bonuses are only editable within a limited window after creation, and admins can edit other users' bonuses within the same window. |
| Update Company | `updateCompany` | Updates the authenticated admin's company. Admin token required. Sends name, show_bonus_amounts, and/or custom_user_properties; any other parameter is rejected with 400. |
| Update Profile | `updateProfile` | Updates profile fields for the user associated with the bearer token. All fields are optional — only provided fields are updated. Avatar changes are subject to the company's avatar uploading policy. If the company disallows avatar uploads, providing image returns 403. Requires the user:write scope and a user-scoped token. |
| Update User | `updateUser` | Updates a user. Requires an admin (or company-scoped) access token. Pass status: archived to deactivate or status: active to reactivate. |
