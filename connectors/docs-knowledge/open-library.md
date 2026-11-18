---
description: "Open Library (Internet Archive) is a free, keyless catalog of millions of books: search books, authors, subjects, editions and lists, read work, edition,…"
hidden: true
---

# Open Library

<img src="../../.gitbook/assets/connectors/lg/open-library.png" alt="Open Library logo">

Open Library (Internet Archive) is a free, keyless catalog of millions of books: search books, authors, subjects, editions and lists, read work, edition, author, subject, publisher and series records, look up books by ISBN/OCLC/LCCN, and browse public reading lists and recent changes.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [openlibrary.org](https://openlibrary.org) |
| **Authentication** | No authentication |
| **Slug** | `openLibrary` |

## Use it

Add Open Library from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openLibrary.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Author | `getAuthor` | Returns an author record: name, birth and death dates, biography, photos, alternate names and links. Docs: https://openlibrary.org/dev/docs/api/authors |
| Get Book Availability by Identifier | `getVolume` | Read API: returns a book's records and its readable/borrowable digital items for one identifier (isbn, oclc, lccn, issn, htid, olid, recordnumber). Docs: https://openlibrary.org/dev/docs/api/read |
| Get Book Availability for Multiple Identifiers | `getVolumesMultiple` | Read API multi-get: returns availability for several identifiers in one call, e.g. isbn:0596156715\|oclc:123. Docs: https://openlibrary.org/dev/docs/api/read |
| Get Books by Identifiers | `getBooksByBibkeys` | Returns book data for one or more bibliographic keys (ISBN, OCLC, LCCN, OLID), e.g. ISBN:0451526538,OCLC:1234. Docs: https://openlibrary.org/dev/docs/api/books |
| Get Edition | `getEdition` | Returns an edition record (a specific published book): title, publishers, publish date, ISBNs, pages, covers and work links. Docs: https://openlibrary.org/dev/docs/api/books |
| Get Edition by ISBN | `getEditionByIsbn` | Returns the edition record for an ISBN-10 or ISBN-13. Docs: https://openlibrary.org/dev/docs/api/books |
| Get List | `getList` | Returns a public reading list: name, description, owner and seeds (works, editions, authors, subjects). Docs: https://openlibrary.org/dev/docs/api/lists |
| Get Publisher | `getPublisher` | Returns the works published by a publisher, with optional details. Docs: https://openlibrary.org/developers/api |
| Get Series | `getSeries` | Returns a book series record (name, description, ordered seeds). Docs: https://openlibrary.org/developers/api |
| Get Subject | `getSubject` | Returns the works for a subject (e.g. love, science_fiction, place:london, person:napoleon), with optional details on related subjects, authors and publishers. Docs: https://openlibrary.org/dev/docs/api/subjects |

<details>

<summary>See 23 more actions</summary>

* **Get User Reading Log** `getUserReadingLog`: Returns a user's public reading-log shelf (want-to-read, currently-reading, already-read or stopped-reading). Only works when the user made the reading log public. Docs: https://openlibrary.org/dev/docs/api/mybooks
* **Get Work** `getWork`: Returns a work record (the abstract book across all editions): title, authors, description, subjects, covers and links. Docs: https://openlibrary.org/dev/docs/api/books
* **Get Work Bookshelves** `getWorkBookshelves`: Returns how many readers have the work on their want-to-read, currently-reading and already-read shelves. Docs: https://openlibrary.org/developers/api
* **Get Work Ratings** `getWorkRatings`: Returns the reader rating summary (average, count, distribution) of a work. Docs: https://openlibrary.org/developers/api
* **List Author Works** `listAuthorWorks`: Returns the works written by an author (paged). Docs: https://openlibrary.org/dev/docs/api/authors
* **List Languages** `listLanguages`: Returns the languages in the catalog with their edition counts. Docs: https://openlibrary.org/developers/api
* **List List Editions** `listListEditions`: Returns the editions in a reading list (paged). Docs: https://openlibrary.org/dev/docs/api/lists
* **List List Seeds** `listListSeeds`: Returns the seeds (works, editions, authors, subjects) of a reading list. Docs: https://openlibrary.org/dev/docs/api/lists
* **List List Subjects** `listListSubjects`: Returns the most common subjects, places, people and times of the books in a reading list. Docs: https://openlibrary.org/dev/docs/api/lists
* **List Lists Containing Author** `listAuthorLists`: Returns public reading lists that contain an author. Docs: https://openlibrary.org/dev/docs/api/lists
* **List Lists Containing Edition** `listEditionLists`: Returns public reading lists that contain an edition. Docs: https://openlibrary.org/dev/docs/api/lists
* **List Lists Containing Work** `listWorkLists`: Returns public reading lists that contain a work. Docs: https://openlibrary.org/dev/docs/api/lists
* **List Lists for Subject** `listSubjectLists`: Returns public reading lists that contain a subject. Docs: https://openlibrary.org/dev/docs/api/lists
* **List Recent Changes** `listRecentChanges`: Returns the most recent edits to the catalog (all kinds), newest first. Docs: https://openlibrary.org/dev/docs/api/recentchanges
* **List Recent Changes by Kind** `listRecentChangesByKind`: Returns recent catalog edits of one kind (e.g. add-book, edit-book, merge-authors, new-account, add-cover). Docs: https://openlibrary.org/dev/docs/api/recentchanges
* **List Recent Edit Activity** `listEditActivity`: Returns a feed of recent book edits with titles, authors, cover and editor names. Docs: https://openlibrary.org/openapi.json
* **List User Lists** `listUserLists`: Returns the public reading lists of a user. Docs: https://openlibrary.org/dev/docs/api/lists
* **List Work Editions** `listWorkEditions`: Returns the editions of a work (paged). Docs: https://openlibrary.org/dev/docs/api/books
* **Search Authors** `searchAuthors`: Searches authors by name and returns author keys, birth dates, top work and work count. Docs: https://openlibrary.org/dev/docs/api/search
* **Search Books** `searchBooks`: Searches works by free text or by title, author, subject, ISBN, publisher and other fields; returns matching works with author, edition, cover and e-book data. Docs: https://openlibrary.org/dev/docs/api/search
* **Search Inside Books** `searchInside`: Full-text search inside the scanned text of digitised books; returns matching books with highlighted snippets. Docs: https://openlibrary.org/dev/docs/api/search_inside
* **Search Lists** `searchLists`: Searches public reading lists by name. Docs: https://openlibrary.org/developers/api
* **Search Subjects** `searchSubjects`: Searches subjects (topics, places, people, times) by name and returns their keys and work counts. Docs: https://openlibrary.org/developers/api

</details>
