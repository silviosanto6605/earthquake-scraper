import requests



def get_earthquakes(startTime, endTime):

    params = (
        ('starttime', startTime),
        ('endtime', endTime),
        ('format', 'text')
    )
    response = requests.get(
        'https://webservices.ingv.it/fdsnws/event/1/query', params=params)

    if response.ok:
        return response.text

    elif not response.ok:
        if response.status_code == 400:
            print("Error! Check the date again and retry")
            exit(0)

        elif response.status_code == 413:
            print("Error! Date range too high!")
            exit(0)

def get_place_earthquake(self, place):
    data = self.get_all_earthquakes()
