def choose_plural(number, string):
    l_string = string.split(",")
    str_number = str(number)
    if str_number[-1] == "1" and len(str_number) == 1:
        return l_string[0]
    elif str_number[-1] == "2" and len(str_number) == 1:
        return l_string[1]
    elif str_number[-1] == "3" and len(str_number) == 1:
        return l_string[1]
    elif str_number[-1] == "4" and len(str_number) == 1:
        return l_string[1]
    elif str_number[-1] == "1" and str_number[-2] != "1":
        return l_string[0]
    elif str_number[-1] == "2" and str_number[-2] != "1":
        return l_string[1]
    elif str_number[-1] == "3" and str_number[-2] != "1":
        return l_string[1]
    elif str_number[-1] == "4" and str_number[-2] != "1":
        return l_string[1]
    else:
        return l_string[2]



result = choose_plural(23, "ананас,ананаса,ананасов")
print(result)