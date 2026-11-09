date = int(input("Enter a date: " ))
month = int(input ("Enter a month: "))
if month == 1 and date == 1:
    print ("New Year's Day")
elif month == 3 and date == 8:
    print ("International Women's Day")
elif month == 3 and date == (21, 22, 23, 24):
    print ("Navruz (Persian New Year)")
elif month == 9 and date == 1:
    print ("Labour Day")
elif month ==1 and date ==9:
    print ("Labour Day")
elif month ==7 and date ==27:
    print ("National Unity Day")
elif month == 9 and date == 9:
    print ("Independence Day")
elif month == 11 and date == 6:
    print ("Constitution Day")
else:
    print ("Not a national holiday")