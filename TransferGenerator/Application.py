from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from FieldExtractor import FieldExtractor
    from FileHandler import FileHandler
    from TransferComposer import TransferComposer


class Application:
    def __init__(
            self,
            field_extractor: 'FieldExtractor',
            file_handler: 'FileHandler',
            transfer_composer: 'TransferComposer'
    ):
        self.__field_extractor: 'FieldExtractor' = field_extractor
        self.__file_handler: 'FileHandler' = file_handler
        self.__transfer_composer: 'TransferComposer' = transfer_composer

    def generate_transfers(self) -> None:
        xml_roots = self.__file_handler.load_xml_roots()

        for xml_root in xml_roots:
            for transfer_fields_set in xml_root:
                field_collection = self.__field_extractor.extract_fields(transfer_fields_set)
                transfer_code = self.__transfer_composer.compose_transfer_code(field_collection)
                self.__file_handler.write_out_transfer_code(field_collection.get_name(), transfer_code)
