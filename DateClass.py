import re

class Date:
    year = None
    month = None
    day = None

    def check_date(self, date):
        date_pattern = r"\d{4}\.\d{2}\.\d{2}"
        match = re.match(date_pattern, date)
        if not match:
            raise Exception("Неверный формат даты (верный: гггг.мм.дд")
        date_elems = date.split(".")
        if (int(date_elems[1]) in [1, 3, 5, 7, 8, 10, 12] and int(date_elems[2]) > 31) and (int(date_elems[1]) in [4, 6, 9, 11] and int(date_elems[2]) > 30):
            raise Exception("Неверное количество дней в месяце")

    def read_date(self, date):
        self.check_date(date)
        date_elems = date.split(".")
        self.year = date_elems[0]
        self.month = date_elems[1]
        self.day = date_elems[2]