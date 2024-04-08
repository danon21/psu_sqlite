from PyQt5.QtGui import QStandardItem, QStandardItemModel

class TableManager:
    def __init__(self):
        self.order_headers = ["Код заказа", "Дата", "Марка автомобиля", "Детали", "Вид работы", "Цвет", "Цена", "Код клиента"]

    def fill_order_table(self, table_view, orders):
        model = QStandardItemModel()
        model.setColumnCount(len(self.order_headers))
        model.setHorizontalHeaderLabels(self.order_headers)

        for order in orders:
            row = []
            for attribute in self.order_headers:
                value = getattr(order, f"o_{attribute.lower().replace(' ', '_')}")
                item = QStandardItem(str(value))
                row.append(item)
            model.appendRow(row)

        table_view.setModel(model)