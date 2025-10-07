# В восточном календаре принят 60-летний цикл, состоящий из 12- летних подциклов,
# обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный.
# В каждом подцикле годы носят названия животных: крысы, коровы, тигра, зайца, дракона,
# змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи. По номеру года вывести его название,
# если 1984 год был началом цикла — годом зеленой крысы.
# animals = [
#         "крысы",
#         "коровы",
#         "тигра",
#         "зайца",
#         "дракона",
#         "змеи",
#         "лошади",
#         "овцы",
#         "обезьяны",
#         "курицы",
#         "собаки",
#         "свиньи",
#     ]
#     colors: list[str] = ["зеленый", "красный", "желтый", "белый", "черный"]
# start_year: int = 1984
# start_color: str = colors[0]
# input_year: int = int(input('Введите ваш год'))
year = int(input("Enter year: "))
match year % 10:
    case 0 | 1:
        color_year = "white"
    case 2 | 3:
        color_year = "black"
    case 4 | 5:
        color_year = "green"
    case 6 | 7:
        color_year = "red"
    case 8 | 9:
        color_year = "yellow"
match year % 12:
    case 1:
        animal = "cock"
    case 2:
        animal = "dog"
    case 3:
        animal = "pig"
    case 4:
        animal = "rat"
    case 5:
        animal = "bull"
    case 6:
        animal = "tiger"
    case 7:
        animal = "rabbit"
    case 8:
        animal = "dragon"
    case 9:
        animal = "snake"
    case 10:
        animal = "horse"
    case 11:
        animal = "goat"
    case 0:
        animal = "monkey"
print(str(year) + " is year of " + color_year + " " + animal)
