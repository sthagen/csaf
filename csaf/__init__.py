"""Calculate (Finnish: laskea) some parts."""
import logging
import os
import pathlib
from typing import no_type_check

APP_ALIAS = 'csaf'
APP_BLURB = (
    'Common Security Advisory Framework (CSAF) Verification, Validation, and Application Programming Interface (API).'
)
APP_ENV = 'CSAF'
APP_NAME = 'Common Security Advisory Framework (CSAF) Verification and Validation.'
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
FAKE_SECRET = '*' * 13

DEFAULT_CONFIG_NAME = f'.{APP_ALIAS}.json'

BAIL_OUT = bool(os.getenv(f'{APP_ENV}_BAIL_OUT', ''))
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
DRY_RUN = bool(os.getenv(f'{APP_ENV}_DRY_RUN', ''))
QUIET = bool(os.getenv(f'{APP_ENV}_QUIET', ''))
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))

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
__version__ = '2023.5.8+parent.aa36605a'
# [[[end]]] (checksum: 99e36df585743bf57b7cbd29fd80ca8c)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__ = ['is_valid', 'log']
