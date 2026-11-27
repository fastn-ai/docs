---
description: "Nager.Date is a free public holiday service for 100+ countries. List upcoming holidays and long weekends, and check if today is a holiday."
hidden: true
---

# Nager.Date

<img src="../../.gitbook/assets/connectors/lg/nager-date.png" alt="Nager.Date logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [date.nager.at](https://date.nager.at) |
| **Authentication** | No sign-in needed |
| **Slug** | `nagerDate` |

## Setup

Nager.Date needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Nager.Date from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Nager.Date**.
2. Select **Connect** on the Nager.Date card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Nager.Date needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Nager.Date's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check If Today Is a Holiday</td><td><code>checkTodayIsHoliday</code></td><td>Checks whether today is a public holiday in a country or subdivision (e.g. AT or AT-1), optionally shifted by a UTC offset. Answer is the HTTP status only: 200 = holiday, 204 = not a holiday. Docs: https://date.nager.at/Api</td></tr><tr><td>Check If Today Is a Public Holiday (API v3)</td><td><code>checkTodayIsPublicHolidayV3</code></td><td>Checks whether today is a public holiday in a country, optionally for a subdivision and UTC offset. Answer is the HTTP status only: 200 = holiday, 204 = not a holiday. Docs: https://date.nager.at/Api</td></tr><tr><td>Get Country</td><td><code>getCountry</code></td><td>Returns country information (common, native and official names, region and neighbouring countries) for an ISO country code. Docs: https://date.nager.at/Api</td></tr><tr><td>Get Country Info (API v3)</td><td><code>getCountryInfoV3</code></td><td>Returns country information (names, region, borders) using the v3 API. Docs: https://date.nager.at/Api</td></tr><tr><td>Get Version</td><td><code>getVersion</code></td><td>Returns the version of the Nager.Date library running on the server. Docs: https://date.nager.at/Api</td></tr><tr><td>Get Version (API v3)</td><td><code>getVersionV3</code></td><td>Returns the Nager.Date library version using the v3 API. Docs: https://date.nager.at/Api</td></tr><tr><td>List Available Countries</td><td><code>listAvailableCountries</code></td><td>Returns every country for which public holiday data is available, with name and ISO code. Docs: https://date.nager.at/Api</td></tr><tr><td>List Available Countries (API v3)</td><td><code>listAvailableCountriesV3</code></td><td>Returns all supported countries using the v3 API. Docs: https://date.nager.at/Api</td></tr><tr><td>List Long Weekends</td><td><code>listLongWeekends</code></td><td>Returns the long weekends (3+ consecutive days off) of a country for a year, optionally counting bridge days and narrowed to a subdivision. Docs: https://date.nager.at/Api</td></tr><tr><td>List Next Public Holidays</td><td><code>listNextPublicHolidays</code></td><td>Returns the public holidays of a country in the next 365 days. Docs: https://date.nager.at/Api</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Next Public Holidays (API v3)</td><td><code>listNextPublicHolidaysV3</code></td><td>Returns the public holidays of a country in the next 365 days using the v3 API. Docs: https://date.nager.at/Api</td></tr><tr><td>List Next Public Holidays Worldwide</td><td><code>listNextPublicHolidaysWorldwide</code></td><td>Returns public holidays in all supported countries in the next 7 days. Docs: https://date.nager.at/Api</td></tr><tr><td>List Public Holidays</td><td><code>listPublicHolidays</code></td><td>Returns all public holidays of a country for a year, with local and English names, whether they are national or regional, the subdivisions they apply to and holiday types. Docs: https://date.nager.at/Api</td></tr><tr><td>List Public Holidays (API v3)</td><td><code>listPublicHolidaysV3</code></td><td>Returns all public holidays of a country for a year using the v3 API. Docs: https://date.nager.at/Api</td></tr></tbody></table>

</details>

