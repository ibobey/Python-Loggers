from LOGGERS.BASE_LOGGER.BaseLogger import BaseLogger
from typing import NoReturn
from os import getenv
import logging


class MainLogger(BaseLogger):

    logger: logging.Logger

    def __init__(self):
        self._IS_ENV_LOADED = super().load_env()
        self._set_env_variables()
        super().create_log_folder(folder_name=self._FOLDER_NAME)
        self._setup()

    def _set_env_variables(self) -> bool:
        if self._IS_ENV_LOADED is not True:
            raise Exception("env files cannot detected!")
        self._FOLDER_NAME = getenv("LOGS_FOLDER_NAME", "logs")
        self._LOGGER_NAME = getenv("LOGGER_NAME", "mainLogger")
        self._FILE_NAME = getenv("LOGGER_FILE_NAME", "mainLogs")
        return True

    def _setup(self) -> bool:
        self.logger = logging.getLogger(self._LOGGER_NAME)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('* %(levelname)s | %(asctime)s | %(name)s | %(message)s')
        file_handler = logging.FileHandler(f'{self._FOLDER_NAME}/{self._FILE_NAME}.log')

        self.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)

        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        return True

    def log(self, message: str) -> NoReturn:
        self.logger.info(message)
