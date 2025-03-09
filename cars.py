class Cars:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return f'{self.name} is {self.year} years old.'


# cars = ['Audi', 'Lexus', 'Renault', 'BMW', 'Mazda']
Cars = [
    Cars('Audi',25),
    Cars('Lexus',25),
    Cars('Renault',25),
    Cars('BMW',25),
    Cars('Mazda', 25)
]

for car in Cars:
    print(f'Car:{car}')