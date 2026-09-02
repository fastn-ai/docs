---
description: Vendor changes to the integrations you use, and the fixes proposed for them. Nothing is applied until you accept it.
---

# Pending updates

**Integrations → Pending updates** · `/integrations/updates`

<figure><img src="../.gitbook/assets/connector-updates.jpg" alt="The pending updates page"><figcaption></figcaption></figure>

Vendors deprecate endpoints, change parameter names and alter response shapes. Normally you find out when a sync starts failing. fastn watches for these changes, works out what the fix is, and files a proposal here. The page states its own promise:

> Vendor changes to the integrations you use, and the fixes proposed for them. Nothing here is applied until you accept it.

It is a single list — there are no *Connector fixes* or *My workflows* tabs. When nothing is outstanding it reads *Nothing needs your attention…*, and a **Show N already handled** toggle brings the resolved ones back into view.

### Reading a proposal

Each card carries:

* a **status word**, such as `Applied`;
* **Integration connector:** — the connector the change affects;
* **Affected workflows:** — the workflows that depend on it;
* a description of what changed and the fix; and
* a **Details** button.

<figure><img src="../.gitbook/assets/connector-update-review.jpg" alt="A pending update in detail"><figcaption></figcaption></figure>

**Details** opens the proposal in full: what changed upstream, with the specific endpoints involved, and the fix set out as numbered migration steps — updated IDs, remapped parameters, changed response parsing.

### Why nothing auto-applies

Because a connector change can alter behaviour your workflows depend on. A parameter rename is safe; a response shape that drops a field your mapping reads is not. fastn does the diagnosis and the drafting, and leaves the decision with you.

{% hint style="info" %}
Version pins on a connector let you hold specific customers on the old version while you migrate the rest — remembering that a version set in code still wins over a pin. See [Connectors](connectors.md).
{% endhint %}
