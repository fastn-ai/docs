---
description: "Run an app's own action with a customer's connection, for anything the unified API does not cover."
---

# Direct app actions

The [unified records](unified-records.md) cover the common records. For anything else (a field the unified shape does not have, an operation an app does not offer through the unified API) run the app's own action, with the customer's own connection.

It takes three steps: find the action, read its input fields, run it.

```typescript
// 1. Find the action's slug
const actions = await fastn.connectors.listConnectorActionsBySlug({ connector: "hubspot" });
// actions.data = [ { id, slug: "getContact", name: "Get Contact", version, description }, … ]

// 2. Read its input fields
const schema = await fastn.connectors.getConnectorActionSchema({ connector: "hubspot", action: "getContact" });
// schema.data.inputContract = { type: "object", required: ["contactId"], properties: { contactId: {…}, properties: {…}, … } }

// 3. Run it for the customer
const r = await customer.runAction({
  connector: "hubspot",
  action: "getContact",
  input: { contactId: "51234567890" },
});

if (r.data?.success) {
  console.log(r.data.response);    // the app's own answer
}
```

---

## Find actions and their fields

| Do this | SDK | Input | Answer |
| ------- | --- | ----- | ------ |
| List an app's actions | `fastn.connectors.listConnectorActionsBySlug({ connector })` | `connector` (required): the app's slug, for example `hubspot`. | `{ data: [ { id, slug, name, version, description } ] }` |
| Read one action's fields | `fastn.connectors.getConnectorActionSchema({ connector, action })` | `connector` and `action` (both required): the app's slug and the action's slug. | `{ data: { slug, name, inputContract, outputContract } }` |

`inputContract` is a JSON schema. Its `required` list holds the fields you must send; `properties` describes every field.

---

## runAction

```typescript
const r = await customer.runAction({ connector: "hubspot", action: "getContact", input: { contactId: "51234567890" } });
```

| Field | Required | Meaning |
| ----- | -------- | ------- |
| `connector` | Yes | The app's slug, the same as `connector.slug` in `customer.connections()`. |
| `action` | Yes | The action's **slug** from `listConnectorActionsBySlug`, for example `getContact`. The display name (`Get Contact`) is refused. |
| `input` | Depends on the action | The fields from the action's `inputContract`. |

The SDK runs the action with **this customer's** connection for that app, so it never uses your own org's account by mistake.

### Answer

```json
{
  "data": {
    "id": "…",
    "actionId": "…",
    "connectionId": "ucl:…:default",
    "success": true,
    "status": 200,
    "response": { "id": "51234567890", "properties": { "email": "jane@example.com" }, "archived": false },
    "durationMs": 412,
    "executedAt": "2026-10-25T23:59:10.000Z",
    "requestUrl": "…",
    "requestBody": null
  }
}
```

| Field | Meaning |
| ----- | ------- |
| `success` | `true` when the app answered with success. |
| `status` | The app's HTTP status, for example `200` or `404`. |
| `response` | The app's own answer, unchanged. |
| `error` | Present when the app answered with an error: the app's error body. |
| `connectionId` | The connection the action ran with. |
| `durationMs`, `executedAt` | How long it took, and when. |

{% hint style="warning" %}
**An error from the app does not throw.** When the app itself answers with an error (for example a record id that does not exist), `runAction` still returns normally, with `data.success: false`, the app's `data.status` (for example `404`) and `data.error`. Always check `success`.

`runAction` throws a `FastnApiError` when fastn cannot run the action at all, for example an unknown action slug (`404 NOT_FOUND`, "connector hubspot has no action …").
{% endhint %}

```typescript
const r = await customer.runAction({ connector: "hubspot", action: "getContact", input: { contactId: "1" } });

if (!r.data?.success) {
  console.log("the app said", r.data?.status, r.data?.error);
}
```
