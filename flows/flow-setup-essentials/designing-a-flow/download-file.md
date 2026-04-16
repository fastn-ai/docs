---
description: >-
  Fetch files from a URL and use them within your Fastn flow. Download CSVs,
  attachments, or other files for processing in subsequent automation steps.
---

# Download files in Fastn flows

Fetch a file from a URL and use it within your flow.

For example, to parse a CSV or attach a file to an email.

```
SourceUrl = "https://files.server.com/report.csv"
DestinationName = monthlyReport
ContentType = text/csv
```

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FjIPqarF3Y0vn2sKhALRV%252Fimage.png%3Falt%3Dmedia%26token%3D464a0364-0057-4a3c-84d2-f1633e3629fc&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=5e10752f&#x26;sv=2" alt="Download File component configured with source URL, destination name, and content type"><figcaption></figcaption></figure>
