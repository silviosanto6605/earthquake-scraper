# TODO: Scrivere parser per l'output del file principale

import pandas as pd


class Formatter():
    filename: str

    # time = data["Time"].str.split(" ", n = 1, expand = True)

    # making separate first name column from new data frame
    print()

    def __init__(self):
        self.filename = ""

    def format(self):
        data = pd.read_csv("file.txt", "|")
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
            return data[["Time", "Magnitude", "EventLocationName"]]
