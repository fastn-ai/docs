---
description: "The Chess.com Published-Data API (PubAPI) is a free read-only API with public Chess.com data: player profiles, stats, current and archived games (JSON and…"
hidden: true
---

# Chess.com Published-Data API

<img src="../../.gitbook/assets/connectors/lg/chess-com-pub-api.png" alt="Chess.com Published-Data API logo">

The Chess.com Published-Data API (PubAPI) is a free read-only API with public Chess.com data: player profiles, stats, current and archived games (JSON and PGN), clubs, team matches, tournaments, titled players, countries, daily puzzles, streamers and leaderboards. No API key needed; requests should be made one at a time.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [chess.com](https://chess.com) |
| **Authentication** | No authentication |
| **Slug** | `chessComPubApi` |

## Use it

Add Chess.com Published-Data API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.chessComPubApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Club | `getClub` | Get a club's profile: name, description, country, members count, admins and visibility (GET /pub/club/{club}). Docs: https://www.chess.com/news/view/published-data-api |
| Get Country | `getCountry` | Get a country profile by ISO 3166 alpha-2 code (Chess.com also uses XA-XZ for some regions) (GET /pub/country/{iso}). Docs: https://www.chess.com/news/view/published-data-api |
| Get Daily Puzzle | `getDailyPuzzle` | Get today's daily puzzle with FEN, PGN and image (GET /pub/puzzle). Docs: https://www.chess.com/news/view/published-data-api |
| Get Daily Team Match | `getDailyTeamMatch` | Get a Daily Chess team match with its teams, boards and settings (GET /pub/match/{match_id}). Docs: https://www.chess.com/news/view/published-data-api |
| Get Daily Team Match Board | `getDailyTeamMatchBoard` | Get one board of a Daily Chess team match with its scores and games (GET /pub/match/{match_id}/{board}). Docs: https://www.chess.com/news/view/published-data-api |
| Get Leaderboards | `getLeaderboards` | Get the top 50 players for daily, live, rapid, blitz, bullet, variants and tactics leaderboards (GET /pub/leaderboards). Docs: https://www.chess.com/news/view/published-data-api |
| Get Live Team Match | `getLiveTeamMatch` | Get a Live Chess team match with its teams, boards and settings (GET /pub/match/live/{match_id}). Docs: https://www.chess.com/news/view/published-data-api |
| Get Live Team Match Board | `getLiveTeamMatchBoard` | Get one board of a Live Chess team match with its scores and games (GET /pub/match/live/{match_id}/{board}). Docs: https://www.chess.com/news/view/published-data-api |
| Get Player Monthly Games | `getPlayerMonthlyGames` | Get all finished Live and Daily games of a player for one month (GET /pub/player/{username}/games/{year}/{month}). Docs: https://www.chess.com/news/view/published-data-api |
| Get Player Monthly Games PGN | `getPlayerMonthlyGamesPgn` | Download all of a player's finished games for one month as a multi-game PGN file (GET /pub/player/{username}/games/{year}/{month}/pgn). Docs: https://www.chess.com/news/view/published-data-api |

<details>

<summary>See 19 more actions</summary>

* **Get Player Profile** `getPlayer`: Get a player's profile: name, title, avatar, country, followers, status, joined and last online (GET /pub/player/{username}). Docs: https://www.chess.com/news/view/published-data-api
* **Get Player Stats** `getPlayerStats`: Get a player's ratings, win/loss/draw records and best results per game type, plus puzzle and puzzle rush scores (GET /pub/player/{username}/stats). Docs: https://www.chess.com/news/view/published-data-api
* **Get Random Puzzle** `getRandomPuzzle`: Get a random daily puzzle (cached about 15 seconds) (GET /pub/puzzle/random). Docs: https://www.chess.com/news/view/published-data-api
* **Get Tournament** `getTournament`: Get a tournament's details, settings, players and round URLs (GET /pub/tournament/{tournament}). Docs: https://www.chess.com/news/view/published-data-api
* **Get Tournament Round** `getTournamentRound`: Get one round of a tournament with its groups and players (GET /pub/tournament/{tournament}/{round}). Docs: https://www.chess.com/news/view/published-data-api
* **Get Tournament Round Group** `getTournamentRoundGroup`: Get one group of a tournament round with its players and games (GET /pub/tournament/{tournament}/{round}/{group}). Docs: https://www.chess.com/news/view/published-data-api
* **List Club Matches** `listClubMatches`: List a club's finished, in-progress and registered team matches (GET /pub/club/{club}/matches). Docs: https://www.chess.com/news/view/published-data-api
* **List Club Members** `listClubMembers`: List a club's members grouped by activity (weekly, monthly, all time) (GET /pub/club/{club}/members). Docs: https://www.chess.com/news/view/published-data-api
* **List Country Clubs** `listCountryClubs`: List the URLs of clubs based in a country (GET /pub/country/{iso}/clubs). Docs: https://www.chess.com/news/view/published-data-api
* **List Country Players** `listCountryPlayers`: List the usernames of players who list a country as their home (GET /pub/country/{iso}/players). Docs: https://www.chess.com/news/view/published-data-api
* **List Player Clubs** `listPlayerClubs`: List the clubs a player belongs to (GET /pub/player/{username}/clubs). Docs: https://www.chess.com/news/view/published-data-api
* **List Player Current Daily Games** `listPlayerDailyGames`: List the Daily Chess games a player is currently playing (GET /pub/player/{username}/games). Docs: https://www.chess.com/news/view/published-data-api
* **List Player Game Archives** `listPlayerGameArchives`: List the monthly archive URLs of a player's finished games (GET /pub/player/{username}/games/archives). Docs: https://www.chess.com/news/view/published-data-api
* **List Player Games To Move** `listPlayerGamesToMove`: List the Daily Chess games where it is the player's turn, with move-by deadline (GET /pub/player/{username}/games/to-move). Docs: https://www.chess.com/news/view/published-data-api
* **List Player Live Games by Time Control** `listPlayerLiveGamesByTimeControl`: List a player's finished Live Chess games for one time control (base seconds and increment) (GET /pub/player/{username}/games/live/{basetime}/{increment}). Docs: https://www.chess.com/news/view/published-data-api
* **List Player Team Matches** `listPlayerMatches`: List a player's finished, in-progress and registered team matches (GET /pub/player/{username}/matches). Docs: https://www.chess.com/news/view/published-data-api
* **List Player Tournaments** `listPlayerTournaments`: List a player's finished, in-progress and registered tournaments (GET /pub/player/{username}/tournaments). Docs: https://www.chess.com/news/view/published-data-api
* **List Streamers** `listStreamers`: List Chess.com streamers with their Twitch and other platform URLs and live status (GET /pub/streamers). Docs: https://www.chess.com/news/view/published-data-api
* **List Titled Players** `listTitledPlayers`: List the usernames of all players holding a title (GET /pub/titled/{title}). Docs: https://www.chess.com/news/view/published-data-api

</details>
