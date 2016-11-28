# Запишем
# Демонстрирует запись в текстовый файл
print("Создаю текстовый файл методом write().")
text_file = open("write_it.txt", "w", encoding='utf-8')

text_file.write("Line 1\n")
text_file.write("This line 2\n")
text_file.write("This line have number 3\n")
text_file.close()

print("\nЧитаю вновь созданный файл.")
text_file = open("write_it.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()

print("\nСоздаю текстовый файл методом writelines().")
text_file = open("write_it.txt", "w", encoding='utf-8')
lines = ["Line 1\n",
         "This line 2\n",
         "This line has number 3\n"]
text_file.writelines(lines)
text_file.close()

print("\nЧитаю вновь созданный файл.")
text_file = open("write_it.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()
input("\n\nНажмите Enter, чтобы выйти.")