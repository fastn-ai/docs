---
description: Values your workflow code reads per environment.
---

# Configs

**Settings → Configs**

> A config holds anything that changes between test and live, like an endpoint or a feature flag. Read one with `fastn.envConfig.get`.

```javascript
const endpoint  = await fastn.envConfig.get("PARTNER_API_BASE");
const batchSize = await fastn.envConfig.get("BATCH_SIZE");
```

### Creating one

**Add config** — or **Add your first config** on the empty state — takes a name and a value per environment. The same name resolves to a different value depending on which environment the run is in, so your code never branches on environment.

### Configs are readable

Unlike [secrets](secrets.md), configs are not encrypted and are visible in the dashboard. That is the point: you want to be able to see what an environment is set to without running anything.

### Choosing between a config and a secret

| Use a **config** for                        | Use a **secret** for                      |
| --------------------------------------------- | ------------------------------------------- |
| Base URLs and endpoints                      | API tokens and passwords                   |
| Feature flags                                | Signing and encryption keys                |
| Batch sizes, page sizes, thresholds          | Database connection strings                |
| Anything you would happily show a colleague  | Anything whose exposure is an incident     |

{% hint style="warning" %}
When in doubt, use a secret. A config that turns out to be sensitive is already visible to everyone who can read settings.
{% endhint %}

### A common pattern

Point test at a sandbox and live at production, without a line of conditional code:

| Config              | test                              | live                          |
| ------------------- | --------------------------------- | ----------------------------- |
| `PARTNER_API_BASE`  | `https://sandbox.partner.example` | `https://api.partner.example` |
| `BATCH_SIZE`        | `10`                              | `500`                         |
| `DRY_RUN`           | `true`                            | `false`                       |

Which environment a run uses is decided by the `x-fastn-env` header or the trigger route — see [Environments](environments.md).
