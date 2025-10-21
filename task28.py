# #todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.
alfa = "abcdefghijklmnopqrstuvwxyz"
shifr = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
shift = int(input("Enter a shift: "))
vzlom = ""

for letter in shifr:
    if letter.isspace():
        vzlom += " "
    elif letter in alfa:
        index = alfa.index(letter)
        vzlom += alfa[(index - shift) % len(alfa)]
    else:
        vzlom += letter

print(vzlom)

# Enter a shift: 6
# although that way may not be obvious at first unless you're dutch.
