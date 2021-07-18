import warnings

import pandas as pd

warnings.filterwarnings('ignore')


class Formatter:
    filename: str
    verbosity: bool
    place: str
    verbosity = False
    place = None
    data = None

    def __init__(self):
        self.filename = ""
        self.verbosity = False
        self.place = None

    def format(self):
        data = pd.read_csv("out.txt", "|")
        data = pd.DataFrame(data)

        def find(place):
            data[['Date', 'Time']] = data.Time.str.split("T", expand=True)
            with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
                if(self.verbosity):
                    return data.loc[data["EventLocationName"].str.contains(place)]
                elif(not self.verbosity):
                    #data.drop(columns=["#EventID","Latitude","Longitude","Depth/Km","Author","Catalog","Contributor","MagType","MagAuthor"])
                    out = data.loc[data["EventLocationName"].str.contains(place)]
                    return out[["Date", "Time", "Magnitude", "EventLocationName"]]

        if not self.verbosity:
            '''Se l'output non è verboso'''

            if (self.place != None):
                return find(self.place)

            else:
                data[['Date', 'Time']] = data.Time.str.split("T", expand=True)
                with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth',
                                       None):
                    return data[["Date", "Time", "Magnitude", "EventLocationName"]] # ritorna solo alcune colonne

        elif self.verbosity:
            '''Se l'output è verboso'''
            if (self.place != None):
                return find(self.place)

            else:
                with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth',
                                       None):
                    return data #ritorna tutti i dati
