---
description: "Dadata is a Russian data quality service for suggestions, standardization and enrichment."
hidden: true
---

# Dadata

<img src="../../.gitbook/assets/connectors/lg/dadata.png" alt="Dadata logo">

Dadata is a Russian data quality service for suggestions, standardization and enrichment. This connector covers the Dadata Suggestions API (companies, banks, addresses, names, emails, countries, currencies, courts, tax and customs offices, postal units, metro, classifiers), the findById and geolocation lookups, the Cleaner (standardization) API for addresses, phones, emails, names, passports and vehicles, brand and company-by-email enrichment, and profile balance, usage statistics and reference-data versions.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [dadata.ru](https://dadata.ru) |
| **Authentication** | Credentials you enter |
| **Slug** | `dadata` |

## Use it

Add Dadata from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dadata.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Clean Address | `cleanAddress` | Standardizes a free-form Russian address: splits it into region, city, street, house and flat, corrects the postal code, geocodes it, adds FIAS/KLADR/OKATO/OKTMO codes, tax office, cadastral number, nearest metro and quality codes. Requires the secret key. |
| Clean Email | `cleanEmail` | Standardizes an email address: corrects common typos, splits the local part and domain, classifies it as personal, corporate, role or disposable, and returns a quality code. Requires the secret key. |
| Clean Full Name | `cleanName` | Standardizes a Russian personal name: corrects spelling, orders surname, given name and patronymic, detects gender and returns the name in genitive, dative and ablative cases with a quality code. Requires the secret key. |
| Clean Passport | `cleanPassport` | Standardizes a Russian passport series and number and checks its validity against the Ministry of Internal Affairs register of invalid passports, returning a quality code. Requires the secret key. |
| Clean Phone | `cleanPhone` | Standardizes a free-form phone number: formats it, splits country/city codes, number and extension, detects the type (mobile or landline), operator, region, city and timezone, and returns a quality code. Requires the secret key. |
| Clean Record | `cleanRecord` | Standardizes a composite record made of several fields in one call, for example a name, an address and a phone. The 'structure' array declares the field types and each row in 'data' supplies the raw values in the same order. Requires the secret key. |
| Clean Vehicle | `cleanVehicle` | Standardizes a free-form vehicle description into a normalized brand and model with a quality code. Requires the secret key. |
| Find Address By ID | `findAddressById` | Looks up a Russian address by its FIAS/GAR ID, KLADR code or cadastral number and returns the fully structured address with codes and coordinates. |
| Find Affiliated Parties | `findAffiliatedParties` | Finds companies affiliated with a person or organization by INN: organizations where the given INN appears among founders and/or managers. |
| Find Bank By ID | `findBankById` | Looks up a Russian bank by BIC, SWIFT, INN, INN/KPP or registration number and returns its payment details and address. |

<details>

<summary>See 49 more actions</summary>

* **Find Belarus Party By ID** `findPartyByById`: Looks up a Belarusian company or individual entrepreneur by its UNP (taxpayer number) and returns its registry details.
* **Find Brand By INN** `findBrandByInn`: Finds the brand of a company or individual entrepreneur by INN and returns its name, website, logo, business summary and social links. Requires the secret key and is billed per request by Dadata.
* **Find Car Brand By ID** `findCarBrandById`: Looks up a car brand by its identifier (Latin brand code such as FORD) and returns its names.
* **Find Company By Email** `findCompanyByEmail`: Identifies the company behind a corporate email address and returns its registry details (name, INN, OGRN, address, management) together with the parsed email. Requires the secret key and the paid 'Company by email' feature on the Dadata account.
* **Find Country By Code** `findCountryById`: Looks up a country by its ISO alpha-2, alpha-3 or numeric code and returns its names and codes from the OKSM classifier.
* **Find Court By Code** `findCourtById`: Looks up a Russian court by its code (e.g. 52MS0022) and returns its name, type, region, address and contact details.
* **Find Currency By Code** `findCurrencyById`: Looks up a currency by its alphabetic (e.g. RUB) or numeric code and returns its OKV classifier record.
* **Find Customs Office By Code** `findFtsUnitById`: Looks up a Russian customs office or post (FTS unit) by its eight-digit code and returns its name, type and address.
* **Find Delivery City IDs** `findDeliveryCityIds`: Returns the city identifiers used by delivery services Boxberry, CDEK and DPD for a city given by its KLADR code.
* **Find Freight Forwarder By ID** `findForwarderById`: Looks up a licensed freight forwarder in the Russian register of forwarding companies by INN, OGRN or registry number and returns its license details.
* **Find Kazakhstan Party By ID** `findPartyKzById`: Looks up a Kazakhstani company or individual entrepreneur by BIN or IIN and returns its registry details.
* **Find Medical Position By Code** `findMedicalPositionById`: Looks up a medical job position in the Russian nomenclature of healthcare positions by its code and returns its name.
* **Find MKTU Class By Code** `findMktuById`: Looks up a goods or service entry in the Nice Classification (MKTU) by its code and returns its class and name.
* **Find OKPD2 Code By ID** `findOkpd2ById`: Looks up a product or service entry in the OKPD-2 classifier by its exact code and returns its name and hierarchy.
* **Find OKPDTR Position By Code** `findOkpdtrPositionById`: Looks up an employee position in the OKPDTR classifier by its code and returns its name and OKZ code.
* **Find OKPDTR Profession By Code** `findOkpdtrProfessionById`: Looks up a worker profession in the OKPDTR classifier by its code and returns its name and OKZ code.
* **Find OKTMO Code By ID** `findOktmoById`: Looks up a municipal territory in the OKTMO classifier by its code and returns its name, hierarchy and parent codes.
* **Find OKVED2 Code By ID** `findOkved2ById`: Looks up an economic activity entry in the OKVED-2 classifier by its exact code and returns its name and hierarchy.
* **Find Party By ID** `findPartyById`: Looks up a Russian company or individual entrepreneur by INN, INN/KPP or OGRN and returns full registry details: names, legal form, status, address, management, OKVED codes, tax authority, founders, employee count and more.
* **Find Postal Unit By Code** `findPostalUnitById`: Looks up a Russian Post office by its postal code and returns its address, type, opening hours and coordinates.
* **Find Tax Office By Code** `findFnsUnitById`: Looks up a Russian tax office (FNS inspectorate) by its four-digit code and returns its name, address, payment details and contacts.
* **Geolocate Address** `geolocateAddress`: Reverse geocodes a pair of coordinates and returns the nearest Russian addresses (houses) within the given radius, each as a fully structured address.
* **Geolocate Postal Unit** `geolocatePostalUnit`: Finds the nearest Russian Post offices to a pair of coordinates within the given radius and returns each with its distance, address and opening hours.
* **Get Balance** `getBalance`: Returns the current balance of your Dadata account in rubles. Requires the secret key.
* **Get Daily Statistics** `getDailyStatistics`: Returns today's usage statistics and remaining request quotas per Dadata service (clean, company, merging, suggestions). Requires the secret key.
* **Get Reference Data Versions** `getReferenceDataVersions`: Returns the versions and actuality dates of the Dadata reference datasets (FIAS, EGRUL, banks and others) behind the suggestions and cleaner services.
* **Locate City By IP** `locateCityByIp`: Determines the city for an IPv4 or IPv6 address and returns it as a structured address in the 'location' field (null when the IP cannot be resolved).
* **Suggest Address** `suggestAddress`: Suggests Russian addresses as the user types, returning up to 20 structured matches with postal code, region, city, street, house, FIAS/KLADR codes, coordinates and tax office. Supports restricting by parent location, radius and granularity bounds.
* **Suggest Bank** `suggestBank`: Searches Russian banks by name, BIC, SWIFT, INN or address and returns matching suggestions with payment details (BIC, correspondent account, registration number, address).
* **Suggest Belarus Party** `suggestPartyBy`: Searches companies and individual entrepreneurs registered in Belarus by name or UNP (taxpayer number) and returns matching suggestions.
* **Suggest Car Brand** `suggestCarBrand`: Suggests car brands by name in Russian or Latin spelling and returns the brand identifier and names.
* **Suggest Country** `suggestCountry`: Suggests countries by name (OKSM classifier) and returns the numeric code, alpha-2 and alpha-3 ISO codes and full and short names.
* **Suggest Court** `suggestCourt`: Suggests Russian courts by name, code or city and returns the court code, name, type, region, address and contact details.
* **Suggest Currency** `suggestCurrency`: Suggests currencies by name or code (OKV classifier) and returns the numeric code, alphabetic code, name and issuing countries.
* **Suggest Customs Office** `suggestFtsUnit`: Suggests Russian customs offices and posts (FTS units) by code or name and returns their code, name, type and address.
* **Suggest Email** `suggestEmail`: Suggests email address completions (popular mail domains) for a partially typed email and returns the parsed local part and domain.
* **Suggest FMS Unit** `suggestFmsUnit`: Suggests passport-issuing authorities (FMS/MVD units) by unit code or name, optionally filtered by region code and unit type.
* **Suggest Full Name** `suggestFio`: Suggests Russian personal names (surname, given name, patronymic) as the user types, with detected gender and the parsed name parts.
* **Suggest Kazakhstan Party** `suggestPartyKz`: Searches companies and individual entrepreneurs registered in Kazakhstan by name or BIN/IIN and returns matching suggestions.
* **Suggest Medical Position** `suggestMedicalPosition`: Suggests medical job positions from the Russian nomenclature of healthcare positions by keyword and returns the code and name.
* **Suggest Metro Station** `suggestMetro`: Suggests metro stations in Russian cities by name and returns the station, line, city, coordinates and closure status. Supports filtering by city, line and closed status.
* **Suggest MKTU Class** `suggestMktu`: Suggests goods and services from the Nice Classification (MKTU) used for trademark registration, by keyword, and returns the class, code and name.
* **Suggest OKPD2 Code** `suggestOkpd2`: Suggests product and service codes from the OKPD-2 classifier by keyword or code fragment and returns the code, name and hierarchy.
* **Suggest OKPDTR Position** `suggestOkpdtrPosition`: Suggests employee positions (office roles) from the OKPDTR classifier by keyword and returns the code, name and OKZ code.
* **Suggest OKPDTR Profession** `suggestOkpdtrProfession`: Suggests worker professions (blue-collar roles) from the OKPDTR classifier by keyword and returns the code, name and OKZ code.
* **Suggest OKVED2 Code** `suggestOkved2`: Suggests economic activity codes from the OKVED-2 classifier by keyword or code fragment and returns the code, name and hierarchy.
* **Suggest Party** `suggestParty`: Searches Russian companies and individual entrepreneurs by INN, INN/KPP, OGRN, name, manager name or address and returns up to 20 matching suggestions with core registry data from the EGRUL/EGRIP registers.
* **Suggest Postal Unit** `suggestPostalUnit`: Suggests Russian Post offices by postal code or address and returns their code, address, type, opening hours and coordinates. Supports filtering by city KLADR code, unit type and closed status.
* **Suggest Tax Office** `suggestFnsUnit`: Suggests Russian tax offices (FNS inspectorates) by code, name or address and returns their code, name, address, payment details and contact information.

</details>
