#  1. Реализовать класса DB - синглтон. Экземляр класса(подключение) к PostgreSQL
#  должно быть единственным.
import psycopg2
from psycopg2 import OperationalError


class DB:
    _instance = None
    _connection = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DB, cls).__new__(cls)
        return cls._instance

    def connect(self, dsn: str):
        # Подключение к PostgreSQL
        if self._connection is None:
            try:
                self._connection = psycopg2.connect(dsn)
                print("Подключение к базе успешно установлено.")
            except OperationalError as e:
                print(f"Ошибка подключения: {e}")
        return self._connection

    def get_connection(self):
        return self._connection


#  2. Реализовать  фабрику которая создает модели различных производителей
    # 2. Реализовать для класса Car абстрактный класс который содержит
    # aбстрактные методы sold, discount


from abc import ABC, abstractmethod

class CarBase(ABC):

    @abstractmethod
    def sold(self):
        pass

    @abstractmethod
    def discount(self):
        pass


class Car(CarBase):

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    @staticmethod
    def make_lada():
        return Car("Lada", "Vesta")

    @staticmethod
    def make_mercedes():
        return Car("Mercedes", "C-class")

    @staticmethod
    def make_toyota():
        return Car("Toyota", "Camry")

    def sold(self):
        print(f"Автомобиль {self.brand} {self.model} продан.")

    def discount(self):
        print(f"На автомобиль {self.brand} {self.model} скидка 5%.")

    def __repr__(self):
        return f"<Car brand='{self.brand}' model='{self.model}'>"
