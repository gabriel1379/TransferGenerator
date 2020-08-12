from TransferBlueprint import TransferBlueprint


class ClassDeclarationProcessor:
    def process(self, transfer_blueprint: TransferBlueprint) -> str:
        name = transfer_blueprint.get_name()
        return f'class {name}:\n'
