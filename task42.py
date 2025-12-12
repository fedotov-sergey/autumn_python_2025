# todo: Реализовать собственный класс исключений, которые будут вызываться (бросаться) в случае:
#  1. пользователь ввел некорректное значение в заданном диапазоне
#  2. результат запроса вернул 0 строк
#  3. Произошел разрыв соединения с сервером
class InvalidRangeError(Exception):
    """Ошибка: значение вне допустимого диапазона."""

    pass


class EmptyResultError(Exception):
    """Ошибка: запрос вернул 0 строк."""

    pass


class ConnectionLostError(Exception):
    """Ошибка: потеряно соединение с сервером."""

    pass


def check_value(value, min_v=1, max_v=10):
    if not (min_v <= value <= max_v):
        raise InvalidRangeError(f"Значение {value} вне диапазона {min_v}–{max_v}")


def zero_rows(rows):
    if len(rows) == 0:
        raise EmptyResultError("Запрос вернул 0 строк")
    return rows


def check_connection(is_connected):
    if not is_connected:
        raise ConnectionLostError("Разрыв соединения с сервером")


try:
    check_value(50)
except InvalidRangeError as e:
    print("Ошибка диапазона:", e)

try:
    zero_rows([])
except EmptyResultError as e:
    print("Ошибка результата:", e)

try:
    check_connection(False)
except ConnectionLostError as e:
    print("Ошибка соединения:", e)
