---
description: "Disease.sh is a free disease statistics service. Get COVID-19 totals and history by world, continent and country."
hidden: true
---

# Disease.sh

<img src="../../.gitbook/assets/connectors/lg/disease-sh.png" alt="Disease.sh logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [disease.sh](https://disease.sh) |
| **Authentication** | No sign-in needed |
| **Slug** | `diseaseSh` |

## Setup

Disease.sh needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Disease.sh from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Disease.sh**.
2. Select **Connect** on the Disease.sh card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Disease.sh needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Disease.sh's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Apple Mobility Data</td><td><code>getAppleMobility</code></td><td>Get COVID-19 Apple mobility data for subregions of a country. Returns a list of mobility data entries for subregion(s) every day since January 13th. Each entry has driving, transit, and walking data with an associated number of percentage change since January 13th Docs: https://disease.sh/docs/</td></tr><tr><td>Get CDC Clinical Labs Influenza Data</td><td><code>getInfluenzaClinicalLabs</code></td><td>Get Influenza report data for the 2019 and 2020 outbreaks from the US Center for Disease Control, reported by US clinical labs. Docs: https://disease.sh/docs/</td></tr><tr><td>Get CDC ILINet Influenza Data</td><td><code>getInfluenzaIlinet</code></td><td>Get Influenza-like-illness data for the 2019 and 2020 outbreaks from the US Center for Disease Control. Docs: https://disease.sh/docs/</td></tr><tr><td>Get CDC Public Health Labs Influenza Data</td><td><code>getInfluenzaPublicHealthLabs</code></td><td>Get Influenza report data for the 2019 and 2020 outbreaks from the US Center for Disease Control, reported by US public health labs. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Continent COVID-19 Totals</td><td><code>getContinent</code></td><td>Get COVID-19 totals for a specific continent. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Country COVID-19 History</td><td><code>getCountryHistory</code></td><td>Get COVID-19 time series data for a specific country. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Country COVID-19 Totals</td><td><code>getCountry</code></td><td>Get COVID-19 totals for a specific country. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Country Vaccine Coverage</td><td><code>getCountryVaccineCoverage</code></td><td>Get COVID-19 vaccine doses administered for a country that has reported vaccination rollout. Sourced from https://covid.ourworldindata.org/. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Country Variant Data</td><td><code>getCountryVariants</code></td><td>Get COVID-19 ECDC reported data for a specific country. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Global COVID-19 History</td><td><code>getGlobalHistory</code></td><td>Get global accumulated COVID-19 time series data. Docs: https://disease.sh/docs/</td></tr></tbody></table>

<details>

<summary>View 22 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Global COVID-19 Totals</td><td><code>getGlobalTotals</code></td><td>Get global COVID-19 totals for today, yesterday and two days ago. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Global Vaccine Coverage</td><td><code>getGlobalVaccineCoverage</code></td><td>Get total global COVID-19 vaccine doses administered. Sourced from https://covid.ourworldindata.org/. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Government Reported Data</td><td><code>getGovCountry</code></td><td>Get COVID-19 government reported data for a specific country. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Multiple Countries COVID-19 History</td><td><code>getCountriesHistory</code></td><td>Get COVID-19 time series data for a specific set of countries. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Multiple Countries COVID-19 Totals</td><td><code>getCountries</code></td><td>Get COVID-19 totals for a specific set of countries. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Multiple Provinces COVID-19 History</td><td><code>getProvincesHistory</code></td><td>Get COVID-19 time series data for a set of provinces in a country. Docs: https://disease.sh/docs/</td></tr><tr><td>Get NYT US State Time Series</td><td><code>getNytState</code></td><td>Get COVID-19 time series data for a state or set of states, with an entry for each day since the pandemic began. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Province COVID-19 History</td><td><code>getProvinceHistory</code></td><td>Get COVID-19 time series data for a specific province in a country. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Therapeutics Trials</td><td><code>getTherapeuticsTrials</code></td><td>Get therapeutics trial data from RAPS (Regulatory Affairs Professional Society). Specifically published by Jeff Craven at https://www.raps.org/news-and-articles/news-articles/2020/3/covid-19-therapeutics-tracker. Docs: https://disease.sh/docs/</td></tr><tr><td>Get US State COVID-19 Totals</td><td><code>getUsStates</code></td><td>Get COVID-19 totals for specific US State(s). - one state returns an object, several comma-separated states return an array Docs: https://disease.sh/docs/</td></tr><tr><td>Get US State Vaccine Coverage</td><td><code>getStateVaccineCoverage</code></td><td>Get COVID-19 vaccine doses administered for a state that has reported vaccination rollout. Sourced from https://covid.ourworldindata.org/. Docs: https://disease.sh/docs/</td></tr><tr><td>Get Vaccine Trials</td><td><code>getVaccineTrials</code></td><td>Get vaccine trial data from RAPS (Regulatory Affairs Professional Society). Specifically published by Jeff Craven at https://www.raps.org/news-and-articles/news-articles/2020/3/covid-19-vaccine-tracker. Docs: https://disease.sh/docs/</td></tr><tr><td>List Apple Mobility Countries</td><td><code>listAppleMobilityCountries</code></td><td>Get a list of supported countries for Apple mobility data. Returns a list of supported country names Docs: https://disease.sh/docs/</td></tr><tr><td>List Apple Mobility Subregions</td><td><code>listAppleMobilitySubregions</code></td><td>Get a list of supported subregions for specific country in the Apple mobility data set. Returns a list of supported subregions in a country where data is available Docs: https://disease.sh/docs/</td></tr><tr><td>List Continent COVID-19 Totals</td><td><code>listContinents</code></td><td>Get COVID-19 totals for all continents. Docs: https://disease.sh/docs/</td></tr><tr><td>List Country COVID-19 Totals</td><td><code>listCountries</code></td><td>Get COVID-19 totals for all countries. Docs: https://disease.sh/docs/</td></tr><tr><td>List Country Vaccine Coverage</td><td><code>listCountryVaccineCoverage</code></td><td>Get COVID-19 vaccine doses administered for all countries that have reported rolling out vaccination. Sourced from https://covid.ourworldindata.org/. Docs: https://disease.sh/docs/</td></tr><tr><td>List Government Data Countries</td><td><code>listGovCountries</code></td><td>Get a list of supported countries for government specific data. Returns a list of supported country names Docs: https://disease.sh/docs/</td></tr><tr><td>List NYT US State Time Series</td><td><code>listNytStates</code></td><td>Get COVID-19 time series data for all states, with an entry for each day since the pandemic began. Docs: https://disease.sh/docs/</td></tr><tr><td>List US State COVID-19 Totals</td><td><code>listUsStates</code></td><td>Get COVID-19 totals for all US States. Docs: https://disease.sh/docs/</td></tr><tr><td>List US State Vaccine Coverage</td><td><code>listStateVaccineCoverage</code></td><td>Get COVID-19 vaccine doses administered for all states that have reported rolling out vaccination. Sourced from https://covid.ourworldindata.org/. Docs: https://disease.sh/docs/</td></tr><tr><td>List Variant Data Countries</td><td><code>listVariantCountries</code></td><td>Get a list of supported countries for ECDC specific data. Returns a list of supported country names Docs: https://disease.sh/docs/</td></tr></tbody></table>

</details>

