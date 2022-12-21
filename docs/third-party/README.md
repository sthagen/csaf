# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/csaf/blob/default/sbom.json) with SHA256 checksum ([8418d336 ...](https://raw.githubusercontent.com/sthagen/csaf/default/sbom.json.sha256 "sha256:8418d3360380ba8012b647e0fad60ab6225b945e21d8d85d68b1c6b2fcd6c12f")).
<!--[[[end]]] (checksum: c9cacbe1a7ed66bd7d3ee417002fb69f)-->
## Licenses

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                | Version                                               | License                                             | Author                                                              | Description (from packaging data)                                             |
|:----------------------------------------------------|:------------------------------------------------------|:----------------------------------------------------|:--------------------------------------------------------------------|:------------------------------------------------------------------------------|
| [jmespath](https://github.com/jmespath/jmespath.py) | [1.0.1](https://pypi.org/project/jmespath/1.0.1/)     | MIT License                                         | James Saryerwinnie                                                  | JSON Matching Expressions                                                     |
| [langcodes](https://github.com/rspeer/langcodes)    | [3.3.0](https://pypi.org/project/langcodes/3.3.0/)    | MIT License                                         | Elia Robyn Speer                                                    | Tools for labeling human languages with IETF language tags                    |
| [lazr.uri](https://launchpad.net/lazr.uri)          | [1.0.6](https://pypi.org/project/lazr.uri/1.0.6/)     | GNU Library or Lesser General Public License (LGPL) | "LAZR Developers" team                                              | A self-contained, easily reusable library for parsing, manipulating,          |
| [msgspec](https://jcristharif.com/msgspec/)         | [0.11.0](https://pypi.org/project/msgspec/0.11.0/)    | BSD License                                         | Jim Crist-Harif                                                     | A fast and friendly JSON/MessagePack library, with optional schema validation |
| [pydantic](https://github.com/pydantic/pydantic)    | [1.10.2](https://pypi.org/project/pydantic/1.10.2/)   | MIT License                                         | Samuel Colvin                                                       | Data validation and settings management using python type hints               |
| [scooby](https://github.com/banesullivan/scooby)    | [0.7.0](https://pypi.org/project/scooby/0.7.0/)       | MIT License                                         | Dieter Werthmüller, Bane Sullivan, Alex Kaszynski, and contributors | A Great Dane turned Python environment detective                              |
| [setuptools](https://github.com/pypa/setuptools)    | [65.6.3](https://pypi.org/project/setuptools/65.6.3/) | MIT License                                         | Python Packaging Authority                                          | Easily download, build, install, upgrade, and uninstall Python packages       |
| [typer](https://github.com/tiangolo/typer)          | [0.7.0](https://pypi.org/project/typer/0.7.0/)        | MIT License                                         | Sebastián Ramírez                                                   | Typer, build great CLIs. Easy to code. Based on Python type hints.            |
| jsonschema                                          | [4.17.3](https://pypi.org/project/jsonschema/4.17.3/) | MIT License                                         | Julian Berman                                                       | An implementation of JSON Schema validation for Python                        |
<!--[[[end]]] (checksum: 5b6606aca0aa833c549d735932146095)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                              | Version                                               | License     | Author            | Description (from packaging data)               |
|:--------------------------------------------------|:------------------------------------------------------|:------------|:------------------|:------------------------------------------------|
| [attrs](https://www.attrs.org/)                   | [21.4.0](https://pypi.org/project/attrs/21.4.0/)      | MIT License | Hynek Schlawack   | Classes Without Boilerplate                     |
| [click](https://palletsprojects.com/p/click/)     | [8.1.3](https://pypi.org/project/click/8.1.3/)        | BSD License | Armin Ronacher    | Composable command line interface toolkit       |
| [pyrsistent](http://github.com/tobgu/pyrsistent/) | [0.18.1](https://pypi.org/project/pyrsistent/0.18.1/) | MIT License | Tobias Gustafsson | Persistent/Functional/Immutable data structures |
<!--[[[end]]] (checksum: 05d6506dda54981d337721dd6cda817e)-->

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
  - attrs [required: >=17.4.0, installed: 21.4.0]
  - pyrsistent [required: >=0.14.0,!=0.17.2,!=0.17.1,!=0.17.0, installed: 0.18.1]
langcodes==3.3.0
lazr.uri==1.0.6
  - setuptools [required: Any, installed: 65.6.3]
msgspec==0.11.0
pydantic==1.10.2
  - typing-extensions [required: >=4.1.0, installed: 4.2.0]
scooby==0.7.0
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: eda40a277d2a2cf2f3a87931a0c433b8)-->
