from typing import TYPE_CHECKING
from xml.etree import ElementTree as ET

if TYPE_CHECKING:
    from xml.etree.ElementTree import Element

from Processors import Processors

from Transfers.FieldTransfer import FieldTransfer
from Transfers.FieldCollectionTransfer import FieldCollectionTransfer
from TransferComposer import TransferComposer


class TransferGenerator:
    def generate_transfers(self):
        xml_root = self.__load_xml_root()

        for transfer_fields_set in xml_root:
            field_collection = self.__extract_fields(transfer_fields_set)
            transfer_code = self.__compose_transfer_code(field_collection)
            self.__write_out_transfer_code(field_collection.get_name(), transfer_code)

        print('Done.')

    def __load_xml_root(self) -> 'Element':
        with open('../IN/sample.xml') as transfer_source_file:
            transfer_source_parsed = ET.parse(transfer_source_file)
            root = transfer_source_parsed.getroot()

        return root

    def __extract_fields(self, transfer_fields_set: 'Element') -> FieldCollectionTransfer:
        field_collection = FieldCollectionTransfer()
        field_collection.set_name(transfer_fields_set.attrib['name'])

        for field_parsed in transfer_fields_set:
            field_name = field_parsed.attrib['name']
            field_type = field_parsed.attrib['type']

            field = FieldTransfer()
            field.set_field_name(field_name)
            field.set_field_type(field_type)

            field_collection.add_field(field)

        return field_collection

    def __create_transfer_creator(self) -> TransferComposer:
        processors = Processors()
        transfer_creator = TransferComposer(
            processors.get_processors()
        )

        return transfer_creator

    def __compose_transfer_code(self, field_collection: FieldCollectionTransfer) -> str:
        transfer_composer = self.__create_transfer_creator()

        return transfer_composer.compose_transfer_code(field_collection)

    def __write_out_transfer_code(self, transfer_name: str, transfer_code: str) -> None:
        with open(f'../OUT/{transfer_name}.py', mode='w') as transfer_target_file:
            transfer_target_file.write(transfer_code)


transferGenerator = TransferGenerator()
transferGenerator.generate_transfers()
