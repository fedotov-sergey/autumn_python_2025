# todo: Дан целочисленный массив размера N из 10 элементов.
# Преобразовать массив, увеличить каждый его элемент на единицу.
arr = list(map(int, input("Введите числа через пробел").split()))
length = len(arr)
i = 0
while i < length:
    arr[i] = arr[i] + 1
    i = i + 1
print(arr)

# альтернатива
new_arr = [x + 1 for x in arr]
print(new_arr)


# альтернатива 2
new_arr = []
for x in arr:
    new_arr.append(x + 1)

print(new_arr)
