---
description: "Recherche d'entreprises is the French government company directory. Search French companies by name or near a location."
hidden: true
---

# Recherche d'entreprises

<img src="../../.gitbook/assets/connectors/lg/recherche-entreprises.png" alt="Recherche d'entreprises logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr) |
| **Authentication** | No sign-in needed |
| **Slug** | `rechercheEntreprises` |

## Setup

Recherche d'entreprises needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Recherche d'entreprises from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Recherche d'entreprises**.
2. Select **Connect** on the Recherche d'entreprises card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Recherche d'entreprises needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Recherche d'entreprises's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Companies</td><td><code>searchCompanies</code></td><td>Recherche textuelle. Cet endpoint permet de récupérer les unités légales et les établissements correspondants à la recherche effectuée sur la dénomination, l'adresse, les dirigeants et les élus. Ou bien par numéro SIREN / SIRET. **Deux modes de recherche selon la valeur du paramètre `q`:** - **Recherche textuelle classique** (dénomination, adresse, dirigeants, élus): tous les filtres optionnels (`code_commune`, `code_postal`, `departement`, `region`, `epci`, etc.) sont appliqués en combinaison avec la recherche. - **Recherche directe par SIREN ou SIRET**: si `q` contient exactement 9 chiffres (SIREN) ou 14 chiffres (SIRET), l'API effectue une recherche directe et **ignore tous les autres filtres**. Combiner un SIREN ou SIRET avec des filtres géographiques ou thématiques ne produira pas d'erreur, mais ces filtres seront silencieusement ignorés. Docs: https://recherche-entreprises.api.gouv.fr/docs/</td></tr><tr><td>Search Companies Near a Point</td><td><code>searchCompaniesNearPoint</code></td><td>Recherche géographique. Cet endpoint prend en paramètre une latitude (:lat) et une longitude (:long) et renvoie les unités légales et leurs établissements autour de ces coordonnées. Vous pouvez également préciser un paramètre radius en km(défaut: 5 km). **Paramètres d'appel:** latitude, longitude, radius, activité principale et section d'activité principale de l'entreprise. Docs: https://recherche-entreprises.api.gouv.fr/docs/</td></tr></tbody></table>

