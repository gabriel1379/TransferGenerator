from typing import List, TYPE_CHECKING

import src.Config.ConfigConstants as ConfigConstants

from src.Application import Application
from src.FieldExtractor import FieldExtractor
from src.FileHandler import FileHandler
from src.MetaFieldAdder import MetaFieldAdder
from src.TransferComposer import TransferComposer
from src.TransferProcessorPlugins.ClassDeclarationProcessorPlugin import ClassDeclarationProcessorPlugin
from src.TransferProcessorPlugins.FieldProcessorPlugin import FieldProcessorPlugin
from src.TransferProcessorPlugins.GetterProcessorPlugin import GetterProcessorPlugin
from src.TransferProcessorPlugins.SetterProcessorPlugin import SetterProcessorPlugin
from src.TransferProcessorPlugins.AdderProcessorPlugin import AdderProcessorPlugin

if TYPE_CHECKING:
    from src.Config.Config import Config
    from src.TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface


class Factory:
    def __init__(self, config: 'Config'):
        self.__config = config

    def create_application(self):
        return Application(
            self.create_field_extractor(),
            self.create_file_handler(),
            self.create_meta_field_adder(),
            self.create_transfer_composer()
        )

    def create_field_extractor(self) -> FieldExtractor:
        return FieldExtractor()

    def create_file_handler(self) -> FileHandler:
        return FileHandler(
            self.__config.get(ConfigConstants.INPUT_PATH),
            self.__config.get(ConfigConstants.OUTPUT_PATH)
        )

    def create_meta_field_adder(self) -> MetaFieldAdder:
        return MetaFieldAdder()

    def create_transfer_composer(self) -> TransferComposer:
        transfer_composer = TransferComposer(
            self.__get_transfer_processor_plugins()
        )

        return transfer_composer

    def __get_transfer_processor_plugins(self) -> List['ProcessorPluginInterface']:
        return [
            ClassDeclarationProcessorPlugin(),
            FieldProcessorPlugin(),
            SetterProcessorPlugin(),
            GetterProcessorPlugin(),
            AdderProcessorPlugin(),
        ]
