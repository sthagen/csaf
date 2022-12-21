# -*- coding: utf-8 -*-
# pylint: disable=c-extension-no-member,expression-not-assigned,line-too-long,logging-fstring-interpolation
"""CSAF Document model.

Minimal length of CSAF (spam) JSON is 116 bytes:
0        1         2         3         4         5         6         7         8         9
12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012
{"document":{"category":" ","csaf_version":"2.0","publisher":{},"title":" ","tracking":{}}}}
"""
from __future__ import annotations

import pathlib
from itertools import chain
from typing import Annotated, Dict, Iterator, List, Mapping, Optional, Tuple, no_type_check

import jmespath
import msgspec
from langcodes import tag_is_valid
from lazr.uri import URI, InvalidURIError  # type: ignore
from pydantic import BaseModel, Field, validator

import csaf
from csaf import log
from csaf.document import Document
from csaf.mandatory.rules import (
    is_valid,
    is_valid_category,
    is_valid_defined_group_ids,
    is_valid_defined_product_ids,
    is_valid_translator,
    is_valid_unique_group_ids,
    is_valid_unique_product_ids,
)
from csaf.product import ProductTree
from csaf.vulnerability import Vulnerability

ENCODING_ERRORS_POLICY = 'ignore'
CSAF_MIN_BYTES = 92
CSAF_WARN_MAX_BYTES = 15 << 20
CSAF_VERSION_STRING = '2.0'


class CSAF(BaseModel):
    """
    Representation of security advisory information as a JSON document.
    """

    document: Annotated[
        Document,
        Field(
            description='Captures the meta-data about this document describing a particular set of'
            ' security advisories.',
            title='Document level meta-data',
        ),
    ]
    product_tree: Annotated[
        Optional[ProductTree],
        Field(
            description='Is a container for all fully qualified product names that can be referenced elsewhere'
            ' in the document.',
            title='Product tree',
        ),
    ]
    vulnerabilities: Annotated[
        Optional[List[Vulnerability]],
        Field(
            description='Represents a list of all relevant vulnerability information items.',
            min_items=1,
            title='Vulnerabilities',
        ),
    ]

    @no_type_check
    @validator('vulnerabilities')
    @classmethod
    def check_len(cls, v):
        if not v:
            raise ValueError('vulnerabilities present but empty')
        return v


@no_type_check
def document_optional_acknowledgments(values):
    """Verify optional properties of document/acknowledgments if present follow rules."""
    parent, prop = 'document', 'acknowledgments'
    if not isinstance(values, list):
        return 1, f'optional {parent} property {prop} present but no array'
    if not values:
        return 1, f'optional {parent} property {prop} present but empty'
    ack_opt_props = ('names', 'organization', 'summary', 'urls')
    min_props, max_props = 1, len(ack_opt_props)
    ack_known_props = {el for el in ack_opt_props}
    for pos, value in enumerate(values):
        jp = f'properties of {parent}.{prop}[{pos}]'
        # log.info(pos, value)
        ack_found_props = {el for el in value}
        # log.info(ack_found_props)
        if ack_found_props <= ack_known_props:
            log.info(f'set of {jp} only contains known properties')
        if ack_found_props < ack_known_props:
            log.info(f'set of {jp} is a proper subset of the known properties')
        nr_distinct_found_props = len(ack_found_props)
        if nr_distinct_found_props < min_props:
            return 1, f'found too few properties ({nr_distinct_found_props}) for {jp}'
        if max_props < nr_distinct_found_props:
            return 1, f'found too many properties ({nr_distinct_found_props}) for {jp}'

        for what in ('names', 'urls'):
            if what not in ack_found_props:
                continue
            seq = value[what]
            if not isinstance(seq, list):
                return 1, f'optional {jp} property {what} present but no array'
            if not len(seq):
                return 1, f'optional {jp} property {what} present but empty'
            for ndx, text in enumerate(seq):
                jpn = f'{jp}[{ndx}]'
                if not isinstance(text, str):
                    return 1, f'optional {jpn} property {what} entry present but no text'
                if not len(text):
                    return 1, f'optional {jpn} property {what} entry present but empty'
                if what == 'urls':
                    try:
                        _ = URI(text)
                    except InvalidURIError as err:
                        return 1, f'optional {jpn} property {what} entry present but invalid as URI({err})'

        for what in ('organization', 'summary'):
            if what not in ack_found_props:
                continue
            text = value[what]
            if not isinstance(text, str):
                return 1, f'optional {jp} property {what} present but no text'
            if not len(text):
                return 1, f'optional {jp} property {what} present but empty'
    return 0, ''


