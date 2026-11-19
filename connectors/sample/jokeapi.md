---
description: "JokeAPI serves jokes in several languages. Get jokes by category and list categories, flags and languages."
hidden: true
---

# JokeAPI

<img src="../../.gitbook/assets/connectors/lg/jokeapi.png" alt="JokeAPI logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [jokeapi.dev](https://jokeapi.dev) |
| **Authentication** | No sign-in needed |
| **Slug** | `jokeapi` |

## Setup

JokeAPI needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add JokeAPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.jokeapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Info</td><td><code>getInfo</code></td><td>Get information about JokeAPI and its jokes: version, joke count, categories, flags, types, id ranges and safe-joke counts per language Docs: https://v2.jokeapi.dev/</td></tr><tr><td>Get Joke</td><td><code>getJoke</code></td><td>Get one or more jokes from the given categories with optional filters With amount 2 or more the response has a jokes array. Returns error code 106 'No matching joke found' when filters match nothing. Docs: https://v2.jokeapi.dev/</td></tr><tr><td>Get Language Code</td><td><code>getLanguageCode</code></td><td>Get the ISO 639-1 code for a language name using fuzzy search Docs: https://v2.jokeapi.dev/</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>List all joke categories and category aliases Docs: https://v2.jokeapi.dev/</td></tr><tr><td>List Endpoints</td><td><code>listEndpoints</code></td><td>List all JokeAPI endpoints with method, URL, supported parameters and description Docs: https://v2.jokeapi.dev/</td></tr><tr><td>List Flags</td><td><code>listFlags</code></td><td>List all blacklist flags Docs: https://v2.jokeapi.dev/</td></tr><tr><td>List Formats</td><td><code>listFormats</code></td><td>List all response formats JokeAPI supports This connector requests JSON. Docs: https://v2.jokeapi.dev/</td></tr><tr><td>List Languages</td><td><code>listLanguages</code></td><td>List supported joke languages, system-message languages and all possible ISO 639-1 codes Docs: https://v2.jokeapi.dev/</td></tr><tr><td>Ping</td><td><code>ping</code></td><td>Check that JokeAPI is reachable; returns 'Pong!' Docs: https://v2.jokeapi.dev/</td></tr><tr><td>Validate Joke Submission</td><td><code>validateJokeSubmission</code></td><td>Check whether a joke would be accepted by the submit endpoint without saving it Real submissions are currently disabled by JokeAPI.' or an error listing what is wrong. Docs: https://v2.jokeapi.dev/</td></tr></tbody></table>

## Events

JokeAPI has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
