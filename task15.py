# todo: Дан целочисленный массив размера N из 10 элементов.
# Преобразовать массив, увеличить каждый его элемент на единицу.
arr = list(map(int, input("Введите числа через пробел").split()))
length = int(len(arr))
i = 0
while i != range(length):
    arr[i] = arr[i] + 1
    i = i + 1
    if i == length:
        break
print(arr)
