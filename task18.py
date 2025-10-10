# todo: Заданы множества
# Даны читатели книг
readers_books = {"id3", "id5", "id9", "id8", "id2", "id1"}

# Даны читатели газет
readers_magazines = {"id8", "id2", "id1", "id4", "id6", "id7", "id10"}
all_shit_readers = readers_books.union(readers_magazines)
# Найти пользователей кто читает и книги и газеты
print("Любители бумаги: " + (str(all_shit_readers)))
