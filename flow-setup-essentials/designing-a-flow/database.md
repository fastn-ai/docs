---
description: >-
  Read from and write to Fastn's internal database using SQL queries. Manage
  structured data, run lookups, and store results within your automation flows.
---

# Database

Use this to read from or write to Fastn's internal database using SQL queries. Ideal for managing structured data inside your flows.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FBn2RQC3mMEMNXjqOoGR4%252Fimage.png%3Falt%3Dmedia%26token%3D478132ce-8b6e-4cee-95f0-b804eae3d357&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=5933f41e&#x26;sv=2" alt="Database component with SQL query editor for reading and writing internal data"><figcaption></figcaption></figure>

* You can run queries to **select**, **insert**, or **create tables**.
* Queries can also use outputs from earlier steps.

#### **Use Case: Manage Internal Data with SQL**

Use the **Database** component to interact directly with Fastn's internal storage. You can create tables, insert new records, or retrieve structured data using SQL. It's perfect for managing intermediate or persistent datasets within your flows, such as syncing user information, logging transactions, or filtering active records.

**Example**\
Retrieve a list of active users to feed into a downstream connector:

```sql
SELECT id, email FROM users WHERE active = True
```

#### **How does it help?**

* Store and reuse structured data between flow steps
* Perform SQL-based lookups and filters dynamically
* Combine database results with outputs from earlier actions
