# Example Use

No args execution yields usage information:
```
$ csaf
Usage: csaf paths-to-files
```

Initial test (an empty file is not valid):
```
$ csaf empty.json
FAIL
```

Hypothetical valid file:
```
$ csaf minimal_csaf-document.json
OK
```
