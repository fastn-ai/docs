---
description: "AbstractAPI Avatars generates a customizable initials avatar image (PNG or SVG) from a person's name, with control over size, colors, font, shape, and letter…"
hidden: true
---

# AbstractAPI Avatars

AbstractAPI Avatars generates a customizable initials avatar image (PNG or SVG) from a person's name, with control over size, colors, font, shape, and letter styling.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 1 |
| **Events** | 0 |
| **Slug** | `abstractApiAvatars` |

## Use it

Add AbstractAPI Avatars from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiAvatars.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Generate Avatar | `generateAvatar` | Generates an initials avatar image for a person's name and returns the image file (PNG by default, or SVG). Size, colors, font size, number of letters, rounding, case, italics, and bold are all configurable. |
