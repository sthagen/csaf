#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Easing the CSAF way."""
import pathlib
import sys

import csaf
import csaf.csaf as lint


# pylint: disable=expression-not-assigned
def main(argv=None, abort=None, debug=None):
    """Dispatch processing of the job.
    This is the strings only command line interface.
    For python API use interact with lint functions directly.
    """
    argv = sys.argv[1:] if argv is None else argv
    debug = debug if debug else csaf.DEBUG
    abort = abort if abort else csaf.ABORT
    unique_trees = {arg: None for arg in argv}
    for tree_or_leaf in unique_trees:
        if not pathlib.Path(tree_or_leaf).is_file() and not pathlib.Path(tree_or_leaf).is_dir():
            print('ERROR: For now only existing paths accepted.')
            sys.exit(2)

    code, _ = lint.process(unique_trees, abort=abort, debug=debug)
    return code
