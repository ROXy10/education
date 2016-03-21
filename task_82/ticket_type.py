def ticket_type(number):
    l_number = list(number)
    i = 0
    while i <= len(l_number) - 1:
        l_number[i] = int(l_number[i])
        i += 1
    if sum(l_number[:3]) == sum(l_number[3:]):
        return "счастливый"
    elif sum(l_number[:3]) == sum(l_number[3:]) + 1/
    or sum(l_number[:3]) == sum(l_number[3:]) - 1:
        return "встречный"
    elif sum(l_number[:3]) == sum(l_number[3:]) + 2/
    or sum(l_number[:3]) == sum
    (l_number[3:]) - 2:
        return "пьяный"
    else:
        return "обычный"
print(ticket_type("123325"))
