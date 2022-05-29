import requests
from datetime import datetime, timedelta



def get_lowtide(date):
    begin_date = date.strftime('%Y%m%d')
    stop_date = (date + timedelta(days=0)).strftime('%Y%m%d') 
    url = f"https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date={begin_date}&end_date={stop_date}&station=9410230&product=predictions&datum=MLLW&time_zone=lst_ldt&interval=hilo&units=english&format=json"
    res = requests.get(url=url).json()
    tide_data = res.get('predictions')
    try:
        low_tide_value = [data.get('t') for data in tide_data if data.get('type') == 'L']
        return [datetime.strptime(i, '%Y-%m-%d %H:%M') for i in low_tide_value]


    except Exception as e:
        print('tide error', e)
        return 0


if __name__ == '__main__':
    get_lowtide()

