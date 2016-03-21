import sys
string = sys.argv[1]

if string == string[::-1]:
    print(1)
else:
    print(0)
