import Config.ConfigConstants as ConfigConstants


class Config:
    def __init__(self):
        self.__config: dict = {
            ConfigConstants.PATH_INPUT: 'IN/',
            ConfigConstants.PATH_OUTPUT: 'OUT/',
            ConfigConstants.NAME_ENDING_TRANSFER_XML: '_transfer'
        }

    def get(self, key: str):
        if key in self.__config:
            return self.__config[key]
