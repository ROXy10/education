import sys
light_green = int(sys.argv[1])
light_yellow = int(sys.argv[2])
light_red = int(sys.argv[3])
minute = int(sys.argv[4])

light = 0
i = 0
while i <= minute:
    if light == 0:
        i += light_green
        light = 1
    elif light == 1:
        i += light_yellow
        light = 2
    else:
        i += light_red
        light = 0

if light == 1:
    print("green")
elif light == 2:
    print("yellow")
else:
    print("red")
