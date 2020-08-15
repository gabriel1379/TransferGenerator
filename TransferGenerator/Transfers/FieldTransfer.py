class FieldTransfer:
    def __init__(self):
        self.__field_name: str = None
        self.__field_type: str = None

    def set_field_name(self, field_name: str) -> 'FieldTransfer':
        self.__field_name = field_name
        return self

    def set_field_type(self, field_type: str) -> 'FieldTransfer':
        self.__field_type = field_type
        return self

    def get_field_name(self) -> str:
        return self.__field_name

    def get_field_type(self) -> str:
        return self.__field_type
