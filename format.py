import warnings

import pandas as pd

warnings.filterwarnings('ignore')


class Formatter:

    filename: str
    verbosity: bool
    place: str
    verbosity = False
    place = None

    def __init__(self):
        self.filename = ""
        self.verbosity = False
        self.place = None

    def format(self):

        def find(df, self, place):
            data = pd.read_csv("out.txt", "|")
            data = pd.DataFrame(data)
            data[['Date', 'Time']] = data.Time.str.split("T", expand=True)
            with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
                return data.loc[data["EventLocationName"].str.contains(self.place)]

        if not self.verbosity:
            data = pd.read_csv("out.txt", "|")
            data = pd.DataFrame(data)
            data[['Date', 'Time']] = data.Time.str.split("T", expand=True)
            with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
                return data[["Date", "Time", "Magnitude", "EventLocationName"]]

        elif self.verbosity:
            data = pd.read_csv("out.txt", "|")
            with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
                return data

        if(self.place != None):
            return find(self.place)

        else:
            pass


