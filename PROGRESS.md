# PROGRESS — SEO Leoniedelacroix.com

## État global
- Phase actuelle : Phase 1 — Audit
- Dernière session : 2026-04-20
- Prochain objectif : Obtenir les credentials API et valider le plan Phase 1

## ✅ Terminé
- Initialisation repo Git + structure dossiers
- Création CLAUDE.md avec contexte projet complet (URL, domaine, stack, MCP, règles, arborescence, commandes)
- Création PROGRESS.md avec suivi de session
- Règle 9 ajoutée : mise à jour PROGRESS.md obligatoire en fin de session
- Prompt d'amorçage défini (Bloc 1)

## 🔄 En cours
- Obtention credentials API (Shopify, Google Search Console, Ahrefs, GA4)

## ⏳ À faire (Phase 1)
- [ ] crawl_shopify.py — crawl complet catalogue Shopify
- [ ] fetch_gsc.py — export 90 jours Search Console
- [ ] fetch_pagespeed.py — Core Web Vitals par page
- [ ] detect_issues.py — détection problèmes techniques SEO
- [ ] generate_report.py — premier rapport Markdown avec score /100
- [ ] keywords.yaml — définir les mots-clés cibles par thème
- [ ] seo_rules.yaml — règles métier (longueurs meta, etc.)
- [ ] pyproject.toml + requirements.txt — figer les dépendances
- [ ] .env.example — template des secrets nécessaires

## 🚧 Blocages / Questions ouvertes
- En attente des 4 credentials (Shopify token, Google credentials.json, Ahrefs API key, GitHub token)

## 📋 Historique des sessions
### Session 2026-04-20
- Initialisation complète du projet SEO_LD
- Structure repo créée, CLAUDE.md rédigé et complété (URL, domaine myshopify, arborescence, commandes, historique des décisions)
- PROGRESS.md créé avec suivi d'avancement
- Prochaine étape : récupérer les credentials API, puis valider le plan Phase 1 et commencer crawl_shopify.py
