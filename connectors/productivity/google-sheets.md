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

| Action | Slug | What it does |
| --- | --- | --- |
| Add Named Range | `addNamedRange` | Create a named range in a spreadsheet for easy cell range referencing. |
| Add Sheet | `addSheet` | Add a new sheet tab to an existing spreadsheet. |
| Append Values | `appendValues` | Append rows to a spreadsheet after the last row with data in the given range. |
| Batch Clear Values | `batchClearValues` | Clear values from multiple ranges in a single request. |
| Batch Clear Values By Data Filter | `batchClearValuesByDataFilter` | Clears one or more ranges of values selected by the supplied dataFilters. Only values are cleared; formatting and other properties are preserved. |
| Batch Get Values | `batchGetValues` | Read values from multiple ranges in a single request. |
| Batch Get Values By Data Filter | `batchGetValuesByDataFilter` | Returns one or more ranges of values matched by the supplied dataFilters, with control over major dimension and value/date rendering. |
| Batch Update Spreadsheet | `batchUpdateSpreadsheet` | Generic power action: applies one or more update Requests to the spreadsheet atomically (addSheet, deleteSheet, updateCells, formatting, charts, etc.). Pass a bare requests array. The specific addSheet/deleteSheet actions wrap single request types. |
| Batch Update Values | `batchUpdateValues` | Write values to multiple ranges in a single request. |
| Batch Update Values By Data Filter | `batchUpdateValuesByDataFilter` | Sets values in one or more ranges selected by dataFilters. Each data entry pairs a dataFilter with the values to write and the major dimension. |

<details>

<summary>See 15 more actions</summary>

* **Clear Values** `clearValues`: Clear all values in a specific range of a spreadsheet, leaving formatting intact.
* **Copy Sheet To** `copySheetTo`: Copy a sheet tab from one spreadsheet to another spreadsheet.
* **Create Spreadsheet** `createSpreadsheet`: Create a new Google Sheets spreadsheet with a given title.
* **Delete Named Range** `deleteNamedRange`: Delete a named range from a spreadsheet by its ID.
* **Delete Sheet** `deleteSheet`: Delete a sheet tab from a spreadsheet by its sheetId (numeric ID, not title).
* **Duplicate Sheet** `duplicateSheet`: Duplicate an existing sheet tab within the same spreadsheet.
* **Get Developer Metadata** `getDeveloperMetadata`: Returns the developer metadata with the specified ID from the given spreadsheet.
* **Get Spreadsheet** `getSpreadsheet`: Get full spreadsheet metadata including all sheet tabs, named ranges, and properties.
* **Get Spreadsheet By Data Filter** `getSpreadsheetByDataFilter`: Returns the spreadsheet at the given ID, selecting subsets of data via dataFilters (a1Range, gridRange, or developerMetadataLookup). Optionally includes grid cell data.
* **Get Values** `getValues`: Read cell values from a specific range in a spreadsheet. Range format: 'Sheet1!A1:B10'.
* **Rename Sheet** `renameSheet`: Rename a sheet tab by its sheetId.
* **Search Developer Metadata** `searchDeveloperMetadata`: Returns all developer metadata matching the criteria described by the supplied dataFilters (developerMetadataLookup, a1Range, or gridRange).
* **TEMP watch spreadsheet check (delete me)** `tempWatchSpreadsheetCheck`: Temporary B185 probe: can a Sheets connection open a Drive watch channel on a spreadsheet. Delete after the check.
* **Update Named Range** `updateNamedRange`: Update the name or cell range of an existing named range.
* **Update Values** `updateValues`: Write values to a specific range in a spreadsheet, overwriting existing data.

</details>
