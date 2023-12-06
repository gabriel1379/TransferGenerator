from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.ArgumentHandler import ArgumentHandler
    from src.FieldExtractor import FieldExtractor
    from src.FileHandler import FileHandler
    from src.TransferComposer import TransferComposer


class Application:
    def __init__(
            self,
            arg_handler: 'ArgumentHandler',
            field_extractor: 'FieldExtractor',
            file_handler: 'FileHandler',
            transfer_composer: 'TransferComposer'
    ):
        self.__arg_handler: 'ArgumentHandler' = arg_handler
        self.__field_extractor: 'FieldExtractor' = field_extractor
        self.__file_handler: 'FileHandler' = file_handler
        self.__transfer_composer: 'TransferComposer' = transfer_composer

    def generate_transfers(self) -> None:
        xml_roots = self.__file_handler.load_xml_roots(
            self.__arg_handler.get_input()
        )

        for xml_root in xml_roots:
            for transfer_fields_set in xml_root:
                field_collection = self.__field_extractor.extract_fields(transfer_fields_set)
                transfer_code = self.__transfer_composer.compose_transfer_code(field_collection)
                self.__file_handler.write_out_transfer_code(field_collection.get_name(), transfer_code, self.__arg_handler.get_output())
