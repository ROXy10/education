file_1 = open("shopping_list_1.txt", encoding="UTF-8")
file_2 = open("shopping_list_2.txt", encoding="UTF-8")
file_3 = open("shopping_list_3.txt", encoding="UTF-8")
file = open("shopping_list.txt", "w+", encoding="UTF-8")

read_1 = file_1.read()
read_2 = file_2.read()
read_3 = file_3.read()


read = read_1+read_2+read_3
set_r = set(read.split("\n"))
set_r.remove("")
list_r = list(set_r)
list_r.sort()

file.write("\n".join(list_r)+"\n")
