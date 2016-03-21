def dates(date):
    global previous_day, previous_day, previous_month, next_month, next_day
    l_date = date.split(".")

    day = int(l_date[0])
    month = int(l_date[1])
    year = int(l_date[2])
    big_month = (1, 3, 5, 7, 8, 10, 12)
    small_month = (4, 6, 9, 11)
    if month in big_month:
        if day == 1:
            if month == 3:
                previous_day = 28
            else:
                previous_day = 31

            next_day = day + 1

            next_month = month

            if month == 1:
                previous_month = 12
                previous_year = year - 1
            else:
                previous_month = month - 1
                previous_year = year
            next_year = year
        elif day == 31:
            previous_day = day - 1
            next_day = 1

            previous_month = month

            if month == 12:
                next_year = year + 1
                next_month = 1
            else:
                next_year = year
                next_month = month + 1
            previous_year = year
        else:
            previous_day = day - 1
            next_day = day + 1

            previous_month = month
            next_month = month

            next_year = year
            previous_year = year
    elif month in small_month:
        if day == 1:
            previous_day = 30
            next_day = day + 1

            previous_month = month - 1
            next_month = month

            next_year = year
            previous_year = year
        elif day == 30:
            previous_day = day - 1
            next_day = 1

            previous_month = month
            next_month = month + 1

            next_year = year
            previous_year = year
        else:
            previous_day = day - 1
            next_day = day + 1

            previous_month = month
            next_month = month

            next_year = year
            previous_year = year
    elif month == 2:
        if day == 1:
            previous_day = 28
            next_day = day + 1

            previous_month = month - 1
            next_month = month

            next_year = year
            previous_year = year
        elif day == 28:
            previous_day = day - 1
            next_day = 1

            previous_month = month
            next_month = month + 1

            next_year = year
            previous_year = year
        else:
            previous_day = day - 1
            next_day = day + 1

            previous_month = month
            next_month = month

            next_year = year
            previous_year = year

    previous_date = zero_ahead(previous_day) + "." + zero_ahead(previous_month) + "." + str(previous_year)
    next_date = zero_ahead(next_day) + "." + zero_ahead(next_month) + "." + str(next_year)

    t_dates = (previous_date, next_date)
    return t_dates

def zero_ahead(value):
    if value < 10:
        return "0" + str(value)
    else:
        return str(value)


print(dates('01.03.2016'))


