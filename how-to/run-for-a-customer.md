---
description: Run a workflow from your backend for a named customer, and read the result.
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

# Run an integration for one customer

Your backend needs to run an integration for one customer, for example to sync their orders now, and use the result. One workflow serves all your customers; the `x-org-id` header says which one a call is for.

<figure><img src="../.gitbook/assets/diagrams/run-for-a-customer.svg" alt="Running an integration for one customer: your backend calls fastn with x-org-id, fastn loads that customer's setup, calls their apps, and returns the result or an execution id."><figcaption><p>fastn uses the named customer's own connections and settings for the run.</p></figcaption></figure>

### Before you start

* A published workflow. Until a version is published, every call returns `WORKFLOW_NOT_PUBLISHED`. See [Test and release](../build/workflows/lifecycle.md).
* Its workflow id, shown on the workflow's **API** tab, in the form `wf_b5880b29eb25`.
* An API key. See [Authentication](../tutorials/developer/authentication-and-api-keys.md).
* A customer that has connected the apps the workflow uses.

### 1. Call the workflow

Send the input in `input` and name the customer in `x-org-id`. This example uses a test key, so it also sends `X-fastn-Test-Mode: true`:

```bash
curl -X POST https://api.fastn.dev/api/v1/workflows/WORKFLOW_ID/execute \
  -H "Authorization: Bearer fsk_test_<your-key>" \
  -H "X-fastn-Test-Mode: true" \
  -H "x-fastn-env: test" \
  -H "x-org-id: acme_customer_42" \
  -H "Content-Type: application/json" \
  -d '{"input": {"since": "2026-11-01"}}'
```

The `input` object arrives in the workflow as `ctx.input`. Its fields come from the workflow's input contract: the workflow's **API** tab shows a ready curl with the right fields.

### 2. Read the result

What comes back depends on the workflow's execution tier:

| Tier | Response | Result |
| --- | --- | --- |
| **Instant** | `200`, within 25 seconds | The workflow's return value is the response body. The execution id is in the `X-Execution-Id` header. |
| **Standard** or **Long** | `202 Accepted` | The run continues in the background. The execution id is at `data.executionId`. |

For Standard and Long runs, poll until the run finishes:

```bash
curl https://api.fastn.dev/api/v1/workflows/WORKFLOW_ID/executions/EXECUTION_ID \
  -H "Authorization: Bearer fsk_test_<your-key>" \
  -H "X-fastn-Test-Mode: true"
```

**You should see:** the run in **Operate → Activity → Executions**, with its input, output and the time each step took.

### If the call fails

| Response | Cause |
| --- | --- |
| `404 IDENTITY_ORG_NOT_FOUND` | `x-org-id` does not name one of your customers |
| `403` with *Test API keys require X-fastn-Test-Mode: true header* | A test key without the test-mode header |
| `401 IDENTITY_HEADERS_REQUIRED` | The key enforces identity verification: send `x-user-id` and `x-identity-hmac` too |

### Related

* [HTTP API](../reference/api.md): the full execute reference and every scoping header
* [Start an integration from your product's events](events-from-your-product.md)
* [Executions](../operate/executions.md)
