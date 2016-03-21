def code(text, key=1):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    symbol = " !@#$%^&*()_+~|"
    i = 0
    while i < len(text)-1:
        print(text[i])
        i += 1


print(code("Агент 007, срочно выйдите на связь"))