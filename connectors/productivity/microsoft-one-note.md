---
description: "Microsoft OneNote via Microsoft Graph v1.0."
hidden: true
---

# Microsoft OneNote

<img src="../../.gitbook/assets/connectors/lg/microsoft-one-note.png" alt="Microsoft OneNote logo">

Microsoft OneNote via Microsoft Graph v1.0. Covers the signed-in user's notebooks, section groups, sections and pages, page HTML content read and patch, asynchronous copy operations for notebooks, sections and pages, notebook lookup by web URL, recently opened notebooks, and long-running operation status. All actions target the signed-in user's own OneNote content (the /me root); group-owned and SharePoint site-hosted notebooks are not covered.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [graph.microsoft.com](https://graph.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `microsoftOneNote` |

## Use it

Add Microsoft OneNote from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.microsoftOneNote.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Copy Notebook | `copyNotebook` | Copy a OneNote notebook to the signed-in user's notebooks or to a Microsoft 365 group. The copy runs asynchronously and returns HTTP 202 with the operation in the response body; poll it with Get Operation. The copied notebook can appear before the operation status catches up. |
| Copy Page To Section | `copyPageToSection` | Copy a OneNote page into another section. The copy runs asynchronously and returns HTTP 202 with the operation in the response body; poll it with Get Operation. The copied page can appear before the operation status catches up. |
| Copy Section To Notebook | `copySectionToNotebook` | Copy a OneNote section into another notebook. The copy runs asynchronously and returns HTTP 202 with the operation in the response body; poll it with Get Operation. The copied section can appear before the operation status catches up. |
| Copy Section To Section Group | `copySectionToSectionGroup` | Copy a OneNote section into a section group. The copy runs asynchronously and returns HTTP 202 with the operation in the response body; poll it with Get Operation. The copied section can appear before the operation status catches up. |
| Create Nested Section Group | `createNestedSectionGroup` | Create a new section group nested inside an existing OneNote section group. Names must be unique within the same level and are limited to 50 characters. |
| Create Notebook | `createNotebook` | Create a new OneNote notebook for the signed-in user. Notebook names must be unique, are limited to 128 characters, and cannot contain the characters ? * \ / : \| ' " or angle brackets. |
| Create Notebook Section | `createNotebookSection` | Create a new section inside a OneNote notebook. Section names must be unique within the same level and are limited to 50 characters. |
| Create Notebook Section Group | `createNotebookSectionGroup` | Create a new section group inside a OneNote notebook. Section group names must be unique within the same level and are limited to 50 characters. |
| Create Page | `createPage` | Create a OneNote page in the signed-in user's default section by posting its HTML. The title comes from the title element in the HTML head. Binary images and file attachments require a multipart request and are not supported by this action. |
| Create Section Group Section | `createSectionGroupSection` | Create a new section inside a OneNote section group. Section names must be unique within the same level and are limited to 50 characters. |
| Create Section Page | `createSectionPage` | Create a OneNote page in a specific section by posting its HTML. The title comes from the title element in the HTML head. Binary images and file attachments require a multipart request and are not supported by this action. |
| Delete Page | `deletePage` | Delete a OneNote page belonging to the signed-in user. |
| Get Notebook | `getNotebook` | Retrieve the properties of a single OneNote notebook belonging to the signed-in user. |
| Get Notebook From Web URL | `getNotebookFromWebUrl` | Look up a OneNote notebook by the full URL path to it, for example a link copied from OneNote or SharePoint. The URL may also carry a onenote: prefix. |
| Get Operation | `getOperation` | Check the status of a long-running OneNote operation such as a notebook, section or page copy. Poll this until the status reports completed or failed. Note that the copied resource can appear before the operation status catches up, so a status that still reads 'not started' does not mean the copy has not happened. |
| Get Page | `getPage` | Retrieve the metadata of a single OneNote page, including its title and the content URL. Use Get Page Content to fetch the HTML body. |
| Get Page Content | `getPageContent` | Retrieve the HTML body of a OneNote page. Set Include IDs to true to have OneNote return the generated element identifiers that Update Page Content targets. |
| Get Recent Notebooks | `getRecentNotebooks` | Retrieve the OneNote notebooks the signed-in user has opened most recently, optionally including their personal notebooks. |
| Get Section | `getSection` | Retrieve the properties of a single OneNote section belonging to the signed-in user. |
| Get Section Group | `getSectionGroup` | Retrieve the properties of a single OneNote section group belonging to the signed-in user. |
| List Nested Section Groups | `listNestedSectionGroups` | Retrieve the section groups nested inside another OneNote section group belonging to the signed-in user. |
| List Notebook Section Groups | `listNotebookSectionGroups` | Retrieve the section groups directly inside a OneNote notebook belonging to the signed-in user. |
| List Notebook Sections | `listNotebookSections` | Retrieve the sections directly inside a OneNote notebook belonging to the signed-in user. |
| List Notebooks | `listNotebooks` | Retrieve the OneNote notebooks belonging to the signed-in user, including notebooks shared with them. |
| List Pages | `listPages` | Retrieve every OneNote page the signed-in user has access to, across all of their notebooks and sections. |
| List Section Group Sections | `listSectionGroupSections` | Retrieve the sections inside a OneNote section group belonging to the signed-in user. |
| List Section Groups | `listSectionGroups` | Retrieve every OneNote section group the signed-in user has access to, across all of their notebooks. |
| List Section Pages | `listSectionPages` | Retrieve the pages held in a specific OneNote section belonging to the signed-in user. |
| List Sections | `listSections` | Retrieve every OneNote section the signed-in user has access to, across all of their notebooks. |
| Update Page Content | `updatePageContent` | Change the HTML content of a OneNote page by applying a list of patch commands. Each command names a target element, an action such as append, insert or replace, and the HTML to apply. Use Get Page Content with Include IDs to discover the target identifiers. |
