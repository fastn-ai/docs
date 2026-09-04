---
description: How a workflow goes from draft to deployed, review gates, and code-off workspaces.
---

# Lifecycle

```
Create → Save (draft) → Publish (snapshot) → Deploy (to an environment)
```

| Stage       | Effect                                                                |
| ----------- | ----------------------------------------------------------------------- |
| **Save**    | Persists the draft. Nothing goes live.                                 |
| **Publish** | Creates v1, v2, … A snapshot, so rollback is deploying an older one.    |
| **Deploy**  | The version starts handling real events in that environment.           |

An environment can be marked **Requires review**. Promoting to one of those opens a pull request on the connected GitHub repository instead of deploying straight away — the setting is per environment, and lives on [Environments](../../manage/environments.md), which is also where the repository is connected.

### When code editing is switched off

Code editing is a per-workspace setting, and **off in almost every workspace** — it is enabled only for the parent organisation. Where it is off, a banner says so, and the editor simply has no code column: workflows are generated and updated by the AI builder, and you change behaviour by talking to the [agent](../agent/README.md) rather than editing the file. Everything else is unchanged — you still test, wire connectors, edit the contract, publish and deploy, and the runtime surface is identical. It can be switched on if you want to write workflow code yourself; ask fastn to enable it.
