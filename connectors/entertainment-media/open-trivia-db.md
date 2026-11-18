---
description: "Open Trivia DB is a free, keyless, user-contributed trivia question database: get multiple-choice or true/false questions by category, difficulty and…"
hidden: true
---

# Open Trivia DB

Open Trivia DB is a free, keyless, user-contributed trivia question database: get multiple-choice or true/false questions by category, difficulty and encoding, use session tokens to avoid repeats, and look up categories and question counts. Each IP may call the API once every 5 seconds. Data is CC BY-SA 4.0.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [opentdb.com](https://opentdb.com) |
| **Authentication** | No authentication |
| **Slug** | `openTriviaDb` |

## Use it

Add Open Trivia DB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openTriviaDb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Category Question Count | `getCategoryQuestionCount` | Returns how many verified questions a category has in total and per difficulty. Docs: https://opentdb.com/api_config.php |
| Get Global Question Count | `getGlobalQuestionCount` | Returns total, pending, verified and rejected question counts overall and per category. Docs: https://opentdb.com/api_config.php |
| Get Trivia Questions | `getQuestions` | Returns 1-50 trivia questions with correct and incorrect answers, optionally filtered by category, difficulty and type; pass a session token to never repeat questions. response_code 0 = success, 1 = not enough questions, 2 = invalid parameter, 3 = token not found, 4 = token exhausted (reset it), 5 = rate limit (1 call per 5 s per IP). Docs: https://opentdb.com/api_config.php |
| List Categories | `listCategories` | Returns all trivia categories with their ids. Docs: https://opentdb.com/api_config.php |
| Request Session Token | `requestSessionToken` | Creates a session token that makes Get Trivia Questions never return the same question twice; tokens expire after 6 hours of inactivity. Docs: https://opentdb.com/api_config.php |
| Reset Session Token | `resetSessionToken` | Resets a session token so it can return all questions again (use after response_code 4). Docs: https://opentdb.com/api_config.php |