@no_type_check
def document_aggregate_severity(value):
    """Verify properties of document/aggregate_severity present follow rules."""
    parent, prop = 'document', 'aggregate_severity'
    jp = f'{parent}.{prop}'
    if not isinstance(value, dict):
        return 1, f'optional property {jp} present but no object'
    if not value:
        return 1, f'optional property {jp} present but empty'
    agg_norm_props = ('text',)
    agg_opt_props = ('namespace',)
    agg_known_props = {el for el in chain(agg_norm_props, agg_opt_props)}
    min_props, max_props = 1, len(agg_known_props)
    agg_found_props = {el for el in value}
    if agg_found_props <= agg_known_props:
        log.info(f'set of {jp} properties only contains known properties')
    if agg_found_props < agg_known_props:
        log.info(f'set of {jp} properties is a proper subset of the known properties')
    nr_distinct_found_props = len(agg_found_props)
    if nr_distinct_found_props < min_props:
        return 1, f'found too few properties ({nr_distinct_found_props}) for {jp}'
    if max_props < nr_distinct_found_props:
        return 1, f'found too many properties ({nr_distinct_found_props}) for {jp}'

    sub = 'text'
    jps = f'property {parent}.{prop}.{sub}'
    entry = value.get(sub)
    if entry is None:
        return 1, f'mandatory {jps} not present'
    if not isinstance(entry, str):
        return 1, f'mandatory {jps} present but no text'
    if not entry:
        return 1, f'mandatory {jps} present but empty'

    sub = 'namespace'
    jps = f'optional property {parent}.{prop}.{sub}'
    entry = value.get(sub)
    if entry is None:
        return 0, ''
    if not isinstance(entry, str):
        return 1, f'{jps} present but no text'
    if not entry:
        return 1, f'mandatory {jps} present but empty'
    try:
        _ = URI(entry)
    except InvalidURIError as err:
        return 1, f'{jps} present but invalid as URI({err})'

    return 0, ''


@no_type_check
def document_category(value):
    """Verify value of document/category follow rules."""
    parent, prop = 'document', 'category'
    jp = f'property {parent}.{prop}'
    if not isinstance(value, str):
        return 1, f'{jp} present but no text'
    if not value:
        return 1, f'{jp} present but empty'

    return 0, ''


@no_type_check
def document_csaf_version(value):
    """Verify value of document/csaf_version follow rules."""
    parent, prop = 'document', 'csaf_version'
    jp = f'property {parent}.{prop}'
    if not isinstance(value, str):
        return 1, f'{jp} present but no text'
    if not value:
        return 1, f'{jp} present but empty'
    if value != CSAF_VERSION_STRING:
        return 1, f'{jp} present but ({value}) not matching CSAF version 2.0'

    return 0, ''


@no_type_check
def document_lang(value):
    """Verify value of document/lang follow rules."""
    parent, prop = 'document', 'lang'
    jp = f'property {parent}.{prop}'
    if not isinstance(value, str):
        return 1, f'{jp} present but no text'
    if not value:
        return 1, f'{jp} present but empty'
    if not tag_is_valid(value):
        return 1, f'{jp} present but ({value}) is no valid language tag'

    return 0, ''


