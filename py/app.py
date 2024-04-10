import sys
from py.constants import PATH_DB_FILE
from PyQt5.QtWidgets import QApplication, QMainWindow
from py.gui_manager import GUIManager
from py.ui.ui_class.main_window_report import Ui_MainWindowViewerReports
from py.db_manager import DatabaseManager
from py.src.table_manager import TableManager
from py.ui.combo_box_manager import ComboBoxManager

class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.gui_manager = GUIManager()
        self.db_manager = self.gui_manager.db_manager
        self.table_manager = TableManager()
        self.combo_box_manager = ComboBoxManager()

    def run(self):
        self.gui_manager.start_application()
        sys.exit(self.app.exec_())
    
    def connect_handlers(self):
        self.ui_manager.pushButton_report_date.clicked.connect(self.fill_report_table_date)
        self.ui_manager.pushButton_report_emp.clicked.connect(self.fill_report_table_emp)

    # def fill_combo_boxes(self):
    #     personnel_list = self.db_manager.get_all_personnel()
    #     self.combo_box_manager.fill_year_combo(self.ui_manager.comboBox_year)
    #     self.combo_box_manager.fill_month_combo(self.ui_manager.comboBox_month)
    #     self.combo_box_manager.fill_employee_combo(self.ui_manager.comboBox_emp, personnel_list)