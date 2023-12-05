from pathlib import Path
from typing import List, TYPE_CHECKING
from xml.etree import ElementTree as ET

from src.Exceptions.InvalidPathException import InvalidPathException
from src.Exceptions.NoXMLsFoundException import NoXMLsFoundException
from src.FileHandlerConstants import INPUT_PATH_DEFAULT, OUTPUT_PATH_DEFAULT
from src.TransferProcessorPlugins.TransferProcessorConstants import NAME_TRANSFER_CLASS_SUFFIX

if TYPE_CHECKING:
    from xml.etree.ElementTree import Element

    from src.Config.Config import Config


class FileHandler:
    def __init__(self, config: 'Config'):
        self.__config: Config = config

    def load_xml_roots(self, custom_path: str = None) -> List['Element']:
        input_path = Path(self.__config.get(INPUT_PATH_DEFAULT))

        if custom_path is not None:
            input_path = Path(custom_path)

        if not input_path.exists():
            raise InvalidPathException(f"The provided input path '{input_path}' does not exist. Please check and try again.")

        xml_source_file_paths = self.__scan_for_xmls(input_path)
        if len(xml_source_file_paths) == 0:
            raise NoXMLsFoundException(f"No files ending in '_transfers.xml' could be found at the provided location '{input_path}'. Please check and try again.")

        xml_roots = []
        for xml_source_file_path in xml_source_file_paths:
            xml_roots.append(
                self.__load_xml_root(xml_source_file_path)
            )

        return xml_roots

    def write_out_transfer_code(self, transfer_name: str, transfer_code: str, custom_path: str = None) -> None:
        output_path = Path(self.__config.get(OUTPUT_PATH_DEFAULT))

        if custom_path is not None:
            output_path = Path(custom_path)

        output_path.mkdir(parents=True, exist_ok=True)

        name_transfer_file = f'{transfer_name}{NAME_TRANSFER_CLASS_SUFFIX}.py'
        with open(output_path.joinpath(name_transfer_file), mode='w') as transfer_target_file:
            transfer_target_file.write(transfer_code)

    def __scan_for_xmls(self, input_path: Path) -> List[Path]:
        return sorted(input_path.glob('**/*_transfers.xml'))

    def __load_xml_root(self, input_path: Path) -> 'Element':
        with open(input_path) as transfer_source_file:
            transfer_source_parsed = ET.parse(transfer_source_file)
            root = transfer_source_parsed.getroot()

        return root
