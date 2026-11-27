---
description: "Open Trivia DB is a free trivia question database. Get trivia questions by category and difficulty and list categories."
hidden: true
---

# Open Trivia DB

<img src="../../.gitbook/assets/connectors/lg/open-trivia-db.png" alt="Open Trivia DB logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [opentdb.com](https://opentdb.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `openTriviaDb` |

## Setup

Open Trivia DB needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Open Trivia DB from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Open Trivia DB**.
2. Select **Connect** on the Open Trivia DB card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Open Trivia DB needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Open Trivia DB's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Category Question Count</td><td><code>getCategoryQuestionCount</code></td><td>Returns how many verified questions a category has in total and per difficulty. Docs: https://opentdb.com/api_config.php</td></tr><tr><td>Get Global Question Count</td><td><code>getGlobalQuestionCount</code></td><td>Returns total, pending, verified and rejected question counts overall and per category. Docs: https://opentdb.com/api_config.php</td></tr><tr><td>Get Trivia Questions</td><td><code>getQuestions</code></td><td>Returns 1-50 trivia questions with correct and incorrect answers, optionally filtered by category, difficulty and type; pass a session token to never repeat questions. response_code 0 = success, 1 = not enough questions, 2 = invalid parameter, 3 = token not found, 4 = token exhausted (reset it), 5 = rate limit (1 call per 5 s per IP). Docs: https://opentdb.com/api_config.php</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>Returns all trivia categories with their ids. Docs: https://opentdb.com/api_config.php</td></tr><tr><td>Request Session Token</td><td><code>requestSessionToken</code></td><td>Creates a session token that makes Get Trivia Questions never return the same question twice; tokens expire after 6 hours of inactivity. Docs: https://opentdb.com/api_config.php</td></tr><tr><td>Reset Session Token</td><td><code>resetSessionToken</code></td><td>Resets a session token so it can return all questions again (use after response_code 4). Docs: https://opentdb.com/api_config.php</td></tr></tbody></table>

