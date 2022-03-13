SHELL = /bin/bash
package = shagen/csaf

.DEFAULT_GOAL := all
isort = isort csaf tests
black = black -S -l 120 --target-version py38 csaf tests

.PHONY: install
install:
	pip install -U pip wheel
	pip install -r tests/requirements.txt
	pip install -U .

.PHONY: install-all
install-all: install
	pip install -r tests/requirements-dev.txt

.PHONY: isort
format:
	$(isort)
	$(black)

.PHONY: init
init:
	pip install -r tests/requirements.txt
	pip install -r tests/requirements-dev.txt

.PHONY: lint
lint:
	python setup.py check -ms
	flake8 csaf/ tests/
	$(isort) --check-only --df
	$(black) --check --diff

.PHONY: mypy
mypy:
	mypy csaf

.PHONY: test
test: clean
	pytest --cov=csaf --log-format="%(levelname)s %(message)s" --asyncio-mode=strict

.PHONY: testcov
testcov: test
	@echo "building coverage html"
	@coverage html

.PHONY: all
all: lint mypy testcov

.PHONY: sbom
sbom:
	@./gen-sbom
	@cog -I. -P -c -r --check --markers="[[fill ]]] [[[end]]]" -p "from gen_sbom import *;from gen_licenses import *" docs/third-party/README.md

.PHONY: version
version:
	@cog -I. -P -c -r --check --markers="[[fill ]]] [[[end]]]" -p "from gen_version import *" pyproject.toml csaf/__init__.py

.PHONY: secure
secure:
	@bandit --output current-bandit.json --baseline baseline-bandit.json --format json --recursive --quiet --exclude ./tests,./build csaf
	@diff -Nu {baseline,current}-bandit.json; printf "^ Only the timestamps ^^ ^^ ^^ ^^ ^^ ^^ should differ. OK?\n"

.PHONY: baseline
baseline:
	@bandit --output baseline-bandit.json --format json --recursive --quiet --exclude ./tests,./build csaf
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
