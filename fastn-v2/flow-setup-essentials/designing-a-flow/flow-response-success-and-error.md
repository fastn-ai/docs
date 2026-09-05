---
description: >-
  Configure success and error responses for your Fastn flow. Customize HTTP
  response messages and status codes returned when an automation completes.
---

# Flow Response: Success & Error

The **Flow Response** components control what your flow returns when it finishes. Use **Flow Response: Success** to define the payload and HTTP status code returned on a successful run, and **Flow Response: Error** to define what gets returned when the flow encounters a failure. Every API-triggered flow should include both so that callers receive meaningful feedback regardless of the outcome.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FDAduJicFuosyr81g6L5w%252Fimage.png%3Falt%3Dmedia%26token%3D71f42458-ebf4-4c2f-8cae-82f88ffad067&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=cb51acfb&#x26;sv=2" alt="Flow Response component with success and error message configuration fields"><figcaption></figcaption></figure>

**Example Success Definition**

```
Str Status = "success"  
Str Message = "Order processed"  
Int OrderId = 12345
```

**Example Error Definition**

```
Str Status = "error"  
Str ErrorMessage = "Invalid customer email"
```
