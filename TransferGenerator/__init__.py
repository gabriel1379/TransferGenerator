from Factory import Factory


class TransferGenerator:
    def __init__(self):
        self.__factory: Factory = None

    def generate_transfers(self) -> None:
        self.__boot()

        app = self.__factory.create_application()

        app.generate_transfers()

    def __boot(self) -> None:
        if self.__is_booted():
            return

        self.__factory = Factory()

    def __is_booted(self) -> bool:
        return self.__factory is not None
