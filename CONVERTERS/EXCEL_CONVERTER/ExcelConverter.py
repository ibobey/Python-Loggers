import pandas as pd
from pandas import DataFrame
from dotenv import load_dotenv
from os import getenv


class LogToExcelConverter:
    __is_file_exists: bool
    __raw_columns: list[str]
    __columns: list[str]
    __raw_data: str
    __data: DataFrame
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    def read_log_file(self) -> bool:
        try:
            with open(self.path, "r") as file:
                self.__raw_data = file.read()
                self.__is_file_exists = True
                print("P1")
                return True

        except FileNotFoundError:
            self.__is_file_exists = False
            return False

        except Exception:
            self.__is_file_exists = False
            return False

    def __convert_raw_data_to_dataframe(self) -> None:
        print("P2")
        test_ = [row.split("|") for row in self.__raw_data.splitlines()]
        columns = ['Type', 'DateTime', 'Logger', 'Message']
        self.__data = pd.DataFrame(test_, columns=columns)

    def __separate_datetime_column(self) -> None:
        print("P3")
        self.__data[["Date", "Time"]] = self.__data["DateTime"].str.split(" ", expand=True)
        self.__data.drop(columns={"DateTime"}, inplace=True)
        self.__data = self.__data[['Type', 'Date', 'Time', 'Logger', 'Message']]

    def convert_dataframe_to_excel(self) -> bool:
        self.__convert_raw_data_to_dataframe()
        self.__separate_datetime_column()
        try:
            print("P4")
            self.__data.to_excel("testAAA.xlsx", engine='xlsxwriter')
            return True
        except Exception as e:
            print(e)
