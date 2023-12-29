import unittest
from TeacherClass import TeacherRoom
from DateClass import Date

class TestCase(unittest.TestCase):
    def test_date(self):
        validator_1 = "2023/00/01"
        validator_2 = "00.00.123"
        object_0 = Date()
        with self.assertRaises(Exception):
            object_0.check_date(validator_1)
        with self.assertRaises(Exception):
            object_0.check_date(validator_2)

    def test_name(self):
        validator = "Тудакин.ИП"
        object_1 = TeacherRoom()
        with self.assertRaises(Exception):
            object_1.check_teacher(validator)

    def test_room(self):
        validator = "ABC"
        object_2 = TeacherRoom()
        with self.assertRaises(Exception):
            object_2.check_room(validator)

if __name__ == '__main__':
    unittest.main()