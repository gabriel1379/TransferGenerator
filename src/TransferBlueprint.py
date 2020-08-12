from typing import List

from Field import Field


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
