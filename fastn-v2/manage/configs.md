---
description: Values your workflow code reads per environment.
---

# Configs

**Settings → Configs**

With nothing configured yet, the page reads **No configs yet** above the line that explains the feature:

![The Configs page empty state with Add config and Add your first config](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/configs-empty.jpg)

_The Configs page before any config exists. Read a config from workflow code with `fastn.envConfig.get("key")`._

> A config holds anything that changes between test and live, like an endpoint or a feature flag. Read one with fastn.envConfig.get.

```javascript
const endpoint  = await fastn.envConfig.get("PARTNER_API_BASE");
const batchSize = await fastn.envConfig.get("BATCH_SIZE");
```

### Creating one

**Add config** opens the **Add Config** dialog, which takes two things.

**Key \*** is the string your code passes — `fastn.envConfig.get("PARTNER_API_BASE")` reads the config whose key is `PARTNER_API_BASE`.

**Values per environment** is one editor per environment, labelled with the display name and the slug: **Test (test)**, **Live (live)**, and a row for each named environment you have added. A value may be raw text or valid JSON.

{% hint style="info" %}
**Leaving an environment's editor blank skips that environment on save** — it does not write an empty value. That is usually what you want when you are only setting up test, but it means a config can silently have no value in live.
{% endhint %}

The same key resolves to a different value depending on which environment the run is in, so your code never branches on environment.

### Configs versus secrets

A config's value is entered and edited in the dashboard rather than written once and hidden, which is the practical difference from a [secret](secrets.md): you can see what an environment is set to without running anything. Treat that as the working assumption — anything whose exposure would be an incident belongs in a secret regardless.

### Choosing between a config and a secret

| Use a **config** for                        | Use a **secret** for                   |
| ------------------------------------------- | -------------------------------------- |
| Base URLs and endpoints                     | API tokens and passwords               |
| Feature flags                               | Signing and encryption keys            |
| Batch sizes, page sizes, thresholds         | Database connection strings            |
| Anything you would happily show a colleague | Anything whose exposure is an incident |

{% hint style="warning" %}
When in doubt, use a secret. A config that turns out to be sensitive is already visible to everyone who can read settings.
{% endhint %}

### A common pattern

Point test at a sandbox and live at production, without a line of conditional code:

| Config             | test                              | live                          |
| ------------------ | --------------------------------- | ----------------------------- |
| `PARTNER_API_BASE` | `https://sandbox.partner.example` | `https://api.partner.example` |
| `BATCH_SIZE`       | `10`                              | `500`                         |
| `DRY_RUN`          | `true`                            | `false`                       |

Which environment a run uses is decided by the `x-fastn-env` header or the trigger route — see [Environments](environments-and-github.md).
