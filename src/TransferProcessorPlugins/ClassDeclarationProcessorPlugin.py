from typing import TYPE_CHECKING

from src.TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface
from src.TransferProcessorPlugins.TransferProcessorConstants import NAME_TRANSFER_CLASS_SUFFIX

if TYPE_CHECKING:
    from src.Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class ClassDeclarationProcessorPlugin(ProcessorPluginInterface):
    def process(self, field_collection: 'FieldCollectionTransfer') -> str:
        name = field_collection.get_name()

        return f'class {name}{NAME_TRANSFER_CLASS_SUFFIX}:\n'
