from PyQt5.QtWidgets import QMainWindow, QMessageBox
from py.ui.ui_class.row_client import Ui_DialogViewerRowClient

from py.src.models import Client
# from py.gui_manager import GUIManager

class Manager_OrderClient(Ui_DialogViewerRowClient):
    def __init__(self, gui_manager=None):
    # def __init__(self, gui_manager : GUIManager=None):
        super().__init__()
        self.gui_manager = gui_manager

    def setupUi(self, MainWindowViewerReports):
        Ui_DialogViewerRowClient.setupUi(self, MainWindowViewerReports)
        self.pushButton_cancel.clicked.connect(self.cancel)
    
    def setupUi_without_model(self):
        try:
            self.pushButton_save.clicked.disconnect(self.update_client)
        except Exception:
            pass
        finally:
            self.pushButton_save.clicked.connect(self.create_client)

        self.lineEdit_address.setText('')
        self.lineEdit_full_name.setText('')
        self.lineEdit_phone.setText('')

        self.label_4.setText(f'{self.label_4.text().split()[0]}')
    
    def setupUi_by_model(self, client: Client):
        self.setupUi_without_model()  
        self.pushButton_save.clicked.disconnect(self.create_client)
        self.pushButton_save.clicked.connect(self.update_client)

        self.label_4.setText(f'{self.label_4.text().split()[0]} {client.c_code}')
        self.lineEdit_address.setText(client.c_address)
        self.lineEdit_full_name.setText(client.c_full_name)
        self.lineEdit_phone.setText(client.c_telephone)
    
    def show_window(self, parent, model = None):
        if model:
            self.setupUi_by_model(model)
        else:
            self.setupUi_without_model()

        self.gui_manager.show_dialog_and_block_main(
            dialog=self.gui_manager.form_client,
            main=parent
        )
        self.gui_manager.form_client.exec_()
        self.gui_manager.unlock_main_window(parent)

    def create_client(self, client_id = None):
        try:
            model = Client()
            if client_id:
                model.c_code = client_id
            model.c_address = self.lineEdit_address.text()
            model.c_full_name = self.lineEdit_full_name.text()
            model.c_telephone = self.lineEdit_phone.text()
            
            if client_id:
                res = self.gui_manager.db_manager.update_by_model(model)
            else:
                res = self.gui_manager.db_manager.create_by_model(model)
            if not res: 
                raise Exception

            QMessageBox.information(self.gui_manager.form_client, "Успех", "Строка успешно добавлена в базу данных", QMessageBox.Ok)
            self.gui_manager.form_client.accept()
        except Exception as e:
            print(e)
            QMessageBox.warning(self.gui_manager.form_client, "Ошибка", "Возникла ошибка при сохранении клиента в базу данных!")
    
    def update_client(self):
        code = int(self.label_4.text().split(" ")[1])
        self.create_client(code);

    def cancel(self):
        self.gui_manager.form_client.accept()