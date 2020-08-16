from typing import TYPE_CHECKING

from TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface

if TYPE_CHECKING:
    from Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class ClassDeclarationProcessorPlugin(ProcessorPluginInterface):
    def process(self, transfer_blueprint: 'FieldCollectionTransfer') -> str:
        name = transfer_blueprint.get_name()
        return f'class {name}:\n'
