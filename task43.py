# todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.
import datetime

# Глобальный словарь для подсчёта вызовов
stats = {}


def myFirstDecorator(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()

        # Выполняем функцию
        res = func(*args, **kwargs)

        end = datetime.datetime.now()

        # Считаем вызовы
        name = func.__name__
        if name not in stats:
            stats[name] = {"count": 0, "last": None}

        stats[name]["count"] += 1
        stats[name]["last"] = end

        # Логируем в файл каждое выполнение
        with open("debug.log", "a", encoding="utf-8") as fd:
            fd.write(f"{name}, {stats[name]['count']}, {end.strftime('%d.%m.%Y %H:%M:%S')}\n")

        print(f"Время выполнение функции: {end - start}")
        return res

    return wrapper


# Оставляем твою тестовую функцию
def summ(x, y):
    return x + y


test = myFirstDecorator(summ)
res = test(3, 3)
print(res)


@myFirstDecorator
def power(x, y):
    return x * y


print(power(3, 3))
print(power(10, 10))
