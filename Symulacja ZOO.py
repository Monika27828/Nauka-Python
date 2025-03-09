class Zwierze:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    def __str__(self):
            return f'{self.name} is {self.type} is {self.age}years old.'

# Zwierze = ['Lion', 'Giraffe', 'Tiger']
Zwierze = [
    Zwierze('Lion','Gucio',2),
    Zwierze('Giraffe', 'Zuzi', 1),
    Zwierze('Tiger', 'Poncjusz',4)
]

for zwierze in Zwierze:
    print(f'Zwierze:{zwierze}')