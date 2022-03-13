"""Configuration API for csaf."""

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
