from PyQt5.QtWidgets import QMessageBox
from py.ui.ui_class.create_dim_backup import Ui_DialogCreateDimBackup

from py.src.models import WorkType
# from py.gui_manager import GUIManager

class Manager_DimRowTypeWork(Ui_DialogCreateDimBackup):
    def __init__(self, gui_manager=None):
    # def __init__(self, gui_manager : GUIManager=None):
        super().__init__()
        self.gui_manager = gui_manager

    def setupUi(self, MainWindowViewerReports):
        Ui_DialogCreateDimBackup.setupUi(self, MainWindowViewerReports)
        self.pushButton_cancel.clicked.connect(self.cancel)
    
    def setupUi_without_model(self):
        try:
            self.pushButton_save.clicked.disconnect()
        except Exception:
            pass
        finally:
            self.pushButton_save.clicked.connect(self.create_type_work)

        self.lineEdit_name.setText('')
    
    def setupUi_by_model(self, type_work: WorkType):
        self.setupUi_without_model()  
        self.pushButton_save.clicked.disconnect()
        self.pushButton_save.clicked.connect(lambda: self.update_type_work(type_work.w_code))
        self.lineEdit_name.setText(type_work.w_name)
    
    def show_window(self, parent, model = None):
        if model:
            self.setupUi_by_model(model)
        else:
            self.setupUi_without_model()

        self.gui_manager.show_dialog_and_block_main(
            dialog=self.gui_manager.form_dim_type_work,
            main=parent
        )
        self.gui_manager.form_dim_type_work.exec_()
        self.gui_manager.unlock_main_window(parent)

    def create_type_work(self, type_work_id = None):
        try:
            model = WorkType()
            if type_work_id:
                model.w_code = type_work_id
            model.w_name = self.lineEdit_name.text()
            
            if type_work_id:
                res = self.gui_manager.db_manager.update_by_model(model)
            else:
                res = self.gui_manager.db_manager.create_by_model(model)
            if not res: 
                raise Exception

            QMessageBox.information(self.gui_manager.form_dim_type_work, "Успех", "Строка успешно сохранена в базу данных", QMessageBox.Ok)
            self.gui_manager.form_dim_type_work.accept()
        except Exception as e:
            print(e)
            QMessageBox.warning(self.gui_manager.form_dim_type_work, "Ошибка", "Возникла ошибка при сохранении в базу данных!")
    
    def update_type_work(self, code):
        self.create_type_work(code);

    def cancel(self):
        self.gui_manager.form_dim_type_work.accept()