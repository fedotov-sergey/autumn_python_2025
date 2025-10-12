# #todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# # Для этого считайте список всех строк при помощи метода readlines().

# #Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
f = open("inverted_sort.txt", "r+")
lines = f.readlines()
inversio = lines[::-1]
if not inversio[0].endswith("\n"):
    f.write("\n")
f.seek(0, 2)
f.writelines(inversio)
f.close()

# # Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.
