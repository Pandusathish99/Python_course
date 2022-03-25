import datetime
Pandu = datetime.datetime.now()
print("Current date and time is:", Pandu)
print(Pandu.isocalendar())
print(Pandu.month)
print(Pandu.day)
print(Pandu.astimezone())
print(Pandu.now())
print("Current time zone is:", Pandu.astimezone())
print(Pandu.year)
print(Pandu.month)

import calendar
print(calendar.calendar(1994))
