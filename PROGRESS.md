# PROGRESS — SEO Leoniedelacroix.com

## État global
- Phase actuelle : Phase 1 — Audit (préparation)
- Dernière session : 2026-04-22
- Prochain objectif : Finir le setup des credentials API (étapes 3 à 6), puis valider le plan Phase 1

## ✅ Terminé
- Initialisation repo Git + structure dossiers
- Création CLAUDE.md avec contexte projet complet
- Création PROGRESS.md avec suivi de session
- Prompt d'amorçage défini et exécuté
- Installation ruff (via brew)
- Création Custom App Shopify "SEO Audit Tool" — token obtenu
- Configuration .env avec token Shopify + domaine store
- Configuration .env.example (template à jour)
- Ajout credentials.json et token.json au .gitignore
- Volume site confirmé : 3 collections, 5 produits (max ~20) — Screaming Frog gratuit suffira largement

## 🔄 En cours — Setup credentials (4 restantes sur 6)
- [ ] Étape 3 : Créer projet Google Cloud, activer 3 APIs (Search Console, GA4 Data, PageSpeed), télécharger credentials.json, copier API key PageSpeed
- [ ] Étape 4 : Créer compte Ahrefs Webmaster Tools, vérifier le site, générer API token
- [ ] Étape 5 : Récupérer le Property ID GA4
- [ ] Étape 6 : Compléter .env avec toutes les clés

## ⏳ À faire (Phase 1 — Audit)
- [ ] Valider le plan Phase 1 détaillé
- [ ] pyproject.toml + requirements.txt — figer les dépendances
- [ ] config/seo_rules.yaml — règles métier (longueurs meta, etc.)
- [ ] config/keywords.yaml — mots-clés cibles par thème
- [ ] scripts/audit/crawl_shopify.py — crawl complet catalogue Shopify
- [ ] scripts/audit/fetch_gsc.py — export 90 jours Search Console
- [ ] scripts/audit/fetch_pagespeed.py — Core Web Vitals par page
- [ ] scripts/audit/detect_issues.py — détection problèmes techniques SEO
- [ ] scripts/report/generate_report.py — premier rapport Markdown avec score /100

## 🚧 Blocages / Questions ouvertes
- ⚠️ Token Shopify exposé en clair dans le chat — recommandé de le révoquer et régénérer
- En attente des credentials : Google Cloud (credentials.json + API key), Ahrefs (token), GA4 (Property ID)

## 📋 Historique des sessions

### Session 2026-04-22
- Revue complète du contexte projet et des règles de travail
- Guide de setup fourni : 6 étapes détaillées pour obtenir tous les accès API
- Étape 1 complétée : ruff installé
- Étape 2 complétée : Custom App Shopify créée, token obtenu, .env configuré
- .env.example mis à jour avec toutes les clés attendues
- .gitignore renforcé (credentials.json, token.json)
- Prochaine session : compléter les étapes 3-6 (GCP, Ahrefs, GA4, PageSpeed), puis proposer le plan Phase 1

### Session 2026-04-20
- Initialisation complète du projet SEO_LD
- Structure repo créée, CLAUDE.md rédigé et complété
- PROGRESS.md créé avec suivi d'avancement
