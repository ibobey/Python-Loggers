from typing import NoReturn
from os import getenv
from LOGGERS.BASE_LOGGER.BaseLogger import BaseLogger
import logging


class InfoLogger(BaseLogger):

    def __init__(self):
        super().__init__()
        self._set_env_variables()
        self._setup()

    def _set_env_variables(self) -> bool:
        if self.IS_ENV_EXISTS is not True:
            raise Exception("Cannot find env variables")
        self._LOGGER_NAME = getenv("INFO_LOGGER_NAME", "ErrorLogger")
        return True

    def _setup(self) -> bool:
        self.logger = logging.getLogger(self._LOGGER_NAME)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(self._LOG_FORMAT)
        file_handler = logging.FileHandler(f'{self._FOLDER_NAME}/{self._FILE_NAME}.log')
        self.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        return True

    def log(self, message: str) -> NoReturn:
        self.logger.info(message)
