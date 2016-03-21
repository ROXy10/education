import sys
string = sys.argv[1]
new_spring = list(string)
new_spring.sort()
print("".join(new_spring))