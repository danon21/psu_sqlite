from PyQt5.QtWidgets import QFileDialog, QMessageBox
from py.ui.ui_class.table_viewer import Ui_Dialog

# from py.gui_manager import GUIManager

class Manager_DialogTableEmp(Ui_Dialog):
    def __init__(self, gui_manager=None):
    # def __init__(self, gui_manager : GUIManager=None):
        super().__init__()
        self.gui_manager = gui_manager

    def setupUi(self, DialogStartAppDbChange):
        Ui_Dialog.setupUi(self, DialogStartAppDbChange)
        self.DialogViewerTable.verticalHeader().setVisible(False)
        self.pushButton_create_new_row.clicked.connect(self.create_new_row)
        self.pushButton_edit_row.clicked.connect(self.edit_row)
        self.pushButton_delete_row.clicked.connect(self.delete_win)

    def setup_combobox(self):
        self.gui_manager.combobox_manager.fill_combobox_by_dict(
            self.comboBox_row,
            self.gui_manager.db_manager.get_personnals_dict()
        )

    def fill_table(self):
        self.gui_manager.table_manager.clear_table(self.DialogViewerTable)
        emp = self.gui_manager.db_manager.get_all_personnel()
        self.gui_manager.table_manager.fill_personnel_table(
            self.DialogViewerTable,
            emp
        )
        self.gui_manager.table_manager.adjust_columns(self.DialogViewerTable)
    
    def create_new_row(self):
        self.gui_manager.ui_form_empl.show_window(self.gui_manager.view_table_emp)
        self.fill_table()

    def delete_row(self, model):
        try:
            self.gui_manager.db_manager.delete_by_model(model)
            QMessageBox.information(self.gui_manager.view_table_emp, "Успех", "Строка успешно удалена.", QMessageBox.Ok)
        except Exception:
            QMessageBox.warning(self.gui_manager.view_table_emp, "Ошибка", "Возникла ошибка при удалении клиента.")

    def delete_win(self):
        emp_id = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_row)
        emp = self.gui_manager.db_manager.get_personnel_by_code(emp_id)
        msg_box = QMessageBox(self.gui_manager.view_table_clients)
        msg_box.setWindowTitle("Удаление строки")
        msg_box.setText(f"Вы уверены, что хотите удалить строку {emp_id}?")
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        result = msg_box.exec_()

        if result == QMessageBox.Ok:
            self.delete_row(emp)
        
        self.fill_table()
        self.setup_combobox()

    def edit_row(self):
        emp_id = self.gui_manager.combobox_manager.get_selected_element_code(self.comboBox_row)
        emp = self.gui_manager.db_manager.get_personnel_by_code(emp_id)
        self.gui_manager.ui_form_empl.show_window(self.gui_manager.view_table_clients, emp)
        self.fill_table()