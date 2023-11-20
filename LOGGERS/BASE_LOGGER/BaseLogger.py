from typing import NoReturn
from abc import ABC, abstractmethod
from dotenv import load_dotenv


class BaseLogger(ABC):

    @staticmethod
    def load_env() -> bool:
        if load_dotenv() is False:
            return False
        return True

    @abstractmethod
    def _set_env_variables(self) -> bool:
        pass

    @abstractmethod
    def _setup(self) -> bool:
        pass

    @abstractmethod
    def _log(self, message: str) -> NoReturn:
        pass



