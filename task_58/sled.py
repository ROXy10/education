file = open("matrix.txt", encoding="UTF-8")

i = 0
mat_trace = 0
for line in file:
    mat_line = line.strip().split()
    mat_trace += int(mat_line[i])
    i += 1
print(mat_trace)
file.close()
