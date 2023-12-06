from typing import TYPE_CHECKING

from src.Transfers.FieldCollectionTransfer import FieldCollectionTransfer
from src.Transfers.FieldTransfer import FieldTransfer

if TYPE_CHECKING:
    from xml.etree.ElementTree import Element


class FieldExtractor:
    def extract_fields(self, transfer_fields_set: 'Element') -> FieldCollectionTransfer:
        field_collection = FieldCollectionTransfer()
        field_collection.set_name(transfer_fields_set.attrib['name'])

        for field_parsed in transfer_fields_set:
            field_name = field_parsed.attrib['name']
            field_type = field_parsed.attrib['type']

            field = FieldTransfer()
            field.set_field_name(field_name)
            field.set_field_type(field_type)

            field_collection.add_field(field)

        return field_collection
