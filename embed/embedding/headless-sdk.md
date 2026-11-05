---
description: "Headless SDK guide: build a custom integrations screen with @fastn-ai/embed/headless. Tokens, connect, setups, settings, events and errors."
---

# Build your own integrations UI

{% hint style="info" %}
What this guide is. The headless SDK gives your frontend the Fastn connector catalog, sign-in to each app (OAuth popups, API key forms, token renewal), each customer's setups and settings, and the same rules the hosted Fastn hub uses. You draw every screen yourself. This guide follows the order you build it in: set up once, add a token endpoint, wrap your screens, connect apps, create setups, edit settings. Sections 8 to 11 are the reference: events, errors, the full API and troubleshooting. Words used here. A customer is one business you serve, named by your own id. A connector is an app Fastn talks to (HubSpot, Slack, Google Drive). A connection is a customer's signed-in account on a connector. A widget is an integration you published in the Widget Builder, such as "Sync HubSpot deals to Slack". A setup (an installation in the API) is one customer's copy of a widget: which connection it uses for each connector, and its settings. Settings (a configuration in the API) are the answers the customer gives in a widget's form.
{% endhint %}

{% hint style="info" %}
This is the **headless** path of `@fastn-ai/embed` — you draw every screen yourself. For the hosted widget (iframe / React components), see [SDK](sdk.md) and [Token API](token-api.md).
{% endhint %}


## 1. Before you start

### 1.1 Your constants

Every fixed value in this guide, in one place.

| Value | Yours | Where it is used |
| --- | --- | --- |
| Base URL | https://api.fastn.dev for a dashboard on app.fastn.dev | Token endpoint (3), FastnProvider (4). The same value on both |
| API key | fsk_..., in FASTN_API_KEY on your backend only | The token endpoint (3). It can act as every one of your customers, so it never goes in frontend code, VITE_* or NEXT_PUBLIC_* variables, or git |
| Embed token | emb_..., minted per signed-in customer, lasts 8 hours | Every browser call. The SDK renews it for you |
| Allowed origins | Every origin that serves your UI, such as https://app.example.com | The API key (1.2). Without them every browser call fails the CORS check |
| Package | @fastn-ai/embed 0.5.0 or newer | No runtime dependencies. React ^17, ^18 or ^19 is an optional peer, needed only for /headless/react. ESM and CommonJS, TypeScript types for every entry point |

### 1.2 Dashboard steps (once per environment)

> 1. Go to Settings > API keys > Create key. Name it after the service, such as web-backend. Choose the **Embed backend** template (connectors.read, connections.read, customers.create), not End user. Copy the key when it is shown: Fastn stores only a hash.  
> 2. Add your origins to the key. The API keys screen has no Allowed Origins field yet (the one in the Widget Builder is the iframe framing list, a different setting). Set them through the API with an Admin-template API key. The Embed backend key gets 403 here; you can revoke the Admin key afterwards. GET {baseUrl}/v1/api-keys lists your keys with their id. Send the full list: it replaces the origins already on the key.

```http
PUT {baseUrl}/v1/api-keys/{keyId} Authorization: Bearer <Admin-template API key>
{ "allowedOrigins": ["https://app.example.com", "https://staging.example.com"] }
```

A token copies the key's origins when it is minted, and renewals keep that copy. A change applies to tokens minted after it, within about a minute. Sessions already open keep the old list until your token endpoint mints them a new token.

> 3. Publish the connectors and widgets your customers should see in the Widget Builder. Until then every list is empty.

### 1.3 Install

```bash
npm install @fastn-ai/embed
```

Headless is a set of subpaths of the same package. A subpath you never import is never loaded.

| Import | Use for |
| --- | --- |
| @fastn-ai/embed/headless | createFastnClient(): the client for connectors, connections, widgets, setups, settings, workflows and activity |
| @fastn-ai/embed/headless/react | FastnProvider and hooks such as useConnectors, useConnect and useWidgets, with one shared cache |
| @fastn-ai/embed/headless/domain | The hosted hub's rules as pure functions: connected state, setup status, form-field visibility |
| @fastn-ai/embed/headless/pickers | Google Drive, Dropbox and OneDrive file pickers (browser only) |
| @fastn-ai/embed/server | The token endpoint: createFastnTokenRoute, mintEmbedToken, ensureTenant |

