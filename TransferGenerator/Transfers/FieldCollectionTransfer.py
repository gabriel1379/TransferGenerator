from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Transfers.FieldTransfer import FieldTransfer


class FieldCollectionTransfer:
    def __init__(self):
        self.__name: str = ''
        self.__fields: List['FieldTransfer'] = []

    def add_field(self, field: 'FieldTransfer') -> None:
        self.__fields.append(field)

    def get_fields(self) -> List['FieldTransfer']:
        return self.__fields

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name
