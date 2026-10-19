---
description: How to save, publish and deploy a workflow — the three buttons, where they are, and what each one actually does.
---

# Lifecycle

**Build → Workflows →** open a workflow

```
Create → Save (draft) → Publish (snapshot) → Deploy (to an environment)
```

Three separate actions, three separate buttons. Nothing you do in the editor reaches real traffic until you deploy.

| Stage | Effect |
| ----------- | ----------------------------------------------------------------------- |
| **Save** | Persists the draft. Nothing goes live. |
| **Publish** | Creates v1, v2, … A snapshot, so rollback is deploying an older one. |
| **Deploy** | The version starts handling real events in that environment. |

### How to do each one

#### Save

**Save** sits in the workflow editor and reads **Saving…** while it works. On the create form the same button reads **Save workflow**.

Saving only persists your draft. A saved workflow has no version yet and is running nowhere.

#### Publish

Open the **Publish & Deploy** panel and select **Publish snapshot**. (The draft row in the same panel offers **Publish now**, which does the same thing.)

A publish freezes the current code as the next numbered version. When it succeeds the confirmation reads *Published successfully — ready to deploy to any environment*, which is the distinction worth internalising: publishing makes a version **available**, it does not put it anywhere.

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

The **Publish & Deploy** panel lists every environment with the version currently active in it, and flags how many versions behind that is. An environment showing a gap is one where a published fix has not been deployed yet — the most common reason for "I fixed it but it is still broken".

The version table also records who published each version and which environments it reached.

### When an environment requires review

An environment can be marked **Requires review**. Promoting to one of those opens a pull request on the connected GitHub repository instead of deploying straight away, and the deployment stays **pending** until that pull request is merged.

The setting is per environment and lives on [Environments](../../manage/environments.md), which is also where the repository is connected. The gate needs both: a connected repository **and** **Requires review** switched on for the environment you are promoting into.

### When code editing is switched off

Code editing is a per-workspace setting, and it is off in almost every workspace — it is enabled only for the parent organisation.

Where it is off, a banner says so and the editor has no code column. Workflows are generated and updated by the AI builder, and you change behaviour by talking to the [agent](../agent/README.md) rather than editing a file. **Publish snapshot** and **Deploy to environment** are disabled in that mode, so publishing and deploying are driven through the agent too.

Everything else is unchanged: you still test, wire connectors, edit the contract, and the runtime surface is identical. Code editing can be switched on if you want to write workflow code yourself — ask fastn to enable it.

### What you can do next

* [The tabs](the-tabs.md) — testing a workflow before you publish it
* [Environments](../../manage/environments.md) — adding a stage and putting a review gate in front of it
