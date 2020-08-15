from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class TransferComposer:
    def __init__(self, processors):
        self.__processors = processors

    def compose_transfer_code(self, transfer_blueprint: 'FieldCollectionTransfer') -> str:
        class_code = ''

        for processor in self.__processors:
            class_code += processor.process(transfer_blueprint)

        return class_code
