---
description: "AbstractAPI Avatars creates initials avatars. Generate a PNG or SVG avatar image from a person's name."
hidden: true
---

# AbstractAPI Avatars

<img src="../../.gitbook/assets/connectors/lg/abstract-api-avatars.png" alt="AbstractAPI Avatars logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiAvatars` |

## Setup

Your customers enter their API key for AbstractAPI Avatars when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AbstractAPI Avatars from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AbstractAPI Avatars**.
2. Select **Connect** on the AbstractAPI Avatars card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AbstractAPI Avatars's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Avatar</td><td><code>generateAvatar</code></td><td>Generates an initials avatar image for a person's name and returns the image file (PNG by default, or SVG). Size, colors, font size, number of letters, rounding, case, italics, and bold are all configurable.</td></tr></tbody></table>

