def open_document(file_path):
    with open(file_path, 'r') as file:
        if not file_path.endswith(".txt"):
            raise ValueError("Необходим формат файла .txt")
        line = file.readlines()
        file.close()
        if len(line) == 0:
            raise Exception("Документ не может быть пустым")
        return line

def parse_records(obj, lines) -> list:
    records = []
    try:
        for string in lines:
            ed_class = obj()
            ed_class.read(string)
            records.append(ed_class)
        return records
    except TypeError as error:
        print(f"Невозможно обработать файл: {error}")
        raise TypeError

def display_agenda(rec_list):
    try:
        if len(rec_list) == 0:
            raise Exception("Список записей пуст")
        for elem in rec_list:
            elem.print_teacherroom()
    except AttributeError as error:
        print(f"Ошибка ввода данных: {repr(error)}")
        raise AttributeError