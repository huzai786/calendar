from packages.temp import get_temperature
from datetime import datetime, timedelta



d = datetime(2022, 5, 17)

a = get_temperature(d)
for i in range(14):
    a = get_temperature(d + timedelta(days=i))
    print(d + timedelta(days=i))
    print(a)