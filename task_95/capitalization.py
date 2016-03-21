def capitalization(deposited, percent, period):
    i = 1
    while i <= period:
        deposited += deposited * (percent/12)/100
        print(deposited)
        i += 1
    return int(deposited)

print(capitalization(10000, 10, 2))
