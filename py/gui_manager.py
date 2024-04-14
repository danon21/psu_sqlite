from PyQt5 import QtWidgets
from py.ui.combo_box_manager import ComboBoxManager
from py.src.table_manager import TableManager
from py.ui.list_widget_manager import ListManager
from py.ui.ui_class.dim_elements import Ui_DialogViewerDimElements
from py.ui.ui_class.create_dim_backup import Ui_DialogCreateDimBackup
from py.ui.ui_managers.choise_db_manager import Manager_DialogStartAppDbChange
from py.ui.ui_managers.report_manager import Manager_MainWindowViewerReports
from py.ui.ui_managers.create_backup_manager import Manager_DialogCreateBackup
from py.ui.ui_managers.table_viewer_orders_manager import Manager_DialogTableOrder
from py.ui.ui_managers.table_viewer_clients_manager import Manager_DialogTableClient
from py.ui.ui_managers.table_viewer_emp_manager import Manager_DialogTableEmp
from py.ui.ui_managers.row_order_manager import Manager_OrderRow
from py.ui.ui_managers.row_client_manager import Manager_OrderClient
from py.ui.ui_managers.row_empl_manager import Manager_RowEmp
from py.ui.ui_managers.dim_viewer_brand_manager import Manager_DimViewBrand
from py.ui.ui_managers.dim_viewer_detail_manager import Manager_DimViewDetail
from py.ui.ui_managers.dim_viewer_color_manager import Manager_DimViewColor
from py.ui.ui_managers.dim_viewer_work_manager import Manager_DimViewTypeWork
from py.ui.ui_managers.dim_brand_manager import Manager_DimRowBrand
from py.ui.ui_managers.dim_detail_manager import Manager_DimRowDetail
from py.ui.ui_managers.dim_color_manager import Manager_DimRowColor 
from py.ui.ui_managers.dim_work_manager import Manager_DimRowTypeWork 


from py.db_manager import DatabaseManager


class GUIManager:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.table_manager = TableManager()
        self.combobox_manager = ComboBoxManager()
        self.list_manager = ListManager()

        self.report = QtWidgets.QMainWindow()
        
        self.view_table_orders = QtWidgets.QDialog()
        self.view_table_clients = QtWidgets.QDialog()
        self.view_table_emp = QtWidgets.QDialog()
        self.form_client = QtWidgets.QDialog()
        self.form_empl = QtWidgets.QDialog()
        self.form_order = QtWidgets.QDialog()

        self.view_dim_brand = QtWidgets.QDialog()
        self.view_dim_color = QtWidgets.QDialog()
        self.view_dim_detail = QtWidgets.QDialog()
        self.view_dim_type_work = QtWidgets.QDialog()
        self.form_dim_brand = QtWidgets.QDialog()
        self.form_dim_color = QtWidgets.QDialog()
        self.form_dim_detail = QtWidgets.QDialog()
        self.form_dim_type_work = QtWidgets.QDialog()

        self.form_backup = QtWidgets.QDialog()
        self.choise_db = QtWidgets.QDialog()

        self.ui_report = Manager_MainWindowViewerReports(self)
        self.ui_view_table_orders = Manager_DialogTableOrder(self)
        self.ui_view_table_clients = Manager_DialogTableClient(self)
        self.ui_view_table_emp = Manager_DialogTableEmp(self)
        self.ui_form_client = Manager_OrderClient(self)
        self.ui_form_empl = Manager_RowEmp(self)
        self.ui_form_order = Manager_OrderRow(self)
        
        self.ui_view_dim_brand = Manager_DimViewBrand(self)
        self.ui_view_dim_color = Manager_DimViewColor(self)
        self.ui_view_dim_detail = Manager_DimViewDetail(self)
        self.ui_view_dim_type_work = Manager_DimViewTypeWork(self)
        self.ui_form_dim_brand = Manager_DimRowBrand(self)
        self.ui_form_dim_color = Manager_DimRowColor(self)
        self.ui_form_dim_detail = Manager_DimRowDetail(self)
        self.ui_form_dim_type_work = Manager_DimRowTypeWork(self)

        self.ui_form_backup = Manager_DialogCreateBackup(self)
        self.ui_choise_db = Manager_DialogStartAppDbChange(self)

        self.ui_report.setupUi(self.report) 
        self.ui_view_table_orders.setupUi(self.view_table_orders)
        self.ui_view_table_clients.setupUi(self.view_table_clients)
        self.ui_view_table_emp.setupUi(self.view_table_emp)
        self.ui_form_client.setupUi(self.form_client) 
        self.ui_form_empl.setupUi(self.form_empl) 
        self.ui_form_order.setupUi(self.form_order)

        self.ui_view_dim_brand.setupUi(self.view_dim_brand)
        self.ui_view_dim_color.setupUi(self.view_dim_color)
        self.ui_view_dim_detail.setupUi(self.view_dim_detail)
        self.ui_view_dim_type_work.setupUi(self.view_dim_type_work)
        self.ui_form_dim_brand.setupUi(self.form_dim_brand)
        self.ui_form_dim_color.setupUi(self.form_dim_color)
        self.ui_form_dim_detail.setupUi(self.form_dim_detail)
        self.ui_form_dim_type_work.setupUi(self.form_dim_type_work)
        
        self.ui_form_backup.setupUi(self.form_backup)
        self.ui_choise_db.setupUi(self.choise_db)

    def create_connect_db(self, connect_string):
        try:
            self.db_manager = DatabaseManager(connect_string)
            self.db_manager.get_all_personnel()
            return True
        except Exception:
            return False

    def show_dialog_and_block_main(self, main, dialog):
        dialog.show()
        main.setEnabled(False)

    def unlock_main_window(self, main):
        main.setEnabled(True)

    def start_application(self):
        self.report.show()
        self.show_dialog_and_block_main(self.report, self.choise_db)
        self.choise_db.exec_()
        self.ui_report.fill_all_combobox()
        self.ui_report.clear_table()
        self.unlock_main_window(self.report)
    
    def save_backup(self):
        self.show_dialog_and_block_main(self.report, self.form_backup)
        self.form_backup.exec_()
        self.unlock_main_window(self.report)
    
    def clearLayout(self, layout):
        if layout:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
                if child.layout():
                    self.clearLayout(child.layout())


        



