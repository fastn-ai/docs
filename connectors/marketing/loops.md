---
description: "Loops (loops.so) is an email platform for SaaS companies covering transactional email sending, contact management, custom contact properties, event-triggered…"
hidden: true
---

# Loops

<img src="../../.gitbook/assets/connectors/lg/loops.png" alt="Loops logo">

Loops (loops.so) is an email platform for SaaS companies covering transactional email sending, contact management, custom contact properties, event-triggered emails, and mailing lists, all through one REST API.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [loops.so](https://loops.so) |
| **Authentication** | Bearer token |
| **Slug** | `loops` |

## Use it

Add Loops from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.loops.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Workflow Branch | `addWorkflowBranch` | Adds a branch under an existing branch or experiment node. A BranchNode gains an AudienceFilter child and an ExperimentBranchNode gains a VariantNode child. Returns the created child node with the updated workflow. |
| Change Workflow Mailing List | `changeWorkflowMailingList` | Changes or clears the mailing list a workflow sends to. If the change would remove queued contacts the call returns status queuedContactsFound instead of applying; retry with queuedContactPolicy set to discard to apply it and drop those contacts. |
| Check Contact Suppression Status | `checkContactSuppression` | Checks whether a contact is on Loops' suppression list (e.g. due to a hard bounce or spam report), identified by email address or user ID. |
| Complete Upload | `completeUpload` | Finalizes an image upload after the file has been PUT to the pre-signed URL, returning the public URL of the stored image asset. |
| Create Audience Segment | `createAudienceSegment` | Creates a saved audience segment from a tree of contact conditions, for reuse when targeting campaigns. The name must be unique within the team. |
| Create Campaign | `createCampaign` | Creates a new draft campaign. An empty email message is created automatically and its ID is returned; use Update Email Message to set the campaign's subject, sender and content. |
| Create Campaign Group | `createCampaignGroup` | Creates a new campaign group for organising campaigns. The name cannot be the reserved value Unsorted. |
| Create Component | `createComponent` | Creates a reusable email component from an LMX body, which can then be embedded in campaign and transactional emails. |
| Create Contact | `createContact` | Creates a new contact in Loops. Returns an error if a contact with the same email or user ID already exists. |
| Create Contact Property | `createContactProperty` | Creates a new custom contact property that can then be set on contacts and used to personalize emails and segment audiences. |

<details>

<summary>See 55 more actions</summary>

* **Create Theme** `createTheme`: Creates a new email theme defining the colors, spacing, borders, fonts and heading styles applied across Loops emails.
* **Create Transactional Email Template** `createTransactionalEmail`: Creates a new transactional email template. An empty draft email message is created automatically and its ID is returned; use Update Email Message to add content, then Publish Transactional Email Template before sending.
* **Create Transactional Group** `createTransactionalGroup`: Creates a new transactional group for organising transactional email templates. The name cannot be the reserved value Unsorted.
* **Create Upload** `createUpload`: Requests a pre-signed URL for uploading an image asset. Upload the file with an HTTP PUT to the returned URL using the same content type, then call Complete Upload to finalize it.
* **Create Workflow** `createWorkflow`: Creates a draft workflow containing a blank trigger node and an exit node. Use Create Workflow Node to build out the automation and Update Workflow Node to configure its trigger.
* **Create Workflow Node** `createWorkflowNode`: Adds a new node to a workflow graph and returns it with the updated workflow. Position it with insertMode: between requires fromNodeId and toNodeId, before requires toNodeId, and after requires fromNodeId. Trigger and exit nodes cannot be created.
* **Delete Contact** `deleteContact`: Permanently deletes a contact, identified by email address or user ID. Provide exactly one of the two.
* **Delete Workflow** `deleteWorkflow`: Permanently deletes a workflow, returning 204 No Content on success. If the workflow is currently sending or has queued contacts, Loops returns 409 Conflict; retry with confirmDelete set to true to delete it, stop sending and cancel queued contacts.
* **Delete Workflow Node** `deleteWorkflowNode`: Deletes a single workflow node, reconnecting its parent to its child. If contacts are queued at the node the call returns status queuedContactsFound instead of deleting; retry with queuedContactPolicy set to discard to delete it and drop those contacts.
* **Delete Workflow Nodes Recursively** `deleteWorkflowNodeRecursively`: Deletes a workflow node together with its entire downstream subtree. If contacts are queued at any node that would be removed the call returns status queuedContactsFound instead of deleting; retry with queuedContactPolicy set to discard to delete them and drop those contacts.
* **Ensure Transactional Email Draft** `ensureTransactionalDraft`: Ensures a transactional email template has a draft email message. An existing draft is returned unchanged; otherwise a new empty draft is created from the published version.
* **Find Contact** `findContact`: Finds a contact by email address or user ID and returns their full contact record, including mailing list subscriptions and opt-in status.
* **Get Audience Segment** `getAudienceSegment`: Retrieves a single audience segment by ID, including the full tree of contact conditions that defines it.
* **Get Campaign** `getCampaign`: Retrieves a single campaign by ID, including its status, scheduling, audience targeting and the ID of the email message holding its content.
* **Get Campaign Group** `getCampaignGroup`: Retrieves a single campaign group by ID, returning its name, description and timestamps.
* **Get Component** `getComponent`: Retrieves a single reusable email component by ID, returning its name and body serialized as LMX.
* **Get Email Message** `getEmailMessage`: Retrieves a single email message by ID, returning its sending settings and its body serialized as LMX. An email message belongs either to a campaign or to a transactional email template.
* **Get Event Pattern** `getEventPattern`: Retrieves a single event pattern by ID, including the event properties Loops has seen for it, which can be used to personalize emails.
* **Get Event Pattern By Name** `getEventPatternByName`: Retrieves an event pattern by its exact event name, including the event properties Loops has seen for it. Event names are case-sensitive, so signup and Signup are different events.
* **Get Theme** `getTheme`: Retrieves a single email theme by ID, returning its full set of style attributes (colors, padding, borders, fonts and heading styles) as used by the LMX Style tag.
* **Get Transactional Email Template** `getTransactionalEmail`: Retrieves a single transactional email template by ID, including its draft and published email message IDs, group membership and data variables.
* **Get Transactional Group** `getTransactionalGroup`: Retrieves a single transactional group by ID, returning its name, description and timestamps.
* **Get Workflow** `getWorkflow`: Retrieves a single workflow by ID, including its status, mailing list, root node and the full map of nodes making up the workflow graph.
* **Get Workflow Node** `getWorkflowNode`: Retrieves a single node from a workflow graph, returning its type and downstream connections plus the fields specific to that node type, such as the event name of a trigger or the email message of a send step.
* **List Audience Segments** `listAudienceSegments`: Lists the saved audience segments on this Loops account, most recently created first. Audience segments define reusable contact filters for targeting campaigns.
* **List Campaign Groups** `listCampaignGroups`: Lists the campaign groups on this Loops account, most recently created first. Campaign groups organise campaigns into folders.
* **List Campaigns** `listCampaigns`: Lists the campaigns on this Loops account, most recently created first, with their send status, group, audience and associated email message.
* **List Components** `listComponents`: Lists the reusable email components on this Loops account, returning each component's body serialized as LMX (Loops Markup Language).
* **List Contact Properties** `listContactProperties`: Lists the custom and default contact properties defined on this Loops account.
* **List Dedicated Sending IP Addresses** `listDedicatedSendingIps`: Lists Loops' dedicated sending IP addresses, for the rare case where they must be allowlisted. The list is subject to change and excludes shared sending IPs.
* **List Event Patterns** `listEventPatterns`: Lists the event patterns available to workflow event trigger nodes, showing every event name this Loops account has seen and whether it originated from an incoming webhook platform.
* **List Mailing Lists** `listMailingLists`: Lists all mailing lists configured on this Loops account, used for opt-in/opt-out segmentation of contacts.
* **List Published Transactional Emails** `listPublishedTransactionalEmails`: Lists published transactional email templates with their data variables, using the legacy transactional listing endpoint. Prefer List Transactional Email Templates, which also returns drafts and group membership.
* **List Themes** `listThemes`: Lists the email themes on this Loops account, each with its full set of style attributes and whether it is the account default.
* **List Transactional Email Templates** `listTransactionalEmailTemplates`: Lists the transactional email templates configured on this Loops account, including their data variables. Requires the Content API to be enabled for the team; on accounts without it, this returns an error naming the requirement.
* **List Transactional Groups** `listTransactionalGroups`: Lists the transactional groups on this Loops account, most recently created first. Transactional groups organise transactional email templates into folders.
* **List Workflows** `listWorkflows`: Lists the workflows (automations) configured on this Loops account, with their publish status, trigger type and Loops app URL.
* **Publish Transactional Email Template** `publishTransactionalEmailTemplate`: Publishes the draft version of a transactional email template, making it the live version that can be sent. The draft is cleared after publishing. Requires the Content API to be enabled for the team.
* **Remove Contact Suppression** `removeContactSuppression`: Removes a contact from Loops' suppression list, identified by email address or user ID, re-enabling email delivery to them.
* **Reroute Workflow Node Connection** `rerouteNodeConnection`: Reroutes a workflow node's single outgoing connection to a different valid target node, returning the updated source node and workflow.
* **Run Guardian Checks On Email Message** `getEmailMessageGuardian`: Runs Loops' Guardian quality checks against an email message and returns the errors that must be resolved before it can be published, plus non-blocking warnings.
* **Send Email Message Preview** `previewEmailMessage`: Sends a test preview of an email message to one or more addresses. The variable fields accepted depend on the parent: campaign previews take contact properties, workflow previews also take event properties, and transactional previews take data variables.
* **Send Event** `sendEvent`: Records a custom event for a contact, identified by email address or user ID (or both). Loops can trigger loop (workflow) emails off named events. Creates the contact if it does not already exist.
* **Send Transactional Email** `sendTransactionalEmail`: Sends a transactional email (e.g. password reset, receipt, login code) using a published transactional email template, to a single recipient.
* **Test API Key** `testApiKey`: Validates the configured Loops API key and returns the name of the team it belongs to. Use this to confirm credentials are working before calling other actions.
* **Update Campaign** `updateCampaign`: Updates a draft campaign's name, group, audience targeting or scheduling. At least one field must be provided, and a campaign can no longer be updated once it has started sending.
* **Update Campaign Group** `updateCampaignGroup`: Updates a campaign group's name or description. At least one field must be provided, and the reserved Unsorted group cannot be edited.
* **Update Component** `updateComponent`: Updates a component's name or LMX body. At least one must be provided. Changing the body cascades to every email using the component, and the response reports how many emails were affected.
* **Update Contact** `updateContact`: Updates an existing contact, or creates one if no match is found. Requires either email or userId to identify the contact; if both are provided, Loops matches on either value and reconciles the other.
* **Update Email Message** `updateEmailMessage`: Updates an email message's sending settings and LMX content. The parent campaign must still be in draft status. Pass the contentRevisionId you last read as expectedRevisionId; a stale token returns a conflict.
* **Update Theme** `updateTheme`: Updates a theme's name or styles. At least one must be provided. Changing the styles cascades to every email using the theme, and the response reports how many emails were affected.
* **Update Transactional Email Template** `updateTransactionalEmail`: Renames a transactional email template or moves it to a different transactional group. At least one field must be provided.
* **Update Transactional Group** `updateTransactionalGroup`: Updates a transactional group's name or description. At least one field must be provided, and the reserved Unsorted group cannot be edited.
* **Update Workflow Node** `updateWorkflowNode`: Updates the node-owned fields of a single workflow node, such as a trigger's event, a timer's delay or an experiment variant's sampling rate. Shared resources such as email messages and audience segments are updated through their own actions.
* **Update Workflow Properties** `updateWorkflowProperties`: Updates a workflow's display properties. At least one of name or description must be provided. To change the workflow's mailing list use Change Workflow Mailing List instead.

</details>
