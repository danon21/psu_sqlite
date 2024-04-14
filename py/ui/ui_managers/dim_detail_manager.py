from PyQt5.QtWidgets import QMessageBox
from py.ui.ui_class.create_dim_backup import Ui_DialogCreateDimBackup

from py.src.models import Detail
# from py.gui_manager import GUIManager

class Manager_DimRowDetail(Ui_DialogCreateDimBackup):
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
            self.pushButton_save.clicked.connect(self.create_detail)

        self.lineEdit_name.setText('')
    
    def setupUi_by_model(self, detail: Detail):
        self.setupUi_without_model()  
        self.pushButton_save.clicked.disconnect()
        self.pushButton_save.clicked.connect(lambda: self.update_detail(detail.d_code))
        self.lineEdit_name.setText(detail.d_name)
    
    def show_window(self, parent, model = None):
        if model:
            self.setupUi_by_model(model)
        else:
            self.setupUi_without_model()

        self.gui_manager.show_dialog_and_block_main(
            dialog=self.gui_manager.form_dim_detail,
            main=parent
        )
        self.gui_manager.form_dim_detail.exec_()
        self.gui_manager.unlock_main_window(parent)

    def create_detail(self, detail_id = None):
        try:
            model = Detail()
            if detail_id:
                model.d_code = detail_id
            model.d_name = self.lineEdit_name.text()
            
            if detail_id:
                res = self.gui_manager.db_manager.update_by_model(model)
            else:
                res = self.gui_manager.db_manager.create_by_model(model)
            if not res: 
                raise Exception

            QMessageBox.information(self.gui_manager.form_dim_detail, "Успех", "Строка успешно сохранена в базу данных", QMessageBox.Ok)
            self.gui_manager.form_dim_detail.accept()
        except Exception as e:
            print(e)
            QMessageBox.warning(self.gui_manager.form_dim_detail, "Ошибка", "Возникла ошибка при сохранении в базу данных!")
    
    def update_detail(self, code):
        self.create_detail(code);

    def cancel(self):
        self.gui_manager.form_dim_detail.accept()