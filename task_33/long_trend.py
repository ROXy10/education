import sys
string = sys.argv[1].split()

previous_value = 0
increasing_trend = [[]]
decreasing_trend = [[]]
for value in string:
    if int(value) <= previous_value:
        increasing_trend.append([])
    elif int(value) >= previous_value:
        decreasing_trend.append([])
    previous_value = int(value)
    increasing_trend[-1].append(value)
    decreasing_trend[-1].append(value)

i_max = max(len(i) for i in increasing_trend)
d_max = max(len(i) for i in decreasing_trend)

#print(i_max, d_max)

if i_max > d_max:
    for trend in [_ for _ in increasing_trend if len(_) == i_max]:
        pass
else:
    for trend in [_ for _ in decreasing_trend if len(_) == d_max]:
        pass

print(" ".join(trend))
