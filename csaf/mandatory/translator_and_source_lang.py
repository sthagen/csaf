"""6.1.15 Translator

It must be tested that /document/source_lang is present and set if the value translator is used
for /document/publisher/category.

The relevant path for this test is:

    /document/source_lang

Example 54 which fails the test:

  "document": {
    // ...
    "publisher": {
      "category": "translator",
      "name": "CSAF TC Translator",
      "namespace": "https://csaf.io/translator"
    },
    "title": "Mandatory test: Translator (failing example 1)",
    // ...
  }

The required element source_lang is missing.
"""

ID = (6, 1, 15)
TOPIC = 'Translator'
BASE_URL = 'https://docs.oasis-open.org/csaf/csaf/v2.0/cs01/csaf-v2.0-cs01.html'
REFERENCE = f'{BASE_URL}#6115-translator'
TRIGGER_PATH = '/document/publisher/category'
TRIGGER_JMES_PATH = TRIGGER_PATH.lstrip('/').replace('/', '.')
TRIGGER_VALUE = 'translator'
CONDITION_PATH = '/document/source_lang'
CONDITION_JMES_PATH = CONDITION_PATH.lstrip('/').replace('/', '.')
PATHS = (CONDITION_PATH,)
