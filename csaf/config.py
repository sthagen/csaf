"""Configuration API for csaf."""
import pathlib
from typing import Any, Mapping, Union

import msgspec

TEMPLATE_EXAMPLE = """\
{
  "remote": {
    "user": "",
    "token": "",
    "base_url": ""
  },
  "local": {
    "bail_out": false,
    "quiet": false,
    "verbose": false,
    "strict": false
  }
}
"""


def generate_template() -> str:
    """Return template of a well-formed JSON configuration."""
    return TEMPLATE_EXAMPLE


def read_configuration(path: Union[pathlib.Path, str]) -> Union[Any, Mapping[str, object]]:
    """LaterAlligator."""
    with open(str(path), 'rb') as handle:
        return msgspec.json.decode(handle.read())
