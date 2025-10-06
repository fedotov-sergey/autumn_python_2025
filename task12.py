# todo: Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм,
#  4 — тонна, 5 — центнер. Дан номер единицы массы и масса тела M в этих единицах (вещественное число).
#  Вывести массу данного тела в килограммах
def mass_to_kg():
    weight_type: int = int(
        input(
            """Какие единицы измерения используем?\n 1 — килограмм\n 2 — миллиграмм\n 3 — грамм\n 4 — тонна \n 5 — центнер\n"""
        )
    )
    mass: float = float(input("Какая масса?"))
    if weight_type == 1:
        mass: float = mass * 1
    elif weight_type == 2:
        mass: float = mass // (1000**2)
    elif weight_type == 3:
        mass: float = mass // 1000
    elif weight_type == 4:
        mass: float = mass * 1000
    print(mass, " килограмм")


mass_to_kg()
