---
description: "Composio Browser Tool lets AI agents run cloud-browser automation tasks (navigate sites, fill forms, extract data) through the Composio Connect Tool Router."
hidden: true
---

# Composio Browser Tool

<img src="../../.gitbook/assets/connectors/lg/composio-browser-tool.png" alt="Composio Browser Tool logo">

Composio Browser Tool lets AI agents run cloud-browser automation tasks (navigate sites, fill forms, extract data) through the Composio Connect Tool Router. This connector calls the Tool Router MCP endpoint over HTTPS (JSON-RPC): create, watch and stop Browser Tool tasks, get the live browser session and download output files, plus the router's own tools for searching tools, fetching tool schemas, executing any Composio tool, managing app connections, remote bash and Python workbench, and organization skills.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [composio.dev](https://composio.dev) |
| **Authentication** | API key |
| **Slug** | `composioBrowserTool` |

## Use it

Add Composio Browser Tool from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.composioBrowserTool.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Browser Task | `createBrowserTask` | Starts an AI-powered browser automation task in a Composio cloud browser (BROWSER_TOOL_CREATE_TASK). The agent follows your natural-language instructions to navigate sites, click, fill forms and extract data. Returns a watch_task_id to poll with Watch Browser Task and a browser_session_id for Get Browser Session. Pass sessionId to continue in an existing browser session (its previous task must be finished or stopped). Consumes Composio credits. |
| Execute Tools | `executeTools` | Executes one or more Composio tools discovered with Search Tools, in parallel (COMPOSIO_MULTI_EXECUTE_TOOL). Each entry names a tool slug (for example BROWSER_TOOL_CREATE_TASK) and its schema-compliant arguments; the toolkit must have an active connection. Use the dedicated Browser Tool actions for the common browser operations. |
| Get Browser Output File | `getBrowserOutputFile` | Gets a download URL for a file produced by a browser task (BROWSER_TOOL_GET_OUTPUT_FILE), such as a PDF, image or spreadsheet listed in Watch Browser Task's outputFiles. Download promptly; the URL is temporary. |
| Get Browser Session | `getBrowserSession` | Retrieves a cloud browser session by id (BROWSER_TOOL_GET_SESSION), including its status and the liveUrl where the AI agent can be watched working in real time. Call it right after Create Browser Task with the browser_session_id. |
| Get Tool Schemas | `getToolSchemas` | Retrieves the full input (and optionally output) schemas of Composio tools by slug (COMPOSIO_GET_TOOL_SCHEMAS), for example BROWSER_TOOL_CREATE_TASK. Only pass slugs returned by Search Tools. |
| List Router Tools | `listRouterTools` | Lists the tools exposed by the Composio Tool Router MCP server for your consumer key (search tools, get tool schemas, execute tools, manage connections, remote bash and workbench, skills), with each tool's name, description and input schema. |
| Manage Connections | `manageConnections` | Creates or manages app connections for a toolkit through the Tool Router (COMPOSIO_MANAGE_CONNECTIONS): add returns an authorization link, list returns connected accounts with ids, aliases and statuses, rename changes an account alias and remove deletes a connected account. Browser Tool itself needs no connection. |
| Manage Skill | `manageSkill` | Creates, updates or deletes an organization Skill (COMPOSIO_MANAGE_SKILL). create needs title and skill_markdown; update needs the exact existing skill id plus title and skill_markdown; delete needs only the id. Send only the fields that apply to the chosen action. |
| Run Remote Bash Command | `runRemoteBashCommand` | Executes a bash command in Composio's remote sandbox (COMPOSIO_REMOTE_BASH_TOOL), for example to process large tool responses saved there with jq, awk or grep. Commands run from /home/user with a hard 3-minute limit. |
| Run Remote Workbench Code | `runRemoteWorkbenchCode` | Runs Python code in Composio's persistent remote Jupyter workbench (COMPOSIO_REMOTE_WORKBENCH) to process files saved there or script bulk tool executions with the preloaded helpers (run_composio_tool, invoke_llm, upload_local_file, proxy_execute, web_search). Hard 3-minute limit per cell. |
| Search Skills | `searchSkills` | Searches the reusable Skills (saved workflows) of your Composio organization by query (COMPOSIO_SEARCH_SKILLS) and returns matching skills with their ids and slugs. |
| Search Tools | `searchTools` | Searches the Composio catalog for tools that fit a use case (COMPOSIO_SEARCH_TOOLS) and returns a recommended execution plan, known pitfalls, the matching tool slugs with input schemas, toolkit connection status and a session_id to reuse in later router calls. |
| Stop Browser Task | `stopBrowserTask` | Stops a running browser task and its cloud browser session (BROWSER_TOOL_STOP_TASK). Use it when a task is stuck, looping or heading in the wrong direction, or before starting a new task in the same session. |
| Use Skill | `useSkill` | Loads one organization Skill by its exact slug (COMPOSIO_USE_SKILL) and returns its Markdown instructions. |
| Wait For Connections | `waitForConnections` | Waits for pending toolkit authorizations started with Manage Connections to reach an active or failed state, or times out (COMPOSIO_WAIT_FOR_CONNECTIONS). Mode any returns when one toolkit finishes; all waits for every toolkit. |
| Watch Browser Task | `watchBrowserTask` | Polls a browser task for progress and results (BROWSER_TOOL_WATCH_TASK). While status is started the task is still running; when it is finished, check isSuccess and read output, the executed steps, the current URL and any outputFiles. Pass lastStepSeen to receive only steps after that number. |
