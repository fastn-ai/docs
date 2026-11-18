---
description: "Google Slides API v1 — create presentations, read presentation and page content, generate page thumbnails, and apply batch updates to slides, shapes, text,…"
hidden: true
---

# Google Slides

<img src="../../.gitbook/assets/connectors/lg/google-slides.png" alt="Google Slides logo">

Google Slides API v1 — create presentations, read presentation and page content, generate page thumbnails, and apply batch updates to slides, shapes, text, tables, and images.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [slides.googleapis.com](https://slides.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleSlides` |

## Use it

Add Google Slides from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleSlides.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Update Presentation | `batchUpdatePresentation` | Applies one or more arbitrary update requests to a presentation in a single atomic batch. Every request is validated first, and if any request is invalid the whole batch fails and nothing is applied. Use this general-purpose action for any Slides update kind not covered by a dedicated action on this connector. |
| Create Image | `createImage` | Adds an image to a page of a presentation from a publicly accessible image URL. The image is copied into the presentation at insertion time and must be under 50 MB, no more than 25 megapixels, and in PNG, JPEG, or GIF format. |
| Create Line | `createLine` | Creates a line, curved connector, or bent connector on a page of a presentation. |
| Create Paragraph Bullets | `createParagraphBullets` | Turns a range of paragraphs in a shape or table cell into a bulleted or numbered list using one of the Slides bullet presets. Nesting level is inferred from each paragraph's leading indentation. |
| Create Presentation | `createPresentation` | Creates a blank Google Slides presentation with the given title and returns the newly created presentation, including its generated presentation ID and default first slide. |
| Create Shape | `createShape` | Creates a shape such as a text box, rectangle, or ellipse on a page of a presentation, positioned and sized by the given transform and dimensions. |
| Create Sheets Chart | `createSheetsChart` | Embeds a chart from a Google Sheets spreadsheet onto a page of a presentation, either as a static image or as a chart linked to the source spreadsheet. Requires the Google Sheets read scope in addition to the Slides scope. |
| Create Slide | `createSlide` | Adds a new slide to a presentation at the given index, using a predefined layout such as TITLE_AND_BODY or BLANK. |
| Create Table | `createTable` | Creates a table with the given number of rows and columns on a page of a presentation. The table is created with a default style and empty cells. |
| Create Video | `createVideo` | Embeds a YouTube or Google Drive video on a page of a presentation. Drive videos require the requesting user to have access to the file. |
| Delete Object | `deleteObject` | Deletes a page or page element from a presentation. Deleting a group also deletes all of its child elements, and placeholders inherited from a layout cannot be deleted individually. |
| Delete Paragraph Bullets | `deleteParagraphBullets` | Removes bullets from a range of paragraphs in a shape or table cell. The paragraph indentation applied by the bullets is preserved as explicit indentation. |
| Delete Table Column | `deleteTableColumn` | Deletes the table column containing the given reference cell. A table must always keep at least one column, so deleting the final column fails. |
| Delete Table Row | `deleteTableRow` | Deletes the table row containing the given reference cell. A table must always keep at least one row, so deleting the final row fails. |
| Delete Text | `deleteText` | Deletes a range of text from a shape or table cell in a presentation. Set the range type to ALL to remove all of the object's text. |
| Duplicate Object | `duplicateObject` | Duplicates a slide or page element in a presentation. Duplicating a slide places the copy immediately after the original, and duplicating a group also copies all of its child elements. |
| Get Page | `getPage` | Retrieves the latest version of a single page (slide, layout, master, or notes page) within a presentation, including all of its page elements. |
| Get Page Thumbnail | `getPageThumbnail` | Generates a thumbnail image of the latest version of a page in a presentation and returns a temporary content URL for it. The returned URL is valid for approximately 30 minutes. This counts as an expensive read request against the Slides API quota. |
| Get Presentation | `getPresentation` | Retrieves the latest version of the specified presentation, including all of its slides, layouts, masters, and page elements. |
| Group Objects | `groupObjects` | Groups two or more page elements on the same page into a single group element. Videos, tables, and placeholders cannot be grouped. |
| Insert Table Columns | `insertTableColumns` | Inserts one or more empty columns into a table, to the left or right of the column containing the reference cell. |
| Insert Table Rows | `insertTableRows` | Inserts one or more empty rows into a table, above or below the row containing the reference cell. |
| Insert Text | `insertText` | Inserts text into a shape or table cell in a presentation at the given character index. |
| Merge Table Cells | `mergeTableCells` | Merges a rectangular block of cells in a table into a single cell. Text from every merged cell is concatenated into the upper-left cell of the range. |
| Refresh Sheets Chart | `refreshSheetsChart` | Refreshes an embedded linked Google Sheets chart by replacing it with the latest version from the source spreadsheet. Requires the Google Sheets read scope in addition to the Slides scope. |
| Replace All Shapes With Image | `replaceAllShapesWithImage` | Replaces every shape whose text matches the given search string with an image loaded from a URL, and returns how many shapes were replaced. |
| Replace All Shapes With Sheets Chart | `replaceAllShapesWithSheetsChart` | Replaces every shape whose text matches the given search string with a chart from a Google Sheets spreadsheet, and returns how many shapes were replaced. Requires the Google Sheets read scope in addition to the Slides scope. |
| Replace All Text | `replaceAllText` | Replaces every occurrence of a text string across the presentation with new text, and returns how many occurrences were changed. Commonly used to fill placeholder tokens in a template deck. |
| Replace Image | `replaceImage` | Replaces the contents of an existing image on a slide with a new image loaded from a URL, keeping the original image's position and size. |
| Reroute Line | `rerouteLine` | Reroutes a connector line so that it takes the shortest path between the two page elements it is attached to. The line must already be connected at both ends. |
| Ungroup Objects | `ungroupObjects` | Ungroups one or more group elements, promoting their child elements back onto the page. Only regular groups and word art can be ungrouped. |
| Unmerge Table Cells | `unmergeTableCells` | Splits previously merged cells in a table back into individual cells. Text from a merged cell remains in the resulting upper-left cell. |
| Update Line Category | `updateLineCategory` | Changes the routing category of a connector line between straight, bent, and curved, and reroutes it to the shortest path for the new category. |
| Update Page Element Alt Text | `updatePageElementAltText` | Sets the accessibility alt text title and description on a page element such as an image, shape, or video. |
| Update Page Element Transform | `updatePageElementTransform` | Moves, scales, shears, or rotates a page element by applying an affine transform, either replacing the element's existing transform or composing with it. |
| Update Page Elements Z Order | `updatePageElementsZOrder` | Changes the stacking order of page elements on a slide, bringing them forward or sending them backward relative to the other elements on the same page. |
| Update Paragraph Style | `updateParagraphStyle` | Applies paragraph formatting such as alignment, line spacing, indentation, and paragraph spacing to a range of text in a shape or table cell. Only the properties named in the field mask are applied. |
| Update Slide Properties | `updateSlideProperties` | Updates the properties of a slide, such as whether the slide is skipped during presentation. |
| Update Slides Position | `updateSlidesPosition` | Reorders slides in a presentation by moving the given slides to a new position. The slides must be listed in their existing presentation order and must be contiguous. |
| Update Text Style | `updateTextStyle` | Applies character formatting such as bold, italic, font family, font size, and colour to a range of text in a shape or table cell. Only the properties named in the field mask are applied, so send the full set of style inputs and use the mask to select which of them take effect. |
