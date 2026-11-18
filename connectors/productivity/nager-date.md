---
description: "Nager.Date is a free, keyless public holiday API covering 100+ countries: public holidays per year, upcoming holidays, long weekends, 'is today a holiday'…"
hidden: true
---

# Nager.Date

<img src="../../.gitbook/assets/connectors/nager-date.png" alt="Nager.Date logo" width="64">

Nager.Date is a free, keyless public holiday API covering 100+ countries: public holidays per year, upcoming holidays, long weekends, 'is today a holiday' checks and country information. Uses the free Community API (v4 and v3).

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [date.nager.at](https://date.nager.at) |
| **Authentication** | No authentication |
| **Slug** | `nagerDate` |

## Use it

Add Nager.Date from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nagerDate.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check If Today Is a Holiday | `checkTodayIsHoliday` | Checks whether today is a public holiday in a country or subdivision (e.g. AT or AT-1), optionally shifted by a UTC offset. Answer is the HTTP status only: 200 = holiday, 204 = not a holiday. Docs: https://date.nager.at/Api |
| Check If Today Is a Public Holiday (API v3) | `checkTodayIsPublicHolidayV3` | Checks whether today is a public holiday in a country, optionally for a subdivision and UTC offset. Answer is the HTTP status only: 200 = holiday, 204 = not a holiday. Docs: https://date.nager.at/Api |
| Get Country | `getCountry` | Returns country information (common, native and official names, region and neighbouring countries) for an ISO country code. Docs: https://date.nager.at/Api |
| Get Country Info (API v3) | `getCountryInfoV3` | Returns country information (names, region, borders) using the v3 API. Docs: https://date.nager.at/Api |
| Get Version | `getVersion` | Returns the version of the Nager.Date library running on the server. Docs: https://date.nager.at/Api |
| Get Version (API v3) | `getVersionV3` | Returns the Nager.Date library version using the v3 API. Docs: https://date.nager.at/Api |
| List Available Countries | `listAvailableCountries` | Returns every country for which public holiday data is available, with name and ISO code. Docs: https://date.nager.at/Api |
| List Available Countries (API v3) | `listAvailableCountriesV3` | Returns all supported countries using the v3 API. Docs: https://date.nager.at/Api |
| List Long Weekends | `listLongWeekends` | Returns the long weekends (3+ consecutive days off) of a country for a year, optionally counting bridge days and narrowed to a subdivision. Docs: https://date.nager.at/Api |
| List Next Public Holidays | `listNextPublicHolidays` | Returns the public holidays of a country in the next 365 days. Docs: https://date.nager.at/Api |

<details>

<summary>See 4 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Next Public Holidays (API v3) | `listNextPublicHolidaysV3` | Returns the public holidays of a country in the next 365 days using the v3 API. Docs: https://date.nager.at/Api |
| List Next Public Holidays Worldwide | `listNextPublicHolidaysWorldwide` | Returns public holidays in all supported countries in the next 7 days. Docs: https://date.nager.at/Api |
| List Public Holidays | `listPublicHolidays` | Returns all public holidays of a country for a year, with local and English names, whether they are national or regional, the subdivisions they apply to and holiday types. Docs: https://date.nager.at/Api |
| List Public Holidays (API v3) | `listPublicHolidaysV3` | Returns all public holidays of a country for a year using the v3 API. Docs: https://date.nager.at/Api |

</details>
