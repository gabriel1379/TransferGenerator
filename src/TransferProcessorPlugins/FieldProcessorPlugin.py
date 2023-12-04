from typing import TYPE_CHECKING

from src.TransferProcessorPlugins.TransferProcessorConstants import META_FIELD_MODIFIED_NAME, META_FIELD_MODIFIED_TYPE
from src.TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface

if TYPE_CHECKING:
    from src.Transfers.FieldCollectionTransfer import FieldCollectionTransfer
    from src.Transfers.FieldTransfer import FieldTransfer


class FieldProcessorPlugin(ProcessorPluginInterface):
    def process(self, field_collection: 'FieldCollectionTransfer') -> str:
        field_code = '    def __init__(self):\n'

        for field in field_collection.get_fields():
            field_code += self.__create_field(field)

        field_code += self.__create_modified_meta_field(field_collection)

        field_code += '\n'

        return field_code

    def __create_field(self, field: 'FieldTransfer') -> str:
        field_name = field.get_field_name()
        field_type = field.get_field_type()

        return f'        self.__{field_name}: {field_type} = None\n'

    def __create_modified_meta_field(self, field_collection: 'FieldCollectionTransfer') -> str:
        dict_code = f'        self.__{META_FIELD_MODIFIED_NAME}: {META_FIELD_MODIFIED_TYPE} = '
        dict_code += '{\n'

        for field in field_collection.get_fields():
            dict_code += f'            \'{field.get_field_name()}\': False,\n'

        dict_code += '        }\n'

        return dict_code
