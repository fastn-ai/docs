---
description: What changed in fastn, release by release, and known issues with their workarounds.
---

# Changelog

Changes that affect how you build, embed or run integrations, newest first. Dates are release dates. Internal and infrastructure changes are not listed.

## Known issues

None open. When there is one, it is listed here with the date it was found, its workaround and its status, and moved into the release that fixes it.

## v1.13.0 (10 November 2026)

**Embed**

* The headless SDK now covers the whole widget hub, so you can build your own UI for every widget screen.
* A UI library for the widget hub, and a hosted iframe hub built from it.
* A hub's own dialogs are centered on screen, and fixed-height frames scroll.

**Workflows**

* When an Instant run is escalated to a background tier, the run now shows it.

**Customers and plans**

* Customer tiers can cap every per-customer plan limit, and every tier limit is enforced.
* A tier's connector allowlist is enforced by the API, not only in the dashboard.
* Developer is no longer offered as a role for a customer tier.
* The Customers page shows your plan's customer cap.

**Triggers and events**

* The `connection.revoked` event carries the connection name and the reason.
* A webhook on a shared URL is verified with the secret of the app it names.

**Dashboard**

* The Connect dialog's scope picker has search, select all and clear.
* An expired or missing connect link says so, with a way back.
* An empty Connections page says where your organization's own connections are.
* Inviting someone who already has an account waits for them to accept.

## v1.12.0 (7 November 2026)

**Workflows**

* `fastn.connectors` (plural) works as an alias for `fastn.connector` in workflow code. See [Workflow runtime API](workflow-runtime.md).
* Any default export compiles, and timers and abort signals work in the sandbox.
* Test runs act as the installation's customer, including from an embed session.
* An Instant run whose connector call fails the way a timeout does is escalated instead of failed.

**Customers**

* API responses name each customer by your own id, never fastn's internal id. See [Core concepts](../getting-started/concepts.md).

**Triggers and events**

* A customer's app trigger runs as that customer, on the connector webhook URL and when polling.
* A trigger pinned to an environment with no deployment shows a warning.

**Widget and connect links**

* Adding a second setup or several accounts asks with a picker.
* An expired connect link says it expired instead of "Connector not found".

**Sign-in and email**

* "Keep me signed in" is offered on the passwordless email step.
* Notification emails come from the verified `mail.fastn.ai` domain.

## v1.11.0 (4 November 2026)

**Plans**

* The Launch plan allows 3 customer connections across all your customers. See [Billing and limits](../manage/billing.md).

**Workflows**

* The workflows list shows **Unpublished**, **In review**, **Published**, **Live** and **Paused**.
* Workflow code can call `update`, `delete` and `search` on `fastn.unified`, and has `TextEncoder` and `TextDecoder`.
* `fastn.checkpoint` carries across an Instant to Standard escalation.
* An array returned by a connector comes back as an array.

**Widget**

* Guided Connect: customers connect one app after another, then finish the setup.
* One connect experience across the builder, the preview and the embed.
* Each integration has one accurate How it works doc, with an agent API.
* Every installation has its own config.

**Triggers**

* Schedulers stop firing for a workflow that is not published, and skip a run when the organization has used its run quota.
* App triggers on the same event share one provider subscription.

**Dashboard**

* Alerts live under **Operate → Health** only.
* API key presets are named after the roles on **Settings → Roles**.
* Windsurf is now listed as Devin under Connect AI tools.
