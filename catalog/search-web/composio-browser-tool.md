---
description: "Composio Browser Tool runs cloud browser tasks for AI agents. Create browser tasks, read sessions and output files, and run tools."
hidden: true
---

# Composio Browser Tool

<img src="../../.gitbook/assets/connectors/lg/composio-browser-tool.png" alt="Composio Browser Tool logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [composio.dev](https://composio.dev) |
| **Authentication** | API key |
| **Slug** | `composioBrowserTool` |

## Setup

Your customers enter their API key for Composio Browser Tool when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Composio Browser Tool from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Composio Browser Tool**.
2. Select **Connect** on the Composio Browser Tool card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Composio Browser Tool's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Browser Task</td><td><code>createBrowserTask</code></td><td>Starts an AI-powered browser automation task in a Composio cloud browser (BROWSER_TOOL_CREATE_TASK). The agent follows your natural-language instructions to navigate sites, click, fill forms and extract data. Returns a watch_task_id to poll with Watch Browser Task and a browser_session_id for Get Browser Session. Pass sessionId to continue in an existing browser session (its previous task must be finished or stopped). Consumes Composio credits.</td></tr><tr><td>Execute Tools</td><td><code>executeTools</code></td><td>Executes one or more Composio tools discovered with Search Tools, in parallel (COMPOSIO_MULTI_EXECUTE_TOOL). Each entry names a tool slug (for example BROWSER_TOOL_CREATE_TASK) and its schema-compliant arguments; the toolkit must have an active connection. Use the dedicated Browser Tool actions for the common browser operations.</td></tr><tr><td>Get Browser Output File</td><td><code>getBrowserOutputFile</code></td><td>Gets a download URL for a file produced by a browser task (BROWSER_TOOL_GET_OUTPUT_FILE), such as a PDF, image or spreadsheet listed in Watch Browser Task's outputFiles. Download promptly; the URL is temporary.</td></tr><tr><td>Get Browser Session</td><td><code>getBrowserSession</code></td><td>Retrieves a cloud browser session by id (BROWSER_TOOL_GET_SESSION), including its status and the liveUrl where the AI agent can be watched working in real time. Call it right after Create Browser Task with the browser_session_id.</td></tr><tr><td>Get Tool Schemas</td><td><code>getToolSchemas</code></td><td>Retrieves the full input (and optionally output) schemas of Composio tools by slug (COMPOSIO_GET_TOOL_SCHEMAS), for example BROWSER_TOOL_CREATE_TASK. Only pass slugs returned by Search Tools.</td></tr><tr><td>List Router Tools</td><td><code>listRouterTools</code></td><td>Lists the tools exposed by the Composio Tool Router MCP server for your consumer key (search tools, get tool schemas, execute tools, manage connections, remote bash and workbench, skills), with each tool's name, description and input schema.</td></tr><tr><td>Manage Connections</td><td><code>manageConnections</code></td><td>Creates or manages app connections for a toolkit through the Tool Router (COMPOSIO_MANAGE_CONNECTIONS): add returns an authorization link, list returns connected accounts with ids, aliases and statuses, rename changes an account alias and remove deletes a connected account. Browser Tool itself needs no connection.</td></tr><tr><td>Manage Skill</td><td><code>manageSkill</code></td><td>Creates, updates or deletes an organization Skill (COMPOSIO_MANAGE_SKILL). create needs title and skill_markdown; update needs the exact existing skill id plus title and skill_markdown; delete needs only the id. Send only the fields that apply to the chosen action.</td></tr><tr><td>Run Remote Bash Command</td><td><code>runRemoteBashCommand</code></td><td>Executes a bash command in Composio's remote sandbox (COMPOSIO_REMOTE_BASH_TOOL), for example to process large tool responses saved there with jq, awk or grep. Commands run from /home/user with a hard 3-minute limit.</td></tr><tr><td>Run Remote Workbench Code</td><td><code>runRemoteWorkbenchCode</code></td><td>Runs Python code in Composio's persistent remote Jupyter workbench (COMPOSIO_REMOTE_WORKBENCH) to process files saved there or script bulk tool executions with the preloaded helpers (run_composio_tool, invoke_llm, upload_local_file, proxy_execute, web_search). Hard 3-minute limit per cell.</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Skills</td><td><code>searchSkills</code></td><td>Searches the reusable Skills (saved workflows) of your Composio organization by query (COMPOSIO_SEARCH_SKILLS) and returns matching skills with their ids and slugs.</td></tr><tr><td>Search Tools</td><td><code>searchTools</code></td><td>Searches the Composio catalog for tools that fit a use case (COMPOSIO_SEARCH_TOOLS) and returns a recommended execution plan, known pitfalls, the matching tool slugs with input schemas, toolkit connection status and a session_id to reuse in later router calls.</td></tr><tr><td>Stop Browser Task</td><td><code>stopBrowserTask</code></td><td>Stops a running browser task and its cloud browser session (BROWSER_TOOL_STOP_TASK). Use it when a task is stuck, looping or heading in the wrong direction, or before starting a new task in the same session.</td></tr><tr><td>Use Skill</td><td><code>useSkill</code></td><td>Loads one organization Skill by its exact slug (COMPOSIO_USE_SKILL) and returns its Markdown instructions.</td></tr><tr><td>Wait For Connections</td><td><code>waitForConnections</code></td><td>Waits for pending toolkit authorizations started with Manage Connections to reach an active or failed state, or times out (COMPOSIO_WAIT_FOR_CONNECTIONS). Mode any returns when one toolkit finishes; all waits for every toolkit.</td></tr><tr><td>Watch Browser Task</td><td><code>watchBrowserTask</code></td><td>Polls a browser task for progress and results (BROWSER_TOOL_WATCH_TASK). While status is started the task is still running; when it is finished, check isSuccess and read output, the executed steps, the current URL and any outputFiles. Pass lastStepSeen to receive only steps after that number.</td></tr></tbody></table>

</details>

