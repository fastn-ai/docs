---
description: "Labels and categories: how to create them, attach them to workflows, and what happens when you delete one."
---

# Workflow tags

**Settings → Workflow tags**. Developer or above.

Once an organization holds more than a handful of workflows, the list stops being scannable. Tags are how you cut it back down. There are two kinds, and they behave differently on purpose.

| | Labels | Categories |
| --- | ------ | ---------- |
| Per workflow | Many | **One** |
| What they do to the list | Filter it | Group it |
| Per organization | Launch 2, Scale 10, Enterprise 15 | Launch 2, Scale 10, Enterprise 15 |
| Per workflow limit | Up to 5 labels | n/a, a workflow is in one category or none |

A label is a tag you filter by, so a workflow can carry several: a sync can be both `Dev` and `Billing`. A category is where a workflow *lives*, so it only gets one, the way a file sits in one folder.

<figure><img src="../.gitbook/assets/workflow-tags-settings.webp" alt="The Workflow tags page, reached from Workflow tags in the Settings menu. A Labels panel counts how many labels exist against the plan limit and holds one row, Dev, reading 1 workflow. A Categories panel carries the same counter and holds one row reading 1 workflow. Each row carries a colored dot before its name, and each panel ends with a color swatch, a name field and an Add button"><figcaption>Both panels carry a counter: how many you have defined, against the number allowed. Once the two match, the name field is replaced by a line saying so until you delete something.</figcaption></figure>

## Creating one

Tags are created here and nowhere else. The page is the registry; workflows only attach what already exists.

1. Pick a color from the swatch to the left of the field.
2. Type the name.
3. **Add**.

Each row then shows how many workflows use that tag, reading **Not used yet** until something does. That count is the thing to check before deleting one.

{% hint style="info" %}
**The limit is per organization, not per workflow.** The whole organization shares one registry of labels and one of categories, and **how many of each you get comes from your plan**: 2 of each on Launch, 10 on Scale and 15 on Enterprise. [Billing and limits](billing.md) lists both, with your usage against them. The counter on each panel is the number that applies to you, including any override fastn has set for your account.
{% endhint %}

### When a panel is full

The name field is replaced by a line saying so, rather than being greyed out. Delete a tag to make room.

Changing plan never deletes a tag. If a new plan allows fewer than you already have, **you keep all of them** and simply cannot add another until you delete down to the new number. The panel says how many that is.

A full registry also affects workflows arriving from a prebuilt integration. Their tags are recreated by name in your organization, so when there is no room left the workflow lands without that label, or uncategorized. For a category, the result says which one it could not create.

## Attaching one to a workflow

Tags are attached from the workflow itself, on **Workflows**, not from this page. Each workflow's panel carries two controls:

* **Labels**, a multi-select. A workflow can carry up to 5 of them, whatever your plan. That cap is separate from how many the organization may define.
* **Category**, a single select. Choosing a new one replaces the old.

Both are available when you create a workflow and when you edit an existing one. Both are disabled for roles that cannot manage workflows, so a read-only role sees the tags but cannot change them.

## Using them on the list

<figure><img src="../.gitbook/assets/workflow-tags-list.webp" alt="The workflows list grouped by category, showing one named category group holding a single workflow and an Uncategorised group holding four. The workflow row carries a blue Dev label chip under its description"><figcaption>Labels render as chips on the row. Categories become the group headers.</figcaption></figure>

Two controls sit above the list:

* **Labels** filters it. Pick several and a workflow has to carry all of them to show, so the filter narrows rather than widens.
* **Group by category** switches the flat list into one group per category.

### Uncategorised

Every workflow without a category falls into **Uncategorised**. It is not a category you create or can delete, it is where everything starts, and an organization that has never defined a category shows a single Uncategorised group holding everything.

## Deleting one

Deleting a tag never deletes the workflows carrying it.

* Delete a **label** and it comes off the workflows that had it.
* Delete a **category** and its workflows fall back to **Uncategorised**.

{% hint style="warning" %}
Deleting is the only way to make room once a panel is full. Check the usage count on the row first: a category showing **3 workflows** will drop those three into Uncategorised, and nothing records which category they used to be in.
{% endhint %}

## Who can change them

Tags follow workflow permissions rather than carrying their own:

| Action | Needs |
| ------ | ----- |
| See tags, filter and group by them | Permission to read workflows |
| Create a tag, attach one to a workflow | Permission to update workflows |
| Delete a tag | Permission to delete workflows |

Anyone who can edit a workflow can therefore also create a tag. The page itself opens for Developer or above; an Operator or Viewer can see tags on the workflows list but not reach this page. See [Roles](roles.md).
