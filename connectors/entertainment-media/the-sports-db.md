---
description: "TheSportsDB is an open, crowd-sourced sports database with artwork."
hidden: true
---

# TheSportsDB

<img src="../../.gitbook/assets/connectors/lg/the-sports-db.png" alt="TheSportsDB logo">

TheSportsDB is an open, crowd-sourced sports database with artwork. Search teams, players, events and venues; look up leagues, tables, teams, kits, players (honours, contracts, results, stats), events (results, lineups, timelines, stats, TV); list sports, countries, leagues, seasons and teams; and get schedules, TV listings and video highlights. Use the free key 123 or your own premium key.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [thesportsdb.com](https://thesportsdb.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `theSportsDb` |

## Use it

Add TheSportsDB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.theSportsDb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Event | `getEvent` | Get an event's details by id (GET /lookupevent.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Event Lineup | `getEventLineup` | Get the team lineups of an event by id (GET /lookuplineup.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Event Results | `getEventResults` | Get all results of an event by id (GET /eventresults.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Event Statistics | `getEventStatistics` | Get the statistics of an event by id (GET /lookupeventstats.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Event Timeline | `getEventTimeline` | Get the timeline (goals, cards, subs) of an event by id (GET /lookuptimeline.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Event TV Broadcasts | `getEventTvBroadcasts` | List the TV channels showing an event by id (GET /lookuptv.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get League | `getLeague` | Get a league's details by id (GET /lookupleague.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get League Table | `getLeagueTable` | Get a league's points table, optionally for a season (featured soccer leagues only) (GET /lookuptable.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Player | `getPlayer` | Get a player's details by id (GET /lookupplayer.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Player Contracts | `getPlayerContracts` | List a player's contracts by player id (GET /lookupcontracts.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Player Former Teams | `getPlayerFormerTeams` | List a player's former teams by player id (GET /lookupformerteams.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Player Honours | `getPlayerHonours` | List a player's honours by player id (GET /lookuphonours.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Player Milestones | `getPlayerMilestones` | List a player's milestones by player id (GET /lookupmilestones.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Player Results | `getPlayerResults` | List a player's event results by player id (GET /playerresults.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Player Statistics | `getPlayerStatistics` | Get a player's statistics by player id (GET /lookupplayerstats.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Team | `getTeam` | Get a team's details by id (GET /lookupteam.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Team Equipment | `getTeamEquipment` | Get a team's current and historical kits by team id (GET /lookupequipment.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Get Venue | `getVenue` | Get a venue's details by id (GET /lookupvenue.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List Countries | `listCountries` | List all countries (GET /all_countries.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List Event Highlights | `listEventHighlights` | List YouTube highlight videos for events on a date, optionally by league or sport (GET /eventshighlights.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List Events by Day | `listEventsByDay` | List events on a day, optionally for a sport or league (GET /eventsday.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List League Next Events | `listLeagueNextEvents` | List a league's next upcoming events (GET /eventsnextleague.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List League Past Events | `listLeaguePastEvents` | List a league's most recent past events (GET /eventspastleague.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List League Seasons | `listSeasons` | List the seasons of a league, optionally with poster, badge or description (GET /search_all_seasons.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List Leagues | `listLeagues` | List all leagues (GET /all_leagues.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List Leagues by Country and Sport | `listLeaguesByCountry` | List the leagues in a country, optionally for one sport (GET /search_all_leagues.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List Season Events | `listSeasonEvents` | List the events of a league season (GET /eventsseason.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List Sports | `listSports` | List all sport categories (GET /all_sports.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List Team Last Events | `listTeamLastEvents` | List a team's most recent events (free key shows home events only) (GET /eventslast.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List Team Next Events | `listTeamNextEvents` | List a team's next upcoming events (free key shows home events only) (GET /eventsnext.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List Team Players | `listTeamPlayers` | List the players of a team by team id (GET /lookup_all_players.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List Teams | `listTeams` | List the teams in a league by name, or by sport and country (GET /search_all_teams.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| List TV Events | `listTvEvents` | List televised events by date, sport, country, channel name or channel id (GET /eventstv.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Search Events | `searchEvents` | Search events by title (Home_vs_Away), optionally for a season or date, or by event filename (GET /searchevents.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Search Events by Filename | `searchEventsByFilename` | Search events by their filename, optionally for a season (GET /searchfilename.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Search Players | `searchPlayers` | Search players by main or alternate name (GET /searchplayers.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Search Teams | `searchTeams` | Search sports teams by name. The free key only matches Arsenal (GET /searchteams.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
| Search Venues | `searchVenues` | Search venues by name or alternate name (GET /searchvenues.php). The free key 123 returns a limited number of rows (premium keys return more). Docs: https://www.thesportsdb.com/documentation |
