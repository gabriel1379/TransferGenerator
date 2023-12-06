from src.Config.Exceptions.ConfigKeyNotFoundException import ConfigKeyNotFoundException
import src.FileHandlerConstants as FileHandlerConstants


class Config:
    def __init__(self):
        self.__config: dict = {
            FileHandlerConstants.INPUT_PATH_DEFAULT: 'IN/',
            FileHandlerConstants.OUTPUT_PATH_DEFAULT: 'OUT/',
        }

    def get(self, key: str):
        if key not in self.__config:
            raise ConfigKeyNotFoundException

        return self.__config[key]
