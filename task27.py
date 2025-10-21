# todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
alfa = "abcdefghijklmnopqrstuvwxyz"
crossword = input("Enter a digit: ")

result = ""
for word in crossword.split(" "):
    if word.isdigit():
        num = int(word)
        if num == 0:
            result += " "
        elif 1 <= num <= 26:
            result += alfa[num - 1]
        else:
            result += word
    else:
        result += word
print(result)
