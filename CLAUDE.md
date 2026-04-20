# Projet SEO — Leoniedelacroix.com

## Contexte
Site Shopify, produits chien et chat, marché français.
Positionnement : niche premium santé, fabriqué en France, longue traîne.
URL : https://www.leoniedelacroix.com
Domaine :  287c4a-bb.myshopify.com
## Stack technique imposée
- Python 3.11+ uniquement (pas de JS/TS sauf si indispensable pour MCP)
- Shopify Admin API GraphQL (API version 2025-01 minimum)
- Google Search Console API
- PageSpeed Insights API
- Ahrefs Webmaster Tools API
- GA4 Data API
- Screaming Frog Free (lancement manuel, parsing CSV export)
- SQLite (historique, via sqlite3 stdlib)
- GitHub Actions (cron hebdo)

## MCP servers installés
- @shopify/dev-mcp (officiel Shopify, documentation + schema)
- shopify-mcp de GeLi2001 (mutations CRUD produits/metafields)

## Dépendances Python autorisées
requests, pandas, python-dotenv, pydantic, click, rich,
google-auth, google-api-python-client, pyyaml.
Demander confirmation avant d'ajouter toute autre lib.

## Règles de comportement (NON NÉGOCIABLES)
1. **Plan avant code.** Toute tâche > 15 lignes commence par un plan
   en bullet points, validé par l'utilisateur.
2. **Mode dry-run par défaut.** Tout script qui modifie Shopify doit
   avoir --dry-run comme comportement par défaut et --apply explicite.
3. **Confirmation humaine obligatoire** avant chaque appel en écriture
   sur Shopify pendant les 3 premiers mois du projet.
4. **Jamais de secrets en dur.** Tout va dans .env, .env.example tenu
   à jour, .gitignore vérifié avant chaque commit.
5. **Français uniquement** dans les commits, commentaires, rapports,
   docstrings, messages CLI.
6. **Commits atomiques.** Un commit = une fonctionnalité. Format
   conventionnel : feat:, fix:, docs:, refactor:, chore:.
7. **Tests minimaux.** Pour chaque fonction qui touche une API,
   au moins un test unitaire avec réponse mockée.
8. **Pas d'hallucination de données.** Si une info manque, le script
   lève une exception explicite au lieu de deviner.
9. **Mise à jour PROGRESS.md obligatoire** en fin de chaque session :
   tâches complétées, tâches restantes, blocages éventuels.

## Arborescence du repo
SEO_LD/
├── CLAUDE.md                  # ce fichier
├── README.md                  # documentation usage
├── .env.example               # template secrets
├── .gitignore
├── pyproject.toml             # deps + config
├── requirements.txt
├── config/
│   ├── keywords.yaml          # mots-clés cibles par thème
│   └── seo_rules.yaml         # règles métier (longueurs meta, etc.)
├── scripts/
│   ├── audit/                 # lecture seule
│   │   ├── crawl_shopify.py
│   │   ├── fetch_gsc.py
│   │   ├── fetch_pagespeed.py
│   │   └── detect_issues.py
│   ├── apply/                 # écriture Shopify (--dry-run par défaut)
│   │   ├── update_meta.py
│   │   ├── update_alt_text.py
│   │   ├── create_redirects.py
│   │   └── add_schema.py
│   └── report/
│       └── generate_report.py
├── data/
│   ├── raw/                   # exports bruts (gitignored)
│   └── history.db             # SQLite
├── reports/                   # rapports Markdown horodatés
│   └── YYYY-MM-DD/
└── .github/
└── workflows/
└── weekly_audit.yml

## Commandes fréquentes
- `python -m scripts.audit.crawl_shopify` : crawl complet Shopify
- `python -m scripts.report.generate_report --week` : rapport hebdo
- `python -m scripts.apply.update_meta --dry-run --collection=croquettes-chien`
- `python -m scripts.apply.update_meta --apply --collection=croquettes-chien`

## Historique des décisions
(Claude Code remplit cette section à chaque choix structurant)

