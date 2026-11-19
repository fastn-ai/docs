---
description: "NHTSA vPIC is the US Department of Transportation's vehicle data service. Decode VINs and list vehicle makes, models and manufacturers."
hidden: true
---

# NHTSA vPIC

<img src="../../.gitbook/assets/connectors/lg/nhtsa-vpic.png" alt="NHTSA vPIC logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [vpic.nhtsa.dot.gov](https://vpic.nhtsa.dot.gov) |
| **Authentication** | No sign-in needed |
| **Slug** | `nhtsaVpic` |

## Setup

NHTSA vPIC needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add NHTSA vPIC from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nhtsaVpic.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Decode VIN</td><td><code>decodeVin</code></td><td>Decode a full or partial VIN into a list of variable/value pairs (make, model, body, engine, safety and more) Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Decode VIN (Flat)</td><td><code>decodeVinFlat</code></td><td>Decode a full or partial VIN into one flat record with a field per variable Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Decode VIN Batch</td><td><code>decodeVinBatch</code></td><td>Decode up to 50 VINs in one call, each returned as a flat record Format: vin,modelYear;vin,modelYear (model year optional). Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Decode VIN Extended</td><td><code>decodeVinExtended</code></td><td>Decode a VIN like Decode VIN, plus variables used by other NHTSA programs such as NCSA Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Decode VIN Extended (Flat)</td><td><code>decodeVinExtendedFlat</code></td><td>Decode a VIN into one flat record including extra NHTSA program variables Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Decode WMI</td><td><code>decodeWmi</code></td><td>Get the manufacturer, vehicle type and country for a World Manufacturer Identifier (3 or 6 characters) Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get All Makes</td><td><code>getAllMakes</code></td><td>List every vehicle make in the vPIC dataset Returns about 12,000 makes in one response. Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get All Manufacturers</td><td><code>getAllManufacturers</code></td><td>List all manufacturers in the vPIC dataset, 100 per page, optionally filtered by manufacturer type Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Canadian Vehicle Specifications</td><td><code>getCanadianVehicleSpecifications</code></td><td>Get Transport Canada vehicle dimension specifications (length, width, height, wheelbase, track, curb weight and more) for a year and make Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Equipment Plant Codes</td><td><code>getEquipmentPlantCodes</code></td><td>List equipment plant (DOT) codes for tires, brake hoses, glazing or retread plants for a year (2016 and later), filtered by report type Docs: https://vpic.nhtsa.dot.gov/api/</td></tr></tbody></table>

<details>

<summary>View 18 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Makes for Manufacturer</td><td><code>getMakesForManufacturer</code></td><td>List the makes of a manufacturer, by id or name Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Makes for Manufacturer and Year</td><td><code>getMakesForManufacturerAndYear</code></td><td>List the makes of a manufacturer that were active in a given year Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Makes for Vehicle Type</td><td><code>getMakesForVehicleType</code></td><td>List the makes that build a vehicle type, matched by name or part of it Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Manufacturer Details</td><td><code>getManufacturerDetails</code></td><td>Get details (address, contacts, vehicle types, WMIs) for a manufacturer by id, or for manufacturers whose name matches, 100 per page Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Models for Make</td><td><code>getModelsForMake</code></td><td>List the models of a make, matched by name or part of it Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Models for Make and Vehicle Type</td><td><code>getModelsForMakeVehicleType</code></td><td>List the models of a make for a vehicle type Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Models for Make and Year</td><td><code>getModelsForMakeYear</code></td><td>List the models of a make for a model year Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Models for Make ID</td><td><code>getModelsForMakeId</code></td><td>List the models of a make id Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Models for Make ID and Vehicle Type</td><td><code>getModelsForMakeIdVehicleType</code></td><td>List the models of a make id for a vehicle type Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Models for Make ID and Year</td><td><code>getModelsForMakeIdYear</code></td><td>List the models of a make id for a model year Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Models for Make ID, Year and Vehicle Type</td><td><code>getModelsForMakeIdYearVehicleType</code></td><td>List the models of a make id for a model year and vehicle type Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Models for Make, Year and Vehicle Type</td><td><code>getModelsForMakeYearVehicleType</code></td><td>List the models of a make for a model year and vehicle type Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Parts</td><td><code>getParts</code></td><td>List manufacturer ORG letters (49 CFR Part 565 VIN guidance or Part 566 manufacturer identification) with letter dates in a range, 1000 per page Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Vehicle Types for Make</td><td><code>getVehicleTypesForMake</code></td><td>List the vehicle types built under a make, matched by name or part of it Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Vehicle Types for Make ID</td><td><code>getVehicleTypesForMakeId</code></td><td>List the vehicle types built under a make id Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Vehicle Variable Values</td><td><code>getVehicleVariableValues</code></td><td>List the allowed values of a look-up variable, by full variable name or id Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get Vehicle Variables</td><td><code>getVehicleVariables</code></td><td>List every vehicle variable in vPIC with its id, name, data type and description Docs: https://vpic.nhtsa.dot.gov/api/</td></tr><tr><td>Get WMIs for Manufacturer</td><td><code>getWmisForManufacturer</code></td><td>List the World Manufacturer Identifiers registered for a manufacturer, optionally for one vehicle type Docs: https://vpic.nhtsa.dot.gov/api/</td></tr></tbody></table>

</details>

## Events

NHTSA vPIC has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
