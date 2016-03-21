file = open("text.txt", encoding="UTF-8")

r_file = file.read()
line_text = r_file.replace(". ", ".\n").replace("! ", "!\n").replace("? ", "?\n")
line_list = line_text.split("\n")

file_record = open("complex.txt", "w", encoding="UTF-8")
for line in line_list:
    if len(line) >= 120 and line.count(",") >= 2:
        file_record.write(line+"\n")