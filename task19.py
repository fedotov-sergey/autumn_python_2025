# todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm
f = open("algoritm.csv", "at")
algoritm = [
    "C4.5",
    "k - means",
    "Метод опорных векторов",
    "Apriori",
    "EM",
    "PageRank",
    "AdaBoost",
    "kNN",
    "Наивный байесовский классификатор",
    "CART",
]
for item in algoritm:
    f.write(item + "\n")
f.close()
f = open("algoritm.csv", "rt")
indx = 1
list_str = f.readlines()
for csv_str in list_str:
    print(indx, ")", csv_str)
    indx += 1
# Каждое значение из списка должно находится на отдельной строке.
# Пример файла algoritm.csv:
# 1) "C4.5"
# 2) "k - means"
