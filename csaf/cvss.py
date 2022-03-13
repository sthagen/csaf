"""CSAF CVSS 2/3.0/3.1 proxy implementation."""

from __future__ import annotations

from enum import Enum
from typing import Annotated, Optional

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
            alias='vector_string',
            regex=(
                '^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:'
                '(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:'
                '(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:'
                '(L|M|H|ND))$'
            ),
        ),
    ]
    access_vector: Annotated[Optional[AccessVectorType], Field(alias='access_vector')] = None
    access_complexity: Annotated[Optional[AccessComplexityType], Field(alias='access_complexity')] = None
    authentication: Optional[AuthenticationType] = None
    confidentiality_impact: Annotated[Optional[CiaType], Field(alias='confidentiality_impact')] = None
    integrity_impact: Annotated[Optional[CiaType], Field(alias='integrity_impact')] = None
    availability_impact: Annotated[Optional[CiaType], Field(alias='availability_impact')] = None
    base_score: Annotated[ScoreType, Field(alias='base_score')]
    exploitability: Optional[ExploitabilityType] = None
    remediation_level: Annotated[Optional[RemediationLevelType], Field(alias='remediation_level')] = None
    report_confidence: Annotated[Optional[ReportConfidenceType], Field(alias='report_confidence')] = None
    temporal_score: Annotated[Optional[ScoreType], Field(alias='temporal_score')] = None
    collateral_damage_potential: Annotated[
        Optional[CollateralDamagePotentialType],
        Field(alias='collateral_damage_potential'),
    ] = None
    target_distribution: Annotated[Optional[TargetDistributionType], Field(alias='target_distribution')] = None
    confidentiality_requirement: Annotated[
        Optional[CiaRequirementType], Field(alias='confidentiality_requirement')
    ] = None
    integrity_requirement: Annotated[Optional[CiaRequirementType], Field(alias='integrity_requirement')] = None
    availability_requirement: Annotated[Optional[CiaRequirementType], Field(alias='availability_requirement')] = None
    environmental_score: Annotated[Optional[ScoreType], Field(alias='environmental_score')] = None


class CVSS30(BaseModel):
    version: Annotated[Version, Field(description='CVSS Version')] = Version.three_zero
    vector_string: Annotated[
        str,
        Field(
            alias='vector_string',
            regex=(
                '^CVSS:3[.]0/((AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|'
                '[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|'
                'AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|'
                'MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'
            ),
        ),
    ]
    attack_vector: Annotated[Optional[AttackVectorType], Field(alias='attack_vector')] = None
    attack_complexity: Annotated[Optional[AttackComplexityType], Field(alias='attack_complexity')] = None
    privileges_required: Annotated[Optional[PrivilegesRequiredType], Field(alias='privileges_required')] = None
    user_interaction: Annotated[Optional[UserInteractionType], Field(alias='user_interaction')] = None
    scope: Optional[ScopeType] = None
    confidentiality_impact: Annotated[Optional[CiaType], Field(alias='confidentiality_impact')] = None
    integrity_impact: Annotated[Optional[CiaType], Field(alias='integrity_impact')] = None
    availability_impact: Annotated[Optional[CiaType], Field(alias='availability_impact')] = None
    base_score: Annotated[ScoreType, Field(alias='base_score')]
    base_severity: Annotated[SeverityType, Field(alias='base_severity')]
    exploit_code_maturity: Annotated[Optional[ExploitCodeMaturityType], Field(alias='exploit_code_maturity')] = None
    remediation_level: Annotated[Optional[RemediationLevelType], Field(alias='remediation_level')] = None
    report_confidence: Annotated[Optional[ConfidenceType], Field(alias='report_confidence')] = None
    temporal_score: Annotated[Optional[ScoreType], Field(alias='temporal_score')] = None
    temporal_severity: Annotated[Optional[SeverityType], Field(alias='temporal_severity')] = None
    confidentiality_requirement: Annotated[
        Optional[CiaRequirementType], Field(alias='confidentiality_requirement')
    ] = None
    integrity_requirement: Annotated[Optional[CiaRequirementType], Field(alias='integrity_requirement')] = None
    availability_requirement: Annotated[Optional[CiaRequirementType], Field(alias='availability_requirement')] = None
    modified_attack_vector: Annotated[Optional[ModifiedAttackVectorType], Field(alias='modified_attack_vector')] = None
    modified_attack_complexity: Annotated[
        Optional[ModifiedAttackComplexityType], Field(alias='modified_attack_complexity')
    ] = None
    modified_privileges_required: Annotated[
        Optional[ModifiedPrivilegesRequiredType],
        Field(alias='modified_privileges_required'),
    ] = None
    modified_user_interaction: Annotated[
        Optional[ModifiedUserInteractionType], Field(alias='modified_user_interaction')
    ] = None
    modified_scope: Annotated[Optional[ModifiedScopeType], Field(alias='modified_scope')] = None
    modified_confidentiality_impact: Annotated[
        Optional[ModifiedCiaType], Field(alias='modified_confidentiality_impact')
    ] = None
    modified_integrity_impact: Annotated[Optional[ModifiedCiaType], Field(alias='modified_integrity_impact')] = None
    modified_availability_impact: Annotated[
        Optional[ModifiedCiaType], Field(alias='modified_availability_impact')
    ] = None
    environmental_score: Annotated[Optional[ScoreType], Field(alias='environmental_score')] = None
    environmental_severity: Annotated[Optional[SeverityType], Field(alias='environmental_severity')] = None


