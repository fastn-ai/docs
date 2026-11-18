---
description: "Pointagram sales gamification platform."
hidden: true
---

# Pointagram

<img src="../../.gitbook/assets/connectors/lg/pointagram.png" alt="Pointagram logo">

Pointagram sales gamification platform. Manage players, teams, score series and point scoring, read competitions and leaderboards, and operate the reward store (items, settings, purchases) through the Pointagram Custom API 2.0.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [pointagram.com](https://pointagram.com) |
| **Authentication** | API key |
| **Slug** | `pointagram` |

## Use it

Add Pointagram from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pointagram.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Player To Team | `addPlayerToTeam` | Adds an existing player to a Pointagram team. Identify the player with exactly one of player_id, player_email or player_external_id. Returns status Ok with message 'Player added to team'. Responds 409 if no player identifier is supplied. |
| Add Score | `addScore` | Adds points to a Pointagram score series for a player. Identify the player with at least one of player_id, player_name, player_email or player_external_id, name the target series with scoreseries_id or scoreseries_name, and supply either points or pointtype_name. Returns the transaction id as insid. Scoring is visible on live leaderboards and in the news feed. |
| Create Player | `createPlayer` | Creates a new player in Pointagram. At least player_name is required. Set offline to 1 to create the player without sending them an invitation email; offline 0 creates an online player and Pointagram emails them an invitation. Returns the new profile_id. Responds 409 with 'Player already exists.' if a matching player is present. |
| Create Reward Store Purchase | `createRewardStorePurchase` | Places an order in the Pointagram reward store for a player and returns the new purchase_id. This spends the player's earned currency balance. Admins can order on behalf of any profile; non-admins can only order for themselves. Use Revoke Reward Store Purchase to reverse an order. |
| Create Team | `createTeam` | Creates a new team in Pointagram and returns its team_id. An icon is mandatory: use one of the standard Pointagram icons (Bears.png, Bulls.png, Cobras.png, Lions.png, Raccons.png, Sharks.png, Tigers.png) or the file name of a custom icon already uploaded in the Add Team settings. Note: the Pointagram Custom API has no delete-team endpoint, so a team created here can only be removed from the Pointagram web app. |
| Delete Player | `deletePlayer` | Soft-deletes a player in Pointagram by profile id. To fully remove and anonymize the player, look up deleted players in the Pointagram web app and anonymize them there. Admin users cannot be removed: calls targeting an admin are ignored. An unknown id returns HTTP 200 with message 'Player not found.' |
| Get Competition | `getCompetition` | Fetches one Pointagram competition by id and returns its full configuration: name, start and end dates, target and winner rules, grouping mode and public access key. An unknown id returns HTTP 200 with message 'Competition not found' and data null. |
| Get Player | `getPlayer` | Fetches a single player from Pointagram by profile id. Returns the player's id, name, email address, external id, admin flag and avatar. An unknown id returns HTTP 200 with message 'Player not found' and data false. |
| Get Reward Store Item | `getRewardStoreItem` | Fetches one item from the Pointagram reward store by item id, as seen by the given profile. Returns the item's name, description, price, currency, stock, publish phase, availability dates, tags and image URL. |
| Get Reward Store Settings | `getRewardStoreSettings` | Fetches the settings of the Pointagram reward store visible to a given profile: store id and name, whether it is active, whether the caller may edit it, the caller's currency balances and their order count. Requires profileid. Returns HTTP 200 with status Error and message 'Store not found' when the organization has no reward store configured. |
| Get Score Series | `getScoreSeries` | Fetches one Pointagram score series by id and returns its name, singular and plural point names and icon. An unknown id returns HTTP 200 with message 'Scoreseries not found' and data null. |
| Get Team | `getTeam` | Fetches a single Pointagram team by id and returns its id, name, icon and icon URL. An unknown id returns HTTP 200 with message 'Team not found' and data false. |
| List Competition Players | `listCompetitionPlayers` | Fetches the leaderboard of a Pointagram competition: every participating player with their profile id, name, individual target, current score, rank and whether the rank is locked. |
| List Competitions | `listCompetitions` | Fetches competitions in Pointagram, optionally narrowed to one player, one competition id or one access key. Returns each competition's id, name, start and end dates, target settings, winner rule, grouping mode and access key. |
| List Players | `listPlayers` | Fetches players in the Pointagram organization, with optional search and pagination. Returns an array of players with id, name, email address, external id and avatar, plus a pagination block whose next_offset feeds the offset input of the next page. |
| List Reward Store Items | `listRewardStoreItems` | Fetches all items available in the Pointagram reward store for a given profile, optionally restricted to one store. Returns each item's id, name, description, price, currency, stock, publish phase, availability dates, tags and image URL. |
| List Reward Store Purchases | `listRewardStorePurchases` | Fetches orders and purchases from the Pointagram reward store. Without viewmember it returns only the calling profile's own purchases; pass a group member id to see that member's orders, or 'all' for every purchase. Returns each order's id, item, quantity, buyer, delivery status and dates. |
| List Score Series | `listScoreSeries` | Fetches all score series defined in the Pointagram organization. A score series is a point account such as Sales, Calls or Coins. Returns each series' id, name, singular and plural point names and icon. |
| List Score Series History | `listScoreSeriesHistory` | Fetches the scoring history of a Pointagram score series, with optional filters on tags, point types, teams, players, time window and revoked transactions. Returns each transaction's id, player, score, comment and timestamp plus a pagination block. |
| List Score Series Point Types | `listScoreSeriesPointTypes` | Fetches the point types configured for a Pointagram score series. A point type is a named, fixed-value scoring rule such as 'Dollar' or 'Demo booked' that can be used instead of a raw points value when adding a score. Returns each point type's id and name. |
| List Team Players | `listTeamPlayers` | Fetches the players that belong to a Pointagram team. Returns each member's profile_id and name. An unknown team id returns HTTP 200 with status Error and message 'Team not found'. |
| List Teams | `listTeams` | Fetches all teams in the Pointagram organization. Returns each team's id, name, icon file name and full icon URL. |
| Remove Player From Team | `removePlayerFromTeam` | Removes a player from a Pointagram team. The player itself is not deleted, only their team membership. Returns status Ok with message 'Player removed from team'. Responds 409 with 'Player not found' when the player is not a member of that team. |
| Revoke Reward Store Purchase | `revokeRewardStorePurchase` | Revokes a purchase or order in the Pointagram reward store, reversing it and returning the spent currency to the player. Requires profileid as a query parameter. |
| Test Credentials | `testCredentials` | Verifies that the configured Pointagram API key and API user are valid. Returns the id and name of the Pointagram organization the credentials belong to. Use this as a connection health check. |
| Update Player | `updatePlayer` | Updates an existing Pointagram player identified by profile id. Supply only the attributes you want to change. Returns the profile_id of the updated player. |
| Update Reward Store Purchase Status | `updateRewardStorePurchaseStatus` | Changes the delivery status of a Pointagram reward store order to PURCHASED, PROCESSED or DELIVERED. The calling profile must have admin rights in Pointagram. |
| Update Team | `updateTeam` | Updates an existing Pointagram team identified by team id. Supply the attributes you want to change. Returns the team_id of the updated team. |
