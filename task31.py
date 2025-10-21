# todo: Извлеките IP-адреса всех запросов, которые завершились с ошибкой
# (коды ответа 4xx или 5xx).

log_entries = [
    "192.168.1.1 - GET /home 200 1.2s",
    "192.168.1.2 - POST /login 404 0.8s",
    "192.168.1.3 - GET /profile 500 2.1s",
    "192.168.1.4 - GET /about 200 0.5s",
    "192.168.1.5 - POST /submit 403 1.5s",
]
ips = [log.split(" - ")[0] for log in log_entries if "404" in log or "500" in log or "403" in log]
print(ips)
# Результат:
# ["192.168.1.2", "192.168.1.3", "192.168.1.5"]
