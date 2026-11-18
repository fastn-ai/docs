---
description: "The Carbon Intensity API from National Energy System Operator (NESO) gives the carbon intensity (gCO2/kWh) of Great Britain's electricity: current, forecast,…"
hidden: true
---

# Carbon Intensity API (GB)

<img src="../../.gitbook/assets/connectors/lg/carbon-intensity-gb.png" alt="Carbon Intensity API (GB) logo">

The Carbon Intensity API from National Energy System Operator (NESO) gives the carbon intensity (gCO2/kWh) of Great Britain's electricity: current, forecast, historic and statistics, nationally and for 14 regions, England, Scotland, Wales or an outward postcode, plus the generation mix and fuel intensity factors. No API key needed.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [carbonintensity.org.uk](https://carbonintensity.org.uk) |
| **Authentication** | No authentication |
| **Slug** | `carbonIntensityGb` |

## Use it

Add Carbon Intensity API (GB) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.carbonIntensityGb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Carbon Intensity Factors | `getIntensityFactors` | Get the carbon intensity factor (gCO2/kWh) of each fuel type (GET /intensity/factors). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Current Generation Mix | `getCurrentGenerationMix` | Get the Great Britain electricity generation mix for the current half hour (GET /generation). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Current Intensity by Postcode | `getPostcodeIntensity` | Get current carbon intensity and generation mix for the region of an outward postcode (GET /regional/postcode/{postcode}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Current Intensity by Region | `getRegionIntensity` | Get current carbon intensity and generation mix for a region id (GET /regional/regionid/{regionid}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Current National Intensity | `getCurrentIntensity` | Get Great Britain carbon intensity for the current half hour (GET /intensity). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Current Regional Intensity | `getCurrentRegionalIntensity` | Get carbon intensity and generation mix for every GB region for the current half hour (GET /regional). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get England Intensity | `getEnglandIntensity` | Get current carbon intensity and generation mix for England (GET /regional/england). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Generation Mix Past 24h | `getGenerationMixPast24h` | Get the national generation mix for the 24 hours before a datetime (GET /generation/{fromDate}T{fromHour}:{fromMinute}Z/pt24h). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Generation Mix Range | `getGenerationMixRange` | Get the national generation mix between two datetimes (GET /generation/{fromDate}T{fromHour}:{fromMinute}Z/{toDate}T{toHour}:{toMinute}Z). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get National Intensity at Time | `getIntensityAt` | Get national carbon intensity for the half hour containing a datetime (GET /intensity/{fromDate}T{fromHour}:{fromMinute}Z). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get National Intensity by Date | `getIntensityByDate` | Get national carbon intensity for every half hour of a date (GET /intensity/date/{date}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get National Intensity by Date and Period | `getIntensityByDatePeriod` | Get national carbon intensity for one settlement period of a date (GET /intensity/date/{date}/{period}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get National Intensity Forecast 24h | `getIntensityForward24h` | Get national carbon intensity for 24 hours forward from a datetime (GET /intensity/{fromDate}T{fromHour}:{fromMinute}Z/fw24h). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get National Intensity Forecast 48h | `getIntensityForward48h` | Get national carbon intensity for 48 hours forward from a datetime (GET /intensity/{fromDate}T{fromHour}:{fromMinute}Z/fw48h). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get National Intensity Past 24h | `getIntensityPast24h` | Get national carbon intensity for the 24 hours before a datetime (GET /intensity/{fromDate}T{fromHour}:{fromMinute}Z/pt24h). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get National Intensity Range | `getIntensityRange` | Get national carbon intensity between two datetimes (maximum range 14 days) (GET /intensity/{fromDate}T{fromHour}:{fromMinute}Z/{toDate}T{toHour}:{toMinute}Z). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get National Intensity Statistics | `getIntensityStats` | Get max, average and min national carbon intensity between two datetimes (maximum range 30 days) (GET /intensity/stats/{fromDate}T{fromHour}:{fromMinute}Z/{toDate}T{toHour}:{toMinute}Z). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get National Intensity Statistics by Block | `getIntensityStatsBlocks` | Get max, average and min national carbon intensity between two datetimes split into blocks of a given number of hours (maximum range 30 days) (GET /intensity/stats/{fromDate}T{fromHour}:{fromMinute}Z/{toDate}T{toHour}:{toMinute}Z/{block}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Postcode Intensity Forecast 24h | `getPostcodeIntensityFw24h` | Get carbon intensity and generation mix of an outward postcode's region for 24 hours forward from a datetime (GET /regional/intensity/{fromDate}T{fromHour}:{fromMinute}Z/fw24h/postcode/{postcode}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Postcode Intensity Forecast 48h | `getPostcodeIntensityFw48h` | Get carbon intensity and generation mix of an outward postcode's region for 48 hours forward from a datetime (GET /regional/intensity/{fromDate}T{fromHour}:{fromMinute}Z/fw48h/postcode/{postcode}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Postcode Intensity Past 24h | `getPostcodeIntensityPt24h` | Get carbon intensity and generation mix of an outward postcode's region for the 24 hours before a datetime (GET /regional/intensity/{fromDate}T{fromHour}:{fromMinute}Z/pt24h/postcode/{postcode}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Postcode Intensity Range | `getPostcodeIntensityRange` | Get carbon intensity and generation mix of an outward postcode's region between two datetimes (GET /regional/intensity/{fromDate}T{fromHour}:{fromMinute}Z/{toDate}T{toHour}:{toMinute}Z/postcode/{postcode}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Region Intensity Forecast 24h | `getRegionIntensityFw24h` | Get carbon intensity and generation mix of a region for 24 hours forward from a datetime (GET /regional/intensity/{fromDate}T{fromHour}:{fromMinute}Z/fw24h/regionid/{regionid}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Region Intensity Forecast 48h | `getRegionIntensityFw48h` | Get carbon intensity and generation mix of a region for 48 hours forward from a datetime (GET /regional/intensity/{fromDate}T{fromHour}:{fromMinute}Z/fw48h/regionid/{regionid}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Region Intensity Past 24h | `getRegionIntensityPt24h` | Get carbon intensity and generation mix of a region for the 24 hours before a datetime (GET /regional/intensity/{fromDate}T{fromHour}:{fromMinute}Z/pt24h/regionid/{regionid}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Region Intensity Range | `getRegionIntensityRange` | Get carbon intensity and generation mix of a region between two datetimes (GET /regional/intensity/{fromDate}T{fromHour}:{fromMinute}Z/{toDate}T{toHour}:{toMinute}Z/regionid/{regionid}). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Regional Intensity Forecast 24h | `getRegionalIntensityFw24h` | Get carbon intensity and generation mix of every region for 24 hours forward from a datetime (GET /regional/intensity/{fromDate}T{fromHour}:{fromMinute}Z/fw24h). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Regional Intensity Forecast 48h | `getRegionalIntensityFw48h` | Get carbon intensity and generation mix of every region for 48 hours forward from a datetime (GET /regional/intensity/{fromDate}T{fromHour}:{fromMinute}Z/fw48h). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Regional Intensity Past 24h | `getRegionalIntensityPt24h` | Get carbon intensity and generation mix of every region for the 24 hours before a datetime (GET /regional/intensity/{fromDate}T{fromHour}:{fromMinute}Z/pt24h). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Regional Intensity Range | `getRegionalIntensityRange` | Get carbon intensity and generation mix of every region between two datetimes (GET /regional/intensity/{fromDate}T{fromHour}:{fromMinute}Z/{toDate}T{toHour}:{toMinute}Z). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Scotland Intensity | `getScotlandIntensity` | Get current carbon intensity and generation mix for Scotland (GET /regional/scotland). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Today's National Intensity | `getTodayIntensity` | Get national carbon intensity for every half hour of today (GET /intensity/date). Docs: https://carbon-intensity.github.io/api-definitions/ |
| Get Wales Intensity | `getWalesIntensity` | Get current carbon intensity and generation mix for Wales (GET /regional/wales). Docs: https://carbon-intensity.github.io/api-definitions/ |
