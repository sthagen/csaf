"""Calculate (Finnish: laskea) some parts."""
import os

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

DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
DRY_RUN = bool(os.getenv(f'{APP_ENV}_DRY_RUN', ''))
QUIET = bool(os.getenv(f'{APP_ENV}_QUIET', ''))
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))

# [[[fill git_describe()]]]
__version__ = '2022.3.12+parent.838249fb'
# [[[end]]]
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__ = []
