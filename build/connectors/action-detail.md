---
description: "A connector's actions: the action list, the action editor and its seven tabs, mocks, versions and proposing an update."
---

# Actions

An **action** is one operation a connector can perform, such as *Create Contact* or *List Owners*. Under the hood it is one HTTP request (method, URL, headers, body) plus two schemas: the input it accepts and the output it returns. Workflows, Build with AI and your AI tool (over MCP) call actions; they never call the vendor's API directly.

### The action list

On the [connector detail page](inside-a-connector.md), the connector rail lists every action of the open connector with its method chip (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).

* Click an action to open it in the editor. The URL becomes `/integrations/connectors/<connector-slug>/<action-slug>`.
* Hover an action and click **⋯** for its menu. On a managed connector it holds **Export**.
* On a connector your workspace owns, **+** next to the connector's name adds an action; see [Add an action](editing-and-deleting.md#add-an-action).
* Tick actions (or **Select all**) to act on several at once. The rail then shows *n selected* and an **Export** button.

### The action editor

The top of the editor holds:

| Element | Meaning |
| --- | --- |
| **Name** | The action's display name. |
| **Description** | What the action does and how to call it. Build with AI reads this, so it should say which inputs matter. |
| **Method** | `GET`, `POST`, `PUT`, `PATCH` or `DELETE`. |
| **URL** | The endpoint. Parts in double braces are filled in when the action runs: `{{input.<field>}}` takes a value from the action's input. |
| **Run** | Opens the run panel to call the action once, live or with a mock. See [Running an action](#running-an-action). |

#### Placeholders

Anywhere in the URL, headers, query parameters or body, values in double braces are filled in at run time:

* `{{input.<field>}}`: a field from the action's input, as defined in **Input schema**.
* `{{auth.<field>}}`: a field from the connection's credential, for example in an `Authorization: Bearer {{auth.token}}` header. Which field names are available depends on the connector's auth method.

#### The seven tabs

| Tab | What you set there |
| --- | --- |
| **Params** | Query parameters (**Query Parameters**, **+ Add**). Each one is a key and a value; the value can be a placeholder. |
| **Headers** | Request headers (**Request Headers**, **+ Add**), as **KEY** / **VALUE** pairs. |
| **Auth** | How this request is authorized. **Auth type** shows the auth that actually runs, which is the connector's auth method, for example *OAuth 2.0 (from connector)*, with a note such as *OAuth 2.0, from the connector*. Below it, **Stored action setting** is a dropdown (`Basic Auth`, `Bearer Token`, `JWT Bearer`, `AWS Signature`, `OAuth 1.0`, `OAuth 2.0`, `API Key`, or *None (use connector)*) that is saved with the action but, as its help text says, *Not used at run time. Requests are signed with the connector's auth method.* The *No auth* panel appears only when the connector has no auth method. |
| **Body** | **Body type**: `JSON`, `Form Data`, `Raw`, `GraphQL` or `Form URL Encoded`, and the body itself. |
| **Input schema** | The inputs the action accepts. See below. |
| **Output schema** | The shape of the response the action returns. Same editor as the input schema. |
| **Mocks** | Canned responses used in mock mode. See below. |

#### Input schema and output schema

> Define the expected input parameters for this action.

Switch between **Form** and **JSON**. In Form view each field is one row:

| Part | Meaning |
| --- | --- |
| Key | The field name used in placeholders, for example `email`. |
| Label | A readable name, for example *Email*. |
| Description | What the field is for. |
| Type | `string`, `number`, `boolean`, `object` or `array`. |
| **Required** / **Optional** | Whether the caller must send it. |
| **⋮** (More options) | **Enum values**: limit the field to a fixed list of values. |
| **+** | Adds a nested field (*Convert to object and add nested field* on a non-object field). |
| **✕** | Removes the field. |

**Add** (top right) adds a top-level field. The count (for example *1 field*) shows how many top-level fields there are.

The **Output schema** tab (*Define the expected output structure for this action.*) uses the same editor. Workflows and Build with AI read it to know which fields a response contains.

#### Mocks

> Test cases returned when running in mock mode. LLM-generated and live-captured stubs are auto-updated when you regenerate.

A mock is a stored response for this action. When a workflow runs in mock mode, the action returns the mock instead of calling the vendor, so you can test a workflow without touching real data.

* **+ Add custom** adds a scenario you write yourself.
* **Generate with AI** has the AI write scenarios for the action. Generated scenarios are replaced when you generate again.
* Each scenario shows its source (`CUSTOM` for hand-written ones), its name and a description. The bin icon deletes it.
* With none saved, the tab reads *No mock scenarios yet.*

### Running an action

**Run** opens a panel titled with the method and the action's name.

| Part | Meaning |
| --- | --- |
| **Mock** | Toggle. Off: the call goes to the real app. On: no call is made; a mock response is returned instead. |
| **Connection** | *(Live mode.)* Which of your connections to run as. With no connection it reads *No connections available.* and **Run Action** stays disabled. |
| **Mock scenario (optional)** | *(Mock mode.)* Which saved mock to return. With none saved: *No saved mock scenarios. AI will generate a realistic response.* |
| **Input** | The action's input, in **Form** or **JSON** view. **+** adds a field. |
| **Run Action** / **Run Mock** | Runs it. |

The result appears beside the inputs: the HTTP status, the time taken (`0ms (mock)` for a mock), and **Response** and **Request** tabs with the response body and the request that was sent.

After a successful live run the action is marked **Live tested** (a green check also appears next to it in the rail), and **Last test** in the panel reopens the most recent result.

### Versions

The footer shows the action's version, for example `v1.2`, and **New version**. On an action your workspace owns it also shows **Save Changes**. Hovering the version explains it: *Internal revision - major.minor. A minor bump reaches pinned callers automatically; a major fork does not.*

**New version** opens a small form:

| Field | Meaning |
| --- | --- |
| **Fork** | **Next internal major (breaking)**: a new major version of this action, for a change that would break existing callers. **New external version**: a version tied to a different version of the vendor's API. External versions are what [version pins](inside-a-connector.md#version-pins) work with. |
| **Deprecate this version** | Marks the current version as deprecated. |
| **Make default** | Makes the new version the one used when a caller does not ask for a specific version. |

**Create** makes the version; **Cancel** closes the form.

### Platform-owned actions and Propose an update

Actions on a managed connector belong to fastn. Their footer reads *Read-only - owned by platform*, and you cannot save changes to them. You can still read every tab, run the action, and export it.

If an action is wrong or missing something, click **Propose an update**:

1. Make your changes in the editor tabs.
2. Click **Propose an update** and add a note for the reviewer: why the update is needed and what changed.
3. Click **Propose update**.

fastn reviews the proposal. Nothing changes on the connector until it is accepted.
