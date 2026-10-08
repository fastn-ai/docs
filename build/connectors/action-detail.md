---
description: "A connector's actions: the action list, the action editor and its seven tabs, mocks, versions and proposing an update."
---

# Actions

An **action** is one operation a connector can perform, such as *Create Contact* or *List Owners*. Under the hood it is one HTTP request (method, URL, headers, body) plus two schemas: the input it accepts and the output it returns. Workflows, the Agent and the MCP gateway call actions; they never call the vendor's API directly.

### The action list

On the [connector detail page](inside-a-connector.md), the connector rail lists every action of the open connector with its method chip (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).

* Click an action to open it in the editor. The URL becomes `/integrations/connectors/<connector-slug>/<action-slug>`.
* Hover an action and click **⋯** for its menu. On a managed connector it holds **Export**.
* Tick actions (or **Select all**) to act on several at once. The rail then shows *n selected* and an **Export** button.

<figure><img src="../../.gitbook/assets/connector-actions-selected.webp" alt="The connector rail with two actions ticked, Add List Members and Archive Call, and a bar at the top reading 2 selected with an Export link"><figcaption>Selecting actions shows the bulk <strong>Export</strong>.</figcaption></figure>

<figure><img src="../../.gitbook/assets/action-row-menu.webp" alt="The Add List Members row with its three-dot menu open, showing one item, Export"><figcaption>The menu on a single action.</figcaption></figure>

On a connector your workspace owns, the rail also offers **Add action**, and each action can be edited and deleted.

### The action editor

<figure><img src="../../.gitbook/assets/action-editor-params.webp" alt="The action editor for HubSpot Add List Members: name and description fields at the top, a PUT method selector, the URL https://api.hubapi.com/crm/v3/lists/{{input.listId}}/memberships/add and a Run button, the tabs Params, Headers, Auth, Body, Input schema, Output schema and Mocks with Params open showing No query parameters, and a footer with v1.2, New version, Read-only owned by platform, and Propose an update"><figcaption>The editor for one action. <code>{{input.listId}}</code> in the URL is filled in from the action's input when it runs.</figcaption></figure>

The top of the editor holds:

| Element | Meaning |
| --- | --- |
| **Name** | The action's display name. |
| **Description** | What the action does and how to call it. The Agent reads this, so it should say which inputs matter. |
| **Method** | `GET`, `POST`, `PUT`, `PATCH` or `DELETE`. |
| **URL** | The endpoint. Parts in double braces are filled in when the action runs: `{{input.<field>}}` takes a value from the action's input. |
| **Run** | Runs the action using your own connection to this connector, so you can check the request before a workflow uses it. |

#### Placeholders

Anywhere in the URL, headers, query parameters or body, values in double braces are filled in at run time:

* `{{input.<field>}}`: a field from the action's input, as defined in **Input schema**.
* `{{auth.token}}`: the credential from the connection, for example in an `Authorization: Bearer {{auth.token}}` header.

#### The seven tabs

| Tab | What you set there |
| --- | --- |
| **Params** | Query parameters (**Query Parameters**, **+ Add**). Each one is a key and a value; the value can be a placeholder. |
| **Headers** | Request headers (**Request Headers**, **+ Add**), as **KEY** / **VALUE** pairs. |
| **Auth** | How this request is authorised. **Auth type**: `No Auth`, `Basic Auth`, `Bearer Token`, `JWT Bearer`, `AWS Signature`, `OAuth 1.0`, `OAuth 2.0` or `API Key`. `No auth` (*This request does not use any authorization.*) is the usual choice when the credential is already sent in a header, as in the HubSpot example below. |
| **Body** | **Body type**: `JSON`, `Form Data`, `Raw`, `GraphQL` or `Form URL Encoded`, and the body itself. |
| **Input schema** | The inputs the action accepts. See below. |
| **Output schema** | The shape of the response the action returns. Same editor as the input schema. |
| **Mocks** | Canned responses used in mock mode. See below. |

<figure><img src="../../.gitbook/assets/action-editor-headers.webp" alt="The Headers tab with two rows: Content-Type application/json and Authorization Bearer {{auth.token}}"><figcaption>The connection's token goes into the <code>Authorization</code> header through <code>{{auth.token}}</code>.</figcaption></figure>

