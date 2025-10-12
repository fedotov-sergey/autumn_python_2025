# todo: База данных пользователя.
# Задан массив объектов пользователя
from unittest import case

users = [
    {"login": "Piter", "age": 23, "group": "admin"},
    {"login": "Ivan", "age": 10, "group": "guest"},
    {"login": "Dasha", "age": 30, "group": "master"},
    {"login": "Fedor", "age": 13, "group": "guest"},
]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
# Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

num = int(
    input(
        """По какому параметру будем искать?
1. По возрасту
2. По первой букве
3. По группе
"""
    )
)
match num:
    case 1:
        age = int(input("Порог возраста: "))
        for user in users:
            if user["age"] < age:
                continue
            else:
                print(f'Пользователь: {user["login"]} возраст {user["age"]} , группа {user["group"]}')
    case 2:
        first_letter = input("Первая буква: ")
        for user in users:
            if first_letter not in user["login"]:
                continue
            else:
                print(f'Пользователь: {user["login"]} возраст {user["age"]} , группа {user["group"]}')
    case 3:
        group = input("Имя группы: ")
        for user in users:
            if group in user["group"]:
                print(f'Пользователь: {user["login"]} возраст {user["age"]} , группа {user["group"]}')
            else:
                continue


# тип сортировки: 1

# Затем сообщение для ввода
# Введите критерии поиска: 16

# Результат:
# Пользователь: 'Piter' возраст 23 года , группа  "admin"
# Пользователь: 'Dasha' возраст 30 лет , группа  "master"
