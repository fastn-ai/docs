---
description: "Google Pay and Wallet Developer helps businesses build Google Pay and Google Wallet integrations. Use its tools to work with your Google Pay and Wallet setup."
hidden: true
---

# Google Pay & Wallet Developer

<img src="../../.gitbook/assets/connectors/lg/google-pay-wallet-developer.png" alt="Google Pay & Wallet Developer logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [paydeveloper.googleapis.com](https://paydeveloper.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googlePayWalletDeveloper` |

## Setup

Your customers sign in to Google Pay & Wallet Developer through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Pay & Wallet Developer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googlePayWalletDeveloper.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Events

Google Pay & Wallet Developer has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
