"""CSAF Document general definitions."""
from __future__ import annotations

from collections.abc import Sequence
from enum import Enum
from typing import Annotated, List, Optional, no_type_check

from pydantic import AnyUrl, BaseModel, Field, validator


class Id(BaseModel):
    """
    Gives the document producer a place to publish a unique label or tracking ID for the vulnerability
    (if such information exists).
    """

    system_name: Annotated[
        str,
        Field(
            description='Indicates the name of the vulnerability tracking or numbering system.',
            examples=['Cisco Bug ID', 'GitHub Issue'],
            min_length=1,
            title='System name',
        ),
    ]
    text: Annotated[
        str,
        Field(
            description='Is unique label or tracking ID for the vulnerability (if such information exists).',
            examples=['CSCso66472', 'oasis-tcs/csaf#210'],
            min_length=1,
            title='Text',
        ),
    ]


class Name(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Contains the name of a single person.',
            examples=['Albert Einstein', 'Johann Sebastian Bach'],
            min_length=1,
            title='Name of entity being recognized',
        ),
    ]


class Acknowledgment(BaseModel):
    """
    Acknowledges contributions by describing those that contributed.
    """

    names: Annotated[
        Optional[List[Name]],
        Field(
            description='Contains the names of entities being recognized.',
            min_items=1,
            title='List of acknowledged names',
        ),
    ]
    organization: Annotated[
        Optional[str],
        Field(
            description='Contains the name of a contributing organization being recognized.',
            examples=['CISA', 'Google Project Zero', 'Talos'],
            min_length=1,
            title='Contributing organization',
        ),
    ]
    summary: Annotated[
        Optional[str],
        Field(
            description='SHOULD represent any contextual details the document producers wish to make known about the'
            ' acknowledgment or acknowledged parties.',
            examples=['First analysis of Coordinated Multi-Stream Attack (CMSA)'],
            min_length=1,
            title='Summary of the acknowledgment',
        ),
    ]
    urls: Annotated[
        Optional[List[AnyUrl]],
        Field(
            description='Specifies a list of URLs or location of the reference to be acknowledged.',
            min_items=1,
            title='List of URLs',
        ),
    ]

    @no_type_check
    @validator('names', 'organization', 'summary', 'urls')
    def check_len(cls, v):
        if not v:
            raise ValueError('optional element present but empty')
        return v


class Acknowledgments(BaseModel):
    """
    Contains a list of acknowledgment elements.
    """

    __root__: Annotated[
        List[Acknowledgment],
        Field(
            description='Contains a list of acknowledgment elements.',
            min_items=1,
            title='List of acknowledgments',
        ),
    ]

    @no_type_check
    @validator('__root__')
    def check_len(cls, v):
        if not v:
            raise ValueError('optional element present but empty')
        return v


class ReferenceTokenForProductGroupInstance(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description=(
                'Token required to identify a group of products so that it can be referred to from'
                ' other parts in the document.'
                ' There is no predefined or required format for the product_group_id as long as it uniquely identifies'
                ' a group in the context of the current document.'
            ),
            examples=['CSAFGID-0001', 'CSAFGID-0002', 'CSAFGID-0020'],
            min_length=1,
            title='Reference token for product group instance',
        ),
    ]


class ProductGroupId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Token required to identify a group of products so that it can be referred to from other'
            ' parts in the document. There is no predefined or required format for the product_group_id'
            ' as long as it uniquely identifies a group in the context of the current document.',
            examples=['CSAFGID-0001', 'CSAFGID-0002', 'CSAFGID-0020'],
            min_length=1,
            title='Reference token for product group instance',
        ),
    ]


class ProductGroupIds(BaseModel):
    """
    Specifies a list of product_group_ids to give context to the parent item.
    """

    __root__: Annotated[
        List[ProductGroupId],
        Field(
            description='Specifies a list of product_group_ids to give context to the parent item.',
            min_items=1,
            title='List of product_group_ids',
        ),
    ]

    @no_type_check
    @validator('__root__')
    def check_len(cls, v):
        if not v:
            raise ValueError('mandatory element present but empty')
        return v


class ProductId(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Token required to identify a full_product_name so that it can be referred to from other parts'
            ' in the document. There is no predefined or required format for the product_id as long as it'
            ' uniquely identifies a product in the context of the current document.',
            examples=['CSAFPID-0004', 'CSAFPID-0008'],
            min_length=1,
            title='Reference token for product instance',
        ),
    ]


class Products(BaseModel):
    """
    Specifies a list of product_ids to give context to the parent item.
    """

    __root__: Annotated[
        List[ProductId],
        Field(
            description='Specifies a list of product_ids to give context to the parent item.',
            min_items=1,
            title='List of product_ids',
        ),
    ]


