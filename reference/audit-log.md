---
description: Audit log columns, filters, action types, and query patterns.
---

# Audit Log

The Audit Log tracks all actions across your organization. Found under **Settings → Audit Log**.

### Columns

| Column        | Description                                                    | Example                                  |
| ------------- | -------------------------------------------------------------- | ---------------------------------------- |
| **TIMESTAMP** | When the action occurred                                       | May 7, 10:39:19 PM                       |
| **USER**      | Who performed it — user name or "system" for automated actions | "John Doe", "system"                     |
| **ACTION**    | What was done — action identifier with dot notation            | `auth.login`, `credential.token_refresh` |
| **RESOURCE**  | What was affected — resource ID + type                         | `eae3a753-7bdc-...` (connection)         |
| **OUTCOME**   | Result of the action                                           | Success (green badge), Failure, Denied   |

### Filters

| Filter          | Options                                                             |
| --------------- | ------------------------------------------------------------------- |
| **All Users**   | Filter by specific user or "system"                                 |
| **All Actions** | Filter by action type (e.g., auth.login, credential.token\_refresh) |
| **All Types**   | Filter by resource type                                             |
| **From / To**   | Date range (dd/mm/yyyy)                                             |

### Known action types

| Action                     | Description                                      |
| -------------------------- | ------------------------------------------------ |
| `auth.login`               | User logged into the platform                    |
| `credential.token_refresh` | System refreshed an OAuth token for a connection |

### User types

| User       | Badge                        | Description                                              |
| ---------- | ---------------------------- | -------------------------------------------------------- |
| Named user | Colored avatar with initials | A human user (e.g., "JD" for John Doe)                   |
| **system** | Green "S" badge              | Automated system action (token refresh, scheduled tasks) |

### Event count

The top-right shows the total number of events matching the current filters (e.g., "100 events").
