"""Report environment to support resolution of user issues."""
from typing import List, no_type_check

import scooby  # type: ignore


@no_type_check
def report() -> str:
    """Return either text options for the user to report her env or the report of the environment for support."""

    class Report(scooby.Report):  # type: ignore
        def __init__(self, additional=None, ncol=3, text_width=80, sort=False):
            """Initiate a scooby.Report instance."""

            # Mandatory packages.
            core = [
                'csaf',
                'jmespath',
                'pydantic',
                'scooby',
                'typer',
            ]

            # Optional packages.
            optional: List[str] = []

            scooby.Report.__init__(
                self, additional=additional, core=core, optional=optional, ncol=ncol, text_width=text_width, sort=sort
            )

    return str(Report()) + '\n'
