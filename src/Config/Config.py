import src.Config.ConfigConstants as ConfigConstants


class Config:
    def __init__(self):
        self.__config: dict = {
            ConfigConstants.INPUT_PATH: 'IN/',
            ConfigConstants.OUTPUT_PATH: 'OUT/',
        }

    def get(self, key: str):
        if key in self.__config:
            return self.__config[key]
