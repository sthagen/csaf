# Example Use

# Synopsis

No args execution yields usage information:

```console
$ csaf
Usage: csaf [OPTIONS] COMMAND [ARGS]...

  Common Security Advisory Framework (CSAF) Verification and Validation.

Options:
  -V, --version  Display the csaf version and exit
  -h, --help     Show this message and exit.

Commands:
  report    Output the report of the environment for support.
  template  Write a template of a well-formed JSON configuration to...
  validate  Common Security Advisory Framework (CSAF) Verification and...
  version   Display the csaf version and exit.
```

## Validate

Initial test (an empty file is not valid):

```console
$ csaf validate empty.json
2022-03-13T20:40:29.067 ERROR [CSAF]: advisory is too short to be valid
```

Hypothetical valid file:

```
$ csaf vaidate minimal_whatever.json
2022-03-13T20:46:30.618 INFO [CSAF]: set of document properties only contains known properties
2022-03-13T20:46:30.618 INFO [CSAF]: set of document properties is a proper subset of the known properties
```

with `minimal_whatever.json`:

```json
{
  "document": {
    "category": "1",
    "csaf_version": "2.0",
    "publisher": {
      "category": "user",
      "name": "1",
      "namespace": "a:b"
    },
    "title": "1",
    "tracking": {
      "current_release_date": "0001-01-01 00:00:00",
      "id": "1",
      "initial_release_date": "0001-01-01 00:00:00",
      "revision_history": [
        {
          "date": "0001-01-01 00:00:00",
          "number": "1",
          "summary": "1"
        }
      ],
      "status": "final",
      "version": "1"
    }
  }
}
```

### Help

```console
$ csaf validate --help
Usage: csaf validate [OPTIONS] SOURCE...

  Common Security Advisory Framework (CSAF) Verification and Validation.

  You can set some options per environment variables:

  * CSAF_USER='remote-user'
  * CSAF_TOKEN='remote-secret'
  * CSAF_BASE_URL='https://csaf.example.com/file/names/below/here/'
  * CSAF_BAIL_OUT='AnythingTruthy'
  * CSAF_DEBUG='AnythingTruthy'
  * CSAF_VERBOSE='AnythingTruthy'
  * CSAF_STRICT='AnythingTruthy'

  The quiet option (if given) disables any conflicting verbosity setting.

Arguments:
  SOURCE...  [required]

Options:
  -i, --input <sourcepath>   Path to CSAF input file
  -c, --config <configpath>  Path to config file (default is $HOME/.csaf.json)
  -b, --bail-out             Bail out (exit) on first failure (default is
                             False)
  -n, --dry-run              Dry run (default is False)
  -v, --verbose              Verbose output (default is False)
  -q, --quiet                Minimal output (default is False)
  -s, --strict               Ouput noisy warnings on console (default is
                             False)
  -h, --help                 Show this message and exit.
```

## Template

```console
$ csaf template
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
```

### Help

```console
# csaf template --help
Usage: csaf template [OPTIONS]

  Write a template of a well-formed JSON configuration to standard out and
  exit

  The strategy for looking up configurations is to start at the current
  working directory trying to read a file with the name `.csaf.json` else try
  to read same named file in the user folder (home).

  In case an explicit path is given to the config option of commands that
  offer it, only that path is considered.

Options:
  -h, --help  Show this message and exit.
```


## Report

```console
$ csaf report

--------------------------------------------------------------------------------
  Date: Sun Mar 13 20:49:51 2022 CET

                OS : Darwin
            CPU(s) : 8
           Machine : arm64
      Architecture : 64bit
       Environment : Python

  Python 3.10.2 (main, Jan 29 2022, 17:30:41) [Clang 13.0.0
  (clang-1300.0.29.30)]

              csaf : 2022.3.12+parent.9f9d5c6c
          jmespath : 0.10.0
         langcodes : 3.3.0
          lazr.uri : 1.0.6
            orjson : 3.6.7
          pydantic : 1.9.0
            scooby : 0.5.12
             typer : 0.4.0
--------------------------------------------------------------------------------
```

### Help

```console
$ csaf report -h
Usage: csaf report [OPTIONS]

  Output the report of the environment for support.

Options:
  -h, --help  Show this message and exit.
```

## Version

```console
$ csaf version
Common Security Advisory Framework (CSAF) Verification and Validation. version 2022.3.12+parent.6025942a
```

### Help

```console
$ csaf version --help
Usage: csaf version [OPTIONS]

  Display the csaf version and exit.

Options:
  -h, --help  Show this message and exit.
```
