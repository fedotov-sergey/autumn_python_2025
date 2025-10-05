# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"
print(type(foo))
age = int(age)
foo = int(foo[:2])
print(type(age), age)
print(type(foo), foo)
# Преобразуйте переменную age в Boolean
age = "123abc"
age = bool(age)
print(type(age),'age = ', age)
# Преобразуйте переменную flag в Boolean
flag = 1
flag = bool(flag);
print(type(flag),'flag = ',flag)
# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""
str_one = bool(str_one)
str_two = bool(str_two)
print(type(str_one),'str_one = ', str_one,type(str_two),'str_two = ', str_two)
# Преобразуйте значение 0 и 1 в Boolean
a = 0
b = 1
a = bool(a)
b = bool(b)
print('a =',a,' b =',b)
# Преобразуйте False в строку
f:bool = False
f=str(f)
print('f =',f, type(f))