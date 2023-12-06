from typing import TYPE_CHECKING

from src.TransferProcessorPlugins.ProcessorPluginInterface import ProcessorPluginInterface

if TYPE_CHECKING:
    from src.Transfers.FieldCollectionTransfer import FieldCollectionTransfer


class InfoHeaderProcessorPlugin(ProcessorPluginInterface):
    def process(self, field_collection: 'FieldCollectionTransfer') -> str:
        info_header = ('# This class is auto-generated. Don\'t modify it manually, as any changes you would make,\n'
                       '# would be lost (overwritten) at the next run of the generator.\n'
                       '\n')

        return info_header
