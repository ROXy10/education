import sys, fractions
string = sys.argv[1]

list_s = string.split(sep=",")
list_s[0] = list_s[0].capitalize()
last_word = list_s.pop(len(list_s)-1)
print(", ".join(list_s), "и", last_word+".")