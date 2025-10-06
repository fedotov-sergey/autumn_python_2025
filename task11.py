#  todo: Дан номер месяца (1 — январь, 2 — февраль, ...). Вывести название соответствующего
#  времени года ("зима", "весна" и т.д.).


def seasons_check():
    month = int(input("Какой сейчас месяц по счету? "))
    if month == 1 or month == 2 or month == 12:
        print("зима")
    elif month == 3 or month == 4 or month == 5:
        print("весна")
    elif month == 6 or month == 7 or month == 8:
        print("лето")
    else:
        print("осень")


seasons_check()
