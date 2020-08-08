from typing import List
import xml.etree.ElementTree as ET


class Field:
    def __init__(self):
        self.__field_name: str = ''
        self.__field_type: str = ''

    def set_field_name(self, field_name: str) -> 'Field':
        self.__field_name = field_name
        return self

    def set_field_type(self, field_type: str) -> 'Field':
        self.__field_type = field_type
        return self

    def get_field_name(self) -> str:
        return self.__field_name

    def get_field_type(self) -> str:
        return self.__field_type


class TransferBlueprint:
    def __init__(self):
        self.__name: str = ''
        self.__fields: List[Field] = []

    def add_field(self, field: Field) -> None:
        self.__fields.append(field)

    def get_fields(self) -> List[Field]:
        return self.__fields

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name


class TransferCreator:
    def create_transfer(self, transfer_blueprint: TransferBlueprint) -> str:
        class_code = self.__create_class_declaration(transfer_blueprint)
        class_code += self.__create_fields(transfer_blueprint)
        class_code += self.__create_setters(transfer_blueprint)
        class_code += self.__create_getters(transfer_blueprint)

        return class_code

    def __create_class_declaration(self, transfer_blueprint: TransferBlueprint) -> str:
        name = transfer_blueprint.get_name()
        return f'class {name}:\n'

    def __create_fields(self, transfer_blueprint: TransferBlueprint) -> str:
        field_code = '    def __init__(self):\n'

        for field in transfer_blueprint.get_fields():
            field_code += self.__create_field(field)

        field_code += '\n'

        return field_code

    def __create_field(self, field: Field) -> str:
        field_name = field.get_field_name()
        field_type = field.get_field_type()

        return f'        self.__{field_name}: {field_type}\n'

    def __create_setters(self, transfer_blueprint: TransferBlueprint):
        setter_code = ''
        class_name = transfer_blueprint.get_name()

        for field in transfer_blueprint.get_fields():
            setter_code += self.__create_setter(field, class_name)

        return setter_code

    def __create_setter(self, field: Field, class_name: str):
        field_name = field.get_field_name()
        field_type = field.get_field_type()

        setter_code = (f'    def set_{field_name}(self, {field_name}: {field_type}) -> \'{class_name}\':\n'
                       f'        self.__{field_name} = {field_name}\n'
                       f'        return self\n'
                       f'\n')

        return setter_code

    def __create_getters(self, transfer_blueprint: TransferBlueprint):
        getter_code = ''

        for field in transfer_blueprint.get_fields():
            getter_code += self.__create_getter(field)

        return getter_code

    def __create_getter(self, field: Field):
        field_name = field.get_field_name()
        field_type = field.get_field_type()

        getter_code = (f'    def get_{field_name}(self) -> {field_type}:\n'
                       f'        return self.__{field_name}\n'
                       f'\n')

        return getter_code


with open('sample.xml') as transfer_source_file:
    transfer_source_parsed = ET.parse(transfer_source_file)

root = transfer_source_parsed.getroot()
print(root.tag)
print(root.attrib)

transfer_blueprint = TransferBlueprint()
transfer_blueprint.set_name(root.attrib['name'])

for field_parsed in root:
    field_name = field_parsed.attrib['name']
    field_type = field_parsed.attrib['type']

    field = Field()
    field.set_field_name(field_name)
    field.set_field_type(field_type)

    transfer_blueprint.add_field(field)

transfer_creator = TransferCreator()

with open('SampleTransfer.py', mode='w') as transfer_target_file:
    transfer_target_file.write(transfer_creator.create_transfer(transfer_blueprint))

print('Done.')
