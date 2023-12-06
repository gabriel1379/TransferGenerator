from argparse import ArgumentParser
from typing import List, TYPE_CHECKING

from src.Application import Application
from src.ArgumentHandler import ArgumentHandler
from src.FieldExtractor import FieldExtractor
from src.FileHandler import FileHandler
from src.TransferComposer import TransferComposer
from src.TransferProcessorPlugins.AdderProcessorPlugin import AdderProcessorPlugin
from src.TransferProcessorPlugins.ClassDeclarationProcessorPlugin import ClassDeclarationProcessorPlugin
from src.TransferProcessorPlugins.FieldProcessorPlugin import FieldProcessorPlugin
from src.TransferProcessorPlugins.GetterProcessorPlugin import GetterProcessorPlugin
from src.TransferProcessorPlugins.InfoHeaderProcessorPlugin import InfoHeaderProcessorPlugin
from src.TransferProcessorPlugins.IsModifiedProcessorPlugin import IsModifiedProcessorPlugin
from src.TransferProcessorPlugins.SetterProcessorPlugin import SetterProcessorPlugin

if TYPE_CHECKING:
    from src.Config.Config import Config
    from src.TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface


class Factory:
    def __init__(self, config: 'Config'):
        self.__config = config

    def create_application(self):
        return Application(
            self.create_arg_handler(),
            self.create_field_extractor(),
            self.create_file_handler(),
            self.create_transfer_composer()
        )

    def create_arg_handler(self) -> ArgumentHandler:
        return ArgumentHandler(self.create_arg_parser())

    def create_arg_parser(self) -> ArgumentParser:
        return ArgumentParser()

    def create_field_extractor(self) -> FieldExtractor:
        return FieldExtractor()

    def create_file_handler(self) -> FileHandler:
        return FileHandler(self.__config)

    def create_transfer_composer(self) -> TransferComposer:
        transfer_composer = TransferComposer(
            self.__get_transfer_processor_plugins()
        )

        return transfer_composer

    def __get_transfer_processor_plugins(self) -> List['ProcessorPluginInterface']:
        return [
            InfoHeaderProcessorPlugin(),
            ClassDeclarationProcessorPlugin(),
            FieldProcessorPlugin(),
            SetterProcessorPlugin(),
            GetterProcessorPlugin(),
            AdderProcessorPlugin(),
            IsModifiedProcessorPlugin(),
        ]
