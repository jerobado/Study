# Ge the week number of the current date
# For example:
#   17 Jan 2021     - date today
#   week 3          - should display this

# Strategy:
# [] loop each month and count every Mondays


import calendar


calendar.setfirstweekday(calendar.SUNDAY)
ox_year = calendar.Calendar(2021)

def use_itermonthdays():
    
    # itermonthdates - prints 2021-01-07
    # itermonthdays - prints 7
    # itermonthdays2 - prints (7, 3)  -> date, weekday number  // starts at Monday at 0 index
    # itermonthdays3 - prints (2021, 1, 7) -> year, month, day
    # itermonthdays4 - prints (2021, 1, 7, 3) -> year, month, day

    month_days = ox_year.itermonthdays4(2021, 12)
    for day in month_days:
        print(day)


def use_iterweekdays():

    weekdays = ox_year.iterweekdays()
    for weekday in weekdays:
        print(weekday)


def use_monthdatescalendar():

    # monthdatescalendar -> [datetime.date(2021, 1, 2), datetime.date(2021, 1, 3), datetime.date(2021, 1, 4), datetime.date(2021, 1, 5), datetime.date(2021, 1, 6), datetime.date(2021, 1, 7), datetime.date(2021, 1, 8)]
    # monthdayscalendar -> [2, 3, 4, 5, 6, 7, 8]
    # monthdays2calendar -> [(2, 5), (3, 6), (4, 0), (5, 1), (6, 2), (7, 3), (8, 4)]

    for week in ox_year.monthdayscalendar(2021, 1):
        print(week)


def use_yeardatescalendar():

    for something in ox_year.yeardayscalendar(2021, 1):
        print(something)


def get_week_count(year=0) -> int:

    week_count = 0
    previous_day = None

    # every_mondays = []

    for month in range(1, 13):
        month_days = ox_year.itermonthdays4(year, month)
        for day in month_days:
            if day[0] == year and day[3] == 0:
                # print(day)
                # previous_day = day
                if previous_day != day:
                    print(day)
                    previous_day = day
                    week_count += 1

    return week_count


def solution():

    year = 2024
    message = f'there are {get_week_count(year)} weeks in {year}'
    print(message)


# use_monthdatescalendar()
# use_yeardatescalendar()
# use_itermonthdays()   # potential solution
# use_monthdatescalendar()

solution()

