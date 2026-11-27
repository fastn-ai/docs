---
description: "Microsoft OneNote is a digital notebook app. Create and copy notebooks, sections, section groups and pages."
hidden: true
---

# Microsoft OneNote

<img src="../../.gitbook/assets/connectors/lg/microsoft-one-note.png" alt="Microsoft OneNote logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [graph.microsoft.com](https://graph.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `microsoftOneNote` |

## Setup

Your customers sign in to Microsoft OneNote through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Microsoft OneNote from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Microsoft OneNote**.
2. Select **Connect** on the Microsoft OneNote card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Microsoft OneNote and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Microsoft OneNote's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Copy Notebook</td><td><code>copyNotebook</code></td><td>Copy a OneNote notebook to the signed-in user's notebooks or to a Microsoft 365 group. The copy runs asynchronously and The copied notebook can appear before the operation status catches up.</td></tr><tr><td>Copy Page To Section</td><td><code>copyPageToSection</code></td><td>Copy a OneNote page into another section. The copy runs asynchronously and The copied page can appear before the operation status catches up.</td></tr><tr><td>Copy Section To Notebook</td><td><code>copySectionToNotebook</code></td><td>Copy a OneNote section into another notebook. The copy runs asynchronously and The copied section can appear before the operation status catches up.</td></tr><tr><td>Copy Section To Section Group</td><td><code>copySectionToSectionGroup</code></td><td>Copy a OneNote section into a section group. The copy runs asynchronously and The copied section can appear before the operation status catches up.</td></tr><tr><td>Create Nested Section Group</td><td><code>createNestedSectionGroup</code></td><td>Create a new section group nested inside an existing OneNote section group. Names must be unique within the same level and are limited to 50 characters.</td></tr><tr><td>Create Notebook</td><td><code>createNotebook</code></td><td>Create a new OneNote notebook for the signed-in user. Notebook names must be unique, are limited to 128 characters, and cannot contain the characters ? * \ /: | ' " or angle brackets.</td></tr><tr><td>Create Notebook Section</td><td><code>createNotebookSection</code></td><td>Create a new section inside a OneNote notebook. Section names must be unique within the same level and are limited to 50 characters.</td></tr><tr><td>Create Notebook Section Group</td><td><code>createNotebookSectionGroup</code></td><td>Create a new section group inside a OneNote notebook. Section group names must be unique within the same level and are limited to 50 characters.</td></tr><tr><td>Create Page</td><td><code>createPage</code></td><td>Create a OneNote page in the signed-in user's default section by posting its HTML. The title comes from the title element in the HTML head. Binary images and file attachments require a multipart request and are not supported by this action.</td></tr><tr><td>Create Section Group Section</td><td><code>createSectionGroupSection</code></td><td>Create a new section inside a OneNote section group. Section names must be unique within the same level and are limited to 50 characters.</td></tr></tbody></table>

<details>

<summary>View 20 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Section Page</td><td><code>createSectionPage</code></td><td>Create a OneNote page in a specific section by posting its HTML. The title comes from the title element in the HTML head. Binary images and file attachments require a multipart request and are not supported by this action.</td></tr><tr><td>Delete Page</td><td><code>deletePage</code></td><td>Delete a OneNote page belonging to the signed-in user.</td></tr><tr><td>Get Notebook</td><td><code>getNotebook</code></td><td>Retrieve the properties of a single OneNote notebook belonging to the signed-in user.</td></tr><tr><td>Get Notebook From Web URL</td><td><code>getNotebookFromWebUrl</code></td><td>Look up a OneNote notebook by the full URL path to it, for example a link copied from OneNote or SharePoint. The URL may also carry a onenote: prefix.</td></tr><tr><td>Get Operation</td><td><code>getOperation</code></td><td>Check the status of a long-running OneNote operation such as a notebook, section or page copy. Poll this until the status reports completed or failed. Note that the copied resource can appear before the operation status catches up, so a status that still reads 'not started' does not mean the copy has not happened.</td></tr><tr><td>Get Page</td><td><code>getPage</code></td><td>Retrieve the metadata of a single OneNote page, including its title and the content URL. Use Get Page Content to fetch the HTML body.</td></tr><tr><td>Get Page Content</td><td><code>getPageContent</code></td><td>Retrieve the HTML body of a OneNote page. Set Include IDs to true to have OneNote return the generated element identifiers that Update Page Content targets.</td></tr><tr><td>Get Recent Notebooks</td><td><code>getRecentNotebooks</code></td><td>Retrieve the OneNote notebooks the signed-in user has opened most recently, optionally including their personal notebooks.</td></tr><tr><td>Get Section</td><td><code>getSection</code></td><td>Retrieve the properties of a single OneNote section belonging to the signed-in user.</td></tr><tr><td>Get Section Group</td><td><code>getSectionGroup</code></td><td>Retrieve the properties of a single OneNote section group belonging to the signed-in user.</td></tr><tr><td>List Nested Section Groups</td><td><code>listNestedSectionGroups</code></td><td>Retrieve the section groups nested inside another OneNote section group belonging to the signed-in user.</td></tr><tr><td>List Notebook Section Groups</td><td><code>listNotebookSectionGroups</code></td><td>Retrieve the section groups directly inside a OneNote notebook belonging to the signed-in user.</td></tr><tr><td>List Notebook Sections</td><td><code>listNotebookSections</code></td><td>Retrieve the sections directly inside a OneNote notebook belonging to the signed-in user.</td></tr><tr><td>List Notebooks</td><td><code>listNotebooks</code></td><td>Retrieve the OneNote notebooks belonging to the signed-in user, including notebooks shared with them.</td></tr><tr><td>List Pages</td><td><code>listPages</code></td><td>Retrieve every OneNote page the signed-in user has access to, across all of their notebooks and sections.</td></tr><tr><td>List Section Group Sections</td><td><code>listSectionGroupSections</code></td><td>Retrieve the sections inside a OneNote section group belonging to the signed-in user.</td></tr><tr><td>List Section Groups</td><td><code>listSectionGroups</code></td><td>Retrieve every OneNote section group the signed-in user has access to, across all of their notebooks.</td></tr><tr><td>List Section Pages</td><td><code>listSectionPages</code></td><td>Retrieve the pages held in a specific OneNote section belonging to the signed-in user.</td></tr><tr><td>List Sections</td><td><code>listSections</code></td><td>Retrieve every OneNote section the signed-in user has access to, across all of their notebooks.</td></tr><tr><td>Update Page Content</td><td><code>updatePageContent</code></td><td>Change the HTML content of a OneNote page by applying a list of patch commands. Each command names a target element, an action such as append, insert or replace, and the HTML to apply. Use Get Page Content with Include IDs to discover the target identifiers.</td></tr></tbody></table>

</details>

