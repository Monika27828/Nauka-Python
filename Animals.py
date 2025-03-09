class Animals:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return 'Typ to:{} a imie to: {}'.format(self.name, self.type)

animals = [
    Animal('Dog', 'Reksio'),
    Animal('Dog','Gucio'),
    Animal('Cat', 'Mruczek'),
    Animal('Hamster', 'Poncjusz'),
    Animal('Horse', 'Secundo'),
    Animal('Giraffe', 'Tubka'),
    Animal('Lizard','Pucio'),
    Animal('Duck', 'Tosia')
]

# Remove animal with name 'Dog'
animals = [animal for animal in animals if animal.name != 'Dog']

for animal in animals:
    print(animal.type)

new_animals = [animal for animal in animal_obj if animal.type != "Dog"]
new_animals.append(Animals("Chicken"))

for animal in new_animals:
    print(animal)
