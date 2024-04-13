from PyQt5.QtWidgets import QMainWindow, QMessageBox
from py.ui.ui_class.row_empl import Ui_DialogViewerRowEmpl

from py.src.models import Personnel
# from py.gui_manager import GUIManager

class Manager_RowEmp(Ui_DialogViewerRowEmpl):
    def __init__(self, gui_manager=None):
    # def __init__(self, gui_manager : GUIManager=None):
        super().__init__()
        self.gui_manager = gui_manager

    def setupUi(self, MainWindowViewerReports):
        Ui_DialogViewerRowEmpl.setupUi(self, MainWindowViewerReports)
        self.pushButton_cancel.clicked.connect(self.cancel)
    
    def setupUi_without_model(self):
        try:
            self.pushButton_save.clicked.disconnect(self.update_emp)
        except Exception:
            pass
        finally:
            self.pushButton_save.clicked.connect(self.create_emp)

        self.lineEdit_address.setText('')
        self.lineEdit_full_name.setText('')
        self.lineEdit_job_title.setText('')
        self.lineEdit_phone.setText('')

        self.label_4.setText(f'{self.label_4.text().split()[0]}')
    
    def setupUi_by_model(self, emp: Personnel):
        self.setupUi_without_model()  
        self.pushButton_save.clicked.disconnect(self.create_emp)
        self.pushButton_save.clicked.connect(self.update_emp)

        self.label_4.setText(f'{self.label_4.text().split()[0]} {emp.p_code}')
        self.lineEdit_address.setText(emp.p_address)
        self.lineEdit_full_name.setText(emp.p_full_name)
        self.lineEdit_phone.setText(emp.p_telephone)
        self.lineEdit_job_title.setText(emp.p_job_title)
    
    def show_window(self, parent, model = None):
        if model:
            self.setupUi_by_model(model)
        else:
            self.setupUi_without_model()

        self.gui_manager.show_dialog_and_block_main(
            dialog=self.gui_manager.form_empl,
            main=parent
        )
        self.gui_manager.form_empl.exec_()
        self.gui_manager.unlock_main_window(parent)

    def create_emp(self, emp_id = None):
        try:
            model = Personnel()
            if emp_id:
                model.p_code = emp_id
            model.p_address = self.lineEdit_address.text()
            model.p_full_name = self.lineEdit_full_name.text()
            model.p_telephone = self.lineEdit_phone.text()
            model.p_job_title = self.lineEdit_job_title.text()
            
            if emp_id:
                res = self.gui_manager.db_manager.update_by_model(model)
            else:
                res = self.gui_manager.db_manager.create_by_model(model)
            if not res: 
                raise Exception

            QMessageBox.information(self.gui_manager.form_empl, "Успех", "Строка успешно добавлена в базу данных", QMessageBox.Ok)
            self.gui_manager.form_empl.accept()
        except Exception as e:
            print(e)
            QMessageBox.warning(self.gui_manager.form_empl, "Ошибка", "Возникла ошибка при сохранении работника в базу данных!")
    
    def update_emp(self):
        code = int(self.label_4.text().split(" ")[1])
        self.create_emp(code);

    def cancel(self):
        self.gui_manager.form_empl.accept()