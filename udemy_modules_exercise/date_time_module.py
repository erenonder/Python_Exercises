from datetime import time
from datetime import date
from datetime import datetime

# the rest of time will be default 0 as in second
mytime = time(13, 20)
print(mytime.minute)
print(mytime.hour)
print(mytime.second)
print(mytime)

today = date.today()
aday = date(2045, 11, 3)

print(aday)
print(today)
print(today.year)
print(aday - today)
print(type(aday - today))

mydt = datetime(2021, 10, 3, 14, 10, 1)
print(mydt)
rpdt = mydt.replace(year=2022, day=17, hour=11)
print(rpdt)
diff = rpdt - mydt
print(diff)
print(diff.seconds)

