from PyQt5.QtWidgets import QMainWindow, QMessageBox
from py.ui.ui_class.main_window_report import Ui_MainWindowViewerReports

# from py.gui_manager import GUIManager

class Manager_MainWindowViewerReports(Ui_MainWindowViewerReports):
    def __init__(self, gui_manager=None):
    # def __init__(self, gui_manager : GUIManager=None):
        super().__init__()
        self.gui_manager = gui_manager

    def setupUi(self, MainWindowViewerReports):
        Ui_MainWindowViewerReports.setupUi(self, MainWindowViewerReports)
        self.action_open_db_file.triggered.connect(self.gui_manager.start_application)
        
        self.action_backup.triggered.connect(self.gui_manager.save_backup)
        self.action_orders.triggered.connect(self.show_table_orders)
        self.action_clients.triggered.connect(self.show_table_clients)
        self.action_emps.triggered.connect(self.show_table_emp)
        
        self.action_add_order.triggered.connect(self.create_new_row)
        self.action_reg_client.triggered.connect(self.create_new_client)
        self.action_reg_emp.triggered.connect(self.create_new_emp)

        self.pushButton_report_date.clicked.connect(self.fill_report_table_date)
        self.pushButton_report_emp.clicked.connect(self.fill_report_table_emp)


    def fill_report_table_date(self):
        start_date, finish_date = self.gui_manager.combobox_manager.get_selected_date(
            self.gui_manager.combobox_manager.get_selected_month(self.gui_manager.ui_report.comboBox_month),
            self.gui_manager.combobox_manager.get_selected_year(self.gui_manager.ui_report.comboBox_year)
        )
        orders = self.gui_manager.db_manager.get_orders_by_date_range(start_date=start_date, end_date=finish_date)
        self.gui_manager.table_manager.fill_order_table2(
            self.gui_manager.ui_report.tableView_date,
            orders,
            self.gui_manager.db_manager.get_dimensions_dict()
        )
        self.gui_manager.table_manager.adjust_columns(self.gui_manager.ui_report.tableView_date)

    def fill_report_table_emp(self):
        orders = self.gui_manager.db_manager.get_orders_by_personnel(
            self.gui_manager.combobox_manager.get_selected_element_code(
                self.gui_manager.ui_report.comboBox_emp
            )
        )
        self.gui_manager.table_manager.fill_order_table2(
            self.gui_manager.ui_report.tableView_emp,
            orders,
            self.gui_manager.db_manager.get_dimensions_dict(),
        )
        self.gui_manager.table_manager.adjust_columns(self.gui_manager.ui_report.tableView_emp)
    

    def show_table_orders(self):
        self.gui_manager.ui_view_table_orders.setup_combobox()
        self.gui_manager.show_dialog_and_block_main(
            dialog=self.gui_manager.view_table_orders,
            main=self.gui_manager.report
        )
        self.gui_manager.ui_view_table_orders.fill_table()
        self.gui_manager.view_table_orders.exec_()
        self.gui_manager.unlock_main_window(self.gui_manager.report)
    
    def show_table_clients(self):
        self.gui_manager.ui_view_table_clients.setup_combobox()
        self.gui_manager.show_dialog_and_block_main(
            dialog=self.gui_manager.view_table_clients,
            main=self.gui_manager.report
        )
        self.gui_manager.ui_view_table_clients.fill_table()
        self.gui_manager.view_table_clients.exec_()
        self.gui_manager.unlock_main_window(self.gui_manager.report)
    
    def show_table_emp(self):
        self.gui_manager.ui_view_table_emp.setup_combobox()
        self.gui_manager.show_dialog_and_block_main(
            dialog=self.gui_manager.view_table_emp,
            main=self.gui_manager.report
        )
        self.gui_manager.ui_view_table_emp.fill_table()
        self.gui_manager.view_table_emp.exec_()
        self.gui_manager.unlock_main_window(self.gui_manager.report)
    
    def clear_table(self):
        model = self.gui_manager.ui_report.tableView_date.model()
        if model is not None:
            model.removeRows(0, model.rowCount())
    
    def fill_combobox_year(self):
        self.gui_manager.combobox_manager.fill_year_combo(self.gui_manager.ui_report.comboBox_year)
    
    def fill_combobox_month(self):
        self.gui_manager.combobox_manager.fill_month_combo(self.gui_manager.ui_report.comboBox_month)
    
    def fill_combobox_emp(self):
        self.gui_manager.combobox_manager.fill_employee_combo(
            self.gui_manager.ui_report.comboBox_emp,
            self.gui_manager.db_manager.get_all_personnel()
        )
    
    def fill_all_combobox(self):
        self.fill_combobox_year()
        self.fill_combobox_month()
        self.fill_combobox_emp()
    
    def refresh(self):
        self.gui_manager.table_manager.clear_table(self.tableView_date)
        self.fill_report_table_date()
        self.gui_manager.table_manager.clear_table(self.tableView_emp)
        self.fill_report_table_emp()
        self.fill_all_combobox()

    def create_new_row(self):
        self.gui_manager.ui_form_order.show_window(self.gui_manager.report)
        self.refresh()
        
    
    def create_new_client(self):
        self.gui_manager.ui_form_client.show_window(self.gui_manager.report)
        self.refresh()
    
    def create_new_emp(self):
        self.gui_manager.ui_form_empl.show_window(self.gui_manager.report)
        # self.gui_manager.combobox_manager.fill_combobox_by_dict(
        #     self.comboBox_emp,
        #     self.gui_manager.db_manager.get_dimensions_dict()
        # )
        self.refresh()