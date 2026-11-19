---
description: "Random User Generator creates realistic fake user profiles for testing, with names, addresses, emails and photos."
hidden: true
---

# Random User Generator

<img src="../../.gitbook/assets/connectors/lg/random-user-generator.png" alt="Random User Generator logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [randomuser.me](https://randomuser.me) |
| **Authentication** | No sign-in needed |
| **Slug** | `randomUserGenerator` |

## Setup

Random User Generator needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Random User Generator from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.randomUserGenerator.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Random Users</td><td><code>generateUsers</code></td><td>Generate random fake user profiles (name, address, email, login, phone, photo and more) for testing, using the latest API version Filter by gender and nationality, use a seed for repeatable results, and include or exclude fields. Docs: https://randomuser.me/documentation</td></tr><tr><td>Generate Random Users for Version</td><td><code>generateUsersForVersion</code></td><td>Generate random fake user profiles from a fixed API version so results do not change with new releases Docs: https://randomuser.me/documentation</td></tr></tbody></table>

## Events

Random User Generator has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
