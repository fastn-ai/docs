---
description: "JokeAPI (v2) serves consistently formatted jokes in several languages."
hidden: true
---

# JokeAPI

JokeAPI (v2) serves consistently formatted jokes in several languages. Get jokes by category with filters for type, text, id range, blacklist flags, safe mode and amount, read API info, categories, flags, formats and languages, look up language codes, and validate a joke submission. Free with no API key (120 requests per minute).

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [jokeapi.dev](https://jokeapi.dev) |
| **Authentication** | No authentication |
| **Actions** | 10 |
| **Events** | 0 |
| **Slug** | `jokeapi` |

## Use it

Add JokeAPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.jokeapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Info | `getInfo` | Get information about JokeAPI and its jokes: version, joke count, categories, flags, types, id ranges and safe-joke counts per language (GET /info). Docs: https://v2.jokeapi.dev/ |
| Get Joke | `getJoke` | Get one or more jokes from the given categories with optional filters (GET /joke/{categories}). With amount 2 or more the response has a jokes array. Returns error code 106 'No matching joke found' when filters match nothing. Docs: https://v2.jokeapi.dev/ |
| Get Language Code | `getLanguageCode` | Get the ISO 639-1 code for a language name using fuzzy search (GET /langcode/{language}). Docs: https://v2.jokeapi.dev/ |
| List Categories | `listCategories` | List all joke categories and category aliases (GET /categories). Docs: https://v2.jokeapi.dev/ |
| List Endpoints | `listEndpoints` | List all JokeAPI endpoints with method, URL, supported parameters and description (GET /endpoints). Docs: https://v2.jokeapi.dev/ |
| List Flags | `listFlags` | List all blacklist flags (GET /flags). Docs: https://v2.jokeapi.dev/ |
| List Formats | `listFormats` | List all response formats JokeAPI supports (GET /formats). This connector requests JSON. Docs: https://v2.jokeapi.dev/ |
| List Languages | `listLanguages` | List supported joke languages, system-message languages and all possible ISO 639-1 codes (GET /languages). Docs: https://v2.jokeapi.dev/ |
| Ping | `ping` | Check that JokeAPI is reachable; returns 'Pong!' (GET /ping). Docs: https://v2.jokeapi.dev/ |
| Validate Joke Submission | `validateJokeSubmission` | Check whether a joke would be accepted by the submit endpoint without saving it (POST /submit?dry-run). Real submissions are currently disabled by JokeAPI. Returns 201 'Dry Run complete! No errors were found.' or an error listing what is wrong. Docs: https://v2.jokeapi.dev/ |
