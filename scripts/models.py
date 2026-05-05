"""Shared domain models for the SEO audit pipeline."""

from enum import StrEnum

from pydantic import BaseModel


class Severity(StrEnum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class Issue(BaseModel):
    resource_type: str
    resource_id: str
    resource_title: str
    issue_type: str
    severity: Severity
    current_value: str | None = None
    detail: str


class SEOScore(BaseModel):
    total: float
    components: dict[str, float]
    issue_count: dict[str, int]
