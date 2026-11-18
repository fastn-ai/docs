---
description: "MusicBrainz is the open music encyclopedia."
hidden: true
---

# MusicBrainz

<img src="../../.gitbook/assets/connectors/musicbrainz.png" alt="MusicBrainz logo" width="64">

MusicBrainz is the open music encyclopedia. Keyless read access to its Web Service v2: look up, browse and search artists, releases, release groups, recordings, works, labels, areas, places, events, instruments, series, URLs and genres, plus lookups by disc ID, ISRC and ISWC. Rate limit: 1 request per second per client.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [musicbrainz.org](https://musicbrainz.org) |
| **Authentication** | No authentication |
| **Slug** | `musicbrainz` |

## Use it

Add MusicBrainz from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.musicbrainz.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Browse Artists | `browseArtist` | Lists the artists linked to another entity (give exactly one of: area, collection, recording, release, release-group, work), paged. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Browse Collections | `browseCollection` | Lists the collections linked to another entity (give exactly one of: area, artist, editor, event, label, place, recording, release, release-group, work), paged. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Browse Events | `browseEvent` | Lists the events linked to another entity (give exactly one of: area, artist, collection, place), paged. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Browse Labels | `browseLabel` | Lists the labels linked to another entity (give exactly one of: area, collection, release), paged. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Browse Places | `browsePlace` | Lists the places linked to another entity (give exactly one of: area, collection), paged. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Browse Recordings | `browseRecording` | Lists the recordings linked to another entity (give exactly one of: artist, collection, release, work), paged. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Browse Release Groups | `browseReleaseGroup` | Lists the release groups linked to another entity (give exactly one of: artist, collection, release), paged. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Browse Releases | `browseRelease` | Lists the releases linked to another entity (give exactly one of: area, artist, collection, label, track, track_artist, recording, release-group), paged. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Browse Works | `browseWork` | Lists the works linked to another entity (give exactly one of: artist, collection), paged. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get Area | `getArea` | Looks up one area by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |

<details>

<summary>See 33 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Artist | `getArtist` | Looks up one artist by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get Collection | `getCollection` | Looks up a public collection by MBID. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get Event | `getEvent` | Looks up one event by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get Genre | `getGenre` | Looks up one genre by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get Instrument | `getInstrument` | Looks up one instrument by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get Label | `getLabel` | Looks up one label by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get Place | `getPlace` | Looks up one place by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get Recording | `getRecording` | Looks up one recording by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get Release | `getRelease` | Looks up one release by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get Release Group | `getReleaseGroup` | Looks up one release group by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get Series | `getSeries` | Looks up one series by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get URL | `getUrl` | Looks up one url by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Get Work | `getWork` | Looks up one work by MusicBrainz ID (MBID); use inc to add related data. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| List All Genres | `listAllGenres` | Lists all genres alphabetically with their MBIDs, paged. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Look Up Disc ID | `lookupDiscId` | Returns the releases (or CD stubs) that match a CD disc ID, or fuzzy-matches by TOC. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Look Up ISRC | `lookupIsrc` | Returns the recordings that have an ISRC. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Look Up ISWC | `lookupIswc` | Returns the works that have an ISWC. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Look Up URL by Address | `lookupUrlByResource` | Finds the MusicBrainz URL entity (and its relationships) for a web address. 404 if the address is not in MusicBrainz. Docs: https://musicbrainz.org/doc/MusicBrainz_API |
| Search Annotations | `searchAnnotation` | Searches annotations with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search Areas | `searchArea` | Searches areas with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search Artists | `searchArtist` | Searches artists with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search CD Stubs | `searchCdstub` | Searches cd stubs with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search Events | `searchEvent` | Searches events with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search Instruments | `searchInstrument` | Searches instruments with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search Labels | `searchLabel` | Searches labels with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search Places | `searchPlace` | Searches places with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search Recordings | `searchRecording` | Searches recordings with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search Release Groups | `searchReleaseGroup` | Searches release groups with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search Releases | `searchRelease` | Searches releases with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search Series | `searchSeries` | Searches series with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search Tags | `searchTag` | Searches tags with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search URLs | `searchUrl` | Searches urls with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |
| Search Works | `searchWork` | Searches works with Lucene query syntax (fields and operators per the search docs) and returns scored results. Docs: https://musicbrainz.org/doc/MusicBrainz_API/Search |

</details>
