# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/csaf/blob/default/sbom.json) with SHA256 checksum ([1fd323e4 ...](https://raw.githubusercontent.com/sthagen/csaf/default/sbom.json.sha256 "sha256:1fd323e42d2374b70079ac183cec911611730c0b714ba98d9635d6eec0bbce43")).
<!--[[[end]]] (checksum: 719054b5a9a757ec5ff6175b62da5556)-->
## Licenses

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                 | Version                                               | License                                             | Author                             | Description (from packaging data)                                              |
|:-----------------------------------------------------|:------------------------------------------------------|:----------------------------------------------------|:-----------------------------------|:-------------------------------------------------------------------------------|
| [jmespath](https://github.com/jmespath/jmespath.py)  | [1.0.1](https://pypi.org/project/jmespath/1.0.1/)     | MIT License                                         | James Saryerwinnie                 | JSON Matching Expressions                                                      |
| [langcodes](https://github.com/rspeer/langcodes)     | [3.3.0](https://pypi.org/project/langcodes/3.3.0/)    | MIT License                                         | Elia Robyn Speer                   | Tools for labeling human languages with IETF language tags                     |
| [lazr.uri](https://launchpad.net/lazr.uri)           | [1.0.6](https://pypi.org/project/lazr.uri/1.0.6/)     | GNU Library or Lesser General Public License (LGPL) | "LAZR Developers" team             | A self-contained, easily reusable library for parsing, manipulating,           |
| [orjson](https://github.com/ijl/orjson)              | [3.7.12](https://pypi.org/project/orjson/3.7.12/)     | Apache Software License; MIT License                | ijl <ijl@mailbox.org>              | Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy |
| [pydantic](https://github.com/samuelcolvin/pydantic) | [1.9.2](https://pypi.org/project/pydantic/1.9.2/)     | MIT License                                         | Samuel Colvin                      | Data validation and settings management using python type hints                |
| [scooby](https://github.com/banesullivan/scooby)     | [0.6.0](https://pypi.org/project/scooby/0.6.0/)       | MIT License                                         | Dieter Werthmüller & Bane Sullivan | A Great Dane turned Python environment detective                               |
| [setuptools](https://github.com/pypa/setuptools)     | [65.3.0](https://pypi.org/project/setuptools/65.3.0/) | MIT License                                         | Python Packaging Authority         | Easily download, build, install, upgrade, and uninstall Python packages        |
| [typer](https://github.com/tiangolo/typer)           | [0.6.1](https://pypi.org/project/typer/0.6.1/)        | MIT License                                         | Sebastián Ramírez                  | Typer, build great CLIs. Easy to code. Based on Python type hints.             |
| jsonschema                                           | [4.8.0](https://pypi.org/project/jsonschema/4.8.0/)   | MIT License                                         | Julian Berman                      | An implementation of JSON Schema validation for Python                         |
<!--[[[end]]] (checksum: cb078bb0b9899d308d79a1286597cf23)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                                           | Version                                                    | License                            | Author                 | Description (from packaging data)                      |
|:-----------------------------------------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:-----------------------|:-------------------------------------------------------|
| [attrs](https://www.attrs.org/)                                                                | [21.4.0](https://pypi.org/project/attrs/21.4.0/)           | MIT License                        | Hynek Schlawack        | Classes Without Boilerplate                            |
| [click](https://palletsprojects.com/p/click/)                                                  | [8.1.3](https://pypi.org/project/click/8.1.3/)             | BSD License                        | Armin Ronacher         | Composable command line interface toolkit              |
| [pyrsistent](http://github.com/tobgu/pyrsistent/)                                              | [0.18.1](https://pypi.org/project/pyrsistent/0.18.1/)      | MIT License                        | Tobias Gustafsson      | Persistent/Functional/Immutable data structures        |
| [typing-extensions](https://github.com/python/typing/blob/master/typing_extensions/README.rst) | [4.2.0](https://pypi.org/project/typing-extensions/4.2.0/) | Python Software Foundation License | The Python Typing Team | Backported and Experimental Type Hints for Python 3.7+ |
<!--[[[end]]] (checksum: 6460b02c3b27fd57c91461595a31a576)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
jmespath==1.0.1
jsonschema==4.8.0
  - attrs [required: >=17.4.0, installed: 21.4.0]
  - pyrsistent [required: >=0.14.0,!=0.17.2,!=0.17.1,!=0.17.0, installed: 0.18.1]
langcodes==3.3.0
lazr.uri==1.0.6
  - setuptools [required: Any, installed: 65.3.0]
orjson==3.7.12
pydantic==1.9.2
  - typing-extensions [required: >=3.7.4.3, installed: 4.2.0]
scooby==0.6.0
typer==0.6.1
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 4f630786fb6385f44c3296a2336836cb)-->
