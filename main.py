from LOGGERS.ErrorLogger import ErrorLogger
from LOGGERS.CriticalLogger import CriticalLogger
from LOGGERS.InfoLogger import InfoLogger
from LOGGERS.WarningLogger import WarningLogger

errorLogger = ErrorLogger()
errorLogger.log(message="this is a test error log 234")

critical_logger = CriticalLogger()
critical_logger.log(message="this is a test log message")


info_logger = InfoLogger()
info_logger.log(message="this is a test info log")

warningLogger = WarningLogger()
warningLogger.log(message="this is a warning test log")
