# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.


# Пример использования
class User:
    def __init__(self, email, password):
        self.__password = password
        self.hashed_password = hash(password)
        if "@" in email:
            self.email = email
        else:
            self.email = None

    def check_password(self, password):
        if self.hashed_password == hash(password):
            return True
        else:
            return False


user = User("test@example.com", "secret")
print(user.email)  # test@example.com
#print(user.password)  # AttributeError
print(user.check_password("secret"))  # True
print(user.check_password("wrong"))  # False
