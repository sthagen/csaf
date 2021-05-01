# Example Use

No args execution yields usage information:
```
$ python -m csaf
Usage: gelee paths-to-files
```

Initial test wmpty file is not valid:
```
$ python -m csaf tests/fixtures/empty.json
2021-05-01T23:19:44.409 INFO [csaf]: Starting validation visiting a forest with 1 tree
2021-05-01T23:19:44.412 ERROR [csaf]: Failed validation for path tests/fixtures/empty.json with error: Expecting value: line 2 column 1 (char 1)
2021-05-01T23:19:44.412 INFO [csaf]: Finished validation of 0 configuration files with 1 failure visiting 1 path (ignored 0 non-config files in 0 folders)
FAIL
```

Empty object valid for now (no schema validation yet):
```
$ python -m csaf tests/fixtures/empty_object.json
2021-05-01T23:19:53.250 INFO [csaf]: Starting validation visiting a forest with 1 tree
2021-05-01T23:19:53.252 INFO [csaf]: - Successfully validated 1 total JSON file.
2021-05-01T23:19:53.253 INFO [csaf]: Finished validation of 1 configuration file with 0 failures visiting 1 path (ignored 0 non-config files in 0 folders)
OK
```
