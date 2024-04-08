import sys
from constants import PATH_DB_FILE
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main_window import Ui_MainWindow
from data.database_manager import DatabaseManager
from ui.table_manager import TableManager

class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = QMainWindow()
        self.ui_manager = Ui_MainWindow()
        self.db_manager = DatabaseManager(db_file=PATH_DB_FILE)
        self.table_manager = TableManager()

    def setup_ui(self):
        self.ui_manager.setupUi(self.main_window)

    def fill_combo_boxes(self):
        personnel_list = self.db_manager.get_all_personnel()
        self.table_manager.fill_employee_combo(self.ui_manager.comboBox_Emp, personnel_list)

    def fill_tables(self):
        orders = self.db_manager.get_all_orders()
        self.table_manager.fill_order_table(self.ui_manager.tableView_reprotEmp, orders)
        self.table_manager.link_scrollbar_to_table(self.ui_manager.tableView_reprotEmp, self.ui_manager.verticalScrollBar_reprotEmp)

    def run(self):
        self.setup_ui()
        self.fill_combo_boxes()
        self.fill_tables()
        self.main_window.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = Application()
    app.run()