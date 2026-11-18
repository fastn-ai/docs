---
description: "DataRobot is an enterprise AI platform for building, deploying and monitoring predictive and generative AI models."
hidden: true
---

# DataRobot

<img src="../../.gitbook/assets/connectors/data-robot.png" alt="DataRobot logo" width="64">

DataRobot is an enterprise AI platform for building, deploying and monitoring predictive and generative AI models. This connector wraps the DataRobot Public API v2 (app.datarobot.com/api/v2): projects, autopilot and leaderboard models, AI Catalog datasets, Use Cases, deployments, model registry, batch predictions, credentials and data connectivity, custom models and execution environments, GenAI playgrounds/LLM blueprints/chats/vector databases, tags, comments and (admin-gated) user management.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [datarobot.com](https://datarobot.com) |
| **Authentication** | Bearer token |
| **Slug** | `dataRobot` |

## Use it

Add DataRobot from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dataRobot.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Model Package | `archiveModelPackage` | Archives a model package by id. Returns no content on success. |
| Archive Registered Model | `archiveRegisteredModel` | Archives a registered model by id (all its versions must be undeployed). Returns no content on success. |
| Cancel Batch Prediction Job | `cancelBatchPredictionJob` | Cancels (aborts) a batch prediction job by id. Returns no content on success. |
| Cancel Model Job | `cancelModelJob` | Cancels a queued or running model training job. Returns no content on success. |
| Cancel Project Job | `cancelProjectJob` | Cancels a queued or running project job by id. Returns no content on success. |
| Change Deployment Status | `changeDeploymentStatus` | Activates or deactivates a deployment. Returns 202. |
| Clone Project | `cloneProject` | Clones a project into a new project with a new name. Returns 202 Accepted (asynchronous; find the clone with List Projects). |
| Compute Feature Impact | `computeFeatureImpact` | Starts feature impact computation for a model. Returns 202 with a job reference. |
| Create Batch Prediction Job | `createBatchPredictionJob` | Creates a batch prediction job for a deployment with intake (e.g. dataset/URL/S3/JDBC) and output settings. Returns 202 with the job record. |
| Create Batch Prediction Job Definition | `createBatchPredictionJobDefinition` | Creates a Batch Prediction job definition (a saved job configuration that can be run manually or on a cron schedule when enabled=true). Payload mirrors createBatchPredictionJob plus name, enabled and schedule. Returns 202 with the definition (id, name, enabled, schedule, batchPredictionJob). Docs: POST /api/v2/batchPredictionJobDefinitions/. |

<details>

<summary>See 182 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Chat | `createChat` | Creates a chat for an LLM blueprint. |
| Create Comment | `createComment` | Posts a comment on an entity. For Use Cases pass entityType experimentContainer with the Use Case id (the API returns 404 for entityType useCase). |
| Create Credential | `createCredential` | Stores a new credential set (basic user/password, api_token, bearer token, s3 keys, gcp key, azure, snowflake, ...). The type-specific secret fields are passed as additional keys. |
| Create Custom Model | `createCustomModel` | Creates a custom inference model (or training task) with name, target type/name, language and class labels. Versions (code) are added separately. |
| Create Custom Model Version | `createCustomModelVersion` | Creates a new custom model version on a base execution environment (metadata-only: JSON body; the vendor's multipart file upload for model artifacts is not supported by the engine, so add files from a repository/codespace or via the UI). isMajorUpdate must be the string "true" or "false". |
| Create Data Source | `createDataSource` | Creates an external data source over a data store (table/schema or SQL query). |
| Create Data Store | `createDataStore` | Creates an external data store (JDBC driver + URL/fields, or native dr-connector/dr-database). |
| Create Dataset Featurelist | `createDatasetFeaturelist` | Creates a featurelist on an AI Catalog dataset from a list of feature names. |
| Create Dataset From URL | `createDatasetFromUrl` | Creates an AI Catalog dataset by ingesting a file from a URL. Returns 202 with catalogId, catalogVersionId and statusId to poll with Get Task Status. Link it to a Use Case afterwards with Link Entities To Use Case. |
| Create Dataset Version From URL | `createDatasetVersionFromUrl` | Creates a new version of an AI Catalog dataset by ingesting a file from a URL. Returns 202 with catalogId, catalogVersionId and statusId. |
| Create Deployment From Model Package | `createDeploymentFromModelPackage` | Creates a deployment from a model package (registered model version) on a prediction environment. Returns 202 with the deployment id. |
| Create Entity Tag | `createEntityTag` | Creates an entity tag (entityType experiment_container = Use Case tag). |
| Create Featurelist | `createFeaturelist` | Creates a featurelist in a project from a list of feature names. |
| Create LLM Blueprint | `createLlmBlueprint` | Creates an LLM blueprint in a playground with an LLM id, settings (system prompt, max completion length, temperature...), optional vector database and prompt template. |
| Create Playground | `createPlayground` | Creates a GenAI playground in a Use Case. |
| Create Project | `createProject` | Creates a new project from a URL, an AI Catalog dataset (datasetId) or a data source. Returns 202 Accepted; the project id arrives asynchronously (Location header status task, not exposed by the engine) - use List Projects with projectName to find it. |
| Create Use Case | `createUseCase` | Creates a Use Case with a name and optional description. |
| Delete Batch Prediction Job Definition | `deleteBatchPredictionJobDefinition` | Deletes a saved batch prediction job definition by id. Returns no content on success. |
| Delete Chat | `deleteChat` | Deletes a chat by id. Returns no content on success. |
| Delete Comment | `deleteComment` | Deletes a comment by id. Returns no content on success. |
| Delete Credential | `deleteCredential` | Deletes a stored credential set by id. Returns no content on success. |
| Delete Custom Model | `deleteCustomModel` | Deletes a custom model by id (must not be deployed). Returns no content on success. |
| Delete Data Source | `deleteDataSource` | Deletes an external data source by id. Returns no content on success. |
| Delete Data Store | `deleteDataStore` | Deletes an external data store by id. Returns no content on success. |
| Delete Dataset | `deleteDataset` | Soft-deletes an AI Catalog dataset by id (recoverable with Recover Deleted Dataset). Returns no content on success. |
| Delete Dataset Featurelist | `deleteDatasetFeaturelist` | Deletes a dataset featurelist by id. Returns no content on success. |
| Delete Deployment | `deleteDeployment` | Deletes a deployment by id. Returns no content on success. |
| Delete Entity Tag | `deleteEntityTag` | Deletes an entity tag by id. Returns no content on success. |
| Delete Featurelist | `deleteFeaturelist` | Deletes a project featurelist by id, optionally as a dry run or deleting dependent models. |
| Delete LLM Blueprint | `deleteLlmBlueprint` | Deletes an LLM blueprint by id. Returns no content on success. |
| Delete Model | `deleteModel` | Deletes a model from the project leaderboard. Returns no content on success. |
| Delete Playground | `deletePlayground` | Deletes a GenAI playground by id. Returns no content on success. |
| Delete Prediction Dataset | `deletePredictionDataset` | Deletes a prediction dataset from a project. Returns no content on success. |
| Delete Project | `deleteProject` | Soft-deletes a project by id (recoverable with Recover Deleted Project). Returns no content on success. |
| Delete Use Case | `deleteUseCase` | Deletes a Use Case by id. Returns no content on success. |
| Download Dataset File | `downloadDatasetFile` | Downloads the original data of an AI Catalog dataset as CSV text (only for datasets with persisted data). |
| Get Account Info | `getAccountInfo` | Returns the authenticated user account: uid, username, email, orgId, tenantId, language and permissions (documented at docs.datarobot.com; not in the OpenAPI file). |
| Get API Version | `getApiVersion` | Returns the DataRobot public API version (major, minor, versionString). |
| Get Batch Prediction Job | `getBatchPredictionJob` | Returns a batch prediction job by id with its status, progress and links. |
| Get Batch Prediction Job Definition | `getBatchPredictionJobDefinition` | Returns a saved batch prediction job definition by id. |
| Get Blueprint | `getBlueprint` | Returns a blueprint of a project by id. |
| Get Catalog Item | `getCatalogItem` | Returns the latest version information of an AI Catalog item by catalog id. |
| Get Chat | `getChat` | Returns a chat by id. |
| Get Chat Prompt | `getChatPrompt` | Returns a chat prompt by id with its execution status and LLM result text. |
| Get Credential | `getCredential` | Returns a stored credential set by id (metadata only). |
| Get Custom Application | `getCustomApplication` | Returns a custom application by id. |
| Get Custom Job | `getCustomJob` | Returns a custom job by id. |
| Get Custom Model | `getCustomModel` | Returns a custom model by id including its latest version. |
| Get Custom Model Limits | `getCustomModelLimits` | Returns the custom model resource limits (memory, replicas, network egress) of the user. |
| Get Custom Model Version | `getCustomModelVersion` | Returns a custom model version by custom model id and version id. |
| Get Data Source | `getDataSource` | Returns an external data source by id. |
| Get Data Store | `getDataStore` | Returns an external data store by id. |
| Get Dataset | `getDataset` | Returns an AI Catalog dataset (latest version) by id. |
| Get Dataset Feature Histogram | `getDatasetFeatureHistogram` | Returns the histogram of a dataset feature. |
| Get Dataset Featurelist | `getDatasetFeaturelist` | Returns a dataset featurelist by id. |
| Get Dataset Permissions | `getDatasetPermissions` | Returns the permissions of the current user on an AI Catalog dataset. |
| Get Dataset Version | `getDatasetVersion` | Returns an AI Catalog dataset version by dataset id and version id. |
| Get Deployment | `getDeployment` | Returns a deployment by id with its model, prediction environment and health summaries. |
| Get Deployment Limits | `getDeploymentLimits` | Returns the deployment limits (max deployments, current count) of the user. |
| Get Deployment Settings | `getDeploymentSettings` | Returns the monitoring settings of a deployment (association id, target drift, feature drift, challenger models, predictions data collection, ...). |
| Get Execution Environment | `getExecutionEnvironment` | Returns an execution environment by id with its latest version. |
| Get Feature Histogram | `getFeatureHistogram` | Returns the histogram (bin plot) of a project feature. |
| Get Feature Impact | `getFeatureImpact` | Returns the computed feature impact of a model (404 until Compute Feature Impact has run). |
| Get Featurelist | `getFeaturelist` | Returns a project featurelist by id. |
| Get LLM | `getLlm` | Returns an LLM definition by id with its settings schema. |
| Get LLM Blueprint | `getLlmBlueprint` | Returns an LLM blueprint by id. |
| Get Model | `getModel` | Returns a leaderboard model by id with its metrics, processes and featurelist. |
| Get Model Job | `getModelJob` | Returns a model training job of a project by id (303 redirect to the model once finished). |
| Get Model Package | `getModelPackage` | Returns a model package by id. |
| Get Notebook | `getNotebook` | Returns a notebook by id. |
| Get Playground | `getPlayground` | Returns a GenAI playground by id. |
| Get Predict Job | `getPredictJob` | Returns a prediction job of a project by id (303 redirect to the predictions once finished). |
| Get Prediction Dataset | `getPredictionDataset` | Returns a prediction dataset of a project by id. |
| Get Predictions | `getPredictions` | Returns a completed set of predictions (rows with prediction values) by prediction id. |
| Get Project | `getProject` | Returns a project by id with its stage, target, metric, partition, holdout and advanced options. |
| Get Project Access Control | `getProjectAccessControl` | Returns the access control list (users and roles) of a project. |
| Get Project Feature | `getProjectFeature` | Returns one project feature by name with its type, importance and statistics. |
| Get Project Job | `getProjectJob` | Returns a project job by id (303 redirect to the result once finished). |
| Get Project Status | `getProjectStatus` | Returns the autopilot status of a project (stage, stageDescription, autopilotDone). |
| Get Quota | `getQuota` | Returns one resource quota by id. |
| Get Rate Limit Usage | `getRateLimitUsage` | Returns the rate limit resource usage of the authenticated user. |
| Get Recommended Model | `getRecommendedModel` | Returns the model recommended for deployment in a project. |
| Get Registered Model | `getRegisteredModel` | Returns a registered model by id. |
| Get Registered Model Version | `getRegisteredModelVersion` | Returns a registered model version (model package) by registered model id and version id. |
| Get Task Status | `getTaskStatus` | Returns the status of an asynchronous task. The statusId is the last path segment of the Location header returned by asynchronous create calls (e.g. Create Project); Create Dataset From URL returns it in the body. |
| Get Use Case | `getUseCase` | Returns a Use Case by id with its entity counts. |
| Get User | `getUser` | Returns a user by id (requires Admin API access permissions). |
| Get Vector Database | `getVectorDatabase` | Returns a GenAI vector database by id. |
| Link Entities To Use Case | `linkEntitiesToUseCase` | Links multiple entities (projects, datasets, deployments, playgrounds, ...) to a Use Case. Returns no content on success. |
| List Access Roles | `listAccessRoles` | Lists the access roles (global and organization-specific) available in the organization. |
| List Application Templates | `listApplicationTemplates` | Lists the application templates accessible to the user. |
| List Batch Prediction Job Definitions | `listBatchPredictionJobDefinitions` | Lists the saved batch prediction job definitions with search, deployment and pagination filters. |
| List Batch Prediction Jobs | `listBatchPredictionJobs` | Lists the batch prediction jobs with status, deployment, model, date and pagination filters. |
| List Blueprints | `listBlueprints` | Lists the blueprints available in a project repository (after the target is set). |
| List Catalog Items | `listCatalogItems` | Lists all AI Catalog items (datasets, files, ...) accessible to the user with search, tag, type, order and pagination filters. |
| List Chat Prompts | `listChatPrompts` | Lists the prompts (with LLM responses) of a chat, LLM blueprint or playground. |
| List Chats | `listChats` | Lists the chats of an LLM blueprint. |
| List Comments | `listComments` | Lists the comments on an entity by type and id. For Use Cases pass entityType experimentContainer with the Use Case id. |
| List Credential Associations | `listCredentialAssociations` | Lists the objects (data stores, etc.) associated with a credential set. |
| List Credentials | `listCredentials` | Lists the stored credential sets of the user (metadata only, never secrets). |
| List Custom Applications | `listCustomApplications` | Lists the custom applications created by the user with name, order and pagination filters. |
| List Custom Job Runs | `listCustomJobRuns` | Lists the runs of a custom job. |
| List Custom Jobs | `listCustomJobs` | Lists the custom jobs with search, type, running and pagination filters. |
| List Custom Model Versions | `listCustomModelVersions` | Lists the versions of a custom model. |
| List Custom Models | `listCustomModels` | Lists the custom inference models / training tasks with type, target, deployed, search, order and pagination filters. |
| List Data Drivers | `listDataDrivers` | Lists the JDBC / native drivers available for creating data stores. |
| List Data Sources | `listDataSources` | Lists the external data sources (tables or queries defined over data stores). |
| List Data Stores | `listDataStores` | Lists the external data stores (JDBC / native connector connections). |
| List Dataset Featurelists | `listDatasetFeaturelists` | Lists the featurelists of an AI Catalog dataset. |
| List Dataset Features | `listDatasetFeatures` | Lists the features of an AI Catalog dataset with statistics, optionally with histogram plots and data quality issues. |
| List Dataset Projects | `listDatasetProjects` | Lists the projects created from an AI Catalog dataset. |
| List Dataset Shared Roles | `listDatasetSharedRoles` | Lists the shared roles (users/groups/orgs) of an AI Catalog dataset. |
| List Dataset Versions | `listDatasetVersions` | Lists the versions of an AI Catalog dataset. |
| List Datasets | `listDatasets` | Lists the AI Catalog datasets with category, Use Case, order and pagination filters. |
| List Deleted Projects | `listDeletedProjects` | Lists soft-deleted projects of the user with search, date, id, order and pagination filters. |
| List Deployment Features | `listDeploymentFeatures` | Lists the features (with types and importance) of the model deployed in a deployment. |
| List Deployments | `listDeployments` | Lists the deployments with search, order and pagination filters. |
| List Entity Tags | `listEntityTags` | Lists the entity tags (currently for Use Cases / experiment containers) with search, order and pagination filters. |
| List Execution Environment Versions | `listExecutionEnvironmentVersions` | Lists the versions of an execution environment with their build status. |
| List Execution Environments | `listExecutionEnvironments` | Lists the execution environments (built-in and custom) with search, use-case and visibility filters. |
| List Feature Metrics | `listFeatureMetrics` | Lists the metrics that are valid when the given feature is used as the project target. |
| List Featurelists | `listFeaturelists` | Lists the featurelists of a project with sort and search filters. |
| List LLM Blueprints | `listLlmBlueprints` | Lists the LLM blueprints of a playground with LLM, saved/starred, sort and pagination filters. |
| List LLMs | `listLlms` | Lists the LLMs available in the GenAI playground with their settings schema. |
| List Model Jobs | `listModelJobs` | Lists the model training jobs of a project (queued and in-progress by default; status filter queue\|inprogress\|error). |
| List Model Packages | `listModelPackages` | Lists the model packages with model, search, prediction-environment and pagination filters. |
| List Models | `listModels` | Lists the leaderboard models of a project with metric, name, sample percentage, starred and order filters. |
| List Notebooks | `listNotebooks` | Lists the notebooks with name, Use Case, order and pagination filters. |
| List Notification Channels | `listNotificationChannels` | Lists the notification channels (requires the notifications management permission). |
| List Notification Policies | `listNotificationPolicies` | Lists the notification policies with channel, name and event-group filters (requires the notifications management permission). |
| List Playgrounds | `listPlaygrounds` | Lists the GenAI playgrounds with Use Case, search, sort and pagination filters. |
| List Predict Jobs | `listPredictJobs` | Lists the prediction jobs of a project (status filter queue\|inprogress\|error). |
| List Prediction Datasets | `listPredictionDatasets` | Lists the prediction datasets uploaded to a project. |
| List Prediction Environments | `listPredictionEnvironments` | Lists the prediction environments available for deployments (documented in the DataRobot MLOps docs; not in the OpenAPI file). |
| List Prediction Servers | `listPredictionServers` | Lists the dedicated prediction servers available to the user. |
| List Predictions | `listPredictions` | Lists the prediction records of a project, optionally filtered by model or prediction dataset. |
| List Project Features | `listProjectFeatures` | Lists the features of a project with type, importance and summary statistics; supports sort, search and featurelist filters. |
| List Project Jobs | `listProjectJobs` | Lists the jobs of a project (queued and in-progress by default; status filter queue\|inprogress\|error). |
| List Projects | `listProjects` | Lists the projects of the user with name, id, orderBy and pagination filters. |
| List Quotas | `listQuotas` | Lists the resource quotas visible to the user with resource filters and pagination. |
| List Recommended Models | `listRecommendedModels` | Lists the models recommended by DataRobot for a project (e.g. Recommended for Deployment, Most Accurate). |
| List Registered Model Deployments | `listRegisteredModelDeployments` | Lists the deployments that use versions of a registered model. |
| List Registered Model Versions | `listRegisteredModelVersions` | Lists the versions (model packages) of a registered model. |
| List Registered Models | `listRegisteredModels` | Lists the registered models with search, target, creator, sort and pagination filters. |
| List Supported Embeddings | `listSupportedEmbeddings` | Lists the embedding models supported for vector databases. |
| List Supported Text Chunkings | `listSupportedTextChunkings` | Lists the text chunking methods and their parameters supported for vector databases. |
| List Use Case Datasets | `listUseCaseDatasets` | Lists the AI Catalog datasets linked to a Use Case. |
| List Use Case Deployments | `listUseCaseDeployments` | Lists the deployments linked to a Use Case. |
| List Use Case Projects | `listUseCaseProjects` | Lists the projects linked to a Use Case. |
| List Use Case Resources | `listUseCaseResources` | Lists all entities (projects, datasets, deployments, playgrounds, ...) linked to a Use Case with type and order filters. |
| List Use Case Shared Roles | `listUseCaseSharedRoles` | Lists the access control list (shared roles) of a Use Case. |
| List Use Cases | `listUseCases` | Lists the Use Cases with search, linked-entity, sort and pagination filters. |
| List Users | `listUsers` | Lists the users of the organization (requires Admin API access permissions; other keys receive 403). |
| List Vector Databases | `listVectorDatabases` | Lists the GenAI vector databases with Use Case, playground, search, sort and pagination filters. |
| Pause Or Resume Autopilot | `pauseAutopilot` | Pauses (command=stop) or resumes (command=start) the Autopilot run of a project. POST /projects/{projectId}/autopilot/. Returns 202 with no body. To start a new Autopilot run on a modeling featurelist use startAutopilot. |
| Recover Deleted Dataset | `recoverDeletedDataset` | Recovers a soft-deleted AI Catalog dataset by id. Returns no content on success. |
| Recover Deleted Project | `recoverDeletedProject` | Recovers a soft-deleted project by id (action: undelete). |
| Register Leaderboard Model | `registerLeaderboardModel` | Creates a model package (registered model version) from a leaderboard model so it can be deployed. |
| Request Predictions | `requestPredictions` | Requests predictions from a model on a prediction dataset already uploaded to the project. Returns 202 (predict job; see List Predict Jobs / List Predictions). |
| Send Chat Prompt | `sendChatPrompt` | Submits a user prompt to an LLM blueprint chat. The response text is generated asynchronously (executionStatus); poll Get Chat Prompt for resultText. |
| Set Project Target | `setProjectTarget` | Sets the target and starts modeling for a project (Aim): autopilot mode, metric, partitioning and common advanced options (the full option set of the vendor's PATCH /projects/{id}/aim/ is accepted via additional keys). Returns 202 Accepted. |
| Start Autopilot | `startAutopilot` | Starts autopilot on a featurelist of a project whose target is already set. Returns 201 with no body. |
| Test Data Store Connection | `testDataStoreConnection` | Tests the connection of an external data store with a stored credential id or inline credentials. |
| Train Model | `trainModel` | Trains a new model from a blueprint in a project, optionally on a featurelist and sample size. Returns 202 (model job created; see List Model Jobs). |
| Update Comment | `updateComment` | Updates the content of a comment by id. |
| Update Credential | `updateCredential` | Updates the name, description or secret fields of a stored credential set (type-specific fields as additional keys). |
| Update Custom Model | `updateCustomModel` | Updates the name, description, target settings or class labels of a custom model. |
| Update Data Store | `updateDataStore` | Updates the name or connection parameters of an external data store. |
| Update Dataset | `updateDataset` | Renames a dataset or updates its categories. Returns the updated dataset. |
| Update Dataset Featurelist | `updateDatasetFeaturelist` | Renames or updates the description of a dataset featurelist. |
| Update Deployment | `updateDeployment` | Updates the label, description or importance of a deployment. Returns no content on success. |
| Update Deployment Settings | `updateDeploymentSettings` | Updates the monitoring settings of a deployment (association id, target/feature drift, challenger models, predictions data collection, automatic actuals, ...). Returns 202. |
| Update Entity Tag | `updateEntityTag` | Renames an entity tag by id. |
| Update Featurelist | `updateFeaturelist` | Renames or updates the description of a project featurelist. Returns no content on success. |
| Update LLM Blueprint | `updateLlmBlueprint` | Updates an LLM blueprint (name, description, LLM, settings, saved/starred flags, vector database). |
| Update Model | `updateModel` | Updates the starred flag or prediction threshold of a leaderboard model. Returns no content on success. |
| Update Playground | `updatePlayground` | Renames a GenAI playground or updates its description. |
| Update Project | `updateProject` | Updates project name, description, holdout unlock or worker counts by id. Returns no content on success. |
| Update Project Access Control | `updateProjectAccessControl` | Grants, updates or removes user roles on a project. Returns no content on success. |
| Update Registered Model | `updateRegisteredModel` | Renames a registered model or updates its description / global flag. |
| Update Use Case | `updateUseCase` | Updates the name or description of a Use Case. |
| Upload Prediction Dataset From URL | `uploadPredictionDatasetFromUrl` | Uploads a prediction dataset to a project from a URL. Returns 202 (asynchronous; see List Prediction Datasets). |

</details>
