import sys
first_day = int(sys.argv[1])
number_day = int(sys.argv[2])

week = 0
if first_da+y > number_day:
    week = -1
else:
    for i in range(first_day, number_day+1, 7):
        week += 1
print(week)