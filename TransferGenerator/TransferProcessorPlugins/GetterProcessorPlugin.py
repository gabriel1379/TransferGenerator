from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Transfers.FieldTransfer import FieldTransfer
    from Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class GetterProcessorPlugin:
    def process(self, transfer_blueprint: 'FieldCollectionTransfer') -> str:
        getter_code = ''

        for field in transfer_blueprint.get_fields():
            getter_code += self.__create_getter(field)

        return getter_code

    def __create_getter(self, field: 'FieldTransfer') -> str:
        field_name = field.get_field_name()
        field_type = field.get_field_type()

        getter_code = (f'    def get_{field_name}(self) -> {field_type}:\n'
                       f'        return self.__{field_name}\n'
                       f'\n')

        return getter_code
