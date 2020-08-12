from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Transfers.TransferBlueprintTransfer import TransferBlueprintTransfer


class ClassDeclarationProcessor:
    def process(self, transfer_blueprint: 'TransferBlueprintTransfer') -> str:
        name = transfer_blueprint.get_name()
        return f'class {name}:\n'
