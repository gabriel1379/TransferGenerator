from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Transfers.FieldCollectionTransfer import FieldCollectionTransfer
    from TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface


class TransferComposer:
    def __init__(self, processors: List['ProcessorPluginInterface']):
        self.__processors: List['ProcessorPluginInterface'] = processors

    def compose_transfer_code(self, transfer_blueprint: 'FieldCollectionTransfer') -> str:
        class_code = ''

        for processor in self.__processors:
            class_code += processor.process(transfer_blueprint)

        return class_code
