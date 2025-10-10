# todo: Заданы множества
# все пользователи
all_users = {"id3", "id5", "id9", "id8", "id2", "id1", "id4", "id6", "id7", "id10"}

# пользователи не в сети
offline_users = {"id3", "id9", "id7", "id2", "id4", "id6"}
online_users = all_users.difference(offline_users)
# Вычислить пользователей online
print("Users online:" + str(online_users))