@no_type_check
def document_optional(document):
    """Verify optional properties of document if present follow rules."""
    norm_props = ('category', 'csaf_version', 'publisher', 'title', 'tracking')
    opt_props = ('acknowledgments', 'aggregate_severity', 'distribution', 'lang', 'notes', 'references', 'source_lang')
    known_props = {el for el in chain(norm_props, opt_props)}
    opt_map = {el: None for el in opt_props}
    parent = 'document'
    for prop in opt_props:
        value = jmespath.search(f'{prop}', document)
        if value is not None:
            opt_map[prop] = value

    prop = 'acknowledgments'
    if opt_map[prop] is not None:
        error, message = document_optional_acknowledgments(opt_map[prop])
        if error:
            return error, message

    prop = 'aggregate_severity'
    if opt_map[prop] is not None:
        error, message = document_aggregate_severity(opt_map[prop])
        if error:
            return error, message

    found_props = {el for el in document}
    if found_props <= known_props:
        log.info(f'set of {parent} properties only contains known properties')
    if found_props < known_props:
        log.info(f'set of {parent} properties is a proper subset of the known properties')

    return 0, 'NotImplemented'


@no_type_check
def verify_document(document):
    """Root of /document member verifier"""
    parent = 'document'
    for prop in ('category', 'csaf_version', 'publisher', 'title', 'tracking'):
        if not jmespath.search(f'{prop}', document):
            return 1, f'missing {parent} property ({prop})'

    parent = 'document'
    prop = 'category'
    if not jmespath.search(f'{prop}', document).strip():
        log.warning(f'warning - {parent} property {prop} value is space-only')
    error, message = document_category(document[prop])
    if error:
        return error, message

    prop = 'csaf_version'
    csaf_version = jmespath.search(f'{prop}', document)
    error, message = document_csaf_version(csaf_version)
    if error:
        return error, message

    prop = 'lang'
    lang = jmespath.search(f'{prop}', document)
    if lang is not None:
        error, message = document_lang(lang)
        if error:
            return error, message

    # Publisher (publisher) is object requires ('category', 'name', 'namespace')
    parent = 'document.publisher'
    for prop in ('category', 'name', 'namespace'):
        if not jmespath.search(f'publisher.{prop}', document):
            return 1, f'missing {parent} property ({prop})'

    parent = 'document'
    prop = 'title'
    if not jmespath.search(f'{prop}', document).strip():
        log.warning(f'warning - {parent} property {prop} value is space-only')

    # Tracking (tracking) is object requires:
    # ('current_release_date', 'id', 'initial_release_date', 'revision_history', 'status', 'version')
    parent = 'document'
    prop = 'tracking'
    for sub in ('current_release_date', 'id', 'initial_release_date', 'revision_history', 'status', 'version'):
        if jmespath.search(f'{prop}.{sub}', document) is None:
            return 1, f'missing {parent}.{prop} property ({sub})'

    return document_optional(document)


@no_type_check
def level_zero(csaf_doc):
    """Most superficial verification."""
    if not csaf_doc.get('document'):
        return 1, 'missing document property'

    error, message = verify_document(csaf_doc['document'])
    if error:
        return error, message

    return 0, ''


def reader(path: str) -> Iterator[str]:
    """Context wrapper / generator to read the lines."""
    with open(pathlib.Path(path), 'rt', encoding=csaf.ENCODING) as handle:
        for line in handle:
            yield line


def peek(data: str) -> str:
    """Determine trivial format of data."""
    if len(data) < CSAF_MIN_BYTES:
        return 'TOO_SHORT'

    sample = data[:CSAF_MIN_BYTES].strip()
    if sample.startswith('{'):
        warn_size = '_MAYBE_TOO_LARGE' if len(data) > CSAF_WARN_MAX_BYTES else ''
        return f'JSON{warn_size}'
    if sample.startswith('<'):
        return 'XML'
    return 'UNKNOWN'


