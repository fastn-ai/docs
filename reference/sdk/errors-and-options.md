---
description: "Request options (retry keys, tracing, time limits, extra fields) and the errors the SDK throws."
---

# Errors, retries and options

## Request options

Every SDK method takes an optional **last argument** with request options. All of them are optional.

```typescript
await contacts.create(
  { first_name: "Jane", email: "jane@example.com" },
  { idempotencyKey: "signup_9f2_contact", correlationId: "signup_9f2", timeoutMs: 10_000 },
);
```

| Option | Sent as | What it does |
| ------ | ------- | ------------ |
| `idempotencyKey` | `Idempotency-Key` header | Makes a write safe to retry (below). |
| `correlationId` | `X-Fastn-Correlation-Id` header | Your own id for the request, to look up later (below). |
| `timeoutMs` | | A time limit for this call, in milliseconds. Overrides the client's `timeoutMs`. |
| `retries` | | How many retries for this call. `0` never retries. Overrides the client's `retries`. |
| `signal` | | An `AbortSignal`, to cancel the call yourself. |
| `customer` | `x-end-org-ref` or `x-end-org-id` header | Run the call for one customer: `{ ref: "acme_customer_42" }` (your id) or `{ id: "<fastn id>" }`. `fastn.customer(ref)` sets this for you. |
| `installationId` | `x-installation-id` header | Run the call for one installation. |
| `headers` | | Extra headers, sent as given. |
| `extraQuery` | query string | Query parameters the SDK does not know yet, sent as given. |
| `extraBody` | request body | Body fields the SDK does not know yet, merged over the body. |

`extraQuery` and `extraBody` are for a new API field that the SDK has not caught up with. They are not checked.

```typescript
const withUsage = await fastn.orgs.listOrgs({ type: "end_org" }, { extraQuery: { include_usage: "true" } });
```

### Safe retries: idempotencyKey

Pass an `idempotencyKey` on unified record writes (create, update, delete). If you send the same request again with the same key, fastn returns the first answer (for a create, the same record `id`) instead of acting twice.

```typescript
const first = await meetings.create(
  { title: "Intro call", start_time: "2026-11-03T15:00:00Z", end_time: "2026-11-03T15:30:00Z" },
  { idempotencyKey: "booking_123" },
);

// a retry of the same step, with the same key, returns the same meeting
const again = await meetings.create(
  { title: "Intro call", start_time: "2026-11-03T15:00:00Z", end_time: "2026-11-03T15:30:00Z" },
  { idempotencyKey: "booking_123" },
);
// again.id === first.id
```

* Use one key per step, for example `<your request id>_book_1`. Reuse it only to retry that same step.
* The same key with a **different** body is refused: `422 IDEMPOTENCY_KEY_REUSED`. Use a new key for a new request.

### Automatic retries

The SDK retries a call on `429`, `502`, `503`, `504` and network errors, up to `retries` times (default 2), and waits for `Retry-After` when the API sends it. It does this only when a repeat is safe:

* reads (`GET` calls), always;
* writes, only when they carry an `idempotencyKey` **and** the operation is one fastn de-duplicates by that key (unified record create, update and delete, and workflow execute).

Every other write is never retried, so a lost answer can never make it act twice.

### Trace a request: correlationId

Send your own id as `correlationId` on unified calls. Then ask what fastn did for it:

```typescript
await meetings.update(
  "5k8j2m1n0p9q8r7s6t5u4v3w2x",
  { start_time: "2026-11-03T16:00:00Z", end_time: "2026-11-03T16:30:00Z" },
  { idempotencyKey: "booking_123_move", correlationId: "req_abc" },
);

const calls = await fastn.unified.listUnifiedCalls({ correlation_id: "req_abc" });
for (const c of calls.data ?? []) {
  console.log(c.operation, c.connectorSlug, c.status, c.durationMs);
}
```

Each row: `id`, `correlationId`, `endOrgId`, `category`, `entity`, `operation`, `connectorSlug`, `executionId`, `status`, `durationMs`, `createdAt`.

