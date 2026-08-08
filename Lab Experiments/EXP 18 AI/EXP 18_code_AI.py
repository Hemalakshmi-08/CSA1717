# Program to generate calendar for a given month and year

import calendar

# Taking input
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Display calendar
print("\nCalendar:")
print(calendar.month(year, month))
