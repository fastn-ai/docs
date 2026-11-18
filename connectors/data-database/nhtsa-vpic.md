---
description: "NHTSA vPIC (Product Information Catalog and Vehicle Listing) is the US Department of Transportation's free vehicle API."
hidden: true
---

# NHTSA vPIC

NHTSA vPIC (Product Information Catalog and Vehicle Listing) is the US Department of Transportation's free vehicle API. Decode VINs (single, partial or batch of 50) and WMIs, and look up makes, models, manufacturers, vehicle types, equipment plant codes, vehicle variables and Canadian vehicle specifications. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [vpic.nhtsa.dot.gov](https://vpic.nhtsa.dot.gov) |
| **Authentication** | No authentication |
| **Actions** | 28 |
| **Events** | 0 |
| **Slug** | `nhtsaVpic` |

## Use it

Add NHTSA vPIC from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nhtsaVpic.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Decode VIN | `decodeVin` | Decode a full or partial VIN into a list of variable/value pairs (make, model, body, engine, safety and more) (GET /DecodeVin/{vin}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Decode VIN (Flat) | `decodeVinFlat` | Decode a full or partial VIN into one flat record with a field per variable (GET /DecodeVinValues/{vin}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Decode VIN Batch | `decodeVinBatch` | Decode up to 50 VINs in one call, each returned as a flat record (POST /DecodeVINValuesBatch/). Format: vin,modelYear;vin,modelYear (model year optional). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Decode VIN Extended | `decodeVinExtended` | Decode a VIN like Decode VIN, plus variables used by other NHTSA programs such as NCSA (GET /DecodeVinExtended/{vin}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Decode VIN Extended (Flat) | `decodeVinExtendedFlat` | Decode a VIN into one flat record including extra NHTSA program variables (GET /DecodeVinValuesExtended/{vin}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Decode WMI | `decodeWmi` | Get the manufacturer, vehicle type and country for a World Manufacturer Identifier (3 or 6 characters) (GET /DecodeWMI/{wmi}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get All Makes | `getAllMakes` | List every vehicle make in the vPIC dataset (GET /GetAllMakes). Returns about 12,000 makes in one response. Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get All Manufacturers | `getAllManufacturers` | List all manufacturers in the vPIC dataset, 100 per page, optionally filtered by manufacturer type (GET /GetAllManufacturers). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Canadian Vehicle Specifications | `getCanadianVehicleSpecifications` | Get Transport Canada vehicle dimension specifications (length, width, height, wheelbase, track, curb weight and more) for a year and make (GET /GetCanadianVehicleSpecifications). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Equipment Plant Codes | `getEquipmentPlantCodes` | List equipment plant (DOT) codes for tires, brake hoses, glazing or retread plants for a year (2016 and later), filtered by report type (GET /GetEquipmentPlantCodes). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Makes for Manufacturer | `getMakesForManufacturer` | List the makes of a manufacturer, by id or name (GET /GetMakeForManufacturer/{manufacturer}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Makes for Manufacturer and Year | `getMakesForManufacturerAndYear` | List the makes of a manufacturer that were active in a given year (GET /GetMakesForManufacturerAndYear/{manufacturer}?year=). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Makes for Vehicle Type | `getMakesForVehicleType` | List the makes that build a vehicle type, matched by name or part of it (GET /GetMakesForVehicleType/{vehicleType}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Manufacturer Details | `getManufacturerDetails` | Get details (address, contacts, vehicle types, WMIs) for a manufacturer by id, or for manufacturers whose name matches, 100 per page (GET /GetManufacturerDetails/{manufacturer}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Models for Make | `getModelsForMake` | List the models of a make, matched by name or part of it (GET /GetModelsForMake/{make}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Models for Make and Vehicle Type | `getModelsForMakeVehicleType` | List the models of a make for a vehicle type (GET /GetModelsForMakeYear/make/{make}/vehicletype/{vehicleType}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Models for Make and Year | `getModelsForMakeYear` | List the models of a make for a model year (GET /GetModelsForMakeYear/make/{make}/modelyear/{year}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Models for Make ID | `getModelsForMakeId` | List the models of a make id (GET /GetModelsForMakeId/{makeId}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Models for Make ID and Vehicle Type | `getModelsForMakeIdVehicleType` | List the models of a make id for a vehicle type (GET /GetModelsForMakeIdYear/makeId/{makeId}/vehicletype/{vehicleType}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Models for Make ID and Year | `getModelsForMakeIdYear` | List the models of a make id for a model year (GET /GetModelsForMakeIdYear/makeId/{makeId}/modelyear/{year}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Models for Make ID, Year and Vehicle Type | `getModelsForMakeIdYearVehicleType` | List the models of a make id for a model year and vehicle type (GET /GetModelsForMakeIdYear/makeId/{makeId}/modelyear/{year}/vehicletype/{vehicleType}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Models for Make, Year and Vehicle Type | `getModelsForMakeYearVehicleType` | List the models of a make for a model year and vehicle type (GET /GetModelsForMakeYear/make/{make}/modelyear/{year}/vehicletype/{vehicleType}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Parts | `getParts` | List manufacturer ORG letters (49 CFR Part 565 VIN guidance or Part 566 manufacturer identification) with letter dates in a range, 1000 per page (GET /GetParts). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Vehicle Types for Make | `getVehicleTypesForMake` | List the vehicle types built under a make, matched by name or part of it (GET /GetVehicleTypesForMake/{make}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Vehicle Types for Make ID | `getVehicleTypesForMakeId` | List the vehicle types built under a make id (GET /GetVehicleTypesForMakeId/{makeId}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Vehicle Variable Values | `getVehicleVariableValues` | List the allowed values of a look-up variable, by full variable name or id (GET /GetVehicleVariableValuesList/{variable}). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get Vehicle Variables | `getVehicleVariables` | List every vehicle variable in vPIC with its id, name, data type and description (GET /GetVehicleVariableList). Docs: https://vpic.nhtsa.dot.gov/api/ |
| Get WMIs for Manufacturer | `getWmisForManufacturer` | List the World Manufacturer Identifiers registered for a manufacturer, optionally for one vehicle type (GET /GetWMIsForManufacturer/{manufacturer}). Docs: https://vpic.nhtsa.dot.gov/api/ |
