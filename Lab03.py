# 1. Name:
#      Braeden Pope
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      Receives input from a user of a month and year, and displays the calendar of the input
# 4. What was the hardest part? Be as specific as possible.
#      I spent a while trying to get the offset to work correctly, I had to do some trial and error but I got it.
# 5. How long did it take for you to complete the assignment?
#      2 hours

def get_month():
    loop = True;
    while (loop):
        try:
            month = int(input("Enter the month number: "))
            if (month < 1 or month > 12):
                print("The number must be between 1 and 12.")
            else:
                loop = False;
        except ValueError:
            print("Please enter an integer between 1 and 12.")
    return month

def get_year():
    loop = True;
    while (loop):
        try:
            year = int(input("Enter the year: "))
            if (year < 1753):
                print("The year must be after 1753.")
            else:
                loop = False;
        except ValueError:
            print("Please enter an integer.")
    return year

def is_leap_year(year):
    if (year % 400 == 0 and year % 100 == 0):
        return True
    elif (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

def days_in_month(month, is_leap):
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        return 30
    elif (month == 2 and is_leap):
        return 29
    else:
        return 28

def get_offset(month, year, is_leap):
    total_days = 0
    i_year = 0
    for i_year in range(1753,year):
        if (is_leap_year(i_year)):
            total_days += 366
        else:
            total_days += 365

    for i_month in range(1, month):
        total_days += days_in_month(i_month, is_leap)
    if (total_days % 7 +1 == 7):
        return 0;
    return (total_days % 7 + 1)


def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline


# Output
month = get_month()
year = get_year()
is_leap = is_leap_year(year)
days = days_in_month(month, is_leap)
offset = get_offset(month, year, is_leap)
display_table(offset, days)
