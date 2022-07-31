"""CSAF Product Tree model."""
from __future__ import annotations

import re
from collections.abc import Sequence
from enum import Enum
from typing import Annotated, List, Optional, no_type_check

from pydantic import BaseModel, Field, validator

from csaf.definitions import AnyUrl, Products, ReferenceTokenForProductGroupInstance, ReferenceTokenForProductInstance


class FileHash(BaseModel):
    """
    Contains one hash value and algorithm of the file to be identified.
    """

    algorithm: Annotated[
        str,
        Field(
            description='Contains the name of the cryptographic hash algorithm used to calculate the value.',
            examples=['blake2b512', 'sha256', 'sha3-512', 'sha384', 'sha512'],
            min_length=1,
            title='Algorithm of the cryptographic hash',
        ),
    ]
    value: Annotated[
        str,
        Field(
            description='Contains the cryptographic hash value in hexadecimal representation.',
            examples=[
                (
                    '37df33cb7464da5c7f077f4d56a32bc84987ec1d85b234537c1c1a4d4fc8d09d'
                    'c29e2e762cb5203677bf849a2855a0283710f1f5fe1d6ce8d5ac85c645d0fcb3'
                ),
                '4775203615d9534a8bfca96a93dc8b461a489f69124a130d786b42204f3341cc',
                '9ea4c8200113d49d26505da0e02e2f49055dc078d1ad7a419b32e291c7afebbb84badfbd46dec42883bea0b2a1fa697c',
            ],
            min_length=32,
            regex='^[0-9a-fA-F]{32,}$',
            title='Value of the cryptographic hash',
        ),
    ]


class CryptographicHashes(BaseModel):
    """
    Contains all information to identify a file based on its cryptographic hash values.
    """

    file_hashes: Annotated[
        Sequence[FileHash],
        Field(
            description='Contains a list of cryptographic hashes for this file.',
            # min_items=1,
            title='List of file hashes',
        ),
    ]
    filename: Annotated[
        str,
        Field(
            description='Contains the name of the file which is identified by the hash values.',
            examples=['WINWORD.EXE', 'msotadddin.dll', 'sudoers.so'],
            # min_length=1,
            title='Filename',
        ),
    ]

    @no_type_check
    @validator('file_hashes', 'filename')
    @classmethod
    def check_len(cls, v):
        if not v:
            raise ValueError('mandatory element present but empty')
        return v


class GenericUri(BaseModel):
    """
    Provides a generic extension point for any identifier which is either vendor-specific or
    derived from a standard not yet supported.
    """

    namespace: Annotated[
        AnyUrl,
        Field(
            description=(
                'Refers to a URL which provides the name and knowledge about the specification used or'
                ' is the namespace in which these values are valid.'
            ),
            title='Namespace of the generic URI',
        ),
    ]
    uri: Annotated[AnyUrl, Field(description='Contains the identifier itself.', title='URI')]


class SerialNumber(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Contains a part, or a full serial number of the component to identify.',
            min_length=1,
            title='Serial number',
        ),
    ]


class StockKeepingUnit(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description=(
                'Contains a part, or a full stock keeping unit (SKU) which is used in the ordering process'
                ' to identify the component.'
            ),
            min_length=1,
            title='Stock keeping unit',
        ),
    ]


