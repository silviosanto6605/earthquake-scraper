import warnings

import pandas as pd

warnings.filterwarnings('ignore')


class Formatter():
    filename: str
    verbosity: bool

    verbosity = False

    # making separate first name column from new data frame
    print()

    def __init__(self):
        self.filename = ""
        self.verbosity = False

    def format(self):

        if(self.verbosity == False):
            data = pd.read_csv("out.txt", "|")
            data = pd.DataFrame(data)
            data[['Date', 'Time']] = data.Time.str.split("T", expand=True)
            with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
                return data[["Date", "Time", "Magnitude", "EventLocationName"]]

        elif(self.verbosity == True):
            data = pd.read_csv("out.txt", "|")
            with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
                return data

