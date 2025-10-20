# todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

# Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................
# Список гласных букв (русские и английские, если нужно)
glasnie = "аеёиоуыэюя"
count_glasnie = {}
f = open("dump.txt", "r")
text = f.read().lower()  # переводим в нижний регистр для единообразия
for i in text:
    if i in glasnie:
        count_glasnie[i] = count_glasnie.get(i, 0) + 1
for glasnie, count in sorted(count_glasnie.items()):
    print(f"Количество букв {glasnie} - {count}")
