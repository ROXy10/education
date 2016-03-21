import sys
string = int(sys.argv[1])

print('{0:,}'.format(string).replace(",", " "))