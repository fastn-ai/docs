---
description: "Cradl AI document-AI / IDP platform."
hidden: true
---

# Cradl AI

<img src="../../.gitbook/assets/connectors/lg/cradl-ai.png" alt="Cradl AI logo">

Cradl AI document-AI / IDP platform. Build and run document agents, upload documents, run LLM field-extraction predictions, manage validation (human-in-the-loop) tasks, hooks, actions, models, roles, users, app clients, connections and secrets on https://api.cradl.ai/v1.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [cradl.ai](https://cradl.ai) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `cradlAi` |

## Use it

Add Cradl AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cradlAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Agent | `createAgent` | Create a new Cradl AI document agent. Returns the created agent including its agentId. |
| Create Agent Run | `createAgentRun` | Start a new run of a Cradl AI agent. METERED: each run consumes one agent run from the organization's monthly allowance. Returns the created run with its runId; poll Get Agent Run for the result. |
| Create App Client | `createAppClient` | Create a Cradl AI OAuth app client. SECURITY WARNING: when generateSecret is true (the default) the response contains a live clientSecret in plaintext - it is returned exactly once and anyone who can read this action's output receives a working API credential. Handle the response as a secret. |
| Create Asset | `createAsset` | Upload a base64 asset used by legacy workflow transitions. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1 - the request body shape could not be confirmed live because the gate rejects the call before body validation. |
| Create Automation Action | `createAutomationAction` | Create a Cradl AI automation action. functionId must reference an existing function, e.g. cradl:organization:cradl/cradl:function:create-prediction. Returns the created action with its actionId. |
| Create Automation Action Run | `createAutomationActionRun` | Execute a Cradl AI automation action with the given input. METERED: consumes one action run from the organization's monthly allowance. "input" is required and must be an object. |
| Create Connection | `createConnection` | Create a third-party identity connection. The only supported type today is "microsoft-idp" (Microsoft Entra). type, config and setupParams are all REQUIRED, and setupParams must carry redirectUrl, code and codeVerifier from a COMPLETED Microsoft OAuth consent - so this call can only be made after an interactive browser sign-in. Undocumented route - discovered live on api.cradl.ai/v1. |
| Create Dataset | `createDataset` | Create a training dataset that documents can be filed under. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1 - the body shape could not be confirmed live because the gate rejects the call before body validation. |
| Create Document | `createDocument` | Upload a document to Cradl AI for extraction. "content" is the file as a base64 string (max 6,250,000 chars) and contentType must be one of application/pdf, image/jpeg, image/png, image/tiff, image/webp, message/rfc822. Returns the documentId plus signed file URLs. |
| Create Function | `createFunction` | Create a custom function that automation actions and hooks can run. runtime must be python or nodejs. Returns the created function with its functionId. |

<details>

<summary>See 118 more actions</summary>

