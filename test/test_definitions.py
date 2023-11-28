import pytest
from pydantic import ValidationError

from csaf.definitions import Acknowledgment, References, Reference


def _subs(count: int, what: str) -> str:
    """DRY."""
    return f'{count} validation error{"" if count == 1 else "s"} for {what}'


def test_def_acknowledgement_empty():
    a = Acknowledgment()
    assert a.model_dump_json() == '{"names":null,"organization":null,"summary":null,"urls":null}'


def test_def_acknowledgment_names():
    a = Acknowledgment(names=['a'])
    assert a.model_dump_json() == '{"names":["a"],"organization":null,"summary":null,"urls":null}'


def test_def_acknowledgment_summary():
    a = Acknowledgment(summary='b')
    assert a.model_dump_json() == '{"names":null,"organization":null,"summary":"b","urls":null}'


def test_def_acknowledgment_urls():
    a = Acknowledgment(urls=['https://example.com'])
    assert a.model_dump_json() == '{"names":null,"organization":null,"summary":null,"urls":["https://example.com/"]}'


def test_def_reference_empty():
    with pytest.raises(ValidationError, match=_subs(2, 'Reference')) as err:
        _ = Reference()  # type: ignore
    for prop in ('summary', 'url'):
        assert f'\n{prop}\n  Field required' in str(err.value)


def test_def_reference_summary_url():
    r = Reference(summary='b', url='file:///')
    assert r.model_dump_json() == '{"category":"external","summary":"b","url":"file:///"}'


def test_def_reference_url():
    rs = References([Reference(summary='b', url='file:///')])
    assert rs.model_dump_json() == '[{"category":"external","summary":"b","url":"file:///"}]'
