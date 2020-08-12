from TransferBlueprint import TransferBlueprint


class TransferCreator:
    def __init__(self, processors):
        self.__processors = processors

    def create_transfer(self, transfer_blueprint: TransferBlueprint) -> str:
        class_code = ''

        for processor in self.__processors:
            class_code += processor.process(transfer_blueprint)

        return class_code
