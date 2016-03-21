import sys
file = open(sys.argv[1], encoding="UTF-8").read().split()

if file.count(file[0]) == len(file):
    seq = 0
else:
    number = 0
    for line in file:
        if int(line) >= number:
            seq = 1
        else:
            seq = 0
            break
        number = int(line)

print(seq)