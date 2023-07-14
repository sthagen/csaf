import json
import pytest  # type: ignore

import csaf.csaf as api

VECTOR_STRING = 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H'
DATA = {
    'document': {
        'aggregate_severity': {
            'text': 'Moderate',
        },
        'category': 'csaf_security_advisory',
        'csaf_version': '2.0',
        'distribution': {
            'tlp': {
                'label': 'WHITE',
                'url': 'https://www.first.org/tlp/',
            },
        },
        'lang': 'en-US',
        'publisher': {
            'category': 'coordinator',
            'name': 'Bundesamt für Sicherheit in der Informationstechnik',
            'namespace': 'https://www.bsi.bund.de',
        },
        'title': 'CVRF-CSAF-Converter: XML External Entities Vulnerability',
        'tracking': {
            'current_release_date': '2022-03-17T13:03:42.105Z',
            'generator': {
                'date': '2022-03-17T13:09:42.105Z',
                'engine': {
                    'name': 'Secvisogram',
                    'version': '1.12.1',
                },
            },
            'id': 'BSI-2022-0001',
            'initial_release_date': '2022-03-17T13:03:42.105Z',
            'revision_history': [
                {
                    'date': '2022-03-17T13:03:42.105Z',
                    'number': '1',
                    'summary': 'Initial revision',
                },
            ],
            'status': 'final',
            'version': '1',
        },
    },
    'product_tree': {
        'branches': [
            {
                'branches': [
                    {
                        'branches': [
                            {
                                'category': 'product_version',
                                'name': '1.0.0-alpha',
                                'product': {
                                    'name': 'CSAF Tools CVRF-CSAF-Converter 1.0.0-alpha',
                                    'product_id': 'CSAFPID-0001',
                                    'product_identification_helper': {
                                        'cpe': 'cpe:/a:csaf-tools:cvrf-csaf-converter:1.0.0-alpha',
                                    },
                                },
                            },
                            {
                                'category': 'product_version',
                                'name': '1.0.0-dev1',
                                'product': {
                                    'name': 'CSAF Tools CVRF-CSAF-Converter 1.0.0-dev1',
                                    'product_id': 'CSAFPID-0002',
                                    'product_identification_helper': {
                                        'cpe': 'cpe:/a:csaf-tools:cvrf-csaf-converter:1.0.0-dev1',
                                    },
                                },
                            },
                            {
                                'category': 'product_version',
                                'name': '1.0.0-dev2',
                                'product': {
                                    'name': 'CSAF Tools CVRF-CSAF-Converter 1.0.0-dev2',
                                    'product_id': 'CSAFPID-0003',
                                    'product_identification_helper': {
                                        'cpe': 'cpe:/a:csaf-tools:cvrf-csaf-converter:1.0.0-dev2',
                                    },
                                },
                            },
                            {
                                'category': 'product_version',
                                'name': '1.0.0-dev3',
                                'product': {
                                    'name': 'CSAF Tools CVRF-CSAF-Converter 1.0.0-dev3',
                                    'product_id': 'CSAFPID-0004',
                                    'product_identification_helper': {
                                        'cpe': 'cpe:/a:csaf-tools:cvrf-csaf-converter:1.0.0-dev3',
                                    },
                                },
                            },
                            {
                                'category': 'product_version',
                                'name': '1.0.0-rc1',
                                'product': {
                                    'name': 'CSAF Tools CVRF-CSAF-Converter 1.0.0-rc1',
                                    'product_id': 'CSAFPID-0005',
                                    'product_identification_helper': {
                                        'cpe': 'cpe:/a:csaf-tools:cvrf-csaf-converter:1.0.0-rc1',
                                    },
                                },
                            },
                            {
                                'category': 'product_version',
                                'name': '1.0.0-rc2',
                                'product': {
                                    'name': 'CSAF Tools CVRF-CSAF-Converter 1.0.0-rc2',
                                    'product_id': 'CSAFPID-0006',
                                    'product_identification_helper': {
                                        'cpe': 'cpe:/a:csaf-tools:cvrf-csaf-converter:1.0.0-rc2',
                                    },
                                },
                            },
                        ],
                        'category': 'product_name',
                        'name': 'CVRF-CSAF-Converter',
                    },
                ],
                'category': 'vendor',
                'name': 'CSAF Tools',
            },
        ],
    },
    'vulnerabilities': [
        {
            'acknowledgments': [
                {
                    'names': [
                        'Damian Pfammatter',
                    ],
                    'organization': 'Cyber-Defense Campus',
                    'summary': 'Finding and reporting the vulnerability',
                },
            ],
            'cve': 'CVE-2022-27193',
            'cwe': {
                'id': 'CWE-611',
                'name': 'Improper Restriction of XML External Entity Reference',
            },
            'ids': [
                {
                    'system_name': 'Github Issue',
                    'text': 'csaf-tools/CVRF-CSAF-Converter#78',
                },
            ],
            'notes': [
                {
                    'category': 'description',
                    'text': (
                        'CSAF Tools CVRF-CSAF-Converter 1.0.0-rc1 resolves XML External Entities (XXE).'
                        ' This leads to the inclusion of arbitrary (local) file content into'
                        ' the generated output document.'
                        ' An attacker can exploit this to disclose information from the system running the converter.'
                    ),
                    'title': 'Vulnerability description',
                },
            ],
            'product_status': {
                'first_fixed': [
                    'CSAFPID-0006',
                ],
                'fixed': [
                    'CSAFPID-0006',
                ],
                'known_affected': [
                    'CSAFPID-0001',
                    'CSAFPID-0002',
                    'CSAFPID-0003',
                    'CSAFPID-0004',
                    'CSAFPID-0005',
                ],
            },
            'remediations': [
                {
                    'category': 'vendor_fix',
                    'date': '2022-03-14T13:10:55.000+01:00',
                    'details': 'Update to the latest version of the product. At least version 1.0.0-rc2',
                    'product_ids': [
                        'CSAFPID-0001',
                        'CSAFPID-0002',
                        'CSAFPID-0003',
                        'CSAFPID-0004',
                        'CSAFPID-0005',
                    ],
                    'url': 'https://github.com/csaf-tools/CVRF-CSAF-Converter/releases/tag/1.0.0-rc2',
                }
            ],
            'scores': [
                {
                    'cvss_v3': {
                        'baseScore': 6.1,
                        'baseSeverity': 'MEDIUM',
                        'vectorString': VECTOR_STRING,
                        'version': '3.1',
                    },
                    'products': [
                        'CSAFPID-0001',
                        'CSAFPID-0002',
                        'CSAFPID-0003',
                        'CSAFPID-0004',
                        'CSAFPID-0005',
                    ],
                },
            ],
        },
    ],
}
JSON = json.dumps(DATA)


def test_csaf_minimal():
    doc = api.CSAF.model_validate_json(JSON)
    json_lines = doc.json(indent=2).split('\n')
    json_rep_of_vs = [line for line in json_lines if 'vectorString' in line]
    assert len(json_rep_of_vs) == 1
    assert VECTOR_STRING in json_rep_of_vs[0]
    assert '"vectorString":' in json_rep_of_vs[0]
