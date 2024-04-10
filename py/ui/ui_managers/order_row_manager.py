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
        self.pushButton_save.clicked.connect(self.create_order)

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
    
    def setup_by_model(self, order: Order):
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

        self.checkBox_done.setTristate(order.o_state != 1)
        self.doubleSpinBox_cost.setValue(order.o_price)
    
    def create_order(self):
        try:
            model = Order()
            model.o_color = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_car_color)
            model.o_car_brand = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_car_mode)
            model.o_c_code = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_client)
            model.o_detail = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_detail)
            model.o_p_code = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_emp)
            model.o_type_work = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_type_work)
            model.o_state = 2 if self.checkBox_done.isChecked else 1
            model.o_price = self.doubleSpinBox_cost.value
            date = self.dateEdit.date().toPyDate()
            datetime_with_time = datetime.combine(date, time=datetime.now().time())
            model.o_date = int(datetime_with_time.timestamp())
            self.gui_manager.db_manager.create_by_model(model)

            self.gui_manager.form_order.accept()
        except Exception as e:
            print(e)
            QMessageBox.warning(self.gui_manager.form_order, "Ошибка", "Возникла ошибка при сохранении заказа в базу данных!")
    
    def cancel(self):
        self.gui_manager.form_order.accept()
