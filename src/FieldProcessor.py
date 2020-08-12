from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from TransferBlueprint import TransferBlueprint
    from Field import Field


class FieldProcessor:
    def process(self, transfer_blueprint: 'TransferBlueprint') -> str:
        field_code = '    def __init__(self):\n'

        for field in transfer_blueprint.get_fields():
            field_code += self.__create_field(field)

        field_code += '\n'

        return field_code

    def __create_field(self, field: 'Field') -> str:
        field_name = field.get_field_name()
        field_type = field.get_field_type()

        return f'        self.__{field_name}: {field_type} = None\n'
