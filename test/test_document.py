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


def test_doc_meta_none():
    with pytest.raises(ValidationError, match=_subs(5, 'Document')) as err:
        _ = csaf.Document()  # type: ignore
    for prop in ('category', 'csaf_version', 'publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  Field required' in str(err.value)


def test_doc_meta_category_empty():
    with pytest.raises(ValidationError, match=_subs(5, 'Document')) as err:
        _ = csaf.Document(category='')  # type: ignore
    hint = 'String should have at least 1 character'
    assert f'\ncategory\n  {hint}' in str(err.value)
    for prop in ('csaf_version', 'publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  Field required' in str(err.value)


def test_doc_meta_csaf_version_wrong():
    with pytest.raises(ValidationError, match=_subs(4, 'Document')) as err:
        _ = csaf.Document(**conftest.META_WRONG_VERSION)  # type: ignore
    hint = "Input should be '2.0'"
    assert f'\ncsaf_version\n  {hint}' in str(err.value)
    for prop in ('publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  Field required' in str(err.value)


def test_doc_meta_publisher_empty():
    with pytest.raises(ValidationError, match=_subs(5, 'Document')) as err:
        _ = csaf.Document(**conftest.META_EMPTY_PUBLISHER)  # type: ignore
    for prop in ('title', 'tracking'):
        assert f'\n{prop}\n  Field required' in str(err.value)
    host = 'publisher'
    for prop in ('category', 'name', 'namespace'):
        assert f'\n{host}.{prop}\n  Field required' in str(err.value)


def test_doc_meta_title_empty():
    with pytest.raises(ValidationError, match=_subs(2, 'Document')) as err:
        _ = csaf.Document(**conftest.META_EMPTY_TITLE)  # type: ignore
    hint = 'String should have at least 1 character'
    assert f'\ntitle\n  {hint}' in str(err.value)
    for prop in ('tracking',):
        assert f'\n{prop}\n  Field required' in str(err.value)


def test_doc_meta_tracking_empty():
    with pytest.raises(ValidationError, match=_subs(6, 'Document')) as err:
        _ = csaf.Document(**conftest.META_EMPTY_TRACKING)  # type: ignore
    host = 'tracking'
    for prop in ('current_release_date', 'id', 'initial_release_date', 'revision_history', 'status', 'version'):
        assert f'\n{host}.{prop}\n  Field required' in str(err.value)


def test_doc_ok_if_spammy():
    doc = csaf.CSAF(**conftest.DOC_OK)
    strip_me = msgspec.json.decode(doc.model_dump_json())
    conftest._strip_and_iso_grace(strip_me)
    assert strip_me == conftest.DOC_OK


def test_doc_vulnerability_empty():
    with pytest.raises(ValidationError, match=_subs(1, 'CSAF')) as err:
        _ = csaf.CSAF(**conftest.DOC_VULN_EMPTY)
    assert '\nvulnerabilities\n  List should have at least 1 item after validation, not 0' in str(err.value)
