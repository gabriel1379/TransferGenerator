from typing import TYPE_CHECKING
from xml.etree import ElementTree as ET

if TYPE_CHECKING:
    from xml.etree.ElementTree import Element


class FileHandler:
    def __init__(self, input_path: str, output_path: str):
        self.__input_path = input_path
        self.__output_path = output_path

    def load_xml_root(self) -> 'Element':
        with open(f'{self.__input_path}sample.xml') as transfer_source_file:
            transfer_source_parsed = ET.parse(transfer_source_file)
            root = transfer_source_parsed.getroot()

        return root

    def write_out_transfer_code(self, transfer_name: str, transfer_code: str) -> None:
        with open(f'{self.__output_path}{transfer_name}.py', mode='w') as transfer_target_file:
            transfer_target_file.write(transfer_code)
