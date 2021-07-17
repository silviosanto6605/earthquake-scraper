import requests
import argparse

import parser


class Scraper():
    
    parser = argparse.ArgumentParser()
    parser.parse_args()

    starttime: str
    endtime: str
    city: str
    verbosityOn: bool
    verbosityOn = False

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

        if(response.ok == True):

            return response.text

        else:
            return "Errore!"
            
        
    def get_place_earthquake(self):
        data = self.get_all_earthquakes()

        
    
        
    
