from PyQt5.QtWidgets import QFileDialog, QMessageBox
from py.ui.ui_class.choise_db import Ui_DialogStartAppDbChange

class Manager_DialogStartAppDbChange(Ui_DialogStartAppDbChange):
    def __init__(self, gui_manager=None):
        super().__init__()
        self.gui_manager = gui_manager

    def setupUi(self, DialogStartAppDbChange):
        Ui_DialogStartAppDbChange.setupUi(self, DialogStartAppDbChange)
        self.lineEdit.setEnabled(False)
        self.pushButton_choiseFile.clicked.connect(self.open_file_dialog)
        self.pushButton_startApp.clicked.connect(self.get_database_path)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self.gui_manager.choise_db, "Выберите файл базы данных", "", "Database Files (*.db *.sqlite)")
        if file_path:
            self.lineEdit.setText(file_path)

    def get_database_path(self):
        database_path = self.lineEdit.text()
        if self.gui_manager.create_connect_db(database_path):
            self.gui_manager.choise_db.accept()
        else:
            QMessageBox.warning(self.gui_manager.choise_db, "Ошибка", "Некорректный файл базы данных!")