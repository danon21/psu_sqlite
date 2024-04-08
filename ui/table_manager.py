from PyQt5.QtGui import QStandardItem, QStandardItemModel
import datetime

class TableManager:
    def __init__(self):
        self.order_headers = ['Код заказа', 'Мастер', 'Клиент', 'Дата', 'Статус работы', 'Марка автомобиля', 'Детали', 'Вид работы', 'Цвет', 'Цена']
        self.order_attributes = ['o_code', 'o_p_code', 'o_c_code', 'o_date', 'o_state', 'o_car_brand', 'o_detail', 'o_type_work', 'o_color', 'o_price']

    def fill_order_table(self, table_view, orders, dict_clients, dict_personnel = None):
        model = QStandardItemModel()
        model.setColumnCount(len(self.order_headers))
        model.setHorizontalHeaderLabels(self.order_headers)

        for order in orders:
            row = []
            for attribute in self.order_attributes:
                if attribute == 'o_p_code':
                    value = dict_personnel.get(getattr(order, attribute), '---')
                elif attribute == 'o_c_code':
                    value = dict_clients.get(getattr(order, attribute), '---')
                elif attribute == 'o_date':
                    date = datetime.datetime.fromtimestamp(getattr(order, attribute))
                    value = date.strftime('%d.%m.%Y')
                elif attribute == 'o_state':
                    if getattr(order, attribute) == 1:
                        value = 'В работе'
                    else:
                        value = 'Выполнено'
                else:
                    value = getattr(order, attribute)
                item = QStandardItem(str(value))
                row.append(item)
            model.appendRow(row)

        table_view.setModel(model)