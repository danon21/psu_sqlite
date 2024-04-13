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
        self.DialogViewerTable.verticalHeader().setVisible(False)
        self.pushButton_create_new_row.clicked.connect(self.create_new_row)
        self.pushButton_edit_row.clicked.connect(self.edit_row)

    def fill_table(self):
        self.gui_manager.table_manager.clear_table(self.DialogViewerTable)
        orders = self.gui_manager.db_manager.get_all_orders()
        self.gui_manager.table_manager.fill_order_table2(
            self.DialogViewerTable,
            orders,
            self.gui_manager.db_manager.get_dimensions_dict()
        )
        self.gui_manager.table_manager.adjust_columns(self.gui_manager.ui_report.tableView_date)
    
    def create_new_row(self):
        self.gui_manager.ui_form_order.show_window(self.gui_manager.view_table_orders)
        self.fill_table()

    def edit_row(self):
        order_id = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_row)
        order = self.gui_manager.db_manager.get_order_by_code(order_id)
        self.gui_manager.ui_form_order.show_window(self.gui_manager.view_table_orders, order)

