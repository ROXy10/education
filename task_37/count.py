import sys
string = sys.argv[1]
signs = {",", ".", "!", "?"}

list_s = set(string.split())
list_s = list_s-signs
print(len(list_s))