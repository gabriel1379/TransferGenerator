from pathlib import Path
from typing import List, TYPE_CHECKING
from xml.etree import ElementTree as ET

from src.TransferProcessorPlugins.TransferProcessorConstants import NAME_TRANSFER_CLASS_SUFFIX

if TYPE_CHECKING:
    from xml.etree.ElementTree import Element


class FileHandler:
    def __init__(self, input_path: str, output_path: str):
        self.__input_path: Path = Path(input_path)
        self.__output_path: Path = Path(output_path)

    def load_xml_roots(self) -> List['Element']:
        xml_source_file_paths = self.__scan_for_xmls()
        xml_roots = []

        for xml_source_file_path in xml_source_file_paths:
            xml_roots.append(
                self.__load_xml_root(xml_source_file_path)
            )

        return xml_roots

    def write_out_transfer_code(self, transfer_name: str, transfer_code: str) -> None:
        self.__output_path.mkdir(parents=True, exist_ok=True)

        name_transfer_file = f'{transfer_name}{NAME_TRANSFER_CLASS_SUFFIX}.py'
        with open(self.__output_path.joinpath(name_transfer_file), mode='w') as transfer_target_file:
            transfer_target_file.write(transfer_code)

    def __scan_for_xmls(self) -> List[Path]:
        return sorted(self.__input_path.glob('**/*_transfers.xml'))

    def __load_xml_root(self, input_path: Path) -> 'Element':
        with open(input_path) as transfer_source_file:
            transfer_source_parsed = ET.parse(transfer_source_file)
            root = transfer_source_parsed.getroot()

        return root
