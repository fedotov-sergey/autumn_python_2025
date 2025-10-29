# Система уведомлений (Полиморфизм)
# todo: Реализовать систему отправки уведомлений пользователям через разные каналы.
#
# Требования:
# Базовый класс NotificationSender с методом send(message, user)
# Дочерние классы:
# EmailSender: отправляет email с темой "Образовательная платформа"
# SMSSender: отправляет SMS (первые 50 символов сообщения)
# PushSender: отправляет push-уведомление с иконкой "🎓"
#
# Класс пользователя User:
# Свойства: name, preferred_notifications (список объектов NotificationSender)
class NotificationSender:
    def send(self, message, user):
        pass


class EmailSender(NotificationSender):
    def send(self, message, user):
        theme = "Образовательная платформа"
        print(f"{user.name}, тема: {theme}, сообщение: {message}")


class SMSSender(NotificationSender):
    def send(self, message, user):
        print(f"📱 {user.name}, SMS: {message[:50]}")


class PushSender(NotificationSender):
    def send(self, message, user):
        print(f"🎓 Push для {user.name}: {message}")


class User:
    def __init__(self, name, preferred_notifications):
        self.name = name
        self.preferred_notifications = preferred_notifications


# Этот код должен работать после релизации:
user = User("Мария", [EmailSender(), PushSender()])


def notify_user(user, message):
    for sender in user.preferred_notifications:
        sender.send(message, user)


notify_user(user, "Блок аналитики начинается с 27 октября!")
