import sys
string = sys.argv[1]

correctly = 0
if string[0] != ")":
    for char in string:
        if char == "(":
            correctly += 1
        elif char == ")":
            correctly -= 1
else:
    correctly = 1

if correctly == 0:
    print(1)
else:
    print(0)
