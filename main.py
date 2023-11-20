from LOGGERS.MainLogger import MainLogger
from LOGGERS.ErrorLogger import ErrorLogger

mainLogger = MainLogger()
mainLogger.log(message="test message 2")

errorLogger = ErrorLogger()
errorLogger.log(message="this is a test error log !")
