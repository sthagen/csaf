"""6.1.2 Multiple Definition of Product ID

For each Product ID (type /$defs/product_id_t) in Full Product Name elements (type: /$defs/full_product_name_t)
it must be tested that the product_id was not already defined within the same document.

The relevant paths for this test are:
  /product_tree/branches[](/branches[])*/product/product_id
  /product_tree/full_product_names[]/product_id
  /product_tree/relationships[]/full_product_name/product_id

Example 41 which fails the test:

  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      },
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product B"
      }
    ]
  }

CSAFPID-9080700 was defined twice.
"""

ID = (6, 1, 2)
TOPIC = 'Multiple Definition of Product ID'
CONDITION_PATHS = (
    # '/product_tree/branches[](/branches[])*/product/product_id',  # TODO(sthagen) recursion may require custom code
    '/product_tree/full_product_names[]/product_id',
    '/product_tree/relationships[]/full_product_name/product_id',
)
CONDITION_JMES_PATHS = tuple(path.lstrip('/').replace('/', '.') for path in CONDITION_PATHS)
PATHS = CONDITION_PATHS
