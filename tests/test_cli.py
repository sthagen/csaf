# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest  # type: ignore

import csaf.cli as cli


def test_main_no_args(capsys):
    with pytest.raises(TypeError, match='expected str, bytes or os.PathLike object, not OptionInfo'):
        cli.validate([''])
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_bad_arg(capsys):
    with pytest.raises(SystemExit, match='0'):
        cli.validate(source=['non-existing-thing'], inp='', bail_out=True)
    out, err = capsys.readouterr()
    assert out.strip() == 'OK'
    assert not err
