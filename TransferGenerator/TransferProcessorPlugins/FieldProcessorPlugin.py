from typing import TYPE_CHECKING

from TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface

if TYPE_CHECKING:
    from Transfers.FieldCollectionTransfer import FieldCollectionTransfer
    from Transfers.FieldTransfer import FieldTransfer


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

        return f'        self.__{field_name}: {field_type} = None\n'
