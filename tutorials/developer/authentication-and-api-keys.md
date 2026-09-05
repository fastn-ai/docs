# Authentication & API Keys

Fastn API keys authenticate your backend's requests — including generating embed tokens. Keys come in test and live variants, and each requires different handling.

### Where to find your keys

Go to **Settings → API Keys**. The page has a **Test / Live toggle** in the top-right and a keys table with a **MODE** column — each key shows a badge indicating whether it's a LIVE or TEST key. Click **+ Create API Key** to generate one. Keys are shown once at creation — copy and store it securely.

When viewing test data, the page shows a banner: "Test keys only work with the X-fastn-Test-Mode: true header."

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

Without it, requests with a test key fail in ways that aren't obvious from the error. If you're getting unexpected failures with a test key, this header is the first thing to check.

#### Live keys must not send that header

Requests with a `fsk_live_` key must **not** include `X-fastn-Test-Mode`. Send the header only with test keys.

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
* The API key is used to mint embed tokens on your backend — it should never reach the browser. See [Generating Embed Tokens](https://claude.ai/fastn/tutorials/developer/generating-embed-tokens).