### 1.4 Check the setup

```bash
# server environment
FASTN_API_KEY=fsk_live_...
FASTN_BASE_URL=https://api.fastn.dev

# from any folder, no install needed
npx @fastn-ai/embed doctor --customer-id cust_123
```

> * doctor checks the deployment, the key, the customer and token minting, in the order they usually fail. It prints no secrets.  
> * Always use the scoped name @fastn-ai/embed. The unscoped name fastn-embed is not a Fastn package on npm.  
> * The customer must already exist. doctor does not register customers, so mint one token for it first (section 3) or it reports tenant not found.  
> * doctor does not check allowed origins. A CORS error in the browser means 1.2 step 2.

## 2. How it works

> * Your backend holds the API key and exchanges it for a short-lived embed token for the signed-in customer (section 3).  
> * The browser calls Fastn directly with that token. Your backend is not in the path of any other call.  
> * The client renews the token at 80% of its life. If renewal fails, it calls your getToken again and the user keeps their place.  
> * Read the customer from your backend session, never from the request body: whoever controls the customer id gets that customer's data.  
> * Connected state, setup status and form-field visibility come from /headless/domain. The hosted hub uses the same functions, so your screens agree with it.

## 3. Token endpoint

### 3.1 Request/Response runtimes (Next.js, Hono, Workers, Deno)

```ts
// app/api/fastn-token/route.ts
import { createFastnTokenRoute } from "@fastn-ai/embed/server";
import { getSession } from "@/lib/auth"; // your session lookup

export const POST = createFastnTokenRoute({
  customer: async (request) => {
    const session = await getSession(request);
    return {
      id: session.orgId,      // your id for this customer
      name: session.orgName,  // registers the customer on first use
      userId: session.userId, // stamped on connections this user creates
    };
  },
});
```

| Answer | When |
| --- | --- |
| 200 { token, baseUrl, expiresIn } | Token minted |
| 401 | Your customer function threw (no session) |
| 403 | Your customer function returned no id |
| 502 "Integrations are unavailable" | Fastn refused the mint. The server log has the FastnServerError |

### 3.2 Express and similar servers

```ts
import { mintEmbedToken } from "@fastn-ai/embed/server";

// requireLogin is your auth middleware
app.post("/api/fastn-token", requireLogin, async (req, res) => {
  const { token } = await mintEmbedToken({
    customerId: req.user.orgId,
    customerName: req.user.orgName,
    userId: req.user.id,
  });
  res.json({ token });
});
```

mintEmbedToken answers { token, baseUrl, endOrgId, expiresIn, expiresAt }.

| Field | Meaning |
| --- | --- |
| id / customerId | Your id for the customer. Required |
| name / customerName | The customer's name. With it, Fastn registers a new customer on first use under that id. Without it, an unknown id fails with 404 Tenant not found |
| userId | Your id for the person signed in. Stamped on the connections they create |
| apiKey, baseUrl | Optional. Default: FASTN_API_KEY and FASTN_BASE_URL. baseUrl falls back to https://api.fastn.dev when neither is set |

> * Both helpers use only fetch, and throw FastnServerError with status, code and a hint that names the fix.  
> * Node 18 or newer is supported and tested. Other runtimes with fetch, Request and Response (Vercel, Cloudflare Workers, Deno, Supabase Edge) should work but are not tested.  
> * Environment variables are read from process.env only. On runtimes without it, such as Workers without nodejs_compat, pass apiKey and baseUrl in code.

### 3.3 Calling the API directly

```http
POST {baseUrl}/v1/embed/token
Authorization: Bearer <FASTN_API_KEY>
{ "endOrgId": "cust_123", "userId": "user_42" }

{ "data": { "token": "emb_...", "endOrgId": "cust_123", "expiresIn": 28800 } }
```

The token is under data.token, not token. expiresIn is in seconds (8 hours).

## 4. Provider

```tsx
import { FastnProvider } from "@fastn-ai/embed/headless/react";

async function getToken(): Promise<string> {
  const res = await fetch("/api/fastn-token", { method: "POST" });
  if (!res.ok) throw new Error(`token endpoint returned ${res.status}`);
  const { token } = await res.json();
  return token;
}

export function IntegrationsPage() {
  return (
    <FastnProvider baseUrl="https://api.fastn.dev" getToken={getToken}>
      <YourIntegrationsScreen />
    </FastnProvider>
  );
}
```

