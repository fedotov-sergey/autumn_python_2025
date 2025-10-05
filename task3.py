# todo: Данные две переменные:
age = 36.6
temperature = 25
# Нужно обменять значения переменных местами. В итого age
# должен равнятся 25 а temperature – 36.6:
# 1-способ
change = age
age = temperature
temperature = change
print('age =',age)
print('temperature =',temperature)
# 2-й способ
age, temperature = temperature, age
print('temperature =',temperature)
print('age =',age)