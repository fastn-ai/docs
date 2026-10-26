---
description: >-
  Fixes for the common Fastn Connect problems: a client that will not connect,
  missing tools, connect links, refused calls, and plan limits.
---

# Troubleshooting

### My client will not connect

* **Check the host.** The URL must start with `https://mcp.fastn.dev`, not `connect.fastn.dev`. Copy it from Home. See [Gateway URLs](reference/gateway-urls.md).
* **Check the workspace.** *This connect link is for the "{slug}" workspace, which you're not a member of* means you need an invite to that workspace. Ask an admin, or use your organisation's URL.
* **Signed in as the wrong person?** On the consent screen, click **Not you?** to sign out and resume the same request. *Wrong account* pages offer **Sign in with a different account**.
* ***This request expired.*** Authorisation requests are short-lived. Start the connection again from your client.
* **The client fails on a large workspace.** Some clients reject a connection carrying hundreds of tool schemas. Pick fewer tools on the consent screen, or ask an admin to switch **Optimization** to **Smart**. See [Choosing tools](tools/choosing-tools.md#how-many-tools-load-into-the-prompt).
* **Claude Team or Enterprise.** Only an organisation owner can add a custom connector. See [Claude](clients/claude.md).

### A tool I expect is missing

1. Is the app connected and **on**? Check its row on [Tools](tools/README.md). A connector that is off is not exposed.
2. Is the tool turned on? Open the row and check **Choose tools**.
3. Did you pick it when you connected the client? Reconnect the client and pick again.
4. Is a policy hiding it? Check the **Can reach** column for you on [Access](access/README.md).
5. For per-user apps that you have not connected, tools may only be listed *after you connect*.

### A tool replies "Authorization required"

The app signs in per person and you have not connected your account yet. Open the link in the reply, sign in to the app, then ask again. If it says *Authorization failed... were rejected*, your stored account expired or was revoked: use the **Reconnect** link. See [the connect link](tools/sign-in-modes.md#each-person-signs-in-the-connect-link).

If the reply says the app is set to require an admin to connect it, the app's **Offer a connect link when not connected** switch is off (in **Choose tools**). Ask an admin to connect the account for you, or to turn the connect link back on.

### A call was refused

Open [Monitor](monitor.md) and find the call under **Recent calls**:

| Tag | Cause | Fix |
| --- | --- | --- |
| **policy** | A policy on the person or key blocked it (read-only, denied tool, or blocked data on write). | Change the policy on [Access](access/policies.md), or use a different key. |
| **auth** | The caller has not connected their account for this app. | Connect it (see above). |
| **connector** | The app itself returned an error. | Check the app account's permissions, or **Test** the tool on Tools. |
| **gateway** | Fastn Connect could not complete the call. | Retry; if it persists, contact fastn support with the time of the call. |

### Calls stop with 429 or 402

* `429` means a rate, concurrency or daily or weekly limit. The response says how many seconds to wait in `Retry-After`.
* `402` means the organisation's monthly quota is used up. Calls resume when the month resets (UTC) or after an upgrade.

Check usage on Monitor or **Settings** → **Plan and billing**. See [Plans and limits](plans-and-limits.md).

### Saving a policy says "Could not save."

On the Free plan, you can have one policy. Remove the existing one or upgrade. See [Plans and limits](plans-and-limits.md).

### A connector shows Failing or Needs a refresh

Open its row on Tools. If it says *Couldn't refresh tools* or *Last sync failed*, click **Retry**. If the account expired, reconnect it. Home lists every failing connector under **Needs your attention**.

### I lost an access key

Keys are shown once and stored only as a hash, so they cannot be recovered. On [Agents](agents/README.md), revoke the old key and create a new one.
