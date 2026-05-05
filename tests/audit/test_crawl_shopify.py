"""Tests for scripts.audit.crawl_shopify."""

import tempfile

from scripts.audit.crawl_shopify import (
    fetch_collections,
    fetch_products,
    init_db,
    save_snapshot,
)


def _products_page(has_next: bool = False, cursor: str | None = None, pid: str = "1") -> dict:
    return {
        "data": {
            "products": {
                "pageInfo": {"hasNextPage": has_next, "endCursor": cursor},
                "edges": [
                    {
                        "node": {
                            "id": f"gid://shopify/Product/{pid}",
                            "title": "Croquettes Chien",
                            "handle": "croquettes-chien",
                            "seo": {"title": "SEO Title", "description": "SEO Desc"},
                            "images": {"edges": []},
                        }
                    }
                ],
            }
        }
    }


def _collections_page() -> dict:
    return {
        "data": {
            "collections": {
                "pageInfo": {"hasNextPage": False, "endCursor": None},
                "edges": [
                    {
                        "node": {
                            "id": "gid://shopify/Collection/1",
                            "title": "Chien",
                            "handle": "chien",
                            "seo": {"title": "Chien SEO", "description": "Desc"},
                        }
                    }
                ],
            }
        }
    }


def test_fetch_products_returns_nodes(mocker):
    mock = mocker.patch("requests.post")
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = _products_page()

    products = fetch_products(endpoint="http://test", headers={})

    assert len(products) == 1
    assert products[0]["id"] == "gid://shopify/Product/1"


def test_fetch_products_paginates(mocker):
    page1 = _products_page(has_next=True, cursor="cur1", pid="1")
    page2 = _products_page(has_next=False, pid="2")

    mock = mocker.patch("requests.post")
    mock.return_value.status_code = 200
    mock.return_value.json.side_effect = [page1, page2]

    products = fetch_products(endpoint="http://test", headers={})

    assert len(products) == 2
    assert mock.call_count == 2


def test_fetch_collections_returns_nodes(mocker):
    mock = mocker.patch("requests.post")
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = _collections_page()

    collections = fetch_collections(endpoint="http://test", headers={})

    assert len(collections) == 1
    assert collections[0]["handle"] == "chien"


def test_init_db_creates_tables():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        conn = init_db(tmp.name)
        tables = {
            row[0]
            for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        }
        assert "snapshots" in tables
        assert "seo_changes" in tables
        conn.close()


def test_save_snapshot_inserts_rows():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        conn = init_db(tmp.name)
        resources = [
            {"id": "gid://shopify/Product/1", "title": "A"},
            {"id": "gid://shopify/Product/2", "title": "B"},
        ]
        save_snapshot(conn, "product", resources)

        count = conn.execute("SELECT COUNT(*) FROM snapshots").fetchone()[0]
        assert count == 2
        conn.close()
