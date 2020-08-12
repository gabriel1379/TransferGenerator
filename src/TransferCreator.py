from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Transfers.TransferBlueprintTransfer import TransferBlueprintTransfer


class TransferCreator:
    def __init__(self, processors):
        self.__processors = processors

    def create_transfer(self, transfer_blueprint: 'TransferBlueprintTransfer') -> str:
        class_code = ''

        for processor in self.__processors:
            class_code += processor.process(transfer_blueprint)

        return class_code
