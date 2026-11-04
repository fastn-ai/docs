---
---

# Authentication & API Keys

fastn API keys authenticate your backend's requests - including generating embed tokens. Keys come in test and live variants, and each requires different handling.

### Where to find your keys

Go to **Embed → API keys and MCP → API keys**. Next to **Search keys**, filter pills read **All**, **Live** and **Test**, and the keys table has a **Mode** column with a **Live** or **Test** badge on each key. Click **Create key** to open the **Create an API key** dialog. Keys are shown once at creation - copy and store it securely.

In that dialog, the **Test** mode card says: "Refused unless the caller sends X-fastn-Test-Mode: true."

### Test vs live keys

Keys are in the `fsk_` format, with two variants:

| Variant | Prefix      | Use for                 |
| ------- | ----------- | ----------------------- |
| Test    | `fsk_test_` | Development and testing |
| Live    | `fsk_live_` | Production              |

#### Test keys require an extra header

Requests made with a `fsk_test_` key **must** include this header:

```
X-fastn-Test-Mode: true
```

Without it, the request is refused with `403` and the error `Test API keys require X-fastn-Test-Mode: true header`. If you're getting unexpected failures with a test key, this header is the first thing to check.

#### Live keys don't need that header

Requests with a `fsk_live_` key do not need `X-fastn-Test-Mode`. Send the header only with test keys.

### Example

Test key:

```javascript
headers: {
  "Authorization": "Bearer fsk_test_...",
  "Content-Type": "application/json",
  "X-fastn-Test-Mode": "true",   // required
}
```

Live key:

```javascript
headers: {
  "Authorization": "Bearer fsk_live_...",
  "Content-Type": "application/json",
  // no X-fastn-Test-Mode header
}
```

### Keeping keys secure

* Store keys in environment variables, never in source code or client-side bundles.
* Use test keys in development and live keys only in production.
* The API key is used to mint embed tokens on your backend - it should never reach the browser. See [Generating Embed Tokens](generating-embed-tokens.md).
