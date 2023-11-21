from os import getenv
from LOGGERS.BASE_LOGGER.BaseLogger import BaseLogger
import logging


class WarningLogger(BaseLogger):

    def __init__(self):
        super().__init__()
        self._set_env_vars()
        self._setup()

    def _set_env_vars(self) -> bool:
        if self.IS_ENV_EXISTS is not True:
            raise Exception("Cannot find env variables")
        self._LOGGER_NAME = getenv("WARNING_LOGGER_NAME", "WarningLogger")
        return True

    def _setup(self) -> None:
        self.logger = logging.getLogger(self._LOGGER_NAME)
        self.logger.setLevel(logging.WARNING)
        formatter = logging.Formatter(self._LOG_FORMAT)
        file_handler = logging.FileHandler(f'{self._FOLDER_NAME}/{self._FILE_NAME}.log')
        self.logger.setLevel(logging.WARNING)
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log(self, message: str) -> None:
        self.logger.warning(message)
