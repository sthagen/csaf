# Change History

2023.10.18
:    * Completed migration to pydantic v2 (<https://todo.sr.ht/~sthagen/csaf/5>)

2023.6.18
:    * Fixed validation failures for CVSS of upstream BSI example (<https://todo.sr.ht/~sthagen/csaf/4>)
* Moved SBOM noise into folder and added SPDX SBOM (derived) in multiple file formats

2023.5.9
:    * Fixed top level aggregator to consume and produce camelCase CVSS keys.

2923.5.8
:    * Fixed CVSS camelCase keyword propagation as mix-ins of score and vulnerability
  objects (https://todo.sr.ht/~sthagen/csaf/2#event-237257)

2023.5.6
:    * Added contributors section to documentation
* Fixed product_id should be a string (<https://todo.sr.ht/~sthagen/csaf/3>)
* Fixed the CVSS Keywords in Generated CSAF Documents (<https://todo.sr.ht/~sthagen/csaf/2>)
* Migrated from orjson to msgspec

## 2022

2022.3.20
:    * Added warning for CSAF files with more than 15 Megabytes

2022.3.13
:    * Added setuptools information to environment report

2022.3.12
:    * First partial implementation with command line api
* Added report of environment facts command to support bug reports (new dependency scooby)
* Added baseline, third-party information, and SBOM

## 2021

0.0.1 (2021-05-01)
:    * Initial release on PyPI


