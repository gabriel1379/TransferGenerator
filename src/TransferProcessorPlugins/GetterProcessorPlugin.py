from typing import TYPE_CHECKING

from src.TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface

if TYPE_CHECKING:
    from src.Transfers.FieldTransfer import FieldTransfer
    from src.Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class GetterProcessorPlugin(ProcessorPluginInterface):
    def process(self, field_collection: 'FieldCollectionTransfer') -> str:
        getter_code = ''

        for field in field_collection.get_fields():
            getter_code += self.__create_getter(field)

        return getter_code

    def __create_getter(self, field: 'FieldTransfer') -> str:
        field_name = field.get_field_name()
        field_type = field.get_field_type()

        getter_code = (f'    def get_{field_name}(self) -> {field_type}:\n'
                       f'        return self.__{field_name}\n'
                       f'\n')

        return getter_code
