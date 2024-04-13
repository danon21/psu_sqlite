from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5 import QtWidgets
import datetime

class TableManager:
    def __init__(self):
        self.order_headers = ['Код заказа', 'Мастер', 'Клиент', 'Дата', 'Статус работы', 'Марка автомобиля', 'Детали', 'Вид работы', 'Цвет', 'Цена']
        self.order_attributes = ['o_code', 'o_p_code', 'o_c_code', 'o_date', 'o_state', 'o_car_brand', 'o_detail', 'o_type_work', 'o_color', 'o_price']
        self.client_headers = ['Код клиента', 'ФИО', 'Телефон', 'Адрес']
        self.client_attributes = ['c_code', 'c_full_name', 'c_telephone', 'c_address']
        self.personnel_headers = ['Код работника', 'ФИО', 'Телефон', 'Адрес', 'Должность']
        self.personnel_attributes = ['p_code', 'p_full_name', 'p_telephone', 'p_address', 'p_job_title']

    def adjust_columns(self, table_view):
        table_view.resizeColumnsToContents()
        header = table_view.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

    def clear_table(self, table_view):
        model = table_view.model()
        if model is not None:
            model.removeRows(0, model.rowCount())


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
    
    def fill_client_table(self, table_view, clients):
        model = QStandardItemModel()
        model.setColumnCount(len(self.client_headers))
        model.setHorizontalHeaderLabels(self.client_headers)

        for client in clients:
            row = []
            for attribute in self.client_attributes:
                value = getattr(client, attribute)
                item = QStandardItem(str(value))
                row.append(item)
            model.appendRow(row)

        table_view.setModel(model)
    
    def fill_personnel_table(self, table_view, personnels):
        model = QStandardItemModel()
        model.setColumnCount(len(self.personnel_headers))
        model.setHorizontalHeaderLabels(self.personnel_headers)

        for personnel in personnels:
            row = []
            for attribute in self.personnel_attributes:
                value = getattr(personnel, attribute)
                item = QStandardItem(str(value))
                row.append(item)
            model.appendRow(row)

        table_view.setModel(model)
    
    def fill_order_table2(self, table_view, orders, dimensions : dict = None):
        model = QStandardItemModel()
        model.setColumnCount(len(self.order_headers))
        model.setHorizontalHeaderLabels(self.order_headers)

        for order in orders:
            row = []
            for attribute in self.order_attributes:
                if attribute == 'o_p_code':
                    value = dimensions.get('personnals', dict()).get(getattr(order, attribute), '---')
                elif attribute == 'o_c_code':
                    value = dimensions.get('clients', dict()).get(getattr(order, attribute), '---')
                elif attribute == 'o_car_brand':
                    value = dimensions.get('brands', dict()).get(getattr(order, attribute), '---')
                elif attribute == 'o_detail':
                    value = dimensions.get('details', dict()).get(getattr(order, attribute), '---')
                elif attribute == 'o_type_work':
                    value = dimensions.get('work_type', dict()).get(getattr(order, attribute), '---')
                elif attribute == 'o_color':
                    value = dimensions.get('colors', dict()).get(getattr(order, attribute), '---')
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