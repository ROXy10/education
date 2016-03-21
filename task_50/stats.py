file_text = open("text.txt", encoding="UTF-8").read()
file_zn = open("zn.txt", encoding="UTF-8").read().split()

for line in file_zn:
    file_text = file_text.replace(line, "")

l_file_text = file_text.split()
l_file_text.sort()

file_stats = open("stats.txt", "w", encoding="UTF-8")
previous_line = ""
for line in l_file_text:
    amount = l_file_text.count(line)
    if line != previous_line:
        file_stats.write("{0}: {1}\n".format(line, amount))
    previous_line = line
