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

## Connect in Fastn

Your customers connect Random User Generator from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Random User Generator**.
2. Select **Connect** on the Random User Generator card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Random User Generator needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Random User Generator's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Random Users</td><td><code>generateUsers</code></td><td>Generate random fake user profiles (name, address, email, login, phone, photo and more) for testing, using the latest API version Filter by gender and nationality, use a seed for repeatable results, and include or exclude fields. Docs: https://randomuser.me/documentation</td></tr><tr><td>Generate Random Users for Version</td><td><code>generateUsersForVersion</code></td><td>Generate random fake user profiles from a fixed API version so results do not change with new releases Docs: https://randomuser.me/documentation</td></tr></tbody></table>

