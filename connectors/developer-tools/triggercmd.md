---
description: "TRIGGERcmd is a cloud service that securely runs commands on your registered computers."
hidden: true
---

# TRIGGERcmd

<img src="../../.gitbook/assets/connectors/triggercmd.png" alt="TRIGGERcmd logo" width="64">

TRIGGERcmd is a cloud service that securely runs commands on your registered computers. This connector wraps the TRIGGERcmd REST API at https://www.triggercmd.com/api: computers, commands, panels and panel buttons, command triggering (run/trigger, run/triggerSave, panel/trigger), and account authentication. WARNING: the trigger actions execute real commands on real machines - use them deliberately.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [triggercmd.com](https://triggercmd.com) |
| **Authentication** | Bearer token, No authentication, OAuth 2.0 |
| **Slug** | `triggercmd` |

## Use it

Add TRIGGERcmd from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.triggercmd.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Authenticate With Email And Password | `authenticate` | Exchange a TRIGGERcmd email and password for the account's API token. Returns 200 {"user":{...},"token":"..."}; bad credentials return 401 {"err":"invalid email or password"} and a missing field returns 401 {"err":"email and password required"}. SECURITY: the response body contains the account's own long-lived API token in clear text - anything that receives this action's output receives the credential, so do not log or forward it. |
| Create Panel | `createPanel` | Create a TRIGGERcmd panel - a named board that panel buttons are grouped into. Set public to true to make the panel shareable through a public link. Returns the created panel in data, with its id, and message 'Created successfully.'. NOTE: TRIGGERcmd's REST API has no panel delete route; a panel is removed from the TRIGGERcmd website under Panels &gt; Delete (GET /user/panel/delete?id=...), which needs a signed-in browser session. |
| Create Panel Button | `createPanelButton` | Add a button to a panel. A panel button points at a command on a computer so it can be pressed from a panel or through Trigger Panel Button. Requires an existing panel and an existing command; TRIGGERcmd answers 403 {"message":"Error creating panel button."} when either is missing or not yours. Creating a button does not press it. |
| Delete Command | `deleteCommand` | Delete a command by id. Returns 200 with the deleted record in data; an id that matches nothing returns 200 {"data":[],"message":"No Record found."}. This is the only delete route TRIGGERcmd exposes on its REST API. |
| Delete Run | `deleteRun` | Delete a run record from your TRIGGERcmd run history by id. KNOWN VENDOR FAULT: as of September 2026 this route answers 502 from TRIGGERcmd's nginx front end for every request shape tested (empty body, id, run), so it currently cannot complete. It is included because the route exists and is expected to be repaired vendor-side. |
| Get Pair Code | `getPairCode` | Start TRIGGERcmd's device pairing flow. Returns a short pairCode to show the user and a pairToken to poll Look Up Pair Token with. The user has 10 minutes to sign in at triggercmd.com, open their name menu &gt; Pair, and type the pairCode; once they do, Look Up Pair Token returns that account's API token. This is how the tcmd CLI obtains a token without asking for a password. |
| List Command Runs | `listRuns` | List the run history for your TRIGGERcmd account - one record per time a command was triggered, with its result. Returns records, queryRecordCount, totalRecordCount and perPage (10 per page). Read-only: it does not run anything. |
| List Commands | `listCommands` | List every command defined across the computers on your TRIGGERcmd account. Optionally filter by command name with the 'name' query parameter. Returns a records array (each with the command id, name, voice trigger phrase, owning computer and allowParams flag) plus queryRecordCount. Read-only: listing a command does not run it. |
| List Computers | `listComputers` | List the computers registered on your TRIGGERcmd account. Optionally filter by computer name with the 'name' query parameter. Returns a records array of computer objects (id, name, computerIdentifier, online status, etc.) plus queryRecordCount. Read-only and safe: it runs nothing on any machine. |
| List Panel Buttons | `listPanelButtons` | List the panel buttons on your TRIGGERcmd account. Each button belongs to a panel and points at a command on a computer. Optionally filter by button name with the 'name' query parameter. Returns records, queryRecordCount, totalRecordCount and perPage. Read-only: listing a button does not press it. |

<details>

