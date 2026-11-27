---
description: "Replicate runs machine learning models in the cloud. Create predictions and trainings, and manage models and deployments."
hidden: true
---

# Replicate

<img src="../../.gitbook/assets/connectors/lg/replicate.png" alt="Replicate logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [replicate.com](https://replicate.com) |
| **Authentication** | Access token |
| **Slug** | `replicate` |

## Setup

Your customers enter their access token for Replicate when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Replicate from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Replicate**.
2. Select **Connect** on the Replicate card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Replicate's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel Prediction</td><td><code>cancelPrediction</code></td><td>Cancel a running prediction by id. Returns the prediction in canceled state.</td></tr><tr><td>Cancel Training</td><td><code>cancelTraining</code></td><td>Cancel a running training by id. Returns the training in canceled state.</td></tr><tr><td>Create Deployment</td><td><code>createDeployment</code></td><td>Create a deployment. Body requires name, model ({owner}/{name}), version (64-char id), hardware (SKU), min_instances (0-5), max_instances (0-20).</td></tr><tr><td>Create Model</td><td><code>createModel</code></td><td>Create a new model. Body requires owner, name, visibility (public|private) and hardware (SKU from List Hardware). Returns the created model object.</td></tr><tr><td>Create Prediction</td><td><code>createPrediction</code></td><td>Run a community model by version id. Body requires version ({owner}/{name}:{version_id} or 64-char version id) and input (object of model inputs). Returns a prediction with status starting/processing/succeeded/failed/canceled.</td></tr><tr><td>Create Prediction Using Deployment</td><td><code>createDeploymentPrediction</code></td><td>Run a prediction via a deployment's private endpoint. Path requires deployment_owner and deployment_name. Body requires input (object). Returns a prediction object.</td></tr><tr><td>Create Prediction Using Model</td><td><code>createModelPrediction</code></td><td>Run an official model (no version needed). Path requires model_owner and model_name. Body requires input (object). Returns a prediction object.</td></tr><tr><td>Create Training</td><td><code>createTraining</code></td><td>Start a fine-tune training run for a trainable model version. Path requires model_owner, model_name, version_id. Body requires destination ({owner}/{name} for the trained model) and input (object of training params).</td></tr><tr><td>Delete Deployment</td><td><code>deleteDeployment</code></td><td>Delete a deployment. Path requires deployment_owner and deployment_name.</td></tr><tr><td>Delete Model</td><td><code>deleteModel</code></td><td>Delete a private model with no versions. Path requires model_owner and model_name.</td></tr></tbody></table>

<details>

<summary>View 18 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Model Version</td><td><code>deleteModelVersion</code></td><td>Delete a specific version of a private model. Path requires model_owner, model_name, version_id.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Get the authenticated account (user or organization). Useful as a credential-validation / health-check action.</td></tr><tr><td>Get Collection</td><td><code>getCollection</code></td><td>Get a collection by slug, including its nested models array. Path requires collection_slug.</td></tr><tr><td>Get Deployment</td><td><code>getDeployment</code></td><td>Get a deployment and its current_release configuration. Path requires deployment_owner and deployment_name.</td></tr><tr><td>Get Model</td><td><code>getModel</code></td><td>Get a model's metadata including latest_version and default_example. Path requires model_owner and model_name.</td></tr><tr><td>Get Model Version</td><td><code>getModelVersion</code></td><td>Get a specific model version including its openapi_schema (input/output schemas). Path requires model_owner, model_name, version_id.</td></tr><tr><td>Get Prediction</td><td><code>getPrediction</code></td><td>Get the current state of a prediction by id. Use urls.get from a created prediction or poll until status is succeeded/failed/canceled.</td></tr><tr><td>Get Training</td><td><code>getTraining</code></td><td>Get the current state of a training by id, including status and output (version + weights when succeeded).</td></tr><tr><td>Get Webhook Default Secret</td><td><code>getWebhookDefaultSecret</code></td><td>Get the signing secret for the default webhook endpoint. Returns { key } used to verify webhook payload signatures.</td></tr><tr><td>List Collections</td><td><code>listCollections</code></td><td>List curated collections of models. Cursor-paginated via next.</td></tr><tr><td>List Deployments</td><td><code>listDeployments</code></td><td>List deployments owned by the authenticated account. Cursor-paginated via next.</td></tr><tr><td>List Hardware</td><td><code>listHardware</code></td><td>List available hardware SKUs for running models. Returns an array of { name, sku }. Use the sku in Create Model / Create Deployment.</td></tr><tr><td>List Model Versions</td><td><code>listModelVersions</code></td><td>List all versions of a model, newest first. Path requires model_owner and model_name.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>List public models on Replicate. Cursor-paginated via next.</td></tr><tr><td>List Predictions</td><td><code>listPredictions</code></td><td>List predictions created by the authenticated account, newest first. Supports created_after, created_before (ISO 8601) and source (web|api) filters. Cursor-paginated via next.</td></tr><tr><td>List Trainings</td><td><code>listTrainings</code></td><td>List trainings created by the authenticated account, newest first. Cursor-paginated via next.</td></tr><tr><td>Search Models</td><td><code>searchModels</code></td><td>Search public models, collections, and docs by free-text query. Uses the current beta endpoint (query param) — replaces the deprecated QUERY-method-override on /v1/models which the gateway forces to application/json (415).</td></tr><tr><td>Update Deployment</td><td><code>updateDeployment</code></td><td>Update a deployment's configuration. Path requires deployment_owner and deployment_name. Body fields (version, hardware, min_instances, max_instances) are all optional — only send fields you wish to change.</td></tr></tbody></table>

</details>