class CVSS31(BaseModel):
    version: Annotated[Version, Field(description='CVSS Version')] = Version.three_wun
    vector_string: Annotated[
        str,
        Field(
            alias='vector_string',
            regex=(
                '^CVSS:3[.]1/((AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:'
                '[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*'
                '(AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:'
                '[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'
            ),
        ),
    ]
    attack_vector: Annotated[Optional[AttackVectorType], Field(alias='attack_vector')] = None
    attack_complexity: Annotated[Optional[AttackComplexityType], Field(alias='attack_complexity')] = None
    privileges_required: Annotated[Optional[PrivilegesRequiredType], Field(alias='privileges_required')] = None
    user_interaction: Annotated[Optional[UserInteractionType], Field(alias='user_interaction')] = None
    scope: Optional[ScopeType] = None
    confidentiality_impact: Annotated[Optional[CiaType], Field(alias='confidentiality_impact')] = None
    integrity_impact: Annotated[Optional[CiaType], Field(alias='integrity_impact')] = None
    availability_impact: Annotated[Optional[CiaType], Field(alias='availability_impact')] = None
    base_score: Annotated[ScoreType, Field(alias='base_score')]
    base_severity: Annotated[SeverityType, Field(alias='base_severity')]
    exploit_code_maturity: Annotated[Optional[ExploitCodeMaturityType], Field(alias='exploit_code_maturity')] = None
    remediation_level: Annotated[Optional[RemediationLevelType], Field(alias='remediation_level')] = None
    report_confidence: Annotated[Optional[ConfidenceType], Field(alias='report_confidence')] = None
    temporal_score: Annotated[Optional[ScoreType], Field(alias='temporal_score')] = None
    temporal_severity: Annotated[Optional[SeverityType], Field(alias='temporal_severity')] = None
    confidentiality_requirement: Annotated[
        Optional[CiaRequirementType], Field(alias='confidentiality_requirement')
    ] = None
    integrity_requirement: Annotated[Optional[CiaRequirementType], Field(alias='integrity_requirement')] = None
    availability_requirement: Annotated[Optional[CiaRequirementType], Field(alias='availability_requirement')] = None
    modified_attack_vector: Annotated[Optional[ModifiedAttackVectorType], Field(alias='modified_attack_vector')] = None
    modified_attack_complexity: Annotated[
        Optional[ModifiedAttackComplexityType], Field(alias='modified_attack_complexity')
    ] = None
    modified_privileges_required: Annotated[
        Optional[ModifiedPrivilegesRequiredType],
        Field(alias='modified_privileges_required'),
    ] = None
    modified_user_interaction: Annotated[
        Optional[ModifiedUserInteractionType], Field(alias='modified_user_interaction')
    ] = None
    modified_scope: Annotated[Optional[ModifiedScopeType], Field(alias='modified_scope')] = None
    modified_confidentiality_impact: Annotated[
        Optional[ModifiedCiaType], Field(alias='modified_confidentiality_impact')
    ] = None
    modified_integrity_impact: Annotated[Optional[ModifiedCiaType], Field(alias='modified_integrity_impact')] = None
    modified_availability_impact: Annotated[
        Optional[ModifiedCiaType], Field(alias='modified_availability_impact')
    ] = None
    environmental_score: Annotated[Optional[ScoreType], Field(alias='environmental_score')] = None
    environmental_severity: Annotated[Optional[SeverityType], Field(alias='environmental_severity')] = None
