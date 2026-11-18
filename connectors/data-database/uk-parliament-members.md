---
description: "The UK Parliament Members API gives open data on MPs and Lords: search current and historical members, get biographies, contact details, experience,…"
hidden: true
---

# UK Parliament Members API

The UK Parliament Members API gives open data on MPs and Lords: search current and historical members, get biographies, contact details, experience, interests, voting records, written questions, early day motions and staff, constituencies with election results and boundaries, party strengths, government and opposition posts, and reference lists. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [parliament.uk](https://parliament.uk) |
| **Authentication** | No authentication |
| **Actions** | 39 |
| **Events** | 0 |
| **Slug** | `ukParliamentMembers` |

## Use it

Add UK Parliament Members API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ukParliamentMembers.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Browse Locations | `browseLocations` | Returns a list of locations, both parent and child. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Location/Browse/{locationType}/{locationName}) |
| Get Constituency | `getConstituency` | Returns a constituency by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Location/Constituency/{id}) |
| Get Constituency Election Result | `getConstituencyElectionResult` | Returns an election result by constituency and election id. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Location/Constituency/{id}/ElectionResult/{electionId}) |
| Get Constituency Geometry | `getConstituencyGeometry` | Returns geometry by constituency ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Location/Constituency/{id}/Geometry) |
| Get Constituency Latest Election Result | `getConstituencyLatestElectionResult` | Returns latest election result by constituency id. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Location/Constituency/{id}/ElectionResult/Latest) |
| Get Constituency Synopsis | `getConstituencySynopsis` | Returns a synopsis by constituency ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Location/Constituency/{id}/Synopsis) |
| Get Lords by Peerage Type | `getLordsByType` | Returns the composition of the House of Lords by peerage type. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Parties/LordsByType/{forDate}) |
| Get Member | `getMember` | Return member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}) |
| Get Member Areas of Focus | `getMemberFocus` | Return list of areas of focus of member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/Focus) |
| Get Member Biography | `getMemberBiography` | Return biography of member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/Biography) |
| Get Member Contact Details | `getMemberContact` | Return list of contact details of member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/Contact) |
| Get Member Contribution Summary | `getMemberContributionSummary` | Return contribution summary of member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/ContributionSummary) |
| Get Member History | `getMemberHistory` | Return members by ID with list of their historical names, parties and memberships. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/History) |
| Get Member Latest Election Result | `getMemberLatestElectionResult` | Return latest election result of member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/LatestElectionResult) |
| Get Member Portrait URL | `getMemberPortraitUrl` | Return portrait url of member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/PortraitUrl) |
| Get Member Registered Interests | `getMemberRegisteredInterests` | Return list of registered interests of member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/RegisteredInterests) |
| Get Member Synopsis | `getMemberSynopsis` | Return synopsis of member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/Synopsis) |
| Get Member Thumbnail URL | `getMemberThumbnailUrl` | Return thumbnail url of member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/ThumbnailUrl) |
| Get State of the Parties | `getStateOfTheParties` | Returns current state of parties. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Parties/StateOfTheParties/{house}/{forDate}) |
| List Active Parties | `listActiveParties` | Returns a list of current parties with at least one active member. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Parties/GetActive/{house}) |
| List Answering Bodies | `listAnsweringBodies` | Returns a list of answering bodies. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Reference/AnsweringBodies) |
| List Constituency Election Results | `listConstituencyElectionResults` | Returns a list of election results by constituency ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Location/Constituency/{id}/ElectionResults) |
| List Constituency Representations | `listConstituencyRepresentations` | Returns a list of representations by constituency ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Location/Constituency/{id}/Representations) |
| List Departments | `listDepartments` | Returns a list of departments. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Reference/Departments) |
| List Departments by Type | `listPostDepartments` | Returns a list of departments. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Posts/Departments/{type}) |
| List Government Posts | `listGovernmentPosts` | Returns a list of government posts. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Posts/GovernmentPosts) |
| List Lords Staff | `listLordsStaff` | Returns a list of staff. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/LordsInterests/Staff) |
| List Member Early Day Motions | `listMemberEarlyDayMotions` | Return list of early day motions of member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/Edms) |
| List Member Staff | `listMemberStaff` | Return list of staff of member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/Staff) |
| List Member Votes | `listMemberVotes` | Return list of votes by member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/Voting) |
| List Member Written Questions | `listMemberWrittenQuestions` | Return list of written questions by member by ID. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/{id}/WrittenQuestions) |
| List Opposition Posts | `listOppositionPosts` | Returns a list of opposition posts. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Posts/OppositionPosts) |
| List Policy Interests | `listPolicyInterests` | Returns a list of policy interest. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Reference/PolicyInterests) |
| List Speaker and Deputies | `listSpeakerAndDeputies` | Returns a list containing the speaker and deputy speakers. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Posts/SpeakerAndDeputies/{forDate}) |
| List Spokespersons | `listSpokespersons` | Returns a list of spokespersons. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Posts/Spokespersons) |
| Search Constituencies | `searchConstituencies` | Returns a list of constituencies. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Location/Constituency/Search) |
| Search Historical Members | `searchHistoricalMembers` | Returns a list of members of the Commons or Lords. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/SearchHistorical) |
| Search Lords Register of Interests | `searchLordsInterestsRegister` | Returns a list of registered interests. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/LordsInterests/Register) |
| Search Members | `searchMembers` | Returns a list of current members of the Commons or Lords. Docs: https://members-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Members/Search) |
