---
description: "Replicate HTTP API (https://api.replicate.com/v1) — run ML models via predictions, manage models/versions, deployments, trainings, collections, hardware,…"
hidden: true
---

# Replicate

Replicate HTTP API (https://api.replicate.com/v1) — run ML models via predictions, manage models/versions, deployments, trainings, collections, hardware, account, and webhook secret. Auth: Bearer r8_ API token.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [replicate.com](https://replicate.com) |
| **Authentication** | Bearer token |
| **Actions** | 28 |
| **Events** | 0 |
| **Slug** | `replicate` |

## Use it

Add Replicate from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.replicate.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Prediction | `cancelPrediction` | Cancel a running prediction by id. Returns the prediction in canceled state. |
| Cancel Training | `cancelTraining` | Cancel a running training by id. Returns the training in canceled state. |
| Create Deployment | `createDeployment` | Create a deployment. Body requires name, model ({owner}/{name}), version (64-char id), hardware (SKU), min_instances (0-5), max_instances (0-20). |
| Create Model | `createModel` | Create a new model. Body requires owner, name, visibility (public\|private) and hardware (SKU from List Hardware). Returns the created model object. |
| Create Prediction | `createPrediction` | Run a community model by version id. Body requires version ({owner}/{name}:{version_id} or 64-char version id) and input (object of model inputs). Returns a prediction with status starting/processing/succeeded/failed/canceled. |
| Create Prediction Using Deployment | `createDeploymentPrediction` | Run a prediction via a deployment's private endpoint. Path requires deployment_owner and deployment_name. Body requires input (object). Returns a prediction object. |
| Create Prediction Using Model | `createModelPrediction` | Run an official model (no version needed). Path requires model_owner and model_name. Body requires input (object). Returns a prediction object. |
| Create Training | `createTraining` | Start a fine-tune training run for a trainable model version. Path requires model_owner, model_name, version_id. Body requires destination ({owner}/{name} for the trained model) and input (object of training params). |
| Delete Deployment | `deleteDeployment` | Delete a deployment. Path requires deployment_owner and deployment_name. Returns 204 No Content. |
| Delete Model | `deleteModel` | Delete a private model with no versions. Path requires model_owner and model_name. Returns 204 No Content. |
| Delete Model Version | `deleteModelVersion` | Delete a specific version of a private model. Path requires model_owner, model_name, version_id. Returns 202 Accepted. |
| Get Account | `getAccount` | Get the authenticated account (user or organization). Useful as a credential-validation / health-check action. |
| Get Collection | `getCollection` | Get a collection by slug, including its nested models array. Path requires collection_slug. |
| Get Deployment | `getDeployment` | Get a deployment and its current_release configuration. Path requires deployment_owner and deployment_name. |
| Get Model | `getModel` | Get a model's metadata including latest_version and default_example. Path requires model_owner and model_name. |
| Get Model Version | `getModelVersion` | Get a specific model version including its openapi_schema (input/output schemas). Path requires model_owner, model_name, version_id. |
| Get Prediction | `getPrediction` | Get the current state of a prediction by id. Use urls.get from a created prediction or poll until status is succeeded/failed/canceled. |
| Get Training | `getTraining` | Get the current state of a training by id, including status and output (version + weights when succeeded). |
| Get Webhook Default Secret | `getWebhookDefaultSecret` | Get the signing secret for the default webhook endpoint. Returns { key } used to verify webhook payload signatures. |
| List Collections | `listCollections` | List curated collections of models. Cursor-paginated via next. |
| List Deployments | `listDeployments` | List deployments owned by the authenticated account. Cursor-paginated via next. |
| List Hardware | `listHardware` | List available hardware SKUs for running models. Returns an array of { name, sku }. Use the sku in Create Model / Create Deployment. |
| List Model Versions | `listModelVersions` | List all versions of a model, newest first. Path requires model_owner and model_name. |
| List Models | `listModels` | List public models on Replicate. Cursor-paginated via next. |
| List Predictions | `listPredictions` | List predictions created by the authenticated account, newest first. Supports created_after, created_before (ISO 8601) and source (web\|api) filters. Cursor-paginated via next. |
| List Trainings | `listTrainings` | List trainings created by the authenticated account, newest first. Cursor-paginated via next. |
| Search Models | `searchModels` | Search public models, collections, and docs by free-text query. Uses the current beta GET /v1/search endpoint (query param) — replaces the deprecated QUERY-method-override on /v1/models which the gateway forces to application/json (415). |
| Update Deployment | `updateDeployment` | Update a deployment's configuration. Path requires deployment_owner and deployment_name. Body fields (version, hardware, min_instances, max_instances) are all optional — only send fields you wish to change. |
