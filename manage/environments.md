---
description: Deployment stages, and the GitHub review gate in front of them.
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

# Environments and GitHub

**Settings → Environments** - in your dashboard, `/settings/environments`. Visible to **developer** and above.

<figure><img src="../.gitbook/assets/screens/settings-environments.webp" alt="Settings, Environments: a New environment button, a GitHub card reading No repository connected with Connect GitHub, and Guardrails with three switches: live uses only live secrets, Runs kept for live, and Separate data per environment"><figcaption>Test and Live are built in. Guardrails are off until you turn them on.</figcaption></figure>

> Test and Live are built in. Add a named environment here when you want another stage, such as staging or review.

### Environments

| Column              | Notes                                                                    |
| ------------------- | -------------------------------------------------------------------------- |
| **Name**            | Display name.                                                            |
| **Slug**            | Used in the `x-fastn-env` header and in trigger routes.                  |
| **Type**            | A badge reading `Default` (your default environment) or `Custom` (a named environment you created). |
| **Requires review** | A toggle per environment, off by default. Switched on, promoting to it opens a pull request instead of deploying. |

An environment that cannot be deleted shows **Protected** in place of the delete button. Live is one of them: it cannot be deleted. Other environments have a delete button at the end of their row.

**New environment** opens the **Create Environment** dialog, which adds a stage and asks for two things:

| Field       | Notes                                              |
| ----------- | ---------------------------------------------------- |
| **Name \*** | Display name, for example `Staging`.                |
| **Slug \*** | What goes in `x-fastn-env` and in trigger routes. The form notes that `test` and `live` are built in, so those two are taken. |

A named environment runs whatever version is deployed to it. If nothing has been deployed there, there is no code for a trigger pointed at it to run: deploy before you point traffic at a new stage.

### The special value `test`

In trigger routes and in the `x-fastn-env` header, `test` is not a deployed environment. It means *the workflow's latest published version*. Any other slug means *the version deployed to that environment*. That is why the table is a list of deployment targets, with `test` handled by the platform rather than sitting among them.

### GitHub

A **GitHub** panel sits above the table, explaining what connecting a repository does:

> Connect a repository and promoting to a reviewed environment opens a pull request instead of deploying straight away.

Until you connect one, its status reads **No repository connected** and the only control is **Connect GitHub**. That is what a new organization sees, and it is worth knowing that the review gate does nothing on its own: it needs both a repository here and **Requires review** switched on for the environment you are promoting into.

Once a repository is connected the panel shows it as `owner/repo` with its default branch, and offers:

| Control | What it does |
| ------- | ------------ |
| **Change repository** | Points the connection at a different repository. |
| **Disconnect** | Removes the repository connection. |
| **Require review before publishing** | A toggle. When on, *every workflow opens a pull request instead of deploying straight away*: **Publish snapshot** opens a PR, the new version is created when the PR merges, and the workflow's row shows `In review` until then. |
| **Mirror all workflows to this repo** | With a **Sync to GitHub** button, which opens a pull request that copies your workflows into the repository. |

Pull requests that are still open appear in an **Awaiting review** card, where you can cancel one to unblock without applying it.

### A workable setup

1. Connect the repository.
2. Add a `staging` environment.
3. Tick **Requires review** on it.
4. Developers publish; the promotion opens a pull request; the reviewed and merged version deploys to staging.
5. Promote from staging to live once it has run against real traffic.

{% hint style="success" %}
A connected repository plus **Requires review** puts a pull request and an approval trail in front of every promotion to that environment. If more than a couple of people build workflows, set up both.
{% endhint %}

Publishing and deploying are both recorded in the [audit log](audit-log.md).
