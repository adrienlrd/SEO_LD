# PROGRESS — SEO Leoniedelacroix.com

## État global
- Phase actuelle : Phase 2 — Recommandations & Application supervisée
- Dernière session : 2026-05-05
- Prochain objectif : Lancer le premier audit réel → `crawl_shopify` + `generate_report`

## ✅ Terminé

### Infrastructure
- Initialisation repo Git + structure dossiers
- Création CLAUDE.md avec contexte projet complet
- Setup credentials API : Shopify token, Google OAuth, PageSpeed key, GA4 Property ID
- `.env`, `.env.example`, `.gitignore` configurés
- `pyproject.toml` avec `[tool.setuptools]` pour discovery correcte

### Phase 1 — Fondations & Audit (tâches 1–15) ✅
- `config/seo_rules.yaml` — règles métier (longueurs, poids scoring)
- `config/keywords.yaml` — 25 mots-clés cibles par catégorie
- `scripts/models.py` — modèles Pydantic partagés (`Issue`, `SEOScore`, `Severity`)
- `scripts/audit/crawl_shopify.py` — GraphQL paginé, snapshot JSON + SQLite
- `scripts/audit/fetch_gsc.py` — OAuth navigateur, export 90j par URL → CSV
- `scripts/audit/fetch_pagespeed.py` — score mobile/desktop + CWV → CSV
- `scripts/audit/parse_screaming_frog.py` — parser overview/images/redirects CSV
- `scripts/audit/detect_issues.py` — 5 détecteurs : titles, descriptions, alt text, duplicates, redirects/404
- `scripts/report/generate_report.py` — score /100 pondéré + rapport Markdown horodaté
- `scripts/apply/update_meta.py` — mutation GraphQL, `--dry-run` par défaut, confirmation humaine
- `data/history.db` initialisé via `init_db()` (SQLite, 2 tables)
- 29 tests unitaires — 29/29 ✅ — ruff clean ✅

## ⏳ À faire (Phase 2)
- [ ] Lancer le premier audit réel : `crawl_shopify` + `generate_report`
- [ ] Matrice ICE — priorisation issues (tâche 16)
- [ ] Générateur meta titles optimisés (tâche 17)
- [ ] Générateur meta descriptions optimisées (tâche 18)
- [ ] Générateur alt text intelligent (tâche 19)
- [ ] `update_meta.py --apply` — pousser les corrections validées (tâche 20)

## 🚧 Blocages / Questions ouvertes
- Premier run `fetch_gsc` : ouvrira un navigateur pour consentement OAuth
- `fetch_pagespeed` : 1 appel par URL × 2 (mobile + desktop) → ~3s par URL

## 📋 Historique des sessions

### Session 2026-05-05
- Phase 1 complète en une session
- 14 fichiers créés : 2 YAML config, 1 models.py, 4 scripts audit, 1 detect_issues, 1 generate_report, 1 update_meta, 5 tests
- pyproject.toml corrigé (`[tool.setuptools]` packages discovery)
- `Severity` migré vers `StrEnum` (Python 3.11+)
- 29/29 tests verts, ruff clean

### Session 2026-04-28
- Setup Google Cloud terminé : projet `leonie-seo`, 3 APIs activées, OAuth client créé
- Bascule service account → OAuth utilisateur (Search Console refusait le service account)
- GA4 Property ID récupéré et ajouté au .env

### Session 2026-04-22
- Custom App Shopify créée, token obtenu, .env configuré

### Session 2026-04-20
- Initialisation complète du projet SEO_LD
