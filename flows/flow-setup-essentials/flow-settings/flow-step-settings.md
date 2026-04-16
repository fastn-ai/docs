---
description: >-
  Configure step-level behavior in your Fastn flows. Learn how to skip steps,
  add notes, group steps with labels, and set up automatic retries.
---

# Flow step settings

Every flow component in Fastn — connectors, switches, loops, data mappers, and more — includes a **Settings** panel where you control how that step behaves at runtime. These step-level settings help you test, document, organize, and harden your flows.

To open the Settings panel, click the **Settings icon** in the **top-right corner** of any component on the canvas.

<figure><img src="../../../.gitbook/assets/image (63).png" alt="Flow step Settings panel accessed via the Settings icon in the top-right corner of a component"><figcaption></figcaption></figure>

The panel contains four key features:

| Feature | Purpose | Access |
|---------|---------|--------|
| [Skip](#skip-a-step) | Temporarily disable a step during testing | Three-dot menu on the step |
| [Step notes](#step-notes) | Document the purpose or logic of a step | Settings tab |
| [Step labels](#step-labels) | Visually group related steps on the canvas | Settings tab |
| [Retry mechanism](#retry-mechanism) | Automatically retry a step on failure | Settings tab |

---

## Skip a step

Skip lets you temporarily disable a step so the flow bypasses it during test runs. The step stays in the flow but does not execute.

### How to skip a step

1. Hover over the step you want to skip on the canvas.
2. Click the **three-dot menu** (⋮) in the top-right corner of the step.
3. Select **Skip** from the dropdown.

The step displays a **dotted border** on the canvas, indicating it is skipped. The flow treats the step as if it does not exist during execution — downstream steps that depend on its output receive no data from it.

### How to unskip a step

1. Click the **three-dot menu** (⋮) on the skipped step.
2. Select **Unskip** to restore normal execution.

The dotted border disappears and the step executes normally on the next run.

### When to use skip

| Scenario | Example |
|----------|---------|
| **Isolating a failure** | Skip steps one at a time to find which step causes an error |
| **Testing a partial flow** | Skip a Slack notification step while testing data transformation logic |
| **Bypassing slow steps** | Skip a step that calls a rate-limited API while iterating on earlier steps |
| **Comparing results** | Run the flow with and without a step to compare output |

{% hint style="warning" %}
Skipped steps do not produce output. If a downstream step maps data from a skipped step, that mapping resolves to empty. Verify your data flow before relying on test results with skipped steps.
{% endhint %}

{% hint style="info" %}
Skip is a **testing and debugging tool**. It does not affect deployed flows. Remove all skips before deploying to production.
{% endhint %}

---

## Step notes

Step notes let you add free-text documentation directly to a step. Use notes to explain why a step exists, what logic it applies, or any context a collaborator needs.

### How to add a note

1. Click the **Settings icon** on the step to open the Settings panel.
2. Scroll to the **Step Note** field.
3. Enter your note text.

<figure><img src="../../../.gitbook/assets/image (66).png" alt="Step Note text field for adding comments about the purpose or logic of a flow step"><figcaption></figcaption></figure>

After you save a note, a **note icon** appears on the step in the canvas. Click the icon to quickly view the note without opening the full Settings panel.

### When to use step notes

| Scenario | Example note |
|----------|--------------|
| **Explaining business logic** | "Filters orders over $500 per compliance policy CP-204" |
| **Flagging workarounds** | "Uses v1 endpoint because v2 does not support bulk queries yet" |
| **Documenting decisions** | "Switch added to handle both JSON and XML responses from vendor" |
| **Onboarding collaborators** | "This loop processes each line item from the Shopify webhook payload" |

{% hint style="info" %}
Clear notes make debugging faster. When a flow fails at 2 AM, the on-call engineer sees your note and understands the intent immediately.
{% endhint %}

---

## Step labels

Step labels let you visually group related steps on the canvas. A label creates a named region that surrounds the steps you assign to it, making complex flows easier to scan and navigate.

### How to add a label

1. Click the **Settings icon** on a step to open the Settings panel.
2. Find the **Step Label** field.
3. Enter a label name (for example, "Data Validation" or "Notification Block").

All steps that share the same label name are grouped together visually on the canvas under that label.

### How labels appear on the canvas

Steps with the same label display inside a shared visual boundary with the label name shown above them. This grouping is purely visual — it does not change execution order or data flow.

### When to use step labels

| Scenario | Example label |
|----------|---------------|
| **Identifying logical phases** | "Input Validation", "Data Transformation", "Output" |
| **Grouping by integration** | "Salesforce Sync", "Slack Notifications" |
| **Marking error-handling blocks** | "Error Handling", "Retry Logic" |
| **Organizing large flows** | "Phase 1: Fetch Data", "Phase 2: Process", "Phase 3: Store" |

{% hint style="info" %}
Labels are especially valuable in flows with 10 or more steps. They turn a flat sequence of steps into a readable, self-documenting flow diagram.
{% endhint %}

---

## Retry mechanism

The retry mechanism configures automatic retries when a step fails. This is critical for connector and API steps where transient errors (network timeouts, rate limits, temporary service outages) are common.

### How to configure retries

1. Click the **Settings icon** on the step to open the Settings panel.
2. Locate the **Retry Settings** section.

<figure><img src="../../../.gitbook/assets/image (64).png" alt="Retry Settings panel with Make Step Required checkbox to stop flow on step failure"><figcaption></figcaption></figure>

### Make step required

Enable the **Make Step Required** checkbox to mark a step as critical to the flow.

| Setting | Behavior |
|---------|----------|
| **Enabled** | The flow stops immediately if this step fails after all retry attempts are exhausted. No downstream steps execute. |
| **Disabled** (default) | The flow continues to the next step even if this step fails. |

Use **Make Step Required** for steps where failure means the rest of the flow produces invalid results — for example, an authentication step or a primary data fetch.

### When to use retries

| Scenario | Recommended approach |
|----------|---------------------|
| **Calling external APIs** | Enable retries to handle rate limits and transient network errors |
| **Database writes** | Enable retries with the step marked as required to prevent partial data |
| **Sending notifications** | Enable retries but leave the step as not required — a failed Slack message should not block the flow |
| **Data transformation steps** | Retries are usually unnecessary — transformation failures are logic errors, not transient |

{% hint style="warning" %}
Retries are most effective for **transient** errors. If a step fails due to incorrect configuration (wrong endpoint, missing field), retrying produces the same error. Fix the root cause instead.
{% endhint %}

{% hint style="info" %}
Combine retries with the **Make Step Required** checkbox for critical integration steps. This ensures the flow retries on transient failures and stops cleanly if the step ultimately fails.
{% endhint %}

---

## Feature summary

Use this table to decide which features to apply during flow development:

| Development phase | Feature | Action |
|-------------------|---------|--------|
| **Building** | Step labels | Group steps into logical sections as you add them |
| **Building** | Step notes | Document each step's purpose while the context is fresh |
| **Testing** | Skip | Disable steps to isolate and debug specific parts of the flow |
| **Hardening** | Retry mechanism | Add retries to connector and API steps before deploying |
| **Hardening** | Make step required | Mark critical steps that must succeed for the flow to produce valid results |

---

## Related

* [Flow Settings](README.md) — configure flow-level behavior (type, validation, authentication, visuals)
* [Debugging & Troubleshooting](../../debugging-and-troubleshooting.md) — use the Test button, Logs page, and Logger step to diagnose flow issues
* [Connectors](../designing-a-flow/connectors.md) — connect your flow to external services and APIs
