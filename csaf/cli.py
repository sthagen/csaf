"""Commandline API gateway for csaf."""
import sys
from typing import List, Mapping

import typer

import csaf
import csaf.config as cfg
import csaf.csaf as lint
import csaf.env as env
from csaf import log

app = typer.Typer(
    add_completion=False,
    context_settings={'help_option_names': ['-h', '--help']},
    no_args_is_help=True,
)


@app.callback(invoke_without_command=True)
def callback(
    version: bool = typer.Option(
        False,
        '-V',
        '--version',
        help='Display the csaf version and exit',
        is_eager=True,
    )
) -> None:
    """
    Common Security Advisory Framework (CSAF) Verification and Validation.
    """
    if version:
        typer.echo(f'{csaf.APP_NAME} version {csaf.__version__}')
        raise typer.Exit()


@app.command('template')
def app_template() -> int:
    """
    Write a template of a well-formed JSON configuration to standard out and exit

    The strategy for looking up configurations is to start at the current working
    directory trying to read a file with the name `.csaf.json` else try to read
    same named file in the user folder (home).

    In case an explicit path is given to the config option of commands that offer
    it, only that path is considered.
    """
    sys.stdout.write(cfg.generate_template())
    return sys.exit(0)


@app.command('report')
def report() -> int:
    """Output the report of the environment for support."""
    sys.stdout.write(env.report())
    return sys.exit(0)


@app.command('validate')
def validate(
    source: List[str],
    inp: str = typer.Option(
        '',
        '-i',
        '--input',
        help='Path to CSAF input file',
        metavar='<sourcepath>',
    ),
    conf: str = typer.Option(
        '',
        '-c',
        '--config',
        help=f'Path to config file (default is $HOME/{csaf.DEFAULT_CONFIG_NAME})',
        metavar='<configpath>',
    ),
    bail_out: bool = typer.Option(
        False,
        '-b',
        '--bail-out',
        help='Bail out (exit) on first failure (default is False)',
    ),
    verify: bool = typer.Option(
        False,
        '-n',
        '--dry-run',
        help='Dry run (default is False)',
    ),
    verbose: bool = typer.Option(
        False,
        '-v',
        '--verbose',
        help='Verbose output (default is False)',
    ),
    quiet: bool = typer.Option(
        False,
        '-q',
        '--quiet',
        help='Minimal output (default is False)',
    ),
    strict: bool = typer.Option(
        False,
        '-s',
        '--strict',
        help='Ouput noisy warnings on console (default is False)',
    ),
) -> int:
    """
    Common Security Advisory Framework (CSAF) Verification and Validation.

    You can set some options per environment variables:

    \b
    * CSAF_USER='remote-user'
    * CSAF_TOKEN='remote-secret'
    * CSAF_BASE_URL='https://csaf.example.com/file/names/below/here/'
    * CSAF_BAIL_OUT='AnythingTruthy'
    * CSAF_DEBUG='AnythingTruthy'
    * CSAF_VERBOSE='AnythingTruthy'
    * CSAF_STRICT='AnythingTruthy'

    The quiet option (if given) disables any conflicting verbosity setting.
    """
    command = 'validate'
    transaction_mode = 'commit' if not verify else 'dry-run'
    if quiet:
        csaf.QUIET = True
        csaf.DEBUG = False
        csaf.VERBOSE = False
    elif verbose:
        csaf.VERBOSE = True

    if strict:
        csaf.STRICT = True

    if bail_out:
        csaf.BAIL_OUT = True

    if transaction_mode == 'dry-run':
        csaf.DRY_RUN = True

    configuration = cfg.read_configuration(str(conf)) if conf else {}

    options: Mapping[str, object] = {
        'configuration': configuration,
        'bail_out': bail_out,
        'quiet': quiet,
        'strict': strict,
        'verbose': verbose,
    }

    paths = (inp,) if inp else tuple(source)
    code, message = lint.process(command, transaction_mode, paths[0], options)
    if message:
        log.error(message)
    return code


@app.command('version')
def app_version() -> None:
    """
    Display the csaf version and exit.
    """
    callback(True)