class HelperToIdentifyTheProduct(BaseModel):
    """
    Provides at least one method which aids in identifying the product in an asset database.
    """

    cpe: Annotated[
        Optional[str],
        Field(
            description=(
                'The Common Platform Enumeration (CPE) attribute refers to a method for naming platforms external'
                ' to this specification.'
            ),
            min_length=5,
            regex=(
                '^(cpe:2\\.3:[aho\\*\\-](:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|'
                '(\\\\[\\\\\\*\\?!"#\\$%&\'\\(\\)\\+,/:;<=>@\\[\\]\\^`\\{\\|\\}~]))+(\\?*|\\*?))|[\\*\\-])){5}'
                '(:(([a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?)|[\\*\\-]))(:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|'
                '(\\\\[\\\\\\*\\?!"#\\$%&\'\\(\\)\\+,/:;<=>@\\[\\]\\^`\\{\\|\\}~]))+(\\?*|\\*?))|[\\*\\-])){4})|'
                '([c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\\._\\-~%]*){0,6})$'
            ),
            title='Common Platform Enumeration representation',
        ),
    ] = None
    hashes: Annotated[
        Optional[Sequence[CryptographicHashes]],
        Field(
            description='Contains a list of cryptographic hashes usable to identify files.',
            # min_items=1,
            title='List of hashes',
        ),
    ] = None
    purl: Annotated[
        Optional[AnyUrl],
        Field(
            description=(
                'The package URL (purl) attribute refers to a method for reliably identifying and'
                ' locating software packages external to this specification.'
            ),
            # min_length=7,
            # regex='^pkg:[A-Za-z\\.\\-\\+][A-Za-z0-9\\.\\-\\+]*/.+',
            title='package URL representation',
        ),
    ] = None
    sbom_urls: Annotated[
        Optional[Sequence[AnyUrl]],
        Field(
            description='Contains a list of URLs where SBOMs for this product can be retrieved.',
            # min_items=1,
            title='List of SBOM URLs',
        ),
    ] = None
    serial_numbers: Annotated[
        Optional[Sequence[SerialNumber]],
        Field(
            description='Contains a list of parts, or full serial numbers.',
            # min_items=1,
            title='List of serial numbers',
        ),
    ] = None
    skus: Annotated[
        Optional[Sequence[StockKeepingUnit]],
        Field(
            description='Contains a list of parts, or full stock keeping units.',
            # min_items=1,
            title='List of stock keeping units',
        ),
    ] = None
    x_generic_uris: Annotated[
        Optional[Sequence[GenericUri]],
        Field(
            description=(
                'Contains a list of identifiers which are either vendor-specific or derived from'
                ' a standard not yet supported.'
            ),
            # min_items=1,
            title='List of generic URIs',
        ),
    ] = None

    @no_type_check
    @validator('hashes', 'sbom_urls', 'serial_numbers', 'skus', 'x_generic_uris')
    @classmethod
    def check_len(cls, v):
        if not v:
            raise ValueError('optional element present but empty')
        return v

    @no_type_check
    @validator('purl')
    @classmethod
    def check_purl(cls, v):
        if not v or len(v) < 7:
            raise ValueError('optional purl element present but too short')
        if not re.match('^pkg:[A-Za-z\\.\\-\\+][A-Za-z0-9\\.\\-\\+]*/.+', v):
            raise ValueError('optional purl element present but is no purl (regex does not match)')
        return v


class FullProductName(BaseModel):
    """
    Specifies information about the product and assigns the product_id.
    """

    name: Annotated[
        str,
        Field(
            description=(
                "The value should be the product's full canonical name, including version number and other attributes,"
                ' as it would be used in a human-friendly document.'
            ),
            examples=[
                'Cisco AnyConnect Secure Mobility Client 2.3.185',
                'Microsoft Host Integration Server 2006 Service Pack 1',
            ],
            min_length=1,
            title='Textual description of the product',
        ),
    ]
    product_id: ReferenceTokenForProductInstance
    product_identification_helper: Annotated[
        Optional[HelperToIdentifyTheProduct],
        Field(
            description='Provides at least one method which aids in identifying the product in an asset database.',
            title='Helper to identify the product',
        ),
    ] = None


class ProductGroup(BaseModel):
    """
    Defines a new logical group of products that can then be referred to in other parts of the document to address
    a group of products with a single identifier.
    """

    group_id: ReferenceTokenForProductGroupInstance
    product_ids: Annotated[
        Sequence[ReferenceTokenForProductInstance],
        Field(
            description='Lists the product_ids of those products which known as one group in the document.',
            # min_items=2,
            title='List of Product IDs',
        ),
    ]
    summary: Annotated[
        Optional[str],
        Field(
            description='Gives a short, optional description of the group.',
            examples=[
                'Products supporting Modbus.',
                'The x64 versions of the operating system.',
            ],
            min_length=1,
            title='Summary of the product group',
        ),
    ] = None

    @no_type_check
    @validator('product_ids')
    @classmethod
    def check_len(cls, v):
        if len(v) < 2:
            raise ValueError('mandatory element present but too few items')
        return v


class ProductStatus(BaseModel):
    """
    Contains different lists of product_ids which provide details on the status of the referenced product related
    to the current vulnerability.
    """

    first_affected: Annotated[
        Optional[Products],
        Field(
            description='These are the first versions of the releases known to be affected by the vulnerability.',
            title='First affected',
        ),
    ]
    first_fixed: Annotated[
        Optional[Products],
        Field(
            description='These versions contain the first fix for the vulnerability but may not be the recommended'
            ' fixed versions.',
            title='First fixed',
        ),
    ]
    fixed: Annotated[
        Optional[Products],
        Field(
            description='These versions contain a fix for the vulnerability but may not be the recommended'
            ' fixed versions.',
            title='Fixed',
        ),
    ]
    known_affected: Annotated[
        Optional[Products],
        Field(
            description='These versions are known to be affected by the vulnerability.',
            title='Known affected',
        ),
    ]
    known_not_affected: Annotated[
        Optional[Products],
        Field(
            description='These versions are known not to be affected by the vulnerability.',
            title='Known not affected',
        ),
    ]
    last_affected: Annotated[
        Optional[Products],
        Field(
            description='These are the last versions in a release train known to be affected by the vulnerability.'
            ' Subsequently released versions would contain a fix for the vulnerability.',
            title='Last affected',
        ),
    ]
    recommended: Annotated[
        Optional[Products],
        Field(
            description='These versions have a fix for the vulnerability and are the vendor-recommended versions for'
            ' fixing the vulnerability.',
            title='Recommended',
        ),
    ]
    under_investigation: Annotated[
        Optional[Products],
        Field(
            description='It is not known yet whether these versions are or are not affected by the vulnerability.'
            ' However, it is still under investigation - the result will be provided in a later release'
            ' of the document.',
            title='Under investigation',
        ),
    ]


