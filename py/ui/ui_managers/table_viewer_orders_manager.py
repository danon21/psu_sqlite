from PyQt5.QtWidgets import QFileDialog, QMessageBox
from py.ui.ui_class.table_viewer import Ui_Dialog

# from py.gui_manager import GUIManager

class Manager_DialogTableOrder(Ui_Dialog):
    def __init__(self, gui_manager=None):
    # def __init__(self, gui_manager : GUIManager=None):
        super().__init__()
        self.gui_manager = gui_manager

    def setupUi(self, DialogStartAppDbChange):
        Ui_Dialog.setupUi(self, DialogStartAppDbChange)
        self.gui_manager.combobox_manager.fill_combobox_by_dict(
            self.comboBox_row,
            self.gui_manager.db_manager.get_order_dict()
        )
        self.pushButton_create_new_row.clicked.connect(self.create_new_row)
    
    def create_new_row(self):
        self.gui_manager.ui_form_order.setupUi(self.gui_manager.form_order)
        self.gui_manager.show_dialog_and_block_main(
            dialog=self.gui_manager.form_order,
            main=self.gui_manager.view_table_orders
        )
        self.gui_manager.form_order.exec_()
        self.gui_manager.unlock_main_window(self.gui_manager.view_table_orders)