> * FastnProvider renders its children and nothing else.  
> * getToken runs on mount and whenever the client cannot renew. Point it at an endpoint that answers JSON for any signed-in user, not one behind a login redirect.  
> * Every data hook answers { data, error, isLoading, isFetching, refetch }. isLoading is the first load; isFetching includes background refreshes.  
> * Hooks share one cache. A value stays fresh for 30 seconds; { staleTimeMs } changes that, and { enabled: false } holds a hook until its input is ready.  
> * useFastnClient() returns the client. After a change made through the client directly, useFastnCache().invalidate("connections") refetches.  
> * To build the client yourself, call createFastnClient() and pass it as <FastnProvider client={client}>.

| Client option | Meaning |
| --- | --- |
| baseUrl | Required. There is no default deployment in the browser client |
| getToken | Your function that fetches a fresh embed token |
| timeoutMs | How long one call may take. Default 30 seconds |
| maxRetries | Retries on gateway and network errors. Default 2 |
| autoRefresh | Renews the token at 80% of its life. Default on. Turn it off in short-lived server processes |
| persistSession, sessionKey | Keeps the token in sessionStorage across reloads. Default on in a browser tab |
| onSessionExpired, headers, debug | A callback for the terminal state (8.1), extra headers on every call, request logging |

## 5. Connect and disconnect

```tsx
import { useConnectors, useConnections, useConnect } from "@fastn-ai/embed/headless/react";
import { resolveSetupConnection, getLogoUrl } from "@fastn-ai/embed/headless/domain";

function Apps() {
  const { data: connectors = [], isLoading } = useConnectors();
  const { data: connections = [] } = useConnections();
  const { connect, disconnect, connectingId, error } = useConnect();
  if (isLoading) return <YourSpinner />;

  return connectors.map((app) => {
    // the hub's rule: the live connection it would use, if any
    const live = resolveSetupConnection(
      connections.filter((c) => c.connectorId === app.id),
    );
    return (
      <YourAppRow key={app.id} name={app.name}
        logo={getLogoUrl(app.icon, app.domain)} connected={!!live}>
        {live ? (
          <YourButton onClick={() => disconnect(live.id)}>Disconnect</YourButton>
        ) : (
          <YourButton disabled={connectingId === app.id}
            onClick={() => connect(app.id)}>Connect</YourButton>
        )}
      </YourAppRow>
    );
  });
}
```

| useConnect returns | Meaning |
| --- | --- |
| connect(connectorId, options) | Starts the connect. Never throws: on failure it resolves to undefined and sets error |
| disconnect(connectionId) | Removes the connection. Throws on failure |
| connectingId, isConnecting | The connector being connected, for spinners and disabled buttons |
| error | The last connect failure, a FastnConnectError or FastnApiError (9.2) |

> * OAuth connectors open a popup. Browsers block a popup opened after an await or a confirmation dialog, so call connect() directly from the click handler.  
> * When your click handler must await first, call openConnectPopup() at the start of the click and pass the window: connect(app.id, { popup }).  
> * connect and disconnect refresh the connections and setups the hooks hold, so lists update on their own.

### 5.1 API key and basic-auth connectors

```ts
import { getCredentialFields, isOAuthType } from "@fastn-ai/embed/headless/domain";

const method = app.authMethods?.find((m) => m.isDefault) ?? app.authMethods?.[0];
if (!method || isOAuthType(method.type)) {
  connect(app.id); // OAuth: straight from the click
} else {
  const fields = getCredentialFields(method);
  // render fields in your form, then on submit:
  await connect(app.id, { credentials: values });
}
```

getCredentialFields turns an auth method into fields: key, label, type, required, placeholder, enumValues. Use isOAuthType to choose the path: an empty field list also comes back for connectors with no auth.

