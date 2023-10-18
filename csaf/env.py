"""Report environment to support resolution of user issues."""
from typing import List, no_type_check

import pkg_resources
import scooby


@no_type_check
def report() -> str:
    """Return either text options for the user to report her env or the report of the environment for support."""
    import langcodes  # noqa

    packages = pkg_resources.working_set  # noqa
    monkey_lc = [p.version for p in packages if p.project_name == 'langcodes'][0]  # noqa
    langcodes.__version__ = monkey_lc

    class Report(scooby.Report):
        def __init__(self, additional=None, ncol=3, text_width=80, sort=False):
            """Initiate a scooby.Report instance."""

            # Mandatory packages.
            core = [
                'csaf',
                'jmespath',
                'langcodes',
                'lazr.uri',
                'msgspec',
                'pydantic',
                'scooby',
                'setuptools',
                'typer',
            ]

            # Optional packages.
            optional: List[str] = []

            scooby.Report.__init__(
                self, additional=additional, core=core, optional=optional, ncol=ncol, text_width=text_width, sort=sort
            )

    return str(Report()) + '\n'