class RelationshipCategory(Enum):
    """
    Defines the category of relationship for the referenced component.
    """

    default_component_of = 'default_component_of'
    external_component_of = 'external_component_of'
    installed_on = 'installed_on'
    installed_with = 'installed_with'
    optional_component_of = 'optional_component_of'


class Relationship(BaseModel):
    """
    Establishes a link between two existing full_product_name_t elements, allowing the document producer to define
    a combination of two products that form a new full_product_name entry.
    """

    category: Annotated[
        RelationshipCategory,
        Field(
            description='Defines the category of relationship for the referenced component.',
            title='Relationship category',
        ),
    ]
    full_product_name: FullProductName
    product_reference: Annotated[
        ReferenceTokenForProductInstance,
        Field(
            description=(
                'Holds a Product ID that refers to the Full Product Name element,'
                ' which is referenced as the first element of the relationship.'
            ),
            title='Product reference',
        ),
    ]
    relates_to_product_reference: Annotated[
        ReferenceTokenForProductInstance,
        Field(
            description=(
                'Holds a Product ID that refers to the Full Product Name element,'
                ' which is referenced as the second element of the relationship.'
            ),
            title='Relates to product reference',
        ),
    ]


class ProductTree(BaseModel):
    """
    Is a container for all fully qualified product names that can be referenced elsewhere in the document.
    """

    branches: Optional[Branches]
    full_product_names: Annotated[
        Optional[List[FullProductName]],
        Field(
            description='Contains a list of full product names.',
            min_items=1,
            title='List of full product names',
        ),
    ]
    product_groups: Annotated[
        Optional[List[ProductGroup]],
        Field(
            description='Contains a list of product groups.',
            min_items=1,
            title='List of product groups',
        ),
    ]
    relationships: Annotated[
        Optional[List[Relationship]],
        Field(
            description='Contains a list of relationships.',
            min_items=1,
            title='List of relationships',
        ),
    ]

    @no_type_check
    @validator('full_product_names', 'product_groups', 'relationships')
    @classmethod
    def check_len(cls, v):
        if not v:
            raise ValueError('optional element present but empty')
        return v


class BranchCategory(Enum):
    """
    Describes the characteristics of the labeled branch.
    """

    architecture = 'architecture'
    host_name = 'host_name'
    language = 'language'
    legacy = 'legacy'
    patch_level = 'patch_level'
    product_family = 'product_family'
    product_name = 'product_name'
    product_version = 'product_version'
    service_pack = 'service_pack'
    specification = 'specification'
    vendor = 'vendor'


class Branch(BaseModel):
    """
    Is a part of the hierarchical structure of the product tree.
    """

    branches: Optional[Branches]
    category: Annotated[
        BranchCategory,
        Field(
            description='Describes the characteristics of the labeled branch.',
            title='Category of the branch',
        ),
    ]
    name: Annotated[
        str,
        Field(
            description="Contains the canonical descriptor or 'friendly name' of the branch.",
            examples=[
                '10',
                '365',
                'Microsoft',
                'Office',
                'PCS 7',
                'SIMATIC',
                'Siemens',
                'Windows',
            ],
            min_length=1,
            title='Name of the branch',
        ),
    ]
    product: Optional[FullProductName]


class Branches(BaseModel):
    """
    Contains branch elements as children of the current element.
    """

    __root__: Annotated[
        List[Branch],
        Field(
            description='Contains branch elements as children of the current element.',
            min_items=1,
            title='List of branches',
        ),
    ]

    @no_type_check
    @validator('__root__')
    @classmethod
    def check_len(cls, v):
        if not v:
            raise ValueError('mandatory element present but empty')
        return v


Branch.update_forward_refs()
FullProductName.update_forward_refs()
ProductTree.update_forward_refs()
