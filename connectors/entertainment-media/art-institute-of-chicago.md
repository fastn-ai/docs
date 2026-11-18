---
description: "The Art Institute of Chicago public API: free, keyless access to the museum's collection (artworks, artists, places, galleries, exhibitions, images, audio,…"
hidden: true
---

# Art Institute of Chicago

<img src="../../.gitbook/assets/connectors/lg/art-institute-of-chicago.png" alt="Art Institute of Chicago logo">

The Art Institute of Chicago public API: free, keyless access to the museum's collection (artworks, artists, places, galleries, exhibitions, images, audio, texts), shop products, mobile tours, publications, events, website content and hours, with list, get-by-id and full-text search for each resource. Anonymous use is rate-limited to 60 requests per minute.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [artic.edu](https://artic.edu) |
| **Authentication** | No authentication |
| **Slug** | `artInstituteOfChicago` |

## Use it

Add Art Institute of Chicago from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.artInstituteOfChicago.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Agent | `getAgent` | Returns one of the agents (people and organizations: artists, makers, owners) by id. Docs: https://api.artic.edu/docs |
| Get Agent Role | `getAgentRole` | Returns one of the agent roles by id. Docs: https://api.artic.edu/docs |
| Get Agent Type | `getAgentType` | Returns one of the agent types by id. Docs: https://api.artic.edu/docs |
| Get Article | `getArticle` | Returns one of the website articles by id. Docs: https://api.artic.edu/docs |
| Get Artist | `getArtist` | Returns one of the artists (agents who created artworks) by id. Docs: https://api.artic.edu/docs |
| Get Artwork | `getArtwork` | Returns one of the artworks in the collection by id. Docs: https://api.artic.edu/docs |
| Get Artwork Date Qualifier | `getArtworkDateQualifier` | Returns one of the artwork date qualifiers by id. Docs: https://api.artic.edu/docs |
| Get Artwork Place Qualifier | `getArtworkPlaceQualifier` | Returns one of the artwork place qualifiers by id. Docs: https://api.artic.edu/docs |
| Get Artwork Type | `getArtworkType` | Returns one of the artwork types by id. Docs: https://api.artic.edu/docs |
| Get Category Term | `getCategoryTerm` | Returns one of the category terms (departments, themes, classifications, subjects, styles, techniques, materials) by id. Docs: https://api.artic.edu/docs |
| Get Digital Publication | `getDigitalPublication` | Returns one of the digital publications by id. Docs: https://api.artic.edu/docs |
| Get Digital Publication Article | `getDigitalPublicationArticle` | Returns one of the digital publication articles by id. Docs: https://api.artic.edu/docs |
| Get Educator Resource | `getEducatorResource` | Returns one of the educator resources by id. Docs: https://api.artic.edu/docs |
| Get Event | `getEvent` | Returns one of the events by id. Docs: https://api.artic.edu/docs |
| Get Event Occurrence | `getEventOccurrence` | Returns one of the event occurrences by id. Docs: https://api.artic.edu/docs |
| Get Event Program | `getEventProgram` | Returns one of the event programs by id. Docs: https://api.artic.edu/docs |
| Get Exhibition | `getExhibition` | Returns one of the exhibitions by id. Docs: https://api.artic.edu/docs |
| Get Gallery | `getGallery` | Returns one of the museum galleries by id. Docs: https://api.artic.edu/docs |
| Get Generic Page | `getGenericPage` | Returns one of the generic website pages by id. Docs: https://api.artic.edu/docs |
| Get Highlight | `getHighlight` | Returns one of the highlights (curated artwork collections) by id. Docs: https://api.artic.edu/docs |
| Get Hours Record | `getHoursRecord` | Returns one of the museum opening hours records by id. Docs: https://api.artic.edu/docs |
| Get Image | `getImage` | Returns one of the image assets by id. Docs: https://api.artic.edu/docs |
| Get Landing Page | `getLandingPage` | Returns one of the website landing pages by id. Docs: https://api.artic.edu/docs |
| Get Mobile Sound | `getMobileSound` | Returns one of the mobile app audio by id. Docs: https://api.artic.edu/docs |
| Get Place | `getPlace` | Returns one of the places associated with artworks by id. Docs: https://api.artic.edu/docs |
| Get Press Release | `getPressRelease` | Returns one of the press releases by id. Docs: https://api.artic.edu/docs |
| Get Printed Publication | `getPrintedPublication` | Returns one of the printed publications by id. Docs: https://api.artic.edu/docs |
| Get Product | `getProduct` | Returns one of the museum shop products by id. Docs: https://api.artic.edu/docs |
| Get Publication | `getPublication` | Returns one of the online scholarly catalogue publications by id. Docs: https://api.artic.edu/docs |
| Get Section | `getSection` | Returns one of the sections of online catalogue publications by id. Docs: https://api.artic.edu/docs |
| Get Site | `getSite` | Returns one of the microsites by id. Docs: https://api.artic.edu/docs |
| Get Sound | `getSound` | Returns one of the sound assets by id. Docs: https://api.artic.edu/docs |
| Get Static Page | `getStaticPage` | Returns one of the static website pages by id. Docs: https://api.artic.edu/docs |
| Get Text | `getText` | Returns one of the text assets by id. Docs: https://api.artic.edu/docs |
| Get Tour | `getTour` | Returns one of the mobile app tours by id. Docs: https://api.artic.edu/docs |
| Get Video | `getVideo` | Returns one of the video assets by id. Docs: https://api.artic.edu/docs |
| List Agent Roles | `listAgentRoles` | Returns a paged list of agent roles, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Agent Types | `listAgentTypes` | Returns a paged list of agent types, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Agents | `listAgents` | Returns a paged list of agents (people and organizations: artists, makers, owners), sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Articles | `listArticles` | Returns a paged list of website articles, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Artists | `listArtists` | Returns a paged list of artists (agents who created artworks), sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Artwork Date Qualifiers | `listArtworkDateQualifiers` | Returns a paged list of artwork date qualifiers, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Artwork Place Qualifiers | `listArtworkPlaceQualifiers` | Returns a paged list of artwork place qualifiers, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Artwork Types | `listArtworkTypes` | Returns a paged list of artwork types, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Artworks | `listArtworks` | Returns a paged list of artworks in the collection, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Category Terms | `listCategoryTerms` | Returns a paged list of category terms (departments, themes, classifications, subjects, styles, techniques, materials), sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Digital Publication Articles | `listDigitalPublicationArticles` | Returns a paged list of digital publication articles, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Digital Publications | `listDigitalPublications` | Returns a paged list of digital publications, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Educator Resources | `listEducatorResources` | Returns a paged list of educator resources, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Event Occurrences | `listEventOccurrences` | Returns a paged list of event occurrences, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Event Programs | `listEventPrograms` | Returns a paged list of event programs, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Events | `listEvents` | Returns a paged list of events, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Exhibitions | `listExhibitions` | Returns a paged list of exhibitions, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Galleries | `listGalleries` | Returns a paged list of museum galleries, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Generic Pages | `listGenericPages` | Returns a paged list of generic website pages, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Highlights | `listHighlights` | Returns a paged list of highlights (curated artwork collections), sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Hours | `listHours` | Returns a paged list of museum opening hours records, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Images | `listImages` | Returns a paged list of image assets, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Landing Pages | `listLandingPages` | Returns a paged list of website landing pages, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Mobile Sounds | `listMobileSounds` | Returns a paged list of mobile app audio, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Places | `listPlaces` | Returns a paged list of places associated with artworks, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Press Releases | `listPressReleases` | Returns a paged list of press releases, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Printed Publications | `listPrintedPublications` | Returns a paged list of printed publications, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Products | `listProducts` | Returns a paged list of museum shop products, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Publications | `listPublications` | Returns a paged list of online scholarly catalogue publications, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Sections | `listSections` | Returns a paged list of sections of online catalogue publications, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Sites | `listSites` | Returns a paged list of microsites, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Sounds | `listSounds` | Returns a paged list of sound assets, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Static Pages | `listStaticPages` | Returns a paged list of static website pages, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Texts | `listTexts` | Returns a paged list of text assets, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Tours | `listTours` | Returns a paged list of mobile app tours, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| List Videos | `listVideos` | Returns a paged list of video assets, sorted by last update (newest first); filter to specific records with ids. Docs: https://api.artic.edu/docs |
| Search Agents | `searchAgents` | Full-text searches agents (people and organizations: artists, makers, owners); returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search All Resources | `searchAll` | Searches across all resources at once and returns the best matches, each tagged with its api_model. Docs: https://api.artic.edu/docs |
| Search Articles | `searchArticles` | Full-text searches website articles; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Artworks | `searchArtworks` | Full-text searches artworks in the collection; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Category Terms | `searchCategoryTerms` | Full-text searches category terms (departments, themes, classifications, subjects, styles, techniques, materials); returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Digital Publication Articles | `searchDigitalPublicationArticles` | Full-text searches digital publication articles; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Digital Publications | `searchDigitalPublications` | Full-text searches digital publications; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Educator Resources | `searchEducatorResources` | Full-text searches educator resources; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Event Occurrences | `searchEventOccurrences` | Full-text searches event occurrences; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Event Programs | `searchEventPrograms` | Full-text searches event programs; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Events | `searchEvents` | Full-text searches events; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Exhibitions | `searchExhibitions` | Full-text searches exhibitions; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Galleries | `searchGalleries` | Full-text searches museum galleries; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Generic Pages | `searchGenericPages` | Full-text searches generic website pages; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Highlights | `searchHighlights` | Full-text searches highlights (curated artwork collections); returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Hours | `searchHours` | Full-text searches museum opening hours records; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Images | `searchImages` | Full-text searches image assets; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Landing Pages | `searchLandingPages` | Full-text searches website landing pages; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Mobile Sounds | `searchMobileSounds` | Full-text searches mobile app audio; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Places | `searchPlaces` | Full-text searches places associated with artworks; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Press Releases | `searchPressReleases` | Full-text searches press releases; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Printed Publications | `searchPrintedPublications` | Full-text searches printed publications; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Products | `searchProducts` | Full-text searches museum shop products; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Publications | `searchPublications` | Full-text searches online scholarly catalogue publications; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Sections | `searchSections` | Full-text searches sections of online catalogue publications; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Sites | `searchSites` | Full-text searches microsites; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Sounds | `searchSounds` | Full-text searches sound assets; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Static Pages | `searchStaticPages` | Full-text searches static website pages; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Texts | `searchTexts` | Full-text searches text assets; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Tours | `searchTours` | Full-text searches mobile app tours; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
| Search Videos | `searchVideos` | Full-text searches video assets; returns matching records with relevance score and optional facet counts. Docs: https://api.artic.edu/docs |
