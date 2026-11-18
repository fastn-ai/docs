---
description: "NamSor is a name-classification API that infers demographic attributes from personal names."
hidden: true
---

# NamSor

NamSor is a name-classification API that infers demographic attributes from personal names. This connector covers the NamSor API v2 classification surface: gender, country of origin and residence, ethnicity and diaspora, US race and ethnicity, religion, Indian caste and regional subclassification, phone country-code inference, name parsing, name-type detection, Chinese and Japanese romanization, transliteration and matching, and migration corridors, plus API key and usage reporting. Single-name and batch variants are provided for every classifier.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [namsor.com](https://namsor.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 104 |
| **Events** | 0 |
| **Slug** | `namsor` |

## Use it

Add NamSor from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.namsor.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get API Key Info | `apiKeyInfo` | Returns the settings attached to your NamSor API key, including its anonymization, learning, explainability and role flags. |
| Get Classifier Status | `apiStatus` | Returns the current status of every NamSor classifier, including whether it is serving requests and whether its probabilities are calibrated. A classifier name here corresponds to a service name returned by List API Services. |
| Get Classifier Taxonomy | `taxonomyClasses` | Returns the set of taxonomy classes a given NamSor classifier can output, so results can be validated or mapped downstream. |
| Get Current API Usage | `apiUsage` | Returns your current NamSor subscription plan, quota and unit usage for the running billing period. |
| Get Software Version | `softwareVersion` | Returns the current version of the NamSor classification software serving your requests. |
| Infer Community Engagement Profile | `communityEngage` | Infers ethnicity or diaspora, country of origin, country of residence, gender and US race and ethnicity for one person in a single call, for community engagement and outreach segmentation. Costs 20 units per name classified. |
| Infer Community Engagement Profile From Full Name | `communityEngageFull` | Infers ethnicity or diaspora, country of origin, country of residence, gender and US race and ethnicity for one person from their full name, for community engagement and outreach segmentation. Costs 20 units per name classified. |
| Infer Community Engagement Profiles (Batch) | `communityEngageBatch` | Infers ethnicity or diaspora, country of origin, country of residence, gender and US race and ethnicity for up to 100 people in a single request. Costs 20 units per name classified. |
| Infer Community Engagement Profiles From Full Names (Batch) | `communityEngageFullBatch` | Infers ethnicity or diaspora, country of origin, country of residence, gender and US race and ethnicity for up to 100 people from their full names. Costs 20 units per name classified. |
| Infer Countries Of Origin (Batch) | `originBatch` | Infers the likely country of origin of up to 100 people from their first and last names in a single request. Costs 10 units per name classified. |
| Infer Countries Of Origin From Full Names (Batch) | `originFullBatch` | Infers the likely country of origin of up to 100 people from their full names in a single request. Costs 10 units per name classified. |
| Infer Countries Of Residence (Batch) | `countryFnLnBatch` | Infers the likely country of residence of up to 100 people from their first and last names in a single request. Costs 10 units per name classified. |
| Infer Countries Of Residence From Full Names (Batch) | `countryBatch` | Infers the likely country of residence of up to 100 people from their full names in a single request. Costs 10 units per name classified. |
| Infer Country Of Origin | `origin` | Infers the likely country of origin of a person from their first and last name. Assumes the name is written as it is in the country of origin. For melting-pot countries such as the US, Canada, Australia and New Zealand, use the Infer Diaspora actions instead. Costs 10 units per name classified. |
| Infer Country Of Origin From Full Name | `originFull` | Infers the likely country of origin of a person from their full name. Assumes the name is written as it is in the country of origin. For melting-pot countries such as the US, Canada, Australia and New Zealand, use the Infer Diaspora actions instead. Costs 10 units per name classified. |
| Infer Country Of Residence | `countryFnLn` | Infers the likely country of residence of a person from their first and last name. Assumes the name is written as it is in the country of residence or the country of origin. Costs 10 units per name classified. |
| Infer Country Of Residence From Full Name | `country` | Infers the likely country of residence of a person from their full name or surname alone. Assumes the name is written as it is in the country of residence or the country of origin. Costs 10 units per name classified. |
| Infer Diaspora | `diaspora` | Infers the likely ethnicity or diaspora of a person from their first and last name, given their country of residence. Designed for melting-pot countries such as the US, Canada, Australia and New Zealand. Costs 20 units per name classified. |
| Infer Diaspora From Full Name | `diasporaFull` | Infers the likely ethnicity or diaspora of a person from their full name, given their country of residence. Designed for melting-pot countries such as the US, Canada, Australia and New Zealand. Costs 20 units per name classified. |
| Infer Diasporas (Batch) | `diasporaBatch` | Infers the likely ethnicity or diaspora of up to 100 people from their first and last names, each with its own country of residence. Costs 20 units per name classified. |
| Infer Diasporas From Full Names (Batch) | `diasporaFullBatch` | Infers the likely ethnicity or diaspora of up to 100 people from their full names, each with its own country of residence. Costs 20 units per name classified. |
| Infer Gender | `gender` | Infers the likely gender of a person from their first and last name, detecting the writing script automatically. |
| Infer Gender From First Name | `genderFirstNameOnly` | Infers the likely gender of a given name on its own, assuming a default US local context. For better accuracy prefer the full-name and country-aware gender actions. |
| Infer Gender From Full Name | `genderFull` | Infers the likely gender of a person from their full name, for example "John H. Smith", detecting the first and last name automatically. |
| Infer Gender From Full Name With Country | `genderFullGeo` | Infers the likely gender of a person from their full name, using a country of residence as local cultural context for better accuracy. |
| Infer Gender Of Chinese Name | `genderChineseName` | Infers the likely gender of a Chinese full name written in Chinese characters, for example 王晓明. |
| Infer Gender Of Japanese Full Name | `genderJapaneseNameFull` | Infers the likely gender of a Japanese full name written in Kanji, for example 山本 早苗. |
| Infer Gender Of Pinyin Chinese Name | `genderChineseNamePinyin` | Infers the likely gender of a Chinese name written in Latin script (Pinyin), for example Wang Xiaoming. |
| Infer Gender Of Romanized Japanese Name | `genderJapaneseName` | Infers the likely gender of a Japanese name written in Latin script, for example Yamamoto Sanae. |
| Infer Gender With Country | `genderGeo` | Infers the likely gender of a person from their first and last name, using a country of residence as local cultural context for better accuracy. |
| Infer Genders (Batch) | `genderBatch` | Infers the likely gender of up to 100 people from their first and last names in a single request, detecting the writing script automatically. |
| Infer Genders From Full Names (Batch) | `genderFullBatch` | Infers the likely gender of up to 100 people from their full names in a single request, detecting the first and last name automatically. |
| Infer Genders From Full Names With Country (Batch) | `genderFullGeoBatch` | Infers the likely gender of up to 100 people from their full names, each with its own country of residence as local cultural context. |
| Infer Genders Of Chinese Names (Batch) | `genderChineseNameBatch` | Infers the likely gender of up to 100 Chinese full names written in Chinese characters in a single request. |
| Infer Genders Of Japanese Full Names (Batch) | `genderJapaneseNameFullBatch` | Infers the likely gender of up to 100 Japanese full names written in Kanji in a single request. |
| Infer Genders Of Pinyin Chinese Names (Batch) | `genderChineseNamePinyinBatch` | Infers the likely gender of up to 100 Chinese names written in Latin script (Pinyin) in a single request. |
| Infer Genders Of Romanized Japanese Names (Batch) | `genderJapaneseNameBatch` | Infers the likely gender of up to 100 Japanese names written in Latin script in a single request. |
| Infer Genders With Country (Batch) | `genderGeoBatch` | Infers the likely gender of up to 100 people from their first and last names, each with its own country of residence as local cultural context. |
| Infer Indian Caste | `casteIndian` | Infers the likely caste of an Indian person from their first and last name, given an Indian state or union territory as local context. Costs 10 units per name classified. |
| Infer Indian Caste Group | `castegroupIndian` | Infers the likely caste group of an Indian person from their first and last name, given an Indian state or union territory as local context. Costs 10 units per name classified. |
| Infer Indian Caste Group From Full Name | `castegroupIndianFull` | Infers the likely caste group of an Indian person from their full name, given an Indian state or union territory as local context. Costs 10 units per name classified. |
| Infer Indian Caste Groups (Batch) | `castegroupIndianBatch` | Infers the likely caste group of up to 100 Indian people from their first and last names, each with its own state or union territory. Costs 10 units per name classified. |
| Infer Indian Caste Groups From Full Names (Batch) | `castegroupIndianFullBatch` | Infers the likely caste group of up to 100 Indian people from their full names, each with its own state or union territory. Costs 10 units per name classified. |
| Infer Indian Castes (Batch) | `casteIndianBatch` | Infers the likely caste of up to 100 Indian people from their first and last names, each with its own state or union territory. Costs 10 units per name classified. |
| Infer Indian Religion | `religionIndian` | Infers the likely religion of an Indian person from their first and last name, given an Indian state or union territory as local context. Costs 10 units per name classified. |
| Infer Indian Religion From Full Name | `religionIndianFull` | Infers the likely religion of an Indian person from their full name, given an Indian state or union territory as local context. Costs 10 units per name classified. |
| Infer Indian Religions (Batch) | `religionIndianBatch` | Infers the likely religion of up to 100 Indian people from their first and last names, each with its own Indian state or union territory. Costs 10 units per name classified. |
| Infer Indian Religions From Full Names (Batch) | `religionIndianFullBatch` | Infers the likely religion of up to 100 Indian people from their full names, each with its own Indian state or union territory. Costs 10 units per name classified. |
| Infer Indian State Subclassification | `subclassificationIndian` | Infers the likely Indian state or union territory a name originates from, returning an ISO 3166-2 subdivision code. Costs 10 units per name classified. |
| Infer Indian State Subclassification From Full Name | `subclassificationIndianFull` | Infers the likely Indian state or union territory a full name originates from, returning an ISO 3166-2 subdivision code. Costs 10 units per name classified. |
| Infer Indian State Subclassifications (Batch) | `subclassificationIndianBatch` | Infers the likely Indian state or union territory of origin for up to 100 names in a single request. Costs 10 units per name classified. |
| Infer Indian State Subclassifications From Full Names (Batch) | `subclassificationIndianFullBatch` | Infers the likely Indian state or union territory of origin for up to 100 full names in a single request. Costs 10 units per name classified. |
| Infer Migration Corridor | `corridor` | Infers gender, country of origin and diaspora for both sides of a cross-border interaction between two named people, such as a remittance, a trip or an international communication. Costs 20 units per name pair classified. |
| Infer Migration Corridors (Batch) | `corridorBatch` | Infers gender, country of origin and diaspora for both sides of up to 100 cross-border interactions between named people in a single request. Costs 20 units per name pair classified. |
| Infer Name Type | `nameType` | Infers the likely type of a proper noun, distinguishing a personal name from a brand name, a place name and other categories. |
| Infer Name Type With Country | `nameTypeGeo` | Infers the likely type of a proper noun using a country as local context, distinguishing a personal name from a brand name, a place name and other categories. |
| Infer Name Types (Batch) | `nameTypeBatch` | Infers the likely type of up to 100 proper nouns in a single request, distinguishing personal names from brand names, place names and other categories. |
| Infer Name Types With Country (Batch) | `nameTypeGeoBatch` | Infers the likely type of up to 100 proper nouns, each with its own country as local context, distinguishing personal names from brand names, place names and other categories. |
| Infer Phone Country Code | `phoneCode` | Infers the likely country and international dialling prefix for a phone number, using the person's name as additional signal and verifying the number with libphonenumber. Costs 11 units per name classified. |
| Infer Phone Country Code With Country | `phoneCodeGeo` | Infers the likely international dialling prefix for a phone number, using the person's name and a known country of residence as additional signal. Costs 11 units per name classified. |
| Infer Phone Country Codes (Batch) | `phoneCodeBatch` | Infers the likely country and international dialling prefix for up to 100 phone numbers in a single request, using each person's name as additional signal. Costs 11 units per name classified. |
| Infer Phone Country Codes With Country (Batch) | `phoneCodeGeoBatch` | Infers the likely international dialling prefix for up to 100 phone numbers in a single request, using each person's name and known country of residence as additional signal. Costs 11 units per name classified. |
| Infer Regional Subclassification | `subclassification` | Infers the likely regional or state origin of a name within a given country, returning an ISO 3166-2 subdivision code. Costs 10 units per name classified. |
| Infer Regional Subclassification From Full Name | `subclassificationFull` | Infers the likely regional or state origin of a full name within a given country, returning an ISO 3166-2 subdivision code. Costs 10 units per name classified. |
| Infer Regional Subclassifications (Batch) | `subclassificationBatch` | Infers the likely regional or state origin of up to 100 names, each within its own country, returning ISO 3166-2 subdivision codes. Costs 10 units per name classified. |
| Infer Regional Subclassifications From Full Names (Batch) | `subclassificationFullBatch` | Infers the likely regional or state origin of up to 100 full names, each within its own country, returning ISO 3166-2 subdivision codes. Costs 10 units per name classified. |
| Infer Religion | `religion` | Infers the likely religion of a person from their first and last name, given a country and state or region as local context. Costs 10 units per name classified. |
| Infer Religion From Full Name | `religionFull` | Infers the likely religion of a person from their full name, given a country and state or region as local context. Costs 10 units per name classified. |
| Infer Religions (Batch) | `religionBatch` | Infers the likely religion of up to 100 people from their first and last names, each with its own country and subdivision as local context. Costs 10 units per name classified. |
| Infer Religions From Full Names (Batch) | `religionFullBatch` | Infers the likely religion of up to 100 people from their full names, each with its own country and subdivision as local context. Costs 10 units per name classified. |
| Infer US Race And Ethnicity | `usRaceEthnicity` | Infers a US resident's likely race and ethnicity from their first and last name, using the six US Census categories. Costs 10 units per name classified. |
| Infer US Race And Ethnicity (Batch) | `usRaceEthnicityBatch` | Infers the likely US race and ethnicity of up to 100 residents from their first and last names in a single request. Costs 10 units per name classified. |
| Infer US Race And Ethnicity From Full Name | `usRaceEthnicityFull` | Infers a US resident's likely race and ethnicity from their full name, using the six US Census categories. Costs 10 units per name classified. |
| Infer US Race And Ethnicity From Full Names (Batch) | `usRaceEthnicityFullBatch` | Infers the likely US race and ethnicity of up to 100 residents from their full names in a single request. Costs 10 units per name classified. |
| Infer US Race And Ethnicity With ZIP Code | `usRaceEthnicityZIP5` | Infers a US resident's likely race and ethnicity from their first and last name together with their five-digit ZIP code, which sharpens the result with local demographic context. Costs 10 units per name classified. |
| Infer US Race And Ethnicity With ZIP Codes (Batch) | `usZipRaceEthnicityBatch` | Infers the likely US race and ethnicity of up to 100 residents from their names and ZIP codes in a single request, using local demographic context. Costs 10 units per name classified. |
| List API Services | `apiServices` | Lists every NamSor classification service together with its usage cost in units per classification. Some endpoints, such as Infer Migration Corridor, combine several classifiers and therefore cost more. |
| List Regions | `regions` | Returns basic statistics about the geographic regions and country groupings NamSor uses in its classifications. |
| Match Chinese Name To Romanized Name | `chineseNameMatch` | Scores whether a Chinese name written in Chinese characters corresponds to a given romanized Pinyin name, returning Match or Mismatch. |
| Match Chinese Names To Romanized Names (Batch) | `chineseNameMatchBatch` | Scores up to 100 pairs of a romanized Pinyin name and a Chinese-character name in a single request, returning Match or Mismatch for each. |
| Match Japanese Kanji Name To Romanized Name | `japaneseNameMatch` | Scores whether a Japanese name written in Kanji corresponds to a given romanized name, returning Match or Mismatch. |
| Match Japanese Kanji Names To Romanized Names (Batch) | `japaneseNameMatchBatch` | Scores up to 100 pairs of a romanized Japanese name and a Kanji name in a single request, returning Match or Mismatch for each. |
| Parse Chinese Name | `parseChineseName` | Splits a Chinese name written in Chinese characters into its surname and given name, for example 王晓明 into 王 as surname and 晓明 as given name. |
| Parse Chinese Names (Batch) | `parseChineseNameBatch` | Splits up to 100 Chinese names written in Chinese characters into their surname and given name in a single request. |
| Parse Japanese Name | `parseJapaneseName` | Splits a Japanese name into its surname and given name, accepting either Kanji such as 山本 早苗 or a romanized form such as Yamamoto Sanae. |
| Parse Japanese Names (Batch) | `parseJapaneseNameBatch` | Splits up to 100 Japanese names into their surname and given name in a single request, accepting either Kanji or romanized forms. |
| Parse Name | `parseName` | Splits a full name into its first and last name components, detecting the name order automatically, for example "John Smith" or "Smith, John". |
| Parse Name With Country | `parseNameGeo` | Splits a full name into its first and last name components using a country as local cultural context, which improves name-order detection. |
| Parse Names (Batch) | `parseNameBatch` | Splits up to 100 full names into their first and last name components in a single request, detecting the name order automatically. |
| Parse Names With Country (Batch) | `parseNameGeoBatch` | Splits up to 100 full names into their first and last name components, each with its own country as local cultural context. |
| Romanize Chinese Name To Pinyin | `pinyinChineseName` | Romanizes a Chinese name written in Chinese characters into Pinyin and splits it into surname and given name, for example 王晓明 into Wang as surname and Xiaoming as given name. |
| Romanize Chinese Names To Pinyin (Batch) | `pinyinChineseNameBatch` | Romanizes up to 100 Chinese names written in Chinese characters into Pinyin and splits each into surname and given name. |
| Romanize Japanese Kanji Name | `japaneseNameLatinCandidates` | Suggests the most likely romanized readings for a Japanese name written in Kanji, for example 山本 早苗, ranked by probability. |
| Romanize Japanese Kanji Names (Batch) | `japaneseNameLatinCandidatesBatch` | Suggests the most likely romanized readings for up to 100 Japanese names written in Kanji in a single request. |
| Submit Japanese Name Match Feedback | `japaneseNameMatchFeedbackLoop` | Submits a confirmed match between a romanized Japanese name and its Kanji spelling back to NamSor so that future matching improves. This call credits one unit rather than spending one. |
| Submit Phone Country Code Feedback | `phoneCodeGeoFeedbackLoop` | Submits a verified E.164 phone number for a person back to NamSor so that future phone country code inference improves. This call credits one unit rather than spending one. |
| Suggest Chinese Name Candidates | `chineseNameCandidates` | Suggests the most likely Chinese-character spellings for a romanized Pinyin name, for example Wang Xiaoming, ranked by probability. |
| Suggest Chinese Name Candidates (Batch) | `chineseNameCandidatesBatch` | Suggests the most likely Chinese-character spellings for up to 100 romanized Pinyin names in a single request. |
| Suggest Chinese Name Candidates By Gender | `chineseNameGenderCandidates` | Suggests the most likely Chinese-character spellings for a romanized Pinyin name, narrowed by the person's known gender. |
| Suggest Chinese Name Candidates By Gender (Batch) | `chineseNameCandidatesGenderBatch` | Suggests the most likely Chinese-character spellings for up to 100 romanized Pinyin names, each narrowed by the person's known gender. |
| Suggest Japanese Kanji Name Candidates | `japaneseNameKanjiCandidates` | Suggests the most likely Kanji spellings for a romanized Japanese name, for example Yamamoto Sanae, ranked by probability. |
| Suggest Japanese Kanji Name Candidates (Batch) | `japaneseNameKanjiCandidatesBatch` | Suggests the most likely Kanji spellings for up to 100 romanized Japanese names in a single request. |
| Suggest Japanese Kanji Name Candidates By Gender | `japaneseNameKanjiCandidatesByGender` | Suggests the most likely Kanji spellings for a romanized Japanese name, narrowed by the person's known gender. |
| Suggest Japanese Kanji Name Candidates By Gender (Batch) | `japaneseNameGenderKanjiCandidatesBatch` | Suggests the most likely Kanji spellings for up to 100 romanized Japanese names, each narrowed by the person's known gender. |
