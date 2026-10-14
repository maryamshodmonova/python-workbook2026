def ordinal_to_gregorian(year, day_of_year):
    import datetime
    date = datetime.date(year, 1, 1) + datetime.timedelta(days=day_of_year - 1)
    return (date.year, date.month, date.day)
print(ordinal_to_gregorian(2024, 1))