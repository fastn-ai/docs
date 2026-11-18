---
description: "Cube Cloud is a universal semantic layer that serves governed metrics and data models to BI tools, applications and AI agents."
---

# Cube Cloud

Cube Cloud is a universal semantic layer that serves governed metrics and data models to BI tools, applications and AI agents. This connector runs analytical queries against a Cube deployment over its REST, SQL and GraphQL data APIs, inspects the deployment's data model, and manages pre-aggregation builds.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [cube.dev](https://cube.dev) |
| **Authentication** | Credentials you enter |
| **Actions** | 16 |
| **Events** | 0 |
| **Slug** | `cubeCloud` |

## Use it

Add Cube Cloud from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cubeCloud.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Running Query | `cancelRunningQuery` | Cancel an in-flight query by the request identifier it is running under. Cube takes that identifier from the x-request-id header supplied when the query was started, so this action is used together with a client that sets that header. Returns the definitions of the queries that were cancelled; an empty result array means no query was running under that identifier, which is also what a completed or unknown identifier returns. |
| Check Liveness | `checkLiveness` | Check the liveness of the Cube deployment by testing the data source connections it already holds open. Returns HTTP 200 when the deployment is healthy and HTTP 500 when it is down. Cube Cloud answers this endpoint with a bare JSON boolean rather than an object, so the response carries no named fields; open-source Cube answers with an object holding a health field set to HEALTH or DOWN. Served at the host root and requires no API scope. |
| Check Pre-Aggregation Match | `checkPreAggregationMatch` | Check whether a given pre-aggregation definition can answer a query. Take the Transformed Query from the transformedQueries array returned by the Dry Run Query action, and describe the candidate pre-aggregation in References. This is the check the Rollup Designer uses when it proposes a rollup. Requires the meta API scope. |
| Check Readiness | `checkReadiness` | Check the readiness of the Cube deployment by opening a connection to its default data source. Returns HTTP 200 when the deployment can reach its database and HTTP 500 when it cannot. Cube Cloud answers this endpoint with a bare JSON boolean rather than an object, so the response carries no named fields; open-source Cube answers with an object holding a health field set to HEALTH or DOWN. Served at the host root and requires no API scope. |
| Convert GraphQL Query To Cube Query | `convertGraphqlQuery` | Translate a GraphQL query written against the Cube GraphQL API into the equivalent Cube query object, so it can be inspected or replayed through the Run Query action. Returns a null Cube query when the GraphQL document cannot be translated. Requires the graphql API scope. |
| Convert SQL Query To Cube Query | `convertSqlQuery` | Translate a SQL statement written against the SQL API into the equivalent Cube query object, so it can be inspected, edited or replayed through the Run Query action. Requires the data API scope. |
| Dry Run Query | `dryRunQuery` | Validate a query and return how Cube would interpret it without running it: the resolved query type, the normalized queries with every default filled in, the transformed queries used for pre-aggregation matching, and the pivot query. Use the returned transformed query as the input to the Check Pre-Aggregation Match action. Requires the data API scope. |
| Get Data Model | `getDataModel` | Retrieve the deployment's data model: every cube and view that is exposed to this API token, together with its measures, dimensions, segments, hierarchies and folders. Use this to discover the exact measure and dimension names that the query actions require. |
| Get Generated SQL | `getGeneratedSql` | Return the SQL that Cube would generate for a query, without executing it against the database. Useful for debugging the semantic layer and for confirming whether a pre-aggregation will be used. Requires the data API scope. |
| Get Pre-Aggregation Job Status | `getPreAggregationJobStatus` | Look up the status of pre-aggregation build jobs by the tokens returned from the Trigger Pre-Aggregation Build action. Requires the jobs API scope, which is off by default: enable it on the deployment by setting the CUBEJS_DEFAULT_API_SCOPES environment variable to meta,data,graphql,jobs. |
| Run Blended Query | `runBlendedQuery` | Run several Cube queries in a single request and return their results side by side, which is how Cube supports data blending across cubes that do not share a join path. Every query in the request must carry a time dimension at the same granularity, otherwise Cube rejects the request with 'Failed to generate blending query key'. Results are returned in the order the queries were submitted. Requires the data API scope. |
| Run GraphQL Query | `runGraphqlQuery` | Run a GraphQL query against the deployment's GraphQL API, which exposes every cube and view as a GraphQL type. Returns the standard GraphQL envelope with a data object and, on failure, an errors array. Requires the graphql API scope. |
| Run Query | `runQuery` | Run an analytical query against the deployment's semantic layer and return the aggregated rows. This is the main data endpoint: supply measures, dimensions, time dimensions, filters and segments and Cube generates and executes the SQL, serving the result from a pre-aggregation where one matches. Requires the data API scope. |
| Run SQL Query | `runSqlQuery` | Execute a SQL statement against the deployment's SQL API, where cubes and views are exposed as tables and their measures must be wrapped in MEASURE(). The response is not a JSON object: Cube streams newline delimited JSON, whose first line is an object holding the column schema and lastRefreshTime and whose following lines each hold a data array of positional row arrays. The connector returns that stream verbatim as a string, so the caller parses it line by line. Requires the data API scope. |
| Subscribe To Query Updates | `subscribeToQueryUpdates` | Poll a query for real-time updates. This endpoint returns the same result as Run Query together with the lastRefreshTime that identifies the underlying data version, so a caller can re-run it on an interval and detect when the result has changed. Cube's push based real-time transport is a WebSocket and is not reachable over HTTP, so this polling endpoint is the HTTP equivalent. Requires the data API scope. |
| Trigger Pre-Aggregation Build | `triggerPreAggregationBuild` | Queue pre-aggregation builds and return one job token per queued build, which can then be polled with the Get Pre-Aggregation Job Status action. Use the selector to narrow the build to particular pre-aggregations, cubes, data sources, time zones or partition date ranges. Requires the jobs API scope, which is off by default: enable it on the deployment by setting the CUBEJS_DEFAULT_API_SCOPES environment variable to meta,data,graphql,jobs. |
