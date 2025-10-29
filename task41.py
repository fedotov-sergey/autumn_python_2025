# todo: Создайте иерархию классов для экспорта данных в разные форматы.
# Требования:
# Абстрактный базовый класс DataExporter:
#
# Методы:
# export(self, data) - абстрактный метод
# get_format_name(self) - возвращает название формата
# validate_data(self, data) - общий метод проверки данных (не пустые ли)
#
# Конкретные реализации:
# JSONExporter:
# Экспортирует данные в JSON-формат
# Добавляет поле "export_timestamp" с текущим временем
#
# CSVExporter:
# Экспортирует данные в CSV (если data - список словарей)
# Автоматически определяет заголовки из ключей первого элемента
#
# XMLExporter:
# Создает XML структуру с корневым элементом <report>
# HTMLExporter (дополнительно):
# Создает красивую HTML-таблицу с CSS-стилями
class DataExporter:
    def __init__(self, data):
            self.data = data
    def get_format_name(self):

    def validate_date(self,date):

class JSONExporter(DataExporter):
    def __init__(self, data):
            super().__init__(data)
    def get_format_name(self):

    def validate_date(self,date):

class CSVExporter(DataExporter):
    def __init__(self, data):
            super().__init__(data)
    def get_format_name(self):

    def validate_date(self,date):

class HTMLExporter(DataExporter):
    def __init__(self, data):
            super().__init__(data)
    def get_format_name(self):

    def validate_date(self,date):

# Этот код должен работать после реализации:
sales_data = [{"product": "Laptop", "price": 1000, "quantity": 2}, {"product": "Mouse", "price": 50, "quantity": 10}]

exporters = [JSONExporter(), CSVExporter(), XMLExporter()]

for exporter in exporters:
    print(f"Формат: {exporter.get_format_name()}")
    exporter.export(sales_data)
    print("---")
