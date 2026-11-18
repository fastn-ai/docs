---
description: "CollegeFootballData.com (CFBD) provides historical and advanced college football data."
hidden: true
---

# College Football Data

<img src="../../.gitbook/assets/connectors/lg/college-football-data.png" alt="College Football Data logo">

CollegeFootballData.com (CFBD) provides historical and advanced college football data. This connector covers the full CFBD REST API: games, box scores, drives, plays, rushing and passing analytics, team and player stats, ratings (SP+, SRS, Elo, FPI), polls, recruiting, rosters, coaches, venues, betting lines, NFL draft, College Football Playoff data, and API usage.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [collegefootballdata.com](https://collegefootballdata.com) |
| **Authentication** | Bearer token |
| **Slug** | `collegeFootballData` |

## Use it

Add College Football Data from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.collegeFootballData.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Adjusted Game Preview | `getAdjustedGamePreview` | Returns stored adjusted team and player metrics until game completion. Requires Patreon Tier 1. Team metrics may use the previous season; players remain current-season. |
| Get Adjusted Player Passing Stats | `getAdjustedPlayerPassingStats` | Returns opponent-adjusted player passing metrics (WEPA). Requires a CollegeFootballData Patreon subscription at Tier 1 or higher. |
| Get Adjusted Player Rushing Stats | `getAdjustedPlayerRushingStats` | Returns opponent-adjusted player rushing metrics (WEPA). Requires a CollegeFootballData Patreon subscription at Tier 1 or higher. |
| Get Adjusted Team Season Stats | `getAdjustedTeamSeasonStats` | Returns opponent-adjusted team statistics by season. Requires a CollegeFootballData Patreon subscription at Tier 1 or higher. |
| Get Advanced Box Score | `getAdvancedBoxScore` | Returns an advanced box score for a game. |
| Get Advanced Team Game Stats | `getAdvancedGameStats` | Returns advanced team offense and defense statistics (PPA, success rate, explosiveness, line yards) for individual games. |
| Get Advanced Team Season Stats | `getAdvancedSeasonStats` | Returns advanced team offense and defense statistics (PPA, success rate, explosiveness, havoc, field position) aggregated by season. |
| Get Aggregated Team Recruiting Ratings | `getAggregatedTeamRecruitingRatings` | Returns recruiting ratings aggregated by team and position group. |
| Get API Key Info | `getUserInfo` | Returns the authenticated API key's Patreon tier, enabled premium features, monthly call limit, and remaining calls. |
| Get Calendar | `getCalendar` | Returns the week-by-week season calendar. |

<details>

<summary>See 83 more actions</summary>

* **Get Cfp Games** `getCfpGames`: Returns College Football Playoff matchups for a season.
* **Get Cfp Participants** `getCfpParticipants`: Returns College Football Playoff participants for a season.
* **Get Cfp Playoff** `getCfpPlayoff`: Returns the complete College Football Playoff bracket for a season.
* **Get Coach Profile** `getCoachProfile`: Returns a coach profile with canonical identity and career totals.
* **Get Coach Seasons** `getCoachSeasons`: Returns coach-season records with attributed results and team context.
* **Get Coach Tenures** `getCoachTenures`: Returns continuous head-coaching tenures and their attributed records. Requires coachId or team; year and active only filter the results.
* **Get Coaches** `getCoaches`: Returns historical head coach records.
* **Get Conference SP** `getConferenceSP`: Returns conference-level SP+ ratings by season.
* **Get Core** `getCore`: Returns Context & Opponent-Relative Efficiency (CORE) ratings. At least one of `year` or `team` is required.
* **Get Draft Picks** `getDraftPicks`: Returns historical NFL Draft picks.
* **Get Draft Positions** `getDraftPositions`: Returns the player position categories used in NFL Draft data.
* **Get Draft Teams** `getDraftTeams`: Returns the NFL teams represented in draft data.
* **Get Drives** `getDrives`: Returns historical drive data.
* **Get Elo** `getElo`: Returns historical Elo ratings.
* **Get Expanded SRS** `getExpandedSRS`: Returns expanded Simple Rating System (SRS) ratings, including FCS teams.
* **Get Field Goal Expected Points** `getFieldGoalExpectedPoints`: Returns expected points values for field goal attempts.
* **Get FPI** `getFPI`: Returns historical Football Power Index (FPI) ratings.
* **Get Game Havoc Stats** `getGameHavocStats`: Returns team offensive and defensive havoc rates and events (front seven and defensive back) for individual games.
* **Get Game Player Stats** `getGamePlayerStats`: Returns player box score statistics by game.
* **Get Game Preview** `getGamePreview`: Returns pregame team comparisons and key players. Analysis remains available until the game is completed. Team statistics may use the previous season; players and context stay in the game season.
* **Get Game Schedule** `getGameSchedule`: Returns the active or next calendar slate, including completed games. Explicit windows require year, seasonType, and week together.
* **Get Game Team Stats** `getGameTeamStats`: Returns team box score statistics by game.
* **Get Games** `getGames`: Returns historical game data.
* **Get Kicker Points Added Above Replacement** `getKickerPaar`: Returns Points Added Above Replacement (PAAR) ratings for kickers. Requires a CollegeFootballData Patreon subscription at Tier 1 or higher.
* **Get Lines** `getLines`: Returns historical betting lines and results.
* **Get Live Plays** `getLivePlays`: Returns live play-by-play data and advanced metrics for a game. Results may be cached for up to five seconds after calculation.
* **Get Media** `getMedia`: Returns broadcast and media information for games.
* **Get Passing Plays** `getPassingPlays`: Returns enriched pass attempts with PPA, success, completion probability, and CPOE.
* **Get Play Stat Types** `getPlayStatTypes`: Returns the available play stat types.
* **Get Play Stats** `getPlayStats`: Returns player and play-stat associations, limited to 2,000 records.
* **Get Play Types** `getPlayTypes`: Returns the available play types.
* **Get Player Game Success Rates** `getPlayerGameSuccessRates`: Returns player passing and rushing success rates for individual games.
* **Get Player Passing By Game** `getPlayerPassingByGame`: Returns passer production, CPOE, advanced metrics, and pass-location breakdowns by game.
* **Get Player Passing By Season** `getPlayerPassingBySeason`: Returns passer production, CPOE, advanced metrics, and pass-location breakdowns by season.
* **Get Player Punting By Game** `getPlayerPuntingByGame`: Returns individually attributed punting and punt return production by game. Player totals do not include team-only or unattributed punts and returns, and therefore are not expected to sum to team totals.
* **Get Player Punting By Season** `getPlayerPuntingBySeason`: Returns individually attributed punting and punt return production by season. Player totals do not include team-only or unattributed punts and returns, and therefore are not expected to sum to team totals.
* **Get Player Rushing By Game** `getPlayerRushingByGame`: Returns individually attributed rusher production by game. Player totals include only guarded rusher attribution, including individually attributed sacks. They do not include team-only or unresolved attempts and therefore are not expected to sum to team totals.
* **Get Player Rushing By Season** `getPlayerRushingBySeason`: Returns individually attributed rusher production by season. Player totals include only guarded rusher attribution, including individually attributed sacks. They do not include team-only or unresolved attempts and therefore are not expected to sum to team totals.
* **Get Player Season Overview** `getPlayerSeasonOverview`: Returns a player season overview with box score, usage, and Predicted Points Added (PPA) data.
* **Get Player Season Stats** `getPlayerSeasonStats`: Returns player statistics aggregated by season, one row per player, category, and stat type.
* **Get Player Season Success Rates** `getPlayerSeasonSuccessRates`: Returns player passing and rushing success rates aggregated by season.
* **Get Player Usage** `getPlayerUsage`: Returns player usage metrics for a season.
* **Get Plays** `getPlays`: Returns historical play-by-play data.
* **Get Predicted Points** `getPredictedPoints`: Returns predicted points values by down and distance.
* **Get Predicted Points Added By Game** `getPredictedPointsAddedByGame`: Returns team Predicted Points Added (PPA) metrics by game.
* **Get Predicted Points Added By Player Game** `getPredictedPointsAddedByPlayerGame`: Returns player Predicted Points Added (PPA) metrics by game.
* **Get Predicted Points Added By Player Season** `getPredictedPointsAddedByPlayerSeason`: Returns player Predicted Points Added (PPA) metrics by season.
* **Get Predicted Points Added By Team** `getPredictedPointsAddedByTeam`: Returns team Predicted Points Added (PPA) metrics by season.
* **Get Pregame Win Probabilities** `getPregameWinProbabilities`: Returns pregame win probabilities.
* **Get Punting Plays** `getPuntingPlays`: Returns enriched punt plays with gross, return, and net yardage, field position, and punt outcomes.
* **Get Rankings** `getRankings`: Returns historical poll rankings.
* **Get Records** `getRecords`: Returns historical team records by season.
* **Get Recruits** `getRecruits`: Returns player recruiting rankings.
* **Get Returning Production** `getReturningProduction`: Returns returning production metrics by team and season.
* **Get Rushing Plays** `getRushingPlays`: Returns enriched rushing attempts. Team results include sacks, kneels, team-only attempts, and unresolved attribution. Direction eligibility identifies the ordinary-rush analysis population; eligible attempts can still have an unknown direction.
* **Get Scoreboard** `getScoreboard`: Returns current scoreboard data.
* **Get SP** `getSP`: Returns SP+ ratings by team and season.
* **Get SRS** `getSRS`: Returns Simple Rating System (SRS) ratings by team and season.
* **Get Team Matchup History** `getTeamMatchup`: Returns the head-to-head record and historical game results between two teams.
* **Get Team Passing By Game** `getTeamPassingByGame`: Returns team passing production, CPOE, advanced metrics, and pass-location breakdowns by game for offense and defense.
* **Get Team Passing By Season** `getTeamPassingBySeason`: Returns team passing production, CPOE, advanced metrics, and pass-location breakdowns by season for offense and defense.
* **Get Team Punting By Game** `getTeamPuntingByGame`: Returns team punting and punt return production by game. Punting describes the team's punts. Returning describes opponent punts and the team's returns.
* **Get Team Punting By Season** `getTeamPuntingBySeason`: Returns team punting and punt return production by season. Punting describes the team's punts. Returning describes opponent punts and the team's returns.
* **Get Team Records Against The Spread** `getTeamsAgainstTheSpread`: Returns against-the-spread (ATS) wins, losses, pushes, and average cover margin by team for a season.
* **Get Team Recruiting Rankings** `getTeamRecruitingRankings`: Returns team recruiting rankings.
* **Get Team Roster** `getRoster`: Returns historical roster data for a team and season, including player positions, measurements, hometowns, and recruit ids.
* **Get Team Rushing By Game** `getTeamRushingByGame`: Returns team rushing production by game. Team totals include sacks, kneels, team-only attempts, and unresolved attribution. Defense contains rushing production allowed.
* **Get Team Rushing By Season** `getTeamRushingBySeason`: Returns team rushing production by season. Team totals include sacks, kneels, team-only attempts, and unresolved attribution. Defense contains rushing production allowed.
* **Get Team Season Overview** `getTeamSeasonOverview`: Returns a stored full-season team overview, including postseason and garbage time.
* **Get Team Season Stats** `getTeamSeasonStats`: Returns team statistics aggregated by season, one row per team and stat name.
* **Get Team Talent Composite Rankings** `getTeamTalent`: Returns 247Sports Team Talent Composite ratings for every team in a season.
* **Get Transfer Portal** `getTransferPortal`: Returns transfer portal entries for a season.
* **Get Usage** `getUsage`: Returns recent usage for the authenticated user's shared CFB and CBB call pool. Returns `null` when the request is not authenticated.
* **Get Weather** `getWeather`: Returns historical and forecast weather data for games. Requires Patreon.
* **Get Win Probability** `getWinProbability`: Returns play-by-play win probabilities for a game.
* **List Conferences** `listConferences`: Returns college football conferences with their abbreviations, classification, and member counts.
* **List FBS Teams** `listFbsTeams`: Returns Football Bowl Subdivision (FBS) teams for a season, including conference, colors, logos, and venue location.
* **List Stat Categories** `listStatCategories`: Returns the available player and team statistical category names.
* **List Team Conference Affiliations** `listTeamConferenceAffiliations`: Returns historical team conference affiliations with start and end years.
* **List Team Conference Changes** `listTeamConferenceChanges`: Returns teams that changed conference or classification effective in a given season.
* **List Teams** `listTeams`: Returns team information, including mascots, colors, logos, venue location, and conference affiliations.
* **List Venues** `listVenues`: Returns all college football venues with location, capacity, construction year, surface, and dome details.
* **Search Players** `searchPlayers`: Returns up to 100 players whose names match the search term.

</details>
