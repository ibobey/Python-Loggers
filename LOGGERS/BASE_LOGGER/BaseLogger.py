from logging import Logger
from typing import NoReturn
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from os import getenv
import os


class BaseLogger(ABC):
    _FOLDER_NAME: str
    _FILE_NAME: str

    _LOGGER_NAME: str
    _IS_ENV_LOADED: bool
    _LOG_FORMAT: str

    IS_ENV_EXISTS: bool
    logger: Logger

    def __init__(self):
        self.IS_ENV_EXISTS = BaseLogger.__load_env()
        self.__set_const_env()
        BaseLogger.__create_log_folder(folder_name=self._FILE_NAME)

    @staticmethod
    def __load_env() -> bool:
        if load_dotenv() is False:
            return False
        return True

    @staticmethod
    def __create_log_folder(folder_name: str) -> bool:
        if not os.path.exists(f"./{folder_name}"):
            os.makedirs(folder_name)
            return True
        return False

    def __set_const_env(self):
        self._FILE_NAME: str = getenv("LOGS_FILE_NAME", "testLogs")
        self._FOLDER_NAME: str = getenv("LOGS_FOLDER_NAME", "logs")
        self._LOG_FORMAT: str = getenv("LOG_FORMAT", "| %(levelname)s | %(asctime)s | %(name)s | %(message)s")

    @abstractmethod
    def _set_env_variables(self) -> bool:
        pass

    @abstractmethod
    def _setup(self) -> bool:
        pass

    @abstractmethod
    def log(self, message: str) -> NoReturn:
        pass