* **Create Hook** `createHook`: Create a hook that reacts to a Cradl AI platform event. trigger must be one of "ActionRun has Completed", "Document is Created", "Email is Received", "Prediction is Created", "ValidationTask has Completed", "ValidationTask is Created". functionId must reference an existing function.
* **Create Hook Run** `createHookRun`: Fire a hook manually. METERED: consumes one hook run from the monthly allowance. hookId, input and agentRunId are all REQUIRED by the live API - a hook run must belong to an agent run. The API rejects name/description fields even though the published OpenAPI lists them.
* **Create Model** `createModel`: Create an extraction model. fieldConfig is REQUIRED and maps each field id to its type/description. llmVersion selects the underlying model (sonnet-4.0, sonnet-4.5, sonnet-4.6, qwen3-vl).
* **Create Model Data Bundle** `createModelDataBundle`: Build a training data bundle for a model from one or more datasets. METERED: consumes a data bundle from the monthly allowance. Undocumented route - discovered live on api.cradl.ai/v1; on free-tier plans the API returns a 403 entitlement gate.
* **Create Model Training** `createModelTraining`: Start a fine-tuning training run for an extraction model over its data bundles. METERED AND EXPENSIVE: consumes a training from the monthly allowance and GPU hours. Undocumented route - discovered live on api.cradl.ai/v1; on free-tier plans the API returns a 403 entitlement gate.
* **Create Organization** `createOrganization`: Create a new Cradl AI organization. NOTE: app-client (client-credentials) tokens cannot call this and receive 400 "Cannot invoke API method with an app client" - it requires an interactive user token.
* **Create Payment Method** `createPaymentMethod`: Register a billing payment method on the organization and return its paymentMethodId, which Update Organization can then set as the active one. BILLING: this creates a real billing object. SECURITY WARNING: the response contains a live Stripe SetupIntent client secret and the Stripe publishable key. Undocumented route - discovered live on api.cradl.ai/v1.
* **Create Prediction** `createPrediction`: Run an extraction model over a document and return the predicted field values. documentId and modelId are REQUIRED. METERED: consumes one prediction plus one page prediction per page - check Get Organization first. Set async true to return immediately and poll Get Prediction. NOTE: the live API rejects a "description" field even though the published OpenAPI lists one.
* **Create Role** `createRole`: Create a custom access role. permissions is REQUIRED: an array of {resourceId, effect (allow|deny), action (read|write|delegate|*)} rules.
* **Create Secret** `createSecret`: Store a secret (API keys, tokens or other credentials) that automation actions reference by secretId. "data" is REQUIRED and holds the secret payload - it is write-only and is never returned by any read route. Undocumented route - discovered live on api.cradl.ai/v1.
* **Create Suggestion** `createSuggestion`: Ask Cradl AI to suggest a configuration - for example a field set for an extraction model - from a document or prompt. "type" selects which kind of suggestion is generated. METERED: suggestions run an LLM. Undocumented route - discovered live on api.cradl.ai/v1.
* **Create Transition** `createTransition`: Create a legacy workflow transition (docker or manual processing step). LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1 - the body shape could not be confirmed live because the gate rejects the call before body validation.
* **Create Validation** `createValidation`: Create a validation definition - a human-in-the-loop review step that agents route low-confidence extractions to. Returns the created validation with its validationId.
* **Create Validation Task** `createValidationTask`: Queue a document or extraction for human review under a validation. METERED: consumes one validation task from the organization's monthly allowance. "input" is required and must be an object.
* **Create Workflow** `createWorkflow`: Create a legacy state-machine workflow. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1 - the body shape could not be confirmed live because the gate rejects the call before body validation.
* **Delete Agent** `deleteAgent`: Permanently delete a Cradl AI agent and its configuration. Returns the deleted agent object.
* **Delete Agent Run** `deleteAgentRun`: Permanently delete an agent run and its associated documents and predictions.
* **Delete App Client** `deleteAppClient`: Permanently delete an OAuth app client. WARNING: deleting the app client whose credentials are in use revokes your own API access - never delete the client you are authenticated as.
* **Delete Asset** `deleteAsset`: Permanently delete a legacy asset by assetId. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1.
* **Delete Automation Action** `deleteAutomationAction`: Permanently delete a Cradl AI automation action. Returns the deleted action object.
* **Delete Connection** `deleteConnection`: Permanently delete a third-party connection. Automation actions referencing it stop working. Undocumented route - discovered live on api.cradl.ai/v1.
* **Delete Dataset** `deleteDataset`: Permanently delete a training dataset and unfile its documents. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1.
* **Delete Document** `deleteDocument`: Permanently delete a single document by documentId. Returns the deleted document object.
* **Delete Documents By Filter** `deleteDocumentsByFilter`: BULK DELETE: permanently delete every document matching the datasetId/consentId filter, up to maxResults. Calling it with no filter targets the whole organization - always run List Documents with the same filter first. Returns the list of deleted documents.
* **Delete Function** `deleteFunction`: Permanently delete a custom function. Any automation action or hook still referencing it will stop working.
* **Delete Hook** `deleteHook`: Permanently delete a hook, stopping the automation it triggers. Returns the deleted hook object.
* **Delete Model** `deleteModel`: Permanently delete an extraction model along with its trainings and data bundles. Agents referencing it stop extracting.
* **Delete Model Data Bundle** `deleteModelDataBundle`: Permanently delete a training data bundle from a model. Undocumented route - discovered live on api.cradl.ai/v1.
* **Delete Payment Method** `deletePaymentMethod`: Permanently remove a billing payment method from the organization. BILLING: removing the active payment method can suspend a paid plan. Undocumented route - discovered live on api.cradl.ai/v1.
* **Delete Role** `deleteRole`: Permanently delete a custom access role. WARNING: users and app clients holding only this role lose their access - never delete a built-in role or the role your own credentials depend on.
* **Delete Secret** `deleteSecret`: Permanently delete a stored secret. Automation actions referencing it stop authenticating. Undocumented route - discovered live on api.cradl.ai/v1.
* **Delete Transition** `deleteTransition`: Permanently delete a legacy transition. Workflows referencing it stop running. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1.
* **Delete Validation** `deleteValidation`: Permanently delete a validation definition and stop the review step it drives. Returns the deleted validation object.
* **Delete Workflow** `deleteWorkflow`: Permanently delete a legacy workflow and its execution history. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1.
* **Get Agent** `getAgent`: Fetch a single Cradl AI agent by its agentId (form cradl:agent:xxx).
* **Get Agent Run** `getAgentRun`: Fetch a single agent run by agentId and runId, including its status and extracted output. Poll this after Create Agent Run - agent runs complete asynchronously.
* **Get Agent Statistics** `getAgentStatistics`: Fetch aggregate accuracy and throughput statistics for an agent - global, per-field, and per-day breakdowns - optionally limited to a date window.
* **Get App Client** `getAppClient`: Fetch a single OAuth app client by appClientId. *** SECURITY WARNING: unlike List App Clients, this endpoint returns the app client's live OAuth clientSecret in plaintext. Anyone who can read this action's output receives working API credentials for the whole organization. Treat every response as a secret and prefer List App Clients when you only need metadata. ***
* **Get Asset** `getAsset`: Fetch a single legacy asset by assetId (form las:asset:xxx). LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1.
* **Get Automation Action** `getAutomationAction`: Fetch a single Cradl AI automation action by actionId (form cradl:action:xxx).
* **Get Automation Action Run** `getAutomationActionRun`: Fetch a single automation action run by actionId and runId, including its status and output.
* **Get Connection** `getConnection`: Fetch a single third-party connection by connectionId, including its config. Undocumented route - discovered live on api.cradl.ai/v1.
* **Get Dataset** `getDataset`: Fetch a single training dataset by datasetId (form las:dataset:xxx). LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1.
* **Get Document** `getDocument`: Fetch a single document by documentId, including its ground truth and signed download URLs. SECURITY: fileUrl is a pre-signed URL that serves the private document content to anyone holding the link until it expires.
* **Get Function** `getFunction`: Fetch a single custom function by functionId. Use the bare id (cradl:function:xxx) - the organization-prefixed form contains a slash and is not a valid path segment.
* **Get Hook** `getHook`: Fetch a single hook by hookId, including its trigger, function and routed actions.
* **Get Hook Run** `getHookRun`: Fetch a single hook run by hookId and runId, including its status and output.
* **Get Log** `getLog`: Fetch a single execution log entry by logId, including its event array.
* **Get Model** `getModel`: Fetch a single extraction model by modelId, optionally with accuracy statistics over the last N days.
* **Get Model Data Bundle** `getModelDataBundle`: Fetch a single training data bundle by modelId and dataBundleId. dataBundleId must match the pattern las:model-data-bundle: followed by 32 hex characters. Undocumented route - discovered live on api.cradl.ai/v1.
* **Get Model Training** `getModelTraining`: Fetch a single training run by modelId and trainingId. trainingId must match the pattern las:model-training:xxx. Undocumented route - discovered live on api.cradl.ai/v1.
* **Get Organization** `getOrganization`: Fetch an organization and its full quota/usage counters (monthly agent runs, predictions, page predictions, documents, action runs, hook runs, validation tasks and the created-vs-allowed counts for agents, actions, hooks, models, datasets, assets and app clients). Pass organizationId "me" for the organization the credentials belong to - app-client tokens are denied on the literal id. This is the quota endpoint: call it before driving any metered route.
* **Get Payment Method** `getPaymentMethod`: Fetch a single billing payment method by paymentMethodId. SECURITY WARNING: the response contains a live Stripe SetupIntent client secret (stripeSetupIntentSecret) that can be used to attach a payment card to this organization's billing. Treat the response as a secret. Undocumented route - discovered live on api.cradl.ai/v1.
* **Get Plan** `getPlan`: Fetch a single subscription plan by planId, with its quotas and pricing. Undocumented route - discovered live on api.cradl.ai/v1.
* **Get Prediction** `getPrediction`: Fetch a single prediction by predictionId, including the extracted field values and their confidences. Poll this after an async Create Prediction.
* **Get Profile** `getProfile`: Fetch the identity profile behind an organization member - email, given/family name and picture. Get the profileId from List Users. The literal "me" is NOT accepted. SECURITY: returns the member's personal email address. Undocumented route - discovered live on api.cradl.ai/v1.
* **Get Role** `getRole`: Fetch a single access role by roleId, including its permission rules.
* **Get Transition** `getTransition`: Fetch a single legacy transition by transitionId (form las:transition:xxx). LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1.
* **Get User** `getUser`: Fetch a single organization member by userId, including roleIds, profileId and account status. The literal "me" is NOT accepted here - pass a real userId from List Users.
* **Get Validation** `getValidation`: Fetch a single validation definition by validationId, including its config and enabled flag.
* **Get Validation Task** `getValidationTask`: Fetch a single human review task by validationId and taskId, including its status, input and reviewer output.
* **Get Workflow** `getWorkflow`: Fetch a single legacy workflow by workflowId (form las:workflow:xxx). LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1.
* **Invite User** `inviteUser`: Invite a person to the Cradl AI organization. email is REQUIRED. CAUTION: this sends a real invitation email to the address given - only call it with an address you own. Returns the created user with its userId.
* **List Agent Runs** `listAgentRuns`: List the processing runs of a Cradl AI agent, optionally filtered by status and created/updated time window.
* **List Agents** `listAgents`: List the document AI agents in the Cradl AI organization. Returns an "agents" array of agent objects (agentId, name, description, metadata, timestamps) plus a nextToken for pagination.
* **List App Clients** `listAppClients`: List the OAuth app clients of the Cradl AI organization. SECURITY: each row contains the app client's own OAuth clientId (half of an API credential); hasSecret is a boolean only, the secret itself is not returned.
* **List Assets** `listAssets`: List the assets (static files such as JSON config or templates referenced by workflow transitions) of the organization. LEGACY "las" API family: the route exists on api.cradl.ai/v1 but is entitlement-gated - accounts without the legacy workflow entitlement receive 403 "[Forbidden] User is not authorized to access this resource because no identity-based policy allows the execute-api:Invoke action", and the auth server refuses to issue the matching scope.
* **List Automation Action Runs** `listAutomationActionRuns`: List the execution runs of a Cradl AI automation action, optionally filtered by status.
* **List Automation Actions** `listAutomationActions`: List the Cradl AI automation actions (export/integration steps attached to agents). Returns an "actions" array plus nextToken.
* **List Connections** `listConnections`: List the third-party connections (credentials stored in Cradl AI for export integrations such as HTTP endpoints, email or storage). Undocumented route - discovered live on api.cradl.ai/v1.
* **List Datasets** `listDatasets`: List the training datasets of the organization (document collections used to build model data bundles). LEGACY "las" API family: the route exists on api.cradl.ai/v1 but is entitlement-gated and returns 403 "[Forbidden] User is not authorized to access this resource because no identity-based policy allows the execute-api:Invoke action" on accounts without it.
* **List Documents** `listDocuments`: List documents stored in Cradl AI, optionally filtered by datasetId, consentId or documentId and sorted.
* **List Functions** `listFunctions`: List the custom functions (python/nodejs code units that automation actions and hooks run) owned by the organization.
* **List Hook Runs** `listHookRuns`: List the execution runs of a hook, optionally filtered by status.
* **List Hooks** `listHooks`: List the hooks of the organization. A hook is a trigger rule: when its trigger event fires it evaluates a function and routes to trueActionId or falseActionId.
* **List Logs** `listLogs`: List execution log entries, optionally filtered by workflowId, workflowExecutionId, transitionId or transitionExecutionId.
* **List Model Data Bundles** `listModelDataBundles`: List the training data bundles attached to an extraction model. Undocumented route - discovered live on api.cradl.ai/v1.
* **List Model Trainings** `listModelTrainings`: List the fine-tuning training runs of an extraction model. Undocumented route - discovered live on api.cradl.ai/v1.
* **List Models** `listModels`: List the extraction models of the organization. Each model carries its fieldConfig, llmVersion and training counts.
* **List Organizations** `listOrganizations`: List organizations visible to the caller. NOTE: app-client (client-credentials) tokens cannot list organizations and receive 400 "App Clients cannot list organizations" - use Get Organization with organizationId "me" instead.
* **List Payment Methods** `listPaymentMethods`: List the billing payment methods registered on the organization. Undocumented route - discovered live on api.cradl.ai/v1.
* **List Plans** `listPlans`: List the subscription plans available to the organization, with their quotas and prices. Undocumented route - discovered live on api.cradl.ai/v1. Read-only: the API exposes no create, update or delete for plans.
* **List Predictions** `listPredictions`: List extraction predictions, optionally filtered by modelId and sorted. Reading predictions is free; only creating them is metered.
* **List Roles** `listRoles`: List the access roles of the organization (administrator, developer, reviewer and any custom roles) with their permission rules.
* **List Secrets** `listSecrets`: List the secrets stored in Cradl AI for automation actions. Only metadata is returned, not the secret data. Undocumented route - discovered live on api.cradl.ai/v1. There is no single-secret GET route.
* **List Transition Executions** `listTransitionExecutions`: List the executions of a legacy transition, optionally filtered by status or execution id. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1.
* **List Transitions** `listTransitions`: List the transitions (docker/manual processing steps that legacy workflows are built from) of the organization. LEGACY "las" API family: the route exists on api.cradl.ai/v1 but is entitlement-gated and returns 403 "[Forbidden] User is not authorized to access this resource because no identity-based policy allows the execute-api:Invoke action" on accounts without it.
* **List Users** `listUsers`: List the members of the Cradl AI organization with their roleIds, profileId and status.
* **List Validation Tasks** `listValidationTasks`: List the human review tasks queued under a validation, optionally filtered by status (ready, in-progress, succeeded, failed, cancelled).
* **List Validations** `listValidations`: List the validation definitions (human-in-the-loop review steps) of the organization.
* **List Workflow Executions** `listWorkflowExecutions`: List the executions of a legacy workflow, optionally filtered by status. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1.
* **List Workflows** `listWorkflows`: List the legacy state-machine workflows of the organization. LEGACY "las" API family: the route exists on api.cradl.ai/v1 but is entitlement-gated - it returns 403 "[Forbidden] User is not authorized to access this resource because no identity-based policy allows the execute-api:Invoke action", and https://auth.cradl.ai/oauth2/token refuses to issue the workflows:read scope at all. Modern Cradl accounts use Agents instead.
* **Remove User** `removeUser`: Permanently remove a member from the Cradl AI organization. DESTRUCTIVE AND IRREVERSIBLE: removing the last remaining member, or the member your own credentials belong to, can lock the organization out entirely. Always run List Users first and confirm another administrator remains.
* **Update Agent** `updateAgent`: Update a Cradl AI agent's name, description, metadata or attached resourceIds. At least one field must be supplied.
* **Update Agent Run** `updateAgentRun`: Update an agent run. The only supported change is setting status to "archived", which removes the run from the active Runs view.
* **Update App Client** `updateAppClient`: Update an OAuth app client's name, description, roles, login URLs or metadata. At least one field must be supplied.
* **Update Asset** `updateAsset`: Replace a legacy asset's content, name or description. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1 - the body shape could not be confirmed live because the gate rejects the call before body validation.
* **Update Automation Action** `updateAutomationAction`: Update a Cradl AI automation action's name, description, config, enabled flag, function, connection or secret. At least one field must be supplied.
* **Update Automation Action Run** `updateAutomationActionRun`: Report the result of an automation action run: set its status to succeeded or failed and attach an output object. At least one field must be supplied.
* **Update Connection** `updateConnection`: Update a third-party connection's name, description or config. At least one field must be supplied. Undocumented route - discovered live on api.cradl.ai/v1.
* **Update Dataset** `updateDataset`: Update a training dataset's name, description or retention. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1 - the body shape could not be confirmed live because the gate rejects the call before body validation.
* **Update Document** `updateDocument`: Update a document's name, description, dataset, retention or ground-truth labels. At least one field must be supplied.
* **Update Function** `updateFunction`: Update a custom function's name, description or metadata. At least one field must be supplied.
* **Update Hook** `updateHook`: Update a hook's trigger, function, routed actions, config or enabled flag. At least one field must be supplied.
* **Update Hook Run** `updateHookRun`: Report the result of a hook run: set status to succeeded, failed or ignored and attach an output object. At least one field must be supplied.
* **Update Model** `updateModel`: Update an extraction model's fields, LLM version, preprocessing, postprocessing or active trainingId. At least one field must be supplied.
* **Update Model Data Bundle** `updateModelDataBundle`: Update a training data bundle's name, description or metadata. At least one field must be supplied. Undocumented route - discovered live on api.cradl.ai/v1.
* **Update Model Training** `updateModelTraining`: Update a training run's name, description, status or metadata. At least one field must be supplied. Undocumented route - discovered live on api.cradl.ai/v1.
* **Update Organization** `updateOrganization`: Update an organization's name, description, URL, document retention, billing plan or payment method. BILLING: changing planId or paymentMethodId affects what the account is charged. At least one field must be supplied.
* **Update Payment Method** `updatePaymentMethod`: Update a billing payment method's name, description or metadata. At least one field must be supplied. Undocumented route - discovered live on api.cradl.ai/v1.
* **Update Profile** `updateProfile`: Update an identity profile's given name, family name or picture. At least one field must be supplied. Undocumented route - discovered live on api.cradl.ai/v1; app-client (client-credentials) tokens are denied on it and receive a 403 entitlement gate.
* **Update Role** `updateRole`: Update a custom role's name, description or permission rules. At least one field must be supplied. Editing a built-in role changes access for every user holding it.
* **Update Secret** `updateSecret`: Rotate or rename a stored secret. At least one field must be supplied; supplying "data" replaces the secret payload. Undocumented route - discovered live on api.cradl.ai/v1.
* **Update Transition** `updateTransition`: Update a legacy transition's name, description, parameters or schemas. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1 - the body shape could not be confirmed live because the gate rejects the call before body validation.
* **Update User** `updateUser`: Update an organization member's name, description, roles or metadata. At least one field must be supplied. Changing roleIds changes what that person can do.
* **Update Validation** `updateValidation`: Update a validation definition's name, description, config or metadata. At least one field must be supplied.
* **Update Validation Task** `updateValidationTask`: Move a human review task through its lifecycle - set status to ready, in-progress, succeeded, failed or cancelled and attach the corrected field values as output. At least one field must be supplied.
* **Update Workflow** `updateWorkflow`: Update a legacy workflow's name, description or notification configuration. LEGACY "las" API family, entitlement-gated on api.cradl.ai/v1 - the body shape could not be confirmed live because the gate rejects the call before body validation.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| ActionRun has Completed | `actionrun.completed` | Fires when an automation action run reaches a terminal status. Registration is UI-only - see Document is Created for the exact click-path. The API-side equivalent is a Hook with trigger "ActionRun has Completed". |
| Document is Created | `document.created` | Fires when a document is uploaded to the agent. REGISTRATION IS UI-ONLY: Cradl AI publishes no outbound-webhook registration API (every guessed webhook function id returns 404 NotFound on POST /actions). To deliver this event to fastn: open app.cradl.ai, pick your agent, open the agent's flow, click Add export, choose Webhook, paste the fastn trigger URL into URL, set HTTP Method to POST, add any auth headers under HTTP Headers, click Test webhook and confirm a 2xx, then Save and Publish the agent. The API-side equivalent of this trigger is a Hook with trigger "Document is Created" (see Create Hook). |
| Email is Received | `email.received` | Fires when a document arrives at the agent's Mailhook address. Registration is UI-only - see Document is Created for the exact click-path, and see docs.cradl.ai/integrations/email for the mailhook address. The API-side equivalent is a Hook with trigger "Email is Received". |
| Prediction is Created | `prediction.created` | Fires when an extraction prediction is produced for a document. Registration is UI-only - see Document is Created for the exact click-path (agent &gt; Add export &gt; Webhook &gt; URL/Method/Headers &gt; Test webhook &gt; Save &gt; Publish). The API-side equivalent is a Hook with trigger "Prediction is Created". |
| ValidationTask has Completed | `validationtask.completed` | Fires when a reviewer finishes a human-review task. Registration is UI-only - see Document is Created for the exact click-path. The API-side equivalent is a Hook with trigger "ValidationTask has Completed". |
| ValidationTask is Created | `validationtask.created` | Fires when a document is routed to human review. Registration is UI-only - see Document is Created for the exact click-path. The API-side equivalent is a Hook with trigger "ValidationTask is Created". |
