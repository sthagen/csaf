"""Common Security Advisory Framework (CSAF) Verification and Validation."""
import logging
import os
import pathlib
from typing import no_type_check

APP_BLURB = (
    'Common Security Advisory Framework (CSAF) Verification, Validation, and Application Programming Interface (API).'
)

APP_ALIAS = str(pathlib.Path(__file__).parent.name)
APP_ENV = APP_ALIAS.upper()
APP_NAME = locals()['__doc__']
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = f'.{APP_ALIAS}.json'

FAKE_SECRET = '*' * 13

BAIL_OUT = bool(os.getenv(f'{APP_ENV}_BAIL_OUT', ''))
DRY_RUN = bool(os.getenv(f'{APP_ENV}_DRY_RUN', ''))
QUIET = bool(os.getenv(f'{APP_ENV}_QUIET', ''))

log = logging.getLogger()  # Temporary refactoring: module level logger
LOG_FOLDER = pathlib.Path('logs')
LOG_FILE = f'{APP_ALIAS}.log'
LOG_PATH = pathlib.Path(LOG_FOLDER, LOG_FILE) if LOG_FOLDER.is_dir() else pathlib.Path(LOG_FILE)
LOG_LEVEL = logging.INFO


@no_type_check
def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global log  # pylint: disable=global-statement

    log_format = {
        'format': '%(asctime)s.%(msecs)03d %(levelname)s [%(name)s]: %(message)s',
        'datefmt': '%Y-%m-%dT%H:%M:%S',
        # 'filename': LOG_PATH,
        'level': LOG_LEVEL if level is None else level,
    }
    logging.basicConfig(**log_format)
    log = logging.getLogger(APP_ENV if name is None else name)
    log.propagate = True


init_logger(name=APP_ENV, level=logging.DEBUG if DEBUG else None)

from csaf.csaf import is_valid  # noqa

# [[[fill git_describe()]]]
__version__ = '2023.11.27+parent.g543c3eb3'
# [[[end]]] (checksum: 5069bde68b3f316ade142397bf03880b)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__ = ['is_valid', 'log']
