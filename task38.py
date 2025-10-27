# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.
from task37 import Product


class Order:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self._products.append(product)
        else:
            raise TypeError("Можно добавить только экземпляры класса Product")

    def remove_product(self, product):
        if product in self._products:
            self._products.remove(product)

    @property
    def total_price(self):
        return sum(p.price for p in self._products)


# Пример использования
book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(f"Общая стоимость: {order.total_price}")  # 12
