file_1 = open("shopping_list_1.txt")
file_2 = open("shopping_list_2.txt")
file_3 = open("shopping_list_3.txt")

read_1 = file_1.read()
read_2 = file_2.read()
read_3 = file_3.read()


list_r = list(set(read.split(sep = "\n")))

list_r.sort()
list_r.remove("")

file = open("shopping_list.txt", "w+")
file.write("\n".join(list_r)+"\n")

file_1.close()
file_2.close()
file_3.close()
file.close()
