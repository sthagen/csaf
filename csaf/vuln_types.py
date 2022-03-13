"""CVSS 2/3.0/3.1 general definitions."""

from __future__ import annotations

from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field


class AccessVectorType(Enum):
    network = 'NETWORK'
    adjacent_network = 'ADJACENT_NETWORK'
    local = 'LOCAL'


class AccessComplexityType(Enum):
    high = 'HIGH'
    medium = 'MEDIUM'
    low = 'LOW'


class AuthenticationType(Enum):
    multiple = 'MULTIPLE'
    single = 'SINGLE'
    none = 'NONE'


class CiaType(Enum):
    none = 'NONE'
    partial = 'PARTIAL'
    complete = 'COMPLETE'


class ExploitabilityType(Enum):
    unproven = 'UNPROVEN'
    proof_of_concept = 'PROOF_OF_CONCEPT'
    functional = 'FUNCTIONAL'
    high = 'HIGH'
    not_defined = 'NOT_DEFINED'


class RemediationLevelType(Enum):
    official_fix = 'OFFICIAL_FIX'
    temporary_fix = 'TEMPORARY_FIX'
    workaround = 'WORKAROUND'
    unavailable = 'UNAVAILABLE'
    not_defined = 'NOT_DEFINED'


class ReportConfidenceType(Enum):
    unconfirmed = 'UNCONFIRMED'
    uncorroborated = 'UNCORROBORATED'
    confirmed = 'CONFIRMED'
    not_defined = 'NOT_DEFINED'


class CollateralDamagePotentialType(Enum):
    none = 'NONE'
    low = 'LOW'
    low_medium = 'LOW_MEDIUM'
    medium_high = 'MEDIUM_HIGH'
    high = 'HIGH'
    not_defined = 'NOT_DEFINED'


class TargetDistributionType(Enum):
    none = 'NONE'
    low = 'LOW'
    medium = 'MEDIUM'
    high = 'HIGH'
    not_defined = 'NOT_DEFINED'


class CiaRequirementType(Enum):
    low = 'LOW'
    medium = 'MEDIUM'
    high = 'HIGH'
    not_defined = 'NOT_DEFINED'


class AttackVectorType(Enum):
    network = 'NETWORK'
    adjacent_network = 'ADJACENT_NETWORK'
    local = 'LOCAL'
    physical = 'PHYSICAL'


class ModifiedAttackVectorType(Enum):
    network = 'NETWORK'
    adjacent_network = 'ADJACENT_NETWORK'
    local = 'LOCAL'
    physical = 'PHYSICAL'
    not_defined = 'NOT_DEFINED'


class AttackComplexityType(Enum):
    high = 'HIGH'
    low = 'LOW'


class ModifiedAttackComplexityType(Enum):
    high = 'HIGH'
    low = 'LOW'
    not_defined = 'NOT_DEFINED'


class PrivilegesRequiredType(Enum):
    high = 'HIGH'
    low = 'LOW'
    none = 'NONE'


class ModifiedPrivilegesRequiredType(Enum):
    high = 'HIGH'
    low = 'LOW'
    none = 'NONE'
    not_defined = 'NOT_DEFINED'


class UserInteractionType(Enum):
    none = 'NONE'
    required = 'REQUIRED'


class ModifiedUserInteractionType(Enum):
    none = 'NONE'
    required = 'REQUIRED'
    not_defined = 'NOT_DEFINED'


class ScopeType(Enum):
    unchanged = 'UNCHANGED'
    changed = 'CHANGED'


class ModifiedScopeType(Enum):
    unchanged = 'UNCHANGED'
    changed = 'CHANGED'
    not_defined = 'NOT_DEFINED'


class ModifiedCiaType(Enum):
    none = 'NONE'
    low = 'LOW'
    high = 'HIGH'
    not_defined = 'NOT_DEFINED'


class ExploitCodeMaturityType(Enum):
    unproven = 'UNPROVEN'
    proof_of_concept = 'PROOF_OF_CONCEPT'
    functional = 'FUNCTIONAL'
    high = 'HIGH'
    not_defined = 'NOT_DEFINED'


class ConfidenceType(Enum):
    unknown = 'UNKNOWN'
    reasonable = 'REASONABLE'
    confirmed = 'CONFIRMED'
    not_defined = 'NOT_DEFINED'


class ScoreType(BaseModel):
    __root__: Annotated[float, Field(ge=0.0, le=10.0)]


class SeverityType(Enum):
    none = 'NONE'
    low = 'LOW'
    medium = 'MEDIUM'
    high = 'HIGH'
    critical = 'CRITICAL'
