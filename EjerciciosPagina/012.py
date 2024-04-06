import calendar

def print_calendar(year, month):
    # Print the calendar for the given month and year
    cal = calendar.month(year, month)
    print("Calendar for {}/{}:".format(month, year))
    print(cal)

# Input month and year from the user
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Call the function to print the calendar
print_calendar(year, month)