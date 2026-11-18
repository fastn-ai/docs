---
description: "Read, write, and manage Google Sheets spreadsheets via the Sheets API v4."
hidden: true
---

# Google Sheets

<img src="../../.gitbook/assets/connectors/lg/google-sheets.png" alt="Google Sheets logo">

Read, write, and manage Google Sheets spreadsheets via the Sheets API v4. Supports spreadsheet creation, sheet tab management, cell value operations, named ranges, and batch updates.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [sheets.google.com](https://sheets.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleSheets` |

## Use it

Add Google Sheets from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleSheets.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Named Range</td><td><code>addNamedRange</code></td><td>Create a named range in a spreadsheet for easy cell range referencing.</td></tr><tr><td>Add Sheet</td><td><code>addSheet</code></td><td>Add a new sheet tab to an existing spreadsheet.</td></tr><tr><td>Append Values</td><td><code>appendValues</code></td><td>Append rows to a spreadsheet after the last row with data in the given range.</td></tr><tr><td>Batch Clear Values</td><td><code>batchClearValues</code></td><td>Clear values from multiple ranges in a single request.</td></tr><tr><td>Batch Clear Values By Data Filter</td><td><code>batchClearValuesByDataFilter</code></td><td>Clears one or more ranges of values selected by the supplied dataFilters. Only values are cleared; formatting and other properties are preserved.</td></tr><tr><td>Batch Get Values</td><td><code>batchGetValues</code></td><td>Read values from multiple ranges in a single request.</td></tr><tr><td>Batch Get Values By Data Filter</td><td><code>batchGetValuesByDataFilter</code></td><td>Returns one or more ranges of values matched by the supplied dataFilters, with control over major dimension and value/date rendering.</td></tr><tr><td>Batch Update Spreadsheet</td><td><code>batchUpdateSpreadsheet</code></td><td>Generic power action: applies one or more update Requests to the spreadsheet atomically (addSheet, deleteSheet, updateCells, formatting, charts, etc.). Pass a bare requests array. The specific addSheet/deleteSheet actions wrap single request types.</td></tr><tr><td>Batch Update Values</td><td><code>batchUpdateValues</code></td><td>Write values to multiple ranges in a single request.</td></tr><tr><td>Batch Update Values By Data Filter</td><td><code>batchUpdateValuesByDataFilter</code></td><td>Sets values in one or more ranges selected by dataFilters. Each data entry pairs a dataFilter with the values to write and the major dimension.</td></tr></tbody></table>

<details>

<summary>View 15 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Clear Values</td><td><code>clearValues</code></td><td>Clear all values in a specific range of a spreadsheet, leaving formatting intact.</td></tr><tr><td>Copy Sheet To</td><td><code>copySheetTo</code></td><td>Copy a sheet tab from one spreadsheet to another spreadsheet.</td></tr><tr><td>Create Spreadsheet</td><td><code>createSpreadsheet</code></td><td>Create a new Google Sheets spreadsheet with a given title.</td></tr><tr><td>Delete Named Range</td><td><code>deleteNamedRange</code></td><td>Delete a named range from a spreadsheet by its ID.</td></tr><tr><td>Delete Sheet</td><td><code>deleteSheet</code></td><td>Delete a sheet tab from a spreadsheet by its sheetId (numeric ID, not title).</td></tr><tr><td>Duplicate Sheet</td><td><code>duplicateSheet</code></td><td>Duplicate an existing sheet tab within the same spreadsheet.</td></tr><tr><td>Get Developer Metadata</td><td><code>getDeveloperMetadata</code></td><td>Returns the developer metadata with the specified ID from the given spreadsheet.</td></tr><tr><td>Get Spreadsheet</td><td><code>getSpreadsheet</code></td><td>Get full spreadsheet metadata including all sheet tabs, named ranges, and properties.</td></tr><tr><td>Get Spreadsheet By Data Filter</td><td><code>getSpreadsheetByDataFilter</code></td><td>Returns the spreadsheet at the given ID, selecting subsets of data via dataFilters (a1Range, gridRange, or developerMetadataLookup). Optionally includes grid cell data.</td></tr><tr><td>Get Values</td><td><code>getValues</code></td><td>Read cell values from a specific range in a spreadsheet. Range format: 'Sheet1!A1:B10'.</td></tr><tr><td>Rename Sheet</td><td><code>renameSheet</code></td><td>Rename a sheet tab by its sheetId.</td></tr><tr><td>Search Developer Metadata</td><td><code>searchDeveloperMetadata</code></td><td>Returns all developer metadata matching the criteria described by the supplied dataFilters (developerMetadataLookup, a1Range, or gridRange).</td></tr><tr><td>TEMP watch spreadsheet check (delete me)</td><td><code>tempWatchSpreadsheetCheck</code></td><td>Temporary B185 probe: can a Sheets connection open a Drive watch channel on a spreadsheet. Delete after the check.</td></tr><tr><td>Update Named Range</td><td><code>updateNamedRange</code></td><td>Update the name or cell range of an existing named range.</td></tr><tr><td>Update Values</td><td><code>updateValues</code></td><td>Write values to a specific range in a spreadsheet, overwriting existing data.</td></tr></tbody></table>

</details>
