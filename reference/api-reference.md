---
description: >-
  Core and platform endpoints, authentication headers, error codes, and rate
  limiting.
---

# API Reference

Base URL: `https://live.fastn.ai`

### Authentication headers

| Header            | Required     | Description                                       |
| ----------------- | ------------ | ------------------------------------------------- |
| `x-fastn-api-key` | Yes          | Your API key (Settings → API Keys — Test or Live) |
| `Content-Type`    | For POST/PUT | `application/json`                                |

{% hint style="info" %}
⚠️ **VERIFY:** Confirm whether `x-fastn-space-id` and `x-fastn-space-tenantid` headers are still required in Fastn, or if the API key scopes requests automatically.
{% endhint %}

### Core endpoints

#### Customers

| Method   | Path                     | Description          |
| -------- | ------------------------ | -------------------- |
| `GET`    | `/api/v1/customers`      | List all customers   |
| `POST`   | `/api/v1/customers`      | Create a customer    |
| `GET`    | `/api/v1/customers/:cid` | Get customer details |
| `PUT`    | `/api/v1/customers/:cid` | Update a customer    |
| `DELETE` | `/api/v1/customers/:cid` | Delete a customer    |

#### Connectors

| Method   | Path                      | Description           |
| -------- | ------------------------- | --------------------- |
| `GET`    | `/api/v1/connectors`      | List connectors       |
| `POST`   | `/api/v1/connectors`      | Create a connector    |
| `GET`    | `/api/v1/connectors/:cid` | Get connector details |
| `PUT`    | `/api/v1/connectors/:cid` | Update a connector    |
| `DELETE` | `/api/v1/connectors/:cid` | Delete a connector    |

#### Connections

| Method   | Path                       | Description         |
| -------- | -------------------------- | ------------------- |
| `GET`    | `/api/v1/connections`      | List connections    |
| `POST`   | `/api/v1/connections`      | Create a connection |
| `DELETE` | `/api/v1/connections/:cid` | Delete a connection |

#### Workflows

| Method   | Path                         | Description          |
| -------- | ---------------------------- | -------------------- |
| `GET`    | `/api/v1/workflows`          | List workflows       |
| `POST`   | `/api/v1/workflows`          | Create a workflow    |
| `GET`    | `/api/v1/workflows/:wid`     | Get workflow details |
| `PUT`    | `/api/v1/workflows/:wid`     | Update a workflow    |
| `DELETE` | `/api/v1/workflows/:wid`     | Delete a workflow    |
| `POST`   | `/api/v1/workflows/:wid/run` | Run a workflow       |

#### Triggers

| Method   | Path                    | Description         |
| -------- | ----------------------- | ------------------- |
| `GET`    | `/api/v1/triggers`      | List triggers       |
| `POST`   | `/api/v1/triggers`      | Create a trigger    |
| `GET`    | `/api/v1/triggers/:tid` | Get trigger details |
| `PUT`    | `/api/v1/triggers/:tid` | Update a trigger    |
| `DELETE` | `/api/v1/triggers/:tid` | Delete a trigger    |

#### Executions

| Method | Path                      | Description           |
| ------ | ------------------------- | --------------------- |
| `GET`  | `/api/v1/executions`      | List executions       |
| `GET`  | `/api/v1/executions/:eid` | Get execution details |

### Platform endpoints

#### People & Roles

| Method | Path                   | Description        |
| ------ | ---------------------- | ------------------ |
| `GET`  | `/api/v1/users`        | List users         |
| `POST` | `/api/v1/users/invite` | Invite a user      |
| `GET`  | `/api/v1/roles`        | List roles         |
| `POST` | `/api/v1/roles`        | Create custom role |

#### API Keys

| Method   | Path                    | Description    |
| -------- | ----------------------- | -------------- |
| `GET`    | `/api/v1/api-keys`      | List API keys  |
| `POST`   | `/api/v1/api-keys`      | Create API key |
| `DELETE` | `/api/v1/api-keys/:kid` | Revoke API key |

#### Secrets

| Method   | Path                   | Description   |
| -------- | ---------------------- | ------------- |
| `GET`    | `/api/v1/secrets`      | List secrets  |
| `POST`   | `/api/v1/secrets`      | Create secret |
| `DELETE` | `/api/v1/secrets/:sid` | Delete secret |

#### Billing & Quotas

| Method | Path                     | Description      |
| ------ | ------------------------ | ---------------- |
| `GET`  | `/api/v1/billing`        | Get billing info |
| `GET`  | `/api/v1/billing/usage`  | Get usage data   |
| `GET`  | `/api/v1/billing/quotas` | Get quota limits |

#### Audit

| Method | Path            | Description     |
| ------ | --------------- | --------------- |
| `GET`  | `/api/v1/audit` | Query audit log |

#### AI

| Method | Path               | Description                              |
| ------ | ------------------ | ---------------------------------------- |
| `POST` | `/api/v1/ai/chat`  | Send message to AI agent                 |
| `POST` | `/api/v1/ai/build` | Trigger AI build (connector or workflow) |

{% hint style="info" %}
⚠️ **VERIFY:** These endpoint paths are inferred from the Fastn UI actions. Confirm exact paths, request/response schemas, and required headers against the actual API.
{% endhint %}

### Error codes

| HTTP Status | Description                             |
| ----------- | --------------------------------------- |
| 400         | Invalid request body or parameters      |
| 401         | Missing or invalid API key              |
| 403         | Insufficient permissions                |
| 404         | Resource not found                      |
| 409         | Resource conflict or version mismatch   |
| 422         | Validation error                        |
| 429         | Rate limited — check Retry-After header |
| 500         | Server error                            |

### Rate limiting

* Limits are per API key
* Rate limit headers on every response:

| Header                  | Description                         |
| ----------------------- | ----------------------------------- |
| `X-RateLimit-Limit`     | Max requests in window              |
| `X-RateLimit-Remaining` | Requests remaining                  |
| `X-RateLimit-Reset`     | When window resets (Unix timestamp) |
| `Retry-After`           | Seconds to wait (only on 429)       |
