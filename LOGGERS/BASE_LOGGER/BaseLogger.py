from typing import NoReturn
from abc import ABC, abstractmethod
from dotenv import load_dotenv
import os


class BaseLogger(ABC):

    _IS_ENV_LOADED: bool
    _FOLDER_NAME: str
    _LOGGER_NAME: str

    @staticmethod
    def load_env() -> bool:
        if load_dotenv() is False:
            return False
        return True

    @staticmethod
    def create_log_folder(folder_name: str) -> bool:
        if not os.path.exists(f"./{folder_name}"):
            os.makedirs(folder_name)
            return True
        return False

    @abstractmethod
    def _set_env_variables(self) -> bool:
        pass

    @abstractmethod
    def _setup(self) -> bool:
        pass

    @abstractmethod
    def _log(self, message: str) -> NoReturn:
        pass