def verify_request(argv: Optional[List[str]]) -> Tuple[int, str, List[str]]:
    """Fail with grace."""
    if not argv or len(argv) != 3:
        return 2, 'received wrong number of arguments', ['']

    command, inp, config = argv

    if command not in ('verify',):
        return 2, 'received unknown command', ['']

    if inp:
        if not pathlib.Path(str(inp)).is_file():
            return 1, 'source is no file', ['']

    if not config:
        return 2, 'configuration missing', ['']

    config_path = pathlib.Path(str(config))
    if not config_path.is_file():
        return 1, f'config ({config_path}) is no file', ['']
    if not ''.join(config_path.suffixes).lower().endswith('.json'):
        return 1, 'config has no .json extension', ['']

    return 0, '', argv


def verify_json(data: str) -> Tuple[int, str, List[str], Dict[str, object]]:
    """Verify the JSON as CSAF."""
    try:
        doc = msgspec.json.decode(data)
    except msgspec.DecodeError:
        return 1, 'advisory is no valid JSON', [], {}

    error, message = level_zero(doc)
    if error:
        return error, message, [], {}
    return 0, 'OK', [], doc


def is_valid_(path: str, options: Mapping[str, bool]) -> bool:
    """Public API."""
    code, message = process('validate', 'commit', path, options)
    if message:
        log.error(message)
    return bool(code)


@no_type_check
def walk_tree_explicit(base_path):
    """Visit the files in the folders below base path."""
    if base_path.is_file():
        yield base_path
    else:
        for entry in base_path.iterdir():
            if entry.is_dir():
                for file_path in entry.iterdir():
                    yield file_path
            else:
                yield entry


@no_type_check
def visit(tree_or_file_path):
    """Visit tree and yield the leaves."""
    thing = pathlib.Path(tree_or_file_path)
    if thing.is_file():
        yield thing
    else:
        for path in thing.rglob('*'):
            yield path


@no_type_check
def slugify(error):
    """Replace newlines by space."""
    return str(error).replace('\n', '')


def process(command: str, transaction_mode: str, path: str, options: Mapping[str, object]) -> Tuple[int, str]:
    """Drive the verification and validation.
    This function acts as the command line interface backend.
    There is some duplication to support testability.
    """
    # bail_out = options.get('bail_out', False)
    if command != 'validate':
        log.error('Usage: csaf validate ...')
        return 2, 'USAGE'
    if not path.strip():
        log.error('Usage: csaf validate path-to-file')
        return 2, 'USAGE'

    if transaction_mode == 'dry-run':
        log.info('Operating in dry run mode (no changes persisted).')

    data = ''.join(line for line in reader(path))

    guess = peek(data)

    if guess == 'TOO_SHORT':
        return 1, 'advisory is too short to be valid'

    if guess == 'UNKNOWN':
        return 1, 'advisory is of unknown format'

    if guess.startswith('JSON'):
        if guess.endswith('_MAYBE_TOO_LARGE'):
            log.warning('File of %d bytes may be above known file size limits' % len(data))
        error, message, strings, doc = verify_json(data)
        if error:
            log.error(message)
            return error, message
        # Later post process the business rules (spec tests) here
        # Like that:
        if is_valid(doc) is False:  # For now, we return NotImplemented, sorry
            messages = []
            log.error('advisory fails mandatory rules:')
            # Why not execute the rules multiple times (until we have traits in place to report the failing rule)?
            if not is_valid_category(doc):
                messages.append('invalid category')
            if not is_valid_defined_group_ids(doc):
                messages.append('undefined group ids')
            if not is_valid_defined_product_ids(doc):
                messages.append('undefined product ids')
            if not is_valid_translator(doc):
                messages.append('invalid translator')
            if not is_valid_unique_group_ids(doc):
                messages.append('non-unique group ids')
            if not is_valid_unique_product_ids(doc):
                messages.append('non-unique product ids')
            return 1, ', '.join(messages)
        return 0, ''

    return 1, 'XML IS OUT OF SCOPE'
