---
description: How the connector catalogue reads: badges, filters, card anatomy, and the counts that mislead.
---

# The catalogue

The page header states the intent plainly:

> Every system your customers can authorise. Depth on the ones that block deals, not a catalogue count.

Connectors marked **managed** are maintained by fastn — when the vendor ships a breaking change, you get a proposal under [Pending updates](../connector-updates.md) rather than a broken sync. Ones you build yourself are badged **Custom**. Either badge is replaced by **Connected** once at least one connection exists.

| Control            | What it filters                                          | URL              |
| ------------------ | ---------------------------------------------------------- | ---------------- |
| **Search connectors** | Name and description                                   | `?q=`            |
| **All / Connected / OAuth** | Everything · at least one live connection · offers OAuth 2.0 | `?category=` |
| **All Visibility** | `All Visibility`, `Private`, `Public`                     | `?visibility=`   |

There is no sort control. The list pages at 24 per page with a footer reading `1–24 of 351`; the page number is not kept in the URL, so a deep link always lands on page one.

A search that matches nothing shows `No connectors match "x"`, *Try another search or category.* and a **Clear search** button.

**Card anatomy.** Favicon, name, badge, description, an `OAuth 2.0` chip where it applies, and a provenance string. The footer button reads **Connect**, or **Add another connection** with a chevron offering **Reconnect** and **Disconnect**. The `⋯` menu holds **Select**, **Edit**, **Export** and **Delete**.

**Header controls.** **Create connector** opens the create dialog. **Import** is a bare file input — it takes a JSON connector definition with no intermediate dialog. Selecting cards (via `⋯ → Select`) reveals **Export Selected (n)**.

{% hint style="warning" %}
Three things about this list are known to mislead, and are worth knowing before you count anything:

* The catalogue contains duplicates — Asana, HubSpot, Salesforce, Slack, Notion and Cin7 Core each appear twice, once `managed` and once `Custom` — so the total is not a count of distinct systems.
* A connector badged `Connected` in the list can still report `0 connections` on its own detail page.
* Provenance is written three different ways for the same thing: *Managed by Fastn*, *Managed by fastn.ai* and *Managed by fastn*.
{% endhint %}
