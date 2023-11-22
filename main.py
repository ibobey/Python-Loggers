from LOGGERS.MainLogger import MainLogger
from LOGGERS.ErrorLogger import ErrorLogger

logger = MainLogger("testLogger")
logger.log_info("sel123am")
logger.log_warning("war123213ning")
logger.log_critical("selam am123123ca")
logger.log_error("errorree123")


err = ErrorLogger("errorLoggger")
err.log_error(message="test error")

