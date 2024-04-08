import sys
from constants import PATH_DB_FILE
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main_window import Ui_MainWindow
from data.database_manager import DatabaseManager
from ui.table_manager import TableManager
from ui.combo_box_manager import ComboBoxManager

class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = QMainWindow()
        self.ui_manager = Ui_MainWindow()
        self.db_manager = DatabaseManager(db_file=PATH_DB_FILE)
        self.table_manager = TableManager()
        self.combo_box_manager = ComboBoxManager()

    def run(self):
        self.setup_ui()
        self.connect_handlers()
        self.fill_combo_boxes()
        self.main_window.show()
        sys.exit(self.app.exec_())

    def setup_ui(self):
        self.ui_manager.setupUi(self.main_window)
    
    def connect_handlers(self):
        self.ui_manager.pushButton_buildReportDate_2.clicked.connect(self.fill_report_table_date)
        self.ui_manager.pushButton_buildReportEmp_2.clicked.connect(self.fill_report_table_emp)

    def fill_combo_boxes(self):
        personnel_list = self.db_manager.get_all_personnel()
        self.combo_box_manager.fill_year_combo(self.ui_manager.comboBox_year_2)
        self.combo_box_manager.fill_month_combo(self.ui_manager.comboBox_month_2)
        self.combo_box_manager.fill_employee_combo(self.ui_manager.comboBox_Emp_2, personnel_list)

    def fill_report_table_date(self):
        start_date, finish_date = self.combo_box_manager.get_selected_date(
            self.combo_box_manager.get_selected_month(self.ui_manager.comboBox_month_2),
            self.combo_box_manager.get_selected_year(self.ui_manager.comboBox_year_2)
        )
        orders = self.db_manager.get_orders_by_date_range(start_date=start_date, end_date=finish_date)
        self.table_manager.fill_order_table(
            self.ui_manager.tableView_reprotDate_2,
            orders,
            self.db_manager.get_client_dict(),
            self.db_manager.get_personnel_dict()
        )
        self.table_manager.adjust_columns(self.ui_manager.tableView_reprotDate_2)

    def fill_report_table_emp(self):
        orders = self.db_manager.get_orders_by_personnel(
            self.combo_box_manager.get_selected_employee_code(
                self.ui_manager.comboBox_Emp_2
            )
        )
        self.table_manager.fill_order_table(
            self.ui_manager.tableView_reprotEmp_2,
            orders,
            self.db_manager.get_client_dict(),
            self.db_manager.get_personnel_dict()
        )
        self.table_manager.adjust_columns(self.ui_manager.tableView_reprotEmp_2)


if __name__ == "__main__":
    app = Application()
    app.run()