class ReferenceTokenForProductInstance(BaseModel):
    value: Annotated[
        str,
        Field(
            description=(
                'Token required to identify a full_product_name so that it can be referred to from other'
                ' parts in the document.'
                ' There is no predefined or required format for the product_id as long as it uniquely'
                ' identifies a product in the context of the current document.'
            ),
            examples=['CSAFPID-0004', 'CSAFPID-0008'],
            min_length=1,
            title='Reference token for product instance',
        ),
    ]


class ListOfProductIds(BaseModel):
    """
    Specifies a list of product_ids to give context to the parent item.
    """

    product_ids: Annotated[
        Sequence[ReferenceTokenForProductInstance],
        Field(
            description='Specifies a list of product_ids to give context to the parent item.',
            # min_items=1,
            title='List of product_ids',
        ),
    ]

    @no_type_check
    @validator('product_ids')
    def check_len(cls, v):
        if not v:
            raise ValueError('mandatory element present but empty')
        return v


class Lang(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Identifies a language, corresponding to IETF BCP 47 / RFC 5646. See IETF language'
            ' registry: https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry',
            examples=['de', 'en', 'fr', 'frc', 'jp'],
            regex='^(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})(-[A-Za-z]{4})?(-([A-Za-z]{2}|'
            '[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-[A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+)*'
            '(-[Xx](-[A-Za-z0-9]{1,8})+)?|[Xx](-[A-Za-z0-9]{1,8})+|[Ii]-[Dd][Ee][Ff][Aa][Uu][Ll][Tt]|'
            '[Ii]-[Mm][Ii][Nn][Gg][Oo])$',
            title='Language type',
        ),
    ]


class NoteCategory(Enum):
    """
    Choice of what kind of note this is.
    """

    description = 'description'
    details = 'details'
    faq = 'faq'
    general = 'general'
    legal_disclaimer = 'legal_disclaimer'
    other = 'other'
    summary = 'summary'


class Note(BaseModel):
    """
    Is a place to put all manner of text blobs related to the current context.
    """

    audience: Annotated[
        Optional[str],
        Field(
            description='Indicate who is intended to read it.',
            examples=[
                'all',
                'executives',
                'operational management and system administrators',
                'safety engineers',
            ],
            min_length=1,
            title='Audience of note',
        ),
    ]
    category: Annotated[
        NoteCategory,
        Field(description='Choice of what kind of note this is.', title='Note category'),
    ]
    text: Annotated[
        str,
        Field(
            description='The contents of the note. Content varies depending on type.',
            min_length=1,
            title='Note contents',
        ),
    ]
    title: Annotated[
        Optional[str],
        Field(
            description='Provides a concise description of what is contained in the text of the note.',
            examples=[
                'Details',
                'Executive summary',
                'Technical summary',
                'Impact on safety systems',
            ],
            min_length=1,
            title='Title of note',
        ),
    ]


class Notes(BaseModel):
    """
    Contains notes which are specific to the current context.
    """

    __root__: Annotated[
        List[Note],
        Field(
            description='Contains notes which are specific to the current context.',
            min_items=1,
            title='List of notes',
        ),
    ]

    @no_type_check
    @validator('__root__')
    def check_len(cls, v):
        if not v:
            raise ValueError('mandatory element present but empty')
        return v


class ReferenceCategory(Enum):
    """
    Indicates whether the reference points to the same document or vulnerability in focus (depending on scope) or
    to an external resource.
    """

    external = 'external'
    self = 'self'


class Reference(BaseModel):
    """
    Holds any reference to conferences, papers, advisories, and other resources that are related and considered
    related to either a surrounding part of or the entire document and to be of value to the document consumer.
    """

    category: Annotated[
        Optional[ReferenceCategory],
        Field(
            description='Indicates whether the reference points to the same document or vulnerability in focus'
            ' (depending on scope) or to an external resource.',
            title='Category of reference',
        ),
    ] = ReferenceCategory.external
    summary: Annotated[
        str,
        Field(
            description='Indicates what this reference refers to.',
            min_length=1,
            title='Summary of the reference',
        ),
    ]
    url: Annotated[
        AnyUrl,
        Field(description='Provides the URL for the reference.', title='URL of reference'),
    ]


class References(BaseModel):
    """
    Holds a list of references.
    """

    __root__: Annotated[
        List[Reference],
        Field(
            description='Holds a list of references.',
            min_items=1,
            title='List of references',
        ),
    ]


class Version(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description=(
                'Specifies a version string to denote clearly the evolution of the content of the document.'
                ' Format must be either integer or semantic versioning.'
            ),
            examples=['1', '4', '0.9.0', '1.4.3', '2.40.0+21AF26D3'],
            regex=(
                '^(0|[1-9][0-9]*)$|^((0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)'
                '(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?'
                '(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?)$'
            ),
            title='Version',
        ),
    ]
