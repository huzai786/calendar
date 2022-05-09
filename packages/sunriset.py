import requests
from astral import LocationInfo, sun

class ZipInfo(object):
    
    def __init__(self, zipcode):
        self.zipcode = zipcode

    def get_sunrise(self, for_date):
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},us&appid=7015d42a7df0d257dad429a045772ef2"
        res = requests.get(url=url).json()
        longitude = res.get('coord').get('lon')
        latitude = res.get('coord').get('lat')

        city = LocationInfo('Carlsbad', 'california', "US/Pacific", latitude, longitude)
        s = sun.sun(city.observer, date=for_date, tzinfo=city.timezone)
        return (s['sunrise']).replace(tzinfo=None, microsecond=0)

    def get_sunset(self, for_date):
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},us&appid=7015d42a7df0d257dad429a045772ef2"
        res = requests.get(url=url).json()
        longitude = res.get('coord').get('lon')
        latitude = res.get('coord').get('lat')

        city = LocationInfo('Carlsbad', 'california', "US/Pacific", latitude, longitude)
        s = sun.sun(city.observer, date=for_date, tzinfo=city.timezone)
        return (s['sunset']).replace(tzinfo=None, microsecond=0)


# 33.0954, -117.2619
