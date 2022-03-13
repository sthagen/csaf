# -*- coding: utf-8 -*-
# pylint: disable=c-extension-no-member,expression-not-assigned,line-too-long,logging-fstring-interpolation
"""CSAF Document model."""
from __future__ import annotations

import json
import pathlib
from typing import Annotated, List, Mapping, Optional, Sequence, Tuple, no_type_check

from pydantic import BaseModel, Field, validator

import csaf
from csaf import log
from csaf.document import Document
from csaf.product import ProductTree
from csaf.vulnerability import Vulnerability


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
    def check_len(cls, v):
        if not v:
            raise ValueError('vulnerabilities present but empty')
        return v


def is_valid(path: str, options: Mapping[str, bool]) -> bool:
    """Public API."""
    code, message = process('validate', 'commit', [path], options)
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


def process(command: str, transaction_mode: str, paths: Sequence[str], options: Mapping[str, bool]) -> Tuple[int, str]:
    """Drive the verification and validation.
    This function acts as the command line interface backend.
    There is some duplication to support testability.
    """
    bail_out = options.get('bail_out', False)
    if command != 'validate':
        log.error('Usage: csaf validate ...')
        return 2, 'USAGE'
    forest = paths
    if not forest:
        log.error('Usage: csaf validate paths-to-files')
        return 2, 'USAGE'

    if transaction_mode == 'dry-run':
        log.info('Operating in dry run mode (no changes persisted).')

    num_trees = len(forest)
    log.debug('Guarded dispatch forest=%s, num_trees=%d', forest, num_trees)

    log.info('Starting validation visiting a forest with %d tree%s', num_trees, '' if num_trees == 1 else 's')
    failure_path_reason = 'Failed validation for path %s with error: %s'
    total, folders, ignored, jsons = 0, 0, 0, 0
    failures = 0
    for tree in forest:
        for path in visit(tree):
            log.debug(' - path=%s, total=%d', path, total)
            total += 1
            if not path.is_file():
                folders += 1
                continue

            final_suffix = '' if not path.suffixes else path.suffixes[-1].lower()

            if final_suffix.lower() == '.json':
                loader = json.load
                with open(path, 'rt', encoding=csaf.ENCODING) as handle:
                    try:
                        _ = loader(handle)
                        jsons += 1
                    except Exception as err:
                        log.error(failure_path_reason, path, slugify(err))
                        if bail_out:
                            return 1, str(err)
                        failures += 1
            else:
                ignored += 1
                continue

    success = 'Successfully validated'
    pairs = ((jsons, 'JSON'),)
    for count, kind in pairs:
        if count:
            log.info('- %s %d total %s file%s.', success, count, kind, '' if count == 1 else 's')

    configs = jsons
    log.info(  # TODO remove f-strings also here
        f'Finished validation of {configs} configuration file{"" if configs == 1 else "s"}'
        f' with {failures} failure{"" if failures == 1 else "s"}'
        f' visiting {total} path{"" if total == 1 else "s"}'
        f' (ignored {ignored} non-config file{"" if ignored == 1 else "s"}'
        f' in {folders} folder{"" if folders == 1 else "s"})'
    )
    print(f'{"OK" if not failures else "FAIL"}')

    return 0, ''
