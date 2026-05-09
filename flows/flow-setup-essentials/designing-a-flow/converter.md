---
description: >-
  Convert data formats in your Fastn flow, such as JSON to CSV, XML, or
  Parquet. Prepare data for exports, analytics, or downstream API integrations.
---

# Convert data formats in Fastn flows

The **Converter** component transforms data from one file format to another — for example, JSON to CSV, JSON to XML, or JSON to Parquet. Use it when you need to prepare data for exports, analytics pipelines, or downstream APIs that expect a specific format. Unlike the [Data Mapper](data-mapper.md), which restructures fields within the same format, the Converter changes the serialization format of the entire dataset.

**Example definition**

```
StepName = convertInput  
ConversionType = JSON_PARQUET  
Source = {{input}}  
Settings = Default  
```

This means:

* The step is named `convertInput`.
* Input data (`{{input}}`) will be taken from the previous step.
* Conversion type is set to `JSON_PARQUET`.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252Fa7vN2JwLXeikJxDXhaPI%252Fimage.png%3Falt%3Dmedia%26token%3Db150d497-8ad6-4e33-b401-ef9c7eaa02e8&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=46963162&#x26;sv=2" alt="Converter step configured for JSON to Parquet data format conversion"><figcaption></figcaption></figure>
