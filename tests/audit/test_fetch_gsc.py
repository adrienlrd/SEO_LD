"""Tests for scripts.audit.fetch_gsc."""

from unittest.mock import MagicMock

from scripts.audit.fetch_gsc import fetch_search_performance


def test_fetch_returns_dataframe(gsc_response):
    service = MagicMock()
    service.searchanalytics().query().execute.return_value = gsc_response

    df = fetch_search_performance(service, "https://www.leoniedelacroix.com", days=90)

    assert len(df) == 2
    assert list(df.columns) == ["url", "clicks", "impressions", "ctr", "position"]


def test_fetch_empty_response_returns_empty_dataframe():
    service = MagicMock()
    service.searchanalytics().query().execute.return_value = {"rows": []}

    df = fetch_search_performance(service, "https://www.leoniedelacroix.com")

    assert df.empty
    assert list(df.columns) == ["url", "clicks", "impressions", "ctr", "position"]


def test_fetch_correct_values(gsc_response):
    service = MagicMock()
    service.searchanalytics().query().execute.return_value = gsc_response

    df = fetch_search_performance(service, "https://www.leoniedelacroix.com")

    row = df[df["url"] == "/products/croquettes-chien-senior"].iloc[0]
    assert row["clicks"] == 42
    assert row["impressions"] == 850
    assert abs(row["position"] - 14.3) < 0.01
