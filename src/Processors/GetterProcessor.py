from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Field import Field
    from Transfers.TransferBlueprintTransfer import TransferBlueprintTransfer


class GetterProcessor:
    def process(self, transfer_blueprint: 'TransferBlueprintTransfer'):
        getter_code = ''

        for field in transfer_blueprint.get_fields():
            getter_code += self.__create_getter(field)

        return getter_code

    def __create_getter(self, field: 'Field'):
        field_name = field.get_field_name()
        field_type = field.get_field_type()

        getter_code = (f'    def get_{field_name}(self) -> {field_type}:\n'
                       f'        return self.__{field_name}\n'
                       f'\n')

        return getter_code