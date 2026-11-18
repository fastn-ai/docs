---
description: "disease.sh is a free open API for disease statistics."
hidden: true
---

# Disease.sh

<img src="../../.gitbook/assets/connectors/lg/disease-sh.png" alt="Disease.sh logo">

disease.sh is a free open API for disease statistics. Get COVID-19 totals by world, continent, country and US state, historical time series, NYT state data, Apple mobility, government-reported data, vaccine coverage and trials, therapeutics, ECDC variant data, and CDC influenza reports. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [disease.sh](https://disease.sh) |
| **Authentication** | No authentication |
| **Slug** | `diseaseSh` |

## Use it

Add Disease.sh from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.diseaseSh.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Apple Mobility Data | `getAppleMobility` | Get COVID-19 Apple mobility data for subregions of a country. Returns a list of mobility data entries for subregion(s) every day since January 13th. Each entry has driving, transit, and walking data with an associated number of percentage change since January 13th (GET /v3/covid-19/apple/countries/{country}/{subregions}). Docs: https://disease.sh/docs/ |
| Get CDC Clinical Labs Influenza Data | `getInfluenzaClinicalLabs` | Get Influenza report data for the 2019 and 2020 outbreaks from the US Center for Disease Control, reported by US clinical labs. (GET /v3/influenza/cdc/USCL). Docs: https://disease.sh/docs/ |
| Get CDC ILINet Influenza Data | `getInfluenzaIlinet` | Get Influenza-like-illness data for the 2019 and 2020 outbreaks from the US Center for Disease Control. (GET /v3/influenza/cdc/ILINet). Docs: https://disease.sh/docs/ |
| Get CDC Public Health Labs Influenza Data | `getInfluenzaPublicHealthLabs` | Get Influenza report data for the 2019 and 2020 outbreaks from the US Center for Disease Control, reported by US public health labs. (GET /v3/influenza/cdc/USPHL). Docs: https://disease.sh/docs/ |
| Get Continent COVID-19 Totals | `getContinent` | Get COVID-19 totals for a specific continent. (GET /v3/covid-19/continents/{continent}). Docs: https://disease.sh/docs/ |
| Get Country COVID-19 History | `getCountryHistory` | Get COVID-19 time series data for a specific country. (GET /v3/covid-19/historical/{country}). Docs: https://disease.sh/docs/ |
| Get Country COVID-19 Totals | `getCountry` | Get COVID-19 totals for a specific country. (GET /v3/covid-19/countries/{country}). Docs: https://disease.sh/docs/ |
| Get Country Vaccine Coverage | `getCountryVaccineCoverage` | Get COVID-19 vaccine doses administered for a country that has reported vaccination rollout. Sourced from https://covid.ourworldindata.org/. (GET /v3/covid-19/vaccine/coverage/countries/{country}). Docs: https://disease.sh/docs/ |
| Get Country Variant Data | `getCountryVariants` | Get COVID-19 ECDC reported data for a specific country. (GET /v3/covid-19/variants/countries/{country}). Docs: https://disease.sh/docs/ |
| Get Global COVID-19 History | `getGlobalHistory` | Get global accumulated COVID-19 time series data. (GET /v3/covid-19/historical/all). Docs: https://disease.sh/docs/ |

<details>

<summary>See 22 more actions</summary>

* **Get Global COVID-19 Totals** `getGlobalTotals`: Get global COVID-19 totals for today, yesterday and two days ago. (GET /v3/covid-19/all). Docs: https://disease.sh/docs/
* **Get Global Vaccine Coverage** `getGlobalVaccineCoverage`: Get total global COVID-19 vaccine doses administered. Sourced from https://covid.ourworldindata.org/. (GET /v3/covid-19/vaccine/coverage). Docs: https://disease.sh/docs/
* **Get Government Reported Data** `getGovCountry`: Get COVID-19 government reported data for a specific country. (GET /v3/covid-19/gov/{country}). Docs: https://disease.sh/docs/
* **Get Multiple Countries COVID-19 History** `getCountriesHistory`: Get COVID-19 time series data for a specific set of countries. (GET /v3/covid-19/historical/{countries}). Docs: https://disease.sh/docs/
* **Get Multiple Countries COVID-19 Totals** `getCountries`: Get COVID-19 totals for a specific set of countries. (GET /v3/covid-19/countries/{countries}). Docs: https://disease.sh/docs/
* **Get Multiple Provinces COVID-19 History** `getProvincesHistory`: Get COVID-19 time series data for a set of provinces in a country. (GET /v3/covid-19/historical/{country}/{provinces}). Docs: https://disease.sh/docs/
* **Get NYT US State Time Series** `getNytState`: Get COVID-19 time series data for a state or set of states, with an entry for each day since the pandemic began. (GET /v3/covid-19/nyt/states/{state}). Docs: https://disease.sh/docs/
* **Get Province COVID-19 History** `getProvinceHistory`: Get COVID-19 time series data for a specific province in a country. (GET /v3/covid-19/historical/{country}/{province}). Docs: https://disease.sh/docs/
* **Get Therapeutics Trials** `getTherapeuticsTrials`: Get therapeutics trial data from RAPS (Regulatory Affairs Professional Society). Specifically published by Jeff Craven at https://www.raps.org/news-and-articles/news-articles/2020/3/covid-19-therapeutics-tracker. (GET /v3/covid-19/therapeutics). Docs: https://disease.sh/docs/
* **Get US State COVID-19 Totals** `getUsStates`: Get COVID-19 totals for specific US State(s). - one state returns an object, several comma-separated states return an array (GET /v3/covid-19/states/{states}). Docs: https://disease.sh/docs/
* **Get US State Vaccine Coverage** `getStateVaccineCoverage`: Get COVID-19 vaccine doses administered for a state that has reported vaccination rollout. Sourced from https://covid.ourworldindata.org/. (GET /v3/covid-19/vaccine/coverage/states/{state}). Docs: https://disease.sh/docs/
* **Get Vaccine Trials** `getVaccineTrials`: Get vaccine trial data from RAPS (Regulatory Affairs Professional Society). Specifically published by Jeff Craven at https://www.raps.org/news-and-articles/news-articles/2020/3/covid-19-vaccine-tracker. (GET /v3/covid-19/vaccine). Docs: https://disease.sh/docs/
* **List Apple Mobility Countries** `listAppleMobilityCountries`: Get a list of supported countries for Apple mobility data. Returns a list of supported country names (GET /v3/covid-19/apple/countries). Docs: https://disease.sh/docs/
* **List Apple Mobility Subregions** `listAppleMobilitySubregions`: Get a list of supported subregions for specific country in the Apple mobility data set. Returns a list of supported subregions in a country where data is available (GET /v3/covid-19/apple/countries/{country}). Docs: https://disease.sh/docs/
* **List Continent COVID-19 Totals** `listContinents`: Get COVID-19 totals for all continents. (GET /v3/covid-19/continents). Docs: https://disease.sh/docs/
* **List Country COVID-19 Totals** `listCountries`: Get COVID-19 totals for all countries. (GET /v3/covid-19/countries). Docs: https://disease.sh/docs/
* **List Country Vaccine Coverage** `listCountryVaccineCoverage`: Get COVID-19 vaccine doses administered for all countries that have reported rolling out vaccination. Sourced from https://covid.ourworldindata.org/. (GET /v3/covid-19/vaccine/coverage/countries). Docs: https://disease.sh/docs/
* **List Government Data Countries** `listGovCountries`: Get a list of supported countries for government specific data. Returns a list of supported country names (GET /v3/covid-19/gov/). Docs: https://disease.sh/docs/
* **List NYT US State Time Series** `listNytStates`: Get COVID-19 time series data for all states, with an entry for each day since the pandemic began. (GET /v3/covid-19/nyt/states). Docs: https://disease.sh/docs/
* **List US State COVID-19 Totals** `listUsStates`: Get COVID-19 totals for all US States. (GET /v3/covid-19/states). Docs: https://disease.sh/docs/
* **List US State Vaccine Coverage** `listStateVaccineCoverage`: Get COVID-19 vaccine doses administered for all states that have reported rolling out vaccination. Sourced from https://covid.ourworldindata.org/. (GET /v3/covid-19/vaccine/coverage/states). Docs: https://disease.sh/docs/
* **List Variant Data Countries** `listVariantCountries`: Get a list of supported countries for ECDC specific data. Returns a list of supported country names (GET /v3/covid-19/variants/countries/). Docs: https://disease.sh/docs/

</details>
