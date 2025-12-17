from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # TODO: добавить нормальную валидацию формата даты и диапазона gpa
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d") # переводим str в формат даты
        except ValueError:
            raise ValueError("Неверный формат даты рождения")
        
        if date.today() < date.fromisoformat(self.birthdate):
            raise ValueError("Дата рождения не может быть больше чем текущая")

        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa должен быть от 0 до 5")
        
        if isinstance(self.gpa,int):
            raise ValueError("gpa должен иметь формат float")

    def age(self) -> int:
        birth = date.fromisoformat(self.birthdate)
        today = date.today()
        age= today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age-=1
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            fio=data['fio'],
            birthdate=data['birthdate'],
            group=data['group'],
            gpa=data['gpa']
        )

    def __str__(self):
        return f"ФИО студента:{self.fio}, группа студента:{self.group}, GPA: {self.gpa}"
    

if __name__ == '__main__':
     student = Student(
         fio = 'Александров Александр Александрович',
         birthdate = '2006-01-25',
         group = 'BIVT-25-2',
         gpa = 4.7
     )
     print(student.to_dict()) # вывод в виде словаря
     print()
     print(student.from_dict(student.to_dict())) # вывод в красивом виде из словаря
     print()
     print(student.age()) # вывод полных лет
     print()
     print(student) # вывод в красивом виде