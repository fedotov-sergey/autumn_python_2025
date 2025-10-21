# todo: Вы пишете скрипт для очистки временных файлов. Создайте список полных путей к временным файлам (с расширениями .tmp, .bak),
# добавив к каждому путь "/tmp/".
files = ["document.pdf", "temp_backup.tmp", "image.jpg", "cache.tmp", "report.docx", "old_data.bak"]
temps = ["/tmp/" + fl for fl in files if fl.endswith(".tmp") or fl.endswith(".bak")]
print(temps)

# результат:
# ["/tmp/temp_backup.tmp", "/tmp/cache.tmp", "/tmp/old_data.bak"]
