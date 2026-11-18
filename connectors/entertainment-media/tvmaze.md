---
description: "TVmaze public API: free, keyless TV metadata - search shows and people, TV schedules by country and date (including web/streaming), show details, episodes,…"
hidden: true
---

# TVmaze

<img src="../../.gitbook/assets/connectors/lg/tvmaze.png" alt="TVmaze logo">

TVmaze public API: free, keyless TV metadata - search shows and people, TV schedules by country and date (including web/streaming), show details, episodes, seasons, cast, crew, alternate episode orders, images, people credits and change feeds. Data is CC BY-SA licensed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [tvmaze.com](https://tvmaze.com) |
| **Authentication** | No authentication |
| **Slug** | `tvmaze` |

## Use it

Add TVmaze from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tvmaze.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Find Single Show | `singleSearchShow` | Returns the single best-matching show for a name, optionally embedding episodes, cast or other resources. Docs: https://www.tvmaze.com/api |
| Get Alternate List | `getAlternateList` | Returns one alternate episode list by id. Docs: https://www.tvmaze.com/api |
| Get Episode | `getEpisode` | Returns one episode by id; embed=show adds the show. Docs: https://www.tvmaze.com/api |
| Get Episode by Number | `getEpisodeByNumber` | Returns one episode of a show by season and episode number. Docs: https://www.tvmaze.com/api |
| Get Full Future Schedule | `getFullSchedule` | Returns every future episode known to TVmaze (broadcast and web). The response is very large (several MB) and refreshed every 24 hours. Docs: https://www.tvmaze.com/api |
| Get Person | `getPerson` | Returns a person's information: name, country, birthday, deathday, gender and image. Docs: https://www.tvmaze.com/api |
| Get Show | `getShow` | Returns a show's main information: name, type, language, genres, status, runtime, premiere/end dates, network, schedule, rating, external ids, image and summary. Docs: https://www.tvmaze.com/api |
| Get TV Schedule | `getSchedule` | Returns the TV episodes airing on a date in a country (broadcast and cable). Docs: https://www.tvmaze.com/api |
| Get Web/Streaming Schedule | `getWebSchedule` | Returns the web and streaming episodes released on a date, optionally for one country (empty country = global services only). Docs: https://www.tvmaze.com/api |
| List Alternate Episodes | `listAlternateEpisodes` | Returns the episodes of an alternate list in that list's order; embed=episodes adds the episode details. Docs: https://www.tvmaze.com/api |

<details>

<summary>See 21 more actions</summary>

* **List Episode Guest Cast** `listEpisodeGuestCast`: Returns the guest cast of an episode. Docs: https://www.tvmaze.com/api
* **List Episode Guest Crew** `listEpisodeGuestCrew`: Returns the guest crew of an episode (e.g. writers, directors). Docs: https://www.tvmaze.com/api
* **List Episodes by Date** `listEpisodesByDate`: Returns the episodes of a show that aired on a date. Docs: https://www.tvmaze.com/api
* **List People** `listPeople`: Returns the full people index, 1000 people per page sorted by id; page 0 is the first page. A 404 means there are no more pages. Docs: https://www.tvmaze.com/api
* **List People Updates** `listPeopleUpdates`: Returns a map of person id to last-updated Unix timestamp; since=day|week|month limits to recent changes. Docs: https://www.tvmaze.com/api
* **List Person Cast Credits** `listPersonCastCredits`: Returns the shows and characters a person has played. Docs: https://www.tvmaze.com/api
* **List Person Crew Credits** `listPersonCrewCredits`: Returns the shows a person worked on as crew, with crew type. Docs: https://www.tvmaze.com/api
* **List Person Guest Cast Credits** `listPersonGuestCastCredits`: Returns the episodes a person appeared in as guest cast. Docs: https://www.tvmaze.com/api
* **List Season Episodes** `listSeasonEpisodes`: Returns the episodes of one season (by season id). Docs: https://www.tvmaze.com/api
* **List Show AKAs** `listShowAkas`: Returns the alternative names (AKAs) of a show per country. Docs: https://www.tvmaze.com/api
* **List Show Alternate Episode Lists** `listShowAlternateLists`: Returns the alternate episode orders of a show (DVD order, story order, broadcast order...). Docs: https://www.tvmaze.com/api
* **List Show Cast** `listShowCast`: Returns the main cast of a show: person and character pairs. Docs: https://www.tvmaze.com/api
* **List Show Crew** `listShowCrew`: Returns the main crew of a show with their crew type (creator, producer...). Docs: https://www.tvmaze.com/api
* **List Show Episodes** `listShowEpisodes`: Returns all episodes of a show in airing order; specials=1 includes specials. Docs: https://www.tvmaze.com/api
* **List Show Images** `listShowImages`: Returns all images of a show (posters, banners, backgrounds) with resolutions. Docs: https://www.tvmaze.com/api
* **List Show Seasons** `listShowSeasons`: Returns the seasons of a show with episode counts, premiere/end dates and networks. Docs: https://www.tvmaze.com/api
* **List Show Updates** `listShowUpdates`: Returns a map of show id to last-updated Unix timestamp; since=day|week|month limits to recent changes. Docs: https://www.tvmaze.com/api
* **List Shows** `listShows`: Returns the full show index, 250 shows per page sorted by id; page 0 is the first page. A 404 means there are no more pages. Docs: https://www.tvmaze.com/api
* **Look Up Show by External ID** `lookupShow`: Finds a show by its TVRage, TheTVDB or IMDb id (give exactly one). Docs: https://www.tvmaze.com/api
* **Search People** `searchPeople`: Searches people (actors, crew) by name. Docs: https://www.tvmaze.com/api
* **Search Shows** `searchShows`: Fuzzy-searches shows by name and returns up to 10 matches with a relevance score. Docs: https://www.tvmaze.com/api

</details>
