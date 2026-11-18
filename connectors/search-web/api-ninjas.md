---
description: "Aggregator of ~139 free micro-APIs from API Ninjas covering financial data lookups, identity/validation utilities (email, phone, IBAN, VIN, routing numbers),…"
hidden: true
---

# API Ninjas

Aggregator of ~139 free micro-APIs from API Ninjas covering financial data lookups, identity/validation utilities (email, phone, IBAN, VIN, routing numbers), text and language processing, AI (sentiment, embeddings, image analysis), geography/weather, and a large catalog of fun/reference data (facts, quotes, animals, recipes) - all authenticated with a single API key.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [api-ninjas.com](https://api-ninjas.com) |
| **Authentication** | API key |
| **Actions** | 136 |
| **Events** | 0 |
| **Slug** | `apiNinjas` |

## Use it

Add API Ninjas from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.apiNinjas.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Analyze Text Sentiment | `getSentiment` | Analyzes the sentiment of a piece of text and returns a sentiment label and confidence score. |
| Calculate Income Tax | `calculateIncomeTax` | Calculates estimated income tax owed given a country, region, income amount, and filing status. |
| Calculate Mortgage Payment | `calculateMortgage` | Calculates estimated monthly and annual mortgage payments given a loan amount, interest rate, and loan duration. |
| Calculate Sales Tax | `calculateSalesTax` | Calculates the sales tax amount and total for a purchase given a US zip code and pre-tax amount. |
| Check Disposable Email | `checkDisposableEmail` | Checks whether an email address belongs to a known disposable/temporary email domain. |
| Check Spelling | `checkSpelling` | Checks spelling in a piece of text and returns corrections for misspelled words. |
| Compare Text Similarity | `compareTextSimilarity` | Compares two pieces of text and returns a semantic similarity score between 0 and 1. |
| Convert Currency | `convertCurrency` | Converts an amount from one currency to another using live exchange rates. Note: on the API Ninjas free tier most currency pairs on this endpoint are premium-gated and return an error. |
| Convert Unit | `convertUnit` | Converts a numeric amount from one unit of measurement to all equivalent units in the same category. |
| Detect Text Language | `detectTextLanguage` | Detects the language of a piece of text. |
| Filter Profanity | `filterProfanity` | Detects and censors profanity within a piece of text. |
| Find EV Charging Stations | `findEvChargers` | Finds electric vehicle charging stations near a given latitude/longitude location. |
| Find Hospitals | `findHospitals` | Searches for US hospitals by state and/or name. |
| Find Rhyming Words | `findRhymes` | Returns a list of words that rhyme with a given word. |
| Generate Barcode | `generateBarcode` | Generates a barcode image encoding the given text in a specified barcode format. |
| Generate Lorem Ipsum Text | `generateLoremIpsum` | Generates placeholder Lorem Ipsum text with a specified number of paragraphs. |
| Generate QR Code | `generateQrCode` | Generates a QR code image encoding the given data string. |
| Generate Random Password | `generatePassword` | Generates a cryptographically random password of a specified length. |
| Generate Random User Agent | `generateUserAgent` | Generates a random, realistic browser User-Agent string, optionally constrained by OS and browser. |
| Generate Sudoku Puzzle | `generateSudoku` | Generates a Sudoku puzzle of a specified difficulty level. |
| Generate Text Embedding | `generateTextEmbedding` | Generates a 768-dimensional vector embedding that encodes the semantic meaning of input text. |
| Geocode City | `geocodeAddress` | Converts a city name into geographic latitude/longitude coordinates. |
| Get Air Quality Index | `getAirQuality` | Returns current air quality index (AQI) and pollutant concentrations for a given city. |
| Get Aircraft Specifications | `getAircraftSpecs` | Returns technical specifications for aircraft matching a manufacturer and/or model. |
| Get Animal Information | `getAnimalFacts` | Returns taxonomy, habitat, and characteristics information for an animal by name. |
| Get Average Mortgage Rate | `getMortgageRate` | Returns the current average 30-year and 15-year fixed mortgage rates in the US. |
| Get Baby Names | `getBabyNames` | Returns a list of popular baby names filtered by gender. |
| Get Balance Sheet | `getBalanceSheet` | Returns balance sheet data (assets, liabilities, equity) for a publicly traded US company by stock ticker symbol. |
| Get Bank Holidays | `getBankHolidays` | Returns official bank holidays for a given country. |
| Get Bitcoin Price | `getBitcoinPrice` | Returns the current real-time Bitcoin (BTC) price in USD along with 24-hour price change statistics. |
| Get Bucket List Idea | `getBucketListIdea` | Returns a random bucket list idea/activity suggestion. |
| Get Calories Burned | `getCaloriesBurned` | Estimates calories burned per hour for a given physical activity. |
| Get Car Specifications | `getCarSpecs` | Returns technical specifications for cars matching a make and model. |
| Get Cash Flow Statement | `getCashFlow` | Returns cash flow statement data (operating, investing, financing activities) for a publicly traded US company by stock ticker symbol. |
| Get Cat Breed Information | `getCatBreed` | Returns physical and behavioral characteristics for a cat breed by name. |
| Get Celebrity Information | `getCelebrityInfo` | Returns biographical and net worth information for a celebrity by name. |
| Get Central Bank Interest Rates | `getInterestRates` | Returns current central bank interest rates for major economies around the world. |
| Get Chuck Norris Joke | `getChuckNorrisJoke` | Returns a random Chuck Norris joke. |
| Get City Information | `getCityInfo` | Returns geographic and demographic information for a city by name. |
| Get Cocktail Recipe | `getCocktailRecipe` | Returns ingredients and preparation instructions for a cocktail by name. |
| Get Commodity Price | `getCommodityPrice` | Returns the current market price for a commodity futures contract (e.g. gold, wheat, corn, natural gas). |
| Get Company Earnings | `getEarnings` | Returns historical earnings and income statement summary data for a publicly traded company by ticker symbol. |
| Get Company Logo | `getCompanyLogo` | Returns a company's logo image URL by company name. |
| Get Country Flag | `getCountryFlag` | Returns image URLs for a country's flag by ISO country code. |
| Get Country Information | `getCountryInfo` | Returns economic and demographic statistics for a country by name. |
| Get Country Population | `getPopulation` | Returns historical and projected population data for a given country. |
| Get COVID-19 Statistics | `getCovidStats` | Returns historical daily COVID-19 case statistics for a given country. |
| Get Crypto Price | `getCryptoPrice` | Returns the current price for a cryptocurrency trading pair. Note: on the API Ninjas free tier this endpoint has been observed down for free users and returns an error. |
| Get Currency Volatility | `getCurrencyVolatility` | Returns historical volatility statistics for a currency pair. Note: on the API Ninjas free tier this endpoint is entirely premium-gated and returns an error for all callers. |
| Get Current Weather | `getWeather` | Returns current weather conditions for a given latitude/longitude location. |
| Get Dad Joke | `getDadJoke` | Returns a random dad joke. |
| Get Daily Horoscope | `getHoroscope` | Returns the daily horoscope reading for a given zodiac sign. |
| Get Day In History | `getDayInHistory` | Returns a notable historical event that occurred on today's date (or the current day/month). |
| Get Dictionary Definition | `getDictionaryDefinition` | Returns the dictionary definition of an English word. |
| Get Dog Breed Information | `getDogBreed` | Returns physical and behavioral characteristics for a dog breed by name. |
| Get Earnings Calendar | `getEarningsCalendar` | Returns upcoming and historical earnings report dates for a publicly traded company by ticker symbol. |
| Get Earnings Call Transcript | `getEarningsCallTranscript` | Returns the full text transcript of a company's quarterly earnings call. Note: on the API Ninjas free tier this endpoint is entirely premium-gated and returns an error for all callers. |
| Get Electric Vehicle Info | `getElectricVehicle` | Returns specifications for electric vehicle models by manufacturer. |
| Get ETF Information | `getEtfInfo` | Returns information about an Exchange Traded Fund (ETF) by ticker symbol, including name, ISIN, and country. |
| Get Exchange Rate | `getExchangeRate` | Returns the current exchange rate for a currency pair. Note: on the API Ninjas free tier most currency pairs on this endpoint are premium-gated and return an error. |
| Get Executive Compensation | `getExecutiveCompensation` | Returns executive compensation data (names, positions, pay) for a publicly traded company by ticker symbol. |
| Get Exercises By Muscle | `getExercises` | Returns a list of exercises targeting a given muscle group, with instructions and difficulty. |
| Get Exoplanet Data | `getExoplanets` | Returns data on known exoplanets, optionally filtered by minimum mass. |
| Get GDP Data | `getGdp` | Returns historical GDP data for a given country. |
| Get Gold Price | `getGoldPrice` | Returns the current spot price of gold per troy ounce. Note: on the API Ninjas free tier this endpoint is entirely premium-gated and returns an error for all callers. |
| Get Helicopter Specifications | `getHelicopterSpecs` | Returns technical specifications for helicopters matching a manufacturer. |
| Get Historical Events | `getHistoricalEvents` | Returns historical events matching a given year and/or month. |
| Get Historical Figure Info | `getHistoricalFigure` | Returns biographical information about a historical figure by name. |
| Get Holidays | `getHolidays` | Returns holidays (public, religious, and observances) for a given country. |
| Get Income Statement | `getIncomeStatement` | Returns income statement data (revenue, net income, EPS) for a publicly traded US company by ticker symbol. |
| Get Income Tax Brackets | `getIncomeTax` | Returns income tax bracket data for a given country and tax year. |
| Get Inflation Rate | `getInflationRate` | Returns historical inflation rate data for a given country. Note: on the API Ninjas free tier this endpoint is entirely premium-gated and returns an error for all callers. |
| Get Insider Transactions | `getInsiderTransactions` | Returns SEC-reported insider trading transactions (Form 4 filings) for a publicly traded company by ticker symbol. |
| Get Institutional Holdings | `getInstitutionalHoldings` | Returns institutional stock holdings data by company CIK number or manager name (13F filings). |
| Get IPO Calendar | `getIpoCalendar` | Returns a calendar of upcoming and recent Initial Public Offerings (IPOs). |
| Get LIBOR Rate | `getLiborRate` | Returns historical LIBOR interest rate data for a given currency. Note: on the API Ninjas free tier this endpoint is entirely premium-gated and returns an error for all callers. |
| Get Market Capitalization | `getMarketCap` | Returns the current market capitalization for a publicly traded company by ticker symbol. |
| Get Motorcycle Specifications | `getMotorcycleSpecs` | Returns technical specifications for motorcycles matching a make. |
| Get Mutual Fund Information | `getMutualFund` | Returns information about a mutual fund by ticker symbol, including name, ISIN, and expense ratio. |
| Get Nutrition Information | `getNutritionInfo` | Returns nutritional information (calories, fat, protein, etc.) for a natural-language food query. |
| Get Oil Price | `getOilPrice` | Returns the current WTI crude oil price per barrel. |
| Get Property Tax Rate | `getPropertyTax` | Returns average property tax rates for a given US city and state. |
| Get Public Holidays | `getPublicHolidays` | Returns official public holidays for a given country. |
| Get Random Advice | `getAdvice` | Returns a random piece of life advice. |
| Get Random Fact | `getRandomFact` | Returns a random interesting trivia fact. |
| Get Random Hobby Idea | `getRandomHobby` | Returns a random hobby idea/suggestion with a category and reference link. |
| Get Random Image | `getRandomImage` | Returns a random stock photo image, optionally filtered by category. |
| Get Random Joke | `getRandomJoke` | Returns a random joke. |
| Get Random Quote | `getRandomQuote` | Returns a random inspirational or famous quote. |
| Get Random Riddle | `getRandomRiddle` | Returns a random riddle with its answer. |
| Get Random User Profile | `getRandomUser` | Generates a random fake user profile (name, email, address). |
| Get Random Word | `getRandomWord` | Returns a random English word. |
| Get Sales Tax Rate | `getSalesTax` | Returns the sales tax rate (state, city, county, combined) for a given US zip code. |
| Get SEC Filings | `getSecFilings` | Returns links to SEC filings (10-K, 10-Q, 8-K, etc.) for a publicly traded company by ticker symbol and filing type. |
| Get Star Data | `getStars` | Returns astronomical data about stars filtered by distance range in light years. |
| Get Stock Exchange Info | `getStockExchange` | Returns information about a stock exchange by name, including MIC code, city, and country. |
| Get Stock News | `getStockNews` | Returns recent news articles related to a stock ticker. Note: on the API Ninjas free tier this endpoint is entirely premium-gated and returns an error for all callers. |
| Get Stock Price | `getStockPrice` | Returns the current stock price for a publicly traded company by ticker symbol. |
| Get Stock Split History | `getStockSplitHistory` | Returns historical stock split events for a publicly traded company by ticker symbol. |
| Get Thesaurus Synonyms | `getThesaurusSynonyms` | Returns synonyms and antonyms for a given word. |
| Get Ticker Company Info | `getTickerInfo` | Returns detailed company profile information (CEO, address, description) for a stock ticker symbol. |
| Get Timezone Info | `getTimezone` | Returns UTC offset and local time information for a given IANA timezone name. |
| Get Trivia Question | `getTriviaQuestion` | Returns a random trivia question with its answer. |
| Get Unemployment Rate | `getUnemploymentRate` | Returns historical unemployment rate data for a given country. |
| Get University Information | `getUniversity` | Returns information about universities matching a given name. |
| Get US County Information | `getCountyInfo` | Returns geographic information about a US county by name and state. |
| Get VAT Rate | `getVatRate` | Returns Value Added Tax (VAT) rate information for a given country. |
| Get Webpage Metadata | `getWebpageMetadata` | Extracts SEO metadata (title, description, meta tags) from a given webpage URL. |
| Get Working Days Count | `getWorkingDays` | Calculates the number of working (business) days between two dates for a given country. |
| Get World Time | `getWorldTime` | Returns the current date and time for a given IANA timezone. |
| Increment Counter | `incrementCounter` | Increments and returns the current value of a named persistent counter. |
| Lookup Australian BSB | `lookupBsb` | Looks up an Australian bank BSB (Bank State Branch) number and returns the associated branch details. |
| Lookup Canada Routing Number | `lookupCanadaRoutingNumber` | Looks up Canadian bank routing/transit number details, including institution and branch numbers. |
| Lookup Canadian Postal Code | `lookupPostalCode` | Looks up geographic details for a Canadian postal code. |
| Lookup Card BIN | `lookupBin` | Looks up card issuer information (brand, type, country) for a given bank identification number (BIN/IIN). |
| Lookup DNS Records | `lookupDns` | Looks up DNS records (A, AAAA, MX, TXT, etc.) for a given domain. |
| Lookup Domain Availability | `lookupDomain` | Checks whether a domain name is registered/available and returns registration details. |
| Lookup IBAN | `lookupIban` | Validates an International Bank Account Number (IBAN) and returns bank/branch details. |
| Lookup IP Address | `lookupIp` | Returns geolocation information (country, region, city) for a given IP address. |
| Lookup MX Records | `lookupMx` | Looks up mail exchange (MX) records for a given domain. |
| Lookup SWIFT/BIC Code | `lookupSwiftCode` | Looks up a bank's SWIFT/BIC code and returns the associated bank name and address. |
| Lookup UK Sort Code | `lookupSortCode` | Looks up a UK bank sort code and returns the associated bank branch details. |
| Lookup URL Geolocation | `lookupUrl` | Resolves a URL's hosting IP address and returns its geolocation information. |
| Lookup US Routing Number | `lookupRoutingNumber` | Looks up a US bank routing/ABA number and returns the associated bank's details. |
| Lookup US Zip Code | `lookupZipCode` | Looks up geographic details for a US zip code. |
| Lookup Vehicle VIN | `lookupVin` | Decodes a Vehicle Identification Number (VIN) into manufacturer, model, and specification details. |
| Lookup WHOIS Record | `lookupWhois` | Returns WHOIS registration data for a given domain name. |
| Reverse Geocode Coordinates | `reverseGeocode` | Converts latitude/longitude coordinates into a place name and country. |
| Scrape Webpage HTML | `scrapeWebpage` | Fetches and returns the raw HTML content of a given webpage URL. |
| Screen Sanctions Lists | `screenSanctions` | Screens a name against global sanctions and watch lists (e.g. OFAC SDN) for potential matches. |
| Search Airports | `getAirports` | Searches for airports by IATA code, country, or other filters. |
| Search Emoji | `getEmoji` | Searches for emoji characters matching a given name or keyword. |
| Search Recipe | `searchRecipe` | Searches for recipes matching a natural-language query, returning ingredients and servings. |
| Validate Email Address | `validateEmail` | Validates an email address format and deliverability, and flags disposable addresses. |
| Validate Phone Number | `validatePhone` | Validates a phone number and returns formatting, country, and timezone information. |
| Validate VAT Number | `validateVat` | Validates a European VAT registration number and returns its format/checksum validity status. |
