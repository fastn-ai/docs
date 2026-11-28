---
description: "Wolfram|Alpha answers questions with computed results. Get short answers, full results, images and spoken results."
hidden: true
---

# Wolfram\|Alpha

<img src="../../.gitbook/assets/connectors/lg/wolfram-alpha.png" alt="Wolfram\|Alpha logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [wolframalpha.com](https://wolframalpha.com) |
| **Authentication** | App ID |
| **Slug** | `wolframAlpha` |

## Setup

Your customers enter their app id for Wolfram\|Alpha when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Wolfram\|Alpha from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Wolfram\|Alpha**.
2. Select **Connect** on the Wolfram\|Alpha card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Wolfram\|Alpha's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Short Answer</td><td><code>getShortAnswer</code></td><td>Returns a single short plain-text answer for a query, taken from the Result pod of Wolfram|Alpha output. Fails with HTTP 501 when no sufficiently short answer exists.</td></tr><tr><td>Get Simple Image</td><td><code>getSimpleImage</code></td><td>Returns a single static image (GIF) of the complete Wolfram|Alpha result page for a query, with layout, colour, font size and width controls. Does not support disambiguation, drilldown or asynchronous results; use Query Full Results for those. Fails with HTTP 501 when the input cannot be interpreted.</td></tr><tr><td>Get Spoken Result</td><td><code>getSpokenResult</code></td><td>Returns a single result phrased as a full spoken sentence, suitable for text-to-speech delivery. Fails with HTTP 501 when no sufficiently short answer exists.</td></tr><tr><td>Get Summary Box</td><td><code>getSummaryBox</code></td><td>Returns a pre-generated XHTML summary box for an entity or entity property, identified by the summary box path returned by Recognize Query (e.g. countries/e/br/du/gh for France). The XHTML uses wasb-* classes for styling.</td></tr><tr><td>Query Full Results</td><td><code>queryFullResults</code></td><td>Runs a free-form query through the Wolfram|Alpha Full Results API and returns the complete structured result: pods and subpods (plain text, images, MathML and more), assumptions, warnings, sources and suggested pod states. Supports pod selection, location, sizing, timeout, assumption and pod-state controls; step-by-step solutions are requested with a pod state such as Step-by-step solution (subject to the AppID's entitlements). Defaults to JSON output.</td></tr><tr><td>Query LLM API</td><td><code>queryLlmApi</code></td><td>Runs a query through the Wolfram|Alpha LLM API and returns a plain-text response optimised for consumption by large language models: the interpreted input, result, key pods, image links and a link to the full website result. Accepts the Full Results location, unit, sizing and timeout parameters.</td></tr><tr><td>Recognize Query</td><td><code>recognizeQuery</code></td><td>Runs the Fast Query Recognizer to classify an input in a few milliseconds: whether Wolfram|Alpha is likely to answer it, its content domain, a result-significance score and, where available, a summary box path or formula variables. Requires an AppID entitled to the Fast Query Recognizer; other AppIDs receive 401 Not permitted. Defaults to JSON output.</td></tr><tr><td>Validate Query</td><td><code>validateQuery</code></td><td>Runs only the parsing phase of the Full Results API to quickly check whether Wolfram|Alpha can make sense of an input, returning success plus any assumptions, warnings and errors without computing pods. Defaults to JSON output.</td></tr></tbody></table>

