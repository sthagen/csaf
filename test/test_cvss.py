import json

from test import conftest

import csaf.cvss as cvss

import pytest
from pydantic import ValidationError

from csaf.cvss import (
    CVSS2,
    CVSS30,
    CVSS31,
    SeverityType as CvssSeverityType,
    Version as CvssVersion,
)


CVSS31_BASE_SEVERITY_LOG4J = 'CRITICAL'  # str(CvssSeverityType.critical)
CVSS30_BASE_SEVERITY_LOG4J = 'CRITICAL'  # str(CvssSeverityType.critical)

DATA = {
    'baseScore': 10.0,
    'baseSeverity': 'CRITICAL',
    'vectorString': 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H',
    'version': '3.1',
}
JSON = json.dumps(DATA)


def test_cvss2_empty():
    message = '2 validation errors for CVSS2'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS2.model_validate_json('{}')  # type: ignore
    assert '\nvectorString\n  Field required' in str(err.value)
    assert '\nbaseScore\n  Field required' in str(err.value)


def test_cvss2_wrong_version():
    data = {
        'version': '42',
        'vectorString': conftest.CVSS2_VECTOR_STRING_LOG4J,
        'baseScore': conftest.CVSS2_BASE_SCORE_LOG4J,
    }
    as_json = json.dumps(data)
    message = '1 validation error for CVSS2'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS2.model_validate_json(as_json)
    err_str = str(err.value)
    assert 'version' in err_str
    assert "Input should be '2.0', '3.0' or '3.1'" in err_str


def test_cvss20_log4j_cve_2021_44228():
    data = {
        'version': '2.0',  # str(CvssVersion.two),
        'vectorString': conftest.CVSS2_VECTOR_STRING_LOG4J,
        'baseScore': conftest.CVSS2_BASE_SCORE_LOG4J,
    }
    as_json = json.dumps(data)
    cvss_cve_2021_44228 = CVSS2.model_validate_json(as_json)
    assert isinstance(cvss_cve_2021_44228, CVSS2)
    assert cvss_cve_2021_44228.version == CvssVersion.two
    assert cvss_cve_2021_44228.vector_string == conftest.CVSS2_VECTOR_STRING_LOG4J
    assert cvss_cve_2021_44228.base_score.root == float(conftest.CVSS2_BASE_SCORE_LOG4J)
    assert cvss_cve_2021_44228.confidentiality_requirement is None


def test_cvss30_empty():
    message = '3 validation errors for CVSS30'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS30()  # type: ignore
    assert '\nvectorString\n  Field required' in str(err.value)
    assert '\nbaseScore\n  Field required' in str(err.value)
    assert '\nbaseSeverity\n  Field required' in str(err.value)


def test_cvss30_wrong_version():
    data = {
        'version': '42',
        'vectorString': conftest.CVSS30_VECTOR_STRING_LOG4J,
        'baseScore': conftest.CVSS30_BASE_SCORE_LOG4J,
        'baseSeverity': CVSS30_BASE_SEVERITY_LOG4J,
    }
    as_json = json.dumps(data)
    message = '1 validation error for CVSS30'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS30.model_validate_json(as_json)
    assert "\nversion\n  Input should be '2.0', '3.0' or '3.1'" in str(err.value)


def test_cvss30_log4j_cve_2021_44228():
    data = {
        'version': '3.0',  # str(CvssVersion.three_zero),
        'vectorString': conftest.CVSS30_VECTOR_STRING_LOG4J,
        'baseScore': conftest.CVSS30_BASE_SCORE_LOG4J,
        'baseSeverity': CVSS30_BASE_SEVERITY_LOG4J,
    }
    as_json = json.dumps(data)
    cvss_cve_2021_44228 = CVSS30.model_validate_json(as_json)
    assert isinstance(cvss_cve_2021_44228, CVSS30)
    assert cvss_cve_2021_44228.version == CvssVersion.three_zero
    assert cvss_cve_2021_44228.vector_string == conftest.CVSS30_VECTOR_STRING_LOG4J
    assert cvss_cve_2021_44228.base_score.root == float(conftest.CVSS30_BASE_SCORE_LOG4J)
    assert cvss_cve_2021_44228.base_severity.critical == CvssSeverityType.critical
    assert cvss_cve_2021_44228.confidentiality_requirement is None


