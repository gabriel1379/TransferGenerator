from Application import Application
from FieldExtractor import FieldExtractor
from FileHandler import FileHandler
from TransferComposer import TransferComposer
from TransferProcessorPlugins import TransferProcessorPlugins


class Factory:
    def create_application(self):
        return Application(
            self.create_field_extractor(),
            self.create_file_handler(),
            self.create_transfer_composer()
        )

    def create_field_extractor(self) -> FieldExtractor:
        return FieldExtractor()

    def create_file_handler(self) -> FileHandler:
        return FileHandler()

    def create_transfer_composer(self) -> TransferComposer:
        transfer_creator = TransferComposer(
            self.__get_transfer_processor_plugins()
        )

        return transfer_creator

    def __get_transfer_processor_plugins(self) -> list:
        return TransferProcessorPlugins().get_processor_plugins()