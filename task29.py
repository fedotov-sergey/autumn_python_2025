# todo: Вы получаете из API список пользователей,
# но нужно отфильтровать и преобразовать данные перед загрузкой в базу.
# Создайте список email-адресов только для активных пользователей старше 18 лет.
# Задачу следует решить с использованием списковых включений

users = [
    {"name": "alice", "email": "alice@example.com", "age": 25, "active": True},
    {"name": "bob", "email": "bob@example.com", "age": 17, "active": True},
    {"name": "charlie", "email": "charlie@example.com", "age": 30, "active": False},
    {"name": "diana", "email": "diana@example.com", "age": 16, "active": True},
]
emails = [u["email"] for u in users if u["active"] and u["age"] > 18]
print(emails)
# Результат
# ['alice@example.com']
