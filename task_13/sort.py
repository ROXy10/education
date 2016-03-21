import sys
string = set(sys.argv[1])
list_str = list(string)
list_str.sort()
print("".join(list_str))
