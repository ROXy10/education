import sys
number = int(sys.argv[1])

print(number, bin(number)[2:], oct(number)[2:], hex(number)[2:])