#  todo: Дан номер месяца (1 — январь, 2 — февраль, ...). Вывести название соответствующего
#  времени года ("зима", "весна" и т.д.).
def seasons_check():
    mounth=int(input('Какой сейчас месяц по счету? '))
    if mounth == 1 or mounth == 2 or mounth == 12:
        print("зима")
    elif mounth == 3 or mounth == 4 or mounth == 5:
        print("весна")
    elif mounth == 6 or mounth == 7 or mounth == 8:
        print("лето")
    else:
        print("осень")
seasons_check()