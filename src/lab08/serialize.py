import json
from pathlib import Path
from models import Student

students_data = [
    Student('Иванов Иван Иванович', '2006-02-13', 'BIVT-24-3', 2.8),
    Student('Григорьев Григорий Григорьевич', '2007-08-22', 'BIVT-25-2', 4.5)
]

def students_to_json(students, path):
    p = Path(path)
    data = [s.to_dict() for s in students]# создает список словарей
    with open(str(p), 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)#создает json, ensure_ascii- поддержка кириллицы, indent форматирование

def students_from_json(path):
    p = Path(path)
    with open(str(p), 'r') as file:
        data = json.load(file)# открывает json
    print([Student.from_dict(item) for item in data]) # преобразует файл в обьект класса Student


if __name__ == '__main__':
    students_to_json(students_data, r'C:\Users\Соня\OneDrive\Рабочий стол\git\python_labs-1\src\data\lab_08\students_output.json')
    students_from_json(r'C:\Users\Соня\OneDrive\Рабочий стол\git\python_labs-1\src\data\lab_08\students_input.json')

