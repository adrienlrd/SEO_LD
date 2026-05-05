"""Tests for scripts.audit.parse_screaming_frog."""

from scripts.audit.parse_screaming_frog import find_404s, parse_images, parse_overview

_OVERVIEW_CSV = (
    "Address,Title 1,Title 1 Length,Meta Description 1,Meta Description 1 Length,Status Code\n"
    "https://www.leoniedelacroix.com/,Accueil,7,Une desc,8,200\n"
    "https://www.leoniedelacroix.com/old-page,Ancienne page,13,,0,404\n"
)

_IMAGES_CSV = (
    "Image,Alt Text,Missing Alt Text,From\n"
    "https://cdn.shopify.com/img1.jpg,Croquettes chien,FALSE,https://www.leoniedelacroix.com/\n"
    "https://cdn.shopify.com/img2.jpg,,TRUE,https://www.leoniedelacroix.com/\n"
)


def test_parse_overview_loads_expected_columns(tmp_path):
    csv_file = tmp_path / "overview.csv"
    csv_file.write_text(_OVERVIEW_CSV, encoding="utf-8")

    df = parse_overview(str(csv_file))

    assert "url" in df.columns
    assert "title" in df.columns
    assert "status_code" in df.columns
    assert len(df) == 2


def test_find_404s_filters_correctly(tmp_path):
    csv_file = tmp_path / "overview.csv"
    csv_file.write_text(_OVERVIEW_CSV, encoding="utf-8")

    df = parse_overview(str(csv_file))
    result = find_404s(df)

    assert len(result) == 1
    assert "old-page" in result["url"].iloc[0]


def test_find_404s_empty_when_no_status_code():
    import pandas as pd

    df = pd.DataFrame({"url": ["https://example.com/"]})
    result = find_404s(df)

    assert result.empty


def test_parse_images_loads_alt_text(tmp_path):
    csv_file = tmp_path / "images.csv"
    csv_file.write_text(_IMAGES_CSV, encoding="utf-8")

    df = parse_images(str(csv_file))

    assert "alt_text" in df.columns
    assert len(df) == 2
