---
description: "Zoho Sheet online spreadsheet application, part of the Zoho suite."
hidden: true
---

# Zoho Sheet

<img src="../../.gitbook/assets/connectors/zoho-sheet.png" alt="Zoho Sheet logo" width="64">

Zoho Sheet online spreadsheet application, part of the Zoho suite. Programmatic access via Zoho Sheet Data APIs (sheet.zoho.com/api/v2) to manage workbooks, worksheets, tabular data, charts, pivot tables, cell/range content, formatting, named ranges, picklists, data validation, merge templates and premium high-throughput record APIs. OAuth 2.0 authorization code auth via the shared Zoho API Console app.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [sheet.zoho.com](https://sheet.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zohoSheet` |

## Use it

Add Zoho Sheet from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoSheet.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Records (High Throughput) | `premiumAddRecords` | Premium high-throughput append of a single row to a worksheet, keyed by column header. Only one row can be added per call, and this endpoint does not recalculate formula cells or refresh pivot tables — use Recalculate afterwards if needed. |
| Add Records to Table | `addRecordsToTable` | Add JSON-formatted records to a Table. Records are appended after the last row of the table by default; keys must match the table's column headers. |
| Add Records to Worksheet | `addRecordsToWorksheet` | Add JSON records to a worksheet, appended after the last used row. Max 1000 rows per call. |
| Append Rows with CSV Data | `appendRowsCsv` | Insert CSV data to a worksheet, appended after the last used row. Each comma moves to the next cell and each newline moves to the next row. |
| Append Rows with JSON Data | `appendRowsJson` | Insert data to a worksheet as JSON. The data is appended after the last used row of the worksheet. The key of each JSON object represents the column header of the worksheet. A maximum of 1000 rows can be added in a single call. |
| Apply Picklist to Range | `applyPicklistToRange` | Apply a picklist to one or more cell ranges. Supply the options explicitly via Picklist Items or derive them from a source range via Source Ranges — exactly one of the two is required. |
| Clear Conditional Format from Range | `clearConditionalFormatFromRange` | Clear the conditional formatting rules covering a given range on a worksheet. |
| Clear Contents of Range | `clearContentsOfRange` | Clear only the contents of a range. Any style or format applied to the range remains intact. |
| Clear Data Validation from Range | `clearDataValidationFromRange` | Clear data validation rules from one or more ranges on a worksheet. |
| Clear Filters | `clearFilters` | Reset or clear all applied filters in a worksheet. |

<details>

<summary>See 110 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Clear Range | `clearRange` | Clear everything in a range, including style, format, and content. |
| Clone Chart | `cloneChart` | Duplicate an existing chart. The clone is placed on the same worksheet as the original and its new chart id is returned. |
| Convert Index to Range | `convertIndexToRange` | Convert start row, start column, end row, and end column indexes into an A1-style range address such as A1:D3. |
| Convert Range to Index | `convertRangeToIndex` | Convert an A1-style range address such as A1:D3 into its start row, start column, end row, and end column indexes. |
| Copy Pivot Table | `copyPivotTable` | Copy an existing pivot table to a new sheet or to a chosen position on an existing sheet. The copy keeps the original's source data, fields, filters, and settings. |
| Copy Workbook | `copyWorkbook` | Make a new copy of an existing workbook. |
| Copy Worksheet (New Workbook) | `copyWorksheetNewWorkbook` | Copy a worksheet and use it to create a brand-new workbook. |
| Copy Worksheet (Other Workbook) | `copyWorksheetOtherWorkbook` | Copy a worksheet from another (source) workbook into this (destination) workbook. |
| Copy Worksheet (Same Workbook) | `copyWorksheetSameWorkbook` | Copy or duplicate a worksheet within the same workbook. |
| Create Named Range | `createNamedRange` | Create an absolute named range over a cell range on a worksheet. Named expressions are not supported through the API. |
| Create Pivot Chart | `createPivotChart` | Create a pivot chart from an existing pivot table. The chart is placed on the same sheet as the pivot table. Scatter, racebar, scatterLine, scatterLineMarkers, bubble, ohlc, candleStick, polar, spiderWeb and box plot types are not supported for pivot charts. |
| Create Pivot Table | `createPivotTable` | Create a pivot table from a source table, named range, or cell range, placing it on a new sheet or at a chosen position on an existing sheet. |
| Create Table | `createTable` | Create a new formal Table object over a range of cells in a worksheet, with optional table style/properties. Table style templates: LIGHT1, LIGHT2, LIGHT3, MEDIUM1, MEDIUM2, MEDIUM3, MEDIUM4, MEDIUM5, DARK1. |
| Create Workbook | `createWorkbook` | Create a new, blank Zoho Sheet workbook with the given name. Returns the new workbook's resource_id, which most other actions need. |
| Create Workbook From Template | `createWorkbookFromTemplate` | Create a new workbook from an existing template. |
| Create Workbook Version | `createWorkbookVersion` | Create a new named version snapshot of a workbook. |
| Create Worksheet | `createWorksheet` | Add a new worksheet into a workbook. If no name is provided, Zoho Sheet assigns a default name such as Sheet2, Sheet3, etc. |
| Delete Charts | `deleteCharts` | Delete one or more charts from the workbook. The call fails if any supplied chart id is invalid or inaccessible. Maximum 10 charts per call. |
| Delete Column | `deleteColumn` | Delete a single column from a worksheet by its column index. |
| Delete Columns from Table | `deleteColumnsFromTable` | Delete one or more columns from a Table by header name. |
| Delete Multiple Worksheets | `deleteMultipleWorksheets` | Delete multiple worksheets from a workbook in one call. The workbook must have more worksheets than the number being deleted, or the API returns an error. |
| Delete Named Range | `deleteNamedRange` | Delete an existing named range from the workbook. |
| Delete Pivot Charts | `deletePivotCharts` | Delete pivot charts from the workbook. Supply either specific chart IDs (maximum 10) or a worksheet to remove every pivot chart on it — the two modes are mutually exclusive. The call fails if any supplied id is invalid or is not a pivot chart. |
| Delete Pivot Tables | `deletePivotTables` | Delete pivot tables from the workbook. Supply either a list of pivot table names or a worksheet (optionally narrowed by range) — the two modes are mutually exclusive. |
| Delete Records from Table | `deleteRecordsFromTable` | Delete records from a Table that match criteria_json. Supported operators: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS, GREATER_THAN, LESS_THAN, IS_EMPTY, IS_NOT_EMPTY, IN, NOT_IN. Use criteria_pattern when combining more than one criterion. |
| Delete Records from Worksheet | `deleteRecordsFromWorksheet` | Delete/erase worksheet records matching a criteria expression. By default only erases data; set deleteRows=true to remove the rows entirely. |
| Delete Row | `deleteRow` | Delete a single row from a worksheet by its row index. |
| Delete Rows | `deleteRows` | Delete multiple discontinuous row ranges from a worksheet in one call. |
| Delete Workbook | `deleteWorkbook` | Permanently delete up to 10 workbooks from the trash. This cannot be undone. |
| Delete Worksheet | `deleteWorksheet` | Delete an existing worksheet from a workbook. The workbook must have more than one worksheet, or the API returns an error. |
| Download Workbook | `downloadWorkbook` | Download an existing workbook, worksheet, or range as xlsx, csv, tsv, ods, or pdf. |
| Edit Pivot Table | `editPivotTable` | Edit an existing pivot table's name, field layout, data source, grouping, settings, and visual theme. Field arrays that are omitted keep their current values; pass an empty array to clear one. |
| Export Charts | `exportCharts` | Retrieve chart images as Base64-encoded strings. Supply chart IDs for specific charts, a worksheet for every chart on that sheet, or neither to export every chart in the workbook. |
| Fetch Records (High Throughput) | `premiumFetchRecords` | Premium high-throughput read of worksheet records with optional criteria filtering. A maximum of 200 records is returned per call. Uses the dedicated fetchrecords endpoint rather than the standard method dispatcher. |
| Fetch Records from Table | `fetchRecordsFromTable` | Fetch records from a formal Table, optionally filtered by criteria_json (e.g. [{"key":"Month","operator":"EQUALS","matcher":"March","type":"String"}]). Supported operators: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS, GREATER_THAN, LESS_THAN, IS_EMPTY, IS_NOT_EMPTY, IN, NOT_IN. Use criteria_pattern (e.g. "1 AND 2") when combining more than one criterion. Maximum 5 criteria. |
| Fetch Records from Worksheet | `fetchRecordsFromWorksheet` | Fetch records from a plain worksheet (first row treated as header by default), optionally filtered by criteria, e.g. "Month"="March" and "Amount"&gt;50. Max 5 nested criteria. |
| Filter Pivot Table | `filterPivotTable` | Apply filters to one or more fields of a pivot table in a single request, using a members filter, a label filter, a value filter, or clearing an existing filter. |
| Find | `findInWorkbook` | Search for a string in a workbook, worksheet, row, or column. |
| Find and Replace | `findAndReplace` | Search for a term in a workbook, worksheet, row, or column, and replace it with the given string. |
| Format Ranges | `formatRanges` | Add or edit the text and cell-level formats of one or more ranges, covering font, colour, alignment, borders, number and currency formats, sizing and cell merging. |
| Freeze Panes | `freezePanes` | Freeze or unfreeze rows and/or columns of a worksheet so they stay visible while scrolling. |
| Get Content of Cell | `getContentOfCell` | Get the content and note of a particular cell. Style or formats applied on the cell are not provided. |
| Get Content of Named Range | `getContentOfNamedRange` | Get the contents of a named range. Style or formats applied on the cells are not provided. |
| Get Content of Range | `getContentOfRange` | Get the contents of a range of cells. Style or formats applied on the cells are not provided. |
| Get Content of Worksheet | `getContentOfWorksheet` | Get the complete contents of a worksheet. Style or formats applied on the cells are not provided. Can be scoped to a sub-range and rendered as an array via response_type/major_dimension. |
| Get Merge Fields | `getMergeFields` | List every merge field defined in a workbook, with each field's name and id. |
| Get Merge Job Details | `getMergeJobDetails` | Get the details of a single merge job, including the file produced for each merged record. |
| Get Merge Jobs | `getMergeJobs` | List every merge job that has been run against a merge template workbook. |
| Get Merge Templates | `getMergeTemplates` | List every merge template the authenticated user owns or has been given access to. |
| Get Pivot Data | `getPivotData` | Retrieve an aggregate value from a pivot table. Optionally narrow it to specific field and item combinations, otherwise the grand total for the data field is returned. |
| Get Used Area | `getUsedArea` | Get the count of the used area of a worksheet: the row and column up to which the worksheet contains data. Cells with only formatting/style but no data are not counted. |
| Insert Chart | `insertChart` | Create a new chart on a worksheet from one or more data sources, choosing the chart type and optionally its top-left position and initial visual metadata. Returns the new chart's id. |
| Insert Checkbox | `insertCheckbox` | Insert checkboxes into a range of a worksheet. Checkboxes are inserted only into eligible cells within the range. |
| Insert Column | `insertColumn` | Insert a new column after a given column index on a worksheet. The new column's cells use the default formats. |
| Insert Columns to Records | `insertColumnsToRecords` | Insert one or more new column headers into a worksheet's header row. |
| Insert Columns to Table | `insertColumnsToTable` | Append one or more columns with headers to a Table. Headers are added to the header row. |
| Insert Images | `insertImages` | Insert images into a workbook, either uploading a new image file or reusing an image already in the account's image library via image_id. |
| Insert Row | `insertRow` | Insert a new row at a given row index on a worksheet and optionally populate it from JSON data keyed by the worksheet's column headers. The new row's cells use the default formats. |
| Insert Row with JSON Data | `insertRowJson` | Insert a new row at the given row index with the specified data. The key of each JSON object represents the column header. The new row inherits the format of the previous row's cells. |
| List Charts | `listCharts` | List every chart in the workbook grouped by worksheet name, including each chart's id, published state, public chart name, and top-left row and column position. |
| List Conditional Formats | `listConditionalFormats` | List the conditional formatting rules in a workbook. Supply a worksheet to list every rule on it, or a worksheet plus all four range indices to list only the rules intersecting that range. Each entry carries whichever rules object matches its format type. |
| List Named Ranges | `listNamedRanges` | List every named range defined in the workbook, with the worksheet it belongs to and its cell range as both A1 notation and row/column indexes. |
| List Picklists | `listPicklists` | List every picklist in the workbook with its applied ranges and items. Optionally filter to the picklists intersecting a given worksheet range. |
| List Pivot Charts | `listPivotCharts` | List the pivot charts in the workbook with their chart id, chart type, the pivot table they belong to, and their worksheet. Optionally restrict to a single worksheet. |
| List Pivot Tables | `listPivotTables` | List the pivot tables in the workbook with their source and target ranges. Optionally restrict to a worksheet, or to pivot tables whose target range falls inside a given range. |
| List Tables | `listTables` | List all Tables defined in the workbook along with their table IDs and cell ranges. |
| List Templates | `listTemplates` | List all spreadsheet templates owned by the authenticated user. |
| List Workbook Versions | `listWorkbookVersions` | List all saved versions of a workbook. |
| List Workbooks | `listWorkbooks` | List all workbooks (owned or shared) that the authenticated user can access. Supports pagination via start_index and count, and sorting via sort_option. |
| List Worksheets | `listWorksheets` | List all worksheets of a workbook, along with their worksheet IDs. |
| Lock Worksheet or Range | `lockWorksheetOrRange` | Lock a worksheet or a selected range of a workbook for specific shared users or external share links. |
| Merge and Email as Attachment | `mergeAndEmailAsAttachment` | Run a mail merge over a merge template and email each generated document as an attachment. The documents are sent but not saved. Returns the merge job id, which starts in the initiated state. |
| Merge and Save | `mergeAndSave` | Run a mail merge over a merge template and store each generated document in Zoho WorkDrive. Returns the merge job id, which starts in the initiated state. |
| Move Chart | `moveChart` | Move a chart to another worksheet within the same workbook. |
| Move Pivot Table | `movePivotTable` | Move an existing pivot table to a new sheet or to a chosen position on an existing sheet. |
| Publish Charts | `publishCharts` | Publish one or more charts and return a unique publish key per chart. Each key can be appended to the public charts URL to reach the published chart page. Maximum 10 charts per call. |
| Publish Workbook | `publishWorkbook` | Publish a workbook, a single worksheet, or a range of a worksheet as a public web page. |
| Read Data Validation in Cell | `readDataValidationInCell` | Read the data validation rule applied to a single cell. When the cell has no validation, only the standard success fields are returned; the operator field appears only for criteria types that use one. |
| Recalculate | `recalculate` | Recalculate formula cells in the workbook. Use after Premium API add/update record calls, since those do not recalculate formulas automatically. |
| Refresh Pivot Tables | `refreshPivotTables` | Refresh pivot tables against their source data. Supply either a list of pivot table names or a worksheet (optionally narrowed by range) — the two modes are mutually exclusive. |
| Remove Picklist from Range | `removePicklistFromRange` | Remove the picklist from one or more cell ranges. |
| Remove Publish | `removePublish` | Unpublish a previously published workbook, worksheet, or range. |
| Remove Table | `removeTable` | Remove a Table object definition. Optionally also clears the table's formats. Does not delete the underlying cell data. |
| Rename Table Headers | `renameTableHeaders` | Rename one or more header values of a Table. |
| Rename Worksheet | `renameWorksheet` | Rename an existing worksheet. The worksheet ID stays the same after renaming. |
| Restore Workbook | `restoreWorkbook` | Restore up to 10 workbooks from the trash. |
| Revert Workbook Version | `revertWorkbookVersion` | Revert a workbook to an earlier saved version. |
| Set Column Width | `setColumnWidth` | Set the width of one or more discontinuous column ranges on a worksheet, or auto-fit them to their cell data. |
| Set Conditional Format to Range | `setConditionalFormatToRange` | Apply a conditional formatting rule to one or more ranges on a worksheet. Choose the format type, then supply the matching rules object for classic rules, a colour scale, a data bar, or an icon set. |
| Set Content to Cell | `setContentToCell` | Add content to a particular cell in a specified worksheet. |
| Set Content to Multiple Cells | `setContentToMultipleCells` | Add content to multiple discontinuous cells in one call. Up to 50 cells can be updated per call. |
| Set Content to Range | `setContentToRange` | Insert CSV data into a worksheet starting at a specified cell reference. Overwrites any existing content in the target cells with the inserted CSV data. |
| Set Content to Row | `setContentToRow` | Update a few discrete columns of a particular row. column_array holds the column indices to update and data_array holds the matching values; both arrays must be the same length. |
| Set Data Validation to Range | `setDataValidationToRange` | Apply a data validation rule to one or more ranges on a worksheet, with an optional input hint and error alert. |
| Set Image Fit Options | `setImageFitOptions` | Change the image fit option for every in-cell image in a range on a worksheet. Images placed over cells rather than inside them are unaffected. |
| Set Note to Cell | `setNoteToCell` | Attach a note to a single cell on a worksheet, identified by its row and column index. |
| Set Row Height | `setRowHeight` | Set the height of one or more discontinuous row ranges on a worksheet, or auto-fit them to their cell data. |
| Share Workbook | `shareWorkbook` | Share a workbook with one or more users at a given access level (share, edit, view_and_comment, view, or remove_share). |
| Sort Pivot Table | `sortPivotTable` | Sort one or more pivot table fields in a single request, either alphabetically by field label or by the values of a chosen data field. |
| Trash Workbook | `trashWorkbook` | Move up to 10 workbooks to the trash. |
| Unlock Worksheet or Range | `unlockWorksheetOrRange` | Unlock a previously locked worksheet or range for specific shared users or external share links. |
| Unpublish Charts | `unpublishCharts` | Revoke public access to previously published charts. The associated publish keys become invalid and the charts are no longer reachable at the public charts URL. Maximum 10 charts per call. |
| Update Chart | `updateChart` | Update a chart's metadata in a single call, covering chart-level appearance (chartMeta) and sheet-level placement and data-table options (sheetMeta). |
| Update Named Range | `updateNamedRange` | Update the source cell range that an existing named range points to. |
| Update Pivot Chart | `updatePivotChart` | Update the metadata of a pivot chart, covering chart-level appearance and sheet-level placement. The chart id must belong to a pivot chart. |
| Update Records (High Throughput) | `premiumUpdateRecords` | Premium high-throughput update of up to 10 worksheet rows, selected either by criteria or by row index. This endpoint does not recalculate formula cells or refresh pivot tables — use Recalculate afterwards if needed. |
| Update Records in Table | `updateRecordsInTable` | Update records in a Table that match criteria_json with the given data. Supported operators: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS, GREATER_THAN, LESS_THAN, IS_EMPTY, IS_NOT_EMPTY, IN, NOT_IN. Use criteria_pattern when combining more than one criterion. |
| Update Records in Worksheet | `updateRecordsInWorksheet` | Update worksheet records matching a criteria expression, e.g. "Month"="March". If no criteria, all rows are updated. |
| Update Rows with JSON Data | `updateRowsJson` | Update multiple discontinuous rows by row index. The key of each JSON object represents the column header; each object must include row_index. |
| Upload Workbook | `uploadWorkbook` | Import a spreadsheet file (.xls, .xlsm, .csv, .tsv, .sxc, .ods, max 10MB) from a URL into a new Zoho Sheet workbook, or insert it as new worksheets into an existing workbook. |

</details>
