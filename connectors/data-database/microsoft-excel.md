---
description: "Microsoft Excel workbooks stored in OneDrive or SharePoint, via the Microsoft Graph Excel (workbook) API at https://graph.microsoft.com/v1.0."
---

# Microsoft Excel

Microsoft Excel workbooks stored in OneDrive or SharePoint, via the Microsoft Graph Excel (workbook) API at https://graph.microsoft.com/v1.0. Read and write worksheets, cell ranges and their formats, tables with rows and columns, charts and chart formatting, named items, pivot tables, comments, sorting, filtering, worksheet protection and workbook sessions. Every action addresses a workbook by its OneDrive drive item ID under /me/drive/items/{itemId}/workbook. Connect with a Microsoft work, school or personal account using Entra ID OAuth 2.0; the signed-in user needs the delegated Files.ReadWrite permission.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [graph.microsoft.com](https://graph.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 156 |
| **Events** | 0 |
| **Slug** | `microsoftExcel` |

## Use it

Add Microsoft Excel from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.microsoftExcel.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Chart | `addChart` | Creates a chart on a worksheet from a source data range, for example a stacked column chart over "A1:B10". |
| Add Named Item | `addNamedItem` | Creates a workbook-scoped named item that points at a range or formula, for example "=Sheet1!$F$15:$N$27". |
| Add Named Item With Local Formula | `addNamedItemFormulaLocal` | Creates a workbook-scoped named item from a formula written in the user's own language and number-formatting locale, for example "=SUM(Sheet2!$A$1+Sheet2!$A$2)". |
| Add Table | `addTable` | Creates an Excel table over a range of cells. Because the table is created at workbook scope, prefix the address with the sheet name, for example "Sheet1!A1:D4". |
| Add Table Column | `addTableColumn` | Adds a column to an Excel table. Give an index to insert the column at a specific position, shifting the previous column at that position to the right. |
| Add Table Row | `addTableRow` | Appends one or more rows to an Excel table. Supply the values as a two-dimensional array with one inner array per row, matching the table's column count. |
| Add Worksheet | `addWorksheet` | Adds a new worksheet to the end of a workbook. If no name is supplied, Excel generates one automatically. |
| Add Worksheet Named Item | `addWorksheetNamedItem` | Creates a named item scoped to a single worksheet, pointing at a range or formula on that sheet. |
| Add Worksheet Table | `addWorksheetTable` | Creates an Excel table over a range on a specific worksheet. Because the worksheet is named in the path, the address needs no sheet prefix, for example "A1:D4". |
| Apply Table Column Filter | `applyTableColumnFilter` | Applies a filter to one column of an Excel table so only matching rows stay visible. The criteria object selects the filter kind, such as a list of allowed values, a custom comparison, a dynamic date range, or a top or bottom N selection. |
| Apply Table Sort | `applyTableSort` | Sorts the rows of an Excel table using one or more sort fields. Each sort field names a zero-based column index within the table and a sort direction. |
| Autofit Range Columns | `autofitRangeColumns` | Resizes the columns of a range so that each column is wide enough for its longest cell value. |
| Autofit Range Rows | `autofitRangeRows` | Resizes the rows of a range so that each row is tall enough for its tallest cell content. |
| Clear Chart Area Fill | `clearChartAreaFill` | Removes the background fill from the whole chart area. |
| Clear Chart Axis Line Format | `clearChartAxisLineFormat` | Removes the line formatting from one chart axis, returning it to no line. |
| Clear Chart Legend Fill | `clearChartLegendFill` | Removes the background fill from behind a chart's legend. |
| Clear Chart Title Fill | `clearChartTitleFill` | Removes the background fill from behind a chart's title. |
| Clear Range | `clearRange` | Clears a cell range. Choose whether to clear the cell contents, the formatting, or both. |
| Clear Range Fill | `clearRangeFill` | Removes the background fill colour from a cell range, returning it to no fill. |
| Clear Table Column Filter | `clearTableColumnFilter` | Removes the filter applied to one column of an Excel table. |
| Clear Table Filters | `clearTableFilters` | Removes every column filter currently applied to an Excel table, so all rows become visible again. |
| Clear Table Sort | `clearTableSort` | Clears the sort currently defined on an Excel table. The rows keep their present order but the sort is no longer reapplied. |
| Close Workbook Session | `closeWorkbookSession` | Closes an existing Excel workbook session. Supply the session ID returned by Create Workbook Session. |
| Convert Table To Range | `convertTableToRange` | Converts an Excel table back into an ordinary cell range, keeping the data and formatting but removing the table structure. |
| Create Comment Reply | `createCommentReply` | Posts a reply to a workbook comment thread. Choose plain text or mention content depending on how the reply is written. |
| Create Workbook | `createWorkbook` | Creates a new, empty Excel workbook at the root of the signed-in user's OneDrive and returns its drive item ID. Excel initialises the new file with a single worksheet named Sheet1 the first time a workbook action touches it. The file name must end in .xlsx. |
| Create Workbook Session | `createWorkbookSession` | Creates a new Excel workbook session and returns its session ID. A persistent session saves changes to the workbook file, while a non-persistent session evaluates the workbook in memory only. |
| Delete Chart | `deleteChart` | Deletes a chart from a worksheet. The chart's source data is left untouched. |
| Delete Drive Item | `deleteDriveItem` | Deletes a file or folder from the signed-in user's OneDrive by its drive item ID, sending it to the recycle bin. Use it to remove a workbook that is no longer needed. |
| Delete Range | `deleteRange` | Deletes the cells of a range and shifts the surrounding cells to fill the gap, either upwards or to the left. |
| Delete Table | `deleteTable` | Deletes an Excel table and the cells it covers from the workbook. |
| Delete Table Column | `deleteTableColumn` | Deletes one column from an Excel table together with its data. |
| Delete Table Row | `deleteTableRow` | Deletes one data row from an Excel table by its zero-based index. Rows below it shift up, so their indexes change. |
| Delete Worksheet | `deleteWorksheet` | Permanently deletes a worksheet and all of its content from the workbook. |
| Get Chart | `getChart` | Retrieves a single chart from a worksheet by its chart name. |
| Get Chart At Index | `getChartAt` | Retrieves a chart by its zero-based position in the worksheet's chart collection. |
| Get Chart Axis | `getChartAxis` | Retrieves one axis of a chart - the value, category or series axis - including its scale bounds and tick mark intervals. |
| Get Chart Axis Font | `getChartAxisFont` | Retrieves the font used for the tick labels of one chart axis. |
| Get Chart Axis Line Format | `getChartAxisLineFormat` | Retrieves the line formatting of one chart axis, such as the colour of the axis line. |
| Get Chart Axis Title | `getChartAxisTitle` | Retrieves the title of one chart axis, including its text and visibility. |
| Get Chart Data Labels | `getChartDataLabels` | Retrieves the data label settings of a chart, showing which pieces of information are displayed next to each data point. |
| Get Chart Gridlines | `getChartGridlines` | Retrieves the major or minor gridlines of one chart axis and reports whether they are visible. |
| Get Chart Image | `getChartImage` | Renders a chart as a base64-encoded PNG image at the requested pixel size, which is useful for embedding the chart in a report or email. |
| Get Chart Legend | `getChartLegend` | Retrieves the legend of a chart, including its position and whether it is visible. |
| Get Chart Point At Index | `getChartPointAt` | Retrieves a chart data point by its zero-based position within a series' point collection. |
| Get Chart Series At Index | `getChartSeriesAt` | Retrieves a chart data series by its zero-based position in the series collection. |
| Get Chart Title | `getChartTitle` | Retrieves the title of a chart, including its text and whether it is visible or overlaid on the plot area. |
| Get Columns After Range | `getColumnsAfterRange` | Retrieves the given number of columns immediately to the right of a range. |
| Get Columns Before Range | `getColumnsBeforeRange` | Retrieves the given number of columns immediately to the left of a range. |
| Get Comment Reply | `getCommentReply` | Retrieves a single reply from a workbook comment thread. |
| Get Drive Item | `getDriveItem` | Retrieves the metadata of a single OneDrive item by its drive item ID, such as the workbook file name, size and last modified time. |
| Get My Drive | `getMyDrive` | Retrieves the signed-in user's default OneDrive, including its ID, drive type and quota. Use it to confirm the connection works before addressing workbooks. |
| Get Named Item | `getNamedItem` | Retrieves a single named item of a workbook by its name. |
| Get Named Item Range | `getNamedItemRange` | Retrieves the cell range that a named item refers to, together with its values and formulas. |
| Get Pivot Table | `getPivotTable` | Retrieves a single pivot table on a worksheet by its pivot table ID. |
| Get Range | `getRange` | Retrieves a cell range from a worksheet by its A1-style address, returning the values, display text, formulas, number formats and dimensions of the range. |
| Get Range Border | `getRangeBorder` | Retrieves a single border of a cell range by the side it applies to, such as EdgeTop or InsideHorizontal. |
| Get Range Border At Index | `getRangeBorderAt` | Retrieves one border of a cell range by its zero-based position within the border collection. |
| Get Range Bounding Rectangle | `getRangeBoundingRect` | Retrieves the smallest rectangular range that encloses both a range and a second range. For example the bounding rectangle of B2:C5 and D10:E15 is B2:E15. |
| Get Range Cell | `getRangeCell` | Retrieves a single cell from within a range, addressed by its zero-based row and column offsets relative to the top-left cell of the range. |
| Get Range Column | `getRangeColumn` | Retrieves a single column of a range, addressed by its zero-based offset from the first column of the range. |
| Get Range Entire Column | `getRangeEntireColumn` | Retrieves the full worksheet columns that a range spans, from row 1 to the last row of the sheet. Returns the range's address, size, position and hidden state; cell values are not returned because a full column has over a million rows (use Get Range for values). |
| Get Range Entire Row | `getRangeEntireRow` | Retrieves the full worksheet rows that a range spans, from column A to the last column of the sheet. Because that is over sixteen thousand columns, always pass Select to limit the properties returned, for example "address,rowCount,columnCount" - without it the response is too large to return. |
| Get Range Fill | `getRangeFill` | Retrieves the background fill colour applied to a cell range. |
| Get Range Font | `getRangeFont` | Retrieves the font settings applied to a cell range, including name, size, colour, bold, italic and underline. |
| Get Range Format | `getRangeFormat` | Retrieves the formatting of a cell range, including column width, row height, text alignment and wrapping. |
| Get Range Format Protection | `getRangeFormatProtection` | Retrieves the cell-level protection settings of a range, showing whether its cells are locked and whether their formulas are hidden. |
| Get Range Intersection | `getRangeIntersection` | Retrieves the range of cells shared by a range and a second range. Returns an error if the two ranges do not overlap. |
| Get Range Last Cell | `getRangeLastCell` | Retrieves the bottom-right cell of a range. |
| Get Range Last Column | `getRangeLastColumn` | Retrieves the last column of a range. |
| Get Range Last Row | `getRangeLastRow` | Retrieves the last row of a range. |
| Get Range Offset Range | `getRangeOffsetRange` | Retrieves a range of the same size as the source range but shifted by the given number of rows and columns. Positive offsets move down and right, negative offsets move up and left. |
| Get Range Resized Range | `getRangeResizedRange` | Retrieves a range that starts at the same top-left cell as the source range but is grown or shrunk by the given number of rows and columns. |
| Get Range Used Range | `getRangeUsedRange` | Retrieves the used portion of a range, that is the smallest sub-range containing all cells with data or formatting. |
| Get Range Visible View | `getRangeVisibleView` | Retrieves only the visible cells of a range, excluding rows and columns hidden by the user or by an active filter. |
| Get Range Visible View Range | `getRangeVisibleViewRange` | Retrieves the underlying range object that a visible view was derived from. |
| Get Range Visible View Row At Index | `getRangeVisibleViewItemAt` | Retrieves one visible row of a range by its zero-based position within the visible view, skipping rows hidden by the user or by an active filter. Implemented with OData paging over the visible-row collection, because Graph rejects both the itemAt(index=N) form shown in its own documentation and the rows(N) indexed form. |
| Get Rows Above Range | `getRowsAboveRange` | Retrieves the given number of rows immediately above a range, which is useful for reading header rows that sit just above a block of data. |
| Get Rows Below Range | `getRowsBelowRange` | Retrieves the given number of rows immediately below a range. |
| Get Table | `getTable` | Retrieves a single Excel table by its table ID or table name. |
| Get Table Column | `getTableColumn` | Retrieves a single column of an Excel table by its column ID or its header name. |
| Get Table Column At Index | `getTableColumnAt` | Retrieves a column of an Excel table by its zero-based position in the column collection. |
| Get Table Column Data Body Range | `getTableColumnDataBodyRange` | Retrieves the data cells of one table column as a cell range, excluding the header and total cells. |
| Get Table Column Header Row Range | `getTableColumnHeaderRowRange` | Retrieves the header cell of one table column as a cell range. |
| Get Table Column Range | `getTableColumnRange` | Retrieves the full cell range of one table column, including its header and total cells. |
| Get Table Column Total Row Range | `getTableColumnTotalRowRange` | Retrieves the total cell of one table column as a cell range. The table must have its total row switched on. |
| Get Table Data Body Range | `getTableDataBodyRange` | Retrieves the data area of an Excel table as a cell range, excluding the header row and the total row. |
| Get Table Header Row Range | `getTableHeaderRowRange` | Retrieves the header row of an Excel table as a cell range, which is the quickest way to read the table's column names. |
| Get Table Range | `getTableRange` | Retrieves the full cell range covered by an Excel table, including its header and total rows. |
| Get Table Row At Index | `getTableRowAt` | Retrieves a data row of an Excel table by its position in the row collection, using the itemAt function form. |
| Get Table Row Range | `getTableRowRange` | Retrieves the underlying cell range of one Excel table row, giving its worksheet address alongside its values. |
| Get Table Sort | `getTableSort` | Retrieves the sort currently defined on an Excel table, including its sort fields and whether the sort is still valid. |
| Get Table Total Row Range | `getTableTotalRowRange` | Retrieves the total row of an Excel table as a cell range. The table must have its total row switched on. |
| Get Workbook Application | `getWorkbookApplication` | Retrieves the Excel application object for a workbook, which reports the workbook's current calculation mode. |
| Get Workbook Comment | `getWorkbookComment` | Retrieves a single cell comment from a workbook by its comment ID. |
| Get Workbook Operation | `getWorkbookOperation` | Retrieves the status of a long-running workbook operation. Excel returns an operation ID in the Location header when a request is processed asynchronously; poll this action until the status is succeeded or failed. |
| Get Worksheet | `getWorksheet` | Retrieves a single worksheet from a workbook by its worksheet ID or its sheet name. |
| Get Worksheet Cell | `getWorksheetCell` | Retrieves a single cell of a worksheet by its zero-based row and column numbers, counted from the top-left corner of the sheet. |
| Get Worksheet Protection | `getWorksheetProtection` | Retrieves the protection state of a worksheet and the set of actions users are still permitted to perform on it. |
| Get Worksheet Used Range | `getWorksheetUsedRange` | Retrieves the smallest range that encompasses all cells with data or formatting on a worksheet, including its address, values and formulas. |
| Insert Range | `insertRange` | Inserts blank cells at a range address and shifts the existing cells down or to the right. Returns the newly inserted range. |
| List Chart Points | `listChartPoints` | Lists the individual data points of one chart data series. The parent series is addressed positionally as itemAt(index=N), which is the only form the Excel API accepts. |
| List Chart Series | `listChartSeries` | Lists the data series of a chart. |
| List Charts | `listCharts` | Lists the charts on a worksheet with their names and on-sheet position and size. |
| List Comment Replies | `listCommentReplies` | Lists the replies posted on one workbook comment thread. |
| List Drive Root Items | `listDriveRootItems` | Lists the files and folders at the root of the signed-in user's OneDrive. Use it to find the drive item ID of an .xlsx workbook, which every Excel action requires. |
| List Folder Children | `listFolderChildren` | Lists the files and folders contained in a OneDrive folder, identified by its drive item ID. Use it to navigate to a workbook stored inside a folder. |
| List Named Items | `listNamedItems` | Lists the named items (defined names) of a workbook, each mapping a name to a range or a constant formula. |
| List Range Borders | `listRangeBorders` | Lists every border of a cell range, one entry per border side such as EdgeTop, EdgeBottom and InsideVertical. |
| List Range Visible View Rows | `listRangeVisibleViewRows` | Lists the individual visible rows of a range, skipping rows hidden by the user or by an active filter. |
| List Table Columns | `listTableColumns` | Lists the columns of an Excel table with their names, indexes and values. |
| List Table Rows | `listTableRows` | Lists the data rows of an Excel table with their values. Use the page size and skip parameters to page through large tables. |
| List Tables | `listTables` | Lists every Excel table in a workbook, across all worksheets. |
| List Workbook Comments | `listWorkbookComments` | Lists the cell comments in a workbook, with their content and the person who left them. |
| List Worksheet Named Items | `listWorksheetNamedItems` | Lists the named items scoped to one worksheet rather than to the whole workbook. |
| List Worksheet Pivot Tables | `listWorksheetPivotTables` | Lists the pivot tables present on a worksheet. |
| List Worksheet Tables | `listWorksheetTables` | Lists the Excel tables that live on one specific worksheet. |
| List Worksheets | `listWorksheets` | Lists every worksheet in a workbook with its ID, name, position and visibility. |
| Merge Range | `mergeRange` | Merges the cells of a range into a single cell. Set Across to true to merge each row of the range separately instead of merging the whole range. |
| Protect Worksheet | `protectWorksheet` | Protects a worksheet so its locked cells cannot be edited. Supply the options object to allow specific operations such as sorting or using AutoFilter while the sheet is protected. |
| Reapply Table Filters | `reapplyTableFilters` | Reapplies the filters currently defined on an Excel table, refreshing which rows are hidden after the underlying data has changed. |
| Reapply Table Sort | `reapplyTableSort` | Reapplies the sort already defined on an Excel table, reordering the rows after the underlying data has changed. |
| Recalculate Workbook | `recalculateWorkbook` | Recalculates all formulas in the workbook using the chosen calculation type: Recalculate for changed formulas only, Full for every formula, or FullRebuild to rebuild dependencies as well. |
| Refresh All Pivot Tables | `refreshAllPivotTables` | Refreshes every pivot table on a worksheet in one call. |
| Refresh Pivot Table | `refreshPivotTable` | Refreshes one pivot table so it reflects the current state of its source data. |
| Refresh Workbook Session | `refreshWorkbookSession` | Extends the lifetime of an existing Excel workbook session so it does not expire while a long-running operation is in progress. |
| Search Drive Items | `searchDriveItems` | Searches the signed-in user's OneDrive for items matching a query string. Search for ".xlsx" to locate Excel workbooks and read their drive item IDs. |
| Set Chart Area Fill Colour | `setChartAreaFillColor` | Fills the background of the whole chart area with a single solid colour. |
| Set Chart Legend Fill Colour | `setChartLegendFillColor` | Fills the background behind a chart's legend with a single solid colour. |
| Set Chart Position | `setChartPosition` | Moves a chart so its top-left corner sits on the given start cell. Supply an end cell as well to make the chart exactly cover that block of cells. |
| Set Chart Source Data | `setChartSourceData` | Repoints an existing chart at a different source data range and optionally changes whether columns or rows form its data series. |
| Set Chart Title Fill Colour | `setChartTitleFillColor` | Fills the background behind a chart's title with a single solid colour. |
| Sort Range | `sortRange` | Sorts the rows or columns of a cell range using one or more sort fields. Each sort field names a zero-based key column or row and a sort direction. |
| Unmerge Range | `unmergeRange` | Splits previously merged cells in a range back into individual cells. |
| Unprotect Worksheet | `unprotectWorksheet` | Removes protection from a worksheet so all of its cells become editable again. |
| Update Chart | `updateChart` | Updates the size and on-sheet position of a chart. All measurements are in points. |
| Update Chart Axis | `updateChartAxis` | Sets the scale bounds and tick mark intervals of one chart axis. Send an empty string for any value to hand it back to Excel's automatic scaling. |
| Update Chart Axis Font | `updateChartAxisFont` | Updates the font of one chart axis' tick labels, setting size, colour, bold, italic and underline. |
| Update Chart Axis Line Format | `updateChartAxisLineFormat` | Sets the colour of the axis line on one chart axis. |
| Update Chart Axis Title | `updateChartAxisTitle` | Sets the text of a chart axis title and whether that title is shown. |
| Update Chart Data Labels | `updateChartDataLabels` | Controls what a chart's data labels display and where they sit relative to each data point. |
| Update Chart Gridlines | `updateChartGridlines` | Shows or hides the major or minor gridlines of one chart axis. |
| Update Chart Legend | `updateChartLegend` | Shows, hides or repositions the legend of a chart, and controls whether it overlaps the main chart body. |
| Update Chart Series | `updateChartSeries` | Renames a data series of a chart. |
| Update Chart Title | `updateChartTitle` | Sets the text of a chart title and controls whether it is shown and whether it overlays the plot area. |
| Update Named Item | `updateNamedItem` | Updates the comment or visibility of an existing named item in a workbook. |
| Update Range | `updateRange` | Writes values, formulas or number formats into a cell range, and optionally hides its rows or columns. Values and formulas are supplied as a two-dimensional array whose shape must match the range address. |
| Update Range Border | `updateRangeBorder` | Updates one border of a cell range, setting its line style, colour and weight. |
| Update Range Fill | `updateRangeFill` | Sets the background fill colour of a cell range. |
| Update Range Font | `updateRangeFont` | Updates the font of a cell range: typeface name, size, colour, bold, italic and underline style. Only the properties you supply are changed. |
| Update Range Format | `updateRangeFormat` | Updates the formatting of a cell range: column width, row height, horizontal and vertical alignment, and text wrapping. Only the properties you supply are changed. |
| Update Range Format Protection | `updateRangeFormatProtection` | Sets whether the cells of a range are locked and whether their formulas are hidden. These settings take effect only once the worksheet itself is protected. |
| Update Table | `updateTable` | Updates an Excel table's header row visibility, total row visibility and visual style. Only the properties you supply are changed. |
| Update Table Column | `updateTableColumn` | Overwrites the values of one column of an Excel table. The values array must include the header cell when the table shows headers. |
| Update Table Row | `updateTableRow` | Overwrites the values of one data row of an Excel table, identified by its zero-based index. |
| Update Worksheet | `updateWorksheet` | Updates a worksheet's name, its zero-based position in the workbook, or its visibility. Only the properties you supply are changed. |
