def is_leap_year(year_number):

    if year_number % 100 == 0:
        if year_number % 400 == 0:
            return True
        else:
            return False
    elif year_number % 4 == 0:
        return True
    else:
        return False


print(is_leap_year(200))