---
description: >-
  The words Fastn Connect uses: organisation, workspace, connector, tool,
  sign-in mode, access key, connection, policy, and how they fit together.
---

# Core concepts

**What this page answers**

* What is the difference between an organisation and a workspace?
* What is a connector, and what is a tool?
* Whose account does a tool call run with?
* What is the difference between an access key and a connection?
* What do the roles allow?

### The picture in one paragraph

Your **organisation** owns one or more **workspaces**. Each workspace has its own **connectors** (apps and MCP servers), and each connector contributes **tools**. A client or agent reaches a workspace through its **gateway URL**, proving who it is with a sign-in or an **access key**. When it calls a tool, the connector's **sign-in mode** decides which stored **connection** (whose account) the call runs with, and any **policies** on the caller can restrict or mask what happens. Every call lands in **Monitor** and **Audit**.

### Organisation

Your company. It is created the first time someone signs in with an address on your company domain, and that person becomes its **Owner**. Anyone who later signs in with the same domain joins it automatically. Someone who signs in with a personal address (Gmail, Outlook and so on) gets a personal organisation of their own.

Billing and plan limits are counted for the whole organisation. See [Plans and limits](plans-and-limits.md).

### Workspace

A separate gateway inside your organisation, with its own connectors, keys, people and policies. Your organisation itself is the default workspace. Create more to keep, say, Marketing's tools apart from Engineering's, or to give an agent fleet its own gateway. Workspaces are invite-only: domain auto-join covers the organisation, not its workspaces. See [Workspaces](workspaces.md).

### Connector and tool

A **connector** is one app or server plugged into the gateway: a catalog app such as Slack, an MCP server you add by URL, or a custom connector you build. Each connector exposes **tools**, the individual actions a model can call (for example *send a message* or *list issues*).

Tools are named `<connector>__<tool>`, for example `slack__send_message`, so a call always reaches the right app even when two apps have a tool with the same name.

You choose which of a connector's tools are turned on. See [Choosing tools](tools/choosing-tools.md).

### Sign-in mode: whose account a call runs with

Every connector has a sign-in mode. It decides which credential a tool call uses.

| Mode | What happens |
| --- | --- |
| **One shared account** | An admin connects one account. Every call uses it. |
| **Each person signs in** | Every person connects their own account, and calls run as them. Until they connect, the tool replies with a link to connect. |
| **Each customer org** | One account per customer organisation, for agents that serve many customers. |
| **The caller brings a token** | Nothing is stored. The client sends its own token on every call. |

Full details: [Whose account a call runs with](tools/sign-in-modes.md).

### Access key and connection: in and out

Two kinds of credential travel in opposite directions. Keep them apart and most of the product makes sense.

| | Direction | What it is |
| --- | --- | --- |
| **Access key** (or a sign-in) | *Into* the gateway | How a client or agent proves who it is to Fastn Connect. People sign in through their client. Agents use an access key (`ucl_...`) or an OAuth client. |
| **Connection** | *Out of* the gateway | A stored authorisation to one app (your Slack, the team's shared GitHub). Fastn Connect uses it to call the app on someone's behalf. |

Access keys are managed in [Agents](agents/README.md). Connections are listed in [Connections](connections.md) and in each person's [Profile](settings.md#your-profile).

### Policy

A reusable rule you attach to people and access keys: read-only, allow or deny specific tools, mask or block personal data, health data, card numbers or secrets, and redact named fields. When several policies apply, the most restrictive one wins. Policies can only narrow what the underlying app already allows; they never widen it. See [Policies](access/policies.md).

### Roles

| Role | In the app | Through the gateway |
| --- | --- | --- |
| **Owner** | Everything. Set once, when the organisation is created. Cannot be changed. | Every tool admins turned on. |
| **Admin** | Manage tools, people, policies, keys, Monitor, Audit and Settings. | Every tool admins turned on. |
| **Member** | Sees Home, Tools, Access and Connections. Connects their own accounts. | Tools admins turned on, limited by any policy on them. |
| **Viewer** | Like Member, but cannot change connectors. This is the default for teammates who join by signing in. | Same as Member. |

An admin can promote people on the [Access](access/README.md) page.

### Skill

A named, reusable recipe the model can call like a tool: either a fixed sequence of tool calls, or a written playbook the model follows. Skills are governed exactly like tools. See [Skills](skills.md).
