from pathlib import Path
from typing import List, TYPE_CHECKING
from xml.etree import ElementTree as ET

if TYPE_CHECKING:
    from xml.etree.ElementTree import Element


class FileHandler:
    def __init__(self, input_path: str, output_path: str, name_ending: str):
        self.__path_input: Path = Path(input_path)
        self.__path_output: Path = Path(output_path)
        self.__name_ending: str = name_ending

    def load_xml_roots(self) -> List['Element']:
        xml_source_file_paths = self.__scan_for_xmls()
        xml_roots = []

        for xml_source_file_path in xml_source_file_paths:
            xml_roots.append(
                self.__load_xml_root(xml_source_file_path)
            )

        return xml_roots

    def write_out_transfer_code(self, transfer_name: str, transfer_code: str) -> None:
        with open(self.__path_output.joinpath(f'{transfer_name}.py'), mode='w') as transfer_target_file:
            transfer_target_file.write(transfer_code)

    def __scan_for_xmls(self) -> List[Path]:
        return sorted(self.__path_input.glob(f'**/*{self.__name_ending}.xml'))

    def __load_xml_root(self, input_path: Path) -> 'Element':
        with open(input_path) as transfer_source_file:
            transfer_source_parsed = ET.parse(transfer_source_file)
            root = transfer_source_parsed.getroot()

        return root
