# -*- coding: utf-8 -*-
# pylint: disable=c-extension-no-member,expression-not-assigned,line-too-long,logging-fstring-interpolation
"""Do the lint."""
import json
import logging
import pathlib
import sys

# import jmespath
# import jsonschema  # type: ignore

import csaf

LOG = logging.getLogger()  # Temporary refactoring: module level logger
LOG_FOLDER = pathlib.Path('logs')
LOG_FILE = f'{csaf.APP_ALIAS}.log'
LOG_PATH = pathlib.Path(LOG_FOLDER, LOG_FILE) if LOG_FOLDER.is_dir() else pathlib.Path(LOG_FILE)
LOG_LEVEL = logging.INFO


def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global LOG  # pylint: disable=global-statement

    log_format = {
        'format': '%(asctime)s.%(msecs)03d %(levelname)s [%(name)s]: %(message)s',
        'datefmt': '%Y-%m-%dT%H:%M:%S',
        # 'filename': LOG_PATH,
        'level': LOG_LEVEL if level is None else level
    }
    logging.basicConfig(**log_format)
    LOG = logging.getLogger(csaf.APP_ENV if name is None else name)
    LOG.propagate = True


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


def visit(tree_or_file_path):
    """Visit tree and yield the leaves."""
    thing = pathlib.Path(tree_or_file_path)
    if thing.is_file():
        yield thing
    else:
        for path in thing.rglob('*'):
            yield path


def slugify(error):
    """Replace newlines by space."""
    return str(error).replace('\n', '')


def process(argv=None, abort=False, debug=None):
    """Drive the verification and validation.
    This function acts as the command line interface backend.
    There is some duplication to support testability.
    """
    init_logger(level=logging.DEBUG if debug else None)
    forest = argv if argv else sys.argv[1:]
    if not forest:
        print('Usage: csaf paths-to-files')
        return 0, 'USAGE'
    num_trees = len(forest)
    LOG.debug('Guarded dispatch forest=%s, num_trees=%d', forest, num_trees)

    LOG.info('Starting validation visiting a forest with %d tree%s',
             num_trees, '' if num_trees == 1 else 's')
    failure_path_reason = 'Failed validation for path %s with error: %s'
    total, folders, ignored, jsons = 0, 0, 0, 0
    failures = 0
    for tree in forest:
        for path in visit(tree):
            LOG.debug(' - path=%s, total=%d', path, total)
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
                        LOG.error(failure_path_reason, path, slugify(err))
                        if abort:
                            return 1, str(err)
                        failures += 1
            else:
                ignored += 1
                continue

    success = 'Successfully validated'
    pairs = (
        (jsons, 'JSON'),
    )
    for count, kind in pairs:
        if count:
            LOG.info(
                '- %s %d total %s file%s.', success, count, kind, '' if count == 1 else 's')

    configs = jsons
    LOG.info(  # TODO remove f-strings also here
        f'Finished validation of {configs} configuration file{"" if configs == 1 else "s"}'
        f' with {failures} failure{"" if failures == 1 else "s"}'
        f' visiting {total} path{"" if total == 1 else "s"}'
        f' (ignored {ignored} non-config file{"" if ignored == 1 else "s"}'
        f' in {folders} folder{"" if folders == 1 else "s"})'
    )
    print(f'{"OK" if not failures else "FAIL"}')

    return 0, ''
