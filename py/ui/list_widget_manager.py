from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QMessageBox

class ListManager:
    def fill_list(self, list_widget: QListWidget, dim_items: dict):
        list_widget.clearSelection()
        list_widget.clear()
        for key, value in dim_items.items():
            list_item = QListWidgetItem(f'{value} ({key})')
            list_widget.addItem(list_item)

    def remove_item_by_code(self, list_widget: QListWidget, code: int):
        for index in range(list_widget.count()):
            item = list_widget.item(index)
            text = item.text()
            el_code = int(text[text.find("(")+1:text.find(")")])
            if code == el_code:
                list_widget.takeItem(index)
    
    def get_item_code(self, item_text):
        try:
            el_code = int(item_text[item_text.find("(")+1:item_text.find(")")])
        except Exception:
            el_code = -1
        return el_code