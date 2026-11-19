---
description: "Connect Recherche d'entreprises to your product with fastn."
hidden: true
---

# Recherche d'entreprises

<img src="../../.gitbook/assets/connectors/lg/recherche-entreprises.png" alt="Recherche d'entreprises logo">

Recherche d'entreprises is the French government's free company search API (Annuaire des Entreprises): find French companies, associations and public bodies by name, SIREN/SIRET, address, executive, activity code, size, labels and finances, or near a GPS point, with their establishments and directors. No API key needed.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr) |
| **Authentication** | No authentication |
| **Slug** | `rechercheEntreprises` |

## Use it

Add Recherche d'entreprises from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rechercheEntreprises.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Companies</td><td><code>searchCompanies</code></td><td>Recherche textuelle. Cet endpoint permet de récupérer les unités légales et les établissements correspondants à la recherche effectuée sur la dénomination, l'adresse, les dirigeants et les élus. Ou bien par numéro SIREN / SIRET. **Deux modes de recherche selon la valeur du paramètre `q` :** - **Recherche textuelle classique** (dénomination, adresse, dirigeants, élus) : tous les filtres optionnels (`code_commune`, `code_postal`, `departement`, `region`, `epci`, etc.) sont appliqués en combinaison avec la recherche. - **Recherche directe par SIREN ou SIRET** : si `q` contient exactement 9 chiffres (SIREN) ou 14 chiffres (SIRET), l'API effectue une recherche directe et **ignore tous les autres filtres**. Combiner un SIREN ou SIRET avec des filtres géographiques ou thématiques ne produira pas d'erreur, mais ces filtres seront silencieusement ignorés. Docs: https://recherche-entreprises.api.gouv.fr/docs/ (GET /search)</td></tr><tr><td>Search Companies Near a Point</td><td><code>searchCompaniesNearPoint</code></td><td>Recherche géographique. Cet endpoint prend en paramètre une latitude (:lat) et une longitude (:long) et renvoie les unités légales et leurs établissements autour de ces coordonnées. Vous pouvez également préciser un paramètre radius en km(défaut: 5 km). **Paramètres d'appel :** latitude, longitude, radius, activité principale et section d'activité principale de l'entreprise. Docs: https://recherche-entreprises.api.gouv.fr/docs/ (GET /near_point)</td></tr></tbody></table>
