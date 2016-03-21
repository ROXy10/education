file = open("matrix.txt", encoding="UTF-8").read().split("\n")

new_matrix = []
i = 0
while i <= len(file[0].split())-1:
    new_matrix.append([])
    n = 0
    while n <= len(file)-1:
        new_matrix[i].append(file[n].split()[i])
        n += 1
    i += 1

file_transpose = open("transpose_matrix.txt", "w", encoding="UTF-8")
for value in new_matrix:
    file_transpose.write(" ".join(value)+"\n")