| connect option | Use for |
| --- | --- |
| authMethodId | An auth method other than the connector's default |
| authProviderId | A specific OAuth app (client) |
| widgetId | Tying the connect to one widget, so its per-widget settings apply |
| scopes | Specific scopes, when the connector exposes selectable scopes |
| credentials | API key, basic or custom credentials for non-OAuth methods |
| connectionId | Reconnecting an existing connection instead of creating one |
| userId | Stamping your end-user id on the connection |
| popup | A window you opened with openConnectPopup() in the click handler |

## 6. Widgets and setups

Pin the connections the customer already has when you create a setup, so it works at once. resolveSetupConnection returns the right one per connector.

```ts
import { useWidgets, useInstallations, useFastnClient } from "@fastn-ai/embed/headless/react";

const { data: widgets = [] } = useWidgets();
const { data: installations = [] } = useInstallations();
const client = useFastnClient();

// activate: create this customer's setup of a widget
await client.installations.create({
  targetType: "widget",
  targetId: widget.id,
  widgetId: widget.id,
  label: `${widget.name} setup`,
  connections: { hubspot: hubspotConnectionId }, // connector slug -> connection id
  status: "active",
});
```

describeSetupStatus is the hub's status rule: it takes counts and answers the label and flags to render.

```ts
import { describeSetupStatus } from "@fastn-ai/embed/headless/domain";

const mine = installations.filter((i) => i.widgetId === widget.id);
const status = describeSetupStatus({
  installationCount: mine.length,
  hasActiveInstallation: mine.some((i) => i.status === "active"),
  connectedCount,           // connectors with a live connection
  totalCount: deps.length,  // connectors the widget needs
});
// status.label, status.isFullyConnected, status.allDepsConnected, ...
```

| Call | Effect |
| --- | --- |
| installations.update(id, { status }) | Pause or resume. Status is one of draft, ready, active, paused, error, archived |
| installations.update(id, { connections }) | Pin a connector to a different connection |
| installations.delete(id) | Remove the setup |
| installations.triggers.list(id) | The setup's triggers (templates and live instances). Also create, update, delete, setStatus |
| installations.setTriggerCategories(id, slugs) | Choose which sync groups run. Removing one deletes its triggers |
| useWidgetInsights() | Runs, records synced and failures over a time window |

## 7. Settings forms

A widget's settings are a template shared by every customer. Each customer's answers are saved on their own copy.

> * Read with client.installations.resolvedConfig(installationId). Use mergedConfig, the template plus this customer's answers: the raw config misses template defaults on a setup nobody has edited.  
> * Fork before the first save. A setup with no configId still points at the shared template. client.configs.create({ forkFromWidgetId, installationId }) forks and pins in one call.  
> * Save with client.configs.update(configId, values).

```ts
const resolved = await client.installations.resolvedConfig(installation.id);
let configId = installation.configId ?? resolved.configId;

if (!configId) {
  const forked = await client.configs.create({
    forkFromWidgetId: widget.id,
    installationId: installation.id,
  });
  configId = forked.id;
}

// render resolved.mergedConfig in your form, then:
await client.configs.update(configId, values);
```

### 7.1 Settings with several rows

useConfigEntriesWithMeta(configId) answers the rows and multiConfig. Show a rows editor only when multiConfig is true. Save rows one at a time: each call is a compare-and-swap on the server. Every row needs a connectorId.

client.configs.entries.create(configId, { values: {}, connectorId });
client.configs.entries.update(configId, entryId, { values });
client.configs.entries.delete(configId, entryId);

### 7.2 Dropdowns filled from the customer's app

A field can take its options from the customer's connected app, such as their Slack channels. Fastn runs the lookup server-side with the customer's connection. isFieldVisible(field, values) shows a field only when the hub would.

```ts
const field = useConfigFieldOptions(configId, "slackChannel", {
  data: values, // current form values, so dependent fields can filter
});
// field.options: [{ label, value }]
// field.search(text), field.loadMore(), field.hasNextPage, field.isLoading
```

Widgets built on the Fastn unified API use useUnifiedConfigOptions and client.installations.saveUnifiedValues instead.

### 7.3 File pickers

```ts
import { openPickerForConnection } from "@fastn-ai/embed/headless/pickers";

const files = await openPickerForConnection({
  client,
  selector: "GOOGLE_FILES_PICKER", // or DROPBOX_FILES_PICKER, ONEDRIVE_FILES_PICKER
  connectionId,
  multi: true,
});
// [{ value, label, metadata }]
```

