"""Fixtures partagées pour tous les tests du projet SEO."""

import pytest

# --- Fixtures Shopify ---


@pytest.fixture
def shopify_products_response() -> dict:
    """Réponse GraphQL simulée pour une liste de produits Shopify."""
    return {
        "data": {
            "products": {
                "pageInfo": {"hasNextPage": False, "endCursor": None},
                "edges": [
                    {
                        "node": {
                            "id": "gid://shopify/Product/1",
                            "title": "Croquettes Chien Senior",
                            "handle": "croquettes-chien-senior",
                            "seo": {
                                "title": "Croquettes Chien Senior | Leoniedelacroix",
                                "description": "Croquettes premium pour chien senior, fabriquées en France.",
                            },
                            "images": {
                                "edges": [
                                    {
                                        "node": {
                                            "id": "gid://shopify/MediaImage/1",
                                            "url": "https://cdn.shopify.com/img1.jpg",
                                            "altText": "Croquettes chien senior sac 2kg",
                                        }
                                    }
                                ]
                            },
                        }
                    },
                    {
                        "node": {
                            "id": "gid://shopify/Product/2",
                            "title": "Croquettes Chat Adulte",
                            "handle": "croquettes-chat-adulte",
                            "seo": {"title": "", "description": ""},
                            "images": {
                                "edges": [
                                    {
                                        "node": {
                                            "id": "gid://shopify/MediaImage/2",
                                            "url": "https://cdn.shopify.com/img2.jpg",
                                            "altText": None,
                                        }
                                    }
                                ]
                            },
                        }
                    },
                ],
            }
        }
    }


@pytest.fixture
def shopify_mutation_success_response() -> dict:
    """Réponse GraphQL simulée pour une mutation réussie."""
    return {
        "data": {
            "productUpdate": {
                "product": {
                    "id": "gid://shopify/Product/1",
                    "seo": {
                        "title": "Nouveau titre SEO",
                        "description": "Nouvelle meta description.",
                    },
                },
                "userErrors": [],
            }
        }
    }


@pytest.fixture
def shopify_mutation_error_response() -> dict:
    """Réponse GraphQL simulée pour une mutation en erreur."""
    return {
        "data": {
            "productUpdate": {
                "product": None,
                "userErrors": [{"field": ["seo", "title"], "message": "Title is too long"}],
            }
        }
    }


# --- Fixtures Google Search Console ---


@pytest.fixture
def gsc_response() -> dict:
    """Réponse API GSC simulée pour une requête de performance."""
    return {
        "rows": [
            {
                "keys": ["/products/croquettes-chien-senior"],
                "clicks": 42,
                "impressions": 850,
                "ctr": 0.0494,
                "position": 14.3,
            },
            {
                "keys": ["/products/croquettes-chat-adulte"],
                "clicks": 5,
                "impressions": 320,
                "ctr": 0.0156,
                "position": 22.1,
            },
        ]
    }


# --- Fixtures PageSpeed ---


@pytest.fixture
def pagespeed_response() -> dict:
    """Réponse API PageSpeed simulée."""
    return {
        "lighthouseResult": {
            "categories": {"performance": {"score": 0.72}},
            "audits": {
                "largest-contentful-paint": {"numericValue": 3200},
                "cumulative-layout-shift": {"numericValue": 0.08},
                "total-blocking-time": {"numericValue": 450},
            },
        }
    }
