# PROGRESS — SEO Leoniedelacroix.com

## État global
- Phase actuelle : Phase 3 — Analyse des données & Optimisations ciblées
- Dernière session : 2026-05-05
- Prochain objectif : Améliorer les pages à fort potentiel identifiées par GSC

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
- `data/history.db` initialisé via `init_db()` (SQLite, 2 tables : `snapshots`, `seo_changes`)
- 49 tests unitaires — 49/49 ✅ — ruff clean ✅

### Phase 2 — Optimisations appliquées sur Shopify ✅
- `scripts/apply/generate_suggestions.py` — générateur règle-based : méta titres (50–65 chars), descriptions (120–155 chars), alt texts (≤125 chars)
- `scripts/apply/update_alt_text.py` — mutation `productImageUpdate`, dry-run par défaut
- **26 méta titres + descriptions poussés** sur Shopify (19 produits + 7 collections) — 0 erreur
- **17 alt texts d'images poussés** sur Shopify — 0 erreur
- Correction automatique "Léonie de la Croix" → "Léonie Delacroix" sur titre existant
- Logging SQLite de chaque changement dans `seo_changes` (69 entrées, rollback possible)
- Garde-fou 429 : boucle itérative max 3 tentatives (remplace récursion infinie)

### Phase 3 — Données GSC connectées ✅
- `fetch_gsc.py` connecté et fonctionnel (OAuth validé, test user ajouté)
- `GSC_SITE_URL=https://www.leoniedelacroix.com` ajouté au `.env`
- **50 URLs, 90 jours** de données récupérées : 245 clics · 3 736 impressions · CTR 10.3% · position moyenne 6.0

## ⏳ À faire — Court terme (gains rapides)

### Corrections manuelles dans l'admin Shopify
- [ ] **6 méta titres trop courts** (existaient déjà avant nos modifs, hors portée du script) :
  - Bol Félin Raffiné (42 chars)
  - L'abreuvoir (45 chars)
  - Griffoir Dimitrios (47 chars)
  - Distributeur Pet Feeder (48 chars)
  - La Fontaine Smart — suffixe "Fontaine Smart" à remplacer par "Léonie Delacroix" (63 chars mais mal formaté)
  - Le Harnais (à vérifier)
- [ ] **Collections courtes** : écrire des titres plus descriptifs pour Chien (32 chars), Chat (31), Accessoires (38), Pour la maison (41), VENTES PRIVÉES (44), Un coup de cœur (44)
- [ ] **2 produits en anglais** : traduire les noms en français pour débloquer la génération de métas

### Optimisations ciblées GSC
- [ ] **Le Tour De Cou Pour Chien** — 210 impressions, 0 clic, position 6 → améliorer méta
- [ ] **Le Tour De Cou Pour Chat** — 271 impressions, 2 clics, position 4.7 → améliorer méta
- [ ] **Collection Chien** — 107 impressions, position 4.5 → titre plus descriptif
- [ ] **L'abreuvoir** — 344 impressions, 18 clics, position 11 → pousser en page 1

## ⏳ À faire — Moyen terme

- [ ] Lancer `fetch_pagespeed.py` → mesurer les Core Web Vitals réels (actuellement estimés à 50%)
- [ ] Relancer audit complet (`detect_issues.py` + `generate_report.py`) → mesurer la progression du score SEO
- [ ] Mettre en place GitHub Actions — audit automatique hebdomadaire
- [ ] Structured data JSON-LD sur les fiches produits (schema.org Product)

## ⏳ À faire — Long terme

- [ ] Analyse mots-clés GSC → identifier des pages de contenu à créer (blog, guides)
- [ ] Ahrefs Webmaster Tools API — backlinks et mots-clés manquants
- [ ] GA4 Data API — trafic e-commerce + taux de conversion par page

## 🚧 Blocages / Questions ouvertes
- `fetch_pagespeed` : 1 appel par URL × 2 (mobile + desktop) → à lancer séparément (lent)
- Score SEO actuel non remesyré depuis les optimisations Phase 2 — à refaire

## 📋 Historique des sessions

### Session 2026-05-05 (suite — Phase 2 & 3)
- Phase 2 complète : generate_suggestions, update_alt_text, corrections bugs (qualificatif dupliqué, brand name)
- 26 méta + 17 alt texts poussés sur Shopify, 69 changements loggés dans history.db
- Logging SQLite et garde-fou 429 ajoutés aux scripts apply
- GSC connecté : credentials.json OAuth, test user ajouté, GSC_SITE_URL configuré
- 50 URLs · 3 736 impressions · 245 clics sur 90 jours
- 49/49 tests verts, ruff clean

### Session 2026-05-05 (Phase 1)
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
