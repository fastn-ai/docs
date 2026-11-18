---
description: "Zoho Assist is Zoho's remote support and unattended remote access platform."
hidden: true
---

# Zoho Assist

<img src="../../.gitbook/assets/connectors/lg/zoho-assist.png" alt="Zoho Assist logo">

Zoho Assist is Zoho's remote support and unattended remote access platform. This connector wraps the Zoho Assist REST API v2 (https://assist.zoho.com/api/v2): create and schedule remote support and screen sharing sessions, resolve session identifiers, fetch session reports, export session notes and retrieve download links for session recordings, screenshots and chat transcripts, manage unattended devices and device groups, and start unattended remote sessions. Every request requires the Zoho Assist organization ID header.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [assist.zoho.com](https://assist.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zohoAssist` |

## Use it

Add Zoho Assist from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoAssist.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Session | `createSession` | Creates a new on-demand Zoho Assist remote support or screen sharing session. Returns a customer URL to share with the end user and a technician URL the agent opens to start the session, along with the session ID and authentication key. Supplying a customer email sends the join invitation directly to that address. |
| Create Unattended Group | `createUnattendedGroup` | Creates a new unattended computer group in a Zoho Assist department, optionally seeding it with a list of devices. Returns the created group's ID, name, description and creation details. |
| Create Unattended Session | `createUnattendedSession` | Starts an unattended remote session with a specific Zoho Assist device, which connects without anyone present at the far end. Returns a technician URI to open in a browser, the session key and authentication details, and whether a user is currently present on the device. |
| Export Session Notes | `exportSessionNotes` | Exports the technician notes recorded during a Zoho Assist session. The note text is returned directly in the response body. Resolve the required system ID from a customer-facing session ID using the Get Session Details action. |
| Get Session Chat Download Link | `getSessionChatDownloadLink` | Returns a download link for the chat transcript of a Zoho Assist session. The link must be opened in a browser by a user signed in to the same Zoho account. Resolve the required system ID from a customer-facing session ID using the Get Session Details action. |
| Get Session Details | `getSessionDetails` | Resolves a customer-facing Zoho Assist session ID to its internal system ID. The session ID is the 9-10 digit number shown to the customer, while the system ID is required by the session notes and file download link actions. |
| Get Session Recording Download Link | `getSessionRecordingDownloadLink` | Returns a download link for the recording files of a Zoho Assist session. The link must be opened in a browser by a user signed in to the same Zoho account. Resolve the required system ID from a customer-facing session ID using the Get Session Details action. |
| Get Session Screenshot Download Link | `getSessionScreenshotDownloadLink` | Returns a download link for the screenshot files captured during a Zoho Assist session. The link must be opened in a browser by a user signed in to the same Zoho account. Resolve the required system ID from a customer-facing session ID using the Get Session Details action. |
| Get Unattended Device | `getUnattendedDevice` | Fetches the full detail of a single unattended Zoho Assist device, including its hardware and platform information, domain and network details, group memberships, department, stored credentials, logged-on users and when it was last accessed and by whom. |
| Get User Details | `getUserDetails` | Fetches the details of the currently authenticated Zoho Assist user, including their role, organization details, license information, department memberships and preferred department ID. Call this first to obtain the department IDs required by the unattended device and group actions. |

<details>

<summary>See 6 more actions</summary>

* **List Session Reports** `listSessionReports`: Fetches reports of previously conducted Zoho Assist sessions within a date range, optionally filtered to a single technician. Each report carries the session ID, session type, technician and customer details, start and end times, and the session duration in milliseconds.
* **List Unattended Devices** `listUnattendedDevices`: Lists the unattended devices enrolled in a Zoho Assist department, with extensive filtering by group, status, operating system, network address, domain and hardware attributes. Returns each device's display name, status, IP addresses, agent version and resource ID. The total device count is included only when the page index is 1.
* **List Unattended Groups** `listUnattendedGroups`: Lists the unattended computer groups defined in a Zoho Assist department, returning each group's ID, name, description, device count, creator and whether it is the preferred group. Supply a search query to filter groups by name.
* **Schedule Session** `scheduleSession`: Schedules a Zoho Assist remote support session for a future time and invites the customer by email. Returns the schedule ID along with the technician and customer join URLs. Retrieve the department ID from the Get User Details action before calling this.
* **Update Unattended Device Display Name** `updateUnattendedDeviceDisplayName`: Renames an unattended Zoho Assist device by setting a new display name. Only the display name can be changed through this endpoint; the underlying device name reported by the agent is unaffected.
* **Update Unattended Group** `updateUnattendedGroup`: Updates an existing unattended computer group in Zoho Assist. Renames the group, changes its description, and adds or removes devices from it in a single call.

</details>
