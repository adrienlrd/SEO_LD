"""Tests for scripts.audit.detect_issues."""

import pandas as pd

from scripts.audit.detect_issues import (
    detect_404_issues,
    detect_alt_text_issues,
    detect_duplicate_content,
    detect_meta_description_issues,
    detect_meta_title_issues,
    detect_redirect_issues,
)
from scripts.models import Severity

_RULES = "config/seo_rules.yaml"


def _product(
    pid: str,
    name: str,
    seo_title: str = "",
    seo_desc: str = "",
    images: list[str | None] | None = None,
) -> dict:
    return {
        "id": pid,
        "title": name,
        "handle": name.lower().replace(" ", "-"),
        "seo": {"title": seo_title, "description": seo_desc},
        "images": {
            "edges": [
                {"node": {"id": f"img-{pid}-{i}", "url": "http://img", "altText": alt}}
                for i, alt in enumerate(images or [])
            ]
        },
    }


# ── Meta title ────────────────────────────────────────────────────────────────


def test_missing_meta_title_is_critical():
    issues = detect_meta_title_issues([_product("1", "Croquettes")], rules_path=_RULES)

    assert len(issues) == 1
    assert issues[0].issue_type == "missing_meta_title"
    assert issues[0].severity == Severity.CRITICAL


def test_too_short_meta_title():
    issues = detect_meta_title_issues([_product("1", "Prod", seo_title="Court")], rules_path=_RULES)

    assert any(i.issue_type == "too_short_meta_title" for i in issues)
    assert issues[0].severity == Severity.HIGH


def test_too_long_meta_title():
    long = "A" * 70
    issues = detect_meta_title_issues([_product("1", "Prod", seo_title=long)], rules_path=_RULES)

    assert any(i.issue_type == "too_long_meta_title" for i in issues)


def test_duplicate_meta_title_flagged_on_second_occurrence():
    title = "Croquettes Chien Premium France"
    issues = detect_meta_title_issues(
        [_product("1", "A", seo_title=title), _product("2", "B", seo_title=title)],
        rules_path=_RULES,
    )

    dup = [i for i in issues if i.issue_type == "duplicate_meta_title"]
    assert len(dup) == 1
    assert dup[0].resource_id == "2"


def test_valid_meta_title_produces_no_issues():
    issues = detect_meta_title_issues(
        [_product("1", "Prod", seo_title="Croquettes Chien Senior Fabriqué France")],
        rules_path=_RULES,
    )
    assert not issues


# ── Meta description ──────────────────────────────────────────────────────────


def test_missing_meta_description_is_high():
    issues = detect_meta_description_issues(
        [_product("1", "Prod", seo_title="Valid title here")], rules_path=_RULES
    )

    assert any(i.issue_type == "missing_meta_description" for i in issues)
    assert issues[0].severity == Severity.HIGH


def test_too_short_meta_description():
    issues = detect_meta_description_issues(
        [_product("1", "Prod", seo_desc="Trop court.")], rules_path=_RULES
    )

    assert any(i.issue_type == "too_short_meta_description" for i in issues)


# ── Alt text ──────────────────────────────────────────────────────────────────


def test_missing_alt_text_when_none():
    issues = detect_alt_text_issues([_product("1", "Prod", images=[None])], rules_path=_RULES)

    assert len(issues) == 1
    assert issues[0].issue_type == "missing_alt_text"
    assert issues[0].severity == Severity.HIGH


def test_missing_alt_text_when_empty_string():
    issues = detect_alt_text_issues([_product("1", "Prod", images=[""])], rules_path=_RULES)

    assert any(i.issue_type == "missing_alt_text" for i in issues)


def test_no_alt_text_issues_when_present():
    issues = detect_alt_text_issues(
        [_product("1", "Prod", images=["Croquettes chien senior naturelles"])],
        rules_path=_RULES,
    )
    assert not issues


# ── Duplicate content ─────────────────────────────────────────────────────────


def test_duplicate_content_flags_all_products_as_info():
    issues = detect_duplicate_content([_product("1", "A"), _product("2", "B")])

    assert len(issues) == 2
    assert all(i.issue_type == "shopify_duplicate_url" for i in issues)
    assert all(i.severity == Severity.INFO for i in issues)


# ── Redirect / 404 from Screaming Frog ───────────────────────────────────────


def test_redirect_issues_empty_when_no_data():
    assert detect_redirect_issues(None) == []


def test_404_issues_empty_when_no_data():
    assert detect_404_issues(None) == []


def test_detect_redirect_chain_flagged():
    df = pd.DataFrame(
        {
            "from_url": ["https://example.com/old"],
            "to_url": ["https://example.com/new"],
            "status_code": [301],
            "chain_length": [2],
        }
    )
    issues = detect_redirect_issues(df)

    assert any(i.issue_type == "redirect_chain" for i in issues)
    assert issues[0].severity == Severity.HIGH


def test_detect_404_from_overview_df():
    df = pd.DataFrame(
        {
            "url": ["https://example.com/missing"],
            "status_code": [404],
        }
    )
    issues = detect_404_issues(df)

    assert len(issues) == 1
    assert issues[0].issue_type == "page_404"
    assert issues[0].severity == Severity.CRITICAL
