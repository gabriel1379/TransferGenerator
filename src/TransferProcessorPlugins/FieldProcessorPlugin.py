from typing import TYPE_CHECKING

from src.TransferProcessorPlugins.TransferProcessorConstants import NAME_META_FIELD_MODIFIED
from src.TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface

if TYPE_CHECKING:
    from src.Transfers.FieldCollectionTransfer import FieldCollectionTransfer
    from src.Transfers.FieldTransfer import FieldTransfer


class FieldProcessorPlugin(ProcessorPluginInterface):
    def process(self, field_collection: 'FieldCollectionTransfer') -> str:
        field_code = '    def __init__(self):\n'

        for field in field_collection.get_fields():
            field_code += self.__create_field(field)

        field_code += '\n'

        return field_code

    def __create_field(self, field: 'FieldTransfer') -> str:
        field_name = field.get_field_name()
        field_type = field.get_field_type()
        initial_value = 'None'

        if field_name == NAME_META_FIELD_MODIFIED:
            initial_value = '{}'

        return f'        self.__{field_name}: {field_type} = {initial_value}\n'
