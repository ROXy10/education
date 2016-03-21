file = open("numbers.txt", encoding="UTF-8")

f_read = file.read().split()
minus = 0
for char in f_read:
    if int(char) < 0:
        minus += int(char)

print(minus)
file.close()