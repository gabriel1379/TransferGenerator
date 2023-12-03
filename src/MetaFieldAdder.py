from typing import TYPE_CHECKING

from src.Transfers.FieldTransfer import FieldTransfer

if TYPE_CHECKING:
    from Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class MetaFieldAdder:
    def add_meta_field_modified(self, field_collection: 'FieldCollectionTransfer') -> 'FieldCollectionTransfer':
        field_modified = FieldTransfer().set_field_name('modified').set_field_type('dict')
        field_collection.add_field(field_modified)

        return field_collection
