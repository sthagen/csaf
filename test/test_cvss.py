import json
import pytest  # type: ignore

import csaf.cvss as cvss

DATA = {
    'baseScore': 10.0,
    'baseSeverity': 'CRITICAL',
    'vectorString': 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H',
    'version': '3.1',
}
JSON = json.dumps(DATA)


def test_cvss31_minimal():
    vector_string = 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H'
    expected_value = (
        f'{{"version": "3.1", "vectorString": "{vector_string}", "attackVector": null,'
        ' "attackComplexity": null, "privilegesRequired": null, "userInteraction": null, "scope": null,'
        ' "confidentialityImpact": null, "integrityImpact": null, "availabilityImpact": null, "baseScore": 10.0,'
        ' "baseSeverity": "CRITICAL", "exploitCodeMaturity": null, "remediationLevel": null, "reportConfidence": null,'
        ' "temporalScore": null, "temporalSeverity": null, "confidentialityRequirement": null,'
        ' "integrityRequirement": null, "availabilityRequirement": null, "modifiedAttackVector": null,'
        ' "modifiedAttackComplexity": null, "modifiedPrivilegesRequired": null, "modifiedUserInteraction": null,'
        ' "modifiedScope": null, "modifiedConfidentialityImpact": null, "modifiedIntegrityImpact": null,'
        ' "modifiedAvailabilityImpact": null, "environmentalScore": null, "environmentalSeverity": null}'
    )
    c31 = cvss.CVSS31.parse_raw(JSON)
    assert c31.json() == expected_value
    assert c31.vector_string == vector_string

    json_lines = c31.json(indent=2).split('\n')
    json_rep_of_vs = [line for line in json_lines if 'vectorString' in line]
    assert len(json_rep_of_vs) == 1
    assert vector_string in json_rep_of_vs[0]
    assert '"vectorString":' in json_rep_of_vs[0]

    expected_schema = {
        'title': 'CVSS31',
        'type': 'object',
        'properties': {
            'version': {
                'description': 'CVSS Version',
                'default': '3.1',
                'allOf': [
                    {'$ref': '#/definitions/Version'}
                ]
            },
            'vectorString': {
                'title': 'Vectorstring',
                'pattern': (
                    '^CVSS:3[.]1/((AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:'
                    '[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*'
                    '(AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:'
                    '[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'
                ),
                'type': 'string'
            },
            'attackVector': {'$ref': '#/definitions/AttackVectorType'},
            'attackComplexity': {'$ref': '#/definitions/AttackComplexityType'},
            'privilegesRequired': {'$ref': '#/definitions/PrivilegesRequiredType'},
            'userInteraction': {'$ref': '#/definitions/UserInteractionType'},
            'scope': {'$ref': '#/definitions/ScopeType'},
            'confidentialityImpact': {'$ref': '#/definitions/CiaType'},
            'integrityImpact': {'$ref': '#/definitions/CiaType'},
            'availabilityImpact': {'$ref': '#/definitions/CiaType'},
            'baseScore': {'$ref': '#/definitions/ScoreType'},
            'baseSeverity': {'$ref': '#/definitions/SeverityType'},
            'exploitCodeMaturity': {'$ref': '#/definitions/ExploitCodeMaturityType'},
            'remediationLevel': {'$ref': '#/definitions/RemediationLevelType'},
            'reportConfidence': {'$ref': '#/definitions/ConfidenceType'},
            'temporalScore': {'$ref': '#/definitions/ScoreType'},
            'temporalSeverity': {'$ref': '#/definitions/SeverityType'},
            'confidentialityRequirement': {'$ref': '#/definitions/CiaRequirementType'},
            'integrityRequirement': {'$ref': '#/definitions/CiaRequirementType'},
            'availabilityRequirement': {'$ref': '#/definitions/CiaRequirementType'},
            'modifiedAttackVector': {'$ref': '#/definitions/ModifiedAttackVectorType'},
            'modifiedAttackComplexity': {'$ref': '#/definitions/ModifiedAttackComplexityType'},
            'modifiedPrivilegesRequired': {'$ref': '#/definitions/ModifiedPrivilegesRequiredType'},
            'modifiedUserInteraction': {'$ref': '#/definitions/ModifiedUserInteractionType'},
            'modifiedScope': {'$ref': '#/definitions/ModifiedScopeType'},
            'modifiedConfidentialityImpact': {'$ref': '#/definitions/ModifiedCiaType'},
            'modifiedIntegrityImpact': {'$ref': '#/definitions/ModifiedCiaType'},
            'modifiedAvailabilityImpact': {'$ref': '#/definitions/ModifiedCiaType'},
            'environmentalScore': {'$ref': '#/definitions/ScoreType'},
            'environmentalSeverity': {'$ref': '#/definitions/SeverityType'}
        },
        'required': ['vectorString', 'baseScore', 'baseSeverity'],
        'definitions': {
            'Version': {
                'title': 'Version',
                'description': 'CVSS Version',
                'enum': ['2.0', '3.0', '3.1']
            },
            'AttackVectorType': {
                'title': 'AttackVectorType',
                'description': 'An enumeration.',
                'enum': ['NETWORK', 'ADJACENT_NETWORK', 'LOCAL', 'PHYSICAL']
            },
            'AttackComplexityType': {
                'title': 'AttackComplexityType',
                'description': 'An enumeration.',
                'enum': ['HIGH', 'LOW']
            },
            'PrivilegesRequiredType': {
                'title': 'PrivilegesRequiredType',
                'description': 'An enumeration.',
                'enum': ['HIGH', 'LOW', 'NONE']
            },
            'UserInteractionType': {
                'title': 'UserInteractionType',
                'description': 'An enumeration.',
                'enum': ['NONE', 'REQUIRED']
            },
            'ScopeType': {
                'title': 'ScopeType',
                'description': 'An enumeration.',
                'enum': ['UNCHANGED', 'CHANGED']
            },
            'CiaType': {
                'title': 'CiaType',
                'description': 'An enumeration.',
                'enum': ['NONE', 'PARTIAL', 'COMPLETE']
            },
            'ScoreType': {
                'title': 'ScoreType',
                'minimum': 0.0,
                'maximum': 10.0,
                'type': 'number'
            },
            'SeverityType': {
                'title': 'SeverityType',
                'description': 'An enumeration.',
                'enum': ['NONE', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL']
            },
            'ExploitCodeMaturityType': {
                'title': 'ExploitCodeMaturityType',
                'description': 'An enumeration.',
                'enum': ['UNPROVEN', 'PROOF_OF_CONCEPT', 'FUNCTIONAL', 'HIGH', 'NOT_DEFINED']
            },
            'RemediationLevelType': {
                'title': 'RemediationLevelType', 'description': 'An enumeration.',
                'enum': ['OFFICIAL_FIX', 'TEMPORARY_FIX', 'WORKAROUND', 'UNAVAILABLE',
                         'NOT_DEFINED']
            },
            'ConfidenceType': {
                'title': 'ConfidenceType', 'description': 'An enumeration.',
                'enum': ['UNKNOWN', 'REASONABLE', 'CONFIRMED', 'NOT_DEFINED']
            },
            'CiaRequirementType': {
                'title': 'CiaRequirementType', 'description': 'An enumeration.',
                'enum': ['LOW', 'MEDIUM', 'HIGH', 'NOT_DEFINED']
            },
            'ModifiedAttackVectorType': {
                'title': 'ModifiedAttackVectorType', 'description': 'An enumeration.',
                'enum': ['NETWORK', 'ADJACENT_NETWORK', 'LOCAL', 'PHYSICAL', 'NOT_DEFINED']
            },
            'ModifiedAttackComplexityType': {
                'title': 'ModifiedAttackComplexityType', 'description': 'An enumeration.',
                'enum': ['HIGH', 'LOW', 'NOT_DEFINED']
            },
            'ModifiedPrivilegesRequiredType': {
                'title': 'ModifiedPrivilegesRequiredType',
                'description': 'An enumeration.',
                'enum': ['HIGH', 'LOW', 'NONE', 'NOT_DEFINED']
            },
            'ModifiedUserInteractionType': {
                'title': 'ModifiedUserInteractionType', 'description': 'An enumeration.',
                'enum': ['NONE', 'REQUIRED', 'NOT_DEFINED']
            },
            'ModifiedScopeType': {
                'title': 'ModifiedScopeType', 'description': 'An enumeration.',
                'enum': ['UNCHANGED', 'CHANGED', 'NOT_DEFINED']
            },
            'ModifiedCiaType': {
                'title': 'ModifiedCiaType', 'description': 'An enumeration.',
                'enum': ['NONE', 'LOW', 'HIGH', 'NOT_DEFINED']
            }
        }
    }
    assert c31.schema(by_alias=True) == expected_schema
