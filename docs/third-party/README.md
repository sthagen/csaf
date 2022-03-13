# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/csaf/blob/default/sbom.json) with SHA256 checksum ([4c4ba951 ...](https://raw.githubusercontent.com/sthagen/csaf/default/sbom.json.sha256 "sha256:4c4ba95190190dbf1727a1d5aeee6f1f6d6e42fd87629c211e0d481d2b91c613")).
<!--[[[end]]] (checksum: 6f98c9974fff75b42cc2241bc0a55a7f)-->
## Licenses

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                 | Version                                             | License     | Author             | Description (from packaging data)                                     |
|:-----------------------------------------------------|:----------------------------------------------------|:------------|:-------------------|:----------------------------------------------------------------------|
| [jmespath](https://github.com/jmespath/jmespath.py)  | [0.10.0](https://pypi.org/project/jmespath/0.10.0/) | MIT License | James Saryerwinnie | JSON Matching Expressions                                             |
| [jsonschema](https://github.com/Julian/jsonschema)   | [4.4.0](https://pypi.org/project/jsonschema/4.4.0/) | MIT License | Julian Berman      | An implementation of JSON Schema validation for Python                |
| [pydantic](https://github.com/samuelcolvin/pydantic) | [1.9.0](https://pypi.org/project/pydantic/1.9.0/)   | MIT License | Samuel Colvin      | Data validation and settings management using python 3.6 type hinting |
| [typer](https://github.com/tiangolo/typer)           | [0.4.0](https://pypi.org/project/typer/0.4.0/)      | MIT License | Sebastián Ramírez  | Typer, build great CLIs. Easy to code. Based on Python type hints.    |
<!--[[[end]]] (checksum: 70f9d229a9d04775fa318d3660bd9564)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                                           | Version                                                    | License                            | Author            | Description (from packaging data)                      |
|:-----------------------------------------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:------------------|:-------------------------------------------------------|
| [attrs](https://www.attrs.org/)                                                                | [21.4.0](https://pypi.org/project/attrs/21.4.0/)           | MIT License                        | Hynek Schlawack   | Classes Without Boilerplate                            |
| [click](https://palletsprojects.com/p/click/)                                                  | [8.0.4](https://pypi.org/project/click/8.0.4/)             | BSD License                        | Armin Ronacher    | Composable command line interface toolkit              |
| [pyrsistent](http://github.com/tobgu/pyrsistent/)                                              | [0.18.1](https://pypi.org/project/pyrsistent/0.18.1/)      | MIT License                        | Tobias Gustafsson | Persistent/Functional/Immutable data structures        |
| [typing-extensions](https://github.com/python/typing/blob/master/typing_extensions/README.rst) | [4.1.1](https://pypi.org/project/typing-extensions/4.1.1/) | Python Software Foundation License | UNKNOWN           | Backported and Experimental Type Hints for Python 3.6+ |
 <!--[[[end]]] (checksum: 150cb43862496c9609953343bff3357c)-->

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
pydantic==1.9.0
  - typing-extensions [required: >=3.7.4.3, installed: 4.1.1]
typer==0.4.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.0.4]
````
<!--[[[end]]] (checksum: 9c1263662612d794ea22472cb0155913)-->