<figure><img src="../../.gitbook/assets/action-editor-auth.webp" alt="The Auth tab with Auth type set to No Auth and the text No auth, This request does not use any authorization"><figcaption>The Auth tab. Here the credential is sent in a header instead.</figcaption></figure>

<figure><img src="../../.gitbook/assets/action-editor-body.webp" alt="The Body tab for HubSpot Create Contact: Body type JSON on the left and a body editor labelled body JSON on the right"><figcaption>The Body tab with <strong>JSON</strong> selected.</figcaption></figure>

#### Input schema and output schema

> Define the expected input parameters for this action.

<figure><img src="../../.gitbook/assets/action-editor-input-schema.webp" alt="The Input schema tab for Create Contact in Form view: 1 field, properties, of type object, with nested fields email, phone, company, website, jobtitle, lastname, firstname, hs_lead_status and lifecyclestage, each with a key, a label, a description, a type selector, a Required/Optional toggle, a more-options button, a plus button and a delete cross"><figcaption>An object field (<code>properties</code>) with nested string fields.</figcaption></figure>

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

<figure><img src="../../.gitbook/assets/action-editor-field-options.webp" alt="The Input schema tab with the more-options menu of the phone field open, showing Enum values"><figcaption><strong>More options</strong> on a field.</figcaption></figure>

The **Output schema** tab (*Define the expected output structure for this action.*) uses the same editor. Workflows and the Agent read it to know which fields a response contains.

<figure><img src="../../.gitbook/assets/action-editor-output-schema.webp" alt="The Output schema tab for Create Contact: 5 fields, id string, archived boolean, createdAt string, updatedAt string and properties object"><figcaption>The fields Create Contact returns.</figcaption></figure>

#### Mocks

> Test cases returned when running in mock mode. LLM-generated and live-captured stubs are auto-updated when you regenerate.

<figure><img src="../../.gitbook/assets/action-editor-mocks.webp" alt="The Mocks tab, headed Mock Scenarios, with + Add custom and Generate with AI buttons and two CUSTOM scenarios: rate-limited-chunk, described as a chunk returning 429 while others succeed, and added-ok, Default success: HubSpot accepted the batch"><figcaption>Two custom mock scenarios on Add List Members.</figcaption></figure>

A mock is a stored response for this action. When a workflow runs in mock mode, the action returns the mock instead of calling the vendor, so you can test a workflow without touching real data.

* **+ Add custom** adds a scenario you write yourself.
* **Generate with AI** has the AI write scenarios for the action. Generated scenarios are replaced when you generate again.
* Each scenario shows its source (`CUSTOM` for hand-written ones), its name and a description. The bin icon deletes it.

### Versions

The footer shows the action's version, for example `v1.2`. **New version** opens a small form:

<figure><img src="../../.gitbook/assets/action-new-version.webp" alt="The New version form above the editor footer: a Fork selector set to Next internal major (breaking), checkboxes Deprecate this version and Make default, and Create and Cancel buttons"><figcaption>Creating a new version of an action.</figcaption></figure>

| Field | Meaning |
| --- | --- |
| **Fork** | **Next internal major (breaking)**: a new major version of this action, for a change that would break existing callers. **New external version**: a version tied to a different version of the vendor's API. External versions are what [version pins](inside-a-connector.md#version-pins) work with. |
| **Deprecate this version** | Marks the current version as deprecated. |
| **Make default** | Makes the new version the one used when a caller does not ask for a specific version. |

**Create** makes the version; **Cancel** closes the form.

### Platform-owned actions and Propose an update

Actions on a managed connector belong to fastn. Their footer reads *Read-only — owned by platform*, and you cannot save changes to them. You can still read every tab, run the action, and export it.

If an action is wrong or missing something, click **Propose an update**:

<figure><img src="../../.gitbook/assets/action-propose-update.webp" alt="The Propose an update form at the bottom of the editor: a text box reading Add a note for the reviewer (optional), why this update, what changed, with Cancel and Propose update buttons"><figcaption>A proposal goes to fastn for review.</figcaption></figure>

1. Make your changes in the editor tabs.
2. Click **Propose an update** and add a note for the reviewer: why the update is needed and what changed.
3. Click **Propose update**.

Fastn reviews the proposal. Nothing changes on the connector until it is accepted.
