from typing import List, TYPE_CHECKING

import Config.ConfigConstants as ConfigConstants

from Application import Application
from FieldExtractor import FieldExtractor
from FileHandler import FileHandler
from TransferComposer import TransferComposer
from TransferProcessorPlugins import TransferProcessorPlugins

if TYPE_CHECKING:
    from Config.Config import Config
    from TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface


class Factory:
    def __init__(self, config: 'Config'):
        self.__config = config

    def create_application(self):
        return Application(
            self.create_field_extractor(),
            self.create_file_handler(),
            self.create_transfer_composer()
        )

    def create_field_extractor(self) -> FieldExtractor:
        return FieldExtractor()

    def create_file_handler(self) -> FileHandler:
        return FileHandler(
            self.__config.get(ConfigConstants.PATH_INPUT),
            self.__config.get(ConfigConstants.PATH_OUTPUT),
            self.__config.get(ConfigConstants.NAME_ENDING_TRANSFER_XML)
        )

    def create_transfer_composer(self) -> TransferComposer:
        transfer_composer = TransferComposer(
            self.__get_transfer_processor_plugins()
        )

        return transfer_composer

    def __get_transfer_processor_plugins(self) -> List['ProcessorPluginInterface']:
        return TransferProcessorPlugins().get_processor_plugins()
