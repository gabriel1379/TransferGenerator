from typing import TYPE_CHECKING

from src.TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface
from src.TransferProcessorPlugins.TransferProcessorConstants import META_FIELD_MODIFIED_NAME

if TYPE_CHECKING:
    from src.Transfers.FieldTransfer import FieldTransfer
    from src.Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class IsModifiedProcessorPlugin(ProcessorPluginInterface):
    def process(self, field_collection: 'FieldCollectionTransfer') -> str:
        is_modified_code = ''

        for field in field_collection.get_fields():
            is_modified_code += self.__create_is_modified(field)

        return is_modified_code

    def __create_is_modified(self, field: 'FieldTransfer') -> str:
        field_name = field.get_field_name()

        is_modified_code = (f'    def is_modified_{field_name}(self) -> bool:\n'
                       f'        return self.__{META_FIELD_MODIFIED_NAME}.get(\'{field_name}\')\n'
                       f'\n')

        return is_modified_code
