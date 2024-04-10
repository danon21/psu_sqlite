import datetime
import calendar

class ComboBoxManager:
    def __init__(self):
        self.months = ['---', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
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

    def get_timestamp(month, year):
        if month < 1 or month > 12:
            raise ValueError("Недопустимый порядковый номер месяца")
        
        date = datetime.datetime(year, month, 1)
        timestamp = int(date.timestamp())
        return timestamp

    def get_range_date(self, month, year, is_year_range):
        if month < 1:
           month = 1
        
        start_date = datetime.datetime(year, month, 1)

        if is_year_range:
            end_date = datetime.datetime(year, 12, 31)
        else:
            end_date = datetime.datetime(year, month, calendar.monthrange(year, month)[1])
        
        start_date = int(start_date.timestamp())
        end_date = int(end_date.timestamp())

        return start_date, end_date

    def get_selected_month(self, combo_box):
        return combo_box.currentText()

    def get_selected_year(self, combo_box):
        return combo_box.currentText()
    
    def get_selected_date(self, str_month, str_year):
        year = int(str_year)
        month = self.months.index(str_month)
        is_year_range = 0 == month
        return self.get_range_date(month, year, is_year_range)

    def get_selected_employee_code(self, combo_box):
        text = combo_box.currentText()
        return int(text[text.find("(")+1:text.find(")")])
