---
description: "Lumify is an agent-ready sports intelligence API covering MLB, NBA, NFL, NHL, NCAAF, NCAAB, tennis and soccer."
hidden: true
---

# Lumify

<img src="../../.gitbook/assets/connectors/lg/lumify.png" alt="Lumify logo">

Lumify is an agent-ready sports intelligence API covering MLB, NBA, NFL, NHL, NCAAF, NCAAB, tennis and soccer. This connector covers the full Lumify v1 API: sports, seasons, teams, players and events; live scores and event statistics; betting odds, line-movement history, period odds, player props, team props and public betting splits; bet intelligence, expected-value scans and forecasts; natural-language search and entity resolution; slip grading; credit and API-key management; and signed webhook subscriptions with delivery history.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [lumify.ai](https://lumify.ai) |
| **Authentication** | Credentials you enter |
| **Slug** | `lumify` |

## Use it

Add Lumify from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.lumify.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create API Key | `createApiKey` | Creates a new Lumify API key without using the dashboard. The secret value is returned only once in this response, so store it immediately. |
| Create Webhook Subscription | `createWebhookSubscription` | Creates a webhook subscription so Lumify pushes signed score, status, line-move or injury events to your HTTPS endpoint. The signing secret is returned once on create and cannot be read back, so store it to verify the Lumify-Signature header. Including line_move requires a sport or an event identifier. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | Deletes a webhook subscription so Lumify stops delivering to it. Returns 404 when the subscription does not belong to the caller. |
| Estimate Credit Cost | `estimateCreditCost` | Estimates the credit cost of one or more planned calls before you make them, so an agent can budget a workload. Estimating is itself free. |
| Get Credit Balance | `getCreditBalance` | Returns the caller's credit balance and usage for the current billing period, including the plan tier, the included limit, any bonus credits and the remaining total. |
| Get Event | `getEvent` | Retrieves a single event by Lumify event identifier. Optionally inline current odds and bet intelligence into the same response at no extra credit cost, scoped to a chosen bookmaker. |
| Get Event Injuries | `getEventInjuries` | Returns late-breaking player injury and availability status for an upcoming event, written by Lumify's automated monitoring pipeline. Beta coverage is NFL and MLB. Always returns 200 when the event exists; check Available to see whether a first report has been written. |
| Get Event Intelligence | `getEventIntelligence` | Returns Lumify's bet intelligence for an event: per-bet confidence scores, signal breakdowns, vig-stripped fair prices, line-shopping edges by book and structured rationale, plus a match overview and any forecasted wagers. |
| Get Event Odds | `getEventOdds` | Returns current moneyline, spread and total betting odds for an event across the requested sportsbooks. Defaults to Pinnacle; pass 'all' or a comma-separated list for multiple books, and set Include Alternates to add alternate spread and total rungs. |
| Get Event Period Odds | `getEventPeriodOdds` | Returns first-half, first-five-innings or first-set lines for an event and grades them against the live period score. Supported for NFL, NCAAF, NBA, NCAAB, MLB, soccer and tennis; other sports return HTTP 400. |

<details>

<summary>See 32 more actions</summary>

* **Get Event Player Props** `getEventPlayerProps`: Returns player-prop lines for an event and grades each over, under or push against the live player box score. Supported for NFL, NCAAF, NBA, NCAAB, NHL, MLB and soccer; other sports return HTTP 400.
* **Get Event Score** `getEventScore`: Returns the current score for an event, with per-participant totals, period-by-period scoring and the live period and clock.
* **Get Event Splits** `getEventSplits`: Returns public betting splits for an event: the percentage of tickets and of handle on each side of the moneyline, spread and total, as a cross-book consensus and per bookmaker. Available for MLB, NBA, NHL, NFL, NCAAF and NCAAB; tennis and soccer are not covered.
* **Get Event Statistics** `getEventStatistics`: Returns deterministic team or match statistics for an event: form, records and head-to-head aggregates derived from completed results. Payload shapes are sport-specific and team-keyed for every sport except tennis. Supported for soccer, MLB, tennis, NFL, NCAAF, NBA, NCAAB and NHL; other sports return HTTP 400.
* **Get Event Team Props** `getEventTeamProps`: Returns team-total lines for an event and grades each over, under or push against the live participant scores. Supported for NFL, NCAAF, MLB and soccer; other sports return HTTP 400.
* **Get Events Batch** `getEventsBatch`: Fetches up to 25 events by identifier in a single round-trip, optionally inlining odds and bet intelligence on each. Duplicate identifiers are billed once and identifiers that do not exist cost nothing and come back under the not-found list.
* **Get Health** `getHealth`: Returns the current health of the Lumify API, including database and cache status and cache memory usage.
* **Get Player** `getPlayer`: Retrieves a single player by Lumify player identifier, including biographical details, position, current team and rankings.
* **Get Team** `getTeam`: Retrieves a single team by its Lumify team identifier, including conference, division and home venue.
* **Grade Slip** `gradeSlip`: Grades settleable player-prop legs as over, under or push against the live box score. Supply structured legs for a deterministic result, or free text that Lumify interprets and grades only when the player and event resolve uniquely. This reports outcomes on completed play; it is not a wagering service.
* **Issue Trial Key** `issueTrialKey`: Issues a throwaway trial API key with 100 lifetime credits and a 14-day expiry, one per network every seven days. It requires a valid Cloudflare Turnstile token obtained from the widget on the Lumify docs site, so it backs that page's button rather than a server-side integration; use a dashboard key for a persistent integration.
* **List API Keys** `listApiKeys`: Lists the caller's Lumify API keys as metadata only. Secret values are shown once at creation and are never returned again.
* **List Credit Packs** `listCreditPacks`: Lists the credit packs that can be purchased to top up the account, with their credit amounts and prices.
* **List Estimate Tools** `listEstimateTools`: Lists the tool names Estimate Credit Cost understands, grouped by how each is priced, so an agent can discover what it can price and what a call will cost.
* **List EV Opportunities** `listEvOpportunities`: Scans a sport for main-line positive expected-value opportunities, packaging the price gap against sharp consensus as an EV percentage with a Kelly stake. Available for the predictive-framework sports: soccer, MLB, tennis, NFL and NCAAF. Tennis totals return HTTP 400.
* **List Event Odds History** `listEventOddsHistory`: Returns the recorded line-movement history for an event, newest movements first. Use it to diff odds over time without holding an open connection.
* **List Events** `listEvents`: Lists events (games and matches) across every covered sport. Filter by sport, league, status, a single date or a date range, season, or participating team; optionally inline participants and scores; and page with the After ID cursor.
* **List Forecasts** `listForecasts`: Lists Lumify's forecasted wagers for a sport and slate date, with hit probability, confidence interval, sufficiency, reliability and the model drivers behind each. Prop forecasts cover MLB, NCAAF, NFL, NBA, NCAAB and NHL; tennis publishes main-line forecasts.
* **List Player Events** `listPlayerEvents`: Lists the events a given player appears in, optionally restricted by event status or a date window, with cursor pagination. Team-sport events list teams rather than individual players as participants, so this returns rows only where Lumify records a per-player participation.
* **List Players** `listPlayers`: Lists players with their biographical details, position, current team and (for tennis) ATP/WTA rankings. Filter by sport, country, active status, ranked status or a partial name search, and page with the After ID cursor.
* **List Seasons** `listSeasons`: Lists competition seasons. By default only currently active seasons are returned; set Current Only to false to include historical seasons.
* **List Sports** `listSports`: Lists the sports Lumify covers, each with its leagues and the league's current season.
* **List Teams** `listTeams`: Lists teams with their identity, conference, division and home venue. Filter by sport, league, conference, division, country, active status or a partial name search, and page with the After ID cursor.
* **List Webhook Deliveries** `listWebhookDeliveries`: Lists every delivery attempt for a webhook subscription, newest first, including automatic retries. Retries are linked to the attempt they retried through the parent delivery identifier, so a full chain can be reconstructed. Filter by success, exhausted retries or event type.
* **List Webhook Subscriptions** `listWebhookSubscriptions`: Lists the caller's webhook subscriptions with their callback URL, subscribed event types, any sport or event restriction and whether each is active.
* **Purchase Credit Pack** `purchaseCreditPack`: Purchases a credit pack and charges the payment method on file. This spends real money, so confirm the pack identifier with List Credit Packs before calling it.
* **Resolve Event** `resolveEvent`: Resolves an event identity from a direct identifier, or from a player or team plus a date window, to a Lumify event identifier. Returns an ambiguous result with candidates rather than guessing.
* **Resolve Player** `resolvePlayer`: Resolves a messy player name such as 'J. Chase' to a Lumify player identifier, optionally narrowed by sport, team, event, position or catalog-key clues. Returns an ambiguous result with candidates rather than guessing. Run this before grading a slip.
* **Resolve Team** `resolveTeam`: Resolves a messy team string - a nickname, abbreviation, metro or alias - to a Lumify team identifier, optionally narrowed by sport, league, event or player clues. Returns an ambiguous result with candidates rather than guessing.
* **Revoke API Key** `revokeApiKey`: Revokes a Lumify API key so it can no longer authenticate. Returns 404 when the key does not belong to the caller. Revoking is immediate and cannot be undone.
* **Search Events By Query** `searchEventsByQuery`: Maps a natural-language phrase such as 'live nfl games today' onto the same filters List Events accepts and runs that query. Results are identical to calling List Events directly with the parsed filters.
* **Stream Event Score Updates** `streamEventScoreUpdates`: Opens a Server-Sent Events stream of live score and status changes for an event. Each API key may hold up to five concurrent streams and a connection closes after five minutes, sending a reconnect frame first. This endpoint returns an open event stream rather than a single JSON document, so it suits a long-lived client rather than a one-shot call.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Injury Status Changed | `injury` | Fires on a material or critical player availability transition for an upcoming event, such as a first-seen out or a change from questionable to out. Routine information-level tags and unchanged reconfirmations never fire, and transitions are de-duplicated. Beta coverage is NFL and MLB. Each delivery costs half a credit. Verify Lumify-Signature downstream with the per-subscription signing secret. |
| Line Moved | `line_move` | Fires once per event per ingest cycle, roughly every ten minutes, when a main line's point changes or its American price moves by at least five cents. Only main lines on live or imminent games are pushed; alternate rungs and one-to-four-cent juice ticks are not. Lumify rejects a platform-wide line_move subscription, so you MUST supply either the Sport or the Event ID input when subscribing to this event. Verify Lumify-Signature downstream with the per-subscription signing secret. |
| Score Changed | `score` | Fires when the score of an event changes. Supply the optional Sport input to restrict deliveries to one sport, or the Event ID input to restrict them to a single event. This is the highest-frequency event type and costs the least per delivery. Signature verification is not configured here: Lumify issues a separate signing secret per subscription (returned once by Create Webhook Subscription) and the fastn engine can only resolve one connector-level HMAC secret, so verify Lumify-Signature downstream using the secret you stored at subscribe time. |
| Status Changed | `status` | Fires when an event transitions status, for example from scheduled to in progress or to final. Supply the optional Sport or Event ID input to narrow deliveries. Signature verification is not configured here: verify Lumify-Signature downstream with the per-subscription signing secret returned by Create Webhook Subscription. |
