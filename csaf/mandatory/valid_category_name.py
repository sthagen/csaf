"""6.1.26 Prohibited Document Category Name

It must be tested that the document category is not equal to the (case insensitive) name of
any other profile than "Generic CSAF".
This does not differentiate between underscore, dash or whitespace.
This test does only apply for CSAF documents with the profile "Generic CSAF".
Therefore, it must be skipped if the document category matches one of the values defined for the profile
other than "Generic CSAF".

>For CSAF 2.0, the test must be skipped for the following values in /document/category:
  security_incident_response
  informational_advisory
  security_advisory
  vex

This is the only test related to the profile "Generic CSAF" as the required fields SHALL be checked by
validating the JSON schema.

The relevant path for this test is:

  /document/category

Examples 65 for currently prohibited values:

  Informational Advisory
  security-incident-response
  Security      Advisory
  veX

Example 66 which fails the test:

  "category": "Security_Incident_Response"

> The value Security_Incident_Response is the name of a profile where the space was replaced with underscores.

"""

ID = (6, 1, 26)
TOPIC = 'Prohibited Document Category Name'
BASE_URL = 'https://docs.oasis-open.org/csaf/csaf/v2.0/cs01/csaf-v2.0-cs01.html'
REFERENCE = f'{BASE_URL}#6126-prohibited-document-category-name'
CONDITION_PATH = '/document/category'
CONDITION_JMES_PATH = CONDITION_PATH.lstrip('/').replace('/', '.')
PATHS = (CONDITION_PATH,)
PROFILES = (
    'informational_advisory',
    'security_advisory',
    'security_incident_response',
    'vex',
)
MIN_LEN = min(len(profile) for profile in PROFILES)
STRIP_THESE = ''.join(IRRELEVANT_CHARACTERS := (SPACE := ' ', UNDERSCORE := '_', DASH := '-'))


def is_valid(text: str) -> bool:
    """Verify category match per spec (disambiguation)."""
    if not text:  # empty (implementer safeguard)
        return False

    if not (text_strip := text.strip(STRIP_THESE)) or len(text) < MIN_LEN:  # short enough or irrelevant chars only
        return True

    # characters other than space present
    term = UNDERSCORE.join(w for w in text.replace(DASH, SPACE).replace(UNDERSCORE, SPACE).split(SPACE) if w.strip())
    term_lc_in_profiles = (term_lc := term.lower()) in PROFILES

    return True if not term_lc_in_profiles or all([term_lc_in_profiles, term_lc == term, text_strip == text]) else False