---

## Errors

Every non-2xx answer throws a `FastnApiError`. A request that never got an answer (network failure, time limit, cancelled) throws a `FastnNetworkError`.

```typescript
import { FastnApiError, FastnNetworkError } from "@fastn-ai/sdk";

try {
  await meetings.create(
    { title: "Intro call", start_time: "2026-11-03T15:00:00Z", end_time: "2026-11-03T15:30:00Z" },
    { idempotencyKey: "booking_123" },
  );
} catch (e) {
  if (e instanceof FastnApiError) {
    switch (e.code) {
      case "UNIFIED_NO_CONNECTED_PROVIDER": /* ask the customer to connect the app */ break;
      case "UNIFIED_VALIDATION_FAILED":     /* fix the fields: e.message names the field */ break;
      default:
        console.error(e.status, e.code, e.message, "request id:", e.requestId);
    }
  } else if (e instanceof FastnNetworkError) {
    // no answer: retry later with the same idempotencyKey
  } else {
    throw e;
  }
}
```

### FastnApiError

| Field | Meaning |
| ----- | ------- |
| `status` | The HTTP status, for example `404`. |
| `code` | The API's error code, for example `UNIFIED_VALIDATION_FAILED`. Some errors have no code: use `status` then. |
| `message` | The method, path, status, code and the API's message, for example `POST /v1/unified/{category}/{entity} -> 400 UNIFIED_VALIDATION_FAILED: Field "title" is required`. |
| `details` | Extra details the API sent, when any. |
| `requestId` | fastn's id for the failed request. Quote it when you ask fastn for help. |
| `method`, `path` | The call that failed. |
| `body` | The raw answer body. |
| `isNotFound`, `isConflict`, `isRateLimited`, `isAuth`, `isValidation` | Shortcuts for the common cases (`404`, `409`, `429`, `401`/`403`, `400`/`422`). |

### FastnNetworkError

| Field | Meaning |
| ----- | ------- |
| `message` | What happened, for example `GET /v1/unified/categories: The operation was aborted due to timeout`. |
| `method`, `path` | The call that failed. |
| `cause` | The underlying error, when there is one. |

### Common errors

| Status and code | Means | What to do |
| --------------- | ----- | ---------- |
| `400 UNIFIED_VALIDATION_FAILED` | A unified field is unknown, has the wrong type, or a required field is missing. | Fix the fields. The message names the field. |
| `400 VALIDATION_ERROR` | The request does not match the operation's input, for example an `http` URL where https is needed. | Fix the input. |
| `400 SETUP_LINK_REDIRECT_NOT_ALLOWED` | The setup link's `redirectUrl` is not registered. | Register it (see [Connecting apps](connecting-apps.md#redirect-addresses)). |
| `401` / `403` | The key is wrong, revoked, or not allowed to do this. | Check the key on [Settings → API keys](../../manage/api-keys.md). |
| `404 NOT_FOUND` (or `404` with no code) | The thing you asked for does not exist. | Check the id. |
| `404 UNIFIED_NO_CONNECTED_PROVIDER` | The customer has not connected an app for this entity. | Send a [setup link](connecting-apps.md#setup-links). |
| `404 UNIFIED_UNSUPPORTED_OPERATION` | The app does not offer that operation for this entity. | Use a [direct app action](app-actions.md). |
| `404 UNIFIED_CONNECTION_NOT_FOUND` | The `connectionId` is wrong, removed or not active. | Stop using it; pick a connection from `customer.connections()`. |
| `422 IDEMPOTENCY_KEY_REUSED` | The same `idempotencyKey` was used for a different request. | Use a new key for a new request. |
| `502 UNIFIED_PROVIDER_ERROR` | The app refused the request. | Read `e.body.providerStatus` and `e.body.providerError` (the app's own status and message); check the record id or fields. |

See [Unified records](unified-records.md#errors-from-unified-calls) for every unified code, and [Errors and failure states](../errors.md) for failures you see in the dashboard.
