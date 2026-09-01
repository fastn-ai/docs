---
description: Fixes fastn proposes when an upstream API changes. Nothing is applied until you accept it.
---

# Connector updates

**Integrations → Connector updates**

<figure><img src="../.gitbook/assets/connector-updates.jpg" alt="The connector updates page"><figcaption></figcaption></figure>

Vendors deprecate endpoints, change parameter names and alter response shapes. Normally you find out when a sync starts failing. fastn watches for these changes, works out what the fix is, and files a proposal here.

The page has two tabs: **Connector fixes** (proposals against managed connectors) and **My workflows** (proposals against workflows you own).

### Reading a proposal

Each row shows a status badge, the connector, the proposed remedy — *Fork a new major*, for example — and the blast radius: *1 workflow across 3 orgs*. **Review** opens the detail.

<figure><img src="../.gitbook/assets/connector-update-review.jpg" alt="A connector update proposal in detail"><figcaption></figcaption></figure>

A proposal contains:

* **What changed upstream**, with the specific endpoints. For example: HubSpot sunset the legacy Contacts Lists v1 API (`PUT /contacts/v1/lists/{listId}/add`) on 30 April 2026; calls now return 404, replaced by `PUT /crm/v3/lists/{listId}/memberships/add`.
* **The migration**, step by step — updated IDs, remapped parameters, changed response parsing.
* **Agent confidence** and how the proposal was derived.

### Acting on one

**Notify affected orgs** tells the organisations running the affected workflows that a change is coming, before anything moves.

Where fastn can derive a patch, you accept it and the connector is updated. Where it cannot, the proposal says so plainly:

> No patch could be derived for this change yet. Run the repair agent, or handle it manually — this is a detected problem with no proposed fix, not a resolved one.

That distinction matters: an unpatched proposal is still a live problem.

### Statuses

| Badge        | Meaning                                                      |
| ------------ | -------------------------------------------------------------- |
| **applied**  | The fix has been applied to the connector.                    |
| **pending**  | Waiting on your decision.                                     |
| **rejected** | You declined it. The upstream change still stands.            |

### Why nothing auto-applies

Because a connector change can alter behaviour your workflows depend on. A parameter rename is safe; a response shape that drops a field your mapping reads is not. fastn does the diagnosis and the drafting, and leaves the decision with you.

{% hint style="info" %}
Version pins on a connector let you hold specific customers on the old version while you migrate the rest. See [Connectors](connectors.md).
{% endhint %}
