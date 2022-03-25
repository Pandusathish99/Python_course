import calendar
print(calendar.calendar(2018))
print(calendar.month(2019,7))
print(calendar.leapdays(2020,2023))
print(calendar.isleap(2024))
print(calendar.weekday(2015,5,3))

for name in calendar.month_name:
    print(name)
    for name in calendar.day_name:
        print(name)