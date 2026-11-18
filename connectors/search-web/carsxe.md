---
description: "CarsXE is a vehicle data API for decoding VINs and license plates and enriching vehicle records."
hidden: true
---

# CarsXE

<img src="../../.gitbook/assets/connectors/lg/carsxe.png" alt="CarsXE logo">

CarsXE is a vehicle data API for decoding VINs and license plates and enriching vehicle records. This connector covers the complete CarsXE REST surface: vehicle specifications (VIN decoding), international VIN decoding, US and worldwide license plate decoding (v1 and v2), market value (v1 and v2), vehicle history, lien and theft checks, safety recalls by VIN, by year/make/model and in bulk batches, vehicle images, year/make/model lookups and dropdown options, OBD-II trouble code decoding, VIN and license plate image recognition, and the Enterprise ownership and identity-graph lookups. Every call spends account credits.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [carsxe.com](https://carsxe.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `carsxe` |

## Use it

Add CarsXE from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.carsxe.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Decode International VIN | `decodeInternationalVin` | Decodes a non-US (international market) VIN into structured vehicle identity, manufacturer and technical attributes. Use this when a VIN is registered outside the United States and the standard specifications decoder returns no data. |
| Decode License Plate | `decodePlate` | Decodes a license plate into vehicle data using the version 1 plate decoder, which proxies to the version 2 decoder. Accepts US state codes, Australian states, and the legacy country codes BR, UK, IR, IT, ES, IND, MX and NZ. |
| Decode License Plate V2 | `decodePlateV2` | Decodes a license plate into vehicle data across more than 60 supported countries. A state is required for the US, Australia and Canada, and a district is additionally required for Pakistani plates registered in Khyber Pakhtunkhwa. |
| Decode OBD Code | `decodeObdCode` | Decodes an OBD-II diagnostic trouble code, such as P0115, into a readable diagnosis of the underlying fault. |
| Decode US License Plate | `decodeUsPlate` | Looks up a US vehicle by license plate number and state, returning the VIN, year, make, model, trim, engine, body style, transmission, drive type, fuel type and exterior color. Optionally decodes the resolved VIN and includes the full specifications object. Accepts plates from all 50 states, the District of Columbia and Puerto Rico. |
| Download Recalls Batch Results | `downloadRecallsBatchResults` | Downloads the results of a completed bulk recalls batch as CSV. Use Get Recalls Batch Results instead when you want the results as structured JSON. |
| Extract VIN From Image | `extractVinFromImage` | Extracts a VIN from a photo of a VIN plate, sticker or windshield using optical character recognition. Accepts either an image URL or a base64-encoded image string, and returns the VIN with a confidence score and alternative candidates. |
| Get Lien And Theft Records | `getLienAndTheftRecords` | Checks a US VIN for active lien and theft records, returning the vehicle identity along with any lien or theft events on file. |
| Get Market Value | `getMarketValue` | Returns the market value of a vehicle by VIN using the version 1 valuation, including retail, trade-in, loan and auction values plus historical trade-in values. |
| Get Market Value V2 | `getMarketValueV2` | Returns detailed market values for a VIN, including wholesale and retail values across extra clean, clean, average and rough condition tiers, with optional adjustments for US state, mileage and condition. |
| Get Ownership By Address | `getOwnershipByAddress` | Finds everyone on file at a US street address in the CarsXE identity graph. Requires a CarsXE Enterprise plan. Charged per resident returned, only when a match is found. |
| Get Ownership By Person | `getOwnershipByPerson` | Resolves contact details for a person you already have a name and address for, from the CarsXE identity graph. Requires a CarsXE Enterprise plan. Charged per match returned, only when a match is found. |
| Get Ownership By Phone | `getOwnershipByPhone` | Resolves people and contact details from one or more US phone numbers in the CarsXE identity graph. Requires a CarsXE Enterprise plan. Charged per match returned, only when a match is found. |
| Get Ownership By Phone In Bulk | `getOwnershipByPhoneBulk` | Resolves people and contact details for up to 100 US phone numbers in a single call. Requires a CarsXE Enterprise plan. Charged per match returned; numbers with no hit are omitted from the matches and are not billed. |
| Get Ownership By VIN | `getOwnershipByVin` | Looks up the registered owners of a vehicle by VIN, with vehicle attributes, vehicle history and owner contact details. Requires a CarsXE Enterprise plan. Charged per owner returned, only when a match is found. |
| Get Ownership By ZIP Code | `getOwnershipByZip` | Searches a US ZIP code for people matching optional gender, age and income filters, returned as a paginated list. Requires a CarsXE Enterprise plan. Charged per record on the page, up to 100 per call, so broad searches consume credits quickly. |
| Get Recalls Batch Results | `getRecallsBatchResults` | Fetches the per-VIN safety recall results of a completed bulk recalls batch as JSON, including the recall count and campaigns found for each VIN. |
| Get Recalls Batch Status | `getRecallsBatchStatus` | Checks the processing status of a previously submitted bulk recalls batch, returning the batch state and the number of VINs in it. |
| Get Recalls By Year Make Model | `getRecallsByYearMakeModel` | Retrieves open safety recalls for a vehicle by year, make and model, for cases where no VIN is available. Returns the recall count and the individual recall campaigns. |
| Get Vehicle By Year Make Model | `getVehicleByYearMakeModel` | Looks up vehicle data by year, make and model, and optionally trim, when no VIN is available. Returns the best matching vehicle and, on request, every trim option for that year, make and model. |
| Get Vehicle History | `getVehicleHistory` | Retrieves a vehicle history report by VIN, including current and historical title records, title brands, junk and salvage events and insurance records. |
| Get Vehicle Images | `getVehicleImages` | Retrieves photos of a vehicle by make and model, optionally narrowed by year, trim, color, angle, photo type, size and image license. Returns image links with dimensions and thumbnails. |
| Get Vehicle Recalls | `getVehicleRecalls` | Retrieves open safety recalls associated with a vehicle by VIN, including the recall campaign details reported for that specific vehicle. |
| Get Vehicle Specifications | `getVehicleSpecs` | Decodes a 17-character VIN and returns detailed vehicle specifications, including attributes such as year, make, model, trim, engine and dimensions, plus available colors, equipment and standard warranties. If the VIN cannot be decoded, CarsXE falls back to an international VIN decoding check unless that fallback is disabled. |
| Get Year Make Model Options | `getYearMakeModelOptions` | Returns one layer of vehicle reference data for populating Year, Make, Model and Variant dropdown menus. Each call returns exactly one layer; when no dimension is given, the layer is inferred from the year, make and model supplied. |
| Recognize License Plate From Image | `recognizePlateImage` | Extracts the license plate number from a photo of a vehicle using computer vision, returning each detected plate with its bounding box and region. |
| Submit Recalls Batch | `submitRecallsBatch` | Submits up to 10,000 VINs for asynchronous safety recall processing. Supply the VINs as a list, as inline CSV text, or as an HTTPS link to a CSV file. Optionally supply a webhook URL that CarsXE will POST to when the batch finishes. Returns a batch ID to poll with Get Recalls Batch Status. |
| Validate API Key | `validateApiKey` | Checks that the connected CarsXE API key is valid and the account is active, and returns the account owner's email and creation date. Use it to verify credentials before making calls that spend credits. |
