from LOGGERS.ErrorLogger import ErrorLogger
from LOGGERS.CriticalLogger import CriticalLogger
from LOGGERS.InfoLogger import InfoLogger
from LOGGERS.WarningLogger import WarningLogger


warningLogger = WarningLogger()
warningLogger.log(message="this is a warning test log")

infoLogger = InfoLogger()
infoLogger.log(message="Test info")

criticalLogger = CriticalLogger()
criticalLogger.log(message="test critical log")

errorLogger = ErrorLogger()
errorLogger.log(message="test errror message")