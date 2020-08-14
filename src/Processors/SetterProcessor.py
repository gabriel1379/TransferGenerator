from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Transfers.FieldTransfer import FieldTransfer
    from Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class SetterProcessor:
    def process(self, transfer_blueprint: 'FieldCollectionTransfer') -> str:
        setter_code = ''
        class_name = transfer_blueprint.get_name()

        for field in transfer_blueprint.get_fields():
            setter_code += self.__create_setter(field, class_name)

        return setter_code

    def __create_setter(self, field: 'FieldTransfer', class_name: str) -> str:
        field_name = field.get_field_name()
        field_type = field.get_field_type()

        setter_code = (f'    def set_{field_name}(self, {field_name}: {field_type}) -> \'{class_name}\':\n'
                       f'        self.__{field_name} = {field_name}\n'
                       f'        return self\n'
                       f'\n')

        return setter_code
