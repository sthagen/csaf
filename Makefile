SHELL = /bin/bash
package = shagen/csaf

.DEFAULT_GOAL := all
isort = isort csaf test
black = black -S -l 120 --target-version py39 csaf test

.PHONY: install
install:
	pip install -U pip wheel
	pip install -r test/requirements.txt
	pip install -U .

.PHONY: install-all
install-all: install
	pip install -r test/requirements-dev.txt

.PHONY: format
format:
	$(isort)
	$(black)

.PHONY: init
init:
	pip install -r test/requirements.txt
	pip install -r test/requirements-dev.txt

.PHONY: lint
lint:
	python setup.py check -ms
	flake8 csaf/ test/
	$(isort) --check-only --df
	$(black) --check --diff

.PHONY: mypy
mypy:
	mypy csaf

.PHONY: test
test: clean
	pytest --asyncio-mode=strict --cov=csaf --cov-report term-missing:skip-covered --cov-branch --log-format="%(levelname)s %(message)s"

.PHONY: testcov
testcov: test
	@echo "building coverage html"
	@coverage html

.PHONY: all
all: lint mypy testcov

.PHONY: dark
dark:
	@black -l120 -S csaf test

.PHONY: sbom
sbom:
	@./gen-sbom
	@cog -I. -P -c -r --check --markers="[[fill ]]] [[[end]]]" -p "from gen_sbom import *;from gen_licenses import *" docs/third-party/README.md
	@if [ $$(grep -c UNKNOWN docs/third-party/README.md) -ne 0 ]; then echo "3rd party NOT_OK"; exit 1; else echo "3rd party documentation OK"; fi

.PHONY: version
version:
	@cog -I. -P -c -r --check --markers="[[fill ]]] [[[end]]]" -p "from gen_version import *" pyproject.toml csaf/__init__.py

.PHONY: secure
secure:
	@bandit --output current-bandit.json --baseline baseline-bandit.json --format json --recursive --quiet --exclude ./test,./build csaf
	@diff -Nu {baseline,current}-bandit.json; printf "^ Only the timestamps ^^ ^^ ^^ ^^ ^^ ^^ should differ. OK?\n"

.PHONY: baseline
baseline:
	@bandit --output baseline-bandit.json --format json --recursive --quiet --exclude ./test,./build csaf
	@cat baseline-bandit.json; printf "\n^ The new baseline ^^ ^^ ^^ ^^ ^^ ^^. OK?\n"

.PHONY: clean
clean:
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -rf .cache htmlcov *.egg-info build dist/*
	@rm -f .coverage .coverage.* *.log current-bandit.json .csaf_cache.sqlite
	python setup.py clean