The provider's own picker opens, and the SDK fetches the credential it needs.

## 8. Events

| Event | When | Payload |
| --- | --- | --- |
| connected | A connection was created, by OAuth or credentials | { connectionId, connectorId? } |
| disconnected | A connection was removed | { connectionId } |
| activated | installations.create made a setup. Resuming with update does not fire it | { installationId, widgetId? } |
| deactivated | installations.delete removed a setup. Pausing does not fire it | { installationId } |
| config-saved | configs.update or an entries call saved settings. The fork does not fire it | { configId } |
| token-refreshed | The token rotated. The new one is already in use | { token } |
| session-expired | Renewal and getToken both failed | none |

```ts
import { useFastnEvents } from "@fastn-ai/embed/headless/react";

useFastnEvents((event, payload) => {
  if (event === "connected") toast("Connected");
  if (event === "session-expired") showSignInAgain();
});

// without React
const off = fastn.on("connected", ({ connectorId }) => refresh(connectorId));
off(); // unsubscribe
```

### 8.1 Token lifecycle

> * Tokens renew before they expire, and a routine 401 is recovered silently.  
> * If renewal fails, the client calls getToken and the user keeps their place. A fixed token cannot recover this way, so pass getToken.  
> * session-expired (FastnSessionExpiredError) is the only terminal state. Retrying cannot recover it, so show a sign-in prompt, not a Retry button.

## 9. Errors

### 9.1 Error classes

Browser-side errors extend FastnError and are exported from @fastn-ai/embed/headless. FastnServerError comes from /server and extends Error.

| Error | Meaning | Fields |
| --- | --- | --- |
| FastnApiError | Fastn answered with an error status | status, code, requestId, method, path, body, retryable |
| FastnAuthError | Authentication was rejected (a kind of FastnApiError) | Same as FastnApiError |
| FastnSessionExpiredError | The session cannot be renewed: the user signs in again | none |
| FastnNetworkError | The request got no response | cause |
| FastnTimeoutError | The request passed timeoutMs, or your AbortSignal aborted it | timeoutMs |
| FastnConnectError | connect did not finish | reason: popup_blocked, cancelled, failed, no_browser |
| FastnServerError (/server) | Minting a token failed | status, code, hint |

Include requestId when you report a FastnApiError to Fastn support: it names the exact request.

### 9.2 Connect errors

With React, read error from useConnect. With the plain client, catch it.

```ts
import { FastnConnectError } from "@fastn-ai/embed/headless";

function connectMessage(err: unknown): string | null {
  if (err instanceof FastnConnectError && err.reason === "popup_blocked")
    return "Allow pop-ups for this site, then try again.";
  if (err instanceof FastnConnectError && err.reason === "cancelled")
    return null; // the user closed the popup
  return err ? "Could not connect. Please try again." : null;
}

// React
const { connect, error } = useConnect();
const message = connectMessage(error);

// plain client
try { await fastn.connect(app.id); } catch (err) { show(connectMessage(err)); }
```

## 10. Without React

The client works on its own in Vue, Svelte, Angular or plain JavaScript. require("@fastn-ai/embed/headless") works as well as import.

```ts
import { createFastnClient } from "@fastn-ai/embed/headless";

const fastn = createFastnClient({ baseUrl: "https://api.fastn.dev", getToken });

const apps = await fastn.connectors.list();
const connection = await fastn.connect(apps[0].id); // OAuth popup if needed
fastn.on("connected", () => refresh());
fastn.on("session-expired", () => showSignInAgain());
```

On your backend, mint an embed token for the customer (3.2) and pass it as token, with autoRefresh: false in short-lived processes. Every call then runs for that customer only.

## 11. Reference

### 11.1 Client

