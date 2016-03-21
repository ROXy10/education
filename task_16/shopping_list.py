file_1 = open("shopping_list_1.txt", encoding="UTF-8")
file_2 = open("shopping_list_2.txt", encoding="UTF-8")
file_3 = open("shopping_list_3.txt", encoding="UTF-8")

read_1 = set(file_1.read().split(sep = "\n"))
read_2 = set(file_2.read().split(sep = "\n"))
read_3 = set(file_3.read().split(sep = "\n"))

read = read_1 | read_2 | read_3
list_r = list(read)

list_r.sort()
list_r.remove("")

file = open("shopping_list.txt", "w", encoding="UTF-8")
file.write("\n".join(list_r)+"\n")

file_1.close()
file_2.close()
file_3.close()
file.close()
