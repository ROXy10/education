import sys
n = int(sys.argv[1])
m = int(sys.argv[2])
t = int(sys.argv[3])

boolean = True
i = 0
while i <= t:
    if boolean:
        i += n
        boolean = False
    else:
        i += m
        boolean = True

if not boolean:
    print("green")
else:
    print("red")