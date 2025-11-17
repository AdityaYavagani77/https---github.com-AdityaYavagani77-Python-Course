"""
import datetime

from datetime import date

today = date.today()

now = datetime.datetime.now()

print(f"\n Today's date is {today} ")

print(f"\n Current date and time is {now}")

print(today.month)
print(today.year)

from datetime import datetime as DT

Time = DT.now()

print("Hour =", Time.hour)
print("Minute =", Time.minute)
print("Second =", Time.second)
print("Microsecond =", Time.microsecond)


import calendar

yy = 1452
mm = 4

print(calendar.month(yy,mm))
"""

import calendar

cal = calendar.Calendar()

for x in cal.itermonthdates(1333, 8):
    print(x)