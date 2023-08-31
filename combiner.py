import datetime
import re
import pandas as pd


def convertDate(date: str):
  # return datetime.datetime object from string parameter
  parts = re.split('\W', date)
  return datetime.datetime(year = int(parts[0]), month = int(parts[1]), day = int(parts[2]))

def combine():
    dfMajor = pd.concat([
                    pd.read_csv('/Users/user/Projects/196124/VNP/RawData/GoogleNews_Microsoft_2018-03-24_2019-01-28.csv'),
                    pd.read_csv('/Users/user/Projects/196124/VNP/RawData/GoogleNews_Microsoft_2019-01-28_2019-08-01.csv'),
                    pd.read_csv('/Users/user/Projects/196124/VNP/RawData/GoogleNews_Microsoft_2019-08-01_2023-08-01.csv')
                     ],
                    ignore_index=True)
    dfMajor = dfMajor.sort_values(by = ['Date'], ascending=False)
    dfMajor = dfMajor[dfMajor['Date'].apply(convertDate) < datetime.datetime(2023, 3, 1)]
    dfMajor.drop_duplicates(inplace=True)
    dfMajor = dfMajor.reset_index(drop=True)
    dfMajor.to_csv('/Users/user/Projects/196124/VNP/RawData/GoogleNews_Microsoft_2018-03-24_2022-03-24.csv', index=False)


if __name__ =="__main__":
  combine()