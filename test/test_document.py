from test import conftest

import msgspec
import pytest
from pydantic import ValidationError

import csaf.csaf as csaf


def _subs(count: int, what: str) -> str:
    """DRY."""
    return f'{count} validation error{"" if count == 1 else "s"} for {what}'


def test_doc_empty_meta():
    with pytest.raises(ValidationError, match=_subs(5, 'Document')) as err:
        _ = csaf.CSAF(document=csaf.Document())  # type: ignore
    for prop in ('category', 'csaf_version', 'publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  Field required' in str(err.value)


def test_doc_ok_if_spammy():
    doc = csaf.CSAF(**conftest.DOC_OK)
    strip_me = msgspec.json.decode(doc.model_dump_json())
    conftest._strip_and_iso_grace(strip_me)
    assert strip_me == conftest.DOC_OK


def test_doc_vulnerability_empty():
    with pytest.raises(ValidationError, match=_subs(1, 'CSAF')) as err:
        _ = csaf.CSAF(**conftest.DOC_VULN_EMPTY)
    assert '\nvulnerabilities\n  List should have at least 1 item after validation, not 0' in str(err.value)
