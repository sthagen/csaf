# -*- coding: utf-8 -*-
# pylint: disable=c-extension-no-member,expression-not-assigned,line-too-long,logging-fstring-interpolation
"""Do the lint."""
import configparser
import csv
import json
import logging
import pathlib
import sys

import jsonschema  # type: ignore
from lxml import etree  # type: ignore
import toml
from yaml import load as load_yaml
try:
    from yaml import CLoader as LoaderYaml
except ImportError:
    from yaml import Loader as LoaderYaml

ENCODING = "utf-8"

APP = 'csaf'

LOG = logging.getLogger()  # Temporary refactoring: module level logger
LOG_FOLDER = pathlib.Path('logs')
LOG_FILE = f'{APP}.log'
LOG_PATH = pathlib.Path(LOG_FOLDER, LOG_FILE) if LOG_FOLDER.is_dir() else pathlib.Path(LOG_FILE)
LOG_LEVEL = logging.INFO


def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global LOG  # pylint: disable=global-statement

    log_format = {
        'format': '%(asctime)s.%(msecs)03d %(levelname)s [%(name)s]: %(message)s',
        'datefmt': '%Y-%m-%dT%H:%M:%S',
        # 'filename': LOG_PATH,
        'level': LOG_LEVEL if level is None else level
    }
    logging.basicConfig(**log_format)
    LOG = logging.getLogger(APP if name is None else name)
    LOG.propagate = True


def load_xml(document_path):
    """
    Parse the document at path (to ensure it is well-formed XML) to obtain an ElementTree object.
    Return value is an ordered pair of Union(None, ElementTree object) and a message string
    """
    try:
        doc = etree.parse(str(document_path), etree.XMLParser(encoding="utf-8"))
    except IOError as err:
        return None, f"file {document_path} failed with IO error {err}"
    except etree.XMLSyntaxError as err:
        return (
            None,
            f"parsing from {document_path} failed with XMLSyntaxError error {err}",
        )

    return doc, f"well-formed xml tree from {document_path}"


def walk_tree_explicit(base_path):
    """Visit the files in the folders below base path."""
    if base_path.is_file():
        yield base_path
    else:
        for entry in base_path.iterdir():
            if entry.is_dir():
                for file_path in entry.iterdir():
                    yield file_path
            else:
                yield entry


def visit(tree_or_file_path):
    """Visit tree and yield the leaves."""
    thing = pathlib.Path(tree_or_file_path)
    if thing.is_file():
        yield thing
    else:
        for path in thing.rglob("*"):
            yield path


def slugify(error):
    """Replace newlines by space."""
    return str(error).replace('\n', '')


