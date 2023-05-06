"""CSAF CVSS 2/3.0/3.1 proxy implementation."""

from __future__ import annotations

from enum import Enum
from typing import Annotated, Optional, no_type_check

from pydantic import BaseModel, Field

from csaf.vuln_types import (
    AccessComplexityType,
    AccessVectorType,
    AttackComplexityType,
    AttackVectorType,
    AuthenticationType,
    CiaRequirementType,
    CiaType,
    CollateralDamagePotentialType,
    ConfidenceType,
    ExploitabilityType,
    ExploitCodeMaturityType,
    ModifiedAttackComplexityType,
    ModifiedAttackVectorType,
    ModifiedCiaType,
    ModifiedPrivilegesRequiredType,
    ModifiedScopeType,
    ModifiedUserInteractionType,
    PrivilegesRequiredType,
    RemediationLevelType,
    ReportConfidenceType,
    ScopeType,
    TargetDistributionType,
    UserInteractionType,
)


class ScoreType(BaseModel):
    __root__: Annotated[float, Field(ge=0.0, le=10.0)]


class SeverityType(Enum):
    none = 'NONE'
    low = 'LOW'
    medium = 'MEDIUM'
    high = 'HIGH'
    critical = 'CRITICAL'


class Version(Enum):
    """
    CVSS Version
    """

    two = '2.0'
    three_zero = '3.0'
    three_wun = '3.1'


class CVSS2(BaseModel):
    version: Annotated[Version, Field(description='CVSS Version')] = Version.two
    vector_string: Annotated[
        str,
        Field(
            alias='vectorString',
            regex=(
                '^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:'
                '(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:'
                '(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:'
                '(L|M|H|ND))$'
            ),
        ),
    ]
    access_vector: Annotated[Optional[AccessVectorType], Field(alias='accessVector')] = None
    access_complexity: Annotated[Optional[AccessComplexityType], Field(alias='accessComplexity')] = None
    authentication: Optional[AuthenticationType] = None
    confidentiality_impact: Annotated[Optional[CiaType], Field(alias='confidentialityImpact')] = None
    integrity_impact: Annotated[Optional[CiaType], Field(alias='integrityImpact')] = None
    availability_impact: Annotated[Optional[CiaType], Field(alias='availabilityImpact')] = None
    base_score: Annotated[ScoreType, Field(alias='baseScore')]
    exploitability: Optional[ExploitabilityType] = None
    remediation_level: Annotated[Optional[RemediationLevelType], Field(alias='remediationLevel')] = None
    report_confidence: Annotated[Optional[ReportConfidenceType], Field(alias='reportConfidence')] = None
    temporal_score: Annotated[Optional[ScoreType], Field(alias='temporalScore')] = None
    collateral_damage_potential: Annotated[
        Optional[CollateralDamagePotentialType],
        Field(alias='collateralDamagePotential'),
    ] = None
    target_distribution: Annotated[Optional[TargetDistributionType], Field(alias='targetDistribution')] = None
    confidentiality_requirement: Annotated[
        Optional[CiaRequirementType], Field(alias='confidentialityRequirement')
    ] = None
    integrity_requirement: Annotated[Optional[CiaRequirementType], Field(alias='integrityRequirement')] = None
    availability_requirement: Annotated[Optional[CiaRequirementType], Field(alias='availabilityRequirement')] = None
    environmental_score: Annotated[Optional[ScoreType], Field(alias='environmentalScore')] = None

    @no_type_check
    def json(self, *args, **kwargs):
        kwargs.setdefault('by_alias', True)
        return super().json(*args, **kwargs)


class CVSS30(BaseModel):
    version: Annotated[Version, Field(description='CVSS Version')] = Version.three_zero
    vector_string: Annotated[
        str,
        Field(
            alias='vectorString',
            regex=(
                '^CVSS:3[.]0/((AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|'
                '[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|'
                'AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|'
                'MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'
            ),
        ),
    ]
    attack_vector: Annotated[Optional[AttackVectorType], Field(alias='attackVector')] = None
    attack_complexity: Annotated[Optional[AttackComplexityType], Field(alias='attackComplexity')] = None
    privileges_required: Annotated[Optional[PrivilegesRequiredType], Field(alias='privilegesRequired')] = None
    user_interaction: Annotated[Optional[UserInteractionType], Field(alias='userInteraction')] = None
    scope: Optional[ScopeType] = None
    confidentiality_impact: Annotated[Optional[CiaType], Field(alias='confidentialityImpact')] = None
    integrity_impact: Annotated[Optional[CiaType], Field(alias='integrityImpact')] = None
    availability_impact: Annotated[Optional[CiaType], Field(alias='availabilityImpact')] = None
    base_score: Annotated[ScoreType, Field(alias='baseScore')]
    base_severity: Annotated[SeverityType, Field(alias='baseSeverity')]
    exploit_code_maturity: Annotated[Optional[ExploitCodeMaturityType], Field(alias='exploitCodeMaturity')] = None
    remediation_level: Annotated[Optional[RemediationLevelType], Field(alias='remediationLevel')] = None
    report_confidence: Annotated[Optional[ConfidenceType], Field(alias='reportConfidence')] = None
    temporal_score: Annotated[Optional[ScoreType], Field(alias='temporalScore')] = None
    temporal_severity: Annotated[Optional[SeverityType], Field(alias='temporalSeverity')] = None
    confidentiality_requirement: Annotated[
        Optional[CiaRequirementType], Field(alias='confidentialityRequirement')
    ] = None
    integrity_requirement: Annotated[Optional[CiaRequirementType], Field(alias='integrityRequirement')] = None
    availability_requirement: Annotated[Optional[CiaRequirementType], Field(alias='availabilityRequirement')] = None
    modified_attack_vector: Annotated[Optional[ModifiedAttackVectorType], Field(alias='modifiedAttackVector')] = None
    modified_attack_complexity: Annotated[
        Optional[ModifiedAttackComplexityType], Field(alias='modifiedAttackComplexity')
    ] = None
    modified_privileges_required: Annotated[
        Optional[ModifiedPrivilegesRequiredType],
        Field(alias='modifiedPrivilegesRequired'),
    ] = None
    modified_user_interaction: Annotated[
        Optional[ModifiedUserInteractionType], Field(alias='modifiedUserInteraction')
    ] = None
    modified_scope: Annotated[Optional[ModifiedScopeType], Field(alias='modifiedScope')] = None
    modified_confidentiality_impact: Annotated[
        Optional[ModifiedCiaType], Field(alias='modifiedConfidentialityImpact')
    ] = None
    modified_integrity_impact: Annotated[Optional[ModifiedCiaType], Field(alias='modifiedIntegrityImpact')] = None
    modified_availability_impact: Annotated[Optional[ModifiedCiaType], Field(alias='modifiedAvailabilityImpact')] = None
    environmental_score: Annotated[Optional[ScoreType], Field(alias='environmentalScore')] = None
    environmental_severity: Annotated[Optional[SeverityType], Field(alias='environmentalSeverity')] = None

    @no_type_check
    def json(self, *args, **kwargs):
        kwargs.setdefault('by_alias', True)
        return super().json(*args, **kwargs)


