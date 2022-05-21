from packages.temp import get_temperature
from datetime import datetime, timedelta


# d = datetime(2022, 5, 17)

# a = get_temperature(d)
# for i in range(14):
#     a = get_temperature(d + timedelta(days=i))
#     print(d + timedelta(days=i))
#     print(a)


dictionary = [{'Temperature': 'yes', 'x1': 45, 'x2': 23}, {'Low tide': 'yes', 'x1': 5, 'x2': 6}, {
    'Sunset': 'yes', 'x1': 34, 'x2': 33}, {'Sunrise': 'yes', 'x1': 7, 'x2': 7}, {'Window': 'no', 'x1': 22, 'x2': 52}]
if any(['Temperature' in _dict for _dict in dictionary]):
    values = [(value.get('x1'), value.get('x2'))
            for value in dictionary if value.get('Temperature')][0]
    print(values)
    print('logic goes here')
