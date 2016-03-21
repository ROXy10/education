import sys
string = sys.argv[1].split()

i = 0
while i <= len(string)-1:
    string[i] = string[i][::-1]
    i += 1

print(" ".join(string))