# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/csaf/blob/default/sbom.json) with SHA256 checksum ([72bd88a4 ...](https://git.sr.ht/~sthagen/csaf/blob/default/sbom.json.sha256 "sha256:72bd88a48b4b6536204fa0258b0538d9ef7cd41c22921861626c67207be99ab0")).
<!--[[[end]]] (checksum: f2ac04c28a346c02df14a75b6209ce5c)-->
## Licenses

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                          | Version                                               | License                                             | Author                                                              | Description (from packaging data)                                                                        |
|:--------------------------------------------------------------|:------------------------------------------------------|:----------------------------------------------------|:--------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| [jmespath](https://github.com/jmespath/jmespath.py)           | [1.0.1](https://pypi.org/project/jmespath/1.0.1/)     | MIT License                                         | James Saryerwinnie                                                  | JSON Matching Expressions                                                                                |
| [jsonschema](https://github.com/python-jsonschema/jsonschema) | [4.17.3](https://pypi.org/project/jsonschema/4.17.3/) | MIT License                                         | Julian Berman                                                       | An implementation of JSON Schema validation for Python                                                   |
| [langcodes](https://github.com/rspeer/langcodes)              | [3.3.0](https://pypi.org/project/langcodes/3.3.0/)    | MIT License                                         | Elia Robyn Speer                                                    | Tools for labeling human languages with IETF language tags                                               |
| [lazr.uri](https://launchpad.net/lazr.uri)                    | [1.0.6](https://pypi.org/project/lazr.uri/1.0.6/)     | GNU Library or Lesser General Public License (LGPL) | "LAZR Developers" team                                              | A self-contained, easily reusable library for parsing, manipulating,                                     |
| [msgspec](https://jcristharif.com/msgspec/)                   | [0.14.2](https://pypi.org/project/msgspec/0.14.2/)    | BSD License                                         | Jim Crist-Harif                                                     | A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML. |
| [pydantic](https://github.com/pydantic/pydantic)              | [1.10.7](https://pypi.org/project/pydantic/1.10.7/)   | MIT License                                         | Samuel Colvin                                                       | Data validation and settings management using python type hints                                          |
| [scooby](https://github.com/banesullivan/scooby)              | [0.7.2](https://pypi.org/project/scooby/0.7.2/)       | MIT License                                         | Dieter Werthmüller, Bane Sullivan, Alex Kaszynski, and contributors | A Great Dane turned Python environment detective                                                         |
| [setuptools](https://github.com/pypa/setuptools)              | [67.7.2](https://pypi.org/project/setuptools/67.7.2/) | MIT License                                         | Python Packaging Authority                                          | Easily download, build, install, upgrade, and uninstall Python packages                                  |
| [typer](https://github.com/tiangolo/typer)                    | [0.9.0](https://pypi.org/project/typer/0.9.0/)        | MIT License                                         | Sebastián Ramírez                                                   | Typer, build great CLIs. Easy to code. Based on Python type hints.                                       |
<!--[[[end]]] (checksum: 56da3a41b30b3fb2ec8534b13ddf57b4)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                    | Version                                                    | License                            | Author                                                                                | Description (from packaging data)                      |
|:------------------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------|
| [attrs](https://www.attrs.org/en/stable/changelog.html)                 | [23.1.0](https://pypi.org/project/attrs/23.1.0/)           | MIT License                        | Hynek Schlawack <hs@ox.cx>                                                            | Classes Without Boilerplate                            |
| [click](https://palletsprojects.com/p/click/)                           | [8.1.3](https://pypi.org/project/click/8.1.3/)             | BSD License                        | Armin Ronacher                                                                        | Composable command line interface toolkit              |
| [pyrsistent](https://github.com/tobgu/pyrsistent/)                      | [0.19.2](https://pypi.org/project/pyrsistent/0.19.2/)      | MIT License                        | Tobias Gustafsson                                                                     | Persistent/Functional/Immutable data structures        |
| [typing_extensions](https://github.com/python/typing_extensions/issues) | [4.4.0](https://pypi.org/project/typing_extensions/4.4.0/) | Python Software Foundation License | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+ |
<!--[[[end]]] (checksum: e580a31c95c9810aced74d78f6cc6ced)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
jmespath==1.0.1
jsonschema==4.17.3
  - attrs [required: >=17.4.0, installed: 23.1.0]
  - pyrsistent [required: >=0.14.0,!=0.17.2,!=0.17.1,!=0.17.0, installed: 0.19.2]
langcodes==3.3.0
lazr.uri==1.0.6
  - setuptools [required: Any, installed: 67.7.2]
msgspec==0.14.2
pydantic==1.10.7
  - typing-extensions [required: >=4.2.0, installed: 4.4.0]
scooby==0.7.2
typer==0.9.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
  - typing-extensions [required: >=3.7.4.3, installed: 4.4.0]
````
<!--[[[end]]] (checksum: 1b34141a2e671506a32627e72fa1b707)-->