def test_cvss31_empty():
    message = '3 validation errors for CVSS31'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS31()  # type: ignore
    assert '\nvectorString\n  Field required' in str(err.value)
    assert '\nbaseScore\n  Field required' in str(err.value)
    assert '\nbaseSeverity\n  Field required' in str(err.value)


def test_cvss31_wrong_version():
    data = {
        'version': '42',
        'vectorString': conftest.CVSS31_VECTOR_STRING_LOG4J,
        'baseScore': conftest.CVSS31_BASE_SCORE_LOG4J,
        'baseSeverity': CVSS31_BASE_SEVERITY_LOG4J,
    }
    as_json = json.dumps(data)
    message = '1 validation error for CVSS31'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS31.model_validate_json(as_json)
    assert "\nversion\n  Input should be '2.0', '3.0' or '3.1'" in str(err.value)


def test_cvss31_log4j_cve_2021_44228():
    data = {
        'version': '3.1',  # str(CvssVersion.three_wun),
        'vectorString': conftest.CVSS31_VECTOR_STRING_LOG4J,
        'baseScore': conftest.CVSS31_BASE_SCORE_LOG4J,
        'baseSeverity': CVSS31_BASE_SEVERITY_LOG4J,
    }
    as_json = json.dumps(data)
    cvss_cve_2021_44228 = CVSS31.model_validate_json(as_json)
    assert isinstance(cvss_cve_2021_44228, CVSS31)
    assert cvss_cve_2021_44228.version == CvssVersion.three_wun
    assert cvss_cve_2021_44228.vector_string == conftest.CVSS31_VECTOR_STRING_LOG4J
    assert cvss_cve_2021_44228.base_score.root == float(conftest.CVSS31_BASE_SCORE_LOG4J)
    assert cvss_cve_2021_44228.base_severity.critical == CvssSeverityType.critical
    assert cvss_cve_2021_44228.confidentiality_requirement is None


