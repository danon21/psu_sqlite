from PyQt5.QtWidgets import QMessageBox
from py.ui.ui_class.dim_elements import Ui_DialogViewerDimElements

# from py.gui_manager import GUIManager

class Manager_DimViewBrand(Ui_DialogViewerDimElements):
    def __init__(self, gui_manager=None):
    # def __init__(self, gui_manager : GUIManager=None):
        super().__init__()
        self.gui_manager = gui_manager

    def setupUi(self, DialogStartAppDbChange):
        Ui_DialogViewerDimElements.setupUi(self, DialogStartAppDbChange)
        self.listWidget_dim_elevents.itemClicked.connect(self.edit_row)
        self.pushButton.clicked.connect(self.create_new_row)
        self.gui_manager.form_dim_brand.accepted.connect(self.fill_table)

    def fill_table(self):
        self.listWidget_dim_elevents.clearSelection()
        self.listWidget_dim_elevents.clear()
        self.gui_manager.list_manager.fill_list(
            self.listWidget_dim_elevents,
            self.gui_manager.db_manager.get_brand_dict()
        )
    
    def create_new_row(self):
        self.gui_manager.ui_form_dim_brand.show_window(self.gui_manager.view_dim_brand)

    def edit_row(self, item):
        brand_id = self.gui_manager.list_manager.get_item_code(item.text())
        brand = self.gui_manager.db_manager.get_brand_by_code(brand_id)
        self.gui_manager.ui_form_dim_brand.show_window(self.gui_manager.view_dim_brand, brand)