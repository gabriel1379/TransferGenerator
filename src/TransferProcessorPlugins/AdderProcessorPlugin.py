from typing import TYPE_CHECKING

from src.TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface
from src.TransferProcessorPlugins.TransferProcessorConstants import NAME_TRANSFER_CLASS_SUFFIX

if TYPE_CHECKING:
    from src.Transfers.FieldTransfer import FieldTransfer
    from src.Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class AdderProcessorPlugin(ProcessorPluginInterface):
    def process(self, field_collection: 'FieldCollectionTransfer') -> str:
        adder_code = ''
        class_name = field_collection.get_name() + NAME_TRANSFER_CLASS_SUFFIX

        for field in field_collection.get_fields():
            if field.get_field_type() == 'dict':
                adder_code += self.__create_dict_adder(field, class_name)

            if field.get_field_type() == 'list':
                adder_code += self.__create_list_adder(field, class_name)

        return adder_code

    def __create_dict_adder(self, field: 'FieldTransfer', class_name: str) -> str:
        field_name = field.get_field_name()
        field_type = field.get_field_type()

        adder_code = (f'    def add_{field_name}(self, key: str, {field_name}: {field_type}) -> \'{class_name}\':\n'
                       f'        self.__{field_name}[key] = {field_name}\n'
                       '\n'
                       f'        return self\n'
                       f'\n')

        return adder_code

    def __create_list_adder(self, field: 'FieldTransfer', class_name: str) -> str:
        field_name = field.get_field_name()
        field_type = field.get_field_type()

        adder_code = (f'    def add_{field_name}(self, {field_name}: {field_type}) -> \'{class_name}\':\n'
                       f'        self.__{field_name}.append({field_name})\n'
                       '\n'
                       f'        return self\n'
                       f'\n')

        return adder_code
