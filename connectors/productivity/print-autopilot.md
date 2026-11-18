---
description: "Print Autopilot (printautopilot.com) automatically prints PDF documents on your own remote printers."
---

# Print Autopilot

Print Autopilot (printautopilot.com) automatically prints PDF documents on your own remote printers. Send a PDF to a print queue over the REST API and a desktop print client picks it up and prints it on the configured printer and paper size. This connector covers the account/queue API (add a document to a print queue, read the account) and the Print App API used by the desktop client (register printers, poll pending print jobs, report results, check client version). Billing is pay-as-you-go per printed document.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [printautopilot.com](https://printautopilot.com) |
| **Authentication** | API key |
| **Actions** | 7 |
| **Events** | 0 |
| **Slug** | `printAutopilot` |

## Use it

Add Print Autopilot from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.printAutopilot.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Document To Print Queue | `addDocumentToPrintQueue` | Upload a base64-encoded PDF to the print queue that the API token belongs to. The document is picked up by the Print Autopilot desktop client and PHYSICALLY PRINTED on the queue's printer, and each accepted document consumes one paid credit (from EUR 0.015). Returns 202 with {"status":"ok"} on acceptance. Print Autopilot does NOT validate the base64 payload, so verify it yourself. Only one document per call is supported. Returns 400 {"status":"Base64 not set"} when base64 is empty. |
| Check Print Client Version | `checkPrintClientVersion` | Report the running semantic version of the Print Autopilot desktop print client and find out whether a newer self-update is available. The vendor documents this route as usable only by their own Windows client application. It is a Print App API route: it requires a connection authenticated with the Print Client Connection Token, not the print queue API token. |
| Get Account | `getAccount` | Retrieve the Print Autopilot account that the print queue API token belongs to, including the account id, display name, email address, team id, avatar URL and creation timestamp. Useful as a connection health check because it needs no input. Undocumented in the vendor's Postman collection but live and stable. |
| Get Token Context | `getTokenContext` | Return the records associated with the print queue API token currently in use. Undocumented in the vendor's Postman collection but live and authenticated. The raw response body is a JSON array, which is empty on an account whose queue has no associated records yet. Use Get Account for a richer connection health check. |
| List Pending Print Jobs | `listPendingPrintJobs` | Poll the print jobs waiting for this print client, each with its target printer, paper size, scaling percentage and the queued documents as base64 PDFs. This is the route the Print Autopilot desktop client polls. It is a Print App API route: it requires a connection authenticated with the Print Client Connection Token, not the print queue API token. Report the outcome of each document afterwards with Report Print Job Result. |
| Register Printer | `registerPrinter` | Register a printer and its supported paper sizes so it can be selected when creating a print queue in the Print Autopilot dashboard. This is a Print App API route: it requires a connection authenticated with the Print Client Connection Token, not the print queue API token. Returns 201 with {"message":"Printers created"}. |
| Report Print Job Result | `reportPrintJobResult` | Mark a queued document as printed or failed after the print client has handled it, so it leaves the pending queue and appears in the document history. This is a Print App API route: it requires a connection authenticated with the Print Client Connection Token, not the print queue API token. Returns 200 with {"message":"Documents updated"}. |
