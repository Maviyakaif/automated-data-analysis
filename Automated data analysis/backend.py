import pandas as pd
from pandas.errors import EmptyDataError, ParserError

filepath = 'D:/CSV files/Netflix Userbase.csv'


def filereader(file):
    try:
        data = pd.read_csv(file)
        return data
    except (EmptyDataError, ParserError):
        pass


if __name__ == "__main__":
    filereader(filepath)
