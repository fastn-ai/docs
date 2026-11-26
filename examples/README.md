# fastn examples

Small, runnable projects that go with the [fastn docs](https://docs.fastn.ai). Each one does one job and reads its settings from environment variables, so no secret is ever in the code.

| Example | What it does | Language | Docs |
| --- | --- | --- | --- |
| [embed-node](embed-node) | A web page with the fastn widget, and the backend route that mints its embed token | Node.js (Express) | [Embedding quickstart](https://docs.fastn.ai/embed/embedding/embedding-quickstart) |
| [token-server-python](token-server-python) | A backend route that mints an embed token with signed identity headers | Python (Flask) | [Authentication](https://docs.fastn.ai/get-started/authentication-and-api-keys) |
| [crm-contacts-node](crm-contacts-node) | Finds or creates a contact in whichever CRM a customer connected, then adds a note | Node.js, `@fastn-ai/sdk` | [Read and write a customer's CRM records](https://docs.fastn.ai/how-to-guides/how-to/crm-records) |
| [webhook-event-node](webhook-event-node) | Sends an event from your product to a webhook trigger, signed for one customer | Node.js | [Start an integration from your product's events](https://docs.fastn.ai/how-to-guides/how-to/events-from-your-product) |

Every example needs an API key from **Embed → API keys** in the [fastn dashboard](https://app.fastn.dev). Use a `fsk_test_` key while you try them: the examples send the `X-fastn-Test-Mode: true` header that test keys need.