def test_cvss31_minimal():
    vector_string = 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H'
    expected_value = (
        f'{{"version":"3.1","vectorString":"{vector_string}","attackVector":null,'
        '"attackComplexity":null,"privilegesRequired":null,"userInteraction":null,"scope":null,'
        '"confidentialityImpact":null,"integrityImpact":null,"availabilityImpact":null,"baseScore":10.0,'
        '"baseSeverity":"CRITICAL","exploitCodeMaturity":null,"remediationLevel":null,"reportConfidence":null,'
        '"temporalScore":null,"temporalSeverity":null,"confidentialityRequirement":null,'
        '"integrityRequirement":null,"availabilityRequirement":null,"modifiedAttackVector":null,'
        '"modifiedAttackComplexity":null,"modifiedPrivilegesRequired":null,"modifiedUserInteraction":null,'
        '"modifiedScope":null,"modifiedConfidentialityImpact":null,"modifiedIntegrityImpact":null,'
        '"modifiedAvailabilityImpact":null,"environmentalScore":null,"environmentalSeverity":null}'
    )
    c31 = cvss.CVSS31.model_validate_json(JSON)
    assert c31.model_dump_json() == expected_value
    assert c31.vector_string == vector_string

    json_lines = c31.model_dump_json(indent=2).split('\n')
    json_rep_of_vs = [line for line in json_lines if 'vectorString' in line]
    assert len(json_rep_of_vs) == 1
    assert vector_string in json_rep_of_vs[0]
    assert '"vectorString":' in json_rep_of_vs[0]

    expected_schema = {
        'title': 'CVSS31',
        'type': 'object',
        'properties': {
            'version': {'description': 'CVSS Version', 'default': '3.1', 'allOf': [{'$ref': '#/$defs/Version'}]},
            'vectorString': {
                'title': 'Vectorstring',
                'pattern': (
                    '^CVSS:3[.]1/((AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:'
                    '[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*'
                    '(AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:'
                    '[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'
                ),
                'type': 'string',
            },
            'attackVector': {
                'anyOf': [{'$ref': '#/$defs/AttackVectorType'}, {'type': 'null'}],
                'default': None,
            },
            'attackComplexity': {
                'anyOf': [{'$ref': '#/$defs/AttackComplexityType'}, {'type': 'null'}],
                'default': None,
            },
            'privilegesRequired': {
                'anyOf': [{'$ref': '#/$defs/PrivilegesRequiredType'}, {'type': 'null'}],
                'default': None,
            },
            'userInteraction': {
                'anyOf': [{'$ref': '#/$defs/UserInteractionType'}, {'type': 'null'}],
                'default': None,
            },
            'scope': {
                'anyOf': [{'$ref': '#/$defs/ScopeType'}, {'type': 'null'}],
                'default': None,
            },
            'confidentialityImpact': {
                'anyOf': [{'$ref': '#/$defs/CiaType'}, {'type': 'null'}],
                'default': None,
            },
            'integrityImpact': {
                'anyOf': [{'$ref': '#/$defs/CiaType'}, {'type': 'null'}],
                'default': None,
            },
            'availabilityImpact': {
                'anyOf': [{'$ref': '#/$defs/CiaType'}, {'type': 'null'}],
                'default': None,
            },
            'baseScore': {'$ref': '#/$defs/ScoreType'},
            'baseSeverity': {'$ref': '#/$defs/SeverityType'},
            'exploitCodeMaturity': {
                'anyOf': [{'$ref': '#/$defs/ExploitCodeMaturityType'}, {'type': 'null'}],
                'default': None,
            },
            'remediationLevel': {
                'anyOf': [{'$ref': '#/$defs/RemediationLevelType'}, {'type': 'null'}],
                'default': None,
            },
            'reportConfidence': {
                'anyOf': [{'$ref': '#/$defs/ConfidenceType'}, {'type': 'null'}],
                'default': None,
            },
            'temporalScore': {
                'anyOf': [{'$ref': '#/$defs/ScoreType'}, {'type': 'null'}],
                'default': None,
            },
            'temporalSeverity': {
                'anyOf': [{'$ref': '#/$defs/SeverityType'}, {'type': 'null'}],
                'default': None,
            },
            'confidentialityRequirement': {
                'anyOf': [{'$ref': '#/$defs/CiaRequirementType'}, {'type': 'null'}],
                'default': None,
            },
            'integrityRequirement': {
                'anyOf': [{'$ref': '#/$defs/CiaRequirementType'}, {'type': 'null'}],
                'default': None,
            },
            'availabilityRequirement': {
                'anyOf': [{'$ref': '#/$defs/CiaRequirementType'}, {'type': 'null'}],
                'default': None,
            },
            'modifiedAttackVector': {
                'anyOf': [{'$ref': '#/$defs/ModifiedAttackVectorType'}, {'type': 'null'}],
                'default': None,
            },
            'modifiedAttackComplexity': {
                'anyOf': [{'$ref': '#/$defs/ModifiedAttackComplexityType'}, {'type': 'null'}],
                'default': None,
            },
            'modifiedPrivilegesRequired': {
                'anyOf': [{'$ref': '#/$defs/ModifiedPrivilegesRequiredType'}, {'type': 'null'}],
                'default': None,
            },
            'modifiedUserInteraction': {
                'anyOf': [{'$ref': '#/$defs/ModifiedUserInteractionType'}, {'type': 'null'}],
                'default': None,
            },
            'modifiedScope': {
                'anyOf': [{'$ref': '#/$defs/ModifiedScopeType'}, {'type': 'null'}],
                'default': None,
            },
            'modifiedConfidentialityImpact': {
                'anyOf': [{'$ref': '#/$defs/ModifiedCiaType'}, {'type': 'null'}],
                'default': None,
            },
            'modifiedIntegrityImpact': {
                'anyOf': [{'$ref': '#/$defs/ModifiedCiaType'}, {'type': 'null'}],
                'default': None,
            },
            'modifiedAvailabilityImpact': {
                'anyOf': [{'$ref': '#/$defs/ModifiedCiaType'}, {'type': 'null'}],
                'default': None,
            },
            'environmentalScore': {
                'anyOf': [{'$ref': '#/$defs/ScoreType'}, {'type': 'null'}],
                'default': None,
            },
            'environmentalSeverity': {
                'anyOf': [{'$ref': '#/$defs/SeverityType'}, {'type': 'null'}],
                'default': None,
            },
        },
        'required': ['vectorString', 'baseScore', 'baseSeverity'],
        '$defs': {
            'Version': {
                'description': 'CVSS Version',
                'enum': ['2.0', '3.0', '3.1'],
                'title': 'Version',
                'type': 'string',
            },
            'AttackVectorType': {
                'enum': ['NETWORK', 'ADJACENT_NETWORK', 'LOCAL', 'PHYSICAL'],
                'title': 'AttackVectorType',
                'type': 'string',
            },
            'AttackComplexityType': {
                'enum': ['HIGH', 'LOW'],
                'title': 'AttackComplexityType',
                'type': 'string',
            },
            'PrivilegesRequiredType': {
                'enum': ['HIGH', 'LOW', 'NONE'],
                'title': 'PrivilegesRequiredType',
                'type': 'string',
            },
            'UserInteractionType': {
                'enum': ['NONE', 'REQUIRED'],
                'title': 'UserInteractionType',
                'type': 'string',
            },
            'ScopeType': {
                'enum': ['UNCHANGED', 'CHANGED'],
                'title': 'ScopeType',
                'type': 'string',
            },
            'CiaType': {
                'enum': ['NONE', 'LOW', 'HIGH'],
                'title': 'CiaType',
                'type': 'string',
            },
            'ScoreType': {'title': 'ScoreType', 'minimum': 0.0, 'maximum': 10.0, 'type': 'number'},
            'SeverityType': {
                'enum': ['NONE', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL'],
                'title': 'SeverityType',
                'type': 'string',
            },
            'ExploitCodeMaturityType': {
                'enum': ['UNPROVEN', 'PROOF_OF_CONCEPT', 'FUNCTIONAL', 'HIGH', 'NOT_DEFINED'],
                'title': 'ExploitCodeMaturityType',
                'type': 'string',
            },
            'RemediationLevelType': {
                'enum': ['OFFICIAL_FIX', 'TEMPORARY_FIX', 'WORKAROUND', 'UNAVAILABLE', 'NOT_DEFINED'],
                'title': 'RemediationLevelType',
                'type': 'string',
            },
            'ConfidenceType': {
                'enum': ['UNKNOWN', 'REASONABLE', 'CONFIRMED', 'NOT_DEFINED'],
                'title': 'ConfidenceType',
                'type': 'string',
            },
            'CiaRequirementType': {
                'enum': ['LOW', 'MEDIUM', 'HIGH', 'NOT_DEFINED'],
                'title': 'CiaRequirementType',
                'type': 'string',
            },
            'ModifiedAttackVectorType': {
                'enum': ['NETWORK', 'ADJACENT_NETWORK', 'LOCAL', 'PHYSICAL', 'NOT_DEFINED'],
                'title': 'ModifiedAttackVectorType',
                'type': 'string',
            },
            'ModifiedAttackComplexityType': {
                'enum': ['HIGH', 'LOW', 'NOT_DEFINED'],
                'title': 'ModifiedAttackComplexityType',
                'type': 'string',
            },
            'ModifiedPrivilegesRequiredType': {
                'enum': ['HIGH', 'LOW', 'NONE', 'NOT_DEFINED'],
                'title': 'ModifiedPrivilegesRequiredType',
                'type': 'string',
            },
            'ModifiedUserInteractionType': {
                'enum': ['NONE', 'REQUIRED', 'NOT_DEFINED'],
                'title': 'ModifiedUserInteractionType',
                'type': 'string',
            },
            'ModifiedScopeType': {
                'enum': ['UNCHANGED', 'CHANGED', 'NOT_DEFINED'],
                'title': 'ModifiedScopeType',
                'type': 'string',
            },
            'ModifiedCiaType': {
                'enum': ['NONE', 'LOW', 'HIGH', 'NOT_DEFINED'],
                'title': 'ModifiedCiaType',
                'type': 'string',
            },
        },
    }
    assert c31.model_json_schema(by_alias=True) == expected_schema
