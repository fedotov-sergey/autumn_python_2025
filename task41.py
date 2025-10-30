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
import csv
import json
import xmltodict
from datetime import datetime


class DataExporter:
    def export(self, data):
        pass

    def get_format_name(self):
        pass

    def validate_data(self, data):
        if len(data) == 0:
            print(f"{data} is empty")
            return False
        else:
            print(f"{data} is valid")
            return True


class JSONExporter(DataExporter):
    def export(self, data):
        if not self.validate_data(data):
            return
        dt = {"time": datetime.now().isoformat(), "data": data}
        file = json.dumps(dt, ensure_ascii=False, indent=4)
        f = open("jsonfile.json", "w", encoding="utf-8")
        f.write(file)
        f.close()

    def get_format_name(self):
        return "json"


class CSVExporter(DataExporter):
    def export(self, data):
        if not self.validate_data(data):
            return
        fieldnames = data[0].keys()
        f = open("csvfile.csv", "w", newline="", encoding="utf-8")
        cvsfile_ = csv.DictWriter(f, fieldnames=fieldnames)
        cvsfile_.writeheader()
        for row in data:
            cvsfile_.writerow(row)
        f.close()

    def get_format_name(self):
        return "csv"


class XMLExporter(DataExporter):
    def get_format_name(self):
        return "xml"

    def export(self, data):
        if not self.validate_data(data):
            return
        xml_data = {"report": {"item": data}}
        xml_string = xmltodict.unparse(xml_data, pretty=True)
        f = open("xmlfile.xml", "w", encoding="utf-8")
        f.write(xml_string)
        f.close()


# Этот код должен работать после реализации:
sales_data = [{"product": "Laptop", "price": 1000, "quantity": 2}, {"product": "Mouse", "price": 50, "quantity": 10}]

exporters = [CSVExporter(), XMLExporter(), JSONExporter()]

for exporter in exporters:
    print(f"Формат: {exporter.get_format_name()}")
    exporter.export(sales_data)
    print("---")
