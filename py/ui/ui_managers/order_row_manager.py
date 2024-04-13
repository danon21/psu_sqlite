from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QDate
from py.ui.ui_class.order_row import Ui_DialogViewerRowOrder
from datetime import datetime

from py.src.models import Order
# from py.gui_manager import GUIManager

class Manager_OrderRow(Ui_DialogViewerRowOrder):
    def __init__(self, gui_manager=None):
    # def __init__(self, gui_manager : GUIManager=None):
        super().__init__()
        self.gui_manager = gui_manager

    def setupUi(self, MainWindowViewerReports):
        Ui_DialogViewerRowOrder.setupUi(self, MainWindowViewerReports)
        self.pushButton_cancel.clicked.connect(self.cancel)
    
    def setupUi_without_model(self):
        try:
            self.pushButton_save.clicked.disconnect(self.update_order)
        except Exception:
            pass
        finally:
            self.pushButton_save.clicked.connect(self.create_order)
        self.doubleSpinBox_cost.setMaximum(100000)
        self.doubleSpinBox_cost.setValue(0)

        self.gui_manager.combobox_manager.fill_combobox_by_dict(
            self.comboBox_car_color,
            self.gui_manager.db_manager.get_color_dict()
        )
        self.gui_manager.combobox_manager.fill_combobox_by_dict(
            self.comboBox_car_mode,
            self.gui_manager.db_manager.get_brand_dict()
        )
        self.gui_manager.combobox_manager.fill_combobox_by_dict(
            self.comboBox_client,
            self.gui_manager.db_manager.get_client_dict()
        )
        self.gui_manager.combobox_manager.fill_combobox_by_dict(
            self.comboBox_detail,
            self.gui_manager.db_manager.get_detail_dict()
        )
        self.gui_manager.combobox_manager.fill_combobox_by_dict(
            self.comboBox_emp,
            self.gui_manager.db_manager.get_personnals_dict()
        )
        self.gui_manager.combobox_manager.fill_combobox_by_dict(
            self.comboBox_type_work,
            self.gui_manager.db_manager.get_work_type_dict()
        )

        curr_date = datetime.now()
        self.dateEdit.setDate(
            QDate(curr_date.year, curr_date.month, curr_date.day)
        )

        self.comboBox_car_color.setCurrentIndex(0)
        self.comboBox_car_mode.setCurrentIndex(0)
        self.comboBox_client.setCurrentIndex(0)
        self.comboBox_detail.setCurrentIndex(0)
        self.comboBox_emp.setCurrentIndex(0)
        self.comboBox_type_work.setCurrentIndex(0)

        self.label_4.setText(f'{self.label_4.text().split()[0]}')
    
    def setupUi_by_model(self, order: Order):
        self.setupUi_without_model()  
        self.pushButton_save.clicked.disconnect(self.create_order)
        self.pushButton_save.clicked.connect(self.update_order)

        self.gui_manager.combobox_manager.select_element_by_code(
            self.comboBox_car_color,
            order.o_color
        )
        self.gui_manager.combobox_manager.select_element_by_code(
            self.comboBox_car_mode,
            order.o_car_brand
        )
        self.gui_manager.combobox_manager.select_element_by_code(
            self.comboBox_client,
            order.o_c_code
        )
        self.gui_manager.combobox_manager.select_element_by_code(
            self.comboBox_detail,
            order.o_detail
        )
        self.gui_manager.combobox_manager.select_element_by_code(
            self.comboBox_emp,
            order.o_p_code
        )
        self.gui_manager.combobox_manager.select_element_by_code(
            self.comboBox_type_work,
            order.o_type_work
        )
        
        date = datetime.fromtimestamp(order.o_date)
        self.dateEdit.setDate(
            QDate(date.year, date.month, date.day)
        )
        self.label_4.setText(f'{self.label_4.text().split()[0]} {order.o_code}')
        self.checkBox_done.setTristate(order.o_state != 1)
        self.doubleSpinBox_cost.setValue(order.o_price)
    
    def show_window(self, parent, model = None):
        if model:
            self.setupUi_by_model(model)
        else:
            self.setupUi_without_model()

        self.gui_manager.show_dialog_and_block_main(
            dialog=self.gui_manager.form_order,
            main=parent
        )
        self.gui_manager.form_order.exec_()
        self.gui_manager.unlock_main_window(parent)

    def create_order(self, order_id = None):
        try:
            model = Order()
            if order_id:
                model.o_code = order_id
            model.o_color = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_car_color)
            model.o_car_brand = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_car_mode)
            model.o_c_code = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_client)
            model.o_detail = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_detail)
            model.o_p_code = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_emp)
            model.o_type_work = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_type_work)
            model.o_state = 2 if self.checkBox_done.isChecked() else 1
            model.o_price = self.doubleSpinBox_cost.value()
            date = self.dateEdit.date().toPyDate()
            datetime_with_time = datetime.combine(date, datetime.now().time())
            model.o_date = int(datetime_with_time.timestamp())
            
            if order_id:
                res = self.gui_manager.db_manager.update_by_model(model)
            else:
                res = self.gui_manager.db_manager.create_by_model(model)
            if not res: 
                raise Exception

            QMessageBox.information(self.gui_manager.form_order, "Успех", "Строка успешно добавлена в базу данных", QMessageBox.Ok)
            self.gui_manager.form_order.accept()
        except Exception as e:
            print(e)
            QMessageBox.warning(self.gui_manager.form_order, "Ошибка", "Возникла ошибка при сохранении заказа в базу данных!")
    
    def update_order(self):
        code = int(self.label_4.text().split(" ")[1])
        self.create_order(code);

    def cancel(self):
        self.gui_manager.form_order.accept()
