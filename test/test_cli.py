import pytest  # type: ignore

import csaf.cli as cli


def test_main_no_args(capsys):
    assert cli.validate(source=[''], inp='', conf='') == 2
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_main_bad_arg(capsys):
    message = r"\[Errno 2\] No such file or directory: 'non-existing-thing'"
    with pytest.raises(FileNotFoundError, match=message):
        cli.validate(source=['non-existing-thing'], inp='', conf='', bail_out=True)
    out, err = capsys.readouterr()
    assert not out
    assert not err
