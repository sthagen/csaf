from typing import Dict, List, Tuple, no_type_check

import jmespath

# import csaf.mandatory.acyclic_product_ids as acy_product_ids
# import csaf.mandatory.consistent_product_status as con_pro_sta
import csaf.mandatory.defined_group_ids as def_gro_ids
import csaf.mandatory.defined_product_ids as def_pro_ids
import csaf.mandatory.translator_and_source_lang as tra_and_sou_lan
import csaf.mandatory.unique_group_ids as uni_gro_ids
import csaf.mandatory.unique_product_ids as uni_pro_ids
import csaf.mandatory.valid_category_name as val_cat_nam


@no_type_check
def guess_max_depth(map_or_seq):
    """HACK A DID ACK - please delete me when cleaning up."""
    if isinstance(map_or_seq, dict):
        return 1 + max(map(guess_max_depth, map_or_seq.values()), default=0)
    elif isinstance(map_or_seq, list):
        return 1 + max(map(guess_max_depth, map_or_seq[0].values()), default=0)
    return 0


@no_type_check
def is_valid(document: dict) -> bool:
    """Complete validation of all mandatory rules.

    This is a spike - we throw it away when all rules are in and back comes something maintainable.
    """
    if not is_valid_category(document):
        return False

    if jmespath.search(tra_and_sou_lan.TRIGGER_JMES_PATH, document) == tra_and_sou_lan.TRIGGER_VALUE:
        if not is_valid_translator(document):
            return False

    if not is_valid_unique_product_ids(document):
        return False

    if not is_valid_unique_group_ids(document):
        return False

    if not is_valid_defined_product_ids(document):
        return False

    if not is_valid_defined_group_ids(document):
        return False

    return NotImplemented


@no_type_check
def is_valid_unique_product_ids(document: dict) -> bool:
    """Temporary implementation of rule for unique product ids."""
    prod_ids = []
    for path in uni_pro_ids.CONDITION_JMES_PATHS:
        pids = jmespath.search(path, document)
        if pids is not None:
            prod_ids.extend(pids)
    probe = jmespath.search('product_tree.branches[]', document)
    trials = guess_max_depth(probe) + 1
    ipath = 'product_tree.branches[].product.product_id'
    inject = 'branches[].product.'
    for trial in range(trials):
        harvest = jmespath.search(ipath, document)
        if harvest:
            prod_ids.extend(harvest)
        ipath = ipath.replace('product.', inject)
    if len(prod_ids) > len(set(prod_ids)):
        return False

    return True


@no_type_check
def is_valid_unique_group_ids(document: dict) -> bool:
    """Temporary implementation of rule for unique group ids."""
    group_ids = jmespath.search(uni_gro_ids.CONDITION_JMES_PATH, document)
    if group_ids is not None:
        if len(group_ids) > len(set(group_ids)):
            return False

    return True


@no_type_check
def is_valid_defined_product_ids(document: dict) -> bool:
    """Temporary implementation of rule for defined product ids."""
    defined_prod_ids = jmespath.search(def_pro_ids.TRIGGER_JMES_PATH, document)
    # TODO(sthagen) too shallow tree visiting # print("DEBUG>>>", defined_prod_ids)
    if defined_prod_ids is None:
        defined_prod_ids = []
    known_prod_ids = set(defined_prod_ids)
    for path in def_pro_ids.CONDITION_JMES_PATHS:
        claim_prod_ids = jmespath.search(path, document)
        if claim_prod_ids is not None:
            if any(claim_prod_id not in known_prod_ids for claim_prod_id in claim_prod_ids):
                return False

    return True


@no_type_check
def is_valid_defined_group_ids(document: dict) -> bool:
    """Temporary implementation of rule for defined group ids."""
    defined_group_ids = jmespath.search(def_gro_ids.TRIGGER_JMES_PATH, document)
    if defined_group_ids is None:
        defined_group_ids = []
    known_group_ids = set(defined_group_ids)
    for path in def_gro_ids.CONDITION_JMES_PATHS:
        claim_group_ids = jmespath.search(path, document)
        if claim_group_ids is not None:
            if any(claim_group_id not in known_group_ids for cl_seq in claim_group_ids for claim_group_id in cl_seq):
                return False

    return True


@no_type_check
def exists(document: dict, claims: Dict[str, List[str]]) -> Tuple[Tuple[str, str, bool]]:
    """Verify the existence and return tuple of triplets with claim, path and result."""
    return tuple(
        (claim, path, bool(jmespath.search(path, document))) for claim, paths in claims.items() for path in paths
    )


@no_type_check
def must_skip(document: dict, path: str, skip_these: Tuple[str, ...]) -> Tuple[str, str, bool]:
    """Verify any skips and return tuple of triplets with claim, path and result."""
    value = jmespath.search(path, document)
    return value, path, any(value == skip for skip in skip_these)


@no_type_check
def is_valid_category(document: dict) -> bool:
    """Verify category value."""
    return val_cat_nam.is_valid(jmespath.search(val_cat_nam.CONDITION_JMES_PATH, document))


@no_type_check
def is_valid_translator(document: dict) -> bool:
    """Verify source_lang value is present for translator."""
    if jmespath.search(tra_and_sou_lan.TRIGGER_JMES_PATH, document) != tra_and_sou_lan.TRIGGER_VALUE:
        return False
    return bool(jmespath.search(tra_and_sou_lan.CONDITION_JMES_PATH, document))
