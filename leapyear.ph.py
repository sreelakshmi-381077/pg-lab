import calendar
year=int(input("enter the year"))
leap_year=calendar.isleap(year)
if leap_year:
    print("the given year is a leap year")
else:
    print("the given leap is a non-leap year")