def main(argv=None, abort=False, debug=None):
    """Drive the validator.
    This function acts as the command line interface backend.
    There is some duplication to support testability.
    """
    init_logger(level=logging.DEBUG if debug else None)
    forest = argv if argv else sys.argv[1:]
    if not forest:
        print("Usage: gelee paths-to-files")
        return 0, "USAGE"
    num_trees = len(forest)
    LOG.debug("Guarded dispatch forest=%s, num_trees=%d", forest, num_trees)

    LOG.info("Starting validation visiting a forest with %d tree%s",
             num_trees, '' if num_trees == 1 else 's')
    failure_path_reason = "Failed validation for path %s with error: %s"
    total, folders, ignored, csvs, inis, jsons, tomls, xmls, yamls = 0, 0, 0, 0, 0, 0, 0, 0, 0
    failures = 0
    for tree in forest:
        for path in visit(tree):
            LOG.debug(" - path=%s, total=%d", path, total)
            total += 1
            if not path.is_file():
                folders += 1
                continue

            final_suffix = '' if not path.suffixes else path.suffixes[-1].lower()

            if final_suffix == ".csv":
                if not path.stat().st_size:
                    LOG.error(failure_path_reason, path, "ERROR: Empty CSV file")
                    if abort:
                        return 1, "ERROR: Empty CSV file"
                    failures += 1
                    continue

                with open(path, newline='') as handle:
                    try:
                        try:
                            dialect = csv.Sniffer().sniff(handle.read(1024), ",\t; ")
                            handle.seek(0)
                        except csv.Error as err:
                            if "could not determine delimiter" in str(err).lower():
                                dialect = csv.Dialect()
                                dialect.delimiter = ','
                                dialect.quoting = csv.QUOTE_NONE
                                dialect.strict = True
                            else:
                                LOG.error(failure_path_reason, path, slugify(err))
                                if abort:
                                    return 1, str(err)
                                failures += 1
                        try:
                            reader = csv.reader(handle, dialect)
                            for _ in reader:
                                pass
                            csvs += 1
                        except csv.Error as err:
                            LOG.error(failure_path_reason, path, slugify(err))
                            if abort:
                                return 1, str(err)
                            failures += 1
                    except (Exception, csv.Error) as err:
                        LOG.error(failure_path_reason, path, slugify(err))
                        if abort:
                            return 1, str(err)
                        failures += 1
            elif final_suffix == ".ini":
                config = configparser.ConfigParser()
                try:
                    config.read(path)
                    inis += 1
                except configparser.NoSectionError as err:
                    LOG.error(failure_path_reason, path, slugify(err))
                    if abort:
                        return 1, str(err)
                    failures += 1
                except configparser.DuplicateSectionError as err:
                    LOG.error(failure_path_reason, path, slugify(err))
                    if abort:
                        return 1, str(err)
                    failures += 1
                except configparser.DuplicateOptionError as err:
                    LOG.error(failure_path_reason, path, slugify(err))
                    if abort:
                        return 1, str(err)
                    failures += 1
                except configparser.NoOptionError as err:
                    LOG.error(failure_path_reason, path, slugify(err))
                    if abort:
                        return 1, str(err)
                    failures += 1
                except configparser.InterpolationDepthError as err:
                    LOG.error(failure_path_reason, path, slugify(err))
                    if abort:
                        return 1, str(err)
                    failures += 1
                except configparser.InterpolationMissingOptionError as err:
                    LOG.error(failure_path_reason, path, slugify(err))
                    if abort:
                        return 1, str(err)
                    failures += 1
                except configparser.InterpolationSyntaxError as err:
                    LOG.error(failure_path_reason, path, slugify(err))
                    if abort:
                        return 1, str(err)
                    failures += 1
                except configparser.InterpolationError as err:
                    LOG.error(failure_path_reason, path, slugify(err))
                    if abort:
                        return 1, str(err)
                    failures += 1
                except configparser.MissingSectionHeaderError as err:
                    LOG.error(failure_path_reason, path, slugify(err))
                    if abort:
                        return 1, str(err)
                    failures += 1
                except configparser.ParsingError as err:
                    LOG.error(failure_path_reason, path, slugify(err))
                    if abort:
                        return 1, str(err)
                    failures += 1
            elif final_suffix in (".geojson", ".json", ".toml"):
                loader = toml.load if final_suffix == ".toml" else json.load
                with open(path, "rt", encoding="utf-8") as handle:
                    try:
                        _ = loader(handle)
                        if final_suffix == ".toml":
                            tomls += 1
                        else:
                            jsons += 1
                    except Exception as err:
                        LOG.error(failure_path_reason, path, slugify(err))
                        if abort:
                            return 1, str(err)
                        failures += 1
            elif final_suffix == ".xml":
                if not path.stat().st_size:
                    LOG.error(failure_path_reason, path, "ERROR: Empty XML file")
                    if abort:
                        return 1, "ERROR: Empty XML file"
                    failures += 1
                    continue

                xml_tree, message = load_xml(path)
                if xml_tree:
                    xmls += 1
                else:
                    LOG.error(failure_path_reason, path, slugify(message))
                    if abort:
                        return 1, str(message)
                    failures += 1
            elif final_suffix in (".yaml", ".yml"):
                with open(path, "rt", encoding="utf-8") as handle:
                    try:
                        _ = load_yaml(handle, Loader=LoaderYaml)
                        yamls += 1
                    except Exception as err:
                        LOG.error(failure_path_reason, path, slugify(err))
                        if abort:
                            return 1, str(err)
                        failures += 1
            else:
                ignored += 1
                continue

    success = "Successfully validated"
    pairs = (
        (csvs, "CSV"),
        (inis, "INI"),
        (jsons, "JSON"),
        (tomls, "TOML"),
        (xmls, "XML"),
        (yamls, "YAML"),
    )
    for count, kind in pairs:
        if count:
            LOG.info(
                "- %s %d total %s file%s.", success, count, kind, "" if count == 1 else "s")

    configs = csvs + inis + jsons + tomls + xmls + yamls
    LOG.info(  # TODO remove f-strings also here
        f"Finished validation of {configs} configuration file{'' if configs == 1 else 's'}"
        f" with {failures} failure{'' if failures == 1 else 's'}"
        f" visiting {total} path{'' if total == 1 else 's'}"
        f" (ignored {ignored} non-config file{'' if ignored == 1 else 's'}"
        f" in {folders} folder{'' if folders == 1 else 's'})"
    )
    print(f"{'OK' if not failures else 'FAIL'}")

    return 0, ""
