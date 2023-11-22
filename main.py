from LOGGERS.MainLogger import MainLogger
from LOGGERS.ErrorLogger import ErrorLogger
from CONVERTERS.EXCEL_CONVERTER.ExcelConverter import LogToExcelConverter
logger = MainLogger("testLogger")
logger.log_info("sel123am")
logger.log_warning("war123213ning")
logger.log_critical("selam am123123ca")
logger.log_error("errorree123")


err = ErrorLogger("errorLoggger")
err.log_error(message="test error")

converter = LogToExcelConverter(path=r"C:\Users\ibrah\OneDrive\Masaüstü\MyActiveProjects\Loggers\Python-Loggers\logs\server_logs.log")
converter.read_log_file()
converter.convert_dataframe_to_excel()