class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old.'


students = [
    Student('Rafal',25),
    Student('Monika',25),
    Student('Patrycja',25),
    Student('Sergiusz',25)
]
# Remove student with name 'Rafal"
students = [student for student in students if student.name != 'Rafal']

for student in students:
    print(f'Student:{student}')