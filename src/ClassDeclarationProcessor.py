from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from TransferBlueprint import TransferBlueprint


class ClassDeclarationProcessor:
    def process(self, transfer_blueprint: 'TransferBlueprint') -> str:
        name = transfer_blueprint.get_name()
        return f'class {name}:\n'
