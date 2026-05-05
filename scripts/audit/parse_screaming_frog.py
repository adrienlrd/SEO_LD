"""Parse Screaming Frog CSV exports into structured DataFrames."""

from pathlib import Path

import click
import pandas as pd
from rich.console import Console

console = Console()

# Screaming Frog column name → our internal name
_OVERVIEW_COLS = {
    "Address": "url",
    "Title 1": "title",
    "Title 1 Length": "title_length",
    "Meta Description 1": "meta_description",
    "Meta Description 1 Length": "meta_description_length",
    "H1-1": "h1",
    "Status Code": "status_code",
    "Indexability": "indexability",
    "Canonical Link Element 1": "canonical",
    "Word Count": "word_count",
}

_IMAGES_COLS = {
    "Image": "image_url",
    "Alt Text": "alt_text",
    "Missing Alt Text": "missing_alt",
    "From": "page_url",
}

_REDIRECTS_COLS = {
    "Address": "from_url",
    "Redirect URL": "to_url",
    "Status Code": "status_code",
    "Redirect Chain Length": "chain_length",
}


def _load_csv(path: str | Path, col_mapping: dict[str, str]) -> pd.DataFrame:
    """Load a Screaming Frog CSV and rename to internal column names."""
    df = pd.read_csv(path, encoding="utf-8-sig", low_memory=False)
    available = {k: v for k, v in col_mapping.items() if k in df.columns}
    return df[list(available.keys())].rename(columns=available)


def parse_overview(path: str | Path) -> pd.DataFrame:
    """Parse a Screaming Frog 'Internal' or 'All' export CSV."""
    df = _load_csv(path, _OVERVIEW_COLS)
    if "status_code" in df.columns:
        df["status_code"] = pd.to_numeric(df["status_code"], errors="coerce")
    return df


def parse_images(path: str | Path) -> pd.DataFrame:
    """Parse a Screaming Frog 'Images' export CSV."""
    return _load_csv(path, _IMAGES_COLS)


def parse_redirects(path: str | Path) -> pd.DataFrame:
    """Parse a Screaming Frog 'Response Codes' CSV, keeping only 3xx rows."""
    df = _load_csv(path, _REDIRECTS_COLS)
    if "status_code" in df.columns:
        df["status_code"] = pd.to_numeric(df["status_code"], errors="coerce")
        df = df[df["status_code"].between(300, 399)]
    return df


def find_404s(overview_df: pd.DataFrame) -> pd.DataFrame:
    """Return a DataFrame of 404 URLs from an overview DataFrame."""
    if "status_code" not in overview_df.columns:
        return pd.DataFrame(columns=["url"])
    return overview_df[overview_df["status_code"] == 404][["url"]].copy()


@click.command()
@click.option("--overview", default=None, help="Path to Screaming Frog overview CSV")
@click.option("--images", default=None, help="Path to Screaming Frog images CSV")
@click.option("--redirects", default=None, help="Path to Screaming Frog response codes CSV")
def main(
    overview: str | None,
    images: str | None,
    redirects: str | None,
) -> None:
    """Parse and summarize Screaming Frog CSV exports."""
    if overview:
        df = parse_overview(overview)
        console.print(f"[green]Overview:[/green] {len(df)} URLs")
        console.print(f"  404s: {len(find_404s(df))}")

    if images:
        df_img = parse_images(images)
        missing = df_img["missing_alt"].sum() if "missing_alt" in df_img.columns else "?"
        console.print(f"[green]Images:[/green] {len(df_img)} — missing alt: {missing}")

    if redirects:
        df_red = parse_redirects(redirects)
        console.print(f"[green]Redirects:[/green] {len(df_red)} 3xx found")


if __name__ == "__main__":
    main()
