# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/csaf/blob/default/sbom.json) with SHA256 checksum ([45b8c3d4 ...](https://raw.githubusercontent.com/sthagen/csaf/default/sbom.json.sha256 "sha256:45b8c3d4afa8d4a10161768046f3ed1f60f959d38ba2193378c44c4214724f61")).
<!--[[[end]]] (checksum: 7953f588b89637fe37151959680c80d0)-->
## Licenses

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                 | Version                                             | License                                             | Author                             | Description (from packaging data)                                              |
|:-----------------------------------------------------|:----------------------------------------------------|:----------------------------------------------------|:-----------------------------------|:-------------------------------------------------------------------------------|
| [jmespath](https://github.com/jmespath/jmespath.py)  | [0.10.0](https://pypi.org/project/jmespath/0.10.0/) | MIT License                                         | James Saryerwinnie                 | JSON Matching Expressions                                                      |
| [jsonschema](https://github.com/Julian/jsonschema)   | [4.4.0](https://pypi.org/project/jsonschema/4.4.0/) | MIT License                                         | Julian Berman                      | An implementation of JSON Schema validation for Python                         |
| [langcodes](https://github.com/rspeer/langcodes)     | [3.3.0](https://pypi.org/project/langcodes/3.3.0/)  | MIT License                                         | Elia Robyn Speer                   | Tools for labeling human languages with IETF language tags                     |
| [lazr.uri](https://launchpad.net/lazr.uri)           | [1.0.6](https://pypi.org/project/lazr.uri/1.0.6/)   | GNU Library or Lesser General Public License (LGPL) | "LAZR Developers" team             | A self-contained, easily reusable library for parsing, manipulating,           |
| [orjson](https://github.com/ijl/orjson)              | [3.6.7](https://pypi.org/project/orjson/3.6.7/)     | Apache Software License; MIT License                | ijl <ijl@mailbox.org>              | Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy |
| [pydantic](https://github.com/samuelcolvin/pydantic) | [1.9.0](https://pypi.org/project/pydantic/1.9.0/)   | MIT License                                         | Samuel Colvin                      | Data validation and settings management using python 3.6 type hinting          |
| [scooby](https://github.com/banesullivan/scooby)     | [0.5.12](https://pypi.org/project/scooby/0.5.12/)   | MIT License                                         | Dieter Werthmüller & Bane Sullivan | A Great Dane turned Python environment detective                               |
| [typer](https://github.com/tiangolo/typer)           | [0.4.0](https://pypi.org/project/typer/0.4.0/)      | MIT License                                         | Sebastián Ramírez                  | Typer, build great CLIs. Easy to code. Based on Python type hints.             |
<!--[[[end]]] (checksum: ec8c3a705597e8a6d1d2ce4059ae6d0e)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                                           | Version                                                    | License                            | Author                     | Description (from packaging data)                                       |
|:-----------------------------------------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:---------------------------|:------------------------------------------------------------------------|
| [attrs](https://www.attrs.org/)                                                                | [21.4.0](https://pypi.org/project/attrs/21.4.0/)           | MIT License                        | Hynek Schlawack            | Classes Without Boilerplate                                             |
| [click](https://palletsprojects.com/p/click/)                                                  | [8.0.4](https://pypi.org/project/click/8.0.4/)             | BSD License                        | Armin Ronacher             | Composable command line interface toolkit                               |
| [pyrsistent](http://github.com/tobgu/pyrsistent/)                                              | [0.18.1](https://pypi.org/project/pyrsistent/0.18.1/)      | MIT License                        | Tobias Gustafsson          | Persistent/Functional/Immutable data structures                         |
| [setuptools](https://github.com/pypa/setuptools)                                               | [60.9.3](https://pypi.org/project/setuptools/60.9.3/)      | MIT License                        | Python Packaging Authority | Easily download, build, install, upgrade, and uninstall Python packages |
| [typing-extensions](https://github.com/python/typing/blob/master/typing_extensions/README.rst) | [4.1.1](https://pypi.org/project/typing-extensions/4.1.1/) | Python Software Foundation License | The Python Typing Team     | Backported and Experimental Type Hints for Python 3.6+                  |
 <!--[[[end]]] (checksum: df40192e701bab2010820fb73f5adc8f)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="https://raw.githubusercontent.com/sthagen/csaf/default/docs/third-party/package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
jmespath==0.10.0
jsonschema==4.4.0
  - attrs [required: >=17.4.0, installed: 21.4.0]
  - pyrsistent [required: >=0.14.0,!=0.17.2,!=0.17.1,!=0.17.0, installed: 0.18.1]
langcodes==3.3.0
lazr.uri==1.0.6
  - setuptools [required: Any, installed: 60.9.3]
orjson==3.6.7
pydantic==1.9.0
  - typing-extensions [required: >=3.7.4.3, installed: 4.1.1]
scooby==0.5.12
typer==0.4.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.0.4]
````
<!--[[[end]]] (checksum: ad8151bab1a35c519f45977d7e22610b)-->
