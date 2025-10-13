# #todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# # нужно сопоставить данные для подстановки.

config_values = {}

f = open("config_default.txt", "r")
lines = f.readlines()
for line in lines:
    if "=" in line:
        option, value = line.replace(" ", "").split("=")
        config_values[option] = value.strip()
print(config_values)


"".startswith()
"".strip()
# # Содержимое файла config_default.txt
# # Конфигурация приложения.
# app_name    = ?
# version     = ?
# debug       = ?
#
# # Настройки базы данных
# db_host     = ?
# db_port     = ?
# db_name     = ?
# db_user     = ?
# db_password = ?
#
# # Настройки API
# api_key     = ?
# api_secret  = ?
# base_url    = ?
