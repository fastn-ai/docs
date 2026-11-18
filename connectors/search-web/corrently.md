---
description: "Corrently Energy APIs by STROMDAO provide regional green-electricity, CO2, price and scheduling signals for Germany: GrünstromIndex forecasts, CO2 Advisor,…"
hidden: true
---

# Corrently

<img src="../../.gitbook/assets/connectors/lg/corrently.png" alt="Corrently logo">

Corrently Energy APIs by STROMDAO provide regional green-electricity, CO2, price and scheduling signals for Germany: GrünstromIndex forecasts, CO2 Advisor, CO2 Meter, best-hour search, renewable dispatch, day-ahead market data, Strommix production mix, merit-order analysis, PHEV charge-or-fuel advice, photovoltaic generation forecasts, energy schedules and tariff lookups. All requests are authenticated with a Corrently access token from https://console.corrently.io/.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [corrently.io](https://corrently.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `corrently` |

## Use it

Add Corrently from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.corrently.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Energy Schedule | `createSchedule` | Creates a new energy schedule for a German postal code that plans on/off time slots for a flexible load according to an optimisation law (comfort, price, solar or emission) and the load's requirements such as active hours, energy demand and maximum load. Returns the schedule with its scheduleId, time slots and current recommendation. |
| Create Or Update CO2 Meter | `createOrUpdateCo2Meter` | Submits an electricity meter reading to a CO2 meter. Pass a meterId to update an existing CO2 meter; omit it and pass a postal code to create a new CO2 meter for that location. The response carries the meterId to use for later updates and reads, the accumulated CO2 value and the local GrünstromIndex forecast. |
| Get Best Hour | `getBestHour` | Finds the hour with the highest regional green-electricity share (and lowest CO2) within a look-ahead window for a German postal code, so that flexible loads such as EV charging or heat pumps can be scheduled into the greenest hour. |
| Get CO2 Advisor Forecast | `getCo2Advisor` | Returns a 24-hour hourly CO2 forecast for electricity consumption at a German postal code together with traffic-light consumption advice (green = increase load, yellow = keep load, red = decrease load) and the CO2 thresholds behind each advice level. |
| Get CO2 Meter Reading | `getCo2MeterReading` | Retrieves the latest CO2 footprint of a CO2 meter created with Create Or Update CO2 Meter: the accumulated CO2 value derived from the electricity meter readings at its location, plus the GrünstromIndex forecast for the next 72 hours. Returns an error field when the meter id is unknown. |
| Get Energy Production Mix | `getStrommix` | Returns the German electricity production mix (Strommix) for a predefined period or a custom date range: total production and the value and percentage contributed by each energy source such as biomass, solar, wind, lignite or gas. |
| Get Energy Schedule | `getSchedule` | Retrieves the current state of an energy schedule created with Create Energy Schedule, including its status, the planned on/off time slots, the current switching recommendation and consumption progress. Returns a not_found error object for an unknown schedule id. |
| Get GrünstromIndex Prediction | `getGsiPrediction` | Returns the GrünstromIndex (Green Power Index) forecast for a German postal code: hourly forecast elements with the regional renewable share, wind and solar contributions, CO2 emissions per kWh and price signals for the upcoming days. |
| Get Market Data | `getMarketData` | Returns electricity market data for a German postal code: the national day-ahead spot market price and the local price (including congestion-management costs) per 15-minute period in EUR/MWh. |
| Get Merit Order Analysis | `getMeritOrderAnalysis` | Returns the Merit Order List analysis for Germany: price buckets of the day-ahead market with, for each bucket, the number of samples, the mid price, the capacity utilisation percentage and the actual generation in MW per production technology. The response is a bare array, exposed here as items. |

<details>

<summary>See 11 more actions</summary>

* **Get PHEV Charge Or Fuel Advice** `getPhevChargeOrFuel`: Advises whether a plug-in hybrid vehicle should be driven on electricity or on fuel at a German postal code, based on the vehicle's electric and fuel consumption and the current regional green-electricity and CO2 situation.
* **Get Renewable Dispatch** `getDispatch`: Returns the physical renewable-energy dispatch for a German postal code: the local energy mix before and after dispatch, the neighbouring locations that feed energy in or receive energy, the average transport distance and a per-day history of the mix.
* **Get Solar Generation Forecast** `getSolarPrediction`: Returns a photovoltaic generation forecast (watt-hours per period) for a solar installation located by German postal code or by latitude/longitude, taking panel capacity, tilt, azimuth, technology and system losses into account. Passing a previously returned plant id reuses the stored plant configuration.
* **Get Stromkonto Balances** `getStromkontoBalances`: Returns the balances (credit, debit, saldo and transactions) of a Corrently Stromkonto electricity account for each account variation. The response is a bare array, exposed here as items.
* **Get Stromkonto Choices** `getStromkontoChoices`: Returns the choices (selectable options) currently available to the customer of a Corrently Stromkonto electricity account. The response is a bare array, exposed here as items.
* **Get Tariff Information** `getTariff`: Returns the Corrently energy tariff for a German postal code according to the standard load profile H0: the working price (ap, ct/kWh), the base price (gp, EUR/month), the matched city and the time of the last update. The response is a bare array, exposed here as items.
* **Get WiM Process Status** `getWimStatus`: Returns the status information of a WiM (Wechselprozesse im Messwesen) metering change process identified by its process id.
* **List Meter Readings** `listMeterReadings`: Lists the electricity meter readings recorded for a Corrently metering account. The response is a bare array, exposed here as items.
* **Report Schedule Consumption** `reportScheduleConsumption`: Reports the actual consumption of a running energy schedule (a status_update) so that Corrently can track progress and adjust the remaining time slots. Returns the updated schedule.
* **Request Access Token** `requestAccessToken`: Requests a new Corrently access token (JWT) and its expiry timestamp. Without an appid an anonymous token is issued; an appid obtained from dev@stromdao.com yields an application-bound token. Use the returned token to renew the connection before it expires.
* **Update Schedule Requirements** `updateScheduleRequirements`: Changes the optimisation requirements (law, active hours, energy demand, load limits) of an existing energy schedule (a requirement_update) and returns the re-planned schedule.

</details>
