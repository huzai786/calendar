from meteostat import Point, Hourly
from datetime import datetime, timedelta

#  + timedelta(days=2)
def get_temp(date):
    start = date + timedelta(days=1, hours=12)
    end = start + timedelta(hours=12)
    Carlsbad = Point(33.0954, -117.2619, 143.5)
    temp = Hourly(Carlsbad, start, end)
    data = temp.fetch().to_dict()
    y = data.get('temp')
    lis = [v for k, v in y.items() if v is not int()]
    try:
        return max(lis)
    except Exception as e:
        return None

def get_temperature(date):
    day = date
    while True:
        a = get_temp(day)
        if a != None:
            return a
            break
        if a == None:
            day = day - timedelta(days = 1)
            continue

if __name__ == '__main__':
    get_temperature()
