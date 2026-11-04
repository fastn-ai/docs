---
description: When an app you connect to changes something your workflows depend on, it lands here with any proposed patch. Nothing is applied until you accept it.
---

# Pending updates

**Operate → Health → Pending updates** · `/health?tab=updates`

Vendors deprecate endpoints, change parameter names and alter response shapes. Normally you find out when a sync starts failing. fastn watches for these changes, works out what the fix is, and files a proposal here. The page states its own promise:

> When an app you connect to changes something your workflows depend on, it lands here, with any patch the maintainer agent proposes. Nothing is applied until you accept it.

It is a single list. There are no *Connector fixes* or *My workflows* tabs. When nothing is outstanding it reads *Nothing waiting* · *Every change an app made to something you use has been dealt with.*, and a **Show N already handled** toggle brings the resolved ones back into view.

### Reading a proposal

When updates are waiting, a line at the top gives the count and says whether any are already failing (for example *One is already failing*), or *Waiting on you* if none has broken yet.

Each update is one row. The row shows:

* the app's **logo**;
* a **headline** saying what the change does to you, rather than the vendor's own wording;
* a one-line **summary**;
* a single **status pill**, such as `Already failing`, `Breaks today`, `No date given`, `Fixed` or `Not going ahead`; and
* a call to action.

Click a row to expand it in place. The expanded row holds the full detail: the vendor's own description of the change (kept as evidence behind a disclosure), which of your workflows are affected, and any patch the maintainer agent proposes. A patch also says how it was checked: `Unverified`, `Reasoned only`, `Seen on live traffic`, `Ran against stubs` or `Probed for real`. If a patch has not been tested, a *Not tested yet* banner sits above it.

On an applied connector fix that your organization owns, **Notify affected organizations** creates a review for each organization whose workflows use the connector.

### Why nothing auto-applies

Because a connector change can alter behavior your workflows depend on. A parameter rename is safe; a response shape that drops a field your mapping reads is not. fastn does the diagnosis and the drafting, and leaves the decision with you.

{% hint style="info" %}
Version pins on a connector let you hold specific customers on the old version while you migrate the rest. Remember that a version set in code still wins over a pin. See [Connectors](connectors/README.md).
{% endhint %}
