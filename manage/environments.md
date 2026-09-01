---
description: Deployment stages, and the GitHub review gate in front of them.
---

# Environments and GitHub

**Settings → Environments**

<figure><img src="../.gitbook/assets/settings-environments.jpg" alt="Environments and the GitHub connection"><figcaption></figcaption></figure>

> Test and Live are built in. Add a named environment here when you want another stage, such as staging or review.

### Environments

| Column              | Notes                                                                    |
| ------------------- | -------------------------------------------------------------------------- |
| **Name**            | Display name.                                                            |
| **Slug**            | Used in the `x-fastn-env` header and in trigger routes.                  |
| **Type**            | Default, or a named environment you created.                             |
| **Requires review** | Whether publishing to it opens a pull request instead of deploying.      |

Live is marked **Protected** — it cannot be deleted.

**New environment** adds a stage. A named environment runs whatever version is deployed to it, and a trigger pointed at it fails if nothing has been deployed there. That is intentional: it fails loudly rather than silently running the wrong code.

### The special value `test`

In trigger routes and in the `x-fastn-env` header, `test` is not a deployed environment — it means *the workflow's latest published version*. Any other slug means *the version deployed to that environment*.

### GitHub

Connect a repository and promoting to a reviewed environment opens a pull request instead of deploying straight away.

| Control                            | Effect                                                                     |
| ---------------------------------- | ---------------------------------------------------------------------------- |
| **Require review before publishing** | Every workflow opens a pull request instead of deploying straight away.   |
| **Mirror all workflows to this repo** | **Sync to GitHub** pushes the current workflows to the repository.       |
| **Disconnect**                     | Removes the integration. Existing deployments are unaffected.               |

The connected repository and branch are shown, for example `your-org/your-repo (main)`.

{% hint style="success" %}
Turning on **Require review before publishing** is the single change that turns fastn from a place where anyone can push to production into one with a real approval trail. If you have more than a couple of people building, do it.
{% endhint %}

### A workable setup

1. Connect the repository.
2. Add a `staging` environment.
3. Turn on **Require review before publishing**.
4. Developers publish; the PR is reviewed and merged; the version deploys to staging.
5. Promote from staging to live once it has run against real traffic.

Every step lands in the [audit log](audit-log.md) — `workflow.publish`, `workflow.deploy`, `workflow.sync.requested`, `workflow.sync.merged`.
