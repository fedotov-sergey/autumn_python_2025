# todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
# Пример:

mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]
number: int = int(input("Введите число для которого будет искаться расстояние "))
distance = []
i = 0
for mas in mass:
    if number == mas:
        i += 1
        distance.append(i)
    else:
        i += 1
        continue
num = len(distance)
match num:
    case 1:
        print(f"Для числа {number} нет минимального расстояния, т.к. элемент в массиве один")
        pass
    case 2:
        print(f"Для числа {number} минимальное расстояние в массиве {abs(distance[0]-distance[1])}")
    case 3:
        if distance[0] < distance[1] and distance[0] < distance[2]:
            print(f"Для числа {number} минимальное расстояние в массиве {abs(distance[1]-distance[2])}")
        elif distance[1] < distance[0] and distance[1] < distance[2]:
            print(f"Для числа {number} минимальное расстояние в массиве {abs(distance[0]-distance[2])}")
        else:
            print(f"Для числа {number} минимальное расстояние в массиве {abs(distance[1]-distance[0])}")

# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.
