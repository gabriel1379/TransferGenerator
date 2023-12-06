from typing import TYPE_CHECKING

from src.TransferProcessorPlugins.TransferProcessorConstants import META_FIELD_MODIFIED_NAME, NAME_TRANSFER_CLASS_SUFFIX
from src.TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface

if TYPE_CHECKING:
    from src.Transfers.FieldTransfer import FieldTransfer
    from src.Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class SetterProcessorPlugin(ProcessorPluginInterface):
    def process(self, field_collection: 'FieldCollectionTransfer') -> str:
        setter_code = ''
        class_name = field_collection.get_name() + NAME_TRANSFER_CLASS_SUFFIX

        for field in field_collection.get_fields():
            if field.get_field_name() == META_FIELD_MODIFIED_NAME:
                continue

            setter_code += self.__create_setter(field, class_name)

        return setter_code

    def __create_setter(self, field: 'FieldTransfer', class_name: str) -> str:
        field_name = field.get_field_name()
        field_type = field.get_field_type()

        setter_code = (f'    def set_{field_name}(self, {field_name}: {field_type}) -> \'{class_name}\':\n'
                       f'        self.__{field_name} = {field_name}\n'
                       f'        self.__modified[\'{field_name}\'] = True\n'
                       f'\n'
                       f'        return self\n'
                       f'\n')

        return setter_code
