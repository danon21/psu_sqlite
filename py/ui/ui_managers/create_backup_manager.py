import os
import shutil
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from py.ui.ui_class.create_dim_backup import Ui_DialogCreateDimBackup

# from py.gui_manager import GUIManager

class Manager_DialogCreateBackup(Ui_DialogCreateDimBackup):
    def __init__(self, gui_manager=None):
    # def __init__(self, gui_manager : GUIManager=None):
        super().__init__()
        self.gui_manager = gui_manager

    def setupUi(self, DialogStartAppDbChange):
        Ui_DialogCreateDimBackup.setupUi(self, DialogStartAppDbChange)
        self.lineEdit_name.setText('')
        self.pushButton_cancel.clicked.connect(self.cancel)
        self.pushButton_save.clicked.connect(self.save_database_as)

    def cancel(self):
        self.gui_manager.form_backup.accept()

    def save_database_as(self):
        database_path = self.gui_manager.db_manager.db_file
        file_name = self.lineEdit_name.text()
        if file_name:
            if file_name[-3:] != '.db':
                file_name += '.db'
            database_new_path = QFileDialog.getExistingDirectory(self.gui_manager.form_backup, "Выберите директорию для сохранения")
            database_new_path += '/' + file_name
            try:
                shutil.copy2(database_path, database_new_path)
                self.gui_manager.form_backup.accept()
            except Exception:
                QMessageBox.warning(self.gui_manager.choise_db, "Ошибка", "Возникла ошибка при сохранении файла базы данных!")
        else:
            QMessageBox.warning(self.gui_manager.choise_db, "Ошибка", "Введите наименование файла!")