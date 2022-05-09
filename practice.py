from packages.temp import get_temperature
from datetime import datetime, timedelta
from packages.lowtide import get_lowtide
from packages.sunriset import ZipInfo


datem = datetime.now().replace(second=0, minute=0, hour=0, microsecond=0)
# print(datem)


for i in range(11):
    date = datem + timedelta(days=i)
    a = get_lowtide(date)
    print(date, a)