class CVSS31(BaseModel):
    version: Annotated[Version, Field(description='CVSS Version')] = Version.three_wun
    vector_string: Annotated[
        str,
        Field(
            alias='vectorString',
            regex=(
                '^CVSS:3[.]1/((AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:'
                '[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*'
                '(AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:'
                '[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'
            ),
        ),
    ]
    attack_vector: Annotated[Optional[AttackVectorType], Field(alias='attackVector')] = None
    attack_complexity: Annotated[Optional[AttackComplexityType], Field(alias='attackComplexity')] = None
    privileges_required: Annotated[Optional[PrivilegesRequiredType], Field(alias='privilegesRequired')] = None
    user_interaction: Annotated[Optional[UserInteractionType], Field(alias='userInteraction')] = None
    scope: Optional[ScopeType] = None
    confidentiality_impact: Annotated[Optional[CiaType], Field(alias='confidentialityImpact')] = None
    integrity_impact: Annotated[Optional[CiaType], Field(alias='integrityImpact')] = None
    availability_impact: Annotated[Optional[CiaType], Field(alias='availabilityImpact')] = None
    base_score: Annotated[ScoreType, Field(alias='baseScore')]
    base_severity: Annotated[SeverityType, Field(alias='baseSeverity')]
    exploit_code_maturity: Annotated[Optional[ExploitCodeMaturityType], Field(alias='exploitCodeMaturity')] = None
    remediation_level: Annotated[Optional[RemediationLevelType], Field(alias='remediationLevel')] = None
    report_confidence: Annotated[Optional[ConfidenceType], Field(alias='reportConfidence')] = None
    temporal_score: Annotated[Optional[ScoreType], Field(alias='temporalScore')] = None
    temporal_severity: Annotated[Optional[SeverityType], Field(alias='temporalSeverity')] = None
    confidentiality_requirement: Annotated[
        Optional[CiaRequirementType], Field(alias='confidentialityRequirement')
    ] = None
    integrity_requirement: Annotated[Optional[CiaRequirementType], Field(alias='integrityRequirement')] = None
    availability_requirement: Annotated[Optional[CiaRequirementType], Field(alias='availabilityRequirement')] = None
    modified_attack_vector: Annotated[Optional[ModifiedAttackVectorType], Field(alias='modifiedAttackVector')] = None
    modified_attack_complexity: Annotated[
        Optional[ModifiedAttackComplexityType], Field(alias='modifiedAttackComplexity')
    ] = None
    modified_privileges_required: Annotated[
        Optional[ModifiedPrivilegesRequiredType],
        Field(alias='modifiedPrivilegesRequired'),
    ] = None
    modified_user_interaction: Annotated[
        Optional[ModifiedUserInteractionType], Field(alias='modifiedUserInteraction')
    ] = None
    modified_scope: Annotated[Optional[ModifiedScopeType], Field(alias='modifiedScope')] = None
    modified_confidentiality_impact: Annotated[
        Optional[ModifiedCiaType], Field(alias='modifiedConfidentialityImpact')
    ] = None
    modified_integrity_impact: Annotated[Optional[ModifiedCiaType], Field(alias='modifiedIntegrityImpact')] = None
    modified_availability_impact: Annotated[Optional[ModifiedCiaType], Field(alias='modifiedAvailabilityImpact')] = None
    environmental_score: Annotated[Optional[ScoreType], Field(alias='environmentalScore')] = None
    environmental_severity: Annotated[Optional[SeverityType], Field(alias='environmentalSeverity')] = None

    @no_type_check
    def json(self, *args, **kwargs):
        kwargs.setdefault('by_alias', True)
        return super().json(*args, **kwargs)
