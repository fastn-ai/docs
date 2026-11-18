---
description: "Random User Generator is a free API that creates realistic fake user profiles for testing: names, addresses, emails, logins, phones and photos."
hidden: true
---

# Random User Generator

<img src="../../.gitbook/assets/connectors/lg/random-user-generator.png" alt="Random User Generator logo">

Random User Generator is a free API that creates realistic fake user profiles for testing: names, addresses, emails, logins, phones and photos. Choose gender, nationality and fields, use seeds for repeatable data, and pin an API version. No API key needed.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [randomuser.me](https://randomuser.me) |
| **Authentication** | No authentication |
| **Slug** | `randomUserGenerator` |

## Use it

Add Random User Generator from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.randomUserGenerator.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Random Users</td><td><code>generateUsers</code></td><td>Generate random fake user profiles (name, address, email, login, phone, photo and more) for testing, using the latest API version (GET /api/). Filter by gender and nationality, use a seed for repeatable results, and include or exclude fields. Docs: https://randomuser.me/documentation</td></tr><tr><td>Generate Random Users for Version</td><td><code>generateUsersForVersion</code></td><td>Generate random fake user profiles from a fixed API version so results do not change with new releases (GET /api/{version}/). Docs: https://randomuser.me/documentation</td></tr></tbody></table>
