---
description: How to save, publish and deploy a workflow, what each step changes, and how to roll back.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Test and release

**Build → Integrations → Workflows** → open a workflow · [Open in Fastn](https://app.fastn.dev/integrations?tab=workflows)

A change to a workflow goes through three steps before it handles real traffic. Each step has its own button.

```
Save (draft) → Publish (version) → Deploy (to an environment)
```

* **Save:** stores your edits as a draft. Nothing that runs changes.
* **Publish:** freezes the draft as a new numbered version (v1, v2 and so on). The `test` environment always runs the newest published version.
* **Deploy:** puts a published version into an environment, such as `live`, where it handles calls and triggers aimed at that environment.

{% hint style="warning" %}
**Publishing can reach real traffic before you deploy anything.** A trigger runs in the environment set on its route, and that defaults to **test (latest published)**: the workflow's newest published version. So every trigger left on that default runs your new version the moment you publish, with no deploy step. If a trigger should only run what you have explicitly deployed, set its route's environment to a named environment such as `live`. See [Triggers](../triggers/README.md).
{% endhint %}

### How to do each one

#### Save

On a new workflow, select **Create Workflow**. On an existing one, select **Save workflow**. Edits to an existing workflow also save automatically, and the editor shows **Saving…** and then **✓ Draft saved**.

Saving doesn't change what runs. A workflow that has never been published shows `Unpublished`, and every call to it returns `WORKFLOW_NOT_PUBLISHED`.

#### Publish

In the editor's **Publish & Deploy** section, select **Publish snapshot**. You can also select **Run** on the workflow's row and use **Publish now** on the **Publish & Deploy** card there.

Fastn saves the current code and configuration as the next numbered version, and confirms with *Published vN. Deploy it to make it live.* The new version doesn't reach `live` or any other named environment until you deploy it. It does reach the `test` environment straight away, and with it every trigger routed to **test (latest published)** (see the warning above).

If **Require review before publishing** is on for your connected GitHub repository (on [Environments](../../manage/environments.md)), **Publish snapshot** opens a pull request instead. The version is created when the pull request merges, and until then the workflow shows `In review`.

#### Deploy

Select **Deploy to environment** and choose:

* **Version:** the published version to deploy. Defaults to the newest.
* **Environment:** where to run it. Defaults to your default environment.

The button is disabled until the workflow has at least one published version (*Publish a snapshot first*).

{% hint style="info" %}
**Deploying an older version is how you roll back.** There is no separate rollback command. Pick the last good version number in the **Version** dropdown and deploy it to the environment you need to fix.
{% endhint %}

### See what is deployed where

The **Publish & Deploy** section lists every environment with the version running in it, and how many versions behind the newest it is. A gap means a published fix hasn't been deployed there yet, which is the most common reason a fix doesn't seem to work.

The version table also records who published each version and which environments it reached.

### When an environment requires review

If an environment is marked **Requires review**, deploying to it opens a pull request on your connected GitHub repository instead. The deployment stays **pending** until the pull request is merged.

This needs both a connected repository and **Requires review** turned on for that environment. You set both on [Environments](../../manage/environments.md) · [Open in Fastn](https://app.fastn.dev/settings/environments).

### When Publish and Deploy are disabled

Publishing and deploying work the same whether code editing is on or off. **Publish snapshot** and **Deploy to environment** are disabled only when:

* your organization can see workflow code but can't save it (read-only code),
* the workflow comes from your provider, so you can run it and read its runs but not edit it, or
* for **Deploy to environment** only, the workflow has no published version yet.

### What you can do next

* [Test a workflow](the-tabs.md): run and check a workflow before you publish it.
* [Triggers](../triggers/README.md): choose which environment each trigger runs in.
* [Environments](../../manage/environments.md): add a stage and put a review gate in front of it.
