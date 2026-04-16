---
description: >-
  Define and reuse values like counters, strings, and flags across your Fastn
  flow steps. Store intermediate data and configuration settings.
---

# Variables

Set and reuse values across your flow, like counters, strings, objects, or flags. Great for storing intermediate data or config settings.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FGYEiW1jB8bhZ8PqwkD6J%252Fimage.png%3Falt%3Dmedia%26token%3Da5377eb1-c0ba-465e-b417-ca99d41a3ed8&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b7827b4b&#x26;sv=2" alt="Variables component showing defined string, integer, and boolean variable types"><figcaption></figcaption></figure>

#### **Use Case: Store and Reuse Values Across the Flow**

\
Use the **Variables** component to define and manage reusable values, such as counters, file paths, booleans, or JSON objects, that persist across different steps in your flow. Ideal for maintaining configuration data, controlling logic, or tracking state dynamically during execution.

```
Str filePath = "https://storage.fastn.ai/file.csv"  
Int retryCount = 2  
Boolean isSynced = False  
```

#### **How does it help?**

* Maintain consistent values across multiple flow actions
* Simplify logic handling with flags and counters
* Dynamically store and update configuration or temporary data
