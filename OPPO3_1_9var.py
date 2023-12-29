import unittest
import Function

class TestCaseNom2(unittest.TestCase):
    def test_format(self):
        self.assertRaises(ValueError, Function.open_document, "file.doc")

    def test_empty(self):
        self.assertRaises(Exception, Function.open_document, "empty.txt")

    def test_None(self):
        none_file = None
        lines = ["2023.10.01 3-21 Malyalik.L.O.", "2023.10.02 4-56 Bananov.Q.T."]
        with self.assertRaises(TypeError):
            Function.parse_records(none_file, lines)

    def test_print_entire_schedule(self):
        none_spisok = [None, None]
        none_list = []
        self.assertRaises(AttributeError, Function.display_agenda, none_spisok)
        self.assertRaises(Exception, Function.display_agenda, none_list)

if __name__ == '__main__':
    unittest.main()
