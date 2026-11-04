---
description: How to save, publish and deploy a workflow - the three buttons, where they are, and what each one actually does.
---

# Lifecycle

**Build → Integrations → Workflows** tab → open a workflow

```
Create → Save (draft) → Publish (snapshot) → Deploy (to an environment)
```

Three separate actions, three separate buttons.

| Stage | Effect |
| ----------- | ----------------------------------------------------------------------- |
| **Save** | Persists the draft. Nothing new runs anywhere. |
| **Publish** | Creates v1, v2, … A snapshot, so rollback is deploying an older one. The newest published version is also what the **test** environment runs. |
| **Deploy** | Puts a published version into a named environment (for example `live`), where it handles calls and trigger fires that target that environment. |

{% hint style="warning" %}
**Publishing can reach real traffic before you deploy anything.** A trigger route's **Environment** defaults to **test (latest published)**, which runs the workflow's newest published version. Every trigger routed that way starts firing the new version the moment you publish, with no deploy step in between. If a trigger should only run what you have explicitly deployed, set its route's environment to a named environment such as `live`. See [Triggers](../triggers/README.md).
{% endhint %}

### How to do each one

#### Save

When you create a workflow, the form's submit button reads **Create Workflow**. On an existing workflow the button reads **Save workflow**, and **Saving…** while it works. Draft edits to an existing workflow also auto-save; the editor shows **Saving…** and then **✓ Draft saved**.

Saving only persists your draft. A saved draft does not change what runs: a workflow with no published version is `Unpublished`, and every call to it returns `WORKFLOW_NOT_PUBLISHED`.

#### Publish

Open the **Publish & Deploy** panel and select **Publish snapshot**. (The draft row in the same panel offers **Publish now**, which does the same thing.)

A publish freezes the current code as the next numbered version. When it succeeds the toast reads *Published vN. Deploy it to make it live.* Publishing does not put a version into a named environment such as `live`, but it does change what the test environment runs, and so what every trigger routed to **test (latest published)** runs (see the warning above).

If **Require review before publishing** is switched on for your connected GitHub repository (on [Environments](../../manage/environments.md)), **Publish snapshot** opens a pull request instead of creating a version. The toast reads *Publish opened for review. The version is created when the PR merges*, followed by the PR link, and the workflow's row shows `In review` until the pull request is merged.

#### Deploy

Select **Deploy to environment**. The dialog asks for two things:

| Field | Notes |
| ----- | ----- |
| **Version** | Which published snapshot to deploy. Defaults to the newest. |
| **Environment** | Where to run it. Defaults to your default environment. |

Until a workflow has at least one published version this button is disabled, and its tooltip tells you why: *Publish a snapshot first*.

{% hint style="info" %}
**Deploying an older version is how you roll back.** There is no separate rollback command. Pick the last good version number in the **Version** dropdown and deploy it to the environment you need to fix.
{% endhint %}

### Seeing what is deployed where

The **Publish & Deploy** panel lists every environment with the version currently active in it, and flags how many versions behind that is. An environment showing a gap is one where a published fix has not been deployed yet - the most common reason for "I fixed it but it is still broken".

The version table also records who published each version and which environments it reached.

### When an environment requires review

An environment can be marked **Requires review**. Promoting to one of those opens a pull request on the connected GitHub repository instead of deploying straight away, and the deployment stays **pending** until that pull request is merged.

The setting is per environment and lives on [Environments](../../manage/environments.md), which is also where the repository is connected. The gate needs both: a connected repository **and** **Requires review** switched on for the environment you are promoting into.

### When code editing is switched off

Code editing is a per-organization entitlement. It is off by default and is enabled by fastn.

Where it is off, a banner says so and the editor has no code column. Workflows are generated and updated with [Build with AI](../agent/README.md), and you change behavior by asking Build with AI rather than editing a file.

Everything else is unchanged: you still test, wire connectors, edit the contract, publish and deploy, and the runtime surface is identical. Code editing can be switched on if you want to write workflow code yourself; ask fastn to enable it.

**Publish snapshot** and **Deploy to environment** are disabled only when:

* your organization can see workflow code but has had code saving switched off (read-only code), or
* the workflow is inherited from your provider (*Provided by your provider. You can run it and read its executions, but it is not yours to edit.*), or
* for **Deploy to environment** only, the workflow has no published version yet (*Publish a snapshot first*).

### What you can do next

* [The tabs](the-tabs.md) - testing a workflow before you publish it
* [Environments](../../manage/environments.md) - adding a stage and putting a review gate in front of it
