import re
from test import conftest

import msgspec
import pytest

import csaf.definitions as defs
import csaf.product as product


def test_product_empty():
    assert isinstance(product.ProductTree(), product.ProductTree)


def test_product_positional_text():
    message = 'BaseModel.__init__() takes 1 positional argument but 3 were given'
    with pytest.raises(TypeError, match=re.escape(message)):
        _ = product.ProductTree('positional', 'text')  # type: ignore


def test_product_relationship():
    pr_ref_other = product.ReferenceTokenForProductInstance('acme-101')
    pr_ref_self = product.ReferenceTokenForProductInstance('acme-112')
    pr_id = pr_ref_self
    pr_ids = product.Products(['acme-101', 'acme-112'])
    assert defs.ProductId('acme-101') in pr_ids.root
    pr_name = product.FullProductName(name='wun', product_id=pr_id)
    data = {
        'category': product.RelationshipCategory.installed_with,
        'full_product_name': pr_name,
        'product_reference': pr_ref_self,
        'relates_to_product_reference': pr_ref_other,
    }
    rel = product.Relationship(**data)
    assert rel.category == product.RelationshipCategory.installed_with


def test_product_relationship_loads():
    rel = product.Relationship(**conftest.PRODUCT_RELATIONSHIP_DATA)
    assert msgspec.json.decode(rel.model_dump_json()) == conftest.PRODUCT_RELATIONSHIP_DATA


def test_product_relationship_dumps():
    pr_ref_other = product.ReferenceTokenForProductInstance('acme-101')
    pr_ref_self = product.ReferenceTokenForProductInstance('acme-112')
    pr_id = pr_ref_self
    pr_ids = product.Products(['acme-101', 'acme-112'])
    assert defs.ProductId('acme-101') in pr_ids.root
    pr_name = product.FullProductName(name='wun', product_id=pr_id)
    data = {
        'category': product.RelationshipCategory.installed_with,
        'full_product_name': pr_name,
        'product_reference': pr_ref_self,
        'relates_to_product_reference': pr_ref_other,
    }
    rel = product.Relationship(**data)
    assert msgspec.json.decode(rel.model_dump_json()) == conftest.PRODUCT_RELATIONSHIP_DATA