<summary>See 13 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Panels | `listPanels` | List the panels on your TRIGGERcmd account. A panel is a saved board of buttons, each button bound to a command. Optionally filter by panel name with the 'name' query parameter. Returns records, queryRecordCount, totalRecordCount and perPage. Read-only. |
| List Public Panel Buttons | `listPublicPanelButtons` | List the buttons on a TRIGGERcmd public panel. Takes the public panel identifier from the panel's shared link (not the panel's internal 24-character id, which TRIGGERcmd re-encodes and rejects). Returns records, queryRecordCount, totalRecordCount and perPage; a panel identifier TRIGGERcmd cannot resolve comes back as 200 with an 'error' field such as 'No panel with ID: ...' or 'Bad panel param', so check that field before using the records. Read-only. |
| Look Up Pair Token | `lookupPairToken` | Poll a pairing attempt started by Get Pair Code. Pass the pairToken it returned. While the user has not yet typed the pair code, returns 200 {"message":"No user authorized that pair code yet."}; once they have, it returns that account's API token. An expired or wrong pairToken returns 401 {"err":"Invalid Token!"}. This action deliberately uses the No Auth method: TRIGGERcmd's /pair/lookup handler returns 502 when any Authorization header is present, so the pairToken must travel only in the query string. SECURITY: on success the response carries a TRIGGERcmd account credential - do not log or forward it. |
| MCP Initialize Session | `mcpInitialize` | Open a session against TRIGGERcmd's hosted Model Context Protocol server at https://www.triggercmd.com/mcp and read back its protocol version, capabilities and server info. The MCP endpoint accepts the same TRIGGERcmd API token as a Bearer token that the REST API uses, as well as an OAuth 2.0 access token with the mcp:read / mcp:execute scopes. Read-only handshake - it runs nothing. |
| MCP List Tools | `mcpListTools` | List the tools TRIGGERcmd's hosted MCP server exposes for your account: list_commands, run_command, and one dynamic tool named run_(computer)_(command) per command that has an MCP Tool Description set. Returns a JSON-RPC result with a tools array; the array is empty when the account has no commands. Read-only - listing tools runs nothing. |
| Run Command By Id | `runCommandById` | DANGER - THIS EXECUTES A REAL COMMAND ON A REAL MACHINE. Creates a run for a command addressed by its 24-character id (rather than by computer and command name, as Trigger Command does) and dispatches it to the TRIGGERcmd agent. A command id that no longer exists returns 401 {"err":"This command has been deleted."}; an empty body returns 500. |
| Save Command | `saveCommand` | Create a command on one of your registered computers. A command is a shell command line that the TRIGGERcmd agent on that computer will run when the command is triggered. Requires an existing computer: pass its id in computer. Creating a command does not run it. |
| Save Computer | `saveComputer` | Register a new computer on your TRIGGERcmd account, or update an existing one by passing its id. Returns the computer record in data plus message 'Created successfully.'. CAUTION: a registered computer is the target that commands run on; only the TRIGGERcmd agent installed on that machine can actually execute anything. TRIGGERcmd's REST API has NO computer delete route - a computer is removed from the TRIGGERcmd website under Computers &gt; Delete (GET /user/computer/delete?id=...), which needs a signed-in browser session. |
| Trigger Command | `triggerCommand` | DANGER - THIS EXECUTES A REAL COMMAND ON A REAL MACHINE. Sends a trigger to the TRIGGERcmd agent on the named computer, which runs the named command's command line. Identify the computer and command by name (as shown by List Computers and List Commands), not by id. Leave computer empty to use your default computer. params is appended to the command line when the command has allowParams enabled. Returns immediately without waiting for the command to finish - use Trigger Command And Wait for the result. An unknown computer returns 401 {"error":"Computer not found. Query: {...}"}. |
| Trigger Command And Wait | `triggerCommandAndWait` | DANGER - THIS EXECUTES A REAL COMMAND ON A REAL MACHINE. Same as Trigger Command, but waits for the TRIGGERcmd agent to report back and returns the run record with the command's output and exit status. This is the endpoint the tcmd CLI uses. An unknown computer returns 401 {"error":"Computer not found. Query: {...}"}. |
| Trigger Panel Button | `triggerPanelButton` | DANGER - THIS EXECUTES A REAL COMMAND ON A REAL MACHINE. Presses a button on one of your panels, which runs the command that button is bound to. Both panel and button are names. Omitting either returns 404 {"message":"Both button and panel must be specified."}. |
| Trigger Public Panel Button | `triggerPublicPanelButton` | DANGER - THIS EXECUTES A REAL COMMAND ON A REAL MACHINE. Presses a button on a TRIGGERcmd public panel, which runs the command that button is bound to on the panel owner's computer. Omitting either value returns 404 {"error":"Both button and panel must be specified."}. |
| Update Command | `updateCommand` | Update an existing command by id - change its name, command line, voice trigger or parameter settings. Returns the updated record. An unknown id returns 404 {"err":"No Record found."}. Updating a command does not run it. |

</details>
