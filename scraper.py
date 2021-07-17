import requests


class Scraper():
    starttime: str
    endtime: str
    place: str
    verbosityOn: bool

    def __init__(self, starttime, endtime):
        self.starttime = starttime
        self.endtime = endtime

    def get_all_earthquakes(self):

        params = (
            ('starttime', self.starttime),
            ('endtime', self.endtime),
            ('format', 'text')
        )
        response = requests.get(
            'https://webservices.ingv.it/fdsnws/event/1/query', params=params)

        if (response.ok == True):
            return response.text

        else:
            print("Errore!")
            exit(0)

    def get_place_earthquake(self, place):
        data = self.get_all_earthquakes()
