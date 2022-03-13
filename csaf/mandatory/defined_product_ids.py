"""6.1.1 Missing Definition of Product ID

For each element of type /$defs/product_id_t which is not inside a Full Product Name (type: full_product_name_t)
and therefore reference an element within the product_tree it must be tested that the Full Product Name element
with the matching product_id exists. The same applies for all items of elements of type /$defs/products_t.

The relevant paths for this test are:
  /product_tree/product_groups[]/product_ids[]
  /product_tree/relationships[]/product_reference
  /product_tree/relationships[]/relates_to_product_reference
  /vulnerabilities[]/product_status/first_affected[]
  /vulnerabilities[]/product_status/first_fixed[]
  /vulnerabilities[]/product_status/fixed[]
  /vulnerabilities[]/product_status/known_affected[]
  /vulnerabilities[]/product_status/known_not_affected[]
  /vulnerabilities[]/product_status/last_affected[]
  /vulnerabilities[]/product_status/recommended[]
  /vulnerabilities[]/product_status/under_investigation[]
  /vulnerabilities[]/remediations[]/product_ids[]
  /vulnerabilities[]/scores[]/products[]
  /vulnerabilities[]/threats[]/product_ids[]

Example 40 which fails the test:

  "product_tree": {
    "product_groups": [
      {
        "group_id": "CSAFGID-1020300",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ]
      }
    ]
  }

Neither CSAFPID-9080700 nor CSAFPID-9080701 were defined in the product_tree.
"""

ID = (6, 1, 1)
TOPIC = 'Missing Definition of Product ID'
TRIGGER_PATH = 'product_tree/full_product_names[]/product_id'
TRIGGER_JMES_PATH = TRIGGER_PATH.lstrip('/').replace('/', '.')
CONDITION_PATHS = (
    '/product_tree/product_groups[]/product_ids[]',
    '/product_tree/relationships[]/product_reference',
    '/product_tree/relationships[]/relates_to_product_reference',
    '/vulnerabilities[]/product_status/first_affected[]',
    '/vulnerabilities[]/product_status/first_fixed[]',
    '/vulnerabilities[]/product_status/fixed[]',
    '/vulnerabilities[]/product_status/known_affected[]',
    '/vulnerabilities[]/product_status/known_not_affected[]',
    '/vulnerabilities[]/product_status/last_affected[]',
    '/vulnerabilities[]/product_status/recommended[]',
    '/vulnerabilities[]/product_status/under_investigation[]',
    '/vulnerabilities[]/remediations[]/product_ids[]',
    '/vulnerabilities[]/scores[]/products[]',
    '/vulnerabilities[]/threats[]/product_ids[]',
)
CONDITION_JMES_PATHS = tuple(path.lstrip('/').replace('/', '.') for path in CONDITION_PATHS)
PATHS = CONDITION_PATHS
