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

## Use it

Add AbstractAPI Avatars from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiAvatars.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Generate Avatar</td><td><code>generateAvatar</code></td><td>Generates an initials avatar image for a person's name and returns the image file (PNG by default, or SVG). Size, colors, font size, number of letters, rounding, case, italics, and bold are all configurable.</td></tr></tbody></table>

## Events

AbstractAPI Avatars has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
