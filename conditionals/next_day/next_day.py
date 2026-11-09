import calendar
year = int (input())
month = int (input ())
date = int (input ())
if month == 2 and date == 28 and calendar.isleap(year):
    date = 29
elif month == 2 and date == 29:
    month = 3 
    date = 1
else: 
    date = date + 1 
print(f"{year:04d}-{month:02d}-{date:02d}")
