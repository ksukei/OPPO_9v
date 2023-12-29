from TeacherClass import TeacherRoom
import Function

if __name__ == '__main__':
    Function.display_agenda(
        Function.parse_records(TeacherRoom, Function.open_document('in.txt')))