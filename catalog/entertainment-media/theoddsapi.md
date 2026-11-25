---
description: "The Odds API provides sports betting odds and scores from bookmakers. Get live and historical odds, events, markets and scores."
hidden: true
---

# The Odds API

<img src="../../.gitbook/assets/connectors/lg/theoddsapi.png" alt="The Odds API logo">

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [the-odds-api.com](https://the-odds-api.com) |
| **Authentication** | API key |
| **Slug** | `theoddsapi` |

## Setup

Your customers enter their API key for The Odds API when they connect. Nothing else needs setting up.

## Use it

Add The Odds API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.theoddsapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Event Markets</td><td><code>getEventMarkets</code></td><td>Returns the list of market keys currently offered by each bookmaker for a single event, without prices, so that a follow-up odds request can be scoped to the markets that actually exist. Costs one credit.</td></tr><tr><td>Get Event Odds</td><td><code>getEventOdds</code></td><td>Returns odds for a single event, including the additional markets such as player props, alternate lines and period markets that are not available from the main odds endpoint. Costs one credit per unique market returned per region requested.</td></tr><tr><td>Get Historical Event Odds</td><td><code>getHistoricalEventOdds</code></td><td>Returns a point-in-time snapshot of the odds for a single event, including additional and player markets, as they stood at a given timestamp. Requires a paid plan; Starter and free keys receive HTTP 401. Costs ten credits per market per region requested.</td></tr><tr><td>Get Historical Odds</td><td><code>getHistoricalOdds</code></td><td>Returns a point-in-time snapshot of games and bookmaker odds for a sport as they stood at a given timestamp. Requires a paid plan; Starter and free keys receive HTTP 401. Costs ten credits per market per region requested.</td></tr><tr><td>Get Odds</td><td><code>getOdds</code></td><td>Returns upcoming and live games for a sport together with bookmaker odds for the requested featured markets and regions. Costs one credit per market per region requested.</td></tr><tr><td>Get Scores</td><td><code>getScores</code></td><td>Returns live and recently completed scores for a sport, and optionally final scores for games completed in the last one to three days. Costs one credit, or two credits when Days From is supplied.</td></tr><tr><td>List Events</td><td><code>listEvents</code></td><td>Returns the upcoming and live games for a sport without any odds attached, which is useful for discovering event IDs. This request does not consume any API credits.</td></tr><tr><td>List Historical Events</td><td><code>listHistoricalEvents</code></td><td>Returns a point-in-time snapshot of the games scheduled for a sport as they stood at a given timestamp, without odds. Requires a paid plan; Starter and free keys receive HTTP 401. Costs one credit when events are returned.</td></tr><tr><td>List Participants</td><td><code>listParticipants</code></td><td>Returns the teams or individual participants that compete in a given sport or competition. Costs one credit.</td></tr><tr><td>List Sports</td><td><code>listSports</code></td><td>Returns the catalogue of sports and competitions covered by The Odds API, including whether each is currently in season. This request does not consume any API credits.</td></tr></tbody></table>

## Events

The Odds API has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