| Area | Calls |
| --- | --- |
| connect | connect(connectorId, options), disconnect(connectionId), openConnectPopup() |
| connectors | list, get, activate, health, activity |
| connections | list, get, create, update, delete, accessToken |
| authProviders | list, create, method |
| widgets | list, get, insights, unifiedConfigOptions |
| installations | list, create, update, delete, resolvedConfig, saveUnifiedValues, setTriggerCategories, triggers.list, triggers.create, triggers.update, triggers.delete, triggers.setStatus |
| configs | list, get, create, update, delete(id, { force }), fieldOptions, enrichOptions, actionSchema, workflows, entries.list, entries.listWithMeta, entries.create, entries.update, entries.delete |
| workflows | list, get, execute, executions, recentExecutions, summary, cancel |
| activity, alerts, ai | Events, sync jobs and traces; alert rules and channels; the hub assistant |
| session, hub | session.get() (who the token is for), hub.settings() (branding from the Widget Builder) |
| Lifecycle | on, once, off, setToken, onTokenChange, dispose |

Every call takes { signal } for cancelling.

### 11.2 React hooks

| Purpose | Hooks |
| --- | --- |
| Setup | FastnProvider, useFastnClient, useFastnContext, useFastnCache, useFastnEvents, useFastnSession, useHubSettings |
| Apps | useConnectors, useConnections, useConnect |
| Widgets and setups | useWidgets, useWidget, useInstallations, useInstallationTriggers, useWidgetInsights |
| Settings | useResolvedConfig, useConfig, useConfigEntries, useConfigEntriesWithMeta, useConfigEntry, useConfigFieldOptions, useUnifiedConfigOptions |
| Runs and activity | useWorkflows, useWorkflowExecutions, useEvents, useSyncJobs |
| Assistant | useFastnChat, useAIUsage |
| Anything else | useFastnQuery(key, fetcher) caches your own call in the same store |

### 11.3 Domain rules

| Purpose | Functions |
| --- | --- |
| Connection state | resolveSetupConnection, connectionIsLive, connectionNeedsReauth, describeSetupStatus |
| Catalog display | getLogoUrl, buildHubDisplayItems, groupHubDisplayItems, formatHubCategoryLabel, collapseWidgetVersions, visibleLogoConnectors |
| Credential forms | getCredentialFields, buildCredentialPayload, getHiddenFieldDefaults, isOAuthType, signsInWithOAuth, resolveAuthProvider |
| Settings fields | isFieldVisible, evaluateVisibleWhen, resolveEnrichParams, hasDepsResolved |
| Verification badges | effectiveConnectionStatus, verifyLabel, verifyNeedsAttention, connectedLabel |

### 11.4 Troubleshooting

Run npx @fastn-ai/embed doctor --customer-id <id> first (1.4).

| Symptom | Cause and fix |
| --- | --- |
| CORS error on every browser call | The page origin is not in the key's allowed origins. Add the exact origin (1.2 step 2). A change takes up to a minute |
| Token endpoint returns 403 Permission denied by API key | The key uses the End user template (the SDK hint may call it "Customer-in-widget"). Create a key from the Embed backend template |
| 404 Tenant not found when minting | The customer does not exist yet. Pass customerName (name in createFastnTokenRoute) to register it on first use |
| 401 Invalid API key | The key belongs to another Fastn deployment or was revoked. Check the API keys page for that base URL |
| "Could not get a token" although the endpoint returned 200 | The raw API nests the token under data.token. Use mintEmbedToken or read data.token |
| The OAuth popup never opens | connect() ran after an await or a confirmation. Call it in the click handler, or pass a popup from openConnectPopup() |
| A blocked popup shows no message | useConnect's connect does not throw. Read error from useConnect (9.2) |
| Lists load but are empty | Nothing is published for customers. Enable connectors and publish widgets in the Widget Builder |
| Error about a missing baseUrl | The browser client has no default deployment. Pass baseUrl to FastnProvider or createFastnClient |
| Users are sent to sign in unexpectedly | getToken hits an endpoint behind a login redirect. Make it answer JSON for any signed-in user |

### 11.5 Go-live checklist

> * The API key is from the Embed backend template and lives only in server environment variables.  
> * Every production origin is in the key's allowed origins.  
> * The token endpoint reads the customer from your session, not the request, and answers without a login redirect.  
> * baseUrl is the same on the server and in the SDK.  
> * npx @fastn-ai/embed doctor passes for a real customer id.  
> * The connectors and widgets customers should see are published in the Widget Builder.  
> * connect() runs from click handlers, and popup_blocked shows a message.  
> * Settings edits fork the template before saving.  
> * session-expired shows a sign-in prompt.  
> * Status labels, connected state and form-field visibility come from /headless/domain.
