---
description: "Chess.com shares public data from its chess site. Get player profiles, clubs, team matches, leaderboards and the daily puzzle."
hidden: true
---

# Chess.com Published-Data API

<img src="../../.gitbook/assets/connectors/lg/chess-com-pub-api.png" alt="Chess.com Published-Data API logo">

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [chess.com](https://chess.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `chessComPubApi` |

## Setup

Chess.com Published-Data API needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Chess.com Published-Data API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.chessComPubApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Club</td><td><code>getClub</code></td><td>Get a club's profile: name, description, country, members count, admins and visibility Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Country</td><td><code>getCountry</code></td><td>Get a country profile by ISO 3166 alpha-2 code (Chess.com also uses XA-XZ for some regions) Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Daily Puzzle</td><td><code>getDailyPuzzle</code></td><td>Get today's daily puzzle with FEN, PGN and image Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Daily Team Match</td><td><code>getDailyTeamMatch</code></td><td>Get a Daily Chess team match with its teams, boards and settings Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Daily Team Match Board</td><td><code>getDailyTeamMatchBoard</code></td><td>Get one board of a Daily Chess team match with its scores and games Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Leaderboards</td><td><code>getLeaderboards</code></td><td>Get the top 50 players for daily, live, rapid, blitz, bullet, variants and tactics leaderboards Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Live Team Match</td><td><code>getLiveTeamMatch</code></td><td>Get a Live Chess team match with its teams, boards and settings Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Live Team Match Board</td><td><code>getLiveTeamMatchBoard</code></td><td>Get one board of a Live Chess team match with its scores and games Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Player Monthly Games</td><td><code>getPlayerMonthlyGames</code></td><td>Get all finished Live and Daily games of a player for one month Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Player Monthly Games PGN</td><td><code>getPlayerMonthlyGamesPgn</code></td><td>Download all of a player's finished games for one month as a multi-game PGN file Docs: https://www.chess.com/news/view/published-data-api</td></tr></tbody></table>

<details>

<summary>View 19 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Player Profile</td><td><code>getPlayer</code></td><td>Get a player's profile: name, title, avatar, country, followers, status, joined and last online Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Player Stats</td><td><code>getPlayerStats</code></td><td>Get a player's ratings, win/loss/draw records and best results per game type, plus puzzle and puzzle rush scores Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Random Puzzle</td><td><code>getRandomPuzzle</code></td><td>Get a random daily puzzle (cached about 15 seconds) Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Tournament</td><td><code>getTournament</code></td><td>Get a tournament's details, settings, players and round URLs Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Tournament Round</td><td><code>getTournamentRound</code></td><td>Get one round of a tournament with its groups and players Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>Get Tournament Round Group</td><td><code>getTournamentRoundGroup</code></td><td>Get one group of a tournament round with its players and games Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Club Matches</td><td><code>listClubMatches</code></td><td>List a club's finished, in-progress and registered team matches Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Club Members</td><td><code>listClubMembers</code></td><td>List a club's members grouped by activity (weekly, monthly, all time) Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Country Clubs</td><td><code>listCountryClubs</code></td><td>List the URLs of clubs based in a country Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Country Players</td><td><code>listCountryPlayers</code></td><td>List the usernames of players who list a country as their home Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Player Clubs</td><td><code>listPlayerClubs</code></td><td>List the clubs a player belongs to Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Player Current Daily Games</td><td><code>listPlayerDailyGames</code></td><td>List the Daily Chess games a player is currently playing Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Player Game Archives</td><td><code>listPlayerGameArchives</code></td><td>List the monthly archive URLs of a player's finished games Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Player Games To Move</td><td><code>listPlayerGamesToMove</code></td><td>List the Daily Chess games where it is the player's turn, with move-by deadline Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Player Live Games by Time Control</td><td><code>listPlayerLiveGamesByTimeControl</code></td><td>List a player's finished Live Chess games for one time control (base seconds and increment) Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Player Team Matches</td><td><code>listPlayerMatches</code></td><td>List a player's finished, in-progress and registered team matches Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Player Tournaments</td><td><code>listPlayerTournaments</code></td><td>List a player's finished, in-progress and registered tournaments Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Streamers</td><td><code>listStreamers</code></td><td>List Chess.com streamers with their Twitch and other platform URLs and live status Docs: https://www.chess.com/news/view/published-data-api</td></tr><tr><td>List Titled Players</td><td><code>listTitledPlayers</code></td><td>List the usernames of all players holding a title Docs: https://www.chess.com/news/view/published-data-api</td></tr></tbody></table>

</details>

## Events

Chess.com Published-Data API has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
