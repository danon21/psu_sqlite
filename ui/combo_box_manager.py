import datetime

class ComboBoxManager:
    def __init__(self):
        self.months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        current_year = datetime.datetime.now().year
        self.years = [str(current_year - i) for i in range(11)]

    def fill_month_combo(self, combo_box):
        combo_box.addItems(self.months)

    def fill_year_combo(self, combo_box):
        combo_box.addItems(self.years)

    def fill_employee_combo(self, combo_box, personnel_list):
        combo_box.clear()
        for personnel in personnel_list:
            combo_box.addItem(f'{personnel.p_full_name} ({personnel.p_code})')

    def get_selected_month(self, combo_box):
        return combo_box.currentText()

    def get_selected_year(self, combo_box):
        return combo_box.currentText()

    def get_selected_employee_code(self, combo_box):
        text = combo_box.currentText()
        return text[text.find("(")+1:text.find(")")]
