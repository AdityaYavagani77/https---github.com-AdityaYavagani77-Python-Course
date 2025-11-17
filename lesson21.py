"""
import datetime

from datetime import date

today = date.today()

now = datetime.datetime.now()

print(f"\n Today's date is {today} ")

print(f"\n Current date and time is {now}")

print(today.month)
print(today.year)
"""
from datetime import datetime as DT

Time = DT.now()

print("Hour =", Time.hour)
print("Minute =", Time.minute)
print("Second =", Time.second)
print("Microsecond =", Time.microsecond)

