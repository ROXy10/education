def floor(number_apartment, amount_apartments):
    if number_apartment == 1:
        return 1
    else:
        return int(round(number_apartment / amount_apartments, 0))