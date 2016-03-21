import sys
string = sys.argv[1]

new_string = ""
for x in string:
    if x in "aeiou":
        new_string += x
print(new_string)