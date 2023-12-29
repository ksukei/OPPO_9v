import re
from DateClass import Date

class TeacherRoom:
    date = Date()
    room = None
    teacher = None

    def check_room(self, room):
        pattern = r"\d+-\d+"
        if not re.match(pattern, room):
            raise Exception("Неверный формат аудитории (верный: этаж-кабинет)")

    def check_teacher(self, teacher):
        pattern = r"[A-Za-z]+\.[A-Z]\.[A-Z]"
        if not re.match(pattern, teacher):
            raise Exception("Неверный формат имени преподавателя (верный: Фамилия.И.О. и на латинице)")

    def read(self, string):
        try:
            result = string.split()
            self.date.read_date(result[0])
            self.check_room(result[1])
            self.check_teacher(result[2])
            self.room = result[1]
            self.teacher = result[2]
        except IndexError as error:
            print("Ошибка прочтения файла")
            raise RuntimeError

    def print_teacherroom(self):
        print(".".join([str(self.date.year), str(self.date.month), str(self.date.day)]), self.room, self.teacher)

