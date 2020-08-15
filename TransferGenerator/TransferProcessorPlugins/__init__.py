from TransferProcessorPlugins.ClassDeclarationProcessorPlugin import ClassDeclarationProcessorPlugin
from TransferProcessorPlugins.FieldProcessorPlugin import FieldProcessorPlugin
from TransferProcessorPlugins.GetterProcessorPlugin import GetterProcessorPlugin
from TransferProcessorPlugins.SetterProcessorPlugin import SetterProcessorPlugin


class TransferProcessorPlugins:
    def get_processor_plugins(self):
        return [
            ClassDeclarationProcessorPlugin(),
            FieldProcessorPlugin(),
            SetterProcessorPlugin(),
            GetterProcessorPlugin(),
        ]
